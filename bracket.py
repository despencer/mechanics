#!/usr/bin/python2

import os
import sys

sys.path.append('/usr/lib/freecad/lib')

import FreeCAD
import FreeCADGui as Gui

def units(val):
    return App.Units.Quantity("{0} mm".format(val))

def makelines(sketch, points):
    for i in range(0, len(points)):
        x1 = points[i][0]
        y1 = points[i][1]
        x2 = points[0][0] if i==len(points)-1 else points[i+1][0]
        y2 = points[0][1] if i==len(points)-1 else points[i+1][1]
        sketch.addGeometry(Part.LineSegment(App.Vector(x1,y1,0),App.Vector(x2,y2,0)),False)

def makeU(sketch, width, height, thickness):

    makelines(sketch, [ (0,0), (width,0), (width, height), (width-thickness,height), (width-thickness,thickness),
                               (thickness,thickness), (thickness,height), (0,height) ] )

    for i, val in enumerate(['H','V','H','V','H','V','H','V']):
        sketch.addConstraint(Sketcher.Constraint('Horizontal' if val=='H' else 'Vertical', i))

    # made start at (0,0)
    sketch.addConstraint(Sketcher.Constraint('Coincident',0,1,-1,1))
    for i in range(1, 8):
        sketch.addConstraint(Sketcher.Constraint('Coincident',i-1, 2, i, 1))
    sketch.addConstraint(Sketcher.Constraint('Coincident',0, 1, 7, 2))

    sketch.addConstraint(Sketcher.Constraint('DistanceX', 0, 1, 0, 2, units(width)))
    sketch.addConstraint(Sketcher.Constraint('DistanceY', 1, 1, 1, 2, units(height)))
    sketch.addConstraint(Sketcher.Constraint('DistanceY', 7, 2, 7, 1, units(height)))
    sketch.addConstraint(Sketcher.Constraint('DistanceY', 0, 1, 3, 2, units(thickness)))
    sketch.addConstraint(Sketcher.Constraint('DistanceX', 2, 1, 2, 2, units(-thickness)))
    sketch.addConstraint(Sketcher.Constraint('DistanceX', 6, 1, 6, 2, units(-thickness)))

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

makeU(doc.BracketSketch, width=30, height=15, thickness=4)

doc.recompute()

doc.saveAs(filename)