# encoding: utf-8

###########################################################################################################
#
#
#	Reporter Plugin
#
#	Read the docs:
#	https://github.com/schriftgestalt/GlyphsSDK/tree/master/Python%20Templates/Reporter
#
#
###########################################################################################################


from __future__ import division, print_function, unicode_literals
import objc
from GlyphsApp import *
from GlyphsApp.plugins import *

# import sys, os, re
import math

class ShowNodeCount(ReporterPlugin):

	@objc.python_method
	def settings(self):
		self.menuName = Glyphs.localize({
			'en': 'Node Count',
			})

	@objc.python_method
	def drawNodeCount( self, Layer ):
		FontMaster = Layer.associatedFontMaster()
		xHeight = FontMaster.xHeight
		angle = FontMaster.italicAngle

		# rotation point is half of x-height:
		offset = math.tan(math.radians(angle)) * xHeight/2

		nodeCount = 0
		for thisPath in Layer.paths:
			nodeCount += len(thisPath.nodes)

		self.drawTextAtPoint( "· %s" % nodeCount, NSPoint(-25-offset, 5) )

	@objc.python_method
	def background(self, layer):
		self.drawNodeCount( layer )
	
	# @objc.python_method
	# def inactiveLayer(self, layer):
	# 	NSColor.redColor().set()
	# 	if layer.paths:
	# 		layer.bezierPath.fill()
	# 	if layer.components:
	# 		for component in layer.components:
	# 			component.bezierPath.fill()

	# @objc.python_method
	# def preview(self, layer):
	# 	NSColor.blueColor().set()
	# 	if layer.paths:
	# 		layer.bezierPath.fill()
	# 	if layer.components:
	# 		for component in layer.components:
	# 			component.bezierPath.fill()
	
	@objc.python_method
	def __file__(self):
		"""Please leave this method unchanged"""
		return __file__


