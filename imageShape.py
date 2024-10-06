#class for storing data about a single image and its coordinates.

import cv2
import numpy as np

import random



class imageShape:
	#           extentList: bottom, top, left, right
	def __init__(self, path, extent = [], flag = True):
		if flag:
			self.path = path
			self.image = cv2.imread(self.path)
		#skip reading from path and load image directly
		else:
			image = path #path variable is actually image
			self.image = image

		#rand = random.random() * 0.3

		self.extent = extent
		self.left = extent[0] #+ rand
		self.right = extent[1] #+ rand
		self.bottom = extent[2] #+ rand
		self.top = extent[3] #+ rand

		self.extent = [self.left, self.right, self.bottom, self.top]


		

	def shape(self):
		return self.image.shape 

	def widthDeg(self):
		return self.right - self.left
	
	def heightDeg(self):
		return self.top - self.bottom

	def getResolution(self):
		pxVert, pxHoriz, channels = self.image.shape
		#calculates vertical resolution only
		degreesHoriz = self.right - self.left
		degreesVert = self.top - self.bottom
		imgResVert = pxVert / degreesVert
		imgResHoriz = pxHoriz / degreesHoriz

		return (imgResHoriz, imgResVert)


	def MergeIntoBlank(self, blank, blankBounds, blankRes):
		
		pxVert, pxHoriz, channels = self.image.shape

		offsetH = int((self.left - blankBounds[2]) * blankRes[0])
		offsetV = int((blankBounds[1] - self.top) * blankRes[1])


		blank[offsetV : offsetV + pxVert, offsetH : offsetH + pxHoriz, :] = self.image

		self.extent = [blankBounds[2], blankBounds[3], blankBounds[0], blankBounds[1]]

		return blank


