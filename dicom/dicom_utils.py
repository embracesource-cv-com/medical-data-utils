# -*- coding: utf-8 -*-
"""
   File Name：     dicom_utils
   Description :  dicom处理工具类
   Author :       mick.yi
   date：          2019/4/4
"""

import os
import cv2
import numpy as np
import dicom
from matplotlib import pyplot as plt


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


def dcm_show(dcm_file):
    """
    Dicom可视化
    :param dcm_file:
    :return:
    """
    dcm = dicom.read_file(dcm_file)
    dcm.image = dcm.pixel_array * dcm.RescaleSlope + dcm.RescaleIntercept
    slices = list()
    slices.append(dcm)
    img = slices[int(len(slices) / 2)].image.copy()
    ret, img = cv2.threshold(img, 90, 3071, cv2.THRESH_BINARY)
    img = np.uint8(img)

    im2, contours, _ = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    mask = np.zeros(img.shape, np.uint8)
    for contour in contours:
        cv2.fillPoly(mask, [contour], 255)
    img[(mask > 0)] = 255

    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2, 2))
    img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

    img2 = slices[int(len(slices) / 2)].image.copy()
    img2[(img == 0)] = -2000

    plt.figure(figsize=(12, 12))
    plt.subplot(131)
    plt.imshow(slices[int(len(slices) / 2)].image, 'gray')
    plt.title('Original')
    plt.subplot(132)
    plt.imshow(img, 'gray')
    plt.title('Mask')
    plt.subplot(133)
    plt.imshow(img2, 'gray')
    plt.title('Result')
    plt.show()
