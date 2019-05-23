# -*- coding: utf-8 -*-
"""
   File Name：     dicom_utils
   Description :  dicom处理工具类
   Author :       mick.yi
   date：          2019/4/4
"""

import os
import numpy as np
import pydicom as dicom
from matplotlib import pyplot as plt
from scipy import ndimage as ndi
from skimage.segmentation import clear_border
from skimage.measure import label, regionprops
from skimage.morphology import disk, dilation, binary_erosion, binary_closing
from skimage.filters import roberts, sobel


def decompress_file(src_file, dst_file):
    """
    解压dicom数据；需要安装gdcm
    wget -c -t 0 https://conda.anaconda.org/clinicalgraphics/linux-64/gdcm-2.8.4-py36hc0039aa_0.tar.bz2
    conda install --use-local gdcm-2.8.4-py36hc0039aa_0.tar.bz2
    :param src_file:
    :param dst_file:
    :return:
    """
    os.system("gdcmconv -w {} {}".format(src_file, dst_file))


def normalize_lung_hu(image):
    """
    灰度标准化（HU值），将HU值（[-1200, 600]）线性变换至0~255内的灰度值
    :param image: numpy数组
    :return: 值为0~255之间的numpy数组,与img有相同的shape,
    """
    # HU值首先归一化
    min_bound, max_bound = -1200, 600
    new_img = (image - min_bound) / (max_bound - min_bound)
    # 不在[-1200, 600]区间里的HU值，采取0/1处理
    new_img[new_img < 0] = 0
    new_img[new_img > 1] = 1
    # HU值线性映射至[0, 255]区间
    new_img = (new_img * 255).astype(np.uint8)
    return new_img


def get_segmented_lungs(image):
    """
    对输入的图像进行肺部区域分割，提取有效的肺部区域，用于模型训练
    :param image：输入的图像
    :return: 返回分割结果
    """
    im = image.copy()
    binary = im < -400  # Step 1: 转换为二值化图像
    cleared = clear_border(binary)  # Step 2: 清除图像边界的小块区域
    label_image = label(cleared)  # Step 3: 分割图像

    areas = [r.area for r in regionprops(label_image)]  # Step 4: 保留2个最大的连通区域
    areas.sort()
    if len(areas) > 2:
        for region in regionprops(label_image):
            if region.area < areas[-2]:
                for coordinates in region.coords:
                    label_image[coordinates[0], coordinates[1]] = 0
    binary = label_image > 0

    selem = disk(2)  # Step 5: 图像腐蚀操作,将结节与血管剥离
    binary = binary_erosion(binary, selem)
    selem = disk(10)  # Step 6: 图像闭环操作,保留贴近肺壁的结节
    binary = binary_closing(binary, selem)
    edges = roberts(binary)  # Step 7: 进一步将肺区残余小孔区域填充
    binary = ndi.binary_fill_holes(edges)
    get_high_vals = binary == 0  # Step 8: 将二值化图像叠加到输入图像上
    im[get_high_vals] = -2000
    print('lung segmentation complete.')
    return im, binary


def load_slice(dcm_file):
    """
    加载dicom切片
    :param dcm_file:
    :return: pydicom.dataset.FileDataset对象
    """
    dcm = dicom.read_file(dcm_file)
    dcm.image = dcm.pixel_array * dcm.RescaleSlope + dcm.RescaleIntercept
    return dcm


def main():
    base_dir = os.path.dirname(os.path.dirname(__file__))
    slice_file = os.path.join(base_dir, 'data', 'example_slice.dcm')
    dcm = load_slice(slice_file)
    im, binary = get_segmented_lungs(dcm.image)  # 肺部区域分割
    norm_im = normalize_lung_hu(im)
    fig = plt.figure(figsize=(20, 20))
    # 原始图像
    ax = fig.add_subplot(2, 2, 1)
    ax.imshow(dcm.image, 'gray')
    # 提取肺部区域
    ax = fig.add_subplot(2, 2, 2)
    ax.imshow(im, 'gray')
    ax = fig.add_subplot(2, 2, 3)
    ax.imshow(binary, 'gray')
    # 归一化后的图像
    ax = fig.add_subplot(2, 2, 4)
    ax.imshow(norm_im, 'gray')
    fig.savefig('{}/data/examples.png'.format(base_dir))


if __name__ == '__main__':
    main()
