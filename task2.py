# -*- coding: utf-8 -*-
"""task2.ipynb

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

import rasterio
from rasterio.enums import Resampling
import matplotlib.pyplot as plt

# Replace with the path to your multiband raster file
input_raster_file = "/content/data/LAKE_ALICE.tif"

# Open the input raster file
with rasterio.open(input_raster_file) as src:
    # Specify the bands you want to combine
    selected_bands = [1]  # Replace with the bands you need

    # Read the selected bands from the raster
    img = src.read(selected_bands)

    # Define the output raster file path
    output_raster_file = "/content/data/output"

    # Update the metadata for the new raster
    profile = src.profile
    profile.update(count=len(selected_bands), dtype=img.dtype)

    # Write the new raster with the selected bands
    with rasterio.open(output_raster_file, 'w', **profile) as dst:
        dst.write(img)

# Display the new raster
with rasterio.open(output_raster_file) as new_src:
    plt.imshow(new_src.read(1), cmap='viridis')  # Change cmap as needed
    plt.title(f'New Band Combination: {selected_bands}')
    plt.axis('off')
    plt.show()

pip install rasterio

import rasterio
import numpy as np
# Open the original dataset
src = rasterio.open("/content/data/LAKE_ALICE.tif")

meta = src.meta
del meta['count']

# Create a new dataset with 3 bands
with rasterio.open("/content/data/output", "w", **meta, count=3) as dst:
    # Create data arrays for each band
    band1_data = np.zeros((src.height, src.width))
    band2_data = np.ones((src.height, src.width))
    band3_data = np.full((src.height, src.width), 255)

    # Write the data for each band to the new dataset
    dst.write(band1_data, 1)
    dst.write(band2_data, 2)
    dst.write(band3_data, 3)

with rasterio.open("/content/data/output") as dst:
  data = dst.read(1)
  bounds = dst.bounds
  print(data)
  print(bounds)

import rasterio

# Open the original dataset
src = rasterio.open("/content/data/LAKE_ALICE.tif")

# Get the metadata for the original dataset
meta = src.meta

# Remove the 'count' parameter from the metadata
del meta['count']

# Set the 'count' parameter to an integer
meta['count'] = 3

# Create a new dataset with 3 bands
with rasterio.open("/content/data/output", "w", **meta) as dst:
    # Write the data for each band to the new dataset
    dst.write(band1_data, 1)
    dst.write(band2_data, 2)
    dst.write(band3_data, 3)

# Open the output file
with rasterio.open("/content/data/output", "r") as dst:
    # Read the data for the first band
    data = dst.read(1)

    # Get the spatial bounds of the dataset
    bounds = dst.bounds

    # Print the data and bounds
    print(data)
    print(bounds)

# Write the data and metadata to a new file
with rasterio.open("/content/data/output", "w", **meta) as out:
    out.write(data, 1)

pip install rasterio

import rasterio

# Open the raster dataset
with rasterio.open("/content/data/LAKE_ALICE.tif") as src:
    # Get the number of bands in the dataset
    num_bands = src.count

    # Prompt the user to select the bands they want to visualize
    print("Enter the band numbers you want to visualize (separated by spaces):")
    bands = list(map(int, input().split()))

    # Ensure that the number of bands the user selected is valid
    if len(bands) > num_bands:
        print(f"Invalid number of bands selected. The dataset has {num_bands} bands.")
        exit()

    # Read the data for the selected bands
    data = src.read(bands)

    # Print the data for the selected bands
    for i, band in enumerate(data):
        print(f"Band {bands[i]}:")
        print(band)

import numpy as np
from PIL import Image

# Create a random NumPy array
array = np.random.randint(0, 256, (300, 300, 3), dtype=np.uint8)

# Convert the NumPy array to an image
image = Image.fromarray(band)

# Display the image
image.show()

image.save('output_image.png')

