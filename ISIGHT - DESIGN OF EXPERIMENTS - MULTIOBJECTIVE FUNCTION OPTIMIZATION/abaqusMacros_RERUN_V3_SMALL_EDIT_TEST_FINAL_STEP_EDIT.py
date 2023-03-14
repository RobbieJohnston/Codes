# Automatic importation of solidworks geometry - assigning material parameters - boundary conditions - contact definitions - step definitions
# Script is read into Isight through OS command prompt - INP file is generated for simulation - ODB result
# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *
import __main__

import section
import regionToolset
import displayGroupMdbToolset as dgm
import part
import material
import assembly
import step
import interaction
import load
import mesh
import optimization
import job
import sketch
import visualization
import xyPlot
import displayGroupOdbToolset as dgo
import connectorBehavior
import os

# Setting work directory for consistent reading and output - Change G: to H: if running at home!!!

os.chdir(
        r"G:\FROM POSTDOC_ STENTING\OPTIMIZATION_SETUP\COLLATION OF COMPONENTS FOR OPTIMIZATION")

# Importation of balloon and coarctation geometry from previous INP file.

a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
mdb.ModelFromInputFile(name='EPLICIT_MODEL_COARCT_HIGHER_DISPLACEMENT', 
inputFileName='G:/FROM POSTDOC_ STENTING/OPTIMIZATION_SETUP/COLLATION OF COMPONENTS FOR OPTIMIZATION/EPLICIT_MODEL_COARCT_HIGHER_DISPLACEMENT.inp')
a = mdb.models['EPLICIT_MODEL_COARCT_HIGHER_DISPLACEME'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a = mdb.models['EPLICIT_MODEL_COARCT_HIGHER_DISPLACEME'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
step = mdb.openStep(
'G:\FROM POSTDOC_ STENTING\OPTIMIZATION_SETUP\COLLATION OF COMPONENTS FOR OPTIMIZATION\OUTPUT_GEOMETRY\OPTIMIZING_GEOMETRY.STEP', 
scaleFromFile=OFF)
mdb.models['Model-1'].PartFromGeometryFile(
name='ASSEMBLED_SKETCH_INNER_SURFACE', geometryFile=step, 
combine=False, dimensionality=THREE_D, type=DEFORMABLE_BODY)
p = mdb.models['Model-1'].parts['ASSEMBLED_SKETCH_INNER_SURFACE']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
meshTechnique=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
referenceRepresentation=OFF)
p = mdb.models['Model-1'].parts['ASSEMBLED_SKETCH_INNER_SURFACE']
p.seedPart(size=0.04, deviationFactor=0.1, minSizeFactor=0.1)
elemType1 = mesh.ElemType(elemCode=S4R, elemLibrary=EXPLICIT, 
secondOrderAccuracy=OFF, hourglassControl=DEFAULT)
elemType2 = mesh.ElemType(elemCode=S3R, elemLibrary=EXPLICIT)
p = mdb.models['Model-1'].parts['ASSEMBLED_SKETCH_INNER_SURFACE']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
pickedRegions =(faces, )
p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2))
p = mdb.models['Model-1'].parts['ASSEMBLED_SKETCH_INNER_SURFACE']
p.generateMesh()
p = mdb.models['Model-1'].parts['ASSEMBLED_SKETCH_INNER_SURFACE']
f = p.faces
pickedRegions = f.getSequenceFromMask(mask=('[#1 ]', ), )
p.deleteMesh(regions=pickedRegions)
p = mdb.models['Model-1'].parts['ASSEMBLED_SKETCH_INNER_SURFACE']
f = p.faces
pickedRegions = f.getSequenceFromMask(mask=('[#1 ]', ), )
p.setMeshControls(regions=pickedRegions, elemShape=QUAD)
p = mdb.models['Model-1'].parts['ASSEMBLED_SKETCH_INNER_SURFACE']
p.generateMesh()

# Assigning surface set to remove from model

p = mdb.models['Model-1'].parts['ASSEMBLED_SKETCH_INNER_SURFACE']
e = p.elements
Total_Elements_SurfaceSet = len(e)
print(Total_Elements_SurfaceSet)

#elems5 = e[0:Total_Elements_SurfaceSet]
#pickedRegions =(elems5, )
#p.Set(regions=pickedRegions, elemTypes=(elems5, ))



elements = e.getSequenceFromMask(mask=('[#ffffffff:1500 #7f  ]', ), )
p.Set(elements=elements, name='SurfaceMeshSet')

mdb.meshEditOptions.setValues(enableUndo=True, maxUndoCacheElements=0.5)
session.viewports['Viewport: 1'].view.setValues(nearPlane=12.2573, 
farPlane=21.4371, width=7.39994, height=3.55573, viewOffsetX=-0.244902, 
viewOffsetY=0.109167)
session.viewports['Viewport: 1'].view.setValues(nearPlane=12.5435, 
farPlane=21.478, width=7.57272, height=3.63875, cameraPosition=(
6.94959, 7.89851, 15.9074), cameraUpVector=(-0.413393, 0.759221, 
-0.502682), cameraTarget=(0.309304, 2.15851, 1.52727), 
viewOffsetX=-0.25062, viewOffsetY=0.111716)
p = mdb.models['Model-1'].parts['ASSEMBLED_SKETCH_INNER_SURFACE']
s = p.elements
side1Elements = s.getSequenceFromMask(mask=('[#ffffffff:1500 #7f ]', ), )
p.Surface(side1Elements=side1Elements, name='Extruding')
p = mdb.models['Model-1'].parts['ASSEMBLED_SKETCH_INNER_SURFACE']

Total_Elements_ExtrudingSet = len(s)
print(Total_Elements_ExtrudingSet)


#viewportElements = mdb.models['Model-1'].parts['ASSEMBLED_SKETCH_INNER_SURFACE'].elements
#Total_Elements_ExtrudingSet = len(viewportElements)
#print(Total_Elements_ExtrudingSet)

## GENERATE MESH BY OFFSET - AMEND AS THIS IS RELATED TO STRUT THICKNESS

#INCLUDE, STRUT_DEPTH=0.4
#print('STRUT DEPTH (mm) =', STRUT_DEPTH)
#Dynamic_Variable_Name = "strut_depth"

#vars()[strut_depth] = 0.4

#command to ask for abaqus import
#from abaqus import getInput
#from math import sqrt
#strut_depth = float(getInput('Enter a number:'))

# ------------------------------------------ THIS WORKS----------------------------------------------
#strut_depth = 0.4

## IMPORTANT NOTE THAT ABAQUS CANNOT CONVERT VALUES LESS THEN 1 TO FLOAT NUMBERS TO BE READ

# ---------------------------------------------------------------------------------------------------
#import os

#strut_depth = int(os.environ['strut_depth'])

os.chdir(
        r"C:\temp")

import sys, math
# Open the text file
file = open("user_params.txt", "r")
# Read the contents of the file
contents = file.read()
# Close the file
file.close()
# Split the contents of the file by line
lines = contents.split("\n")
# Get the value of the variable
strut_depth = float(lines[0])
# Print the value of the variable
print(strut_depth)
#string = "strut_depth"
strut_depth = float(strut_depth)
print(strut_depth)

#with open('user_params.txt', 'r') as file:
 #   num_var = int(file.read())

for item in range(int(strut_depth)):
   print(item)

os.chdir(
        r"G:\FROM POSTDOC_ STENTING\OPTIMIZATION_SETUP\COLLATION OF COMPONENTS FOR OPTIMIZATION")


p.generateMeshByOffset(region=p.surfaces['Extruding'], meshType=SOLID, totalThickness=strut_depth, 
numLayers=4, offsetDirection=INWARD, shareNodes=True)

#### THIS CODE OFFSET THE ELEMENTS INCORRENTLY - ELEMENTS MISSING #############
#p = mdb.models['Model-1'].parts['ASSEMBLED_SKETCH_INNER_SURFACE']
#e = p.elements
#elements = e.getSequenceFromMask(mask=('[#0:887 #ffffff80 #ffffffff:3548 #7 ]', 
#), )
#p.Set(elements=elements, name='OffsetElements-1')

session.linkedViewportCommands.setValues(_highlightLinkedViewports=False)
set1 = mdb.models['Model-1'].parts['ASSEMBLED_SKETCH_INNER_SURFACE'].sets['SurfaceMeshSet']
leaf = dgm.LeafFromSets(sets=(set1, ))
session.viewports['Viewport: 1'].partDisplay.displayGroup.remove(leaf=leaf)

p = mdb.models['Model-1'].parts['ASSEMBLED_SKETCH_INNER_SURFACE']
e = p.elements

Total_Elements_Offset_SurfaceAndSolid = len(e)
print(Total_Elements_Offset_SurfaceAndSolid)

elements = e.getSequenceFromMask(mask=('[#ffffffff:10000 #9f  ]', ), )
p.Set(elements=elements, name='OffsetElements-1')

# Define the element set
#elemSet = model.Elements(elementType='C3D8', range=(1, 10))

# Create the element set
#model.ElementSet(name='mySet', elements=elemSet)


#elements = e.getSequenceFromMask(mask=('[#0:1087 #ff800000 #ffffffff:10000 #7ffffff ]', ), )
#p.Set(elements=elements, name='OffsetElements-1')

#Write the angle in the output parameters file
paramsFile = open ('user_params_1.txt','w')
paramsFile.write('strut_depth'+'\t'+ str(strut_depth))
paramsFile.close()


## Removing of internal surface leaving extruded orphan mesh

p = mdb.models['Model-1'].parts['ASSEMBLED_SKETCH_INNER_SURFACE']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
e = p.edges
edges = e.getSequenceFromMask(mask=('[#ffffffff:12 ]', ), )
v = p.vertices
verts = v.getSequenceFromMask(mask=('[#ffffffff:12 ]', ), )
pickedEntities=regionToolset.Region(vertices=verts, edges=edges, faces=faces)
p.deleteMeshAssociationWithGeometry(geometricEntities=pickedEntities, 
addBoundingEntities=True)
session.linkedViewportCommands.setValues(_highlightLinkedViewports=False)
set1 = mdb.models['Model-1'].parts['ASSEMBLED_SKETCH_INNER_SURFACE'].sets['OffsetElements-1']
leaf = dgm.LeafFromSets(sets=(set1, ))
session.viewports['Viewport: 1'].partDisplay.displayGroup.remove(leaf=leaf)
p = mdb.models['Model-1'].parts['ASSEMBLED_SKETCH_INNER_SURFACE']
p = mdb.models['Model-1'].parts['ASSEMBLED_SKETCH_INNER_SURFACE']
p.deleteElement(elements=p.sets['SurfaceMeshSet'])
p = mdb.models['Model-1'].parts['ASSEMBLED_SKETCH_INNER_SURFACE']
p.features['STEP Geometry-1'].suppress()
session.linkedViewportCommands.setValues(_highlightLinkedViewports=False)
leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].partDisplay.displayGroup.replace(leaf=leaf)

##

## IMPORTATION OF COARCTATION GEOMETRY & BALLOON GEOMETRY

import part
import assembly
import material
import section
import interaction
mdb.models['Model-1'].Part('BALLOON', 
mdb.models['EPLICIT_MODEL_COARCT_HIGHER_DISPLACEME'].parts['BALLOON'])
mdb.models['Model-1'].Part('COARCT_IDEALIZED', 
mdb.models['EPLICIT_MODEL_COARCT_HIGHER_DISPLACEME'].parts['COARCT_IDEALIZED'])
mdb.models['Model-1'].Instance('PART-1-1', 
mdb.models['EPLICIT_MODEL_COARCT_HIGHER_DISPLACEME'].rootAssembly.instances['PART-1-1'])
mdb.models['Model-1'].Instance('BALLOON-1', 
mdb.models['EPLICIT_MODEL_COARCT_HIGHER_DISPLACEME'].rootAssembly.instances['BALLOON-1'])
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
meshTechnique=OFF)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
referenceRepresentation=ON)
p = mdb.models['Model-1'].parts['ASSEMBLED_SKETCH_INNER_SURFACE']
p.ReferencePoint(point=(0.216, 2.34, 1.27))
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
referenceRepresentation=OFF)

## ASSIGNING MATERIAL PARAMETERS FOR ALL MODELS - AORTA / DUCTAL TISSUE , BALLOON AND 3D PRINTED TITANIUM

mdb.models['Model-1'].Material(name='AORTA')
mdb.models['Model-1'].materials['AORTA'].Density(table=((1.1e-09, ), ))
mdb.models['Model-1'].materials['AORTA'].Hyperelastic(materialType=ISOTROPIC, 
testData=OFF, type=OGDEN, volumetricResponse=VOLUMETRIC_DATA, table=((
0.07275, 3.4071, 0.8), ))
mdb.models['Model-1'].Material(name='BALLOON')
mdb.models['Model-1'].materials['BALLOON'].Density(table=((1.5e-09, ), ))
mdb.models['Model-1'].materials['BALLOON'].Elastic(table=((920.0, 0.4), ))
mdb.models['Model-1'].Material(name='DUCTAL')
mdb.models['Model-1'].materials['DUCTAL'].Density(table=((5.5e-10, ), ))
mdb.models['Model-1'].materials['DUCTAL'].Hyperelastic(materialType=ISOTROPIC, 
testData=OFF, type=NEO_HOOKE, volumetricResponse=VOLUMETRIC_DATA, 
table=((0.051675, 0.0), ))
mdb.models['Model-1'].Material(name='TI64_PRINT')
mdb.models['Model-1'].materials['TI64_PRINT'].Density(table=((6.49e-09, ), ))
mdb.models['Model-1'].materials['TI64_PRINT'].Elastic(table=((65090.0, 0.342), 
))
mdb.models['Model-1'].materials['TI64_PRINT'].Plastic(table=((663.519, 
0.0), ))

## Need to amend to assign material parameters to newly created mesh 

############### ELEMENTS MISSING MATERIAL ASSIGNMENT WITH THIS CODE ############
#mdb.models['Model-1'].HomogeneousSolidSection(name='Section-1', 
#material='TI64_PRINT', thickness=None)
#p = mdb.models['Model-1'].parts['ASSEMBLED_SKETCH_INNER_SURFACE']
#e = p.elements
#elements = e.getSequenceFromMask(mask=('[#ffffffff:3459 #ff ]', ), )
#region = p.Set(elements=elements, name='Set-5')
#p = mdb.models['Model-1'].parts['ASSEMBLED_SKETCH_INNER_SURFACE']
#p.SectionAssignment(region=region, sectionName='Section-1', offset=0.0, 
#offsetType=MIDDLE_SURFACE, offsetField='', 
#thicknessAssignment=FROM_SECTION)

mdb.models['Model-1'].HomogeneousSolidSection(name='Section-1', 
material='TI64_PRINT', thickness=None)
p = mdb.models['Model-1'].parts['ASSEMBLED_SKETCH_INNER_SURFACE']
region = p.sets['OffsetElements-1']
p = mdb.models['Model-1'].parts['ASSEMBLED_SKETCH_INNER_SURFACE']
p.SectionAssignment(region=region, sectionName='Section-1', offset=0.0, 
offsetType=MIDDLE_SURFACE, offsetField='', 
thicknessAssignment=FROM_SECTION)

## Balloon created properties

p = mdb.models['Model-1'].parts['BALLOON']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
mdb.models['Model-1'].HomogeneousShellSection(name='Section-2', 
preIntegrate=OFF, material='BALLOON', thicknessType=UNIFORM, 
thickness=0.2, thicknessField='', nodalThicknessField='', 
idealization=NO_IDEALIZATION, poissonDefinition=DEFAULT, 
thicknessModulus=None, temperature=GRADIENT, useDensity=OFF, 
integrationRule=SIMPSON, numIntPts=5)
session.viewports['Viewport: 1'].view.setValues(nearPlane=84.3786, 
farPlane=126.601, width=64.5405, height=30.9346, viewOffsetX=7.92227, 
viewOffsetY=-0.415866)
p = mdb.models['Model-1'].parts['BALLOON']
e = p.elements
elements = e.getSequenceFromMask(mask=('[#ffffffff:180 ]', ), )
region = p.Set(elements=elements, name='Set-3')
p = mdb.models['Model-1'].parts['BALLOON']
p.SectionAssignment(region=region, sectionName='Section-2', offset=0.0, 
offsetType=MIDDLE_SURFACE, offsetField='', 
thicknessAssignment=FROM_SECTION)
del mdb.models['Model-1'].parts['BALLOON'].sectionAssignments[0]
p = mdb.models['Model-1'].parts['COARCT_IDEALIZED']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].enableMultipleColors()
session.viewports['Viewport: 1'].setColor(initialColor='#BDBDBD')
cmap=session.viewports['Viewport: 1'].colorMappings['Part']
session.viewports['Viewport: 1'].setColor(colorMapping=cmap)
session.viewports['Viewport: 1'].disableMultipleColors()
session.viewports['Viewport: 1'].enableMultipleColors()
session.viewports['Viewport: 1'].setColor(initialColor='#BDBDBD')
cmap=session.viewports['Viewport: 1'].colorMappings['Material']
session.viewports['Viewport: 1'].setColor(colorMapping=cmap)
session.viewports['Viewport: 1'].disableMultipleColors()
session.viewports['Viewport: 1'].enableMultipleColors()
session.viewports['Viewport: 1'].setColor(initialColor='#BDBDBD')
cmap=session.viewports['Viewport: 1'].colorMappings['Property']
session.viewports['Viewport: 1'].setColor(colorMapping=cmap)
session.viewports['Viewport: 1'].disableMultipleColors()
del mdb.models['Model-1'].parts['COARCT_IDEALIZED'].sectionAssignments[1]
del mdb.models['Model-1'].parts['COARCT_IDEALIZED'].sectionAssignments[0]
session.linkedViewportCommands.setValues(_highlightLinkedViewports=False)
p = mdb.models['Model-1'].parts['COARCT_IDEALIZED']
e = p.elements
elements = e.getSequenceFromMask(mask=('[#0:340 #ffffffff:68 ]', ), )
leaf = dgm.LeafFromMeshElementLabels(elementSeq=elements)
session.viewports['Viewport: 1'].partDisplay.displayGroup.remove(leaf=leaf)
p = mdb.models['Model-1'].parts['COARCT_IDEALIZED']
e = p.elements
elements = e.getSequenceFromMask(mask=('[#0:272 #ffffffff:68 ]', ), )
leaf = dgm.LeafFromMeshElementLabels(elementSeq=elements)
session.viewports['Viewport: 1'].partDisplay.displayGroup.remove(leaf=leaf)
mdb.models['Model-1'].HomogeneousSolidSection(name='Section-3', 
material='DUCTAL', thickness=None)
p = mdb.models['Model-1'].parts['COARCT_IDEALIZED']
e = p.elements
elements = e.getSequenceFromMask(mask=('[#ffffffff:272 ]', ), )
region = p.Set(elements=elements, name='Set-4')
p = mdb.models['Model-1'].parts['COARCT_IDEALIZED']
p.SectionAssignment(region=region, sectionName='Section-3', offset=0.0, 
offsetType=MIDDLE_SURFACE, offsetField='', 
thicknessAssignment=FROM_SECTION)
session.linkedViewportCommands.setValues(_highlightLinkedViewports=False)
leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].partDisplay.displayGroup.replace(leaf=leaf)
mdb.models['Model-1'].HomogeneousSolidSection(name='Section-4', 
material='AORTA', thickness=None)
session.linkedViewportCommands.setValues(_highlightLinkedViewports=False)
p = mdb.models['Model-1'].parts['COARCT_IDEALIZED']
e = p.elements
elements = e.getSequenceFromMask(mask=(
'[#ffffffff:17 #0:51 #88888888:68 #0:51 #ffffffff:17 #11111111:68 ]', 
), )
leaf = dgm.LeafFromMeshElementLabels(elementSeq=elements)
session.viewports['Viewport: 1'].partDisplay.displayGroup.remove(leaf=leaf)
p = mdb.models['Model-1'].parts['COARCT_IDEALIZED']
e = p.elements
elements = e.getSequenceFromMask(mask=(
'[#0:17 #ffffffff:17 #0:34 #44444444:68 #0:34 #ffffffff:17 #0:17', 
' #22222222:68 ]', ), )
leaf = dgm.LeafFromMeshElementLabels(elementSeq=elements)
session.viewports['Viewport: 1'].partDisplay.displayGroup.remove(leaf=leaf)
p = mdb.models['Model-1'].parts['COARCT_IDEALIZED']
e = p.elements
elements = e.getSequenceFromMask(mask=(
'[#0:34 #ffffffff:17 #0:17 #22222222:68 #0:17 #ffffffff:17 #0:34', 
' #44444444:68 ]', ), )
leaf = dgm.LeafFromMeshElementLabels(elementSeq=elements)
session.viewports['Viewport: 1'].partDisplay.displayGroup.remove(leaf=leaf)
p = mdb.models['Model-1'].parts['COARCT_IDEALIZED']
e = p.elements
elements = e.getSequenceFromMask(mask=(
'[#0:51 #ffffffff:17 #11111111:68 #ffffffff:17 #0:51 #88888888:68 ]', 
), )
leaf = dgm.LeafFromMeshElementLabels(elementSeq=elements)
session.viewports['Viewport: 1'].partDisplay.displayGroup.remove(leaf=leaf)
p = mdb.models['Model-1'].parts['COARCT_IDEALIZED']
e = p.elements
elements = e.getSequenceFromMask(mask=('[#0:272 #ffffffff:136 ]', ), )
region = p.Set(elements=elements, name='Set-5')
p = mdb.models['Model-1'].parts['COARCT_IDEALIZED']
p.SectionAssignment(region=region, sectionName='Section-4', offset=0.0, 
offsetType=MIDDLE_SURFACE, offsetField='', 
thicknessAssignment=FROM_SECTION)
a = mdb.models['Model-1'].rootAssembly
a.regenerate()
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].view.setValues(nearPlane=83.4765, 
farPlane=145.061, width=57.7105, height=27.6609, cameraPosition=(
39.1506, 14.7294, 110.86), cameraUpVector=(-0.213098, 0.883334, 
-0.417504))
session.viewports['Viewport: 1'].view.setValues(nearPlane=85.8944, 
farPlane=142.644, width=31.9841, height=15.3301, viewOffsetX=0.849219, 
viewOffsetY=1.51259)
session.viewports['Viewport: 1'].view.setValues(nearPlane=89.3795, 
farPlane=136.077, width=34.8221, height=16.6904, cameraPosition=(
88.9051, 52.3538, 54.799), cameraUpVector=(-0.617725, 0.67111, 
-0.409912), cameraTarget=(0.677886, -1.9581, 5.55233))
session.viewports['Viewport: 1'].view.setValues(nearPlane=84.6581, 
farPlane=142.945, width=32.9827, height=15.8087, cameraPosition=(
57.1775, 30.8029, 99.5334), cameraUpVector=(-0.395743, 0.803634, 
-0.444477), cameraTarget=(1.23639, -1.57873, 4.76486))
a = mdb.models['Model-1'].rootAssembly
a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-1'].parts['ASSEMBLED_SKETCH_INNER_SURFACE']
a.Instance(name='ASSEMBLED_SKETCH_INNER_SURFACE-1', part=p, dependent=ON)
p1 = a.instances['ASSEMBLED_SKETCH_INNER_SURFACE-1']
p1.translate(vector=(9.16501832008362, 0.0, 0.0))
session.viewports['Viewport: 1'].view.fitView()
session.viewports['Viewport: 1'].view.setValues(nearPlane=88.5479, 
farPlane=145.132, width=43.0734, height=20.6453, cameraPosition=(
4.93984, 4.22514, 121.271), cameraUpVector=(-0.242111, 0.893996, 
-0.377033), cameraTarget=(1.42796, -2.2727, 5.99202))
session.viewports['Viewport: 1'].view.setValues(nearPlane=86.2209, 
farPlane=146.22, width=41.9415, height=20.1027, cameraPosition=(
27.5771, 22.5719, 115.777), cameraUpVector=(-0.46791, 0.780164, 
-0.415217), cameraTarget=(1.68453, -2.06476, 5.92975))
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
engineeringFeatures=OFF)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
referenceRepresentation=ON)
p = mdb.models['Model-1'].parts['COARCT_IDEALIZED']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.linkedViewportCommands.setValues(_highlightLinkedViewports=False)
leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].partDisplay.displayGroup.replace(leaf=leaf)
p = mdb.models['Model-1'].parts['BALLOON']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['BALLOON']
p.ReferencePoint(point=(-1.23e-16, -3.83e-17, 24.0))
a = mdb.models['Model-1'].rootAssembly
a.regenerate()
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].view.setValues(nearPlane=86.9171, 
farPlane=145.524, width=33.0102, height=15.8219, viewOffsetX=0.122636, 
viewOffsetY=0.286646)
session.viewports['Viewport: 1'].view.setValues(nearPlane=89.3857, 
farPlane=144.127, width=33.9478, height=16.2713, cameraPosition=(
3.06025, 5.44762, 121.156), cameraUpVector=(-0.400663, 0.831956, 
-0.383821), cameraTarget=(1.53272, -2.17714, 5.90238), 
viewOffsetX=0.126119, viewOffsetY=0.294788)
session.viewports['Viewport: 1'].view.setValues(nearPlane=89.8433, 
farPlane=143.74, width=30.397, height=14.5694, viewOffsetX=0.0147523, 
viewOffsetY=0.459097)
session.viewports['Viewport: 1'].view.setValues(nearPlane=88.5169, 
farPlane=144.95, width=29.9482, height=14.3543, cameraPosition=(
38.0706, 34.9641, 109.2), cameraUpVector=(-0.489387, 0.738209, 
-0.464272), cameraTarget=(1.90908, -1.8467, 5.85069), 
viewOffsetX=0.0145345, viewOffsetY=0.45232)
session.viewports['Viewport: 1'].view.setValues(nearPlane=88.0307, 
farPlane=145.435, width=38.1476, height=18.2843, viewOffsetX=0.110973, 
viewOffsetY=0.570149)
a = mdb.models['Model-1'].rootAssembly
a.translate(instanceList=('ASSEMBLED_SKETCH_INNER_SURFACE-1', ), vector=(
-9.381048, -2.34976, 3.23))
session.viewports['Viewport: 1'].view.setValues(nearPlane=89.6731, 
farPlane=144.356, width=38.8593, height=18.6255, cameraPosition=(
66.346, 37.6197, 93.2852), cameraUpVector=(-0.587837, 0.734171, 
-0.339767), cameraTarget=(2.23906, -1.81638, 5.65603), 
viewOffsetX=0.113043, viewOffsetY=0.580786)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
adaptiveMeshConstraints=ON)
mdb.models['Model-1'].ExplicitDynamicsStep(name='Step-1', previous='Initial', 
massScaling=((SEMI_AUTOMATIC, MODEL, THROUGHOUT_STEP, 0.0, 10e-06, 
BELOW_MIN, 1000, 0, 0.0, 0.0, 0, None), ), improvedDtMethod=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')
regionDef=mdb.models['Model-1'].rootAssembly.allInstances['ASSEMBLED_SKETCH_INNER_SURFACE-1'].sets['OffsetElements-1']
mdb.models['Model-1'].FieldOutputRequest(name='F-Output-2', 
createStepName='Step-1', variables=('S', 'E', 'PEEQ', 'U'), 
region=regionDef, sectionPoints=DEFAULT, rebar=EXCLUDE)
mdb.models['Model-1'].historyOutputRequests['H-Output-1'].setValues(variables=(
'ALLIE', 'ALLKE'))
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
constraints=ON, connectors=ON, engineeringFeatures=ON, 
adaptiveMeshConstraints=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Initial')
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['PART-1-1'].elements
elements1 = e1.getSequenceFromMask(mask=(
'[#ffffffff:17 #0:51 #88888888:68 #0:51 #ffffffff:17 #11111111:68 ]', 
), )
a.Set(elements=elements1, name='LUMEN')
session.viewports['Viewport: 1'].view.setValues(nearPlane=90.6304, 
farPlane=143.399, width=25.4685, height=12.2072, viewOffsetX=-0.17036, 
viewOffsetY=1.60474)
session.viewports['Viewport: 1'].view.setValues(nearPlane=89.8217, 
farPlane=144.255, width=25.2412, height=12.0982, cameraPosition=(
56.4306, 24.7829, 104.033), cameraUpVector=(-0.543239, 0.782467, 
-0.304364), cameraTarget=(2.0911, -1.99211, 5.67608), 
viewOffsetX=-0.16884, viewOffsetY=1.59042)
session.viewports['Viewport: 1'].view.setValues(nearPlane=90.5493, 
farPlane=143.528, width=16.0914, height=7.71269, viewOffsetX=0.2676, 
viewOffsetY=1.62414)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['PART-1-1'].elements
face1Elements1 = f1.getSequenceFromMask(mask=('[#0:204 #11111111:68 ]', ), )
face2Elements1 = f1.getSequenceFromMask(mask=('[#0:68 #88888888:68 ]', ), )
face4Elements1 = f1.getSequenceFromMask(mask=('[#0:187 #ffffffff:17 ]', ), )
face6Elements1 = f1.getSequenceFromMask(mask=('[#ffffffff:17 ]', ), )
a.Surface(face1Elements=face1Elements1, face2Elements=face2Elements1, 
face4Elements=face4Elements1, face6Elements=face6Elements1, 
name='LUMEN')
session.viewports['Viewport: 1'].view.setValues(nearPlane=90.1316, 
farPlane=143.945, width=23.3127, height=11.1739, viewOffsetX=1.56724, 
viewOffsetY=0.839161)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['ASSEMBLED_SKETCH_INNER_SURFACE-1'].elements
face1Elements1 = f1.getSequenceFromMask(mask=('[#ffffffff:856 #1ffff ]', ), )
a.Surface(face1Elements=face1Elements1, name='STENT_INNER')
session.viewports['Viewport: 1'].view.setValues(nearPlane=91.1228, 
farPlane=142.954, width=9.91134, height=4.75055, viewOffsetX=0.0989168, 
viewOffsetY=0.522735)
session.viewports['Viewport: 1'].view.setValues(nearPlane=91.6291, 
farPlane=143.086, width=9.9664, height=4.77694, cameraPosition=(
45.6566, -5.99167, 112.48), cameraUpVector=(-0.550159, 0.828118, 
-0.107453), cameraTarget=(1.97389, -2.38294, 5.60401), 
viewOffsetX=0.0994663, viewOffsetY=0.525639)
session.viewports['Viewport: 1'].view.setValues(nearPlane=91.033, 
farPlane=143.681, width=17.8248, height=8.5435, viewOffsetX=0.768833, 
viewOffsetY=0.443161)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['ASSEMBLED_SKETCH_INNER_SURFACE-1'].elements
face2Elements1 = f1.getSequenceFromMask(mask=(
'[#0:2569 #fff80000 #ffffffff:856 #f ]', ), )
a.Surface(face2Elements=face2Elements1, name='STENT_OUTER')
session.viewports['Viewport: 1'].view.setValues(nearPlane=89.8076, 
farPlane=144.907, width=32.7818, height=15.7125, viewOffsetX=4.08555, 
viewOffsetY=0.584956)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['BALLOON-1'].elements
side2Elements1 = s1.getSequenceFromMask(mask=('[#ffffffff:180 ]', ), )
a.Surface(side2Elements=side2Elements1, name='BALLOON')
mdb.models['Model-1'].ContactProperty('CONTACT')
mdb.models['Model-1'].interactionProperties['CONTACT'].TangentialBehavior(
formulation=PENALTY, directionality=ISOTROPIC, slipRateDependency=OFF, 
pressureDependency=OFF, temperatureDependency=OFF, dependencies=0, 
table=((0.2, ), ), shearStressLimit=None, maximumElasticSlip=FRACTION, 
fraction=0.005, elasticSlipStiffness=None)
mdb.models['Model-1'].interactionProperties['CONTACT'].NormalBehavior(
pressureOverclosure=HARD, allowSeparation=ON, 
constraintEnforcementMethod=DEFAULT)
mdb.models['Model-1'].ContactExp(name='CONTACT', createStepName='Initial')
r11=mdb.models['Model-1'].rootAssembly.surfaces['BALLOON']
r12=mdb.models['Model-1'].rootAssembly.surfaces['STENT_INNER']
r21=mdb.models['Model-1'].rootAssembly.surfaces['STENT_OUTER']
r22=mdb.models['Model-1'].rootAssembly.surfaces['LUMEN']
mdb.models['Model-1'].interactions['CONTACT'].includedPairs.setValuesInStep(
stepName='Initial', useAllstar=OFF, addPairs=((r11, r12), (r21, r22)))
r21=mdb.models['Model-1'].rootAssembly.surfaces['BALLOON']
r22=mdb.models['Model-1'].rootAssembly.surfaces['STENT_INNER']
r31=mdb.models['Model-1'].rootAssembly.surfaces['STENT_OUTER']
r32=mdb.models['Model-1'].rootAssembly.surfaces['LUMEN']
mdb.models['Model-1'].interactions['CONTACT'].contactPropertyAssignments.appendInStep(
stepName='Initial', assignments=((GLOBAL, SELF, 'CONTACT'), (r21, r22, 
'CONTACT'), (r31, r32, 'CONTACT')))
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
predefinedFields=ON, interactions=OFF, constraints=OFF, 
engineeringFeatures=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=87.884, 
farPlane=146.83, width=56.2149, height=26.9441, viewOffsetX=11.2707, 
viewOffsetY=0.0273296)
session.viewports['Viewport: 1'].view.setValues(nearPlane=112.706, 
farPlane=148.211, width=72.092, height=34.554, cameraPosition=(111.793, 
60.8527, 34.2041), cameraUpVector=(-0.762956, 0.646444, -0.00287319), 
cameraTarget=(13.2277, 3.99887, 14.2976), viewOffsetX=14.4539, 
viewOffsetY=0.0350484)
session.viewports['Viewport: 1'].view.setValues(nearPlane=109.897, 
farPlane=163.013, width=70.2955, height=33.693, cameraPosition=(
99.8441, 68.4503, -59.3863), cameraUpVector=(-0.711397, 0.624407, 
0.322537), cameraTarget=(21.3874, 9.33617, 1.39041), 
viewOffsetX=14.0937, viewOffsetY=0.034175)
session.viewports['Viewport: 1'].view.setValues(nearPlane=110.635, 
farPlane=162.275, width=66.5219, height=31.8843, viewOffsetX=14.6916, 
viewOffsetY=0.0523915)
session.viewports['Viewport: 1'].view.setValues(nearPlane=109.356, 
farPlane=151.729, width=65.7526, height=31.5156, cameraPosition=(
114.191, 41.3795, 54.5254), cameraUpVector=(-0.743003, 0.635575, 
0.209741), cameraTarget=(13.7842, -3.94526, 19.7699), 
viewOffsetX=14.5217, viewOffsetY=0.0517857)
session.viewports['Viewport: 1'].view.setValues(nearPlane=94.9846, 
farPlane=157.733, width=57.1116, height=27.3739, cameraPosition=(
29.8948, 23.9628, 125.889), cameraUpVector=(-0.731581, 0.605224, 
-0.313837), cameraTarget=(-4.55732, -8.67218, 20.5716), 
viewOffsetX=12.6133, viewOffsetY=0.0449801)
session.viewports['Viewport: 1'].view.setValues(nearPlane=97.4077, 
farPlane=155.31, width=35.7016, height=17.112, viewOffsetX=10.6588, 
viewOffsetY=1.25174)
session.viewports['Viewport: 1'].view.setValues(nearPlane=100.128, 
farPlane=151.728, width=36.6988, height=17.5899, cameraPosition=(
65.2503, 54.5599, 98.5661), cameraUpVector=(-0.725047, 0.604065, 
-0.330774), cameraTarget=(-0.599627, -2.33195, 22.6), 
viewOffsetX=10.9565, viewOffsetY=1.2867)
session.viewports['Viewport: 1'].view.setValues(nearPlane=100.044, 
farPlane=151.811, width=39.0087, height=18.697, viewOffsetX=10.2984, 
viewOffsetY=0.980127)
session.viewports['Viewport: 1'].view.setValues(nearPlane=97.6059, 
farPlane=155.339, width=38.0579, height=18.2413, cameraPosition=(
31.503, 34.3422, 123.04), cameraUpVector=(-0.717547, 0.593274, 
-0.3649), cameraTarget=(-4.46275, -6.83986, 21.2847), 
viewOffsetX=10.0474, viewOffsetY=0.956238)
session.viewports['Viewport: 1'].view.setValues(nearPlane=99.2003, 
farPlane=156.238, width=38.6796, height=18.5393, cameraPosition=(
10.3694, -24.9531, 130.228), cameraUpVector=(-0.697086, 0.697385, 
-0.166511), cameraTarget=(-6.47559, -13.7312, 16.5003), 
viewOffsetX=10.2115, viewOffsetY=0.971858)
session.viewports['Viewport: 1'].view.setValues(nearPlane=110.531, 
farPlane=149.099, width=43.0977, height=20.6569, cameraPosition=(
38.2141, -117.976, 45.3756), cameraUpVector=(-0.193112, 0.593458, 
0.781355), cameraTarget=(-6.97708, -18.4851, 7.92055), 
viewOffsetX=11.3779, viewOffsetY=1.08287)
session.viewports['Viewport: 1'].view.setValues(nearPlane=118.182, 
farPlane=142.28, width=46.0811, height=22.0869, cameraPosition=(
14.2353, -130.207, 5.39509), cameraUpVector=(-0.0776698, 0.347484, 
0.934464), cameraTarget=(-10.3887, -17.382, 2.59951), 
viewOffsetX=12.1655, viewOffsetY=1.15783)
session.viewports['Viewport: 1'].view.setValues(nearPlane=118.377, 
farPlane=142.086, width=38.3375, height=18.3753, viewOffsetX=12.9837, 
viewOffsetY=1.29332)
a = mdb.models['Model-1'].rootAssembly
r1 = a.instances['BALLOON-1'].referencePoints
n1 = a.instances['PART-1-1'].nodes
a.DatumCsysByThreePoints(origin=r1[6], point1=n1[15207], point2=n1[14873], 
name='CYLINDRICAL', coordSysType=CYLINDRICAL)
session.viewports['Viewport: 1'].view.setValues(nearPlane=116.52, 
farPlane=143.942, width=65.8577, height=31.5659, viewOffsetX=12.8911, 
viewOffsetY=-0.0922961)
session.viewports['Viewport: 1'].view.setValues(nearPlane=98.4702, 
farPlane=158.833, width=55.6557, height=26.676, cameraPosition=(
53.5028, -55.0037, 108.618), cameraUpVector=(-0.430019, 0.866053, 
0.255021), cameraTarget=(-3.9814, -12.384, 17.9384), 
viewOffsetX=10.8941, viewOffsetY=-0.0779985)
session.viewports['Viewport: 1'].view.setValues(nearPlane=103.228, 
farPlane=154.49, width=58.3447, height=27.9649, cameraPosition=(
89.2327, -5.89817, 98.1952), cameraUpVector=(-0.507755, 0.858799, 
0.0681868), cameraTarget=(2.47594, -6.30074, 21.9275), 
viewOffsetX=11.4204, viewOffsetY=-0.081767)
session.viewports['Viewport: 1'].view.setValues(nearPlane=100.393, 
farPlane=156.466, width=56.7424, height=27.1969, cameraPosition=(
69.5313, 49.2715, 101.447), cameraUpVector=(-0.661484, 0.678348, 
-0.319816), cameraTarget=(0.0265524, 1.14475, 22.7286), 
viewOffsetX=11.1068, viewOffsetY=-0.0795215)
a = mdb.models['Model-1'].rootAssembly
n1 = a.instances['PART-1-1'].nodes
nodes1 = n1.getSequenceFromMask(mask=(
'[#1ffff #0:17 #fffffffc #f #0:16 #ffe00000 #7fffff', 
' #0:17 #ffffff00 #3ff #0:16 #f8000000 #1fffffff #0:17', 
' #ffffc000 #f #0:4 #7fe00 #0:4 #ff000000 #3', 
' #0:4 #1ff80 #0:4 #ffc00000 #0:5 #7fe0 #0:4', 
' #3ff00000 #0:5 #1ff8 #0:4 #ffc0000 #0:5 #7fe', 
' #0:4 #3ff0000 #0:4 #80000000 #1ff #0:4 #ffc000', 
' #0:4 #e0000000 #7f #0:4 #3ff000 #0:4 #f8000000', 
' #1f #0:4 #7ffffc00 #0:16 #ffff8000 #7fff #0:15', 
' #80000000 #7fffffff #0:16 #ffff8000 #7fff #0:15 #80000000', 
' #7fffffff #0:16 #ffff8000 #f #0:4 #7fe00 #0:4', 
' #ff000000 #3 #0:4 #1ff80 #0:4 #ffc00000 #0:5', 
' #7fe0 #0:4 #3ff00000 #0:5 #1ff8 #0:4 #ffc0000', 
' #0:5 #7fe #0:4 #3ff0000 #0:4 #80000000 #1ff', 
' #0:4 #ffc000 #0:4 #e0000000 #7f #0:4 #3ff000', 
' #0:4 #f8000000 #1ffff #0:17 #ffffc #600000 #3000000', 
' #18000000 #c0000000 #0 #6 #30 #180 #c00', 
' #6000 #30000 #180000 #c00000 #6000000 #30000000 #80000000', 
' #1 #7fffc #0:16 #ffff8 #600000 #3000000 #18000000', 
' #c0000000 #0 #6 #30 #180 #c00 #6000', 
' #30000 #180000 #c00000 #6000000 #30000000 #80000000 #1ffff', 
' #0:17 #ffffc #600000 #3000000 #18000000 #c0000000 #0', 
' #6 #30 #180 #c00 #6000 #30000 #180000', 
' #c00000 #6000000 #30000000 #80000000 #1 #7fffc #0:16', 
' #ffff8 #600000 #3000000 #18000000 #c0000000 #0 #6', 
' #30 #180 #c00 #6000 #30000 #180000 #c00000', 
' #6000000 #30000000 #80000000 ]', ), )
region = a.Set(nodes=nodes1, name='Set-2')
datum = mdb.models['Model-1'].rootAssembly.datums[13]
mdb.models['Model-1'].DisplacementBC(name='BC-1', createStepName='Initial', 
region=region, u1=SET, u2=SET, u3=SET, ur1=SET, ur2=SET, ur3=SET, 
amplitude=UNSET, distributionType=UNIFORM, fieldName='', 
localCsys=datum)
session.viewports['Viewport: 1'].view.setValues(nearPlane=99.8841, 
farPlane=156.975, width=67.9699, height=32.5783, viewOffsetX=12.2439, 
viewOffsetY=-0.970705)
session.viewports['Viewport: 1'].view.setValues(nearPlane=97.9992, 
farPlane=158.145, width=66.6873, height=31.9636, cameraPosition=(
58.0788, 44.1505, 110.568), cameraUpVector=(-0.671579, 0.667705, 
-0.321171), cameraTarget=(-1.74354, -0.704419, 22.517), 
viewOffsetX=12.0128, viewOffsetY=-0.952388)
session.viewports['Viewport: 1'].view.setValues(nearPlane=100.475, 
farPlane=155.668, width=41.6776, height=19.9763, viewOffsetX=12.2244, 
viewOffsetY=1.80359)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')
session.viewports['Viewport: 1'].view.setValues(nearPlane=98.085, 
farPlane=156.485, width=40.6862, height=19.5011, cameraPosition=(
32.665, 22.5609, 126.162), cameraUpVector=(-0.528177, 0.770907, 
-0.355994), cameraTarget=(-6.65439, -3.16156, 20.6345), 
viewOffsetX=11.9336, viewOffsetY=1.76069)
mdb.models['Model-1'].TabularAmplitude(name='AMPLITUDE', timeSpan=STEP, 
smooth=SOLVER_DEFAULT, data=((0.0, 0.0), (0.7, 1.0), (1.0, 0.0)))
a = mdb.models['Model-1'].rootAssembly
n1 = a.instances['BALLOON-1'].nodes
nodes1 = n1.getSequenceFromMask(mask=('[#ffffffff:181 #f ]', ), )
region = a.Set(nodes=nodes1, name='Set-3')
datum = mdb.models['Model-1'].rootAssembly.datums[13]
mdb.models['Model-1'].DisplacementBC(name='BC-2', createStepName='Step-1', 
region=region, u1=5.4, u2=UNSET, u3=UNSET, ur1=UNSET, ur2=UNSET, 
ur3=UNSET, amplitude='AMPLITUDE', fixed=OFF, distributionType=UNIFORM, 
fieldName='', localCsys=datum)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON, loads=OFF, 
bcs=OFF, predefinedFields=OFF, connectors=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
meshTechnique=ON)
p = mdb.models['Model-1'].parts['BALLOON']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
meshTechnique=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
referenceRepresentation=OFF)
elemType1 = mesh.ElemType(elemCode=S4R, elemLibrary=EXPLICIT, 
secondOrderAccuracy=OFF, hourglassControl=DEFAULT)
p = mdb.models['Model-1'].parts['BALLOON']
z1 = p.elements
elems1 = z1[0:5760]
pickedRegions =(elems1, )
p.setElementType(regions=pickedRegions, elemTypes=(elemType1, ))
p = mdb.models['Model-1'].parts['COARCT_IDEALIZED']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
elemType1 = mesh.ElemType(elemCode=C3D8R, elemLibrary=EXPLICIT, 
kinematicSplit=AVERAGE_STRAIN, secondOrderAccuracy=OFF, 
hourglassControl=DEFAULT, distortionControl=DEFAULT)
p = mdb.models['Model-1'].parts['COARCT_IDEALIZED']
z1 = p.elements
elems1 = z1[0:13056]
pickedRegions =(elems1, )

## Check this section in second iteration !!

p.setElementType(regions=pickedRegions, elemTypes=(elemType1, ))
p = mdb.models['Model-1'].parts['ASSEMBLED_SKETCH_INNER_SURFACE']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
elemType1 = mesh.ElemType(elemCode=C3D8R, elemLibrary=EXPLICIT, 
kinematicSplit=AVERAGE_STRAIN, secondOrderAccuracy=OFF, 
hourglassControl=DEFAULT, distortionControl=DEFAULT)
p = mdb.models['Model-1'].parts['ASSEMBLED_SKETCH_INNER_SURFACE']
z1 = p.elements

## Find way to read in total elements and insert into code 

Total_Elements_Stent = len(z1)
print(Total_Elements_Stent)

elems1 = z1[0:Total_Elements_Stent]
pickedRegions =(elems1, )
p.setElementType(regions=pickedRegions, elemTypes=(elemType1, ))
a1 = mdb.models['Model-1'].rootAssembly
a1.regenerate()
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
meshTechnique=OFF)

## SETTING CORRECT AMPLITUDE
mdb.models['Model-1'].amplitudes['AMPLITUDE'].setValues(timeSpan=STEP, 
smooth=SOLVER_DEFAULT, data=((0.0, 0.0), (1.0, 1.0)))

## RENAMING STEP 1 AS EXPANSION
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
predefinedFields=OFF, connectors=OFF, adaptiveMeshConstraints=ON)
mdb.models['Model-1'].steps.changeKey(fromName='Step-1', toName='Expansion')

## SETTING STEP 2 AS RECOIL
mdb.models['Model-1'].ExplicitDynamicsStep(name='Recoil', previous='Expansion', 
improvedDtMethod=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Recoil')
mdb.models['Model-1'].steps['Recoil'].setValues(massScaling=((SEMI_AUTOMATIC, 
MODEL, THROUGHOUT_STEP, 0.0, 10e-06, BELOW_MIN, 1000, 0, 0.0, 0.0, 0, 
None), ), improvedDtMethod=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
predefinedFields=ON, connectors=ON, adaptiveMeshConstraints=OFF)
mdb.models['Model-1'].boundaryConditions['BC-2'].setValuesInStep(
stepName='Recoil', u1=-5.4)


## SETTING NUMBER OF INTERVALS IN FIELD OUTPUT - STANDARD = 20
mdb.models['Model-1'].fieldOutputRequests['F-Output-1'].setValues(
numIntervals=10)
mdb.models['Model-1'].fieldOutputRequests['F-Output-2'].setValues(
numIntervals=10)

mdb.models['Model-1'].fieldOutputRequests['F-Output-1'].setValues(
variables=('S', 'E', 'PEEQ', 'U'))

## Create Lumen Gain Set  - Double checking displacement values in Isight.

#a = mdb.models['Model-1'].rootAssembly
#n1 = a.instances['PART-1-1'].nodes
#nodes1 = n1.getSequenceFromMask(mask=(
#'[#0:4 #ffffff00 #ffffffff:9 #7ff #0:79 #84210800 #21084210', 
#' #8421084 #21 #0 #84000000 #21084210 #8421084 #108421', 
#' #0:2 #21084200 #8421084 #42108421 #8 #0 #21000000', 
#' #8421084 #42108421 #42108 #0:2 #8421080 #42108421 #10842108', 
#' #2 #0 #8400000 #42108421 #10842108 #10842 #0:2', 
#' #42108420 #10842108 #84210842 #0:2 #42100000 #10842108 #84210842', 
#' #4210 #0:2 #10842108 #84210842 #21084210 #0:2 #10840000', 
#' #84210842 #21084210 #1084 #0:2 #84210842 #21084210 #8421084', 
#' #0:2 #84210000 #21084210 #8421084 #421 #0 #80000000', 
#' #21084210 #8421084 #2108421 #0:2 #21084000 #8421084 #42108421', 
#' #108 #0 #20000000 #8421084 #42108421 #842108 #0:2', 
#' #8421000 #42108421 #10842108 #42 #0:74 #ffff8000 #ffffffff:8', 
#' #7fffffff #0:5 #8421080 #42108421 #10842108 #2 #0', 
#' #8400000 #42108421 #10842108 #10842 #0:2 #42108420 #10842108', 
#' #84210842 #0:2 #42100000 #10842108 #84210842 #4210 #0:2', 
#' #10842108 #84210842 #21084210 #0:2 #10840000 #84210842 #21084210', 
#' #1084 #0:2 #84210842 #21084210 #8421084 #0:2 #84210000', 
#' #21084210 #8421084 #421 #0 #80000000 #21084210 #8421084', 
#' #2108421 #0:2 #21084000 #8421084 #42108421 #108 #0', 
#' #20000000 #8421084 #42108421 #842108 #0:2 #8421000 #42108421', 
#' #10842108 #42 #0 #8000000 #42108421 #10842108 #210842', 
#' #0:2 #42108400 #10842108 #84210842 #10 #0 #42000000', 
#' #10842108 #84210842 #84210 ]', ), )
#a.Set(nodes=nodes1, name='Lumen_Gain')
#regionDef=mdb.models['Model-1'].rootAssembly.sets['Lumen_Gain']
#mdb.models['Model-1'].FieldOutputRequest(name='F-Output-3', 
#createStepName='Expansion', variables=('U', ), region=regionDef, 
#sectionPoints=DEFAULT, rebar=EXCLUDE)

mdb.models['Model-1'].FieldOutputRequest(name='F-Output-3', 
createStepName='Expansion', variables=('U', ), region=regionDef, 
sectionPoints=DEFAULT, rebar=EXCLUDE)

a = mdb.models['Model-1'].rootAssembly
n1 = a.instances['ASSEMBLED_SKETCH_INNER_SURFACE-1'].nodes
nodes1 = n1.getSequenceFromMask(mask=(
'[#0:4013 #fffff000 #ffffffff:1002 #7fffff ]', ), )
a.Set(nodes=nodes1, name='OuterSurfaceStentSet')
regionDef=mdb.models['Model-1'].rootAssembly.sets['OuterSurfaceStentSet']
mdb.models['Model-1'].fieldOutputRequests['F-Output-3'].setValues(
region=regionDef)
mdb.models['Model-1'].fieldOutputRequests['F-Output-3'].setValues(
numIntervals=10)

## Creat INP File

mdb.Job(name='STENT_OPTIMIZATION', model='Model-1', description='', 
type=ANALYSIS, atTime=None, waitMinutes=0, waitHours=0, queue=None, 
memory=90, memoryUnits=PERCENTAGE, explicitPrecision=DOUBLE_PLUS_PACK, 
nodalOutputPrecision=SINGLE, echoPrint=OFF, modelPrint=OFF, 
contactPrint=OFF, historyPrint=OFF, userSubroutine='', scratch='', 
resultsFormat=ODB, parallelizationMethodExplicit=DOMAIN, numDomains=4, 
activateLoadBalancing=False, multiprocessingMode=DEFAULT, numCpus=4)
mdb.jobs['STENT_OPTIMIZATION'].writeInput(consistencyChecking=OFF)


#import subprocess

# close Abaqus
sys.exit()



# close command window
#subprocess.call(['taskkill', '/f', '/im', 'cmd.exe'])

# Close abaqus CAE
#sys.exit()

# Close windows Command

#os.system("taskkill /f /im cmd.exe")
