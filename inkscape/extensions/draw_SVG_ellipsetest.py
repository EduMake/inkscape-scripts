#!/usr/bin/env python 
import inkex
import simplestyle, sys, re
from math import *
import gettext
_ = gettext.gettext
try:
    from numpy import *
except:
    inkex.errormsg(_("Failed to import the numpy module. This module is required by this extension. Please install it and try again.  On a Debian-like system this can be done with the command 'sudo apt-get install python-numpy'."))
    sys.exit()

def draw_SVG_ellipse((rx, ry), (cx, cy), parent, start_end=(0,2*math.pi), is_open=False,transform='' ):
	style = {   'stroke'        : '#000000',
		'stroke-width'  : '1',
		'fill'          : 'none'            }
	ell_attribs = {'style':simplestyle.formatStyle(style),
		inkex.addNS('cx','sodipodi')        :str(cx),
		inkex.addNS('cy','sodipodi')        :str(cy),
		inkex.addNS('rx','sodipodi')        :str(rx),
		inkex.addNS('ry','sodipodi')        :str(ry),
		inkex.addNS('start','sodipodi')     :str(start_end[0]),
		inkex.addNS('end','sodipodi')       :str(start_end[1]),
		inkex.addNS('type','sodipodi')      :'arc',
		'transform'                         :transform
		}
	if is_open:
		inkex.errormsg("Open")
		ell_attribs[inkex.addNS('open','sodipodi')] = 'true'
	ell = inkex.etree.SubElement(parent, inkex.addNS('path','svg'), ell_attribs )



class EllipseTestPattern(inkex.Effect):
	def __init__(self):
		inkex.Effect.__init__(self)

	def effect(self):
		parent = self.current_layer
		inkex.errormsg("drawing")
		for i0 in range(6):
			for i1 in range(6):
				for i2 in range(6):
					if i1 != i2:
						draw_SVG_ellipse((40,10), (i2*90,i0*600+i1*25), parent, (i1*math.pi/3,i2*math.pi/3), True)

if __name__ == '__main__':
    e = EllipseTestPattern()
    e.affect()
    inkex.errormsg("DONE")


