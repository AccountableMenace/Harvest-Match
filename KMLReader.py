import fiona 
import zipfile 
import xml.etree.ElementTree as ET
from shapely.geometry import Polygon
import geopandas as gpd 
import os

extraction_dir_base = "./extract/"

class KMLReader:
	def __init__(self, path, name = "output"):
		self.path = path
		self.name = name
		self.extraction_dir = extraction_dir_base + name
		
		self.ExtractKMZ()
		self.ReadKML()




	def ExtractKMZ(self):
		
		# Open the KMZ file and extract its contents
		with zipfile.ZipFile(self.path, "r") as kmz:
			kmz.extractall(self.extraction_dir)

	def ReadKML(self):
		# prevents driver error
		fiona.drvsupport.supported_drivers['libkml'] = 'rw' 
		fiona.drvsupport.supported_drivers['LIBKML'] = 'rw'

		# Parse the KML file
		tree = ET.parse(os.path.join(extraction_dir_base, self.name, "doc.kml"))
		root = tree.getroot()

		# Define the KML namespace
		namespace = {'kml': 'http://www.opengis.net/kml/2.2'}

		# Extract LatLonBox from GroundOverlay
		latlon_box = root.find('.//kml:GroundOverlay/kml:LatLonBox', namespace)

		# Extract the bounding box coordinates
		self.north = float(latlon_box.find('kml:north', namespace).text)
		self.south = float(latlon_box.find('kml:south', namespace).text)
		self.east = float(latlon_box.find('kml:east', namespace).text)
		self.west = float(latlon_box.find('kml:west', namespace).text)

		# Create a polygon from the bounding box (clockwise)
		bbox_polygon = Polygon([
			(self.west, self.south),  # bottom-left
			(self.west, self.north),  # top-left
			(self.east, self.north),  # top-right
			(self.east, self.south)   # bottom-right
		])


		self.extent = [self.west, self.east, self.south, self.north]

		# Create a GeoDataFrame from the polygon
		# self.gdf = gpd.GeoDataFrame([{'geometry': bbox_polygon}], crs="EPSG:4326")
