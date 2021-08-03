#!/usr/bin/env python

###
### This file is generated automatically by SALOME v9.6.0 with dump python functionality
###

import sys
import salome

salome.salome_init()
import salome_notebook
notebook = salome_notebook.NoteBook()
sys.path.insert(0, r'D:/Engineering/PhD/Prototypes_Database/2_CFD_DATABASE/CASE1_KVS/SALOME_CAD/VKS_para_mesh')

###
### SHAPER component
###

from SketchAPI import *

from salome.shaper import model

model.begin()
partSet = model.moduleDocument()

### Create Part
Part_1 = model.addPart(partSet)
Part_1_doc = Part_1.document()
model.addParameter(Part_1_doc, "D", "0.05")
model.addParameter(Part_1_doc, "L1", "D*5")
model.addParameter(Part_1_doc, "L2", "D*12")
model.addParameter(Part_1_doc, "H", "D*8")

### Create Sketch
Sketch_1 = model.addSketch(Part_1_doc, model.defaultPlane("XOY"))

### Create SketchProjection
SketchProjection_1 = Sketch_1.addProjection(model.selection("VERTEX", "PartSet/Origin"), False)
SketchPoint_1 = SketchProjection_1.createdFeature()

### Create SketchCircle
SketchCircle_1 = Sketch_1.addCircle(0, 0, 0.02500000000000002)
Sketch_1.setCoincident(SketchPoint_1.result(), SketchCircle_1.center())
Sketch_1.setRadius(SketchCircle_1.results()[1], "D/2")

### Create SketchProjection
SketchProjection_2 = Sketch_1.addProjection(model.selection("EDGE", "PartSet/OX"), False)
SketchLine_1 = SketchProjection_2.createdFeature()
SketchLine_1.setName("SketchLine_3")
SketchLine_1.result().setName("SketchLine_3")

### Create SketchLine
SketchLine_2 = Sketch_1.addLine(-0.25, 0, -0.25, 0.2)
SketchLine_2.setName("SketchLine_4")
SketchLine_2.result().setName("SketchLine_4")
Sketch_1.setVertical(SketchLine_2.result())

### Create SketchLine
SketchLine_3 = Sketch_1.addLine(-0.25, 0, -0.25, -0.2)
SketchLine_3.setName("SketchLine_5")
SketchLine_3.result().setName("SketchLine_5")
Sketch_1.setVertical(SketchLine_3.result())

### Create SketchLine
SketchLine_4 = Sketch_1.addLine(0.6000000000000001, 0, 0.6000000000000001, 0.2)
SketchLine_4.setName("SketchLine_6")
SketchLine_4.result().setName("SketchLine_6")
Sketch_1.setVertical(SketchLine_4.result())

### Create SketchLine
SketchLine_5 = Sketch_1.addLine(0.6000000000000001, 0, 0.6000000000000001, -0.2)
SketchLine_5.setName("SketchLine_7")
SketchLine_5.result().setName("SketchLine_7")
Sketch_1.setVertical(SketchLine_5.result())

### Create SketchLine
SketchLine_6 = Sketch_1.addLine(-0.25, 0.2, 0.6000000000000001, 0.2)
SketchLine_6.setName("SketchLine_8")
SketchLine_6.result().setName("SketchLine_8")
Sketch_1.setCoincident(SketchLine_2.endPoint(), SketchLine_6.startPoint())
Sketch_1.setCoincident(SketchLine_4.endPoint(), SketchLine_6.endPoint())
Sketch_1.setHorizontal(SketchLine_6.result())

### Create SketchLine
SketchLine_7 = Sketch_1.addLine(-0.25, -0.2, 0.6000000000000001, -0.2)
SketchLine_7.setName("SketchLine_9")
SketchLine_7.result().setName("SketchLine_9")
Sketch_1.setCoincident(SketchLine_3.endPoint(), SketchLine_7.startPoint())
Sketch_1.setCoincident(SketchLine_5.endPoint(), SketchLine_7.endPoint())
Sketch_1.setHorizontalDistance(SketchCircle_1.center(), SketchLine_2.endPoint(), "L1")
Sketch_1.setHorizontalDistance(SketchLine_3.endPoint(), SketchCircle_1.center(), "L1")
Sketch_1.setHorizontalDistance(SketchAPI_Point(SketchPoint_1).coordinates(), SketchLine_4.endPoint(), "L2")
Sketch_1.setHorizontalDistance(SketchAPI_Point(SketchPoint_1).coordinates(), SketchLine_7.endPoint(), "L2")
Sketch_1.setVerticalDistance(SketchLine_2.endPoint(), SketchCircle_1.center(), "H/2")
Sketch_1.setVerticalDistance(SketchCircle_1.center(), SketchLine_3.endPoint(), "H/2")
Sketch_1.setVerticalDistance(SketchAPI_Point(SketchPoint_1).coordinates(), SketchLine_7.endPoint(), "H/2")
model.do()

### Create Extrusion
Extrusion_1 = model.addExtrusion(Part_1_doc, [model.selection("FACE", "Sketch_1/Face-SketchLine_5f-SketchLine_9f-SketchLine_7r-SketchLine_6f-SketchLine_8r-SketchLine_4r-SketchCircle_1_2r")], model.selection(), 0.05, 0.05, "Faces|Wires")

### Create Export
Export_1 = model.exportToXAO(Part_1_doc, 'C:\\Users\\u0127798\\AppData\\Local\\Temp\\shaper_iktep62k.xao', model.selection("SOLID", "Extrusion_1_1"), 'XAO')

model.end()

###
### SHAPERSTUDY component
###

model.publishToShaperStudy()
import SHAPERSTUDY
Extrusion_1_1, = SHAPERSTUDY.shape(model.featureStringId(Extrusion_1))
###
### GEOM component
###

import GEOM
from salome.geom import geomBuilder
import math
import SALOMEDS


geompy = geomBuilder.New()

(imported, geo_kvs, [], [], []) = geompy.ImportXAO("C:/Users/u0127798/AppData/Local/Temp/shaper_iktep62k.xao")
inlet = geompy.CreateGroup(geo_kvs, geompy.ShapeType["FACE"])
geompy.UnionIDs(inlet, [41, 3])
outlet = geompy.CreateGroup(geo_kvs, geompy.ShapeType["FACE"])
geompy.UnionIDs(outlet, [27, 20])
bottom = geompy.CreateGroup(geo_kvs, geompy.ShapeType["FACE"])
geompy.UnionIDs(bottom, [55])
top = geompy.CreateGroup(geo_kvs, geompy.ShapeType["FACE"])
geompy.UnionIDs(top, [52])
wallSides = geompy.CreateGroup(geo_kvs, geompy.ShapeType["FACE"])
geompy.UnionIDs(wallSides, [34, 13])
wallCylinder = geompy.CreateGroup(geo_kvs, geompy.ShapeType["FACE"])
geompy.UnionIDs(wallCylinder, [45])
zEdges = geompy.CreateGroup(geo_kvs, geompy.ShapeType["EDGE"])
geompy.UnionIDs(zEdges, [36, 5, 8, 29, 22, 15, 47])
[inlet, outlet, bottom, top, wallSides, wallCylinder, zEdges] = geompy.GetExistingSubObjects(geo_kvs, False)
[inlet, outlet, bottom, top, wallSides, wallCylinder, zEdges] = geompy.GetExistingSubObjects(geo_kvs, False)
[inlet, outlet, bottom, top, wallSides, wallCylinder, zEdges] = geompy.GetExistingSubObjects(geo_kvs, False)
[inlet, outlet, bottom, top, wallSides, wallCylinder, zEdges] = geompy.GetExistingSubObjects(geo_kvs, False)
[inlet, outlet, bottom, top, wallSides, wallCylinder, zEdges] = geompy.GetExistingSubObjects(geo_kvs, False)
[inlet, outlet, bottom, top, wallSides, wallCylinder, zEdges] = geompy.GetExistingSubObjects(geo_kvs, False)
geompy.addToStudy( geo_kvs, 'geo_kvs' )
geompy.addToStudyInFather( geo_kvs, inlet, 'inlet' )
geompy.addToStudyInFather( geo_kvs, outlet, 'outlet' )
geompy.addToStudyInFather( geo_kvs, bottom, 'bottom' )
geompy.addToStudyInFather( geo_kvs, top, 'top' )
geompy.addToStudyInFather( geo_kvs, wallSides, 'wallSides' )
geompy.addToStudyInFather( geo_kvs, wallCylinder, 'wallCylinder' )
geompy.addToStudyInFather( geo_kvs, zEdges, 'zEdges' )

###
### SMESH component
###

import  SMESH, SALOMEDS
from salome.smesh import smeshBuilder

smesh = smeshBuilder.New()
#smesh.SetEnablePublish( False ) # Set to False to avoid publish in study if not needed or in some particular situations:
                                 # multiples meshes built in parallel, complex and numerous mesh edition (performance)

Mesh_30000 = smesh.Mesh(geo_kvs)
Prism_3D = Mesh_30000.Prism()
NETGEN_1D_2D = Mesh_30000.Triangle(algo=smeshBuilder.NETGEN_1D2D,geom=bottom)
NETGEN_2D_Parameters_1 = NETGEN_1D_2D.Parameters()
NETGEN_2D_Parameters_1.SetMaxSize( 0.005 )
NETGEN_2D_Parameters_1.SetMinSize( 0.001 )
NETGEN_2D_Parameters_1.SetSecondOrder( 0 )
NETGEN_2D_Parameters_1.SetOptimize( 1 )
NETGEN_2D_Parameters_1.SetFineness( 2 )
NETGEN_2D_Parameters_1.SetChordalError( -1 )
NETGEN_2D_Parameters_1.SetChordalErrorEnabled( 0 )
NETGEN_2D_Parameters_1.SetUseSurfaceCurvature( 1 )
NETGEN_2D_Parameters_1.SetFuseEdges( 1 )
NETGEN_2D_Parameters_1.SetUseDelauney( 0 )
NETGEN_2D_Parameters_1.SetQuadAllowed( 0 )
NETGEN_2D_Parameters_1.SetWorstElemMeasure( 0 )
NETGEN_2D_Parameters_1.SetCheckChartBoundary( 0 )
Viscous_Layers_2D_1 = NETGEN_1D_2D.ViscousLayers2D(0.001,5,1.1,[ 36, 29, 39, 40, 8, 15, 18, 19, 47, 50, 51 ],0)
Regular_1D = Mesh_30000.Segment(geom=zEdges)
Number_of_Segments_1 = Regular_1D.NumberOfSegments(1)
Viscous_Layers_2D_1.SetTotalThickness( 0.0025 )
Viscous_Layers_2D_1.SetNumberLayers( 5 )
Viscous_Layers_2D_1.SetStretchFactor( 1.1 )
Viscous_Layers_2D_1.SetEdges( [ 36, 29, 39, 40, 8, 15, 18, 19, 47, 50, 51 ], 0 )
isDone = Mesh_30000.Compute()
inlet_1 = Mesh_30000.GroupOnGeom(inlet,'inlet',SMESH.FACE)
outlet_1 = Mesh_30000.GroupOnGeom(outlet,'outlet',SMESH.FACE)
bottom_1 = Mesh_30000.GroupOnGeom(bottom,'bottom',SMESH.FACE)
top_1 = Mesh_30000.GroupOnGeom(top,'top',SMESH.FACE)
wallSides_1 = Mesh_30000.GroupOnGeom(wallSides,'wallSides',SMESH.FACE)
wallCylinder_1 = Mesh_30000.GroupOnGeom(wallCylinder,'wallCylinder',SMESH.FACE)
Prism_3D_5 = smesh.CreateHypothesis( "Prism_3D" )
[ inlet_1, outlet_1, bottom_1, top_1, wallSides_1, wallCylinder_1 ] = Mesh_30000.GetGroups()
#NETGEN_Parameters_2D_4.SetMaxSize( 0.01 ) ### not created Object
#NETGEN_Parameters_2D_4.SetMinSize( 0.005 ) ### not created Object
#NETGEN_Parameters_2D_4.SetSecondOrder( 0 ) ### not created Object
#NETGEN_Parameters_2D_4.SetOptimize( 1 ) ### not created Object
#NETGEN_Parameters_2D_4.SetFineness( 2 ) ### not created Object
#NETGEN_Parameters_2D_4.SetChordalError( 0 ) ### not created Object
#NETGEN_Parameters_2D_4.SetChordalErrorEnabled( 0 ) ### not created Object
#NETGEN_Parameters_2D_4.SetUseSurfaceCurvature( 1 ) ### not created Object
#NETGEN_Parameters_2D_4.SetFuseEdges( 1 ) ### not created Object
#NETGEN_Parameters_2D_4.SetWorstElemMeasure( 397 ) ### not created Object
#NETGEN_Parameters_2D_4.SetCheckChartBoundary( 224 ) ### not created Object
#NETGEN_Parameters_2D_4.SetQuadAllowed( 0 ) ### not created Object
#NETGEN_Parameters_2D_4.SetWorstElemMeasure( 0 ) ### not created Object
#NETGEN_Parameters_2D_4.SetCheckChartBoundary( 0 ) ### not created Object
#NETGEN_Parameters_2D_4.SetMaxSize( 0.005 ) ### not created Object
#NETGEN_Parameters_2D_4.SetMinSize( 0.001 ) ### not created Object
#NETGEN_Parameters_2D_4.SetWorstElemMeasure( 397 ) ### not created Object
#NETGEN_Parameters_2D_4.SetCheckChartBoundary( 64 ) ### not created Object
#NETGEN_Parameters_2D_4.SetWorstElemMeasure( 0 ) ### not created Object
#NETGEN_Parameters_2D_4.SetCheckChartBoundary( 0 ) ### not created Object
#NETGEN_Parameters_2D_4.SetMaxSize( 0.01 ) ### not created Object
#NETGEN_Parameters_2D_4.SetMinSize( 0.005 ) ### not created Object
#NETGEN_Parameters_2D_4.SetWorstElemMeasure( 397 ) ### not created Object
#NETGEN_Parameters_2D_4.SetCheckChartBoundary( 80 ) ### not created Object
#NETGEN_Parameters_2D_4.SetWorstElemMeasure( 0 ) ### not created Object
#NETGEN_Parameters_2D_4.SetCheckChartBoundary( 0 ) ### not created Object
#NETGEN_Parameters_2D_4.SetMaxSize( 0.005 ) ### not created Object
#NETGEN_Parameters_2D_4.SetWorstElemMeasure( 397 ) ### not created Object
#NETGEN_Parameters_2D_4.SetCheckChartBoundary( 240 ) ### not created Object
#NETGEN_Parameters_2D_4.SetWorstElemMeasure( 0 ) ### not created Object
#NETGEN_Parameters_2D_4.SetCheckChartBoundary( 0 ) ### not created Object
#NETGEN_Parameters_2D_4.SetMaxSize( 0.009 ) ### not created Object
#NETGEN_Parameters_2D_4.SetMinSize( 0.009 ) ### not created Object
#NETGEN_Parameters_2D_4.SetWorstElemMeasure( 397 ) ### not created Object
#NETGEN_Parameters_2D_4.SetCheckChartBoundary( 80 ) ### not created Object
#NETGEN_Parameters_2D_4.SetWorstElemMeasure( 0 ) ### not created Object
#NETGEN_Parameters_2D_4.SetCheckChartBoundary( 0 ) ### not created Object
Mesh_5000 = smesh.Mesh(geo_kvs)
Prism_3D_1 = Mesh_5000.Prism()
NETGEN_1D_2D_1 = Mesh_5000.Triangle(algo=smeshBuilder.NETGEN_1D2D,geom=bottom)
NETGEN_2D_Parameters_2 = NETGEN_1D_2D_1.Parameters()
NETGEN_2D_Parameters_2.SetSecondOrder( 0 )
NETGEN_2D_Parameters_2.SetOptimize( 1 )
NETGEN_2D_Parameters_2.SetFineness( 2 )
NETGEN_2D_Parameters_2.SetChordalError( -1 )
NETGEN_2D_Parameters_2.SetChordalErrorEnabled( 0 )
NETGEN_2D_Parameters_2.SetUseSurfaceCurvature( 1 )
NETGEN_2D_Parameters_2.SetFuseEdges( 1 )
NETGEN_2D_Parameters_2.SetUseDelauney( 0 )
NETGEN_2D_Parameters_2.SetQuadAllowed( 0 )
Viscous_Layers_2D_2 = NETGEN_1D_2D_1.ViscousLayers2D(0.0025,5,1.1,[ 36, 29, 39, 40, 8, 15, 18, 19, 47, 50, 51 ],0)
Regular_1D_1 = Mesh_5000.Segment(geom=zEdges)
Number_of_Segments_2 = Regular_1D_1.NumberOfSegments(1)
[ inlet_1, outlet_1, bottom_1, top_1, wallSides_1, wallCylinder_1 ] = Mesh_30000.GetGroups()
inlet_2 = Mesh_5000.GroupOnGeom(inlet,'inlet',SMESH.FACE)
outlet_2 = Mesh_5000.GroupOnGeom(outlet,'outlet',SMESH.FACE)
bottom_2 = Mesh_5000.GroupOnGeom(bottom,'bottom',SMESH.FACE)
top_2 = Mesh_5000.GroupOnGeom(top,'top',SMESH.FACE)
wallSides_2 = Mesh_5000.GroupOnGeom(wallSides,'wallSides',SMESH.FACE)
wallCylinder_2 = Mesh_5000.GroupOnGeom(wallCylinder,'wallCylinder',SMESH.FACE)
NETGEN_2D_Parameters_2.SetMinSize( 0.008 )
[ inlet_2, outlet_2, bottom_2, top_2, wallSides_2, wallCylinder_2 ] = Mesh_5000.GetGroups()
NETGEN_2D_Parameters_2.SetMaxSize( 0.012 )
NETGEN_2D_Parameters_2.SetWorstElemMeasure( 0 )
NETGEN_2D_Parameters_2.SetCheckChartBoundary( 0 )
isDone = Mesh_5000.Compute()
[ inlet_2, outlet_2, bottom_2, top_2, wallSides_2, wallCylinder_2 ] = Mesh_5000.GetGroups()
Mesh_16000 = smesh.Mesh(geo_kvs)
Prism_3D_2 = Mesh_16000.Prism()
NETGEN_1D_2D_2 = Mesh_16000.Triangle(algo=smeshBuilder.NETGEN_1D2D,geom=bottom)
NETGEN_2D_Parameters_3 = NETGEN_1D_2D_2.Parameters()
NETGEN_2D_Parameters_3.SetSecondOrder( 0 )
NETGEN_2D_Parameters_3.SetOptimize( 1 )
NETGEN_2D_Parameters_3.SetFineness( 2 )
NETGEN_2D_Parameters_3.SetChordalError( -1 )
NETGEN_2D_Parameters_3.SetChordalErrorEnabled( 0 )
NETGEN_2D_Parameters_3.SetUseSurfaceCurvature( 1 )
NETGEN_2D_Parameters_3.SetFuseEdges( 1 )
NETGEN_2D_Parameters_3.SetUseDelauney( 0 )
NETGEN_2D_Parameters_3.SetQuadAllowed( 0 )
Viscous_Layers_2D_3 = NETGEN_1D_2D_2.ViscousLayers2D(0.0025,5,1.1,[ 36, 29, 39, 40, 8, 15, 18, 19, 47, 50, 51 ],0)
Regular_1D_2 = Mesh_16000.Segment(geom=zEdges)
Number_of_Segments_3 = Regular_1D_2.NumberOfSegments(1)
NETGEN_2D_Parameters_3.SetMinSize( 0.005 )
NETGEN_2D_Parameters_3.SetCheckChartBoundary( 0 )
NETGEN_2D_Parameters_3.SetMaxSize( 0.007 )
NETGEN_2D_Parameters_3.SetWorstElemMeasure( 0 )
isDone = Mesh_16000.Compute()
inlet_3 = Mesh_16000.GroupOnGeom(inlet,'inlet',SMESH.FACE)
outlet_3 = Mesh_16000.GroupOnGeom(outlet,'outlet',SMESH.FACE)
bottom_3 = Mesh_16000.GroupOnGeom(bottom,'bottom',SMESH.FACE)
top_3 = Mesh_16000.GroupOnGeom(top,'top',SMESH.FACE)
wallSides_3 = Mesh_16000.GroupOnGeom(wallSides,'wallSides',SMESH.FACE)
wallCylinder_3 = Mesh_16000.GroupOnGeom(wallCylinder,'wallCylinder',SMESH.FACE)
try:
  Mesh_30000.ExportUNV( r'D:/Engineering/PhD/Prototypes_Database/2_CFD_DATABASE/CASE1_KVS/SALOME_CAD/VKS1_para_mesh/Mesh_30000.unv' )
  pass
except:
  print('ExportUNV() failed. Invalid file name?')
try:
  Mesh_5000.ExportUNV( r'D:/Engineering/PhD/Prototypes_Database/2_CFD_DATABASE/CASE1_KVS/SALOME_CAD/VKS1_para_mesh/Mesh_5000.unv' )
  pass
except:
  print('ExportUNV() failed. Invalid file name?')
try:
  Mesh_16000.ExportUNV( r'D:/Engineering/PhD/Prototypes_Database/2_CFD_DATABASE/CASE1_KVS/SALOME_CAD/VKS1_para_mesh/Mesh_16000.unv' )
  pass
except:
  print('ExportUNV() failed. Invalid file name?')
isDone = Mesh_30000.Compute()
[ inlet_1, outlet_1, bottom_1, top_1, wallSides_1, wallCylinder_1 ] = Mesh_30000.GetGroups()
Prism_3D_4 = smesh.CreateHypothesis( "Prism_3D" )
NETGEN_2D_Parameters_4 = smesh.CreateHypothesis('NETGEN_Parameters_2D', 'NETGENEngine')
NETGEN_2D_Parameters_4.SetMaxSize( 0.005 )
NETGEN_2D_Parameters_4.SetMinSize( 0.001 )
NETGEN_2D_Parameters_4.SetSecondOrder( 0 )
NETGEN_2D_Parameters_4.SetOptimize( 1 )
NETGEN_2D_Parameters_4.SetFineness( 2 )
NETGEN_2D_Parameters_4.SetChordalError( -1 )
NETGEN_2D_Parameters_4.SetChordalErrorEnabled( 0 )
NETGEN_2D_Parameters_4.SetUseSurfaceCurvature( 1 )
NETGEN_2D_Parameters_4.SetFuseEdges( 1 )
NETGEN_2D_Parameters_4.SetUseDelauney( 0 )
NETGEN_2D_Parameters_4.SetQuadAllowed( 0 )
NETGEN_2D_Parameters_4.SetWorstElemMeasure( 0 )
NETGEN_2D_Parameters_4.SetCheckChartBoundary( 0 )
Mesh_63000 = smesh.Mesh(geo_kvs)
Prism_3D_3 = Mesh_63000.Prism()
NETGEN_1D_2D_3 = Mesh_63000.Triangle(algo=smeshBuilder.NETGEN_1D2D,geom=bottom)
NETGEN_2D_Parameters_5 = NETGEN_1D_2D_3.Parameters()
NETGEN_2D_Parameters_5.SetMinSize( 0.001 )
NETGEN_2D_Parameters_5.SetSecondOrder( 0 )
NETGEN_2D_Parameters_5.SetOptimize( 1 )
NETGEN_2D_Parameters_5.SetFineness( 2 )
NETGEN_2D_Parameters_5.SetChordalError( -1 )
NETGEN_2D_Parameters_5.SetChordalErrorEnabled( 0 )
NETGEN_2D_Parameters_5.SetUseSurfaceCurvature( 1 )
NETGEN_2D_Parameters_5.SetFuseEdges( 1 )
NETGEN_2D_Parameters_5.SetUseDelauney( 0 )
NETGEN_2D_Parameters_5.SetQuadAllowed( 0 )
Viscous_Layers_2D_4 = NETGEN_1D_2D_3.ViscousLayers2D(0.0025,5,1.1,[ 36, 29, 39, 40, 8, 15, 18, 19, 47, 50, 51 ],0)
Regular_1D_3 = Mesh_63000.Segment(geom=zEdges)
Number_of_Segments_4 = Regular_1D_3.NumberOfSegments(1)
inlet_4 = Mesh_63000.GroupOnGeom(inlet,'inlet',SMESH.FACE)
outlet_4 = Mesh_63000.GroupOnGeom(outlet,'outlet',SMESH.FACE)
bottom_4 = Mesh_63000.GroupOnGeom(bottom,'bottom',SMESH.FACE)
top_4 = Mesh_63000.GroupOnGeom(top,'top',SMESH.FACE)
wallSides_4 = Mesh_63000.GroupOnGeom(wallSides,'wallSides',SMESH.FACE)
wallCylinder_4 = Mesh_63000.GroupOnGeom(wallCylinder,'wallCylinder',SMESH.FACE)
NETGEN_2D_Parameters_5.SetMaxSize( 0.0035 )
NETGEN_2D_Parameters_5.SetWorstElemMeasure( 0 )
NETGEN_2D_Parameters_5.SetCheckChartBoundary( 0 )
isDone = Mesh_63000.Compute()
[ inlet_4, outlet_4, bottom_4, top_4, wallSides_4, wallCylinder_4 ] = Mesh_63000.GetGroups()
try:
  Mesh_63000.ExportUNV( r'D:/Engineering/PhD/Prototypes_Database/2_CFD_DATABASE/CASE1_KVS/SALOME_CAD/VKS_para_mesh/Mesh_63000.unv' )
  pass
except:
  print('ExportUNV() failed. Invalid file name?')
Sub_mesh_1 = NETGEN_1D_2D.GetSubMesh()
Sub_mesh_2 = Regular_1D.GetSubMesh()
Sub_mesh_3 = NETGEN_1D_2D_1.GetSubMesh()
Sub_mesh_4 = Regular_1D_1.GetSubMesh()
Sub_mesh_5 = NETGEN_1D_2D_2.GetSubMesh()
Sub_mesh_6 = Regular_1D_2.GetSubMesh()
Sub_mesh_7 = NETGEN_1D_2D_3.GetSubMesh()
Sub_mesh_8 = Regular_1D_3.GetSubMesh()


## Set names of Mesh objects
smesh.SetName(Sub_mesh_7, 'Sub-mesh_7')
smesh.SetName(Mesh_63000.GetMesh(), 'Mesh_63000')
smesh.SetName(Sub_mesh_8, 'Sub-mesh_8')
smesh.SetName(wallCylinder_1, 'wallCylinder')
smesh.SetName(Mesh_16000.GetMesh(), 'Mesh_16000')
smesh.SetName(Sub_mesh_4, 'Sub-mesh_4')
smesh.SetName(Mesh_5000.GetMesh(), 'Mesh_5000')
smesh.SetName(top_1, 'top')
smesh.SetName(bottom_4, 'bottom')
smesh.SetName(wallSides_1, 'wallSides')
smesh.SetName(outlet_4, 'outlet')
smesh.SetName(wallCylinder_3, 'wallCylinder')
smesh.SetName(top_3, 'top')
smesh.SetName(wallSides_3, 'wallSides')
smesh.SetName(outlet_3, 'outlet')
smesh.SetName(bottom_3, 'bottom')
smesh.SetName(inlet_3, 'inlet')
smesh.SetName(Sub_mesh_6, 'Sub-mesh_6')
smesh.SetName(inlet_4, 'inlet')
smesh.SetName(wallSides_2, 'wallSides')
smesh.SetName(top_2, 'top')
smesh.SetName(bottom_1, 'bottom')
smesh.SetName(outlet_1, 'outlet')
smesh.SetName(wallCylinder_2, 'wallCylinder')
smesh.SetName(inlet_1, 'inlet')
smesh.SetName(NETGEN_2D_Parameters_2, 'NETGEN 2D Parameters_2')
smesh.SetName(NETGEN_2D_Parameters_1, 'NETGEN 2D Parameters_1')
smesh.SetName(Number_of_Segments_1, 'Number of Segments_1')
smesh.SetName(Viscous_Layers_2D_1, 'Viscous Layers 2D_1')
smesh.SetName(NETGEN_1D_2D.GetAlgorithm(), 'NETGEN 1D-2D')
smesh.SetName(Regular_1D.GetAlgorithm(), 'Regular_1D')
smesh.SetName(Prism_3D.GetAlgorithm(), 'Prism_3D')
smesh.SetName(Number_of_Segments_2, 'Number of Segments_2')
smesh.SetName(Viscous_Layers_2D_2, 'Viscous Layers 2D_2')
smesh.SetName(Mesh_30000.GetMesh(), 'Mesh_30000')
smesh.SetName(Sub_mesh_1, 'Sub-mesh_1')
smesh.SetName(NETGEN_2D_Parameters_5, 'NETGEN 2D Parameters_5')
smesh.SetName(Viscous_Layers_2D_4, 'Viscous Layers 2D_4')
smesh.SetName(Number_of_Segments_4, 'Number of Segments_4')
smesh.SetName(NETGEN_2D_Parameters_3, 'NETGEN 2D Parameters_3')
smesh.SetName(Viscous_Layers_2D_3, 'Viscous Layers 2D_3')
smesh.SetName(Number_of_Segments_3, 'Number of Segments_3')
smesh.SetName(outlet_2, 'outlet')
smesh.SetName(NETGEN_2D_Parameters_4, 'NETGEN 2D Parameters_4')
smesh.SetName(bottom_2, 'bottom')
smesh.SetName(Sub_mesh_3, 'Sub-mesh_3')
smesh.SetName(inlet_2, 'inlet')
smesh.SetName(Sub_mesh_5, 'Sub-mesh_5')
smesh.SetName(Sub_mesh_2, 'Sub-mesh_2')
smesh.SetName(top_4, 'top')
smesh.SetName(wallSides_4, 'wallSides')
smesh.SetName(wallCylinder_4, 'wallCylinder')


if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()
