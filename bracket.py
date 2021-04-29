#!/usr/bin/python2

import os
import sys

sys.path.append('/usr/lib/freecad/lib')

import FreeCAD
import FreeCADGui

filename = 'bracket.FCStd'

if os.path.isfile(filename):
    os.remove(filename)

# FreeCADGui.showMainWindow()

doc = FreeCAD.newDocument("Bracket")
doc.saveAs(filename)

# print FreeCAD.listDocuments()

# FreeCAD.open('/home/master/cad/3.FCStd')
# print FreeCAD.listDocumenAts()