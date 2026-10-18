from osgeo import gdal
import numpy as np

ds: gdal.Dataset = gdal.Open('Kerle11.tif')
# 蓝波段
blue = ds.GetRasterBand(1).ReadAsArray() * 0.0001
# 绿波段
green = ds.GetRasterBand(2).ReadAsArray() * 0.0001
# 红波段
red = ds.GetRasterBand(3).ReadAsArray() * 0.0001
# 近红外波段
nir = ds.GetRasterBand(4).ReadAsArray() * 0.0001

np.seterr(all="ignore")

ndvi = (nir - red) / (nir + red)
s1 = (blue) / (red)
s5 = (blue * red) / green
savi = (nir - red) / ((nir + red + 0.5) * (1 + 0.5))
# ----------------------------------------ndvi----------------------------------------
# NAN——>0
nan_index = np.isnan(ndvi)
ndvi[nan_index] = 0
ndvi = ndvi.astype(np.float32)
# 创建tif
tif_driver = gdal.GetDriverByName('GTiff')
out_ds = tif_driver.Create('ndvi.tif', ds.RasterXSize, ds.RasterYSize, 1, gdal.GDT_Float32)
# 设置投影坐标
out_ds.SetProjection(ds.GetProjection())
out_ds.SetGeoTransform(ds.GetGeoTransform())
# 写入数据
out_band = out_ds.GetRasterBand(1)
out_band.WriteArray(ndvi)

# ----------------------------------------S1----------------------------------------
# NAN——>0
nan_index = np.isnan(s1)
s1[nan_index] = 0
s1 = s1.astype(np.float32)
# 创建tif
tif_driver = gdal.GetDriverByName('GTiff')
out_ds = tif_driver.Create('s1.tif', ds.RasterXSize, ds.RasterYSize, 1, gdal.GDT_Float32)
# 设置投影坐标
out_ds.SetProjection(ds.GetProjection())
out_ds.SetGeoTransform(ds.GetGeoTransform())
# 写入数据
out_band = out_ds.GetRasterBand(1)
out_band.WriteArray(s1)
# ----------------------------------------S5----------------------------------------
# NAN——>0
nan_index = np.isnan(s5)
s5[nan_index] = 0
s5 = s5.astype(np.float32)
# 创建tif
tif_driver = gdal.GetDriverByName('GTiff')
out_ds = tif_driver.Create('s5.tif', ds.RasterXSize, ds.RasterYSize, 1, gdal.GDT_Float32)
# 设置投影坐标
out_ds.SetProjection(ds.GetProjection())
out_ds.SetGeoTransform(ds.GetGeoTransform())
# 写入数据
out_band = out_ds.GetRasterBand(1)
out_band.WriteArray(s5)
# ----------------------------------------savi----------------------------------------
# NAN——>0
nan_index = np.isnan(savi)
savi[nan_index] = 0
savi = savi.astype(np.float32)
# 创建tif
tif_driver = gdal.GetDriverByName('GTiff')
out_ds = tif_driver.Create('savi.tif', ds.RasterXSize, ds.RasterYSize, 1, gdal.GDT_Float32)
# 设置投影坐标
out_ds.SetProjection(ds.GetProjection())
out_ds.SetGeoTransform(ds.GetGeoTransform())
# 写入数据
out_band = out_ds.GetRasterBand(1)
out_band.WriteArray(savi)
