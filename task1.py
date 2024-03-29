# -*- coding: utf-8 -*-
"""task1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15DZU-frGRS2aWqdYT7a73w8N9xblZMlH
"""

import rasterio

pip install rasterio

import rasterio

from rasterio.plot import show

ds = r'/content/data/LAKE_ALICE.tif'

img = rasterio.open(ds)

show(img)

img.meta

img.profile

raster_meta = img.profile

raster_array = img.read(1)

raster_array

img.indexes

raster_array.shape

from rasterio.plot import show_hist

show_hist(img)

show_hist(img,bins=100)

import folium

from folium import plugins
from folium.plugins import marker_cluster

raster_file = "/content/data/LAKE_ALICE.tif"
map_c = [29.6431,82.3613]
mymap = folium.Map(location=map_c,zoom_start=13)
folium.raster_layers.ImageOverlay(
    image = raster_file,
    bounds=[[1,10],[29.6431,82.3613]],
    opacity=0.8,
    name='raster overlay',
).add_to(mymap)
folium.LayerControl().add_to(mymap)

mymap

