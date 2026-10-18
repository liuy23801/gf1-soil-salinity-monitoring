# import os
# import arcpy
# from arcpy.sa import *
#
#
# def rasterize_and_clip_orthomosaic(input_orthomosaic_path, input_grid_path, output_path):
#     """
#     根据栅格文件(例如：点、线或面数据)裁剪矢量遥感影像。
#     输入参数：
#     input_orthomosaic_path - 输入的遥感影像文件路径
#     input_grid_path - 输入的栅格数据文件路径
#     output_path - 裁剪后输出的影像路径
#     """
#     # 检查输入文件是否存在
#     if not os.path.exists(input_orthomosaic_path):
#         raise ValueError("输入的遥感影像文件不存在。")
#     if not os.path.exists(input_grid_path):
#         raise ValueError("输入的栅格数据文件不存在。")
#
#     # 检查输出路径是否已经是一个影像
#     if os.path.exists(output_path) and arcpy.Describe(output_path).datatype == "RasterDataset":
#         raise ValueError("输出路径已存在并且是一个影像文件。")
#
#     # 使用arcpy.Rasterize函数对栅格数据进行栅格化处理
#     rasterized_grid = arcpy.Rasterize(input_grid_path, "#", "#")
#
#     # 裁剪遥感影像
#     clipped_orthomosaic = Clip(input_orthomosaic_path, rasterized_grid, "#")
#
#     # 输出裁剪后的影像
#     clipped_orthomosaic.save(output_path)
#     print(f"裁剪完成，输出文件保存在：{output_path}")
#
#
# # 示例使用
# input_orthomosaic = "Kerle11.tif"
# input_grid = "库尔勒市.shp"  # 例如：点、线或面数据
# output_orthomosaic_clip = "output_orthomosaic_clip.tif"
#
# rasterize_and_clip_orthomosaic(input_orthomosaic, input_grid, output_orthomosaic_clip)
# # input_raster = 'Kerle11.tif'
# # # 输入的矢量文件（裁剪范围）
# # input_vector = '库尔勒市.shp'


# from osgeo import gdal
#
# data = gdal.Open("Kerle11.tif")
# rows = data.RasterYSize
# cols = data.RasterXSize
# bands = data.RasterCount
# print(f"rows:{rows}")
# print(f"cols:{cols}")
# print(f"bands:{bands}")
#
# #坐标转换参数
# geotrans = data.GetGeoTransform()
# print(geotrans)
# #空间参照系统信息
# proj = data.GetProjection()
# print(proj)
#
# #栅格数据转数组
# data_array = data.ReadAsArray()
# print(data_array.shape)
# band1 = data.GetRasterBand(1)  # 获取第一个波段的数据
# band1_array = band1.ReadAsArray()
# print(band1_array.shape)

# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
# from flask import Flask, send_file
# import geopandas as gpd
# import rasterio
# import tempfile
# from PIL import Image
# import io
#
# app = Flask(__name__)


# @app.route('/')
# def home():
#     return '''<html>
#         <head><title>Drone Imagery Viewer</title></head>
#         <body>
#             <img src="/image" width="1000">
#         </body>
#     </html>'''
#
#
# @app.route('/image')
# def get_image():
#     # 读取遥感影像
#     with rasterio.open('Kerle11.tif') as src:
#         image = src.read()
#         profile = src.profile
#
#     # 将影像转换为PNG并读取为二进制数据
#     with tempfile.NamedTemporaryFile(suffix='.png') as tf:
#         profile['width'] = 600  # 在前端显示时，可以调整大小
#         with rasterio.open(tf.name, 'w', **profile) as dst:
#             dst.write(image)
#         with open(tf.name, 'rb') as png:
#             png_bytes = png.read()
#
#     # 返回PNG图像作为响应
#     return send_file(png_bytes, mimetype='image/png')
#
#
# if __name__ == '__main__':
#     app.run(port=5000,host="127.0.0.1",debug=True)

# import os
# import geopandas as gpd
# import rasterio
# from rasterio.mask import mask
# from rasterio.crs import CRS
#
#
# def clip_raster_by_shp(raster_path, shp_path, output_folder):
#     # 读取shp文件
#     gdf = gpd.read_file(shp_path)
#
#     # 读取栅格数据
#     with rasterio.open(raster_path) as src:
#         # 获取栅格数据的元数据
#         src_meta = src.meta
#
#         if src.crs:
#             gdf_crs = CRS.from_user_input(gdf.crs) if gdf.crs else None
#             src_crs = CRS.from_user_input(src.crs) if src.crs else None
#
#             if gdf_crs != src_crs:
#                 gdf_projected = gdf.to_crs(src.crs)
#             else:
#                 gdf_projected = gdf
#         else:
#             gdf_projected = gdf
#
#         # 遍历shp文件中的每个区域
#         for index, row in gdf_projected.iterrows():
#             # 获取当前区域的几何形状
#             geometry_projected = row['geometry']
#
#             # 使用区域的几何形状裁剪栅格数据
#             out_image, out_transform = mask(src, [geometry_projected], crop=True)
#
#             # 更新元数据
#             out_meta = src_meta.copy()
#             out_meta.update({
#                 "driver": "GTiff",
#                 "height": out_image.shape[1],
#                 "width": out_image.shape[2],
#                 "transform": out_transform
#             })
#
#             # 保存裁剪后的栅格数据
#             out_filename = os.path.join(output_folder, f"clip_{index}.tif")
#             with rasterio.open(out_filename, "w", **out_meta) as dest:
#                 dest.write(out_image)
#
#         raster_path = r'Kerle11.tif'  # 设置需要裁剪的tif路径
#
#         shp_path = r'库尔勒市.shp'  # 设置shp路径
#
#         output_folder = r'cut_result'  # 设置结果保存路径
#
#         # 调用函数实现裁剪
#         clip_raster_by_shp(raster_path, shp_path, output_folder)







from rasterio.plot import show
from matplotlib.pyplot import savefig
from rasterio.plot import plotting_extent
from rasterio import open

# 打开.tif文件
with open('Kerle11.tif') as src:
    # 读取数据
    image = src.read()
    profile = src.profile

# 设置图像的显示范围，这里使用的是src.bounds，即.tif的边界框
extent = plotting_extent(src)

# 使用matplotlib显示.tif文件
show(image, extent=extent, transform=src.transform)

# 保存为.png格式
savefig('output.png', dpi=300, bbox_inches='tight', pad_inches=0.1)

