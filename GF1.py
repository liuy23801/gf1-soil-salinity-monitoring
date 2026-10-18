import numpy as np
import cv2

import numpy as np
import rasterio
from rasterio.plot import show
from rasterio.warp import reproject, Resampling

# 高分一号遥感影像文件路径
tif_path = 'Kerle11.tif'

# 读取影像数据
with rasterio.open(tif_path) as src:
    data = src.read()
    profile = src.profile

# 打印结果
print(f"影像辐射校正完成，结果已输出到本文件夹下")


def radiometric_calibration(image, gain, offset):
    calibrated_image = image * gain + offset
    return calibrated_image

def atmospheric_correction(image, atmospheric_transmission):
    corrected_image = image / atmospheric_transmission
    return corrected_image

# 读取GF-1影像
image = cv2.imread('Kerle11.tif', cv2.IMREAD_GRAYSCALE)

# 辐射定标
gain = 0.2044
offset = 0.0226
calibrated_image = radiometric_calibration(image, gain, offset)

# 大气校正
atmospheric_transmission = 0.8
corrected_image = atmospheric_correction(calibrated_image, atmospheric_transmission)

# 保存校正后的影像
cv2.imwrite('corrected_image.tif', corrected_image)


