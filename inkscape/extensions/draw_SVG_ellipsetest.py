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
		ell_attribs[inkex.addNS('open','sodipodi')] = 'true'
	ell = inkex.etree.SubElement(parent, inkex.addNS('path','svg'), ell_attribs )

def draw_SVG_square((w,h), (x,y), parent, transform='' ):

    style = {   'stroke'        : '#000000',
                'stroke-width'  : '1',
                'fill'          : 'none'
            }
                
    attribs = {
        'style'     : simplestyle.formatStyle(style),
        'height'    : str(h),
        'width'     : str(w),
        'x'         : str(x),
        'y'         : str(y),
	'transform'                         :transform
            }
    r = inkex.etree.SubElement(parent, inkex.addNS('rect','svg'), attribs )

def draw_SVG_text((w,h), (x, y), parent, text, transform='' ):
	rootstyle = { 'font-size':'10px', 'font-style':'normal', 'font-weight':'normal', 'line-height':'125%', 'letter-spacing':'0px',
		'word-spacing':'0px', 'fill':'#000000', 'fill-opacity':'1', 'stroke':'none', 'font-family':'Sans' }
	rootattribs = {'style':simplestyle.formatStyle(rootstyle)}
	flowroot = inkex.etree.SubElement(parent, inkex.addNS('flowRoot','svg'), rootattribs)
	flowregion = inkex.etree.SubElement(flowroot, inkex.addNS('flowRegion','svg'))
	rectattribs = {
		'height'    : str(h),
		'width'     : str(w),
		'x'         : str(x),
		'y'         : str(y),
		'transform' :transform
		}
	rect = inkex.etree.SubElement(flowregion, inkex.addNS('rect','svg'), rectattribs)
	flowpara = inkex.etree.SubElement(flowroot, inkex.addNS('flowPara','svg'))
	flowpara.text = text

class EllipseTestPattern(inkex.Effect):
	def __init__(self):
		inkex.Effect.__init__(self)

	def effect(self):
		parent = self.current_layer
		for i0 in range(6):
			for o in range(2):
				for i1 in range(13):
					for i2 in range(13):
						if (i1 != i2) and ((i1 != 12) or (i2 != 0)):
							draw_SVG_ellipse((40.0,10.0), (i2*90.0+675.0,i1*25.0 + o*350.0 - 350.0), parent, (i1*math.pi/6.0,i2*math.pi/6.0), o==1, 'rotate(%f)' % (i0*60.0))
#							draw_SVG_text((40*2,10*2), (i2*90-40+675,i1*25 + o*350 -10 - 350), parent, "%d %d %d %d" % (i0, o, i1, i2), 'rotate(%f)' % (i0*60))
#						else:
#							draw_SVG_square((40*2,10*2), (i2*90-40+675,i1*25 + o*350 -10 - 350), parent, 'rotate(%f)' % (i0*60))
		for i0 in range(6):
			for o in range(2):
				for i1 in range(13):
					for i2 in range(13):
						if (i1 != i2) and ((i1 != 12) or (i2 != 0)):
							draw_SVG_ellipse((10.0,40.0), (i2*25.0+675.0+675.0+675.0,i1*90.0 + o*1400.0 - 350.0), parent, (i1*math.pi/6.0,i2*math.pi/6.0), o==1, 'rotate(%f)' % (i0*60.0))
#							draw_SVG_text((10*2,40*2), (i2*25-10+675+675+675,i1*90 + o*1400 -40 - 350), parent, "%d %d %d %d" % (i0, o, i1, i2), 'rotate(%f)' % (i0*60))
#						else:
#							draw_SVG_square((10*2,40*2), (i2*25-10+675+675+675,i1*90 + o*1400 -40 - 350), parent, 'rotate(%f)' % (i0*60))

if __name__ == '__main__':
    e = EllipseTestPattern()
    e.affect()


