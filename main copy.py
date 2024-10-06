import zipfile 
import os 
import fiona 
import pandas as pd 
import geopandas as gpd 
from bs4 import BeautifulSoup 
import simplekml
import xml.etree.ElementTree as ET
from shapely.geometry import Polygon
from pykml import parser
from lxml import etree

### KMZ extraction

# Specify the path to our KMZ file
kmz_file_path = "./data1/2024-09-20-00_00_2024-09-20-23_59_Sentinel-2_L2A_NDVI.kmz"  

# Specify the directory where we want to extract the KML file (same directory as the KMZ file)
extraction_dir = "./extract"

# Open the KMZ file and extract its contents
with zipfile.ZipFile(kmz_file_path, "r") as kmz:
	kmz.extractall(extraction_dir)

# prevents driver error
fiona.drvsupport.supported_drivers['libkml'] = 'rw' 
fiona.drvsupport.supported_drivers['LIBKML'] = 'rw'


path_to_data = "./extract/"
transac_file = "doc"

# READING KML


# Parse the KML file
tree = ET.parse('./extract/doc.kml')
root = tree.getroot()

# Define the KML namespace
namespace = {'kml': 'http://www.opengis.net/kml/2.2'}

# Extract LatLonBox from GroundOverlay
latlon_box = root.find('.//kml:GroundOverlay/kml:LatLonBox', namespace)

# Extract the bounding box coordinates
north = float(latlon_box.find('kml:north', namespace).text)
south = float(latlon_box.find('kml:south', namespace).text)
east = float(latlon_box.find('kml:east', namespace).text)
west = float(latlon_box.find('kml:west', namespace).text)

# Create a polygon from the bounding box (clockwise)
bbox_polygon = Polygon([
    (west, south),  # bottom-left
    (west, north),  # top-left
    (east, north),  # top-right
    (east, south)   # bottom-right
])

# Create a GeoDataFrame from the polygon
gdf = gpd.GeoDataFrame([{'geometry': bbox_polygon}], crs="EPSG:4326")

# Display the GeoDataFrame
print(gdf)

# Optional: Save the GeoDataFrame to a file (e.g., GeoJSON or shapefile)
# gdf.to_file('output.geojson', driver='GeoJSON')

print(gdf.head())




