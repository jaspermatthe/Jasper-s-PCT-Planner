#!/usr/bin/env python3
import geopandas as gpd

# Specify the path to the JSON file
json_file_path = 'stelprdb5332131/PacificCrestTrail.shp'

# Read the JSON file into a GeoDataFrame
gdf = gpd.read_file(json_file_path)

# Now you can work with the GeoDataFrame 'gdf'
print(gdf)