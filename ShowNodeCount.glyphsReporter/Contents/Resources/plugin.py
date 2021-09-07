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

GlyphsReporterProtocol = objc.protocolNamed( "GlyphsReporter" )

class ShowNodeCount(ReporterPlugin):

	@objc.python_method
	def settings(self):
		self.menuName = Glyphs.localize({
			'en': 'Node Count',
			})

	@objc.python_method
	def drawNodeCount( self, Layer ):
		Glyph = Layer.parent
		Font = Glyph.parent
		selectedLayer = Font.selectedLayers[0]

		xHeight = Font.selectedFontMaster.xHeight
		angle = Font.selectedFontMaster.italicAngle
		# rotation point is half of x-height
		offset = math.tan(math.radians(angle)) * xHeight/2

		nodeCounter = 0
		for thisPath in selectedLayer.paths:
			nodeCounter += len(thisPath.nodes)

		self.drawTextAtPoint( u"· %s " % nodeCounter, (-offset, 1), fontColor=NSColor.colorWithCalibratedRed_green_blue_alpha_( 0.4, 0, .6, 1 ), align='bottomright' )

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

	@objc.python_method
	def getScale( self ):
		try:
			return self.controller.graphicView().scale()
		except:
			return 1.0

	@objc.python_method
	def setController_( self, Controller ):
		try:
			self.controller = Controller
		except Exception as e:
			pass

