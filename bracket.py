#!/usr/bin/python2

import os
import sys

sys.path.append('/usr/lib/freecad/lib')

import FreeCAD
import FreeCADGui as Gui

def makeU(sketch, width, height, thickness):
    sketch.addGeometry(Part.LineSegment(App.Vector(10,10,0),App.Vector(20,20,0)),False)
    sketch.addGeometry(Part.LineSegment(App.Vector(20,10,0),App.Vector(30,20,0)),False)

    sketch.addConstraint(Sketcher.Constraint('Coincident',0,1,-1,1))
    sketch.addConstraint(Sketcher.Constraint('Coincident',0, 2, 1, 1))

    sketch.addConstraint(Sketcher.Constraint('Horizontal', 0))
    sketch.addConstraint(Sketcher.Constraint('Vertical', 1))

    sketch.addConstraint(Sketcher.Constraint('DistanceX', 0, 1, 0, 2, App.Units.Quantity(width)))
    sketch.addConstraint(Sketcher.Constraint('DistanceY', 1, 1, 1, 2, App.Units.Quantity(height)))


filename = 'bracket.FCStd'

if os.path.isfile(filename):
    os.remove(filename)

# Gui.showMainWindow()

doc = FreeCAD.newDocument("Bracket")

# print FreeCAD.listDocuments()

# FreeCAD.open('/home/master/cad/3.FCStd')
# print FreeCAD.listDocumenAts()

doc.addObject('PartDesign::Body','BracketBody')
doc.recompute()
# doc.BracketBody.ViewObject.Visibility = True
# Gui.getDocument('Bracket').getObject('BracketBody').Visibility = True

doc.BracketBody.newObject('Sketcher::SketchObject','BracketSketch')
doc.BracketSketch.Support = (doc.XZ_Plane, [''])
doc.BracketSketch.MapMode = 'FlatFace'

# doc.BracketSketch.addGeometry(Part.LineSegment(App.Vector(10,0,0),App.Vector(20,0,0)),False)
# doc.BracketSketch.addGeometry(Part.LineSegment(App.Vector(20,0,0),App.Vector(30,0,0)),False)
# doc.BracketSketch.addGeometry(Part.LineSegment(App.Vector(10,10,0),App.Vector(20,20,0)),False)
# doc.BracketSketch.addGeometry(Part.LineSegment(App.Vector(20,10,0),App.Vector(30,20,0)),False)
# doc.recompute()

# doc.BracketSketch.addConstraint(Sketcher.Constraint('Coincident',0,1,-1,1))

# doc.BracketSketch.addConstraint(Sketcher.Constraint('Coincident',0, 2, 1, 1))

# doc.BracketSketch.addConstraint(Sketcher.Constraint('Horizontal', 0))
# doc.recompute()

# doc.BracketSketch.addConstraint(Sketcher.Constraint('Vertical', 1))

# doc.BracketSketch.addConstraint(Sketcher.Constraint('DistanceX', 0, 1, App.Units.Quantity('0 mm')))
# doc.BracketSketch.addConstraint(Sketcher.Constraint('DistanceY', 0, 1, App.Units.Quantity('0 mm')))

# doc.BracketSketch.addConstraint(Sketcher.Constraint('DistanceX', 0, 1, 0, 2, App.Units.Quantity('30 mm')))
# doc.BracketSketch.addConstraint(Sketcher.Constraint('DistanceY', 1, 1, 1, 2, App.Units.Quantity('15 mm')))

makeU(doc.BracketSketch, width='30 mm', height='15 mm', thickness='4 mm')

doc.recompute()

doc.saveAs(filename)