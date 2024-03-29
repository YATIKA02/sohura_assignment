# -*- coding: utf-8 -*-
"""task3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wEY5b8WBICObjJK2QGV8OF2R-LUqkKsY
"""

pip install geopandas

pip install fiona

pip install --upgrade fiona

import os
import fiona

# Set the SHAPE_RESTORE_SHX environment variable to True
os.environ['SHAPE_RESTORE_SHX'] = 'True'

# Open the shapefile
shapefile = fiona.open('/content/data/Coastline.shp')

import geopandas as gpd

# Load the shapefile
shapefile_path = '/content/data/Coastline.shp'
gdf = gpd.read_file(shapefile_path)

# Print the first few rows of the GeoDataFrame
print(gdf.head())

# Get the geometry type of the GeoDataFrame
geometry_type = gdf.geometry.type.iloc[0]
print(f'Geometry type: {geometry_type}')

# Get the bounding box of the GeoDataFrame
bbox = gdf.total_bounds
print(f'Bounding box: {bbox}')

# Get the centroid of each geometry in the GeoDataFrame
gdf['centroid'] = gdf.geometry.centroid

# Print the first few rows of the GeoDataFrame with the centroids
print(gdf.head())

pip install mplleaflet

import geopandas as gpd
import matplotlib.pyplot as plt

# Load the shapefile as a GeoDataFrame

gdf = gpd.read_file('/content/data/Coastline.shp')
print(gdf.columns)

# Get the attribute column name
attribute_column_name = 'attribute_column_name'

# Check if the attribute column exists in the GeoDataFrame
if 'attribute_column_name' in gdf.columns:
    # Get the attribute data from the GeoDataFrame
    attribute_data = gdf['attribute_column_name'].value_counts()

    # Create an interactive bar chart using matplotlib
    fig, ax = plt.subplots()
    ax.bar(attribute_data.index, attribute_data.values)
    ax.set_title('Attribute Data Distribution')
    ax.set_xlabel('Attribute Values')
    ax.set_ylabel('Count')

    # Enable interactive exploration of the bar chart
    plt.ion()
    fig.canvas.mpl_connect('button_press_event', click_event)
    plt.show(block=True)

else:
    print("Error: The attribute column 'attribute_column_name' does not exist in the GeoDataFrame.")

def click_event(event):
    if event.inaxes == ax:
        x = int(event.xdata)
        print(f"Attribute Value: {attribute_data.index[x]}, Count: {attribute_data.values[x]}")

import geopandas as gpd
import matplotlib.pyplot as plt

# Load your shapefile
shapefile_path = '/content/data/Coastline.shp'
gdf = gpd.read_file(shapefile_path)

# Plot the shapefile data
gdf.plot(cmap='viridis',legend=True)
plt.title('Plot of Shapefile Data')
plt.show()

