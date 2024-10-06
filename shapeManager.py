#manages a list of image shapes
 
import cv2
from imageShape import imageShape
import numpy as np
import math


class shapeManager:
	#imShList - list of imageShape
	def __init__(self, imShList = []):
		self.imShList = imShList

		self.bounds = self.CalculateTotalShape()



	#finds the minimum resolution which all images should be scaled to
	def FindBestResolution(self):
		bestResHoriz = 0 # px / deg
		bestResVert = 0 # px / deg
		for im in self.imShList:
			imgResHoriz, imgResVert = im.getResolution()

			print("Image resolution: " + str(imgResHoriz) + " x " + str(imgResVert) + " px/deg")

			if imgResVert > bestResVert:
				bestResVert = imgResVert
			if imgResHoriz > bestResHoriz:
				bestResHoriz = imgResHoriz

		return (bestResHoriz, bestResVert)


	# calculates bounds for combined images
	def CalculateTotalShape(self):
		# left, right, bottom, top, 
		bounds = [999999, -999999, 999999, -999999]
		for im in self.imShList:
			if im.bottom < bounds[0]:
				bounds[0] = im.bottom
			if im.top > bounds[1]:
				bounds[1] = im.top
			if im.left < bounds[2]:
				bounds[2] = im.left
			if im.right > bounds[3]:
				bounds[3] = im.right

		return bounds

	#resizes all images to the same resolution per geographic degree
	def SynchroniseResolution(self):
		bestResolution = self.FindBestResolution() #px/deg

		for i, imSh in enumerate(self.imShList):
			newWidth = imSh.widthDeg() * bestResolution[0]
			newHeight = imSh.heightDeg() * bestResolution[1]
			
			print(str(imSh.shape()))
			print(str(newWidth) + " test " + str(newHeight) + " best: " + str(bestResolution))

			imSh.image = cv2.resize(imSh.image, (int(newWidth), int(newHeight)))		
			self.imShList[i] = imSh


	def ShowAll(self, plt):
		for img in self.imShList:
			plt.imshow(img.image, extent = img.extent)


		
	def CreateBoundsBlank(self):
		bestRes = self.FindBestResolution()
		self.blankRes = bestRes
		heightDeg = self.bounds[1] - self.bounds[0] # top - bottom
		widthDeg =  self.bounds[3] - self.bounds[2] # right - left
		height = math.ceil(heightDeg * bestRes[1]) + 1
		width = math.ceil(widthDeg * bestRes[0]) + 1
		blank = np.zeros((int(height), int(width), 3), np.uint8)
		return blank


	def MergeImagesIntoBlanks(self):
		blank = self.CreateBoundsBlank()

		for i, img in enumerate(self.imShList):
			blankCopy = np.copy(blank)
			self.imShList[i].image = img.MergeIntoBlank(blankCopy, self.bounds, self.blankRes)

	





