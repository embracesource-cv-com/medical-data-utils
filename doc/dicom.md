
dicom样例
[dicom说明](https://blog.csdn.net/inter_peng/article/details/46513847)
```shell
(0008, 0005) Specific Character Set              CS: 'ISO_IR 100'
(0008, 0008) Image Type                          CS: ['ORIGINAL', 'PRIMARY', 'AXIAL', 'CT_SOM5 SPI']
(0008, 0016) SOP Class UID                       UI: CT Image Storage
(0008, 0018) SOP Instance UID                    UI: 1.3.12.2.1107.5.1.4.60414.30000018050400262047700106502
(0008, 0020) Study Date                          DA: '20180506'
(0008, 0021) Series Date                         DA: '20180506'
(0008, 0022) Acquisition Date                    DA: '20180506'
(0008, 0023) Content Date                        DA: '20180506'
(0008, 002a) Acquisition DateTime                DT: '20180506082755.557000'
(0008, 0030) Study Time                          TM: '082556.834000'
(0008, 0031) Series Time                         TM: '082811.368000'
(0008, 0032) Acquisition Time                    TM: '082755.557000'
(0008, 0033) Content Time                        TM: '082755.557000'
(0008, 0050) Accession Number                    SH: 'R05940162'
(0008, 0060) Modality                            CS: 'CT'
(0008, 0070) Manufacturer                        LO: 'SIEMENS'
(0008, 0080) Institution Name                    LO: 'ANONYMIZED'
(0008, 0081) Institution Address                 LO: 'ANONYMIZED'
(0008, 0090) Referring Physician's Name          PN: 'ANONYMIZED'
(0008, 1010) Station Name                        SH: 'CTAWP60414'
(0008, 1030) Study Description                   LO: 'Thorax^1_ThoraxRoutine (Adult)'
(0008, 103e) Series Description                  LO: 'Thorax  1.5  B31f'
(0008, 1040) Institutional Department Name       LO: 'DEFAULT'
(0008, 1090) Manufacturer's Model Name           LO: 'SOMATOM Definition'
(0008, 1110)  Referenced Study Sequence   1 item(s) ---- 
   (0008, 1150) Referenced SOP Class UID            UI: Detached Study Management SOP Class
   (0008, 1155) Referenced SOP Instance UID         UI: 1.2.124.113532.80.22178.14670.20180506.75602.417103997
   ---------
(0008, 1140)  Referenced Image Sequence   1 item(s) ---- 
   (0008, 1150) Referenced SOP Class UID            UI: CT Image Storage
   (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.1.4.60414.30000018050400252406800022747
   ---------
(0008, 2112)  Source Image Sequence   1 item(s) ---- 
   (0008, 1150) Referenced SOP Class UID            UI: 1.3.12.2.1107.5.9.1
   (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.1.4.60414.30000018050400252139000001010
   ---------
(0008, 3010) Irradiation Event UID               UI: 1.3.12.2.1107.5.1.4.60414.30000018050400252139000001010
(0009, 0010) Private Creator                     LO: 'SIEMENS CT VA1 DUMMY'
(0010, 0010) Patient's Name                      PN: 'ANONYMIZED'
(0010, 0020) Patient ID                          LO: 'ANONYMIZED'
(0010, 0021) Issuer of Patient ID                LO: 'UNKNOWN'
(0010, 0030) Patient's Birth Date                DA: 'ANONYMIZED'
(0010, 0040) Patient's Sex                       CS: 'M'
(0010, 1002) Other Patient IDs Sequence          LO: 'ANONYMIZED'
(0010, 1010) Patient's Age                       AS: '055Y'
(0018, 0015) Body Part Examined                  CS: 'CHEST'
(0018, 0050) Slice Thickness                     DS: '1.5'
(0018, 0060) KVP                                 DS: '120'
(0018, 0090) Data Collection Diameter            DS: '500'
(0018, 1000) Device Serial Number                LO: '60414'
(0018, 1020) Software Version(s)                 LO: 'syngo CT 2012B'
(0018, 1030) Protocol Name                       LO: '1_ThoraxRoutine'
(0018, 1100) Reconstruction Diameter             DS: '477'
(0018, 1110) Distance Source to Detector         DS: '1085.6'
(0018, 1111) Distance Source to Patient          DS: '595'
(0018, 1120) Gantry/Detector Tilt                DS: '0'
(0018, 1130) Table Height                        DS: '131'
(0018, 1140) Rotation Direction                  CS: 'CW'
(0018, 1150) Exposure Time                       IS: '500'
(0018, 1151) X-Ray Tube Current                  IS: '276'
(0018, 1152) Exposure                            IS: '115'
(0018, 1160) Filter Type                         SH: 'FLAT'
(0018, 1170) Generator Power                     IS: '34'
(0018, 1190) Focal Spot(s)                       DS: '1.2'
(0018, 1200) Date of Last Calibration            DA: '20180506'
(0018, 1201) Time of Last Calibration            TM: '080324.000000'
(0018, 1210) Convolution Kernel                  SH: 'B31f'
(0018, 5100) Patient Position                    CS: 'HFS'
(0018, 9306) Single Collimation Width            FD: 0.6
(0018, 9307) Total Collimation Width             FD: 19.2
(0018, 9309) Table Speed                         FD: 46.0
(0018, 9310) Table Feed per Rotation             FD: 23.0
(0018, 9311) Spiral Pitch Factor                 FD: 1.2
(0018, 9313) Data Collection Center (Patient)    FD: [0.4658203125, -130.5341796875, -231.5]
(0018, 9318) Reconstruction Target Center (Patie FD: [11.4658203125, -130.5341796875, -231.5]
(0018, 9323) Exposure Modulation Type            CS: 'XYZ_EC'
(0018, 9324) Estimated Dose Saving               FD: 56.6066
(0018, 9345) CTDIvol                             FD: 8.30617344
(0018, 9346)  CTDI Phantom Type Code Sequence   1 item(s) ---- 
   (0008, 0100) Code Value                          SH: '113691'
   (0008, 0102) Coding Scheme Designator            SH: 'DCM'
   (0008, 0104) Code Meaning                        LO: 'IEC Body Dosimetry Phantom'
   ---------
(0018, 9352) Calcium Scoring Mass Factor Device  FL: [0.7940000295639038, 0.8330000042915344, 0.871999979019165]
(0019, 0010) Private Creator                     LO: 'SIEMENS CT VA0  COAD'
(0019, 1090) [Osteo Offset]                      DS: '0'
(0019, 1092) [Osteo Regression Line Slope]       DS: '0.9179'
(0019, 1093) [Osteo Regression Line Intercept]   DS: '-0.21'
(0019, 1096) [Osteo Phantom Number]              IS: '0'
(0019, 10b0) [Feed per Rotation]                 DS: '23'
(0020, 000d) Study Instance UID                  UI: 1.2.124.113532.80.22178.14670.20180506.75602.417103997
(0020, 000e) Series Instance UID                 UI: 1.3.12.2.1107.5.1.4.60414.30000018050400262047700106311
(0020, 0010) Study ID                            SH: 'R05940162'
(0020, 0011) Series Number                       IS: '4'
(0020, 0012) Acquisition Number                  IS: '2'
(0020, 0013) Instance Number                     IS: '191'
(0020, 0032) Image Position (Patient)            DS: ['-227.0341796875', '-369.0341796875', '-231.5']
(0020, 0037) Image Orientation (Patient)         DS: ['1', '0', '0', '0', '1', '0']
(0020, 0052) Frame of Reference UID              UI: 1.3.12.2.1107.5.1.4.60414.30000018050400252139000001008
(0020, 1040) Position Reference Indicator        LO: ''
(0020, 1041) Slice Location                      DS: '-231.5'
(0020, 4000) Image Comments                      LT: ''
(0021, 0010) Private Creator                     LO: 'SIEMENS MED'
(0021, 1011) [Target]                            DS: ['11', '0']
(0028, 0002) Samples per Pixel                   US: 1
(0028, 0004) Photometric Interpretation          CS: 'MONOCHROME2'
(0028, 0010) Rows                                US: 512
(0028, 0011) Columns                             US: 512
(0028, 0030) Pixel Spacing                       DS: ['0.931640625', '0.931640625']
(0028, 0100) Bits Allocated                      US: 16
(0028, 0101) Bits Stored                         US: 12
(0028, 0102) High Bit                            US: 11
(0028, 0103) Pixel Representation                US: 0
(0028, 0106) Smallest Image Pixel Value          US: 0
(0028, 0107) Largest Image Pixel Value           US: 2281
(0028, 1050) Window Center                       DS: ['40', '-600']
(0028, 1051) Window Width                        DS: ['400', '1200']
(0028, 1052) Rescale Intercept                   DS: '-1024'
(0028, 1053) Rescale Slope                       DS: '1'
(0028, 1054) Rescale Type                        LO: 'HU'
(0028, 1055) Window Center & Width Explanation   LO: ['WINDOW1', 'WINDOW2']
(0029, 0010) Private Creator                     LO: 'SIEMENS CSA HEADER'
(0029, 0011) Private Creator                     LO: 'SIEMENS MEDCOM HEADER'
(0029, 0012) Private Creator                     LO: 'MITRA PRESENTATION 1.0'
(0029, 1008) [CSA Image Header Type]             CS: 'SOM 5'
(0029, 1009) [CSA Image Header Version]          LO: 'VA10A 971201'
(0029, 1010) [CSA Image Header Info]             OB: Array of 1302 bytes
(0029, 1140)  [Application Header Sequence]   2 item(s) ---- 
   (0029, 0010) Private Creator                     LO: 'SIEMENS MEDCOM HEADER'
   (0029, 1041) [Application Header Type]           CS: 'VIA_CARE_KV_WIND'
   (0029, 1042) [Application Header ID]             LO: 'ORIG WINDOW VALUES FROM CAREKV'
   (0029, 1043) [Application Header Version]        LO: 'V1 20120914'
   (0029, 1044) [Application Header Info]           OB: b'4\x000\x00#\x004\x000\x000\x00\x00\x00'
   ---------
   (0029, 0010) Private Creator                     LO: 'SIEMENS MEDCOM HEADER'
   (0029, 1041) [Application Header Type]           CS: 'SOM 5 TPOS'
   (0029, 1042) [Application Header ID]             LO: 'SOM 5 NULLPOSITION'
   (0029, 1043) [Application Header Version]        LO: 'VB10A 20030626'
   (0029, 1044) [Application Header Info]           OB: b'-000007250\x00\x00'
   ---------
(0029, 1210) Private tag data                    CS: '-2'
(0029, 1211) Private tag data                    CS: '-2'
(0029, 1212) Private tag data                    CS: '-2'
(0029, 1213) Private tag data                    CS: '-2'
(0031, 0010) Private Creator                     LO: 'AGFA PACS Archive Mirroring 1.0'
(0031, 1000) [Unknown]                           CS: 'N'
(0031, 1001) [Unknown]                           UL: 0
(0032, 000a) Study Status ID                     CS: 'COMPLETED'
(0032, 1060) Requested Procedure Description     LO: 'lung-1 CT_N-RTN'
(0032, 4000) Study Comments                      LT: ''
(0033, 0010) Private Creator                     LO: 'MITRA OBJECT UTF8 ATTRIBUTES 1.0'
(0033, 100e) [Unknown]                           LT: ''
(0040, 0244) Performed Procedure Step Start Date DA: '20180506'
(0040, 0245) Performed Procedure Step Start Time TM: '082556.834000'
(0040, 0275)  Request Attributes Sequence   1 item(s) ---- 
   (0008, 0050) Accession Number                    SH: ''
   (0020, 000d) Study Instance UID                  UI: ''
   (0032, 1060) Requested Procedure Description     LO: ''
   (0040, 0009) Scheduled Procedure Step ID         SH: 'R05940162'
   (0040, 1001) Requested Procedure ID              SH: 'R05940162'
   ---------
(7fe0, 0010) Pixel Data                          OW: Array of 524288 bytes
```