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
renderView1.ViewSize = [1126, 755]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.CenterOfRotation = [0.0, 0.0, 0.004999999888241291]
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [0.0, 0.0, 0.5517515692206815]
renderView1.CameraFocalPoint = [0.0, 0.0, 0.004999999888241291]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 0.14150971908292684
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

# create a new 'OpenFOAMReader'
mixerVessel2Dfoam = OpenFOAMReader(FileName='D:/Engineering/PhD/System_Architecture/7_full_integration/A_Software_development_final/A_PROTOTYPE_TWOWAY_FINAL/openfoam/mixerVessel2D/mixerVessel2D.foam')
mixerVessel2Dfoam.MeshRegions = ['internalMesh']
mixerVessel2Dfoam.CellArrays = ['U', 'epsilon', 'k', 'nut', 'p']

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from mixerVessel2Dfoam
mixerVessel2DfoamDisplay = Show(mixerVessel2Dfoam, renderView1, 'UnstructuredGridRepresentation')

# get color transfer function/color map for 'U'
uLUT = GetColorTransferFunction('U')
uLUT.RGBPoints = [8.57114431788305e-05, 0.231373, 0.298039, 0.752941, 0.24623034892665993, 0.865003, 0.865003, 0.865003, 0.492374986410141, 0.705882, 0.0156863, 0.14902]
uLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'U'
uPWF = GetOpacityTransferFunction('U')
uPWF.Points = [8.57114431788305e-05, 0.0, 0.5, 0.0, 0.492374986410141, 1.0, 0.5, 0.0]
uPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
mixerVessel2DfoamDisplay.Representation = 'Surface'
mixerVessel2DfoamDisplay.ColorArrayName = ['POINTS', 'U']
mixerVessel2DfoamDisplay.LookupTable = uLUT
mixerVessel2DfoamDisplay.OSPRayScaleArray = 'p'
mixerVessel2DfoamDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
mixerVessel2DfoamDisplay.SelectOrientationVectors = 'U'
mixerVessel2DfoamDisplay.ScaleFactor = 0.020000000298023225
mixerVessel2DfoamDisplay.SelectScaleArray = 'p'
mixerVessel2DfoamDisplay.GlyphType = 'Arrow'
mixerVessel2DfoamDisplay.GlyphTableIndexArray = 'p'
mixerVessel2DfoamDisplay.GaussianRadius = 0.0010000000149011613
mixerVessel2DfoamDisplay.SetScaleArray = ['POINTS', 'p']
mixerVessel2DfoamDisplay.ScaleTransferFunction = 'PiecewiseFunction'
mixerVessel2DfoamDisplay.OpacityArray = ['POINTS', 'p']
mixerVessel2DfoamDisplay.OpacityTransferFunction = 'PiecewiseFunction'
mixerVessel2DfoamDisplay.DataAxesGrid = 'GridAxesRepresentation'
mixerVessel2DfoamDisplay.PolarAxes = 'PolarAxesRepresentation'
mixerVessel2DfoamDisplay.ScalarOpacityFunction = uPWF
mixerVessel2DfoamDisplay.ScalarOpacityUnitDistance = 0.01946894989263917
mixerVessel2DfoamDisplay.ExtractedBlockIndex = 1

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
mixerVessel2DfoamDisplay.OSPRayScaleFunction.Points = [0.008018268893823101, 0.0, 0.5, 0.0, 2.3, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
mixerVessel2DfoamDisplay.ScaleTransferFunction.Points = [-0.6950129866600037, 0.0, 0.5, 0.0, 20.028099060058594, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
mixerVessel2DfoamDisplay.OpacityTransferFunction.Points = [-0.6950129866600037, 0.0, 0.5, 0.0, 20.028099060058594, 1.0, 0.5, 0.0]

# setup the color legend parameters for each legend in this view

# get color legend/bar for uLUT in view renderView1
uLUTColorBar = GetScalarBar(uLUT, renderView1)
uLUTColorBar.WindowLocation = 'AnyLocation'
uLUTColorBar.Title = 'U'
uLUTColorBar.ComponentTitle = 'Magnitude'
uLUTColorBar.ScalarBarLength = 0.7008439897698198

# set color bar visibility
uLUTColorBar.Visibility = 1

# show color legend
mixerVessel2DfoamDisplay.SetScalarBarVisibility(renderView1, True)

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# finally, restore active source
SetActiveSource(mixerVessel2Dfoam)
# ----------------------------------------------------------------