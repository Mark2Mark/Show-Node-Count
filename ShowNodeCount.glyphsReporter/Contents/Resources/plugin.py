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
from math import tan, radians

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
		offset = tan(radians(angle)) * xHeight/2

		nodeCount = 0
		for thisPath in Layer.paths:
			nodeCount += len(thisPath.nodes)

		self.drawTextAtPoint( "· %s " % nodeCount, NSPoint(-offset, 1), align='bottomright' )

	@objc.python_method
	def background(self, layer):
		if self.getScale() >= 0.1:
			self.drawNodeCount( layer )
	
	@objc.python_method
	def __file__(self):
		"""Please leave this method unchanged"""
		return __file__


