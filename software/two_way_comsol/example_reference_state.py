# state file generated using paraview version 5.8.0

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

# trace generated using paraview version 5.8.0
#
# To ensure correct image size when batch processing, please search 
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# get the material library
materialLibrary1 = GetMaterialLibrary()

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [1156, 755]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.CenterOfRotation = [0.07000000000000002, 0.02500000000000001, 0.030000000000000013]
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [0.07000000000000002, 0.02500000000000001, -0.2796993796482651]
renderView1.CameraFocalPoint = [0.07000000000000002, 0.02500000000000001, 0.030000000000000013]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 0.08015609770940701
renderView1.BackEnd = 'OSPRay raycaster'
renderView1.OSPRayMaterialLibrary = materialLibrary1

SetActiveView(None)

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

# create new layout object 'Layout #1'
layout1 = CreateLayout(name='Layout #1')
layout1.AssignView(0, renderView1)

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView1)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'XML Unstructured Grid Reader'
pressvtu = XMLUnstructuredGridReader(FileName=['D:/Engineering/PhD/System_Architecture/7_full_integration/A_Software_development_final/A_PROTOTYPE_TWOWAY_FINAL/comsol_paraview_dyn/press.vtu'])
pressvtu.PointArrayStatus = ['Color']

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from pressvtu
pressvtuDisplay = Show(pressvtu, renderView1, 'UnstructuredGridRepresentation')

# get color transfer function/color map for 'Color'
colorLUT = GetColorTransferFunction('Color')
colorLUT.RGBPoints = [-19895.14842135077, 0.231373, 0.298039, 0.752941, 180477.41782225334, 0.865003, 0.865003, 0.865003, 380849.9840658575, 0.705882, 0.0156863, 0.14902]
colorLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'Color'
colorPWF = GetOpacityTransferFunction('Color')
colorPWF.Points = [-19895.14842135077, 0.0, 0.5, 0.0, 380849.9840658575, 1.0, 0.5, 0.0]
colorPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
pressvtuDisplay.Representation = 'Surface'
pressvtuDisplay.ColorArrayName = ['POINTS', 'Color']
pressvtuDisplay.LookupTable = colorLUT
pressvtuDisplay.OSPRayScaleArray = 'Color'
pressvtuDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
pressvtuDisplay.SelectOrientationVectors = 'Color'
pressvtuDisplay.ScaleFactor = 0.014000000000000005
pressvtuDisplay.SelectScaleArray = 'Color'
pressvtuDisplay.GlyphType = 'Arrow'
pressvtuDisplay.GlyphTableIndexArray = 'Color'
pressvtuDisplay.GaussianRadius = 0.0007000000000000002
pressvtuDisplay.SetScaleArray = ['POINTS', 'Color']
pressvtuDisplay.ScaleTransferFunction = 'PiecewiseFunction'
pressvtuDisplay.OpacityArray = ['POINTS', 'Color']
pressvtuDisplay.OpacityTransferFunction = 'PiecewiseFunction'
pressvtuDisplay.DataAxesGrid = 'GridAxesRepresentation'
pressvtuDisplay.PolarAxes = 'PolarAxesRepresentation'
pressvtuDisplay.ScalarOpacityFunction = colorPWF
pressvtuDisplay.ScalarOpacityUnitDistance = 0.004094275983606231

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
pressvtuDisplay.OSPRayScaleFunction.Points = [0.008018268893823101, 0.0, 0.5, 0.0, 2.3, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
pressvtuDisplay.ScaleTransferFunction.Points = [-19895.14842135077, 0.0, 0.5, 0.0, 380849.9840658575, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
pressvtuDisplay.OpacityTransferFunction.Points = [-19895.14842135077, 0.0, 0.5, 0.0, 380849.9840658575, 1.0, 0.5, 0.0]

# setup the color legend parameters for each legend in this view

# get color legend/bar for colorLUT in view renderView1
colorLUTColorBar = GetScalarBar(colorLUT, renderView1)
colorLUTColorBar.WindowLocation = 'AnyLocation'
colorLUTColorBar.Title = 'Color'
colorLUTColorBar.ComponentTitle = ''
colorLUTColorBar.ScalarBarLength = 0.7008439897698198

# set color bar visibility
colorLUTColorBar.Visibility = 1

# show color legend
pressvtuDisplay.SetScalarBarVisibility(renderView1, True)

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# finally, restore active source
SetActiveSource(pressvtu)
# ----------------------------------------------------------------