import os 
import pandas as pd 
import geopandas as gpd 
from bs4 import BeautifulSoup 
import simplekml
from pykml import parser
from lxml import etree

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from matplotlib_scalebar.scalebar import ScaleBar

import cv2
import numpy as np
import math

from imageShape import imageShape
from KMLReader import KMLReader
from shapeManager import shapeManager


### KMZ extraction

# Specify KMZ files which will be averaged later
baseKMZs = [
	KMLReader("./data3/2024-09-30-00_00_2024-09-30-23_59_Sentinel-2_L2A_True_color.kmz", "TrueColor"),

]

additionalKMZs = [
	KMLReader("./data3/2024-09-30-00_00_2024-09-30-23_59_Sentinel-2_L2A_B08_(Raw).kmz", "B08"),
	KMLReader("./data3/2024-09-30-00_00_2024-09-30-23_59_Sentinel-2_L2A_B12_(Raw).kmz", "B12"),
]


# m = Basemap(projection='merc',
# 			llcrnrlat=KMZ1.south + -0.5,
# 			urcrnrlat=KMZ1.north + 0.5,
# 			llcrnrlon=KMZ1.west + -0.5,
# 			urcrnrlon=KMZ1.east + 0.5,
# 			# lat_ts=55,
# 			resolution='c',
# 			epsg=4326)
# # draw coastlines.
# # m.drawcoastlines()
# # draw a boundary around the map, fill the background.
# # this background will end up being the ocean color, since
# # the continents will be drawn on top.
# # m.drawmapboundary(fill_color='aqua') 
# # fill continents, set lake color same as ocean color. 
# # m.fillcontinents(color='coral',lake_color='aqua')
# m.bluemarble()

extractDir = "./extract/"
# plot image on background

fig, ax = plt.subplots(1)

imageShapes1 = list()
imageShapes2 = list()

for kmz in baseKMZs:
	imageShapes1.append(imageShape(os.path.join(extractDir, kmz.name, "image.jpg"), kmz.extent))

for kmz in additionalKMZs:
	imageShapes2.append(imageShape(os.path.join(extractDir, kmz.name, "image.jpg"), kmz.extent))



# shManager = shapeManager([imageSh1, imageSh2, imageSh3])
shManager1 = shapeManager(imageShapes1)
shManager1.SynchroniseResolution()
shManager1.MergeImagesIntoBlanks()

# shManager.ShowAll(plt)
# plt.imshow(shManager.imShList[0].image, extent = shManager.imShList[0].extent)


#averages image pixels
imgCount = len(shManager1.imShList)
avgImage = np.zeros_like(shManager1.imShList[0].image, dtype=np.float32)
weight = 1 / imgCount  

for i, imgSh in enumerate(shManager1.imShList):
	avgImage += imgSh.image * weight


#normalizing from 0 to 255
avgImage *= 255/avgImage.max() 
avgImage = avgImage.astype(int)

avgShape = imageShape(avgImage, shManager1.imShList[0].extent, False)

# finalData = imageShape([avgImage]) #cia cv2.image o ne imageshape, negerai
# shManager.ShowAll(plt)

#additional layers
imageShapes2.append(avgShape)
shManager2 = shapeManager(imageShapes2)

shManager2.SynchroniseResolution()
shManager2.MergeImagesIntoBlanks()




#averages image pixels
lst = shManager2.imShList



#apply custom formula
baseImage1 = lst[0].image * 0.5 - lst[1].image * 0.5
baseImage2 = lst[0].image * 0.5 + lst[1].image * 0.5
finalImage = np.divide(baseImage1, baseImage2)



#normalizing from 0 to 255
finalImage *= 255
finalImage = finalImage.astype(int)
finalShape = imageShape(finalImage, shManager2.imShList[0].extent, False)

# shManager2.ShowAll(plt)
plt.imshow(finalImage, extent = finalShape.extent, label = "test")
# plt.text(finalShape.left + 0.02, finalShape.top - 0.025, "Soil moisture", bbox={'facecolor': 'white', 'pad': 7})
plt.text(22.000, 55.555, "Kvėdarna", fontsize = 9, color = 'w', weight='bold')
plt.text(21.947, 55.544, "Pajūralis", fontsize = 9, color = 'w', weight='bold')
plt.text(21.820714, 55.527078, "Bumbuliškė", fontsize = 9, color = 'w', weight='bold')
plt.text(21.797028, 55.505812, "Stemplės", fontsize = 9, color = 'w', weight='bold')


plt.title("Soil moisture map")

#meters per degree
meterScale = 110000 * math.cos(math.pi/180 * finalShape.top) # horizontal meters per degree
print(finalShape.getResolution()[0])
scalebar = ScaleBar(meterScale)
plt.gca().add_artist(scalebar)

plt.show()


print("Slow")
print("Down")
print("Please")
print("Now")








