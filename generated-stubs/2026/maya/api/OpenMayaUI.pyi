"""
maya.api.OpenMayaUI stub file generated for Maya 2026 using:
https://github.com/nils-soderman/openmaya-stub-generator
"""
from __future__ import annotations

import collections.abc
import maya.api.OpenMaya as om
import maya.api.OpenMayaRender as omr
from typing import Any, Callable, Self, Sequence, overload

class M3dView:
	"""M3dView provides methods for working with 3D model views."""
	kBoundingBox:int=0
	kFlatShaded:int=1
	kGouraudShaded:int=2
	kWireFrame:int=3
	kPoints:int=4
	kActive:int=0
	kLive:int=1
	kDormant:int=2
	kInvisible:int=3
	kHilite:int=4
	kTemplate:int=5
	kActiveTemplate:int=6
	kActiveComponent:int=7
	kLead:int=8
	kIntermediateObject:int=9
	kActiveAffected:int=10
	kNoStatus:int=11
	kActiveColors:int=0
	kDormantColors:int=2
	kTemplateColor:int=5
	kBackgroundColor:int=6
	kLeft:int=0
	kCenter:int=1
	kRight:int=2
	kDisplayEverything:int=-1
	kDisplayNurbsCurves:int=1
	kDisplayNurbsSurfaces:int=2
	kDisplayMeshes:int=4
	kDisplayPlanes:int=8
	kDisplayLights:int=16
	kDisplayCameras:int=32
	kDisplayJoints:int=64
	kDisplayIkHandles:int=128
	kDisplayDeformers:int=256
	kDisplayDynamics:int=512
	kDisplayParticleInstancers:int=1024
	kDisplayLocators:int=2048
	kDisplayDimensions:int=4096
	kDisplaySelectHandles:int=8192
	kDisplayPivots:int=16384
	kDisplayTextures:int=32768
	kDisplayGrid:int=65536
	kDisplayCVs:int=131072
	kDisplayHulls:int=262144
	kDisplayStrokes:int=524288
	kDisplaySubdivSurfaces:int=1048576
	kDisplayFluids:int=2097152
	kDisplayFollicles:int=4194304
	kDisplayHairSystems:int=8388608
	kDisplayImagePlane:int=16777216
	kDisplayNCloths:int=33554432
	kDisplayNRigids:int=67108864
	kDisplayDynamicConstraints:int=134217728
	kDisplayManipulators:int=268435456
	kDisplayNParticles:int=536870912
	kExcludeMotionTrails:int=1073741824
	kExcludePluginShapes:int=-2147483648
	kLightAll:int=0
	kLightSelected:int=1
	kLightActive:int=2
	kLightDefault:int=3
	kUnused1:int=4
	kLightNone:int=5
	kDefaultQualityRenderer:int=0
	kHighQualityRenderer:int=1
	kViewport2Renderer:int=2
	kExternalRenderer:int=3
	kDepth_8:int=0
	kDepth_Float:int=1
	kStippleNone:int=0
	kStippleDashed:int=1
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def display(self)->int:
		"""display() -> long

		Returns a long containing a C++ 'void' pointer which points to the OpenGL context for this view.
		On 32-bit OS X this is an AGLContext.
		On 64-bit OS X this is an NSOpenGLContext pointer.
		On Windows this is an HGLRC."""
	def deviceContext(self)->int:
		"""deviceContext() -> long

		Returns a long containing a C++ 'void' pointer which points to the Windows device context for this view."""
	@staticmethod
	def active3dView()->M3dView:
		"""active3dView() -> M3dView

		Returns the active view in the form of a class (M3dView) that can operate on it."""
	@staticmethod
	def activeAffectedColor()->om.MColor:
		"""activeAffectedColor() -> MColor

		Returns the color for active affected objects."""
	@staticmethod
	def activeTemplateColor()->om.MColor:
		"""activeTemplateColor() -> MColor

		Returns the color for active template objects."""
	@staticmethod
	def applicationShell()->int:
		"""applicationShell() -> long

		Returns a long containing a C++ 'void' pointer which points to the native handle for Maya's main window."""
	@staticmethod
	def backgroundColor()->om.MColor:
		"""backgroundColor() -> MColor

		Returns the value of the background color."""
	@staticmethod
	def backgroundColorBottom()->om.MColor:
		"""backgroundColorBottom() -> MColor

		Returns the value of the background gradient bottom color."""
	@staticmethod
	def backgroundColorTop()->om.MColor:
		"""backgroundColorTop() -> MColor

		Returns the value of the background gradient top color."""
	def beginGL(self)->Self:
		"""(Deprecated: Please use Viewport 2.0 APIs instead.) beginGL() -> self

		Setup port for native OpenGL drawing calls."""
	def beginProjMatrixOverride(self,projectionMatrix:om.MMatrix)->Self:
		"""(Deprecated: Please use MHWRender::MRenderOverride instead.) beginProjMatrixOverride(projectionMatrix) -> self

		Begin overriding the projection matrix used in openGL drawing.
		This override is enabled until endProjMatrixOverride() is called.

		* projectionMatrix (MMatrix) - Projection matrix used in openGL drawing"""
	def beginSelect(self,buffer:bytearray|None=None,size:int=0)->Self:
		"""beginSelect(buffer=None, size=0) -> self

		Start selecting. The buffer passed is used to record selection hits.

		* buffer (bytearray) - OpenGl pick buffer
		* size (int) - Buffer size"""
	def beginXorDrawing(self,drawOrthographic:bool=True,disableDepthTesting:bool=True,lineWidth:float=1.0,stipplePattern:int=M3dView.kStippleNone,lineColor:om.MColor=Any,1:Any,12:Any)->None:
		"""beginXorDrawing(drawOrthographic=True, disableDepthTesting=True, lineWidth=1.0, stipplePattern=kStippleNone, lineColor=MColor(1, 1, 1)) -> self

		Setup the context for exclusive-or (XOR) drawing.

		In XOR drawing the color values of the pixels being drawn is exclusive-ored with the color values already present in the view. The advantage of this is that exclusive-oring the same pixels with the same color values a second time will restore the pixels to their original colors, making it possible to temporarily display and erase lines without having to redraw the entire view. This makes XOR drawing particularly useful for drawing guidelines for tools.

		One disadvantage of XOR drawing is that the final color after the exclusive-or will not match your drawing color, except when the original color of the pixel was black. For example, XORing a white line across a red background will result in a cyan line and XORing it across a changing background will result in a line of changing colors. However in most situations where you would use XOR drawing the color of the lines is irrelevant just so long as they are visible.

		It is an error to call beginXorDrawing() again before calling endXorDrawing() first.

		* drawOrthographic (bool) - Draw using orthographic projection. Default is True.
		* disableDepthTesting (bool) - Disable depth testing during draw. Default is True.
		* lineWidth (float) - Set up line width. Default is 1.
		* stipplePattern (int) - Line stipple pattern. Default is kStippleNone.
		* lineColor (MColor) - Line color. Default is white (1,1,1).

		Valid stipple patterns:
		  kStippleNone      No stipple. Solid line
		  kStippleDashed    Dashed line stipple"""
	def colorAtIndex(self,index:int,table:int=M3dView.kActiveColors)->om.MColor:
		"""colorAtIndex(index, table=kActiveColors) -> MColor

		Returns the value of the color at the given index in the application's color table.


		* index (int) - Index of the color to retrieve
		* table (int) - Table to index into

		Valid color tables:
		  kActiveColors        Colors for active objects
		  kDormantColors       Colors for dormant objects
		  kTemplateColor       Colors for templated objects
		  kBackgroundColor     Colors for background color"""
	def colorMask(self)->list[bool]:
		"""(Deprecated: Please use MHWRender::MUIDrawManager instead.) colorMask() -> [bool, bool, bool, bool]

		Get the current color mask"""
	def disallowPolygonOffset(self)->bool:
		"""disallowPolygonOffset() -> bool

		Returns the current state of the disallow polygon offset bit.  See setDisallowPolygonOffset for more information."""
	@staticmethod
	def displayStatus(path:om.MDagPath)->int:
		"""displayStatus(path) -> int

		Returns the display status of the given DAG path.

		* path (MDagPath) - the DAG path to get.

		Valid display status:
		  kActive               Object is active (selected).
		  kLive                 Object is live (construction surface).
		  kDormant              Object is dormant.
		  kInvisible            Object is invisible (not drawn).
		  kHilite               Object is hilited (has selectable components).
		  kTemplate             Object is templated (Not renderable).
		  kActiveTemplate       Object is active and templated.
		  kActiveComponent      Object has active components.
		  kLead                 Last selected object.
		  kIntermediateObject   Construction object (not drawn).
		  kActiveAffected       Affected by active object(s).
		  kNoStatus             Object does not have a valid display status."""
	def displayStyle(self)->int:
		"""displayStyle() -> int

		Return the display style for this 3d view.  kBoundingBox     Bounding box display.
		  kFlatShaded      Flat shaded display.
		  kGouraudShaded   Gouraud shaded display.
		  kWireFrame       Wire frame display.
		  kPoints          Points only display."""
	def drawText(self,text:str,position:om.MPoint,textPosition:int=M3dView.kLeft)->Self:
		"""(Deprecated: Please use MHWRender::MUIDrawManager in a MHWRender::MHUDRender operation instead.) drawText(text, position, textPosition=kLeft) -> self

		Draws the given text at the given spot in the default font.  This method is provided as a convienient way to draw OpenGL text.

		* text (string) - Text to draw
		* position (MPoint) - Position in space to draw at
		* textPosition (int) - Text position relative to the point

		Valid textPosition values:
		  kLeft      Draw text to the left of the point
		  kCenter    Draw text centered around the point
		  kRight     Draw text to the right of the point"""
	def endGL(self)->Self:
		"""(Deprecated: Please use Viewport 2.0 APIs instead.) endGL() -> self

		End OpenGL drawing."""
	def endProjMatrixOverride(self)->Self:
		"""(Deprecated: Please use MHWRender::MRenderOverride instead.) endProjMatrixOverride() -> self

		End projection matrix override enabled by beginProjMatrixOverride()."""
	def endSelect(self)->int:
		"""endSelect() -> int

		Finish a selection sequence. Result is stored in the buffer passed  in the beginSelect call."""
	def endXorDrawing(self)->Self:
		"""endXorDrawing() -> self

		Reset the context to non-exclusive-or (non-XOR) screen drawing.

		If endXorDrawing() is called without first calling beginXorDrawing() an error will result."""
	@staticmethod
	def get3dView(index:int)->M3dView:
		"""get3dView(index) -> M3dView

		Returns the 3D view at the given index.

		* index (int) - index of the view to get"""
	def getCamera(self)->om.MDagPath:
		"""getCamera() -> MDagPath

		Get the camera for this view."""
	def getColorIndexAndTable(self,glindex:int)->list[int]:
		"""getColorIndexAndTable(glindex) -> [int, int]

		Returns the index and color table representing the given OpenGL color-index value. This method is useful when converting color indices obtained from glReadPixels(GL_COLOR_INDEX) to Maya color-index values suitable for use with the colorAtIndex and setDrawColor methods.

		* glindex (int) - Value of the OpenGL color-index to retrieve"""
	def getLightCount(self,visible:bool=True)->int:
		"""getLightCount(visible=True) -> int

		Get the number of lights for the view.

		* visible (bool) - Specify whether to count visible lights only. By Default this is set True."""
	def getLightIndex(self,lightNumber:int)->int:
		"""getLightIndex(lightNumber) -> int

		Get the internal light index for a given light number

		* lightNumber (int) - Number of the light interested in"""
	def getLightPath(self,lightNumber:int)->om.MDagPath:
		"""getLightPath(lightNumber) -> MDagPath

		Get the path to a certain light.

		* lightNumber (int) - Number of the light interested in"""
	def getLightingMode(self)->int:
		"""getLightingMode() -> int

		Get the current lighting mode for the view:
		  kLightAll         All lights
		  kLightSelected    Selected lights
		  kLightActive      Active lights
		  kLightDefault     Default light
		  kUnused1          Not currently used in Maya
		  kLightNone        No lights / lighting disabled"""
	@staticmethod
	def getM3dViewFromModelEditor(name:str)->M3dView:
		"""getM3dViewFromModelEditor(name) -> M3dView

		Given the name of a model editor, get the M3dView used by that editor. If this fails, then a editor with the given name could not be located.

		* name (string) - The name of the model editor."""
	@staticmethod
	def getM3dViewFromModelPanel(name:str)->M3dView:
		"""getM3dViewFromModelPanel(name) -> M3dView

		Given the name of a model panel, get the M3dView used by that panel. If this fails, then a panel with the given name could not be located.

		* name (string) - The name of the model panel."""
	def getRendererName(self)->int:
		"""getRendererName() -> int

		Get the name of the current renderer being used for drawing to this view:
		  kDefaultQualityRenderer   Equivalent to when the renderer name is "base_OpenGL_Renderer" when queried from the "modelEditor" command
		  kHighQualityRenderer      Equivalent to when the renderer name is "hwRender_OpenGL_Renderer" when queried from the "modelEditor" command
		  kViewport2Renderer        Equivalent to the viewport 2.0 renderer
		  kExternalRenderer         An externally defined renderer name has been set."""
	def getScreenPosition(self)->list[int]:
		"""getScreenPosition() -> [int, int]

		Returns the current position of this view window in screen coordinates.

		This is useful for finding out the exact location of the window as it appears on the screen. These values are in UI coordinate space so the y value increases from bottom to top."""
	@staticmethod
	def hiliteColor()->om.MColor:
		"""hiliteColor() -> MColor

		Returns the color for hilited objects."""
	def initNames(self)->Self:
		"""initNames() -> self

		Reset the name stack. Valid only when beginSelect() has been called."""
	@staticmethod
	def isBackgroundGradient()->bool:
		"""isBackgroundGradient() -> bool

		Returns whether a gradient is being used as the background color."""
	def isLightVisible(self,lightNumber:int)->bool:
		"""isLightVisible(lightNumber) -> bool

		Find out if a light is visible in the view

		* lightNumber (int) - Number of the light interested in"""
	def isShadeActiveOnly(self)->bool:
		"""isShadeActiveOnly() -> bool

		Returns True if this view's display style is shaded for objects that are active and wireframe otherwise."""
	def isVisible(self)->bool:
		"""isVisible() -> bool

		Returns True if this viewport is visible."""
	@staticmethod
	def leadColor()->om.MColor:
		"""leadColor() -> MColor

		Returns the color for lead objects."""
	@staticmethod
	def liveColor()->om.MColor:
		"""liveColor() -> MColor

		Returns the color for live objects."""
	def loadName(self,int:int)->Self:
		"""loadName(int) -> self

		Replace the top of the name stack with the given name. Valid only when beginSelect() has been called.

		* name (int) - Name to be loaded onto the top of the stack."""
	def modelViewMatrix(self)->om.MMatrix:
		"""modelViewMatrix() -> MMatrix

		Returns the modelview matrix currently being used by OpenGL in the current view"""
	def multipleDrawEnabled(self)->bool:
		"""multipleDrawEnabled() -> bool

		This method returns the multiple draw enable state for this view."""
	def multipleDrawPassCount(self)->int:
		"""(Deprecated: Please use MHWRender::MRenderOverride instead.) multipleDrawPassCount() -> int

		This method returns the number of multiple draw passes that are going to be made. By default a 1 is returned."""
	def numActiveColors(self)->int:
		"""numActiveColors() -> int

		Returns the number of active object colors in the internal application color table."""
	def numDormantColors(self)->int:
		"""numDormantColors() -> int

		Returns the number of dormant object colors in the internal application color table."""
	def numUserDefinedColors(self)->int:
		"""numUserDefinedColors() -> int

		Returns the number of user defined colors in the internal application color table.  These colors may be changed by the user and assigned to specific objects.  See the methods of MFnDagNode for information on assigning user defined colors to individual objects.

		The user defined colors are not a color table of their own.  They exist in the active and dormant color tables."""
	@staticmethod
	def numberOf3dViews()->int:
		"""numberOf3dViews() -> int

		Returns the number of 3D views currently in existance."""
	def objectDisplay(self)->int:
		"""objectDisplay() -> int

		Returns a display object mask that indicates which object types are drawn in the current view:
		  kDisplayEverything            Show everything
		  kDisplayNurbsCurves           Show nurbs curves
		  kDisplayNurbsSurfaces         Show nurbs surfaces
		  kDisplayMeshes                Show meshes
		  kDisplayPlanes                Show planes
		  kDisplayLights                Show lights
		  kDisplayCameras               Show camera
		  kDisplayJoints                Show joints
		  kDisplayIkHandles             Show IK handles
		  kDisplayDeformers             Show deformers
		  kDisplayDynamics              Show dynamics
		  kDisplayLocators              Show locators
		  kDisplayDimensions            Show dimensions
		  kDisplaySelectHandles         Show selection handles
		  kDisplayPivots                Show pivots
		  kDisplayTextures              Show textures
		  kDisplayGrid                  Show the grid
		  kDisplayCVs                   Show NURBS CVs
		  kDisplayHulls                 Show NURBS hulls
		  kDisplayStrokes               Show strokes
		  kDisplaySubdivSurfaces        Show subdivision surfaces
		  kDisplayFluids                Show fluids
		  kDisplayFollicles             Show follcles
		  kDisplayHairSystems           Show hair systems
		  kDisplayImagePlane            Show image plane
		  kDisplayNCloths               Show nCloths
		  kDisplayNRigids               Show nRigids
		  kDisplayDynamicConstraints    Show nDynamicConstraints
		  kDisplayManipulators          Show Manipulators
		  kDisplayNParticles            Show nParticles
		  kExcludeMotionTrails          Show motion trails
		  kExcludePluginShapes          Show plugin shapes"""
	def objectListFilterName(self)->str:
		"""objectListFilterName() -> string

		Get the current object list filter name. If none then an emptystring will be returned."""
	def playblastPortHeight(self)->int:
		"""playblastPortHeight() -> int

		Returns the port height of current playblast.
		Valid only when playblast command has been called.
		Otherwise, an invalid value 0 is returned."""
	def playblastPortWidth(self)->int:
		"""playblastPortWidth() -> int

		Returns the port width of current playblast.
		Valid only when playblast command has been called.
		Otherwise, an invalid value 0 is returned."""
	def pluginObjectDisplay(self,pluginDisplayFilter:str)->bool:
		"""pluginObjectDisplay(pluginDisplayFilter) -> bool

		Returns True if the plugin display filter specified by the pluginDisplayFilter is enabled in the current view.

		* pluginDisplayFilter (string) - The name of the plugin display filter."""
	def popName(self)->Self:
		"""popName() -> self

		Removes the top of the name stack. Valid only when beginSelect() has been called."""
	def popViewport(self)->Self:
		"""popViewport() -> self

		Pops the current viewport off of the viewport stack."""
	def portHeight(self)->int:
		"""portHeight() -> int

		Returns the height of the current viewport."""
	def portWidth(self)->int:
		"""portWidth() -> int

		Returns the width of the current viewport."""
	def projectionMatrix(self)->om.MMatrix:
		"""projectionMatrix() -> MMatrix

		Returns the projection matrix currently being used by OpenGL in the current view"""
	def pushName(self,int:int)->Self:
		"""pushName(int) -> self

		Pushes a new name on the name stack. Valid only when beginSelect() has been called.

		* name (int) - Name to be loaded onto the top of the stack."""
	def pushViewport(self,x:int,y:int,width:int,height:int)->Self:
		"""pushViewport(x, y, width, height) -> self

		Set the current viewport dimensions. Will keep track of the last viewport dimensions on a stack.
		When finished with this viewport, the current dimensions should be removed from the top of stack using M3dView.popViewport().

		* x (int) - Lower left corner of viewport (x coordinate).
		* y (int) - Lower left corner of viewport (y coordinate).
		* width (int) - Width of the viewport.
		* height (int) - Height of the viewport."""
	def readBufferTo2dTexture(self,x:int,y:int,width:int,height:int)->Self:
		"""(Deprecated: Please use MHWRender::MRenderTargetManager instead.) readBufferTo2dTexture(x, y, width, height) -> self

		Read the depth values from the frame buffer for a given view into a predefined OpenGL 2d texture. It is assumed that such a texture has been created and bound before making this call.

		* x (int) - Start position x to read.
		* y  (int) - Start position y to read.
		* width (int) - Number of pixels in x to read.
		* height (int) - Number of pixels in y to read."""
	def readColorBuffer(self,*args)->Any:
		"""(Deprecated: Please use MHWRender::MRenderTargetManager::acquireRenderTarget() instead.)readColorBuffer(image, readRGBA=False) -> self

		Read the RGB values from the frame buffer for a given view.
		The buffer is read in a pixel format which is BGRA by default, such that each channel is one byte in size.

		* image (MImage) - The image contains the frame buffer pixels.
		* readRGBA (bool) - Read the image back in RGBA format. By default the format is BGRA."""
	def readDepthMap(self,*args)->Any:
		"""(Deprecated: Please use MHWRender::MRenderTargetManager::acquireRenderTarget() instead.) readDepthMap(x, y, width, heigth, bufferPtr, depthMapPrecision) -> self

		Read the depth values from the frame buffer for a given view.
		The buffer is read into a block of data as defined as an argument. The data block size must be large enough to accomodate ( view width * view height * depth map precision ) bytes of data.

		* x (int) - Start position x to read.
		* y (int) - Start position y to read.
		* width (int) - Number of pixels in x to read.
		* height (int) - Number of pixels in y to read.
		* bufferPtr (byterray) - Pointer to depth data allocated by the caller.
		* depthMapPrecision (int) - Enumerated depth precision:
		    kDepth_8          8 bits.
		    kDepth_Float      Floating point."""
	@staticmethod
	def referenceLayerColor()->om.MColor:
		"""referenceLayerColor() -> MColor

		Returns the color for objects which belong to a display layer whose display type is Reference. This color is also used for objects whose display override is set to Reference."""
	def refresh(self,all:bool=False,force:bool=False,offscreen:bool=False)->Self:
		"""refresh(all=False, force=False, offscreen=False) -> self


		Refresh the this view.

		* all (bool) - If True then refresh all views, otherwise refresh this view.
		* force (bool) - If True then force views to refresh even if they do not require it.
		* offscreen (bool) - Should the buffer be redrawn if it's offscreen?"""
	def renderOverrideName(self)->str:
		"""renderOverrideName() -> string

		Get the current render override name. If none then an empty string will be returned."""
	def rendererString(self)->str:
		"""rendererString() -> string

		Get the string name of the current renderer being used for drawing to this view"""
	def scheduleRefresh(self)->Self:
		"""scheduleRefresh() -> self

		Schedule a forced refresh for this 3d-view. This method may be called safely at any time from any thread. The refresh will occur on the main thread when Maya next becomes idle. If a refresh has already been scheduled for this view but has not yet occurred then this method will do nothing."""
	@staticmethod
	def scheduleRefreshAllViews()->None:
		"""scheduleRefreshAllViews() -> None

		Schedule a forced refresh for all 3d-views. This method may be called safely at any time from any thread. The refresh will occur on the main thread when Maya next becomes idle. If a refresh has already been scheduled but has not yet occurred then this method will do nothing."""
	def selectMode(self)->bool:
		"""selectMode() -> bool

		Tells if this M3dView is in selection mode."""
	def setCamera(self,camera:om.MDagPath)->Self:
		"""setCamera(camera) -> self

		Set the camera for this view.

		* camera (MDagPath) - Dag path of the camera for this view"""
	def setColorMask(self,r:bool,g:bool,b:bool,a:bool)->Self:
		"""(Deprecated: Please use MHWRender::MUIDrawManager instead.) setColorMask(r, g, b, a) -> self

		Set the current color mask.

		* r (bool) - Red color mask flag.
		* g (bool) - Green color mask flag.
		* b (bool) - Blue color mask flag.
		* a (bool) - Alpha color mask flag."""
	def setDisallowPolygonOffset(self,v:bool)->Self:
		"""setDisallowPolygonOffset(v) -> self

		Certain Maya actions will use glPolygonOffset to offset polygons drawing into the depth buffer.  This method controls this behavior. When True, it prevents Maya from altering the polygon offset parameters.

		* v (bool) - enable/disable the polygon offset"""
	def setDisplayStyle(self,style:int,activeOnly:Any=False)->Self:
		"""setDisplayStyle(style, activeOnly=False) -> self

		Sets the display style for this view.

		* style (int) - The display style to be set for this view
		See displayStyle() description for a list a valid display style"""
	@overload
	def setDrawColor(self,index:int,table:int=M3dView.kActiveColors)->Self:
		"""(Deprecated: Please use MUIDrawManager::setColorIndex instead.) setDrawColor(index, table=kActiveColors) -> self
		setDrawColor(color) -> self

		Set the color to draw in.  The index argument is an index into the application's color tables.  Valid values range between zero and the size of the table minus one.  The size of the active and dormant color tables can be found using methods of this class.  The background and template color tables are both of size one.

		These indices do not directly correspond to those of the underlying OpenGL color index mode.  Using the glIndex call directly is not recommended and may cause unpredictable results.  This method should be used instead.

		Note that this method will work in either RGBA mode or color index mode.

		* index (int) - index of the color to draw in
		* table (int) - color table to index into
		See colorAtIndex() description of a list a valid color table

		Or
		Set the color to draw in.
		It is a convenient replacement for glColor3.

		* color (MColor) - color to draw in"""
	@overload
	def setDrawColor(self,color:om.MColor)->Self:
		"""(Deprecated: Please use MUIDrawManager::setColorIndex instead.) setDrawColor(index, table=kActiveColors) -> self
		setDrawColor(color) -> self

		Set the color to draw in.  The index argument is an index into the application's color tables.  Valid values range between zero and the size of the table minus one.  The size of the active and dormant color tables can be found using methods of this class.  The background and template color tables are both of size one.

		These indices do not directly correspond to those of the underlying OpenGL color index mode.  Using the glIndex call directly is not recommended and may cause unpredictable results.  This method should be used instead.

		Note that this method will work in either RGBA mode or color index mode.

		* index (int) - index of the color to draw in
		* table (int) - color table to index into
		See colorAtIndex() description of a list a valid color table

		Or
		Set the color to draw in.
		It is a convenient replacement for glColor3.

		* color (MColor) - color to draw in"""
	def setDrawColorAndAlpha(self,color:om.MColor)->Self:
		"""(Deprecated: Please use MUIDrawManager::setColor instead.) setDrawColorAndAlpha(color) -> self

		Set the color to draw in.
		It is a convenient replacement for glColor4.

		* color (MColor) - color to draw in"""
	def setMultipleDrawEnable(self,enable:bool)->Self:
		"""(Deprecated: Please use MHWRender::MRenderOverride instead.)setMultipleDrawEnable(enable) -> self

		This method enables/disables multiple camera drawing for this view. If multiple draw is disabled, then this view will behave like a normal Maya view.

		* enable (bool) - If True, then multiple draw is enabled."""
	def setMultipleDrawPassCount(self,count:int)->Self:
		"""(Deprecated: Please use MHWRender::MRenderOverride instead.) setMultipleDrawPassCount(count) -> self

		This method sets the number of multiple draw passes when multiple draw is enabled.

		* count (int) - The number of multiple draw passes."""
	def setObjectDisplay(self,displayMask:int)->Self:
		"""setObjectDisplay(displayMask) -> self

		Sets a display object mask that indicates which object types are drawn in current view. By default every thing is displayed.

		* displayMask (int) - A combination of display object mask
		See objectDisplay() description for a list of valid display mask"""
	def setObjectListFilterName(self,name:str)->Self:
		"""setObjectListFilterName(name) -> self

		Set the name of the object list filter (MObjectListFilter) to use.

		The filter must be registered before it can be used.

		If the name is an empty string then any existing filter will be removed.

		Any previously set filter will be replaced with the new one.

		* name (string) - Name of the filter."""
	def setPluginObjectDisplay(self,pluginDisplayFilter:str,on:bool)->Self:
		"""setPluginObjectDisplay(pluginDisplayFilter, on) -> self

		Enables or disables a user-defined display filter (i.e. one which was registered using MFnPlugin.registerDisplayFilter() or the 'pluginDisplayFilter' command).

		In Default Viewport, the plug-in will have to check the state of the user-defined display filter in the node's draw code.
		In Viewport 2.0, nodes will be filtered automatically based on the classification associated with the filter.
		During selection/snapping, the plugin will have to check the state of the filter in the node's select/snap code.

		* pluginDisplayFilter (string) - The name of the plugin display filter.
		* on (bool) - Enable or disable the plugin display filter."""
	def setRenderOverrideName(self,name:str)->Self:
		"""setRenderOverrideName(name) -> self

		Set the name of a render override (MRenderOverride) to use.

		The override must be registered before it can be used.

		The override cannot be set unless the view is set to be using the Viewport 2.0 renderer.

		If the override name is an empty string then the any existing override will be removed.

		* name (string) - name Name of the override."""
	def setShowObjectFilterNameInHUD(self,show:bool)->Self:
		"""setShowObjectFilterNameInHUD(show) -> self

		Sets whether or not to display the object filter UI name in the heads up display when an object filter is active. This string is concatenated with the camera name.

		* show (bool) - If True, show the filter UI name in the HUD"""
	def setShowViewSelectedChildren(self,show:bool)->Self:
		"""setShowViewSelectedChildren(show) -> self

		This method changes the way that view selected works. By default, view selected with show all of the children of the objects in the view selected set. If False is passed to this method, then only the obejcts in the view selected set and their shapes will be drawn.

		* show (bool) - True if all of the children of view selected objects should be displayed. True is the default behavior for view selected."""
	def setUserDefinedColor(self,index:int,color:om.MColor)->Self:
		"""setUserDefinedColor(index, color) -> self

		Sets the user defined color at the given index.  Valid indices range between zero and the number of user defined colors.
		Returns an index into the application's color table

		* index (int) - index into the user defined color
		* color (MColor) - color to set to"""
	def setViewSelectedPrefix(self,prefix:str)->Self:
		"""setViewSelectedPrefix(prefix) -> self

		Sets the prefix for the camera name as displayed in the heads up display when view selected is enabled. The prefix is concatenated with the camera name.
		The default value is "isolate: "

		* prefix (string) - The prefix to use."""
	def showObjectFilterNameInHUD(self)->bool:
		"""showObjectFilterNameInHUD() -> bool

		Returns whether the object filter UI name is shown in the heads up display when an object filter is active."""
	def showViewSelectedChildren(self)->bool:
		"""showViewSelectedChildren() -> bool

		Returns turn if view selected shows all of the children of the obejcts that are flagged for view selected."""
	@staticmethod
	def templateColor()->om.MColor:
		"""templateColor() -> MColor

		Returns the value of the template color."""
	def textureMode(self)->bool:
		"""textureMode() -> bool

		Tells if this M3dView is in texture mode."""
	def twoSidedLighting(self)->bool:
		"""twoSidedLighting() -> bool

		Return True if the Two-sided lighting mode is enabled."""
	def updateViewingParameters(self)->Self:
		"""updateViewingParameters() -> self

		This method tells the camera to set the view's transformation matrix."""
	def userDefinedColorIndex(self,index:int)->int:
		"""userDefinedColorIndex(index) -> int

		Returns the index for the given user-defined color.  Valid values for the index argument range between zero and the number of user-defined colors minus one.

		The index returned gives the location of the specified color inside the active and dormant color tables (the index is the same in both tables).

		* index (int) - Index into user-defined colors"""
	def usingDefaultMaterial(self)->bool:
		"""usingDefaultMaterial() -> bool

		Returns True if the view is currently displaying objects using the default material."""
	def usingMipmappedTextures(self)->bool:
		"""usingMipmappedTextures() -> bool

		Returns if the view is using mipmapped texture display."""
	def viewSelectedPrefix(self)->str:
		"""viewSelectedPrefix() -> string

		Returns the prefix used when displaying the camera name in the heads up display when view selected in on"""
	def viewToObjectSpace(self,x_pos:int,y_pos:int,localMatrixInverse:om.MMatrix,oPt:Any,oVector:Any)->Self:
		"""viewToObjectSpace(x_pos, y_pos, localMatrixInverse, oPt, oVector) -> self

		Takes a point in port coordinates and returns a corresponding ray in object coordinates.

		* x_pos (int) - the x position of the point in port coordinates
		* y_pos (int) - the y position of the point in port coordinates
		* localMatrixInverse (MMatrix) - the inclusive matrix inverse of the object in question
		* oPt [OUT] (MPoint) - the source of the ray in object space
		* oVector [OUT] (MVector) - the direction of the ray in object space"""
	@overload
	def viewToWorld(self,x_pos:int,y_pos:int,worldPt:Any,worldVector:Any)->Self:
		"""viewToWorld(x_pos, y_pos, worldPt, worldVector) -> self
		viewToWorld(x_pos, y_pos, nearClipPt, farClipPt) -> self

		Takes a point in port coordinates and returns a corresponding ray in world coordinates.

		* x_pos (int) - the x position of the point in port coordinates
		* y_pos (int) - the y position of the point in port coordinates
		* worldPt [OUT] (MPoint) - the source of the ray
		* worldVector [OUT] (MVector) - the direction of the ray

		Or
		Takes a point in port coordinates and returns a point on the near and far clipping planes.

		* x_pos (int) - the x position of the point in port coordinates
		* y_pos (int) - the y position of the point in port coordinates
		* nearClipPt [OUT] (MPoint) - point on near clipping plane
		* farClipPt [OUT] (MPoint) - point on far clipping plane"""
	@overload
	def viewToWorld(self,x_pos:int,y_pos:int,nearClipPt:Any,farClipPt:Any)->Self:
		"""viewToWorld(x_pos, y_pos, worldPt, worldVector) -> self
		viewToWorld(x_pos, y_pos, nearClipPt, farClipPt) -> self

		Takes a point in port coordinates and returns a corresponding ray in world coordinates.

		* x_pos (int) - the x position of the point in port coordinates
		* y_pos (int) - the y position of the point in port coordinates
		* worldPt [OUT] (MPoint) - the source of the ray
		* worldVector [OUT] (MVector) - the direction of the ray

		Or
		Takes a point in port coordinates and returns a point on the near and far clipping planes.

		* x_pos (int) - the x position of the point in port coordinates
		* y_pos (int) - the y position of the point in port coordinates
		* nearClipPt [OUT] (MPoint) - point on near clipping plane
		* farClipPt [OUT] (MPoint) - point on far clipping plane"""
	def viewport(self)->list[int]:
		"""viewport() -> [int, int, int, int]

		Get the current viewport dimensions."""
	def widget(self)->int:
		"""widget() -> long

		Returns a long containing a C++ 'void' pointer which points to the view's Qt widget."""
	def window(self)->int:
		"""window() -> long

		Returns a long containing a C++ 'void' pointer which points to the native window for this view."""
	def wireframeOnShaded(self)->bool:
		"""wireframeOnShaded() -> bool

		Return whether we draw wireframe in shaded mode."""
	def wireframeOnlyInShadedMode(self)->bool:
		"""wireframeOnlyInShadedMode() -> bool

		Return whether we are in shaded mode, but that only non shaded drawing should occur (wireframe).

		In general it will return True only when the current renderer is "hwRender_OpenGL_Renderer". See the M3dView.rendererString() method for more details."""
	def worldToView(self,worldPt:om.MPoint)->list[int|bool]:
		"""worldToView(worldPt) -> [int, int, bool]

		Converts a point in world space to port space.
		Returns the x and y coordinates of the world point in port space and if the point is not clipped.

		* worldPt (MPoint) - the point to world space"""
	def writeColorBuffer(self,image:om.MImage,x:int=0,y:int=0)->Self:
		"""(Deprecated: Please use MHWRender::MQuadRender operation inside MHWRender::MRenderOverride instead.) writeColorBuffer(image, x=0, y=0) -> self

		Overwrite the RGB values for the frame buffer for a given view.
		Expected input is a block of RGBA, such that each channel is one byte in size.

		* image (MImage) - The image containing the block of pixels to write
		* x (int) - The location in screen space of the lower left corner (X) of the image to write. The default value is 0.
		* y (int) - The location in screen space of the lower left corner (Y) of the image to write. The default value is 0."""
	def xray(self)->bool:
		"""xray() -> bool

		Return True if the X-Ray mode is enabled."""
	def xrayJoints(self)->bool:
		"""xrayJoints() -> bool

		Return True if the X-Ray Joints mode is enabled."""
	def viewIsFiltered(self)->bool:
		"""viewIsFiltered() -> bool

		Returns True if the view is filtered."""
	def filteredObjectList(self)->om.MSelectionList:
		"""filteredObjectList() -> MSelectionList

		Returns a selection list containing all of the objects that remain after filtering is applied to the view."""
class MCursor:
	"""Manipulate Cursors."""
	__hash__:None=None
	kDefaultCursor:MCursor
	kCrossHairCursor:MCursor
	kDoubleCrossHairCursor:MCursor
	kEditCursor:MCursor
	kPencilCursor:MCursor
	kHandCursor:MCursor
	def __lt__(self,other)->bool:
		"""Return self<value."""
	def __le__(self,other)->bool:
		"""Return self<=value."""
	def __eq__(self,other)->bool:
		"""Return self==value."""
	def __ne__(self,other)->bool:
		"""Return self!=value."""
	def __gt__(self,other)->bool:
		"""Return self>value."""
	def __ge__(self,other)->bool:
		"""Return self>=value."""
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
class MDrawData:
	"""The MDrawData class holds geometry specific information for user defined shapes which maya does not intrinsicly know about."""
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def geometry(self)->int:
		"""geometry() -> long

		Returns a long containing a C++ 'void' pointer which points to the geometry associated with this draw data object.
		The geometry is set using the getDrawData method of MPxSurfaceShapeUI."""
class MDrawInfo:
	"""This class is used by the getDrawRequests method of MPxSurfaceShapeUI to specify the current object drawing state for a user defined shape."""
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def canDrawComponent(self,isDisplayOn:bool,compMask:Any)->bool:
		"""canDrawComponent(isDisplayOn, compMask) -> bool

		Convenience method to test if components specified by the given mask can be drawn.

		* isDisplayOn (bool) - component display is on
		* mask (MSelectionMask) - component mask to test"""
	def completelyInside(self)->bool:
		"""completelyInside() -> bool

		Returns True if the object being drawn is inside the viewing frustum."""
	def displayStatus(self)->int:
		"""displayStatus() -> int

		Returns the status of the object to draw.
		See M3dView.displayStatus() for a list of status."""
	def displayStyle(self)->int:
		"""displayStyle() -> int

		Returns the display appearance.
		See M3dView.displayStyle() for a list of styles."""
	def getPrototype(self,drawHandler:MPxSurfaceShapeUI)->MDrawRequest:
		"""getPrototype(drawHandler) -> MDrawRequest

		This method creates a draw request based on the current draw state.

		The draw request is placed onto maya's drawing queue (MDrawRequestQueue) where it can be processed in turn. The drawHandler argument is the shape that will be doing the drawing which is the object calling this function.

		* drawHandler (MPxSurfaceShapeUI) - the ui object that is doing the drawing"""
	def inSelect(self)->bool:
		"""inSelect() -> bool

		Returns True during any interactive refresh, as when user is interacting with the scene in any way including camera changes, object or component TRS changes, etc. Use userChangingViewContext for determining whether user is changing the view using view context tools such as tumble, dolly or track."""
	def inUserInteraction(self)->bool:
		"""inUserInteraction() -> bool

		Returns True during any interactive refresh, as when user is changing the view using view context tools such as tumble, dolly or track.  Useful for changing drawing mode to something simpler to speed up interaction re-draw.  Use inUserInteraction for determining whether user is interacting with the scene in any way."""
	def inclusiveMatrix(self)->om.MMatrix:
		"""inclusiveMatrix() -> MMatrix

		Returns the world space inclusive matrix."""
	def multiPath(self)->om.MDagPath:
		"""multiPath() -> MDagPath

		Returns the path to the object to be drawn."""
	def objectDisplayStatus(self,displayObj:int)->bool:
		"""objectDisplayStatus(displayObj) -> bool

		Determines whether the specified objects are allowed to be displayed.

		* displayObj (int) - display object mask. See M3dView.objectDisplay() for a list of valid masks."""
	def pluginObjectDisplayStatus(self,pluginDisplayFilter:str)->bool:
		"""pluginObjectDisplayStatus(pluginDisplayFilter) -> bool

		Determines whether the specified plugin object is allowed to be displayed.

		* pluginDisplayFilter (string) - The name of the plugin display filter which is registered by pluginDisplayFilter command."""
	def projectionMatrix(self)->om.MMatrix:
		"""projectionMatrix() -> MMatrix

		Returns the camera*projection matrix."""
	def setMultiPath(self,path:om.MDagPath)->Self:
		"""setMultiPath(path) -> self

		Sets the path of the object to be drawn.

		* path (MDagPath) - the path of the object to be drawn"""
	def userChangingViewContext(self)->bool:
		"""userChangingViewContext() -> bool

		Returns True during any interactive refresh, as when user is interacting with the scene in any way including camera changes, object or component TRS changes, etc. Use userChangingViewContext for determining whether user is changing the view using view context tools such as tumble, dolly or track."""
	def view(self)->M3dView:
		"""view() -> M3dView

		Returns the view that the drawing will take place."""
class MDrawProperties:
	"""Draw properties"""
	@property
	def color(self)->Any:
		"""color"""
	@color.setter
	def color(self,value:Any)->None:...
	@property
	def lineWidth(self)->Any:
		"""line width"""
	@lineWidth.setter
	def lineWidth(self,value:Any)->None:...
	@property
	def lineStyle(self)->Any:
		"""line style"""
	@lineStyle.setter
	def lineStyle(self,value:Any)->None:...
	@property
	def pointSize(self)->Any:
		"""point size"""
	@pointSize.setter
	def pointSize(self,value:Any)->None:...
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
class MDrawRequest:
	"""This class encapsulates all the information needed to fulfill a request to draw an object or part of an object.
	This class is used by the draw methods of MPxSurfaceShapeUI derived objects."""
	@property
	def view(self)->Any:
		"""The view where drawing will be done."""
	@view.setter
	def view(self,value:Any)->None:...
	@property
	def multiPath(self)->Any:
		"""The path to the object to be drawn."""
	@multiPath.setter
	def multiPath(self,value:Any)->None:...
	@property
	def component(self)->Any:
		"""An optional component. If set draw the components that are specified, otherwise draw all components of this type for the object."""
	@component.setter
	def component(self,value:Any)->None:...
	@property
	def drawData(self)->Any:
		"""The object specific draw data."""
	@drawData.setter
	def drawData(self,value:Any)->None:...
	@property
	def displayStatus(self)->Any:
		"""The state of object (active, dormant, etc.).
		See M3dView.displayStatus() for a list of display status."""
	@displayStatus.setter
	def displayStatus(self,value:Any)->None:...
	@property
	def displayCulling(self)->Any:
		"""The state of the culling flag for the object."""
	@displayCulling.setter
	def displayCulling(self,value:Any)->None:...
	@property
	def displayCullOpposite(self)->Any:
		"""The state of the opposite culling flag for the object."""
	@displayCullOpposite.setter
	def displayCullOpposite(self,value:Any)->None:...
	@property
	def displayStyle(self)->Any:
		"""How the object should be drawn (wireframe, shaded, etc.).
		See M3dView.displayStyle() for a list of display styles."""
	@displayStyle.setter
	def displayStyle(self,value:Any)->None:...
	@property
	def color(self)->Any:
		"""The RGBA wireframe display color."""
	@color.setter
	def color(self,value:Any)->None:...
	@property
	def material(self)->Any:
		"""The shaded material."""
	@material.setter
	def material(self,value:Any)->None:...
	@property
	def isTransparent(self)->Any:
		"""The transparency state of the object."""
	@isTransparent.setter
	def isTransparent(self,value:Any)->None:...
	@property
	def drawLast(self)->Any:
		"""The order in which this object will be drawn."""
	@drawLast.setter
	def drawLast(self,value:Any)->None:...
	@property
	def token(self)->Any:
		"""The user-defined draw token for this request.
		The token is used to identify a particular part of an object to draw. It is also used to distinguish draw requests generated by derived UI objects from those generated by base classes.
		It some cases, it provides a way of indicating that a component should be displayed without creating a component MObject."""
	@token.setter
	def token(self,value:Any)->None:...
	@property
	def matrix(self)->Any:
		"""The draw matrix."""
	@matrix.setter
	def matrix(self,value:Any)->None:...
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def planeColor(self,table:int)->int:
		"""planeColor(table) -> int

		Get which color is used for the specified color table.

		* table (int) - color table

		See M3dView.colorAtIndex() for a list of color tables."""
	def setPlaneColor(self,value:int,table:int)->Self:
		"""setPlaneColor(value, table) -> self

		Set which color to use for the specified color table.

		* value (int) - index into the color table
		* table (int) - color table

		See M3dView.colorAtIndex() for a list of color tables."""
class MEvent:
	"""Query interactive system events."""
	@property
	def position(self)->Any:
		"""The location of the event."""
	@position.setter
	def position(self,value:Any)->None:...
	@property
	def modifiers(self)->Any:
		"""The state of the modifiers."""
	@modifiers.setter
	def modifiers(self,value:Any)->None:...
	shiftKey:int=1
	controlKey:int=4
	kLeftMouse:int=64
	kMiddleMouse:int=128
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def getWindowPosition(self)->tuple[float,float]:
		"""getWindowPosition() -> (x, y)

		This routine is used by responders to query the position of the
		pointer when the event occurred.  It is given in screen co-ordinates.


		Returns a tuple containing the x and y position of the event."""
	def mouseButton(self)->int:
		"""mouseButton() -> mouseButtonType

		Get the mouse button of the last event.


		Returns the mouse button from last event."""
	def isModifierKeyRelease(self)->bool:
		"""isModifierKeyRelease() -> bool

		Was a modifier key released.


		Returns True if a modifier key was released, False otherwise."""
	def isModifierNone(self)->bool:
		"""isModifierNone() -> bool

		Determines if there are any modifiers for this event.


		Returns True if there are modifiers for this event, False otherwise."""
	def isModifierShift(self)->bool:
		"""isModifierShift() -> bool

		Return the state of the shift key.


		Returns True if the shift key was pressed at the time the event was triggered, False otherwise."""
	def isModifierControl(self)->bool:
		"""isModifierControl() -> bool

		Return the state of the control key.


		Returns True if the control key was pressed at the time the event was triggered, False otherwise."""
	def isModifierLeftMouseButton(self)->bool:
		"""isModifierLeftMouseButton() -> bool

		Return the state of the left mouse button.


		This method is only valid when called in the hold event for
		another mouse press.


		Returns True if the left mouse button was pressed at the time the event was triggered, False otherwise."""
	def isModifierMiddleMouseButton(self)->bool:
		"""isModifierMiddleMouseButton() -> bool

		Return the state of the middle mouse button.


		This method is only valid when called in the hold event for
		another mouse press.


		Returns True if the left mouse button was pressed at the time the event was triggered, False otherwise."""
class MFnCircleSweepManip(MFnManip3D):
	"""The CircleSweepManip allows the user to manipulate a point constrained to move around a circle, in order to specify a sweep angle. This manipulator generates a single floating point value corresponding to the sweep angle."""
	@property
	def startPoint(self)->Any:
		"""The start point of the CircleSweepManip."""
	@startPoint.setter
	def startPoint(self,value:Any)->None:...
	@property
	def endPoint(self)->Any:
		"""The end point of the CircleSweepManip."""
	@endPoint.setter
	def endPoint(self,value:Any)->None:...
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def angleIndex(self)->int:
		"""angleIndex() -> int

		Returns the index for the angle of CircleSweepManip. The data type corresponding to this index is a double."""
	def axisIndex(self)->int:
		"""axisIndex() -> int

		Returns the index for the axis of CircleSweepManip. The data type corresponding to this index is MFnNumericData.k3Double."""
	def centerIndex(self)->int:
		"""centerIndex() -> int

		Returns the index for the center of the CircleSweepManip. The data type corresponding to this index is MFnNumericData.k3Double."""
	def connectToAnglePlug(self,anglePlug:om.MPlug)->Self:
		"""connectToAnglePlug(anglePlug) -> self

		Connect to the angle plug. The data type corresponding to the anglePlug is a double. (Note that MFnUnitAttribute.kAngle is used to specify an angle attribute.)

		* anglePlug (MPlug) - the angle plug"""
	def create(self,manipName:str|None=None,angleName:str|None=None)->om.MObject:
		"""create(manipName=None, angleName=None) -> MObject

		Creates a new CircleSweepManip.
		This function set's object is set to be the new manipulator.

		This method should only be used to create a non-composite CircleSweepManip.

		The name that appears in the feedback line is specified by the angleName argument.

		* manipName (string) - Name of the manip for UI purposes.
		* angleName (string) - Label for the angle value which appears in the feedback line."""
	def endCircleIndex(self)->int:
		"""endCircleIndex() -> int

		Returns the index for the end of the circle of CircleSweepManip. The data type corresponding to this index is a double."""
	def setAngle(self,angle:om.MAngle)->Self:
		"""setAngle(angle) -> self

		Sets the angle of the CircleSweepManip.

		* angle (MAngle) - the angle of the CircleSweepManip"""
	def setCenterPoint(self,centerPoint:om.MPoint)->Self:
		"""setCenterPoint(centerPoint) -> self

		Sets the center point of the CircleSweepManip.

		* centerPoint (MPoint) - the center point of the CircleSweepManip"""
	def setDrawAsArc(self,state:bool)->Self:
		"""setDrawAsArc(state) -> self

		Sets whether or not to draw as arc.

		* state (bool) - whether or not to draw as arc"""
	def setNormal(self,normal:om.MVector)->Self:
		"""setNormal(normal) -> self

		Sets the normal of the CircleSweepManip.

		* normal (MVector) - the normal of the CircleSweepManip"""
	def setRadius(self,radius:float)->Self:
		"""setRadius(radius) -> self

		Sets the radius of the CircleSweepManip.

		* radius (float) - the radius of the CircleSweepManip"""
	def startCircleIndex(self)->int:
		"""startCircleIndex() -> int

		Returns the index for the start of the circle of CircleSweepManip. The data type corresponding to this index is a double."""
class MFnCurveSegmentManip(MFnManip3D):
	"""The CurveSegmentManip allows the user to manipulate two points on a curve, in order to specify a curve segment. This manipulator generates two floating point values, which correspond to the parameters of the start and end of the curve segment."""
	@property
	def startParameter(self)->Any:
		"""The start parameter of the CurveSegmentManip."""
	@startParameter.setter
	def startParameter(self,value:Any)->None:...
	@property
	def endParameter(self)->Any:
		"""The end parameter of the CurveSegmentManip."""
	@endParameter.setter
	def endParameter(self,value:Any)->None:...
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def connectToCurvePlug(self,curvePlug:om.MPlug)->Self:
		"""connectToCurvePlug(curvePlug) -> self

		Connect to the curve plug. The data type corresponding to the curvePlug is MFnData.kNurbsCurve.

		* curvePlug (MPlug) - the curve plug"""
	def connectToEndParamPlug(self,endParamPlug:om.MPlug)->Self:
		"""connectToEndParamPlug(endParamPlug) -> self

		Connect to the endParam plug. The data type corresponding to the endParamPlug is a double.

		* endParamPlug (MPlug) - the endParam plug"""
	def connectToStartParamPlug(self,startParamPlug:om.MPlug)->Self:
		"""connectToStartParamPlug(startParamPlug) -> self

		Connect to the startParam plug. The data type corresponding to the startParamPlug is a double.

		* startParamPlug (MPlug) - the startParam plug"""
	def create(self,manipName:str|None=None,startParamName:str|None=None,endParamName:str|None=None)->om.MObject:
		"""create(manipName=None, startParamName=None, endParamName=None) -> MObject

		Creates a new CurveSegmentManip.
		This function set's object is set to be the new manipulator.

		This method should only be used to create a non-composite CurveSegmentManip.

		The names that appears in the feedback line are specified by the startParamName and endParamName arguments.

		* manipName (string) - Name of the manip for UI purposes.
		* startParamName (string) - Label for the startParam value which appears in the feedback line.
		* endParamName (string) - Label for the endParam value which appears in the feedback line."""
	def curveIndex(self)->int:
		"""curveIndex() -> int

		Returns the index of the curve. The data type corresponding to this index is MFnData.kNurbsCurve."""
	def endParamIndex(self)->int:
		"""endParamIndex() -> int

		Returns the index of the end parameter of the CurveSegmentManip. The data type corresponding this index is a double."""
	def startParamIndex(self)->int:
		"""startParamIndex() -> int

		Returns the index of the start parameter of the CurveSegmentManip. The data type corresponding to this index is a double."""
class MFnDirectionManip(MFnManip3D):
	"""The DirectionManip allows the user to specify a direction, as defined by the vector from the start point to the manipulator position."""
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def connectToDirectionPlug(self,directionPlug:om.MPlug)->Self:
		"""connectToDirectionPlug(directionPlug) -> self

		Connect to the direction plug. The data type corresponding to the directionPlug is MFnNumericData.k3Double.

		* directionPlug (MPlug) - the direction plug"""
	def create(self,manipName:str|None=None,directionName:str|None=None)->om.MObject:
		"""create(manipName=None, directionName=None) -> MObject

		Creates a new DirectionManip.
		This function set's object is set to be the new manipulator.

		This method should only be used to create a non-composite DirectionManip.

		The name that appears in the feedback line is specified by the directionName argument.

		* manipName (string) - Name of the manip for UI purposes.
		* directionName (string) - Label for the direction value which appears in the feedback line."""
	def directionIndex(self)->int:
		"""directionIndex() -> int

		Returns the index of the direction. The data type corresponding to this index is MFnNumericData.k3Double."""
	def endPointIndex(self)->int:
		"""endPointIndex() -> int

		Returns the index of the end point of the DirectionManip. The data type corresponding to this index is MFnNumericData.k3Double."""
	def setDirection(self,direction:om.MVector)->Self:
		"""setDirection(direction) -> self

		Sets the direction of the DirectionManip.

		* direction (MVector) - the direction of the DirectionManip"""
	def setDrawStart(self,bool:bool)->Self:
		"""setDrawStart(bool) -> self

		Sets whether or not to draw the start of the DirectionManip.
		The start of the DirectionManip is indicated by a grey dot.
		By default the start is not drawn."""
	def setNormalizeDirection(self,bool:bool)->Self:
		"""setNormalizeDirection(bool) -> self

		Sets whether or not to the direction should be normalized.
		By default the direction is normalized."""
	def setStartPoint(self,startPoint:om.MPoint)->Self:
		"""setStartPoint(startPoint) -> self

		Sets the start point of the DirectionManip.

		* startPoint (MPoint) - the start point of the DirectionManip"""
	def startPointIndex(self)->int:
		"""startPointIndex() -> int

		Returns the index of the start point of the DirectionManip. The data type corresponding to this index is MFnNumericData.k3Double."""
class MFnDiscManip(MFnManip3D):
	"""The DiscManip allows the user to rotate a disc in order to specify a rotation about an axis. This manipulator generates a single floating point value corresponding to the rotation."""
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def angleIndex(self)->int:
		"""angleIndex() -> int

		Returns the index of the angle. The data type corresponding to this index is a double."""
	def axisIndex(self)->int:
		"""axisIndex() -> int

		Returns the index of the axis of the DiscManip. The data type corresponding to this index is MFnNumericData.k3Double."""
	def centerIndex(self)->int:
		"""centerIndex() -> int

		Returns the index of the center of the DiscManip. The data type corresponding to this index is MFnNumericData.k3Double."""
	def connectToAnglePlug(self,directionPlug:Any)->Self:
		"""connectToAnglePlug(directionPlug) -> self

		Connect to the angle plug. The data type corresponding to the anglePlug is a double. (Note that MFnUnitAttribute.kAngle is used to specify an angle attribute.)

		* anglePlug (MPlug) - the angle plug"""
	def create(self,manipName:str|None=None,angleName:str|None=None)->om.MObject:
		"""create(manipName=None, angleName=None) -> MObject

		Creates a new DiscManip.
		This function set's object is set to be the new manipulator.

		This method should only be used to create a non-composite DiscManip.

		The name that appears in the feedback line is specified by the angleName argument.

		* manipName (string) - Name of the manip for UI purposes.
		* angleName (string) - Label for the angle value which appears in the feedback line."""
	def setAngle(self,angle:om.MAngle)->Self:
		"""setAngle(angle) -> self

		Sets the angle of the DiscManip.

		* angle (MAngle) - the angle of the DiscManip"""
	def setCenterPoint(self,centerPoint:om.MPoint)->Self:
		"""setCenterPoint(centerPoint) -> self

		Sets the center point of the DiscManip.

		* centerPoint (MPoint) - the center point of the DiscManip"""
	def setNormal(self,normal:om.MVector)->Self:
		"""setNormal(normal) -> self

		Sets the normal of the DiscManip.

		* normal (MVector) - the normal of the DiscManip"""
	def setRadius(self,radius:float)->Self:
		"""setRadius(radius) -> self

		Sets the radius of the DiscManip.

		* radius (float) - the radius of the DiscManip"""
class MFnDistanceManip(MFnManip3D):
	"""The DistanceManip allows the user to manipulate a point that is constrained to move along a line. This manipulator generates a single floating point value. Scaling factors can be used to determine how the manipulator appears when it is drawn."""
	@property
	def isDrawStartOn(self)->Any:
		"""Whether or not the start of the DistanceManip is being drawn.
		By default the start is not drawn."""
	@isDrawStartOn.setter
	def isDrawStartOn(self,value:Any)->None:...
	@property
	def isDrawLineOn(self)->Any:
		"""Whether or not to draw a line from the start to the end of the DistanceManip.
		By default the line is drawn."""
	@isDrawLineOn.setter
	def isDrawLineOn(self,value:Any)->None:...
	@property
	def scalingFactor(self)->Any:
		"""The scaling factor is used to determine how int the DistanceManip appears when it is drawn.
		The default scaling factor is 1.0."""
	@scalingFactor.setter
	def scalingFactor(self,value:Any)->None:...
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def connectToDistancePlug(self,directionPlug:Any)->Self:
		"""connectToDistancePlug(directionPlug) -> self

		Connect to the distance plug. The data type corresponding to the distancePlug is a double. (Note that MFnUnitAttribute.kDistance is used to specify a distance attribute.)

		* distancePlug (MPlug) - the distance plug"""
	def create(self,manipName:str|None=None,distanceName:str|None=None)->om.MObject:
		"""create(manipName=None, distanceName=None) -> MObject

		Creates a new DistanceManip.
		This function set's object is set to be the new manipulator.

		This method should only be used to create a non-composite DistanceManip.

		The name that appears in the feedback line is specified by the distanceName argument.

		* manipName (string) - Name of the manip for UI purposes.
		* distanceName (string) - Label for the distance value which appears in the feedback line."""
	def currentPointIndex(self)->int:
		"""currentPointIndex() -> int

		Returns the index of the current point of the DistanceManip. The data type corresponding to this index is MFnNumericData.k3Double."""
	def directionIndex(self)->int:
		"""directionIndex() -> int

		Returns the index of the direction. The data type corresponding to this index is MFnNumericData.k3Double."""
	def distanceIndex(self)->int:
		"""distanceIndex() -> int

		Returns the index of the distance. The data type corresponding to this index is a double."""
	def setDirection(self,direction:om.MVector)->Self:
		"""setDirection(direction) -> self

		Sets the direction of the DistanceManip.

		* direction (MVector) - the direction of the DistanceManip"""
	def setStartPoint(self,startPoint:om.MPoint)->Self:
		"""setStartPoint(startPoint) -> self

		Sets the start point of the DistanceManip.

		* startPoint (MPoint) - the start point of the DistanceManip"""
	def startPointIndex(self)->int:
		"""startPointIndex() -> int

		Returns the index of the start point of the DistanceManip. The data type corresponding to this index is MFnNumericData.k3Double."""
class MFnFreePointTriadManip(MFnManip3D):
	"""The FreePointTriadManip provides a moveable point, which can be moved anywhere, and has axes for constrained x, y, and z movement and obeys grid snapping, point snapping, and curve snapping. The FreePointTriadManip generates the 3D position of the moveable point. It is useful for specifying the position of an object in space.

	Note that only the MFnNumericData::k3Double data type is supportedwhen connecting to a pointPlug via connectToPointPlug."""
	@property
	def isDrawAxesOn(self)->Any:
		"""Whether or not the axes of the FreePointTriadManip are being drawn. By default the axes are drawn."""
	@isDrawAxesOn.setter
	def isDrawAxesOn(self,value:Any)->None:...
	@property
	def isSnapModeOn(self)->Any:
		"""Whether or not the FreePointTriadManip is in snap mode."""
	@isSnapModeOn.setter
	def isSnapModeOn(self,value:Any)->None:...
	@property
	def isKeyframeAllOn(self)->Any:
		"""Whether or not the FreePointTriadManip is in keyframeAll mode."""
	@isKeyframeAllOn.setter
	def isKeyframeAllOn(self,value:Any)->None:...
	kYZPlane:int=0
	kXZPlane:int=1
	kXYPlane:int=2
	kViewPlane:int=3
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def connectToPointPlug(self,pointPlug:om.MPlug)->Self:
		"""connectToPointPlug(pointPlug) -> self

		Connect to the point plug. The data type corresponding to the pointPlug is MFnNumericData.k3Double.

		* pointPlug (MPlug) - the point plug"""
	def create(self,manipName:str|None=None,pointName:str|None=None)->om.MObject:
		"""create(manipName=None, pointName=None) -> MObject

		Creates a new FreePointTriadManip.
		This function set's object is set to be the new manipulator.

		This method should only be used to create a non-composite FreePointTriadManip.

		The name that appears in the feedback line is specified by the pointName argument.

		* manipName (string) - Name of the manip for UI purposes.
		* pointName (string) - Label for the position value which appears in the feedback line."""
	def pointIndex(self)->int:
		"""pointIndex() -> int

		Returns the index of the point of the FreePointTriadManip. The data type corresponding to this index is MFnNumericData.k3Double."""
	def setDirection(self,direction:om.MVector)->Self:
		"""setDirection(direction) -> self

		Sets the orientation of the FreePointTriadManip.

		* direction (MVector) - the new direction for freePointTriadManip."""
	def setDrawArrowHead(self,state:bool)->Self:
		"""setDrawArrowHead(state) -> self

		Sets whether or not drawArrowHead is on.

		* state (bool) - whether or not drawArrowHead is on"""
	def setGlobalTriadPlane(self,whichPlane:int)->Self:
		"""setGlobalTriadPlane(whichPlane) -> self

		Sets which plane to use as the global triad plane. The global triad plane does not change until the context switches.

		* whichPlane (int) - which plane to use as the global triad plane

		Valid plane values:
		  kYZPlane       Y-Z Plane
		  kXZPlane       X-Z Plane
		  kXYPlane       X-Y Plane
		  kViewPlane     View Plane"""
	def setPoint(self,pointValue:om.MPoint)->Self:
		"""setPoint(pointValue) -> self

		Set the point manipulator value to the given vector.  This method can be called in the MPxManipContainer.connectToDependNode() method to set the initial position for the manipulator.

		* pointValue (MPoint) - The new value of the point manipValue"""
class MFnManip3D(om.MFnTransform):
	"""MFnManip3D allows the creation and manipulation of 3D manipulators."""
	@property
	def isVisible(self)->Any:
		"""Whether or not the manipulator is visible."""
	@isVisible.setter
	def isVisible(self,value:Any)->None:...
	@property
	def manipScale(self)->Any:
		"""The manipulator scale."""
	@manipScale.setter
	def manipScale(self,value:Any)->None:...
	@property
	def isOptimizePlaybackOn(self)->Any:
		"""Whether or not optimize playback is on."""
	@isOptimizePlaybackOn.setter
	def isOptimizePlaybackOn(self,value:Any)->None:...
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	@staticmethod
	def deleteManipulator(manip:om.MObject)->None:
		"""deleteManipulator(manip) -> None

		Delete a manipulator.  This method should be used to delete manipulators that have been created using base manipulator create() methods.

		* manip (MObject) - the manipulator to be deleted"""
	@staticmethod
	def globalSize()->float:
		"""globalSize() -> float

		Returns the global manipulator size."""
	@staticmethod
	def handleSize()->float:
		"""handleSize() -> float

		Returns the manipulator handle size."""
	@staticmethod
	def lineSize()->float:
		"""lineSize() -> float

		Returns the manipulator line size."""
	def rotateXYZValue(self,valIndex:int)->om.MEulerRotation:
		"""rotateXYZValue(valIndex) -> MEulerRotation

		Gets the rotation for the active manipulator.

		* valIndex (int) - rotation index of the manipulator"""
	@staticmethod
	def drawPlaneHandles()->bool:
		"""drawPlaneHandles() -> bool

		This method returns the global option that says if the planar manipulator handles should be drawn or not.Setting this will affect the drawing of all manipulators that support the planar handles."""
	@staticmethod
	def setGlobalSize(float:float)->None:
		"""setGlobalSize(float) -> None

		Sets the global manipulator size."""
	@staticmethod
	def setHandleSize(float:float)->None:
		"""setHandleSize(float) -> None

		Sets the manipulator handle size."""
	@staticmethod
	def setLineSize(float:float)->None:
		"""setLineSize(float) -> None

		Sets the manipulator line size."""
	@staticmethod
	def setDrawPlaneHandles(bool:bool)->None:
		"""setDrawPlaneHandles(bool) -> None

		Sets the global option to display planar handles or not on supported manipulators."""
class MFnPointOnCurveManip(MFnManip3D):
	"""The PointOnCurveManip allows the user to manipulate a point constrained to move along a curve, in order to specify the "u" curve parameter value. This manipulator generates a single floating point value corresponding to the curve parameter.the sweep angle."""
	@property
	def isDrawCurveOn(self)->Any:
		"""Whether or not the curve is drawn."""
	@isDrawCurveOn.setter
	def isDrawCurveOn(self,value:Any)->None:...
	@property
	def parameter(self)->Any:
		"""The parameter of the PointOnCurveManip."""
	@parameter.setter
	def parameter(self,value:Any)->None:...
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def connectToCurvePlug(self,curvePlug:om.MPlug)->Self:
		"""connectToCurvePlug(curvePlug) -> self

		Connect to the curve plug. The data type corresponding to the curvePlug is MFnData::kNurbsCurve.

		* curvePlug (MPlug) - the curve plug"""
	def connectToParamPlug(self,paramPlug:om.MPlug)->Self:
		"""connectToParamPlug(paramPlug) -> self

		Connect to the param plug. The data type corresponding to the paramPlug is a double.

		* paramPlug (MPlug) - the param plug"""
	def create(self,manipName:str|None=None,paramName:str|None=None)->om.MObject:
		"""create(manipName=None, paramName=None) -> MObject

		Creates a new PointOnCurveManip.
		This function set's object is set to be the new manipulator.

		This method should only be used to create a non-composite PointOnCurveManip.

		The name that appears in the feedback line is specified by the paramName argument.

		* manipName (string) - Name of the manip for UI purposes.
		* paramName (string) - Label for the parameter value that appears in the feedback line."""
	def curveIndex(self)->int:
		"""curveIndex() -> int

		Returns the index of the curve. The data type corresponding to this index is MFnData::kNurbsCurve."""
	def curvePoint(self)->om.MPoint:
		"""curvePoint() -> MPoint

		Returns the curve point."""
	def paramIndex(self)->int:
		"""paramIndex() -> int

		Returns the index of the parameter of the PointOnCurveManip. The data type corresponding to this index is a double."""
class MFnPointOnSurfaceManip(MFnManip3D):
	"""The PointOnSurfaceManip allows the user to manipulate a point constrained to move along a surface, in order to specify the (u, v) surface parameter values. This manipulator generates two floating point values corresponding to the surface (u, v) parameters."""
	@property
	def uParam(self)->Any:
		"""The u parameter"""
	@uParam.setter
	def uParam(self,value:Any)->None:...
	@property
	def vParam(self)->Any:
		"""The v parameter"""
	@vParam.setter
	def vParam(self,value:Any)->None:...
	@property
	def isDrawSurfaceOn(self)->Any:
		"""Whether or not the surface is drawn."""
	@isDrawSurfaceOn.setter
	def isDrawSurfaceOn(self,value:Any)->None:...
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def connectToParamPlug(self,paramPlug:om.MPlug)->Self:
		"""connectToParamPlug(paramPlug) -> self

		Connect to the param plug. The data type corresponding to the paramPlug is MFnNumericData.k2Double.

		* paramPlug (MPlug) - the param plug"""
	def connectToSurfacePlug(self,surfacePlug:om.MPlug)->Self:
		"""connectToSurfacePlug(surfacePlug) -> self

		Connect to the surface plug. The data type corresponding to the surfacePlug is MFnData.kNurbsSurface.

		* surfacePlug (MPlug) - the surface plug"""
	def create(self,manipName:str|None=None,paramName:str|None=None)->om.MObject:
		"""create(manipName=None, paramName=None) -> MObject

		Creates a new PointOnSurfaceManip.
		This function set's object is set to be the new manipulator.

		This method should only be used to create a non-composite PointOnSurfaceManip.

		The name that appears in the feedback line is specified by the paramName argument.

		* manipName (string) - Name of the manip for UI purposes.
		* paramName (string) - Label for the parameter value which appears in the feedback line"""
	def paramIndex(self)->int:
		"""paramIndex() -> int

		Returns the index of the parameter of the PointOnSurfaceManip. The data type corresponding to this index is MFnNumericData.k2Double."""
	def setDrawArrows(self,state:bool)->Self:
		"""setDrawArrows(state) -> self

		Sets whether or not the arrows should be drawn.

		* state (bool) - whether or not the arrows should be drawn"""
	def surfaceIndex(self)->int:
		"""surfaceIndex() -> int

		Returns the index of the surface. The data type corresponding to this index is MFnData.kNurbsSurface."""
class MFnRotateManip(MFnManip3D):
	"""This class provides access to the built-in Maya rotate manipulator."""
	@property
	def isSnapModeOn(self)->Any:
		"""Whether or not the snap mode is on. When snap mode is on, rotation manip values will snap to the values within some increment apart."""
	@isSnapModeOn.setter
	def isSnapModeOn(self,value:Any)->None:...
	@property
	def snapIncrement(self)->Any:
		"""The snap increment is specified in degrees. Manipulator values will snap to the next rotation at an angle of snapIncrement from the original rotation.  Note that snap rotate does not apply to the trackball rotations (when dragging between the rotate discs)."""
	@snapIncrement.setter
	def snapIncrement(self,value:Any)->None:...
	@property
	def rotateMode(self)->Any:
		"""The mode for the rotation manipulator.  The manipulator mode controls the appearance of the manipulator when is it used.

		The following modes are supported for the rotation manipulator:

		* kObjectSpace In object space mode, the manipulator is displayed as three perpendicular manipulator discs, as well as a view disc enclosing the manipulator.  The manipulator will rotate whenever the manip value is changed.
		* kWorldSpace This mode forces the manipulator to display in the default orientation regardless of the manipulator value.  The manipulator is displayed the same as in object space mode, except it does not rotate when the manip value is changed.
		* kGimbal In gimbal mode, only the constrained axis rotation discs are allowed to be manipulated.  Gimbal mode treats the X,Y, and Z axis rotations as a sequence of operations on the default manipulator display.  First, the X rotation is applied.  Then, the Y rotation is applied, causing the X rotation disc to become transformed.  Finally, the Z rotation is applied, transforming both the X and Y rotation discs.  The Z rotation disc remains fixed during the operation.  No view disc can be manipulated in gimbal mode."""
	@rotateMode.setter
	def rotateMode(self,value:Any)->None:...
	kObjectSpace:int=0
	kWorldSpace:int=1
	kGimbal:int=2
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def connectToRotationCenterPlug(self,rotationCenterPlug:om.MPlug)->Self:
		"""connectToRotationCenterPlug(rotationCenterPlug) -> self

		Create a 1-1 association of the rotation center on the manipulator and the rotationCenterPlug parameter.  When both the rotation center is attached to a plug and the displayWithNode() method has been called, the manipulator will display with the node regardless of the connection made to the rotation center.

		The plug must have a data type of MFnNumericData.k3Double.

		* rotationCenterPlug (MPlug) - The plug to connect the rotation center to"""
	def connectToRotationPlug(self,rotationPlug:om.MPlug)->Self:
		"""connectToRotationPlug(rotationPlug) -> self

		Create a 1-1 connection from the rotation manipVal to the rotationPlug parameter.  Any changes to the rotation manipVal will be immediately reflected in the connected plug.  Connecting to the "rotation" plug on a transform node will produce similar behavior to the built-in rotation manipulator.

		The plug must have a data type of MFnNumericData.k3Double.

		* rotationPlug (MPlug) - The plug to connect the rotation value to"""
	def create(self,manipName:str|None=None,rotationName:str|None=None)->om.MObject:
		"""create(manipName=None, rotationName=None) -> MObject

		Creates a new RotateManip, and attaches this function set to the new manipulator.

		This method should only be used to create a non-composite manipulator, meaning that the manipulator is standalone and not part of a container.

		When the manipulator is being used, the feedback line will display a string including rotationName, indicating that this manipulator is in use.

		* manipName (string) - Name of the manip for UI purposes.
		* rotationName (string) - Label for the rotation value displayed in the feedback line."""
	def displayWithNode(self,node:om.MObject)->Self:
		"""displayWithNode(node) -> self

		Configures the manipulator to display with the node, causing the position of the manipulator to follow the position of the node whenever the node is moved.  The node must be a DAG object.

		* node (MObject) - The node the manipulator should display with"""
	def rotationCenterIndex(self)->int:
		"""rotationCenterIndex() -> int

		Returns the index of the rotation center for this manipulator.

		Note that the rotation center is only used for positioning the display of the manipulator, and has no effect on the rotation values generated by the manipulator."""
	def rotationIndex(self)->int:
		"""rotationIndex() -> int

		Returns the index of the rotation manipVal for the manipulator.  When plugToManip conversion functions are used to produce the rotation manipVal, the manipulator data must be of the type MFnNumericData.k3Double, with X,Y, and Z rotations given in radians.  This is easily accomplished by using the MEulerRotation class to manage the rotations."""
	def setInitialRotation(self,rotation:om.MEulerRotation)->Self:
		"""setInitialRotation(rotation) -> self

		Sets the initial rotation for the rotate manipulator.  Setting the initial rotation will prevent the manipulator from jumping back to the default rotation when there is already an existing rotation on the target plug.

		* rotation (MEulerRotation) - The initial rotation"""
	def setRotationCenter(self,rotationCenter:om.MPoint)->Self:
		"""setRotationCenter(rotationCenter) -> self

		Sets the position of the rotation center for the manipulator.

		The value set by this method is ignored if a plug has been connected to the rotationCenterPlug. This value is only relevant when there is no plug connection to rotationCenterPlug nor node associated with the manip (see connectToRotationCenterPlug and displayWithNode, respectively).

		Note that the rotation center is only used for positioning the display of the manipulator, and has no effect on the rotation values generated by the manipulator.

		* rotationCenter (MPoint) - The world space position of the rotation center."""
class MFnScaleManip(MFnManip3D):
	"""This class provides access to the built-in Maya scale manipulator."""
	@property
	def isSnapModeOn(self)->Any:
		"""Whether or not the snap mode is on."""
	@isSnapModeOn.setter
	def isSnapModeOn(self,value:Any)->None:...
	@property
	def snapIncrement(self)->Any:
		"""The snap increment is specified in the working	unit, and is the distance between snap points when dragging the scale handles."""
	@snapIncrement.setter
	def snapIncrement(self,value:Any)->None:...
	@property
	def orientation(self)->Any:
		"""The arbitrary orientation of the MFnScaleManip. This only has any effect when the orientation mode is set to kArbitraryOrientation."""
	@orientation.setter
	def orientation(self,value:Any)->None:...
	@property
	def orientationMode(self)->Any:
		"""When the manipulator's orientationMode is set to kArbitraryOrientation the manipulator will be oriented according to oritentation value. When the orientationMode is set to kDefaultOrientation the manipulator will be aligned with the world-space axes."""
	@orientationMode.setter
	def orientationMode(self,value:Any)->None:...
	kDefaultOrientation:int=0
	kArbitraryOrientation:int=1
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def connectToScaleCenterPlug(self,scaleCenterPlug:om.MPlug)->Self:
		"""connectToScaleCenterPlug(scaleCenterPlug) -> self

		Create a 1-1 association of the scale center on the manipulator and the scaleCenterPlug parameter.  When both the scale center is attached to a plug and the displayWithNode() method has been called, the manipulator will display with the node regardless of the connection made to the scale center.

		The plug must have a data type of MFnNumericData.k3Double.

		* scaleCenterPlug (MPlug) - The plug to connect the scale center to"""
	def connectToScalePlug(self,scalePlug:om.MPlug)->Self:
		"""connectToScalePlug(scalePlug) -> self

		Create a 1-1 connection from the scale manipVal to the scalePlug parameter.  Any changes to the scale manipVal will be immediately reflected in the connected plug.  Connecting to the "scale" plug on a transform node will produce similar behavior to the built-in scale manipulator.

		The plug must have a data type of MFnNumericData.k3Double.

		* scalePlug (MPlug) - The plug to connect the scale value to"""
	def create(self,manipName:str|None=None,scaleName:str|None=None)->om.MObject:
		"""create(manipName=None, scaleName=None) -> MObject

		Creates a new ScaleManip, and attaches this function set to the new manipulator.

		This method should only be used to create a non-composite manipulator, meaning that the manipulator is standalone and not part of a container.

		When the manipulator is being used, the feedback line will display a string including scaleName, indicating that this manipulator is in use.

		* manipName (string) - Name of the manip for UI purposes.
		* scaleName (string) - Label for the scale value displayed in the feedback line."""
	def displayWithNode(self,node:om.MObject)->Self:
		"""displayWithNode(node) -> self

		Configures the manipulator to display with the node, causing the position of the manipulator to follow the position of the node whenever the node is moved.  The node must be a DAG object.

		* node (MObject) - The node the manipulator should display with"""
	def scaleCenterIndex(self)->int:
		"""scaleCenterIndex() -> int

		Returns the index of the scale center manipVal for this manipulator.

		Note that the scale center is only used for display of the manipulator and has no effect on scale values produced by the manipulator."""
	def scaleIndex(self)->int:
		"""scaleIndex() -> int

		Returns the index of the scale manipVal for this manipulator."""
	def setInitialScale(self,scale:om.MVector)->Self:
		"""setInitialScale(scale) -> self

		Sets the initial scale for the scale manipulator.  Setting the initial scale will prevent the manipulator from jumping back to the default scale when there is already an existing scale on the target plug.

		* scale (MVector) - The initial scale"""
class MFnStateManip(MFnManip3D):
	"""The StateManip allows the user to switch between multiple states. It is drawn as a circle with a notch. Each click on the circle increments the value of the state (modulo the maximum number of states). This manipulator generates an integer value corresponding to the state of the manip."""
	@property
	def maxStates(self)->Any:
		"""The maximum number of states that the StateManip will have.
		The default number of maximum states is 4."""
	@maxStates.setter
	def maxStates(self,value:Any)->None:...
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def connectToStatePlug(self,statePlug:om.MPlug)->Self:
		"""connectToStatePlug(statePlug) -> self

		Connect to the state plug. The data type corresponding to the statePlug is a int integer.

		* statePlug (MPlug) - the state plug"""
	def create(self,manipName:str|None=None,stateName:str|None=None)->om.MObject:
		"""create(manipName=None, stateName=None) -> MObject

		Creates a new StateManip.
		This function set's object is set to be the new manipulator.

		This method should only be used to create a non-composite StateManip.

		The name that appears in the feedback line is specified by the stateName argument.

		* manipName (string) - Name of the manip for UI purposes.
		* stateName (string) - Label for the state value which appears in the feedback line."""
	def positionIndex(self)->int:
		"""positionIndex() -> int

		Returns the index of the position of the StateManip. The data type corresponding to this index is MFnNumericData.k3Double."""
	def setInitialState(self,initialState:int)->Self:
		"""setInitialState(initialState) -> self

		Sets the initial state of the StateManip.

		* initialState (int) - initial state of the StateManip"""
	def state(self)->int:
		"""state() -> int

		Returns the current state."""
	def stateIndex(self)->int:
		"""stateIndex() -> int

		Returns the index of the state. The data type corresponding to this index is a int integer."""
class MFnToggleManip(MFnManip3D):
	"""The ToggleManip allows the user to switch between two modes or some on/off state. It is drawn as a circle with or without a dot. When the mode is on, the dot is drawn in the circle; when the mode is off, the circle is drawn without the dot. This manipulator generates a boolean value corresponding to whether or not the mode is on or off."""
	@property
	def startPoint(self)->Any:
		"""The start point of the ToggleManip."""
	@startPoint.setter
	def startPoint(self,value:Any)->None:...
	@property
	def direction(self)->Any:
		"""The direction of the ToggleManip."""
	@direction.setter
	def direction(self,value:Any)->None:...
	@property
	def length(self)->Any:
		"""The length of the ToggleManip."""
	@length.setter
	def length(self,value:Any)->None:...
	@property
	def toggle(self)->Any:
		"""The toggle of the ToggleManip."""
	@toggle.setter
	def toggle(self,value:Any)->None:...
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def connectToTogglePlug(self,togglePlug:om.MPlug)->Self:
		"""connectToTogglePlug(togglePlug) -> self

		Connect to the toggle plug. The data type corresponding to the togglePlug is a boolean value.

		* togglePlug (MPlug) - the toggle plug"""
	def create(self,manipName:str|None=None,toggleName:str|None=None)->om.MObject:
		"""create(manipName=None, toggleName=None) -> MObject

		Creates a new ToggleManip.
		This function set's object is set to be the new manipulator.

		This method should only be used to create a non-composite ToggleManip.

		The name that appears in the feedback line is specified by the toggleName argument.

		* manipName (string) - Name of the manip for UI purposes.
		* toggleName (string) - Label for the toggle value which appears in the feedback line."""
	def directionIndex(self)->int:
		"""directionIndex() -> int

		Returns the index of the direction. The data type corresponding to this index is MFnNumericData.k3Double."""
	def lengthIndex(self)->int:
		"""lengthIndex() -> int

		Returns the index of the length of the ToggleManip. The data type corresponding to this index is a double."""
	def startPointIndex(self)->int:
		"""startPointIndex() -> int

		Returns the index of the start point of the ToggleManip. The data type corresponding to this index is MFnNumericData.k3Double."""
	def toggleIndex(self)->int:
		"""toggleIndex() -> int

		Returns the index of the toggle of the ToggleManip. The data type corresponding to this index is a boolean."""
class MHWShaderSwatchGenerator(omr.MSwatchRenderBase):
	"""Hardware shader swatch generator utility class."""
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	@staticmethod
	def createObj(obj:om.MObject,renderObj:om.MObject,res:Any)->omr.MSwatchRenderBase:
		"""createObj(obj, renderObj, res) -> MSwatchRenderBase

		Class constructor.
		Saves the Node object and image resolution as data members for future use.

		* obj (MObject) - The node object for which the swatch needs to be generated.
		* renderObj (MObject) - The node used to actually compute the swatch. In most situations, this can be the same as <b>obj</b>. This parameter can be used to request the computation of the swatch on another node, and display the swatch on the obj node.* resolution (int) - The expected resolution of the swatch image."""
	def doIteration(self)->bool:
		"""doIteration() -> bool

		Method called from the MSwatchRenderRegister for generation of swatch image. The doIteration function is called repeatedly (during idle events) until it returns true. Using this swatch image can be generated in stages.

		This method should be overridden in derived classes which can compute the swatches in several steps.

		Returns False as long as the swatch computation is not completed."""
	@staticmethod
	def getSwatchBackgroundColor()->om.MColor:
		"""getSwatchBackgroundColor() -> MColor

		Returns the default background color for the hardware rendered swatch."""
	@staticmethod
	def initialize()->str:
		"""initialize() -> string

		This method sets a swatch name, and registers a new swatch generator creation function for the swatch name.
		The string returned from this method can be used for node classification purpose."""
class MManipData:
	"""Class that encapsulates manipulator data."""
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def asBool(self)->bool:
		"""asBool() -> bool

		Returns the manipulator data as a bool"""
	def asDouble(self)->float:
		"""asDouble() -> float

		Returns the manipulator data as a double"""
	def asFloat(self)->float:
		"""asFloat() -> float

		Returns the manipulator data as a float"""
	def asLong(self)->int:
		"""asLong() -> int

		Returns the manipulator data as a long"""
	def asMObject(self)->int:
		"""asMObject() -> int

		Returns the manipulator data as an MObject.
		The MObjects returned from this method are created and used
		by MFnData or classes derived from MFnData."""
	def asShort(self)->int:
		"""asShort() -> int

		Returns the manipulator data as a short"""
	def asUnsigned(self)->int:
		"""asUnsigned() -> int

		Returns the manipulator data as a unsigned"""
	def isSimple(self)->bool:
		"""isSimple() -> bool

		Returns whether or not the manipulator data is simple or complex.
		Simple data is used to represent bool, int, and float types.
		Complex data is used to represent MObjects created by MFnData,
		or classes derived from MFnData."""
class MMaterial:
	"""This class is used in the draw functions of user defined shapes (see MPxSurfaceShapeUI) for setting up and querying materials in shaded mode drawing."""
	kColor:int=0
	kTransparency:int=1
	kAmbientColor:int=2
	kIncandescence:int=3
	kBumpMap:int=4
	kDiffuse:int=5
	kTransluscence:int=6
	kRoughness:int=7
	kHighlightSize:int=8
	kWhiteness:int=9
	kCosinePower:int=10
	kEccentricity:int=11
	kSpecularRollOff:int=12
	kSpecularColor:int=13
	kReflectivity:int=14
	kReflectedColor:int=15
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def applyTexture(self,view:M3dView,data:MDrawData)->Self:
		"""applyTexture(view, data) -> self

		For materials that have texture, this method must be used before the OpenGL drawing to apply the texture to the current view.
		This method should be called from within your MPxSurfaceShapeUI.draw() method.

		* view (M3dView) - the view in which the textured drawing is to take place
		* data (MDrawData) - the draw data from the draw request"""
	@staticmethod
	def defaultMaterial()->MMaterial:
		"""defaultMaterial() -> MMaterial

		Get the default material. There will always be a default material in the scene and therefore the result of this function should always succeed.  The default material will correspond to the initialShadingGroup node that is in the scene."""
	def evaluateDiffuse(self)->Self:
		"""evaluateDiffuse() -> self

		Perform necessary evaluation to be able to get diffuse back."""
	def evaluateEmission(self)->Self:
		"""evaluateEmission() -> self

		Perform necessary evaluation to be able to get emission back."""
	def evaluateMaterial(self,view:M3dView,path:om.MDagPath)->Self:
		"""evaluateMaterial(view, path) -> self

		Evaluate a material. Must be called before evaluating or getting any material properties.

		* view (M3dView) - the view
		* path (MDagPath) - path to the object"""
	def evaluateShininess(self)->Self:
		"""evaluateShininess() -> self

		Perform necessary evaluation to be able to get shininess back."""
	def evaluateSpecular(self)->Self:
		"""evaluateSpecular() -> self

		Perform necessary evaluation to be able to get specular back."""
	def evaluateTexture(self,data:MDrawData)->Self:
		"""evaluateTexture(data) -> self

		Evaluate texturing related information. Must be called before getting any texture properties such as getHasTransparency(), getTextureTransformation() and applyTexture().

		This method should be called from MPxSurfaceShapeUI.getDrawRequests().
		The draw data argument is the MDrawData for the request that will carry the texture information to the MPxSurfaceShapeUI.draw() method.

		* data (MDrawData) - draw request data to carry the texture information"""
	def getDiffuse(self)->om.MColor:
		"""getDiffuse() -> MColor

		Get the GL diffuse color."""
	def getEmission(self)->om.MColor:
		"""getEmission() -> MColor

		Get the GL emission color."""
	def getHasTransparency(self)->bool:
		"""getHasTransparency() -> bool

		Returns True if material or texture has transparency, False otherwise."""
	def getHwShaderNode(self)->MPxHwShaderNode:
		"""getHwShaderNode() -> MPxHwShaderNode

		Get the hardware shader node."""
	def getShininess(self)->float:
		"""getShininess() -> float

		Get the GL shininess."""
	def getSpecular(self)->om.MColor:
		"""getSpecular() -> MColor

		Get the GL specular color."""
	@overload
	def getTextureTransformation(self,data:MDrawData,texXform:Any)->Self:
		"""getTextureTransformation(data, texXform) -> self
		getTextureTransformation(data) -> [float, float, float, float, float, float]

		Get the current textures transformation.

		* data (MDrawData) - the draw data from the draw request
		* texXform [OUT] (MMatrix) - storage for the texture transformation

		Or
		* data (MDrawData) - the draw data from the draw request
		Returns the transformations values:
		   rotateUV (float) - storage for rotatation value of the UV coordinates
		   scaleU (float) - storage for u scale value
		   scaleV (float) - storage for v scale value
		   translateU (float) - storage for u translation value
		   translateV (float) - storage for v translation value
		   rotateFrame (float) - storage for rotatation value of the frame coordinates"""
	@overload
	def getTextureTransformation(self,data:MDrawData)->list[float]:
		"""getTextureTransformation(data, texXform) -> self
		getTextureTransformation(data) -> [float, float, float, float, float, float]

		Get the current textures transformation.

		* data (MDrawData) - the draw data from the draw request
		* texXform [OUT] (MMatrix) - storage for the texture transformation

		Or
		* data (MDrawData) - the draw data from the draw request
		Returns the transformations values:
		   rotateUV (float) - storage for rotatation value of the UV coordinates
		   scaleU (float) - storage for u scale value
		   scaleV (float) - storage for v scale value
		   translateU (float) - storage for u translation value
		   translateV (float) - storage for v translation value
		   rotateFrame (float) - storage for rotatation value of the frame coordinates"""
	def materialIsTextured(self)->bool:
		"""materialIsTextured() -> bool

		Returns True if the material is textured, False otherwise."""
	def setMaterial(self,path:om.MDagPath,hasTransparency:bool)->Self:
		"""setMaterial(path, hasTransparency) -> self

		Set the current GL material.

		* path (MDagPath) - path to the object
		* hasTransparency (bool) - whether the material has transparency"""
	def shadingEngine(self)->om.MObject:
		"""shadingEngine() -> MObject

		Get the shading engined associated with this material."""
	def textureImage(self,image:Any,color:Any,chan:int,dagPath:om.MDagPath,xRes:int=-1,yRes:int=-1)->Self:
		"""textureImage(image, color, chan, dagPath, xRes=-1, yRes=-1) -> self

		For materials that have texture, this method will attempt to retrieve the pixel map for a given mapped channel of that material.
		Will fails If the channel is not mapped.

		The material types that can be queried include:
		  - Lambert
		  - Phong
		  - PhongE
		  - Anisotropic
		  - Blinn

		Currently only channels mapped to single file textures is supported.

		* image [OUT] (MImage) - The image retrieved. If no image could be retrieve, the value will not change.
		* color [OUT] (MColor) - Either the mapped or unmapped color. If the channel is mapped then an RGBA value of (1,1,1,1) will be returned, otherwise the unmapped channel's current color value will be returned.
		* chan (int) - Texture channel to check.
		* dagPath (MDagPath) - Optional dag path to object. An object path is required to produce texture maps from non-2D procedural textures.
		* xRes (int) - Optional width of image to create. The minimal allowed value is 2. This parameter only applies to procedural textures. The dimension in X will be 128 by default, if a value less than 2 is specified.
		* yRes (int) - Optional height of image to create. The minimal allowed value is 2. This parameter only applies to procedural textures. The dimension in Y will be 128 by default, if a value less than 2 is specified.

		Valid Texture channel:
		  kColor
		  kTransparency
		  kAmbientColor
		  kIncandescence
		  kBumpMap
		  kDiffuse
		  kTransluscence
		  kRoughness           PhongE only
		  kHighlightSize       PhongE only
		  kWhiteness           PhongE only
		  kCosinePower         Phong only
		  kEccentricity        Blinn only
		  kSpecularRollOff     Blinn only
		  kSpecularColor       Blinn and Phong(E) only
		  kReflectivity        Blinn and Phong(E) only
		  kReflectedColor      Blinn and Phong(E) only"""
class MMaterialArray(collections.abc.Sequence[MMaterial]):
	"""An array of MMaterial."""
	@property
	def sizeIncrement(self)->Any:
		"""The size by which the array will be expanded whenever expansion is necessary."""
	@sizeIncrement.setter
	def sizeIncrement(self,value:Any)->None:...
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def __len__(self)->int:
		"""Return len(self)."""
	def __getitem__(self,index:int)->MMaterial:
		"""Return self[key]."""
	def append(self,element:MMaterial)->Self:
		"""append(element) -> self

		Adds a new element to the end of the array.

		* element (MMaterial) - the value for the new last element."""
	def clear(self)->Self:
		"""clear() -> self

		Clear the contents of the array. After this operation the length will be 0.  This does not change the amount of memory allocated to the array, only the number of valid elements in it."""
	def copy(self,source:MMaterialArray)->Self:
		"""copy(source) -> self

		Copy the contents of the source array to this array.

		* source (MMaterialArray) - array to copy from."""
	def insert(self,element:MMaterial,index:int)->Self:
		"""insert(element, index) -> self

		Inserts a new value into the array at the given index. The initial element at that index, and all following elements, are shifted towards the last.

		* element (MMaterial) - the new value to insert into the array.
		* index (int) - the index of the element to set."""
	def remove(self,index:int)->Self:
		"""remove(index) -> self

		Removes the element in the array at the given index.

		* index (int) - the index of the element to remove."""
	def set(self,element:MMaterial,index:int)->Self:
		"""set(element, index) -> self

		Sets the value of the specified element to the given attribute spec.

		* element (MMaterial) - the new value for the specified element.
		* index (int) - the index of the element to be set."""
	def setLength(self,length:int)->Self:
		"""setLength(length) -> self

		Set the length of the array. This will grow and shrink the array as desired. Elements that are grown have uninitialized values, while those which are shrunk will lose the data contained in the deleted elements

		* length (int) - the new size of the array."""
class MPaintMessage(om.MMessage):
	"""Class used to register callbacks for paint related messages."""
	@staticmethod
	def addVertexColorCallback(function:Callable,clientData:Any|None=None)->int:
		"""addVertexColorCallback(function, clientData=None) -> id

		Adds a new callback on vertex color paint.

		Note: the 'colors' parameter supplied to the callback function contains a color per vertex, even if the type of the component being painted is faces. To interpret the colors when faces are being painted, it will be necessary to query the vertex count of each face and step over that many vertices while iterating the array.

		The callback function will be passed any client data that was
		provided when the callback was registered.

		 * function - callable which will be passed:
		   The DAG path of the object being painted (MDagPath)
		   The components (e.g. vertices, faces) being painted (MObject)
		   The plug being painted (MPlug)
		   The colors that were applied to the components (MColorArray)
		 * clientData - User defined data passed to the callback function

		 * return: Identifier used for removing the callback."""
class MPanelCanvas:
	"""Provides API extension to panel canvas.

	__init__()
	Initializes a new MPanelCanvas."""
	kGraphEditorUndefined:int=-1
	kGraphEditorBackground:int=0
	kGraphEditorFirstDefaultDraw:int=100
	kGraphEditorGrid:int=100
	kGraphEditorAxisLabels:int=1000
	kGraphEditorCurves:int=2000
	kGraphEditorCurveNames:int=3000
	kGraphEditorTimeMarker:int=4000
	kGraphEditorRetimeToolText:int=5000
	kGraphEditorLastDefaultDraw:int=10000
	kGraphEditorOverlayTexture:int=10000
	def __init__(self)->None:
		"""Initializes a new MPanelCanvas."""
	def addPrimitive(self,int:int,int2:int)->None:
		"""addPrimitive( int, int )

		Add the primitive referred to by the given id to the list of
		primitives to be drawn at the given layer.
		Return: None"""
	def createFloatVertexBuffer(self,tVals:Any,yVals:Any,colors:Any)->int:
		"""createFloatVertexBuffer( tVals, yVals, colors ) -> int

		Create a vertex buffer with float values as the x-coordinate.
		An id referring to the created buffer is returned. The values
		are passed as arrays of float values
		Return: int"""
	def createTimeVertexBuffer(self,tVals:Any,yVals:Any,colors:Any)->int:
		"""createTimeVertexBuffer( tVals, yVals, colors ) -> int

		Create a vertex buffer with time values as the x-coordinate.
		An id referring to the created buffer is returned. The values
		are passed as arrays of OpenMaya.MTime values
		Return: int"""
	def createPrimitive(self,primType:Any,bufferId:Any,startIndex:Any,numVertices:Any,props:Any)->int:
		"""createPrimitive( primType, bufferId, startIndex, numVertices, props ) -> int

		Create a primitive of the given type using the vertex buffer
		specified by the given id, the range of vertices used from
		the buffer, and a drawing style. An id referring to the
		created primitive is returned.
		Return: int"""
	def destroyVertexBuffer(self,bufferId:Any)->None:
		"""destroyVertexBuffer( bufferId )

		Destroy the vertex buffer referred to by the given id.  If the.
		buffer is being used by a primitive, an error will be generated.
		Return: None"""
	def destroyPrimitive(self,primitiveId:Any)->None:
		"""destroyPrimitive( primitiveId )

		Destroy the primitive referred to by the given id.
		Return: None"""
	def isAutoRefresh(self)->bool:
		"""isAutoRefresh() -> bool

		Returns whether the associated editor will automatically refresh.


		Return: bool"""
	def isLayerVisible(self,int:int)->bool:
		"""isLayerVisible( int) -> bool

		Return whether the given layer is visible.
		Return: bool"""
	def registerDrawUICallback(self,layer:Any,cb:Any,clientData:Any)->callbackId:
		"""registerDrawUICallback( layer, cb, clientData ) -> callbackId

		Register a callback to be called when the given panel is drawing
		the given layer. An id to the callback is returned. The function
		takes two parameters, an instance of an OpenMayaRender.MUIDrawManager
		and whatever client data was passed to this method.
		Return: int"""
	def removePrimitive(self,int:int,int2:int)->None:
		"""removePrimitive( int, int )

		Remove the primitive referred to by the given id from the list of
		primitives to be drawn at the given layer. The primitive will not
		be destroyed.
		Return: None"""
	def setLayerVisible(self,int:int,bool:bool)->None:
		"""setLayerVisible( int, bool )

		Set whether the given layer will be drawn. All layers are
		initially set to be visible. Only user defined layers may have
		their visibility set.
		Return: None"""
	def refresh(self)->None:
		"""refresh()

		Force the associated Graph Editor to refresh
		Return: None"""
	def setAutoRefresh(self)->None:
		"""setAutoRefresh()

		Set whether the associated editor will be automatically refreshed.
		Initially, automatic refresh is enabled.
		Return: None"""
	def supportsUIDrawing(self)->bool:
		"""supportsUIDrawing() -> bool

		Returns whether the attached panel control supports drawing
		primitives in screen space. If such drawing is not supported,
		the registerDrawUICallback () method will throw an exception.

		Note that the Graph Editor will return false if it exists, but the
		panel for drawing has not yet been created (e.g., for the default
		Graph Editor when it has not yet been opened, but exists by default).
		Return: bool"""
	def isValid(self)->bool:
		"""isValid() -> bool

		Returns True if MPanelCanvas has a valid pointer to a Graph
		Editor object, False otherwise.
		Return: bool"""
	def unregisterDrawUICallback(self,callbackId:Any)->None:
		"""unregisterDrawUICallback( callbackId )

		 Unregister the callback specified by the given id.
		Return: None"""
class MPanelCanvasInfo:
	"""Provides API extension to get/set panel canvas information.

	__init__()
	Initializes a new MPanelCanvasInfo."""
	def __init__(self)->None:
		"""Initializes a new MPanelCanvasInfo."""
	def getViewportBounds(self)->None:
		"""getViewportBounds()

		Returns an array of four values representing the corners of the
		viewing region: [left, right, bottom, top].
		Return: float[]"""
	def getViewportSize(self)->None:
		"""getViewportSize()

		Returns an array of two values representing the size of the
		viewing region: [width, height].
		Return: int[]"""
	def name(self)->str:
		"""name() -> MString

		Return the name of the currently attached panel.
		Return: MString"""
	def setViewportBounds(self,bounds:Any)->None:
		"""setViewportBounds( bounds )

		Set the bounds of the editor's viewing region. The passed.
		bounds are specified as an array of four values: [left, right,
		bottom, top].
		Return: None"""
	def supportsUIDrawing(self)->bool:
		"""supportsUIDrawing() -> bool

		Returns whether the attached panel control supports drawing
		primitives in screen space. If such drawing is not supported,
		the registerDrawUICallback () method will throw an exception.

		Note that the Graph Editor will return false if it exists, but the
		panel for drawing has not yet been created (e.g., for the default
		Graph Editor when it has not yet been opened, but exists by default).
		Return: bool"""
class MPxContext:
	"""This is the base class for user defined drag and drop behaviors."""
	kImage1:int=0
	kImage2:int=1
	kImage3:int=2
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def toolOnSetup(self,event:MEvent)->None:
		"""toolOnSetup(event) -> None

		This method is called when the context is activated, i.e when
		the toolButton for the context is pressed.
		Users can override this method and use it to set up any user
		defined data that needs to be initialized on each activation.


		* event (MEvent) - The button press event information."""
	def toolOffCleanup(self)->None:
		"""toolOffCleanup() -> None

		This method is called when the context is deactivated, i.e when
		another context is activated.
		Users can override this method and use it to reset any user
		defined data to a specific state."""
	def doPress(self,event:MEvent,drawMgr:Any,context:Any)->None:
		"""doPress(event, drawMgr, context) -> None

		This method is called when any mouse button is pressed.
		The base method does nothing and should be overridden if
		the user needs to do anything on a button press.

		This method is called only when in Viewport 2.0. MUIDrawManager
		must be used for any viewport drawing done in this method. Direct
		calls to OpenGL or DirectX are unsupported and may result in instability
		or unpredictable behavior.

		MUIDrawManager allows for drawing primitives in the 3D modeling space.
		Those primitives will then be projected onto a 2D overlay plane before being
		displayed.

		The event can be used to get more explicit information
		about the press such as the button number. See MEvent for
		more information.

		* event (MEvent) - The button press event information.
		* drawMgr (MHWRender::MUIDrawManager) - The UI draw manager, it can be used to draw some simple geometry including text.
		* context (MHWRender::MFrameContextFrame) - level context information."""
	def doRelease(self,event:MEvent,drawMgr:Any,context:Any)->None:
		"""doRelease(event, drawMgr, context) -> None

		This method is called when any mouse button is released.
		The base method does nothing and should be overridden if
		the user needs to do anything on a button release.

		This method is called only when in Viewport 2.0. MUIDrawManager
		must be used for any viewport drawing done in this method. Direct
		calls to OpenGL or DirectX are unsupported and may result in instability
		or unpredictable behavior.

		MUIDrawManager allows for drawing primitives in the 3D modeling space.
		Those primitives will then be projected onto a 2D overlay plane before being
		displayed.

		The <b>event</b> can be used to get more explicit information
		about the release such as the button number. See MEvent for
		more information.

		* event (MEvent) - The button press event information.
		* drawMgr (MHWRender::MUIDrawManager) - The UI draw manager, it can be used to draw some simple geometry including text.
		* context (MHWRender::MFrameContextFrame) - level context information."""
	def doDrag(self,event:MEvent,drawMgr:Any,context:Any)->None:
		"""doDrag(event, drawMgr, context) -> None

		This method is called when a mouse drag event occurs.
		The base method does nothing and should be overridden if
		the user needs to do anything during a mouse drag.

		This method is called only when in Viewport 2.0. MUIDrawManager
		must be used for any viewport drawing done in this method. Direct
		calls to OpenGL or DirectX are unsupported and may result in instability
		or unpredictable behavior.

		MUIDrawManager allows for drawing primitives in the 3D modeling space.
		Those primitives will then be projected onto a 2D overlay plane before being
		displayed.

		The <b>event</b> can be used to get more explicit information
		about the drag such as the cursor location. See MEvent for
		more information.

		* event (MEvent) - The button press event information.
		* drawMgr (MHWRender::MUIDrawManager) - The UI draw manager, it can be used to draw some simple geometry including text.
		* context (MHWRender::MFrameContextFrame) - level context information."""
	def doHold(self,event:MEvent,drawMgr:Any,context:Any)->None:
		"""doHold(event, drawMgr, context) -> None

		This method is called when a mouse button is pressed but
		before the mouse is dragged.
		The base method does nothing and should be overridden if the user needs
		to do anything on a button hold.

		This method is called only when in Viewport 2.0. MUIDrawManager
		must be used for any viewport drawing done in this method. Direct
		calls to OpenGL or DirectX are unsupported and may result in instability
		or unpredictable behavior.

		MUIDrawManager allows for drawing primitives in the 3D modeling space.
		Those primitives will then be projected onto a 2D overlay plane before being
		displayed.

		The <b>event</b> can be used to get more explicit information
		about the hold such as the button number. See MEvent for
		more information.

		* event (MEvent) - The button press event information.
		* drawMgr (MHWRender::MUIDrawManager) - The UI draw manager, it can be used to draw some simple geometry including text.
		* context (MHWRender::MFrameContextFrame) - level context information."""
	def drawFeedback(self,event:Any,drawMgr:Any,context:Any)->None:
		"""drawFeedback(event, drawMgr, context ) -> None

		This method is called to draw primitives when your context is activated

		This method is called only when using Viewport 2.0. MUIDrawManager
		must be used for any viewport drawing done in this method. Direct
		calls to OpenGL or DirectX are unsupported and may result in instability
		or unpredictable behavior.

		MUIDrawManager allows for drawing primitives in the 3D modeling space.
		Those primitives will then be projected onto a 2D overlay plane before being
		displayed.

		* drawMgr (MHWRender::MUIDrawManager) - The UI draw manager, it can be used to draw some simple geometry including text.
		* context (MHWRender::MFrameContextFrame) - level context information."""
	def doPtrMoved(self,event:MEvent,drawMgr:Any,context:Any)->None:
		"""doPtrMoved(event, drawMgr, context ) -> None

		This method is called when a mouse move event occurs.
		The base method does nothing and should be overridden if
		the user needs to do anything during a mouse drag.

		This method is called only when in Viewport 2.0. MUIDrawManager
		must be used for any viewport drawing done in this method. Direct
		calls to OpenGL or DirectX are unsupported and may result in instability
		or unpredictable behavior.

		MUIDrawManager allows for drawing primitives in the 3D modeling space.
		Those primitives will then be projected onto a 2D overlay plane before being
		displayed.

		The <b>event</b> can be used to get more explicit information
		about the drag such as the cursor location. See MEvent for
		more information.

		* event (MEvent) - The button press event information.
		* drawMgr (MHWRender::MUIDrawManager) - The UI draw manager, it can be used to draw some simple geometry including text.
		* context (MHWRender::MFrameContextFrame) - level context information."""
	def doPressLegacy(self,event:MEvent)->None:
		"""doPressLegacy(event) -> None

		This method is called when any mouse button is pressed.
		The base method does nothing and should be overridden if
		the user needs to do anything on a button press.

		This method is called only when it is in either default viewport renderer
		or hardware viewport renderer, not viewport 2.0.

		The <b>event</b> can be used to get more explicit information
		about the press such as the button number. See MEvent for
		more information.

		* event (MEvent) - The button press event information."""
	def doReleaseLegacy(self,event:MEvent)->None:
		"""doReleaseLegacy(event) -> None

		This method is called when any mouse button is released.
		The base method does nothing and should be overridden if
		the user needs to do anything on a button release.

		This method is called only when it is in either default viewport renderer
		or hardware viewport renderer, not viewport 2.0.

		The <b>event</b> can be used to get more explicit information
		about the release such as the button number. See MEvent for
		more information.

		* event (MEvent) - The button release event information."""
	def doDragLegacy(self,event:MEvent)->None:
		"""doDragLegacy(event) -> None

		This method is called when a mouse drag event occurs.
		The base method does nothing and should be overridden if
		the user needs to do anything during a mouse drag.

		This method is called only when it is in either default viewport renderer
		or hardware viewport renderer, not viewport 2.0.

		The <b>event</b> can be used to get more explicit information
		about the drag such as the cursor location. See MEvent for
		more information.

		* event (MEvent) - The button drag event information."""
	def doHoldLegacy(self,event:MEvent)->None:
		"""doHoldLegacy(event) -> None

		This method is called when a mouse button is pressed but
		before the mouse is dragged.
		The base method does nothing and should be overridden if the user needs
		to do anything on a button hold.

		This method is called only when it is in either default viewport renderer
		or hardware viewport renderer, not viewport 2.0.

		The <b>event</b> can be used to get more explicit information
		about the hold such as the button number. See MEvent for
		more information.

		* event (MEvent) - The button hold event information."""
	def doPtrMovedLegacy(self,event:MEvent)->None:
		"""doPtrMovedLegacy(event) -> None

		This method is called when a mouse drag event occurs.
		The base method does nothing and should be overridden if
		the user needs to do anything during a mouse drag.

		This method is called only when it is in either default viewport renderer
		or hardware viewport renderer, not viewport 2.0.

		The <b>event</b> can be used to get more explicit information
		about the drag such as the cursor location. See MEvent for
		more information.

		* event (MEvent) - The button press event information."""
	def doEnterRegion(self,event:MEvent)->None:
		"""doEnterRegion(event) -> None

		This method is called when a mouse enters the viewport.
		The base method does nothing and should be overridden if
		the user needs to do anything during an enter event.

		The <b>event</b> can be used to get more explicit information
		about the event such as the cursor location. See MEvent for
		more information.

		* event (MEvent) - The event information."""
	def doExitRegion(self,event:MEvent)->None:
		"""doExitRegion(event) -> None

		This method is called when a mouse exits the viewport.
		The base method does nothing and should be overridden if
		the user needs to do anything during an exit event.

		The <b>event</b> can be used to get more explicit information
		about the event such as the cursor location. See MEvent for
		more information.

		* event (MEvent) - The event information."""
	def helpStateHasChanged(self,event:MEvent)->None:
		"""helpStateHasChanged(event) -> None

		This method is called whenever the help state may need to be
		updated.
		The base method does nothing and should be overriden if
		the user needs to change the help information based on events.

		The <b>event</b> can be used to get more explicit information
		about the event. See MEvent for more information.

		* event (MEvent) - The event information."""
	def deleteAction(self)->None:
		"""deleteAction() -> None

		This method is called when the delete or backspace key is pressed.
		The default behaviour for this method is to delete the items on the
		current selection list.
		Users can override this method if they wish to do anything else
		when this event occurs."""
	def completeAction(self)->None:
		"""completeAction() -> None

		This method is called when the complete key is pressed.
		The default complete key in Maya is the <b>enter</b> key.
		Users can override this method if a tool has several steps.
		For example, a tool may have several steps where the user must
		select objects and then press the completion key before proceeding."""
	def addManipulator(self,manipulator:om.MObject)->None:
		"""addManipulator(manipulator) -> None

		This method adds a manipulator to the context.

		* manipulator (MObject) - the manipulator to be added to the context."""
	def deleteManipulators(self)->None:
		"""deleteManipulators() -> None

		This method deletes all the manipulators that belong
		to the context."""
	def setImage(self,image:str,index:ImageIndex)->Self:
		"""setImage(image, index) -> self

		This method is used to set an XPM icon image that is to be
		used to represent this tool context in various places
		including the tool bar and can be queried from mel using the
		contextInfo command.

		* image (string) - the name of an XPM file to be used as the icon.
		* index (ImageIndex) - the index of the image being set; three image
		representations are permitted: kImage1, kImage2, kImage3."""
	def image(self,index:ImageIndex)->str:
		"""image(index) -> string

		This method is used to retrieve an XPM icon image that has
		previously been set for this tool context. This icon image will be
		used to represent this tool context in various places including
		the tool bar and can be queried from mel using the contextInfo
		command.

		* index (ImageIndex) - the index of the image being retrieved; three image
		representations are permitted: kImage1, kImage2, kImage3."""
	def abortAction(self)->None:
		"""abortAction() -> None

		This method is called when the abort key is pressed.
		The default abort key in Maya is the <b>escape</b> key.
		Users can override this method if they wish to perform
		certain operations when the abort key is pressed."""
	def processNumericalInput(self,values:om.MDoubleArray,flags:om.MIntArray,isAbsolute:bool)->bool:
		"""processNumericalInput(values, flags, isAbsolute) -> bool

		This method processes the input from the numerical input field.
		Users can override this method if they wish to process numerical input.
		For a given entry in the numeric input field, if the user types a dot '.',
		this indicates that the entry should not be modified.
		The overridden version of this method should take this into account
		using the ignoreEntry method with the flags that are passed in.
		The overridden version of this method should also process the numeric
		input as an absolute input or relative input depending on whether
		the isAbsolute flag is true or not.
		The return value should indicate whether or not the numerical input has
		been processed.

		* values (MDoubleArray) - the values from the numerical input field.
		* flags (MIntArray) - used in conjunction with the ignoreEntry method,
		determines whether or not a given entry should be ignored.
		* isAbsolute (bool) - whether or not the input should be interpreted as absolute."""
	def feedbackNumericalInput(self)->bool:
		"""feedbackNumericalInput() -> bool

		This method is called to update the numerical feedback.
		The format and values for the feedback line can be set through the
		methods in MFeedbackLine, specifically setFormat and setValue.
		The return value should indicate whether or not the numerical feedback
		has been provided.  The default return value is false."""
	def argTypeNumericalInput(self,index:int)->int:
		"""argTypeNumericalInput(index) -> MSyntax.MArgType

		This method is used by the feedback line to determine what units to display.
		Users should override this method to return the appropriate
		argument type for the given index of the numeric input field.
		Specifically, this method should be overridden to return one of the following:

		    <b>MSyntax.kNoArg</b> for no argument
		    <b>MSyntax.kDistance</b> for linear units
		    <b>MSyntax.kAngle</b> for angular units

		* index (int) - the index of the numerical input whose argument type is requested."""
	def setHelpString(self,str:str)->Self:
		"""setHelpString(str) -> self

		Set the help string to the given MString.
		This string will appear in the help line in Maya.

		* str (string) - The new help string."""
	def setTitleString(self,str:str)->Self:
		"""setTitleString(str) -> self

		Set the title of the context to the MString that is passed in.
		This string will appear in the help line when this context is
		activated.

		* str (string) - The new title string."""
	def setCursor(self,newCursor:MCursor)->Self:
		"""setCursor(newCursor) -> self

		Set the cursor used by the context to the MCursor that is passed in.

		* newCursor (MCursor) - The new cursor."""
	def beginMarquee(self,event:MEvent)->Self:
		"""beginMarquee(event) -> self

		Start drawing a dragged out marquee box.
		A marquee box is a rectangular area of the screen specified by
		two points representing opposite corners of the rectangle.
		Marquee's are commonly used in the selection of multiple items from
		a region of the screen. The marquee rectangle acts as a guideline
		for the region of the screen that will be effected.

		* event (MEvent) - current event information."""
	def dragMarquee(self,event:MEvent)->Self:
		"""dragMarquee(event) -> self

		Draws a rectangle representing the dragged out area initiated with
		the beginMarquee method.

		* event (MEvent) - current event information."""
	def releaseMarquee(self,event:MEvent)->tuple[top,left,bottom,right]:
		"""releaseMarquee(event) -> (top, left, bottom, right)

		End the marquee drawing cycle and return the coordinates corresponding to
		the dragged out area.
		The rectangular guideline representing the dragged area is cleared.

		Returns a tuple consisting of the top, left, bottom, and right corners of the marquee area.
		* event (MEvent) - current event information."""
	def newToolCommand(self)->MPxToolCommand:
		"""newToolCommand() -> MPxToolCommand

		Create a new instance of the tool command associated with this context.
		The tool command (derived from MPxToolCommand) is the command that was
		registered along with the context command in.

		Returns a new instance of the MPxToolCommand."""
	def stringClassName(self)->str:
		"""stringClassName() -> string

		This method is called to determine the name that uniquely identifies
		the context.  Either this method, or the getClassName method, should
		be overridden such that the name is set to the appropriate string.
		For example:

		def stringClassName(self)
		    return 'exampleTool'

		This name is used by Maya to call the appropriate
		tool property sheet MEL scripts, specifically:
		    <b>name</b>Properties.mel
		    <b>name</b>Values.mel
		If this method is not overriden, by default it will set
		the string to 'defaultTool'.  The method returns a string
		that uniquely identifies the context."""
	def inAlternateContext(self)->bool:
		"""inAlternateContext() -> bool

		This method is called to determine if an alternate context is active.
		For example, this method returns true if the user moves the camera
		while the current context is active."""
class MPxContextCommand:
	"""Base class for custom context commands."""
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def doEditFlags(self)->None:
		"""doEditFlags() -> None

		This method is called when the command is called in edit mode.
		This method should be overridden by context commands
		to determine which edit flags are set in conjunction with
		the argument parser for this command.  The argument parser
		for this command can be obtained by calling the
		parser method.
		If the command is called with both the edit flag and
		the query flag, then the query flag will be ignored."""
	def doQueryFlags(self)->None:
		"""doQueryFlags() -> None

		This method is called when the command is called in query mode.
		This method should be overridden by context commands
		to determine which query flags are set in conjunction with
		the argument parser for this command.  The argument parser
		for this command can be obtained by calling the
		parser method.
		If the command is called with both the edit flag and
		the query flag, then the query flag will be ignored."""
	def makeObj(self)->MPxContext:
		"""makeObj() -> MPxContext

		This function is used to instantiate a proxy context.
		In your derived class, declare this function:

		def makeObj(self)
		    return userContextClass()

		where userContextClass is derived from MPxContext."""
	def appendSyntax(self)->None:
		"""appendSyntax() -> None

		This method should be overridden to append syntax
		to the context command.  The syntax object can be
		obtained by calling the syntax method.
		The following flags cannot be used as user-defined
		flags as they are reserved for edit and query:
		'-e', '-edit', '-q', '-query'."""
	def parser(self,*args)->Any:
		"""Returns the context command's MArgParser object, if it has one."""
	def setResult(self)->None:
		"""setResult() -> None

		Set the value of the result to be returned by the command.  The value can be
		either a boolean, integer, floating point value, or string."""
	def syntax(self,*args)->Any:
		"""Returns the context command's MSyntax object, if it has one."""
class MPxDragAndDropBehavior:
	"""This is the base class for user defined drag and drop behaviors."""
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def shouldBeUsedFor(self,sourceNode:om.MObject,destinationNode:om.MObject,sourcePlug:om.MPlug,destinationPlug:om.MPlug)->bool:
		"""shouldBeUsedFor(sourceNode, destinationNode, sourcePlug, destinationPlug) -> bool

		This method must be overridden in order to use a drag and drop behavior.

		The overridden method will be called by the defaultNavigation command to determine wether or not to use this drag and drop behavior to finish a connection. If the user would like to handle the connection between sourceNode/Plug and destinationNode/Plug then this routine must pass back true, otherwise the routine must pass back false in order for the default connection mechanism to work between these two nodes. sourcePlug and destinationPlug may be null depending on if there were any attributes given in the drag and drop. Use the isNull() method on MPlug to assure the plugs are valid.

		* sourceNode (MObject) - The source node of the drag and drop or the node being dragged.
		* destinationNode (MObject) - the destination node of the drag and drop or the node being dropped upon.
		* sourcePlug (MPlug) - The source plug of the drag and drop or the plug being dragged (this may be null).
		* destinationPlug (MPlug) - The destination plug of the drag and drop or the plug being dropped upon (this may be null)."""
	def connectAttrToAttr(self,sourcePlug:om.MPlug,destinationPlug:om.MPlug,force:bool)->None:
		"""connectAttrToAttr(sourcePlug, destinationPlug, force) -> None

		This method is called by the defaultNavigation command to connect a source attribute to a destination attribute.

		If this method is overidden it should attempt to determine what the user probably wants this connection to be, and set up the connection appropriately. If the force argument is true it is intended to notify the user to break any existing connections to the plug, similar to what the mel command 'connectAttr' -f flag is used for.

		* sourcePlug (MPlug) - Source plug in the connection.
		* destinationPlug (MPlug) - Destination plug in the connection.
		* force (bool) - Tells whether or not to break any existing connections to the destination attribute."""
	def connectAttrToNode(self,sourcePlug:om.MPlug,destinationNode:om.MObject,force:bool)->None:
		"""connectAttrToNode(sourcePlug, destinationNode, force) -> None

		This method is called by the defaultNavigation command to connect a source attribute to a destination node.

		You should override this method if you can determine from the type of source node and attribute and the type of destination node what the user is trying to do and you know the appropriate connections that must be made for the end result to be what the user expects.

		* sourcePlug (MPlug) - Source plug in the connection.
		* destinationNode (MObject) - Destination node for the connection.
		* force (bool) - Tells whether or not to break any existing connections to the destination node."""
	def connectNodeToAttr(self,sourceNode:om.MObject,destinationPlug:om.MPlug,force:bool)->None:
		"""connectNodeToAttr(sourceNode, destinationPlug, force) -> None

		This method is called by the defaultNavigation command to connect a source node to a destination attribute.

		You should override this method if you can determine from the type of source node and the type of destination node and attribute what the user is trying to do and you know the appropriate connections that must be made for the end result to be what the user expects.

		* sourceNode (MObject) - Source node in the connection.
		* destinationPlug (MPlug) - Destination plug for the connection.
		* force (bool) - Tells whether or not to break any existing connections to the destination attribute."""
	def connectNodeToNode(self,sourceNode:om.MObject,destinationNode:om.MObject,force:bool)->None:
		"""connectNodeToNode(sourceNode, destinationNode, force) -> None

		This method is called by the defaultNavigation command to connect a source node to a destination node.

		You should override this method if you can determine from the type of source node and the type of destination node what the user is trying to do and you know the appropriate connections that must be made for the end result to be what the user expects.

		* sourceNode (MObject) - Source node in the connection.
		* destinationNode (MObject) - Destination node for the connection.
		* force (bool) - Tells whether or not to break any existing connections to the destination node."""
class MPxHardwareShader(om.MPxNode):
	"""Base class for user defined hardware shaders."""
	kIsTransparent:int=1
	kNoTransparencyFrontBackCull:int=2
	kNoTransparencyPolygonSort:int=4
	outColor:om.MObject
	outColorR:om.MObject
	outColorG:om.MObject
	outColorB:om.MObject
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	@staticmethod
	def findResource(name:str,shaderPath:str)->str:
		"""findResource(name, shaderPath) -> string

		This is a static utility to find the full path to a shader resource (typically a texture). This method will search the list of paths in the MAYA_HW_SHADER_RESOURCE_PATH environment variable, resolving relative paths based on the directory containing the shader.

		* name (string) - The name of the resource to look for (e.g. 'normals.dds')
		* shaderPath (string) - The full path to the current shader (e.g. 'C:/shaders/myshader.fx')


		Return the full path of the resource (e.g. 'C:/shaders/textures/normals.dds')."""
	def getAvailableImages(self,context:ShaderContext,uvSetName:str)->list[str|None]:
		"""getAvailableImages(context, uvSetName) -> list of string/None

		Maya will call this method to get your shader's list of images which are available for use in the UV texture editor for the UV set specified. Typically, this list will include one entry for each texture using the specified UV set, however, your shader is free to return as many images as you wish (for example, blending between two textures, texture alpha masks, artificially shaded views of bump/normal maps, etc). Your shader's renderImage() method will be used to render the images themselves.

		* context (ShaderContext) - Context of the draw request (e.g. the surface being shaded, shading engine making the request)
		* uvSetName (string) - Name of a UV set the channel list should be filtered against.

		Returns the names of the images this shader defines which are valid for the uvSetName specified.
		Returns None if method is not implemented : Use the default behaviour."""
	@staticmethod
	def getHardwareShader(object:om.MObject)->TODO:
		"""getHardwareShader(object) -> TODO

		This is a static convenience method to be able to get an MPxHardwareShader from an MObject provided by a swatch generator class (Class derived from MSwatchRenderRegister).

		* object (MObject) - The object to examine.

		Return a MPxHardwareShader. If the method failed for any reason then None will be returned."""
	def profile(self)->omr.MRenderProfile:
		"""profile() -> MRenderProfile

		Override this method to specify the renderers your shader supports. If this method is not overridden, Maya will assume your shader supports only Maya's iternal OpenGL based renderer.

		Note that this method is called inside the rendering loop and as such, you should make this method as fast as possible - typically just returning a static/precalculated value.

		Return a reference to the render profile for this Shader. Your shader class should create this once (usually for the whole class) and return the same object each time this method is called."""
	@overload
	def renderImage(self,context:ShaderContext,imageName:str,region:float[2][2],parameters:RenderParamters)->list[int]|None:
		"""renderImage(context, imageName, region, parameters) -> [int, int]/None
		renderImage(context, uiDrawManager, imageName, region, parameters) -> [int, int]/None

		This method allows you to to render the background image used for this shader in the UV texture editor. The image requested will be one of the image names returned by your shader's getAvailableImages() method.

		The implementation must return the dimensions of the image in the 'imageWidth' and 'imageHeight' parameters so that Maya can perform pixel snapping and other resolution-dependent operations.

		The implementation can assume OpenGL context, model view projection matrix, and texture transformations have already been set. A default color of white will be set, however you are free to change this. The magnification filter will be set to either point or bilinear based on user configuration and should not be modified. The values of GL_TEXTURE_WRAP_S and GL_TEXTURE_WRAP_T are undefined on entry, and your implementation is responsible for setting them to appropriate values (e.g. GL_REPEAT).

		The arguments contain the name of the image to render, and the vertex and texture coordinate values to use at each corner of the rectangular image being rendered. Your implementation is responsible for restoring the original the value of any OpenGL state that is modified.

		* context (ShaderContext) - Context of the draw request (e.g. the surface being shaded, shading engine making the request)
		* imageName (string) - Name of the image to render. This corresponds to one of the image names returned by your shader's getAvailableImages() method.
		* region (float[2][2]) - Rectangular region to be rendered. The values of this parameter should be used to populate the vertex and texture coordinates of the rectangle being rendered.
		* parameters (RenderParamters) - Additional parameters on how to render the image. The values reflect the image settings of the UV editor.

		A second version with the uiDrawManager parameter allows you to to render the background image used for this shader in the UV texture editor in viewport 2.0.

		* uiDrawManager (MUIDrawManager) - The UI draw manager, it can be used to draw some simple geometry

		Returns None if method is not implemented : No rendering will occur."""
	@overload
	def renderImage(self,context:ShaderContext,uiDrawManager:omr.MUIDrawManager,imageName:str,region:float[2][2],parameters:RenderParamters)->list[int]|None:
		"""renderImage(context, imageName, region, parameters) -> [int, int]/None
		renderImage(context, uiDrawManager, imageName, region, parameters) -> [int, int]/None

		This method allows you to to render the background image used for this shader in the UV texture editor. The image requested will be one of the image names returned by your shader's getAvailableImages() method.

		The implementation must return the dimensions of the image in the 'imageWidth' and 'imageHeight' parameters so that Maya can perform pixel snapping and other resolution-dependent operations.

		The implementation can assume OpenGL context, model view projection matrix, and texture transformations have already been set. A default color of white will be set, however you are free to change this. The magnification filter will be set to either point or bilinear based on user configuration and should not be modified. The values of GL_TEXTURE_WRAP_S and GL_TEXTURE_WRAP_T are undefined on entry, and your implementation is responsible for setting them to appropriate values (e.g. GL_REPEAT).

		The arguments contain the name of the image to render, and the vertex and texture coordinate values to use at each corner of the rectangular image being rendered. Your implementation is responsible for restoring the original the value of any OpenGL state that is modified.

		* context (ShaderContext) - Context of the draw request (e.g. the surface being shaded, shading engine making the request)
		* imageName (string) - Name of the image to render. This corresponds to one of the image names returned by your shader's getAvailableImages() method.
		* region (float[2][2]) - Rectangular region to be rendered. The values of this parameter should be used to populate the vertex and texture coordinates of the rectangle being rendered.
		* parameters (RenderParamters) - Additional parameters on how to render the image. The values reflect the image settings of the UV editor.

		A second version with the uiDrawManager parameter allows you to to render the background image used for this shader in the UV texture editor in viewport 2.0.

		* uiDrawManager (MUIDrawManager) - The UI draw manager, it can be used to draw some simple geometry

		Returns None if method is not implemented : No rendering will occur."""
	def renderSwatchImage(self,image:Any)->Self:
		"""renderSwatchImage(image) -> self

		If the shader specifies to override swatch rendering, then this method must be overridden in order to draw anything into a swatch.

		The shader will only draw a swatch if it has been registered to do so, by providing a valid classification during MFnPlugin::registerNode(). The shader should provide a classification that defines a swatch rendering node such as : "shader/surface/utility/:drawdb/shader/surface/myCustomShader:swatch/myCustomShaderSwatchGenerator" and have "myCustomShaderSwatchGenerator" registered has a swatch renderer : MSwatchRenderRegister.registerSwatchRender("myCustomShaderSwatchGenerator", MHWShaderSwatchGenerator.createObj );

		The default implementation is to draw nothing. The basic logic to draw a swatch is as follows:

		  Determine the size of the swatch required. This is the dimensions of the MImage passed in as an argument. The pixels for the MImage will have been pre-allocated. The format of the pixels is 32-bit R,G,B,A, with 8-bits per channel.
		  Either use an offscreen "swatch context" provided to you or use your own offscreen context. The provided context is available via the MHardwareRenderer class method makeSwatchContextCurrent(). Note that the swatch context may be smaller than the desired image size. In this case the rendering dimensions will be clamped.
		  Either use swatch geometry provided to you, or use your own swatch geometry. The provided geometry is available via the method MHardwareRenderer::referenceDefaultGeometry(). The possible "default" geometries are either a sphere, cube or plane.
		  Either use the provided "default" light and "default" camera or set up your own. Use the methods (getSwatchOrthoCameraSetting(), getSwatchLightDirection()) on MHardwareRenderer to get these defaults.
		  Read back the swatch context into the provided MImage. The convenience method MHardwareRenderer::readSwatchContextPixels() can be used. By default the format of the MImage and the swatch context are the same, so the user does not need to worry about this. The context will read into the pre-allocated MImage pixels.
		  Unreference any swatch geometry used for rendering using MHardwareRenderer::dereferenceGeometry().

		* image [IN/OUT] (MImage) - Image object to which this method must write the rendered swatch. On input the image's dimensions are already set and pixel storage already allocated.

		Returns None if method is not implemented : No rendering will occur."""
	def setUniformParameters(self,parameters:omr.MUniformParameterList,remapCurrentValues:bool=True,dagModifier:om.MDagModifier|None=None)->Self:
		"""setUniformParameters(parameters, remapCurrentValues=True, dagModifier=None) -> self

		Call this method to set the list of uniform parameters this shader uses. Once set, you can use these parameters to access the cached values of shader parameters, including testing when the value has been updated (to minimise the shader state changes). When using this method to manage uniform parameters, Maya will handle the underlyintg attributes, serialization and user interface for you.It is important to call this method whenever the shader parameters are modified (including at load time).This is an optional method - shader implementations are still free to manage uniform (i.e. shader-level) parameters independently if they wish.* parameters (MUniformParameterList) - the list of uniform parameters for this shader
		* remapCurrentValues (bool) - if True (the default), Maya will attempt to initialise the value of new parameters based on any equivalently named parameters that currently exist on the node. Otherwise, the parameters will be setup using default values. Unless you wish to forcibly reset parameter values, the default value of True should be used.
		* dagModifier (MDagModifier) - an optional DG modifier to use when managing the attributes used to represent the geometry parameters on this shader."""
	def setVaryingParameters(self,parameters:omr.MUniformParameterList,remapCurrentValues:bool=True,dagModifier:om.MDagModifier|None=None)->Self:
		"""setVaryingParameters(parameters, remapCurrentValues=True, dagModifier=None) -> self

		Call this method to set the list of varying parameters this shader uses. Once set, you can use these parameters directly to access geometry data for surfaces being shaded. When using this method to manage shader varying parameters, there is no need to override populateRequirements or handle the node interface as Maya will handle parameter setup, presentation and configuration for you.

		It is important to call this method whenever the shader parameters are modified (including at load time).

		This is an optional method - shader implementations are still free to manage geometry parameters independently if they wish.

		* parameters (MUniformParameterList) - the list of varying parameters for this shader
		* remapCurrentValues (bool) - if True (the default), Maya will attempt to initialise the value of new parameters based on any equivalently named parameters that currently exist on the node. Otherwise, the parameters will be setup using default values. Unless you wish to forcibly reset parameter values, the default value of True should be used.
		* dagModifier (MDagModifier) - an optional DG modifier to use when managing the attributes used to represent the geometry parameters on this shader."""
	def transparencyOptions(self)->int:
		"""transparencyOptions() -> int

		This method returns transparency options for usage as hints for Maya's internal draw during a given rendering pass. Parameters are returned via an integer containing masked out bits. By default the mask is set to 0, meaning that the drawing should be treated as regular opaque object drawing. This will generally mean one call per draw pass.

		Options to control transparency are specified by returning one or more masks specified by the following values :
		  - kIsTransparent : Draw as a transparent object. If no transparency overrides are specified, then control of how to draw during a given pass is determined internally by Maya's refresh algorithm, and options the user can set per modelling viewport.
		  - kNoTransparencyFrontBackCull : When kisTransparent is set and this flag is set, do not perform transparency drawing using the internal 2-pass front-face + back-face culling algorithm.
		  - kNoTransparencyPolygonSort : When kisTransparent is set and this flag is set, do not perform transparency drawing using the internal 2-pass drawing of back-to-front sorted triangles."""
class MPxHwShaderNode(om.MPxNode):
	"""Base class for user defined hardware shaders."""
	kWriteNone:int=0
	kWriteVertexArray:int=1
	kWriteNormalArray:int=2
	kWriteColorArrays:int=4
	kWriteTexCoordArrays:int=8
	kWriteAll:int=15
	kDirtyNone:int=0
	kDirtyVertexArray:int=1
	kDirtyNormalArray:int=2
	kDirtyColorArrays:int=4
	kDirtyTexCoordArrays:int=8
	kDirtyAll:int=15
	kIsTransparent:int=1
	kNoTransparencyFrontBackCull:int=2
	kNoTransparencyPolygonSort:int=4
	outColor:om.MObject
	outColorR:om.MObject
	outColorG:om.MObject
	outColorB:om.MObject
	outTransparency:om.MObject
	outTransparencyR:om.MObject
	outTransparencyG:om.MObject
	outTransparencyB:om.MObject
	outMatteOpacity:om.MObject
	outMatteOpacityR:om.MObject
	outMatteOpacityG:om.MObject
	outMatteOpacityB:om.MObject
	outGlowColor:om.MObject
	outGlowColorR:om.MObject
	outGlowColorG:om.MObject
	outGlowColorB:om.MObject
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def bind(self,request:MDrawRequest,view:M3dView)->Self:
		"""bind(request, view) -> self

		This method is invoked for hardware rendering to Maya's 3D view.

		This is the preferred method of interactive feedback and performance. the "gl" version should be used for batch hardware rendering.

		This method is called to set up the OpenGL state.  It would typically ensure that textures were bound and that any specific OpenGL extensions are enabled.  A status code of MS::kSuccess should be returned unless there was a problem during the display, such as insufficient memory or required input data is missing or invalid.

		* request (MDrawRequest) - the draw request.
		* view (M3dView) - the view in which to draw."""
	def colorsPerVertex(self)->int:
		"""colorsPerVertex() -> int

		This method returns the number of color values per vertex that the hw shader node would like to receive from Maya.  Maya will attempt to provide all the color data that the shader would like but it will never provide more data that is actually available in the shape.  The color sets returned by getColorSetNames() will override the number of color sets specified by colorsPerVertex(). If you do not override this method or getColorSetNames(), Maya will provide no colors per vertex.

		Returns the number of color values desired"""
	def currentPath(self)->om.MDagPath:
		"""currentPath() -> MDagPath

		This method returns a reference to the current path that the shader is invoked for.

		The path is only valid before a call to any of the attribute specifying routines:

		   normalsPerVertex()
		   colorsPerVertex()
		   getColorSetNames()
		   texCoordsPerVertex()
		   getTexCoordSetNames()
		   hasTransparency()
		   provideVertexIDs()

		The path is not guaranteed to be valid at any other time.

		This method allows the plugin to return attribute queries which are relative to a specific path or object.

		For example, the plugin can retrieve the MObject from the path, then use the MFnMesh class on the MObject, assuming the object is a polygonal surface. Through MFnMesh the code can query the actual number of texture coordinate sets on the surface and return appropriate values for the getTexCoordSetNames() routine.

		The [gl]bind(), [gl]unbind() and [gl]geometry() routines already have access to a dag path which is the same path as the one which can be retrieved via this method.

		For performance reasons, it is recommended that for those methods the MDagPath passed in as an argument should be used.

		Returns an MDagPath. Note that this path can be invalid
		Use MDagPath.isValid() to confirm the validity of the path."""
	def currentShadingEngine(self)->om.MObject:
		"""currentShadingEngine() -> MObject

		This method returns an MObject to the shading engine that is currently being rendered. This method will only return a valid MObject during the following calls:

		  normalsPerVertex()
		  colorsPerVertex()
		  getColorSetNames()
		  texCoordsPerVertex()
		  getTexCoordSetNames()
		  hasTransparency()
		  provideVertexIDs()
		  getAvailableImages()
		  bind(), glBind()
		  geometry(), glGeometry()
		  unbind(), glUnbind()"""
	def dirtyMask(self)->int:
		"""dirtyMask() -> int

		This method returns a "dirty" mask that indicates which geometry items have changed from the last invocation of the plugin to draw. The mask is valid at the time that geometry() or glGeometry() is called and at no other time.

		Note that this mask is relative to the geometry for the current object (path) being drawn by the shader. The current path is the MDagPath argument passed in via the geometry routines.

		In general the mask will mark the geometry as not being dirty.

		Scenarios where the geometry will be marked dirty include:

		  Whenever a geometry attribute changes. For example positions or normals are modified.
		  Whenever the attributes being requested changes from the previous invocation of the shader. For example, if in the previous invocation the plugin asks for position only, and in the current invocation asks for position and normals, then the geometry attributes returned will have changed and thus be marked "dirty".

		Returns the dirty mask which can be bit 'AND'ed against the values:
		  kDirtyNone
		  kDirtyVertexArray
		  kDirtyNormalArray
		  kDirtyColorArrays
		  kDirtyTexCoordArrays
		  kDirtyAll"""
	def geometry(self,request:MDrawRequest,view:M3dView,prim:int,writable:int,indexCount:int,indexArray:Any,vertexCount:int,vertexIDs:Any,vertexArray:Any,normalCount:int,normalArrays:Any,colorCount:int,colorArrays:Any,texCoordCount:int,texCoordArrays:Any)->Self:
		"""geometry(request, view, prim, writable, indexCount, indexArray, vertexCount, vertexIDs, vertexArray, normalCount, normalArrays, colorCount, colorArrays, texCoordCount, texCoordArrays) -> self

		This method is invoked for hardware rendering to Maya's 3D view.

		This is the preferred method of interactive feedback and performance. the "gl" version should be used for batch hardware rendering.

		This method does all the actual OpenGL drawing.  The arguments contain all the data to successfully call glDrawElements or glDrawRangeElements.  It is possible that there will be multiple calls to this method surrounded by a single call to bind() and unbind().

		Note 1.
		The array of vertex IDs returned corresponds to each triangle's vertex. This allows access to associated blind data per vertex. The vertexIDs array allows querying of information such as color per vertex etc.

		Note 2.
		The arrays passed to this method can contain sparse information.  Check array positions against None to ensure that the array information item is valid.

		It is necessary to use the indexArray to access information contained in the data arrays.

		* request (MDrawRequest) - the draw request.
		* view (M3dView) - the view in which to draw.
		* prim (int) - the type of primitive to draw.  This is one of the values accepted by glBegin().  Typically it will be GL_TRIANGLES but it could be any of the others.
		* writable (int) this is a mask which indicates which of the various array arguments can be modified in place.  If a bit in writable is set then you can modify corresponding data array (after casting it to a non-const type).  If the bit is not set in writable then you must not> modify the data since it points to internal Maya storage.  You can test the bits in writeable against the values
		:  kWriteNone
		  kWriteVertexArray
		  kWriteNormalArray
		  kWriteColorArrays
		  kWriteTexCoordArrays
		  kWriteAll
		* indexCount (int) - specifies both the number of indices to draw and the size of the indexArray argument.
		* indexArray (buffer of int values) - the array of index values.  This array is in a format suitable for passing as the indices argument to glDrawElements() or glDrawRangeElements().  See the OpenGL documentation for details on calling these routines.
		* vertexCount (int) - the number of elements in the vertexArray, the normalArray, each of the colorArrays, and each of the texCoordArrays.
		* vertexIDs (buffer - int values) - the component IDs of the vertices in vertexArray. This array is only provided if it was requested by overriding the provideVertexIDs() method to return True.
		* vertexArray (buffer - float values) - the array of vertex data.  Currently, this is always 3 element floating point values.  This data is in a format suitable for passing to glVertexPointer().  See the OpenGL documentation for details.
		* normalCount (int) - the number of individual "normal" arrays that are being provided in normalArrays.  See the description of normalsPerVertex method below for details.
		* normalArrays (array of buffer - float values) - the normal (and tangent) data suitable. There may be 0, 1, 2, or 3 "normal" arrays.  See the description of the normalsPerVertex method below for details.
		* colorCount (int) - the number of individual color arrays.
		* colorArrays (array of buffer - float values) - the arrays of color data.  The first set of color data is pointed to by colorArrays[0].  Each color array contains vertexCount color values, each of which is 4 floating point values long and represents the red, green, blue, and alph values on a 0 to 1 scale.  Each individual array is suitable for passing to glColorPointer().
		* texCoordCount (int) - the number of texture coordinate arrays. Each array contains one set of UV texture coordinates.
		* texCoordArrays (array of buffer - float values) - the arrays of texture coordinate data. The first set of texture coordinate data is pointed to by texCoordArrays[0].  Each array contains vertexCount coordinate values, each of which is 2 floating point values long.  Each individual array is suitable for passing to glTexCoordPointer()."""
	def getAvailableImages(self,uvSetName:str)->list[list[str]|None]:
		"""getAvailableImages(uvSetName) -> list of strings/None

		Maya will call this method to get your shader's list of images which are available for use in the UV texture editor for the UV set specified. Typically, this list will include one entry for each texture using the specified UV set, however, your shader is free to return as many images as you wish (for example, blending between two textures, texture alpha masks, artificially shaded views of bump/normal maps, etc). Your shader's renderImage() method will be used to render the images themselves.

		* uvSetName (string) - Name of a UV set the channel list should be filtered against.

		Returns the names of the images this shader defines which are valid for the uvSetName specified.
		Returns None if method is not implemented : Use the default behaviour."""
	def getColorSetNames(self,names:Any)->int:
		"""getColorSetNames(names) -> int

		This method returns an array of color per vertex set names. Maya will attempt to provide color per vertex data from these maps in the corresponding array element in the colorArrays argument to the geometry method.  For example, if the names[2] is "cpv56" then colorArrays[2] will be the array of values from cpv56, or None if the shape being rendered does not have a color set of that name. Ifthis method is not overridden an empty list of names will be returned,and Maya will use colorsPerVertex() to determine how many color setsto provide.

		* names [IN/OUT] (list of string) - a string array holding the names of the color per vertex sets from which color data should be extracted.

		Returns the number of elements in the names array."""
	@staticmethod
	def getHwShaderNode(object:om.MObject)->MPxHwShaderNode:
		"""getHwShaderNode(object) -> MPxHwShaderNode

		This is a static convenience method to be able to get an MPxHwShaderNode from an MObject provided by a swatch generator class (Class derived from MSwatchRenderRegister).

		* object (MObject) - The object to examine."""
	def getTexCoordSetNames(self,names:Any)->int:
		"""getTexCoordSetNames(names) -> int

		This method returns an array of texture coordinate set names. Maya will attempt to provide texture coordinates from these maps in the corresponding array element in the texCoordArrays argument to the geometry method.  For example, if the names[2] is "uvSet3" then texCoordArrays[2] will be the array of values from uvSet3. If this method is not overridden an empty list of names will be returned, and Maya will use texCoordsPerVertex() to determine how many uv sets to provide.

		* names [IN/OUT] (list of string) - a string array holding the names of the uvSets from which texture coordinate data should be extracted.

		Returns the number of elements in the names array."""
	def glBind(self,shapePath:om.MDagPath)->Self:
		"""glBind(shapePath) -> self

		This method should only be overridden for hardware rendering.

		The implementation can assume the graphics context and model view projection matrix have already been set.

		This method will be invoked once per frame and should be overridden to allocate any resources needed for the draw. For example, binding vertex programs, fragment programs, or allocating textures. A status code of MS::kSuccess should be returned unless there was a problem such as insufficient memory or required input data is missing or        invalid.

		* shapePath (MDagPath) - Path to the surface being drawn."""
	def glGeometry(self,shapePath:om.MDagPath,prim:Any,writable:Any,indexCount:Any,indexArray:Any,vertexCount:Any,vertexIDs:Any,vertexArray:Any,normalCount:Any,normalArrays:Any,colorCount:Any,colorArrays:Any,texCoordCount:Any,texCoordArrays:Any)->Self:
		"""glGeometry(shapePath, prim, writable, indexCount, indexArray, vertexCount, vertexIDs, vertexArray, normalCount, normalArrays, colorCount, colorArrays, texCoordCount, texCoordArrays) -> self

		This method should only be overridden for hardware rendering.

		The implementation can assume graphics context and model view projection matrix have already been set.

		This method does all the actual OpenGL drawing.  The arguments contain all the data to successfully call glDrawElements or glDrawRangeElements.  It is possible that there will be multiple calls to this method surrounded by a single call to bind() and unbind().

		Note 1.
		The array of vertex IDs returned corresponds to each triangle's vertex. This allows access to associated blind data per vertex. The vertexIDs array allows querying of information such as color per vertex etc.

		Note 2.
		The arrays passed to this method can contain sparse information.  Check array positions against None to ensure that the array information item is valid.

		It is necessary to use the indexArray to access information contained in the data arrays.

		* shapePath (MDagPath) - Path to the surface being drawn.
		See geometry() description for detail on the other parameters."""
	def glUnbind(self,shapePath:om.MDagPath)->Self:
		"""glUnbind(shapePath) -> self

		This method should only be overridden for hardware rendering.

		The implementation can assume the graphics context and model view projection matrix have already been set.

		This method will be invoked once per frame and should be overridden to deallocate any resources used to draw. It's important that all resources be released when a batch hardware render has occured because the graphics context will be deleted. It may be desireable to override the other version of bind/unbind to keep track of whether the draw is for the 3D view or the batch hardware renderer. This information could then be used to better track the reuse of resources and optimize performance.

		A status code of MS::kSuccess should be returned unless there was a problem.

		* shapePath (MDagPath) - Path to the surface being drawn."""
	def hasTransparency(self)->bool:
		"""hasTransparency() -> bool

		This method returns a boolean value that indicates whether the object will be drawn transparently or not.  Transparent objects must be drawn after all the opaque objects in the scene or they will not display correctly.  Maya uses the return value to determine when it can draw this shape.

		Note : The functionality in this method has been subsumed by the transparencyOptions() method. It is recommended that shader node writers use this newer method as it provides greater control over how transparency is interpreted by Maya's refresh mechanism.

		For backward compatibility, if this method is specified and returns True, it will override the transparencyOptions() method.

		Returns True if the object will be transparent or False if it will not."""
	def invertTexCoords(self)->bool:
		"""invertTexCoords() -> bool

		Specifies whether this shader requires inverted texture coordinates. (i.e. where the top-left hand corner of UV space is (0,0) instead of the bottom-left corner).

		By default, this method will return False to ensure compatibility with existing shader code."""
	def normalsPerVertex(self)->int:
		"""normalsPerVertex() -> int

		Specifies how many normals per vertex the HW shader would like Maya to provide.  This can range from 0 to 3.  The first normal is the surface normal.  The second "normal" is the primary tangent (generally the "u" direction).  The third "normal" is the secondary tangent or the binormal (generally the "v" direction). Together, the normal, tangent and binormal form an orthogonal basis frequently named "tangent space basis".

		The tangent and binormal vectors are guaranteed to be normalized and orthogonal to the surface normal. Please note that extracting the tangent and/or binormal requires expensive calculations, that will slow down refresh time substantially. In a future version, Maya may cache the resulting tangent space basis; in the meantime, only ask for more than one normal per vertex if they are absolutely required.

		Also note that the tangent and binormal calculation requires a uv map. Currently, they are always computed from the first available uv map; if there is no uv mapping on the surface, Maya will only provide surface normals in the geometry call, regardless of the value returned by normalsPerVertex().

		If you do not override this method, Maya will provide 1 normal per vertex.

		Maya will automatically and silently clamp the result of this function to the [0,3] range.

		COMPATIBILITY NOTE: Automatic tangent space basis calculation is only supported starting with Maya 4.0.1. Maya 4.0 supported a different scheme that was much more complicated and no longer supported.

		Returns the number of normal values desired. (0 = none, 1 = surface normal only, 2 = surface normal + tangent, 3 = surface normal + tangent + binormal)"""
	def provideVertexIDs(self)->bool:
		"""provideVertexIDs() -> bool

		This method returns a boolean value that indicates whether a map of the vertex IDs will be provided to the geometry method.

		Returns True if vertex IDs should be provided to the geometry method."""
	@overload
	def renderImage(self,imageName:str,region:float[2][2],parameters:RenderParamters)->list[int]|None:
		"""renderImage(imageName, region, parameters) -> [int, int]/None
		renderImage(uiDrawManager, imageName, region, parameters) -> [int, int]/None

		This method allows you to to render the background image used for this shader in the UV texture editor. The image requested will be one of the image names returned by your shader's getAvailableImages() method.

		The implementation must return the dimensions of the image in the 'imageWidth' and 'imageHeight' parameters so that Maya can perform pixel snapping and other resolution-dependent operations.

		The implementation can assume OpenGL context, model view projection matrix, and texture transformations have already been set. A default color of white will be set, however you are free to change this. The magnification filter will be set to either point or bilinear based on user configuration and should not be modified. The values of GL_TEXTURE_WRAP_S and GL_TEXTURE_WRAP_T are undefined on entry, and your implementation is responsible for setting them to appropriate values (e.g. GL_REPEAT).

		The arguments contain the name of the image to render, and the vertex and texture coordinate values to use at each corner of the rectangular image being rendered. Your implementation is responsible for restoring the original the value of any OpenGL state that is modified.

		* imageName (string) - Name of the image to render. This corresponds to one of the image names returned by your shader's getAvailableImages() method.
		* region (float[2][2]) - Rectangular region to be rendered. The values of this parameter should be used to populate the vertex and texture coordinates of the rectangle being rendered.
		* parameters (RenderParamters) - Additional parameters on how to render the image. The values reflect the image settings of the UV editor.

		A second version with the uiDrawManager parameter allows you to to render the background image used for this shader in the UV texture editor in viewport 2.0.

		* uiDrawManager (MUIDrawManager) - The UI draw manager, it can be used to draw some simple geometry

		Returns None if method is not implemented : No rendering will occur."""
	@overload
	def renderImage(self,uiDrawManager:omr.MUIDrawManager,imageName:str,region:float[2][2],parameters:RenderParamters)->list[int]|None:
		"""renderImage(imageName, region, parameters) -> [int, int]/None
		renderImage(uiDrawManager, imageName, region, parameters) -> [int, int]/None

		This method allows you to to render the background image used for this shader in the UV texture editor. The image requested will be one of the image names returned by your shader's getAvailableImages() method.

		The implementation must return the dimensions of the image in the 'imageWidth' and 'imageHeight' parameters so that Maya can perform pixel snapping and other resolution-dependent operations.

		The implementation can assume OpenGL context, model view projection matrix, and texture transformations have already been set. A default color of white will be set, however you are free to change this. The magnification filter will be set to either point or bilinear based on user configuration and should not be modified. The values of GL_TEXTURE_WRAP_S and GL_TEXTURE_WRAP_T are undefined on entry, and your implementation is responsible for setting them to appropriate values (e.g. GL_REPEAT).

		The arguments contain the name of the image to render, and the vertex and texture coordinate values to use at each corner of the rectangular image being rendered. Your implementation is responsible for restoring the original the value of any OpenGL state that is modified.

		* imageName (string) - Name of the image to render. This corresponds to one of the image names returned by your shader's getAvailableImages() method.
		* region (float[2][2]) - Rectangular region to be rendered. The values of this parameter should be used to populate the vertex and texture coordinates of the rectangle being rendered.
		* parameters (RenderParamters) - Additional parameters on how to render the image. The values reflect the image settings of the UV editor.

		A second version with the uiDrawManager parameter allows you to to render the background image used for this shader in the UV texture editor in viewport 2.0.

		* uiDrawManager (MUIDrawManager) - The UI draw manager, it can be used to draw some simple geometry

		Returns None if method is not implemented : No rendering will occur."""
	def renderSwatchImage(self,image:Any)->Self|None:
		"""renderSwatchImage(image) -> self/None

		If the shader specifies to override swatch rendering, then this method must be overridden in order to draw anything into a swatch.

		The shader will only draw a swatch if it has been registered to do so, by providing a valid classification during MFnPlugin::registerNode(). The shader should provide a classification that defines a swatch rendering node such as : "shader/surface/utility/:drawdb/shader/surface/myCustomShader:swatch/myCustomShaderSwatchGenerator" and have "myCustomShaderSwatchGenerator" registered has a swatch renderer : MSwatchRenderRegister.registerSwatchRender("myCustomShaderSwatchGenerator", MHWShaderSwatchGenerator.createObj );

		The default implementation is to draw nothing. The basic logic to draw a swatch is as follows:

		  Determine the size of the swatch required. This is the dimensions of the MImage passed in as an argument. The pixels for the MImage will have been pre-allocated. The format of the pixels is 32-bit R,G,B,A, with 8-bits per channel.
		  Either use an offscreen "swatch context" provided to you or use your own offscreen context. The provided context is available via the MHardwareRenderer class method makeSwatchContextCurrent(). Note that the swatch context may be smaller than the desired image size. In this case the rendering dimensions will be clamped.
		  Either use swatch geometry provided to you, or use your own swatch geometry. The provided geometry is available via the method MHardwareRenderer::referenceDefaultGeometry(). The possible "default" geometries are either a sphere, cube or plane.
		  Either use the provided "default" light and "default" camera or set up your own. Use the methods (getSwatchOrthoCameraSetting(), getSwatchLightDirection()) on MHardwareRenderer to get these defaults.
		  Read back the swatch context into the provided MImage. The convenience method MHardwareRenderer::readSwatchContextPixels() can be used. By default the format of the MImage and the swatch context are the same, so the user does not need to worry about this. The context will read into the pre-allocated MImage pixels.
		  Unreference any swatch geometry used for rendering using MHardwareRenderer::dereferenceGeometry().

		* image [IN/OUT] (MImage) - Image object to which this method must write the rendered swatch. On input the image's dimensions are already set and pixel storage already allocated.

		Returns None if method is not implemented : No rendering will occur."""
	def supportsBatching(self)->bool:
		"""supportsBatching() -> bool

		Specifies whether or not this shader supports batched rendering of shapes.

		In normal rendering, a shader is invoked using bind/geometry/unbind (or glBind/glGeometry/glUnbind) once for each shape being rendered. When a shader is used in batched rendering mode however, bind is called once, a series of geometry calls are made for each shape being rendered, followed by a single call to unbind (and similarly for glBind, glGeometry and glUnbind). As shader binding/unbinding can be expensive, batched rendering can significantly improve rendering performance. The more (particularly expensive) operations that can be moved out of the geometry/glGeometry methods the greater the performance improvement is. Ideally, only shape specific operations (such as binding geometry arrays and shape matrices) should be left in the geometry methods.

		It is important to note that your shader can only use batched rendering mode if there is no shape (i.e. dag path) specific code in bind, glBind, unbind, or glUnbind. If any of these methods perform shape specific processing, this code must either be moved into geometry/glGeometry, or you must return False in this method to indicate batching should be disabled for this shader.

		By default, this method will return False to ensure compatibility with existing shader code."""
	def texCoordsPerVertex(self)->int:
		"""texCoordsPerVertex() -> int

		This method returns the number of texture coordinate values per vertex that the hw shader node would like to receive from Maya. Maya will attempt to provide all the texture coordinate data that the shader would like but it will never provide more data than is actually available in the shape.  The uv sets returned by getTexCoordSetNames() will override the number of uv sets specified by texCoordsPerVertex(). If you do not override this method or getTexCoordSetNames(), Maya will provide no texture coordinates per vertex.

		Note: Currently, Maya only retains 2 dimensional texture coordinate data but this may change in a future release.

		Returns the number of texture coordinate values desired"""
	def transparencyOptions(self)->int:
		"""transparencyOptions() -> int

		This method returns transparency options for usage as hints for Maya's internal draw during a given rendering pass. Parameters are returned via an integer containing masked out bits. By default the mask is set to 0, meaning that the drawing should be treated as regular opaque object drawing. This will generally mean one call per draw pass.

		Options to control transparency are specified by returning one or more masks specified by the values
		:

		  kIsTransparent : Draw as a transparent object. If no transparency overrides are specified, then control of how to draw during a given pass is determined internally by Maya's refresh algorithm, and options the user can set per modelling viewport.
		  kNoTransparencyFrontBackCull : When kisTransparent is set and this flag is set, do not perform transparency drawing using the internal 2-pass front-face + back-face culling algorithm.
		  kNoTransparencyPolygonSort : When kisTransparent is set and this flag is set, do not perform transparency drawing using the internal 2-pass drawing of back-to-front sorted triangles.

		Note : Setting the "hasTransparency()" method to True will override this method. This is for backward compatibility with behaviour on existing hardware shader nodes. It is recommended that shaders use the "transparencyOptions()" override, and not longer use the older "hasTransparency()" override from their shader classes.

		Retuns an integer containing the appropriate options set via masks."""
	def unbind(self,request:MDrawRequest,view:M3dView)->Self:
		"""unbind(request, view) -> self

		This method is invoked for hardware rendering to Maya's 3D view.

		This is the preferred method of interactive feedback and performance. the "gl" version should be used for batch hardware rendering.

		This method is called to restore the OpenGL state.  Specifically, it must disable any OpenGL extensions that the matching bind() method may have enabled.  This is necessary to ensure that the rest of Maya's drawing code continues to work correctly.  A status code of MS::kSuccess should be returned unless there was a problem such as insufficient memory or required input data is missing or invalid.

		The arguments passed to this method are the same ones that were passed to the bind() method.

		* request (MDrawRequest) - the draw request.
		* view (M3dView) - the view in which to draw."""
class MPxLocatorNode(om.MPxNode):
	"""Base class for user defined locators."""
	underWorldObject:om.MObject
	localPosition:om.MObject
	localPositionX:om.MObject
	localPositionY:om.MObject
	localPositionZ:om.MObject
	worldPosition:om.MObject
	worldPositionX:om.MObject
	worldPositionY:om.MObject
	worldPositionZ:om.MObject
	localScale:om.MObject
	localScaleX:om.MObject
	localScaleY:om.MObject
	localScaleZ:om.MObject
	nodeBoundingBox:om.MObject
	nodeBoundingBoxMin:om.MObject
	nodeBoundingBoxMinX:om.MObject
	nodeBoundingBoxMinY:om.MObject
	nodeBoundingBoxMinZ:om.MObject
	nodeBoundingBoxMax:om.MObject
	nodeBoundingBoxMaxX:om.MObject
	nodeBoundingBoxMaxY:om.MObject
	nodeBoundingBoxMaxZ:om.MObject
	nodeBoundingBoxSize:om.MObject
	nodeBoundingBoxSizeX:om.MObject
	nodeBoundingBoxSizeY:om.MObject
	nodeBoundingBoxSizeZ:om.MObject
	center:om.MObject
	boundingBoxCenterX:om.MObject
	boundingBoxCenterY:om.MObject
	boundingBoxCenterZ:om.MObject
	matrix:om.MObject
	inverseMatrix:om.MObject
	worldMatrix:om.MObject
	worldInverseMatrix:om.MObject
	parentMatrix:om.MObject
	parentInverseMatrix:om.MObject
	visibility:om.MObject
	intermediateObject:om.MObject
	isTemplated:om.MObject
	instObjGroups:om.MObject
	objectGroups:om.MObject
	objectGrpCompList:om.MObject
	objectGroupId:om.MObject
	objectGroupColor:om.MObject
	useObjectColor:om.MObject
	objectColor:om.MObject
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def boundingBox(self)->om.MBoundingBox:
		"""boundingBox() -> MBoundingBox

		This method should be overridden to return a bounding box for the locator.
		If this method is overridden, then MPxLocatorNode.isBounded should also be overridden to return True."""
	def closestPoint(self,rayPoint:om.MPoint,rayDir:om.MVector)->om.MPoint:
		"""closestPoint(rayPoint, rayDir) -> MPoint

		Returns the point on the locator, in the locator's local space, which is closest along the specified ray.

		By default, the locator's origin (0, 0, 0) is returned.

		This is currently only used by Maya during single selection. See useClosestPointForSelection() for further details on that.

		* rayPoint (MPoint) - The base point defining the ray in space
		* rayDir (MVector) - The ray direction in space"""
	def color(self,status:Any)->int:
		"""color(status) -> int

		This method returns the index of the color that is the default draw color for the given display status.  The index should be used with the methods of M3dView.  The value is not an index into the OpenGL color table.

		The index that is returned will be into the active, dormant, or template color tables depending on the display status passed in.

		* displayStatus (int) - display status. See M3dView.displayStatus() for a list of valid status."""
	def colorRGB(self,status:Any)->om.MColor:
		"""colorRGB(status) -> MColor

		This method returns the RGB values of the default draw color for the given display status.

		* displayStatus (int) - display status. See M3dView.displayStatus() for a list of valid status."""
	def draw(self,view:M3dView,path:om.MDagPath,style:int,status:int)->Self:
		"""draw(view, path, style, status) -> self

		Overriding this method allows the drawing of custom geometry using standard OpenGL calls.  The OpenGL state should be left in the same state that it was in previously.  The OpenGL routine glPushAttrib may be used to make this easier.

		When this routine is called, the following conditions may be assumed:
		 - the correct transform matrix will be loaded for the locator, so the geometry should be drawn in local space
		 - the correct default color will be set for wire frame drawing given the object's state (eg active, dormant, etc.)
		 - the object is not invisible or hidden
		 - if the object has a bounding box, then the bounding box is at least partially in the frustum


		As a convenience, this draw method will also be used by OpenGL's selection mechanism to determine whether this object gets selected by a particular mouse event.  The user does not need to write a separate selection routine.

		* view (M3dView) - 3D view that is being drawn into.
		* path (MDagPath) - to the parent (transform node) of this locator in the DAG.
		If there is a shape node parented directly beneath the transform node, you can access it
		by calling MDagPath.extendToShape().
		* style (int) - style to draw object in. See M3dView.displayStyle() for a list of valid styles.
		* status (int) - selection status of object. See M3dView.displayStatus() for a list of valid status.

		                DEPRECATED in 2024, draw is no longer supported."""
	def drawLast(self)->bool:
		"""drawLast() -> bool

		Indicates that this locator should be the last item draw in a given refresh cycle.  Objects drawn out-of-order will not preserve the proper transparency sorting.  Conflicts among multiple objects with the drawLast indicator set to TRUE will be resolved by their order in the Outliner, where they will be drawn top-to-bottom.

		The default return value is True."""
	def excludeAsLocator(self)->bool:
		"""excludeAsLocator() -> bool

		When the modelPanel is set to not draw locators, returing True will also not draw the custom locator. If False is returned, the custom locator will also be drawn.

		The default return value is True."""
	def isBounded(self)->bool:
		"""isBounded() -> bool

		This method should be overridden to return True if the user supplies a bounding box routine.  Supplying a bounding box routine makes refresh and selection more efficient."""
	def isTransparent(self)->bool:
		"""isTransparent() -> bool

		Indicates that this locator uses transparency during ::draw method calls. Objects with transparency must be drawn in a special queue, i.e. after all opaque objects are drawn.

		The default return value is False."""
	def useClosestPointForSelection(self)->bool:
		"""useClosestPointForSelection() -> bool

		Determines whether Maya should call closestPoint() when doing single selection.

		When doing single selection Maya generally chooses the object closest to the selection ray. For locators it first does a hit test by calling the locator's draw method to determine if any part of it lies within the selection box. If the hit test succeeds Maya will add the locator to the list of objects being considered for selection and will use the center of the locator (i.e. its local origin) in determining its distance from the selection ray. This works well for locators which mark a single point in space, with no offset, but may not work as well for more complex locators.

		If this method is overridden to return True, then rather than using the locator's center to determine its distance from the selection ray, Maya will pass the ray to the closestPoint() method and use the point it returns. Note that you will have override closestPoint() as well to provide an appropriate point."""
	def getShapeSelectionMask(self)->om.MSelectionMask:
		"""getShapeSelectionMask() -> MSelectionMask

		This routine can be overridden to provide information aboutthe selection mask of the locator. By default the selection maskfor locators is returned."""
class MPxManipContainer(om.MPxNode):
	"""Parent class of all user defined manipulators."""
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def addCircleSweepManip(self,manipName:str,angleName:str)->om.MDagPath:
		"""addCircleSweepManip(manipName, angleName) -> MDagPath

		This method creates a CircleSweepManip and adds it to
		the MPxManipContainer container.

		* manipName (string) manipulator name
		* angleName (string) angle name

		Returns the new CircleSweepManip"""
	def addCurveSegmentManip(self,manipName:str,startParamName:str,endParamName:str)->om.MDagPath:
		"""addCurveSegmentManip(manipName, startParamName, endParamName ) -> MDagPath

		This method creates a CurveSegmentManip and adds it to
		the MPxManipContainer container.

		* manipName (string) manipulator name
		* startParamName (string) start param name
		* endParamName (string) end param name

		Returns the new CurveSegmentManip"""
	def addDirectionManip(self,manipName:str,directionName:str)->om.MDagPath:
		"""addDirectionManip(manipName, directionName) -> MDagPath

		This method creates a DirectionManip and adds it to
		the MPxManipContainer container.

		* manipName (string) manipulator name
		* directionName (string) direction name

		Returns the new DirectionManip"""
	def addDiscManip(self,manipName:str,angleName:str)->om.MDagPath:
		"""addDiscManip(manipName, angleName) -> MDagPath

		This method creates a DiscManip and adds it to
		the MPxManipContainer container.

		* manipName (string) manipulator name
		* angleName (string) angle name

		Returns the new DiscManip"""
	def addDistanceManip(self,manipName:str,distanceName:str)->om.MDagPath:
		"""addDistanceManip(manipName, distanceName) -> MDagPath

		This method creates a DistanceManip and adds it to
		the MPxManipContainer container.

		* manipName (string) manipulator name
		* distanceName (string) distance name

		Returns the new DistanceManip"""
	def addFreePointTriadManip(self,manipName:str,pointName:str)->om.MDagPath:
		"""addFreePointTriadManip(manipName, pointName) -> MDagPath

		This method creates a FreePointTriadManip and adds it to
		the MPxManipContainer container.

		* manipName (string) manipulator name
		* pointName (string) point name

		Returns the new FreePointTriadManip"""
	def addManipToPlugConversion(self,plug:om.MPlug)->int:
		"""addManipToPlugConversion(plug) -> unsigned int

		This method adds a manipulator to plug converter for the specified
		plug. The converter must be implemented in the manipToPlugConversion()
		virtual method of this class.

		NOTE: The conversion methods and callback methods of this class should
		not be mixed.  The conversion methods are: addManipToPlugConversion(),
		addManipToPlugConversion() The callback methods are:
		addPlugToManipConversionCallback() addManipToPlugConversionCallback()

		* plug (MPlug) - The plug for which the converter is being requested.

		Returns the index used to identify the plug inside the
		manipToPlugConversion() method."""
	def addMPxManipulatorNode(self,manipTypeName:str,manipName:str,proxyManip:Any)->None:
		"""addMPxManipulatorNode(manipTypeName, manipName, proxyManip) -> None

		This method creates a custom MPxManipulatorNode and adds it to the
		MPxManipContainer container.

		* manipTypeName (string) manipulator name
		* manipName (string) name of the manip
		Returns a pointer to the new manipulator"""
	def addPlugToInViewEditor(self,plug:om.MPlug)->None:
		"""addPlugToInViewEditor(plug)

		Adds a plug to the In-View Editor.

		The first such call will cause the In-View Editor to
		be displayed automatically with the custom manip.

		Should be called from connectToDependNode().

		* plug (MPlug) - The plug that the slider should control"""
	def addPlugToManipConversion(self,manipIndex:int)->None:
		"""addPlugToManipConversion(manipIndex)

		This method adds a plug to manipulator converter for the specified
		manipulator value (e.g. the start point of a distance manip). The
		converter must be implemented in the plugToManipConversion() virtual
		method of this class.

		NOTE: The conversion methods and callback methods of this class should
		not be mixed.  The conversion methods are: addManipToPlugConversion(),
		addManipToPlugConversion() The callback methods are:
		addPlugToManipConversionCallback() addManipToPlugConversionCallback()

		* manipIndex (int) - The index of the manipulator value for which the
		converter is being requested. The index is determined by calling the
		appropriate method of the manipulator's functionset (e.g.
		MFnDistanceManip::startPointIndex)."""
	def addPointOnCurveManip(self,manipName:str,paramName:str)->om.MDagPath:
		"""addPointOnCurveManip(manipName, paramName) -> MDagPath

		This method creates a PointOnCurveManip and adds it to
		the MPxManipContainer container.

		* manipName (string) manipulator name
		* paramName (string) param name

		Returns the new PointOnCurveManip"""
	def addPointOnSurfaceManip(self,manipName:str,paramName:str)->om.MDagPath:
		"""addPointOnSurfaceManip(manipName, paramName) -> MDagPath

		This method creates a PointOnSurfaceManip and adds it to
		the MPxManipContainer container.

		* manipName (string) manipulator name
		* paramName (string) param name

		Returns the new PointOnSurfaceManip"""
	def addRotateManip(self,manipName:str,rotationName:str)->om.MDagPath:
		"""addRotateManip(manipName, rotationName) -> MDagPath

		This method creates a RotateManip and adds it to
		the MPxManipContainer container.

		* manipName (string) manipulator name
		* rotationName (string) name of the rotation vector

		Returns the dag path to the new rotate manipulator"""
	def addScaleManip(self,manipName:str,scaleName:str)->om.MDagPath:
		"""addScaleManip(manipName, scaleName) -> MDagPath

		This method creates a ScaleManip and adds it to
		the MPxManipContainer container.

		* manipName (string) manipulator name
		* scaleName (string) name of the scale vector

		Returns the dag path to the new scale manipulator"""
	def addStateManip(self,manipName:str,stateName:str)->om.MDagPath:
		"""addStateManip(manipName, stateName) -> MDagPath

		This method creates a StateManip and adds it to
		the MPxManipContainer container.

		* manipName (string) manipulator name
		* stateName (string) state name

		Returns the new StateManip"""
	def addToggleManip(self,manipName:str,toggleName:str)->om.MDagPath:
		"""addToggleManip(manipName, toggleName) -> MDagPath

		This method creates a ToggleManip and adds it to
		the MPxManipContainer container.

		* manipName (string) manipulator name
		* toggleName (string) toggle name

		Returns the new ToggleManip"""
	@staticmethod
	def addToManipConnectTable(typeId:Any)->None:
		"""addToManipConnectTable( typeId )

		This method adds the user defined node as an entry in the
		manipConnectTable so that when this node is selected the user can
		use the show manip tool to get the user defined manipulator
		associated with this node. Note that the name of the manipulator
		node has to be the name of the plug-in node appended with 'Manip'.

		* mid (MTypeId) - Id of the user defined node"""
	def connectToDependNode(self,node:om.MObject)->None:
		"""connectToDependNode(node) -> None

		This method connects the manipulator to the dependency node. This
		is a virtual method and needs to be overridden from the plug-in.

		* node (MObject) - the node to which the manipulator should be connected"""
	def createChildren(self)->None:
		"""createChildren() -> None

		This method should be overridden in user defined manipulators.
		This method is called after the user node derived from
		MPxManipContainer is set up."""
	def doPress(self)->None:
		"""doPress() -> None

		This method gets called when the manipulator receives a mouse down event.

		Returns None if successful.  Otherwise, returns MStatus.kUnknownParameter
		to allow Maya to further process the event."""
	def doDrag(self)->None:
		"""doDrag() -> None

		This method gets called when the manipulator receives a mouse drag event.

		Returns None if successful.  Otherwise, returns MStatus.kUnknownParameter
		to allow Maya to further process the event."""
	def doRelease(self)->None:
		"""doRelease() -> None

		This method gets called when the manipulator receives a mouse release
		event.

		Returns None if successful.  Otherwise, returns MStatus.kUnknownParameter
		to allow Maya to further process the event."""
	def draw(self,view:M3dView,path:om.MDagPath,style:M3dView.DisplayStyle,status:M3dView.DisplayStatus)->None:
		"""draw(view, path, style, status) -> None

		This method can be overloaded to customize the drawing of the
		child manipulators. If the default draw is also required, this
		method should be called from the derived method.

		* view (M3dView) - the view in which to draw
		* path (MDagPath) - the current path
		* style (M3dView.DisplayStyle) - the display appearance
		* status (M3dView.DisplayStatus) - the display status"""
	def drawUI(self,drawManager:omr.MUIDrawManager,frameContext:omr.MFrameContext)->None:
		"""drawUI(drawManager, frameContext) -> None

		This is the primary method for doing custom drawing for the
		manipulator in Viewport 2.0. All drawing should occur using the
		MUIDrawManager and any data cached in preDrawUI(). Raw OpenGL calls
		are not supported and if used behaviour will be undefined. Selection
		must still be handled in the draw() method, this method is only for
		display.

		This method is only called when the manipulator needs to be drawn in
		Viewport 2.0.

		We only need to override this function when we have some custom
		elements to draw other than the child manipulators in Viewport 2.0.

		This function is empty in this base class.

		* drawManager (MUIDrawManager) - The draw manager interface for
		                                 drawing some simple UI
		* frameContext (MFrameContext) - Frame level context information"""
	def finishAddingManips(self)->None:
		"""finishAddingManips()

		This method should be called from the user-defined manipulator
		plug-in near the end of the connectToDependNode method so that the
		converter in the manipulator can be initialized. The converter
		cannot be initialized until all the connections from the manip
		values to the plug values have been specified."""
	def getConverterManipDoubleValue(self)->float:
		"""getConverterManipDoubleValue() -> double

		This method retrieves the value of a converterManipValue of type
		double at a given index from the converter.

		* manipIndex (unsigned int) - The index of the value"""
	def getConverterManipMEulerRotationValue(self)->Any:
		"""getConverterManipMEulerRotationValue() -> MEulereRotation

		This method retrieves the value of a converterManipValue of type
		MEulerRotation at a given index from the converter.

		* manipIndex (unsigned int) - The index of the value"""
	def getConverterManipMMatrixValue(self)->om.MMatrix:
		"""getConverterManipMMatrixValue() -> MMatrix

		This method retrieves the value of a converterManipValue of type
		MMatrix at a given index from the converter.

		* manipIndex (unsigned int) - The index of the value"""
	def getConverterManipMPointValue(self)->om.MPoint:
		"""getConverterManipMPointValue() -> MPoint

		This method retrieves the value of a converterManipValue of type
		MPoint at a given index from the converter.

		* manipIndex (unsigned int) - The index of the value"""
	def getConverterManipMTransformationMatrixValue(self)->om.MTransformationMatrix:
		"""getConverterManipMTransformationMatrixValue() -> MTransformationMatrix

		This method retrieves the value of a converterManipValue of type
		MTransformationMatrix at a given index from the converter.

		* manipIndex (unsigned int) - The index of the value"""
	def getConverterManipMVectorValue(self)->om.MVector:
		"""getConverterManipMVectorValue() -> MVector

		This method retrieves the value of a converterManipValue of type
		MVector at a given index from the converter.

		* manipIndex (unsigned int) - The index of the value"""
	def getConverterManipUIntValue(self)->int:
		"""getConverterManipUIntValue() -> unsigned int

		This method retrieves the value of a converterManipValue of type
		unsigned int at a given index from the converter.

		* manipIndex (unsigned int) - The index of the value"""
	def getConverterManipValues(self)->list[float]:
		"""getConverterManipValues() -> [double,double]

		This method retrieves the value of a converterManipValue of type
		[double, double] at a given index from the converter.

		* manipIndex (unsigned int) - The index of the value"""
	def getConverterPlugDoubleValue(self)->float:
		"""getConverterPlugDoubleValue() -> double

		This method retrieves the value of a converterPlugValue of type
		double at a given index from the converter.

		* plugIndex (unsigned int) - The index of the value"""
	def getConverterPlugMEulerRotationValue(self)->om.MEulerRotation:
		"""getConverterPlugMEulerRotationValue() -> MEulerRotation

		This method retrieves the value of a converterPlugValue of type
		MEulerRotation at a given index from the converter.

		* plugIndex (unsigned int) - The index of the value"""
	def getConverterPlugMMatrixValue(self)->om.MMatrix:
		"""getConverterPlugMMatrixValue() -> MMatrix

		This method retrieves the value of a converterPlugValue of type
		MMatrix at a given index from the converter.

		* plugIndex (unsigned int) - The index of the value"""
	def getConverterPlugMPointValue(self)->om.MPoint:
		"""getConverterPlugMPointValue() -> MPoint

		This method retrieves the value of a converterPlugValue of type
		MPoint at a given index from the converter.

		* plugIndex (unsigned int) - The index of the value"""
	def getConverterPlugMVectorValue(self)->om.MVector:
		"""getConverterPlugMVectorValue() -> MVector

		This method retrieves the value of a converterPlugValue of type
		MVector at a given index from the converter.

		* plugIndex (unsigned int) - The index of the value"""
	def getConverterPlugValues(self)->list[float]:
		"""getConverterPlugValues() -> [double, double]

		This method retrieves the value of a converterPlugValue of type
		[double, double] at a given index from the converter.

		* plugIndex (unsigned int) - The index of the value"""
	@staticmethod
	def initialize()->None:
		"""initialize() -> None

		This method initializes the manipulator,
		and should be overriden in user-defined manipulators.

		Return: Status of the operation.
		The base class always returns MS::kSuccess."""
	def isManipActive(self,manipName:Any,stateName:Any)->om.MDagPath:
		"""isManipActive(manipName, stateName) -> MDagPath

		This method returns if custom manip is active & gets the
		current manip object.

		* manipType (MFn Type constant) - The type of the custom manip
		* manipObject (MObject) - Manipulator object"""
	def manipToPlugConversion(self,manipIndex:int)->MManipData:
		"""manipToPlugConversion(manipIndex) -> MManipData

		This virtual method calculates and returns the requested manipulator
		value, based upon the values of plugs on the nodes being manipulated.

		To use, call addPlugToManipConversion() for each manipulator value
		(e.g. the start point of a distance manip) you want this method to
		calculate, then implement this method to calculate those
		manipulator values. Each manipulator value is identified by the
		unique index returned by the corresponding method of its functionset
		(e.g. MFnDistanceManip::startPointIndex).

		* manipIndex (int) - The index of the manipulator value to be
		calculated

		return
		New manipulator value."""
	@staticmethod
	def newManipulator(manipName:str)->tuple[MPxManipContainer,om.MObject]:
		"""newManipulator(manipName) -> (MPxManipContainer, MObject)

		This static function is used to create a user-defined manipulator.
		The manipObject argument is set to the new manipulator node.
		Note that the manipName argument must be the name of a
		manipulator derived from MPxManipContainer.
		Also note that this method creates the newManipulator,
		but doesn't add it to the DAG.
		The primary use of this method is in conjunction with
		MPxSelectionContext::addManipulator, to add
		user-defined manipulators to a context.

		Returns a tuple consisting of new MPxManipContainer instance,
		and the manipulator node.

		* manipName (string) - manipulator name"""
	def plugToManipConversion(self,manipIndex:Any)->MManipData:
		"""plugToManipConversion(manipIndex) -> MManipData

		This virtual method calculates and returns the requested
		plug value, based upon the container's manipulator values.

		To use, call addManipToPlugConversion() for each plug whose value you
		want this method to calculate then implement this method to calculate
		those plug values. Each plug is identified by the unique index
		returned by the addManipToPlugConversion() call.

		plugIndex (int) - The index of the plug value to be calculated

		return
		New plug value."""
	def preDrawUI(self,view:M3dView)->None:
		"""preDrawUI(view) -> None

		This function is used to setup some drawing data for drawing the
		manipulator in Viewport 2.0 . The data updated and cached in this
		function will be used later during 'drawUI()'.

		This method is only called when the manipulator needs to be drawn
		in Viewport 2.0.

		This method needs only be overridden if custom data is needed for
		drawing in drawUI(). If no such data is needed, this method may be
		left unimplemented.

		This function is empty in this base class.

		* view (M3dView) * The view in which to draw"""
	@staticmethod
	def removeFromManipConnectTable(typeId:Any)->None:
		"""removeFromManipConnectTable( typeId )

		This method adds the user defined node as an entry in the
		manipConnectTable so that when this node is selected the user can
		use the show manip tool to get the user defined manipulator
		associated with this node. Note that the name of the manipulator
		node has to be the name of the plug-in node appended with 'Manip'.

		* mid (MTypeId) - Id of the user defined node"""
class MPxManipulatorNode(om.MPxNode):
	"""Parent class of all user defined manipulators."""
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def connectToDependNode(self,node:om.MObject)->None:
		"""connectToDependNode(node) -> None

		This method connects the manipulator to the dependency node. This
		is a virtual method and needs to be overridden from the plug-in.

		* node (MObject) - the node to which the manipulator should be connected"""
	def preDrawUI(self,view:M3dView)->None:
		"""preDrawUI(view) -> None

		This method is used to setup some drawing data for drawing the manipulator
		in Viewport 2.0 . The data updated and cached in this function will be used later
		during 'drawUI()'.

		This method is only called when the manipulator needs to be drawn in Viewport 2.0.

		This method need only be overridden if custom data is needed for drawing in drawUI().
		If no such data is needed, this method may be left unimplemented.

		This function is empty in this base class.

		* view (M3dView) - The view in which to draw"""
	def drawUI(self,drawManager:omr.MUIDrawManager,frameContext:omr.MFrameContext)->None:
		"""drawUI(drawManager, frameContext) -> None

		This is the primary method for drawing the manipulator in Viewport 2.0.
		All drawing should occur using the MUIDrawManager and any data cached
		in preDrawUI(). Raw OpenGL calls are not supported and if used behaviour
		will be undefined. Selection must still be handled in the draw() method,
		this method is only for display.

		This method is only called when the manipulator needs to be drawn in Viewport 2.0.

		This function is empty in this base class.

		* drawManager (MUIDrawManager) - The MUIDrawManager used to draw some simple UI
		* frameContext (MFrameContext) - Frame level context information"""
	def draw(self,view:M3dView,path:om.MDagPath,style:M3dView.DisplayStyle,status:M3dView.DisplayStatus)->None:
		"""draw(view, path, style, status) -> None

		This method is overloaded to draw the manipulators. Selection
		is also setup with this method using the colorAndName()
		method call.

		* view (M3dView) - the view in which to draw
		* path (MDagPath) - the current path
		* style (M3dView.DisplayStyle) - the display appearance
		* status (M3dView.DisplayStatus) - the display status"""
	def doPress(self,view:M3dView)->None:
		"""doPress(view) -> None

		This method gets called when the manipulator receives a mouse down event.

		Returns None if successful.  Otherwise, returns MStatus.kUnknownParameter
		to allow Maya to further process the event.

		* view (M3dView) - the view in which to draw"""
	def doDrag(self,view:M3dView)->None:
		"""doDrag(view) -> None

		This method gets called when the manipulator receives a mouse drag event.

		Returns None if successful.  Otherwise, returns MStatus.kUnknownParameter
		to allow Maya to further process the event.

		* view (M3dView) - the view in which to draw"""
	def doRelease(self,view:M3dView)->None:
		"""doRelease(view) -> None

		This method gets called when the manipulator receives a mouse release event.

		Returns None if successful.  Otherwise, returns MStatus.kUnknownParameter
		to allow Maya to further process the event.

		* view (M3dView) - the view in which to draw"""
	def doMove(self,view:M3dView,refresh:bool)->None:
		"""doMove(view, refresh) -> None

		This method gets called when the manipulator receives a mouse move event,
		if the manipulator registered for mouse move events. To register for mouse
		move events, invoke registerForMouseMove() in the postConstructor of your
		manipulator.

		Returns MStatus.kSuccess if successful.  Otherwise, returns MStatus.kUnknownParameter
		to allow Maya to further process the event.

		* view (M3dView) - the view in which to draw
		* refresh (bool) - if true, refresh the view on this event. Default is false."""
	def finishAddingManips(self)->None:
		"""finishAddingManips() -> None

		This method should be called from the user-defined manipulator
		plug-in near the end of the connectToDependNode method so that the
		converter in the manipulator can be initialized. The converter
		cannot be initialized until all the connections from the manip
		values to the plug values have been specified."""
	def colorAndName(self,view:M3dView,glName:Any,glNameIsPickable:bool,colorIndex:half)->None:
		"""colorAndName(view, glName, glNameIsPickable, colorIndex) -> None

		This method is used to set the color of the GL component that is
		being drawn next. It is also used to set GL name of the component
		so that picking can be supported.

		* view (M3dView) - the view in which to draw
		* glName (MGLuint) - GL 'name' (an unsigned int) of the component. Must be unique.
		* glNameIsPickable (bool) - If true, the component will be pickable
		* colorIndex (half) - Color to use, as provided by one of the *Color()
		                      methods in this class."""
	def setHandleColor(self,drawManager:omr.MUIDrawManager,handleName:Any,colorIndex:half)->None:
		"""setHandleColor(drawManager, handleName, colorIndex) -> None

		This method is used to set the color of component that is being drawn next.
		The color will be correctly selected based on the component's state(highlighted, selected, etc.)

		* drawManager (MUIDrawManager) - The MUIDrawManager used to draw some simple UI
		* handleName (MGLuint) - The unique name (an unsigned int) of the component.
		* colorIndex (half) - The default color to use, as provided by one of the *Color()
		                      methods in this class.  If the component is neither highlighted nor selected,
		                      this colorIndex will be used."""
	def shouldDrawHandleAsSelected(self,name:int)->bool:
		"""shouldDrawHandleAsSelected(name) -> bool
		This function is obsolete, please use 'setHandleColor' instead

		This method can be used to find out if the handle should be drawn
		using the selected color instead of the regular one.

		* name (unsigned int) unique name of the component.

		Returns true if the handle is active or highlighted."""
	def glFirstHandle(self)->Any:
		"""glFirstHandle() -> MGLuint

		This method is used to find the unsigned int value that should
		be used for the first GL handle name.

		Returns the first handle name."""
	def glActiveName(self)->Any:
		"""glActiveName() -> MGLuint

		This method returns the unsigned int value which
		specifies the current active handle.

		Returns the active handle name."""
	def mouseRay(self)->tuple[om.MPoint,om.MVector]:
		"""mouseRay() -> (MPoint, MVector)

		This method returns the location of the mouse within
		a view. The location is defined by a point and a direction
		through the point. Both point and direction are in local
		space.

		Returns a tuple consisting the local space point and direction."""
	def mouseRayWorld(self)->tuple[om.MPoint,om.MVector]:
		"""mouseRayWorld() -> (MPoint, MVector)

		This method returns the location of the mouse within
		a view. The location is defined by a point and a direction
		through the point. Both point and direction are in world
		space.

		Returns a tuple consisting the world space point and direction."""
	def mousePosition(self)->tuple[half,half]:
		"""mousePosition() -> (half, half)

		This method returns the current mouse position within
		a view. The position is in port coordinates.

		Returns a tuple consisting of the x and y port coodinates."""
	def mouseDown(self)->tuple[half,half]:
		"""mouseDown() -> (half, half)

		This method returns the mouse down position within
		a view. The position is in port coordinates.

		Returns a tuple consisting of the x and y port coodinates."""
	def mouseUp(self)->tuple[half,half]:
		"""mouseUp() -> (half, half)

		This method returns the mouse up position within
		a view. The position is in port coordinates.

		Returns a tuple consisting of the x and y port coodinates."""
	def registerForMouseMove(self)->None:
		"""registerForMouseMove() -> None

		This method registers this manipulator to receive mouse
		move events. When registered, the doMove() function will
		be invoked on mouse move events."""
	def deregisterForMouseMove(self)->None:
		"""deregisterForMouseMove() -> None

		This method deregisters this manipulator from receiving
		mouse move events."""
	def addDoubleValue(self,valueName:str,defaultValue:float)->int:
		"""addDoubleValue(valueName, defaultValue) -> int

		Manipulators which call connectPlugToValue() must first create
		the value on the node. Use this method to create a value of
		double type.
		Returns the index assigned to this value by Maya.

		* valueName (string) - Name of the value.
		* defaultValue (float) - Default value."""
	def addPointValue(self,valueName:str,defaultValue:om.MPoint)->int:
		"""addPointValue(valueName, defaultValue) -> int

		Manipulators which call connectPlugToValue() must first create
		the value on the node. Use this method to create a value of
		MPoint type.
		Returns the index assigned to this value by Maya.

		* valueName (string) - Name of the value.
		* defaultValue (MPoint) - Default value."""
	def addVectorValue(self,valueName:str,defaultValue:om.MVector)->int:
		"""addVectorValue(valueName, defaultValue) -> int

		Manipulators which call connectPlugToValue() must first create
		the value on the node. Use this method to create a value of
		MVector type.
		Returns the index assigned to this value by Maya.

		* valueName (string) - Name of the value.
		* defaultValue (MVector) - Default value."""
	def setDoubleValue(self,valueIndex:int,value:float)->None:
		"""setDoubleValue(valueIndex, value) -> None

		This method is used for setting a floating point value associated with the
		manipulator.

		* valueIndex (int) - the index of the value to be set
		* value (float) - the value to set it to"""
	def setPointValue(self,valueIndex:int,value:om.MPoint)->None:
		"""setPointValue(valueIndex, value) -> None

		This method is used for setting an MPoint value associated with the
		manipulator.

		* valueIndex (int) - the index of the value to be set
		* value (MPoint) - the value to set it to"""
	def setVectorValue(self,valueIndex:int,value:om.MVector)->None:
		"""setVectorValue(valueIndex, value) -> None

		This method is used for setting an MVector value associated with the
		manipulator.

		* valueIndex (int) - the index of the value to be set
		* value (MVector) - the value to set it to"""
	def getDoubleValue(self,valueIndex:int,previousValue:bool)->float:
		"""getDoubleValue(valueIndex, previousValue) -> float

		This method is used for getting a floating point value associated with the manipulator.

		Returns the floating point value

		* valueIndex (int) - the index of the value to be retrieved
		* previousValue (bool) - if true, get the previous value. if false, get the current value"""
	def getPointValue(self,valueIndex:int,previousValue:bool)->om.MPoint:
		"""getPointValue(valueIndex, previousValue) -> MPoint

		This method is used for getting an MPoint value associated with the manipulator.

		Returns the MPoint value

		* valueIndex (int) - the index of the value to be retrieved
		* previousValue (bool) - if true, get the previous value. if false, get the current value"""
	def getVectorValue(self,valueIndex:int,previousValue:bool)->float:
		"""getVectorValue(valueIndex, previousValue) -> float

		This method is used for getting an MVector value associated with the manipulator.

		Returns the MVector value

		* valueIndex (int) - the index of the value to be retrieved
		* previousValue (bool) - if true, get the previous value. if false, get the current value"""
	def connectPlugToValue(self,plug:om.MPlug,valueIndex:int)->int:
		"""connectPlugToValue(plug, valueIndex) -> int

		This method is called in the connectToDependNode() virtual if
		it is implemented for the custom manipulator. It will
		connect a plug to an already added manipulator value of
		the same type.

		Returns a new index for the plug that is being connected.

		* plug (MPlug) - the plug to connect the value to
		* valueIndex (int) - the index of the value. index is set by add*Value() method"""
	@staticmethod
	def newManipulator(manipName:str)->tuple[MPxManipulatorNode,om.MObject]:
		"""newManipulator(manipName) -> (MPxManipulatorNode, MObject)

		This static function is used to create a user-defined manipulator node.
		The manipObject argument is set to the new manipulator node.
		Note that the manipName argument must be the name of a
		manipulator derived from MPxManipulatorNode.
		Also note that this method creates the newManipulator
		but doesn't add it to the DAG.
		The primary use of this method is in conjunction with
		MPxSelectionContext.addManipulator, to add
		user-defined manipulators to a context.

		Returns a tuple consisting of new MPxManipulatorNode instance,
		and the manipulator node.

		* manipName (string) - manipulator name"""
	def addDependentPlug(self,plug:om.MPlug)->None:
		"""addDependentPlug(plug) -> None

		This method adds the plug to the list of those to be keyframed.
		The call to addDependentPlug() should happen prior to the manipulator
		identifying the plugs to be set. For example, if your manipulator
		sets plugs based on the selection list or modifier keys you could
		call addDependentPlug() from your doPress() method. Note that the
		dependentPlugsReset() method is provided to clear out the list and
		should be called prior to addDependentPlugs().

		* plug (MPlug) - the plug to keyframe when using this manipulator"""
	def dependentPlugsReset(self)->None:
		"""dependentPlugsReset() -> None

		This method resets the list of dependent plugs for this manipulator.
		Call this method prior to adding plugs via addDependentPlug() such as
		from your doPress() method."""
	def mainColor(self)->half:
		"""mainColor() -> half

		This method returns the main color index."""
	def xColor(self)->half:
		"""xColor() -> half

		This method returns the color index of the x axis."""
	def yColor(self)->half:
		"""yColor() -> half

		This method returns the color index of the y axis."""
	def zColor(self)->half:
		"""zColor() -> half

		This method returns the color index of the z axis."""
	def prevColor(self)->half:
		"""prevColor() -> half

		This method returns the previously color used by the colorAndName() method."""
	def lineColor(self)->half:
		"""lineColor() -> half

		This method returns the color index of a line"""
	def dimmedColor(self)->half:
		"""dimmedColor() -> half

		This method returns the color index for a dimmed or unselectable component."""
	def selectedColor(self)->half:
		"""selectedColor() -> half

		This method returns the color index of a selected component."""
	def labelColor(self)->half:
		"""labelColor() -> half

		This method returns the color index of a label."""
	def labelBackgroundColor(self)->half:
		"""labelBackgroundColor() -> half

		This method returns the color index of a label background."""
class MPxSelectionContext(MPxContext):
	"""Base class for interative selection tools."""
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def addManipulator(self,manipulator:om.MObject)->None:
		"""addManipulator(manipulator) -> None

		This method adds a manipulator to the context.

		* manipulator (MObject) - the manipulator to be added to the context."""
	def deleteManipulators(self)->None:
		"""deleteManipulators() -> None

		This method deletes all the manipulators that belong
		to the context."""
	def setAllowPreSelectHilight(self)->None:
		"""setAllowPreSelectHilight() -> None

		This method enables the support of pre-selection highlight for this context.
		It needs to be called by the user-overriden MPxContext::toolOnSetup method."""
	def setAllowSoftSelect(self)->None:
		"""setAllowSoftSelect() -> None

		This method enables the support of soft selection for this context."""
	def setAllowSymmetry(self)->None:
		"""setAllowSymmetry() -> None

		This method enables the support of symmetrical selection for this context."""
	def setAllowDoubleClickAction(self)->None:
		"""setAllowDoubleClickAction() -> None

		This method enables the support of double click smart selection for this context."""
	def setAllowPaintSelect(self)->None:
		"""setAllowPaintSelect() -> None

		This method enables drag selection mode for this context."""
	def doDragLegacy(self,event:MEvent)->None:
		"""doDragLegacy(event) -> None

		This method is called when a mouse drag event occurs.
		The base method does nothing and should be overridden if
		the user needs to do anything during a mouse drag.

		This method is called only when it is in either default viewport renderer
		or hardware viewport renderer, not viewport 2.0.

		The <b>event</b> can be used to get more explicit information
		about the drag such as the cursor location. See MEvent for
		more information.

		* event (MEvent) - The button drag event information.

		    DEPRECATED in 2023, please use doDrag."""
	def doHoldLegacy(self,event:MEvent)->None:
		"""doHoldLegacy(event) -> None

		This method is called when a mouse button is pressed but
		before the mouse is dragged.
		The base method does nothing and should be overridden if the user needs
		to do anything on a button hold.

		This method is called only when it is in either default viewport renderer
		or hardware viewport renderer, not viewport 2.0.

		The <b>event</b> can be used to get more explicit information
		about the hold such as the button number. See MEvent for
		more information.

		* event (MEvent) - The button hold event information.

		    DEPRECATED in 2023, please use doHold."""
	def doPressLegacy(self,event:MEvent)->None:
		"""doPressLegacy(event) -> None

		This method is called when any mouse button is pressed.
		The base method does nothing and should be overridden if
		the user needs to do anything on a button press.

		This method is called only when it is in either default viewport renderer
		or hardware viewport renderer, not viewport 2.0.

		The <b>event</b> can be used to get more explicit information
		about the press such as the button number. See MEvent for
		more information.

		* event (MEvent) - The button press event information.

		    DEPRECATED in 2023, please use doPress."""
	def doReleaseLegacy(self,event:MEvent)->None:
		"""doReleaseLegacy(event) -> None

		This method is called when any mouse button is released.
		The base method does nothing and should be overridden if
		the user needs to do anything on a button release.

		This method is called only when it is in either default viewport renderer
		or hardware viewport renderer, not viewport 2.0.

		The <b>event</b> can be used to get more explicit information
		about the release such as the button number. See MEvent for
		more information.

		* event (MEvent) - The button release event information.

		    DEPRECATED in 2023, please use doRelease."""
	def doDrag(self,event:MEvent,drawManager:omr.MUIDrawManager,frameContext:omr.MFrameContext)->None:
		"""doDrag(event, drawManager, frameContext) -> None

		This method is called when a mouse drag event occurs.
		The base method does nothing and should be overridden if
		the user needs to do anything during a mouse drag.

		This method is called only when it is in either default viewport renderer
		or hardware viewport renderer, not viewport 2.0.

		The <b>event</b> can be used to get more explicit information
		about the drag such as the cursor location. See MEvent for
		more information.

		* event (MEvent) - The button drag event information.
		* drawManager (MUIDrawManager) - Draw manager to use to draw custom shape
		* frameContext (MFrameContext) - Context of the frame being rendered."""
	def doHold(self,event:MEvent,drawManager:omr.MUIDrawManager,frameContext:omr.MFrameContext)->None:
		"""doHold(event, drawManager, frameContext) -> None

		This method is called when a mouse button is pressed but
		before the mouse is dragged.
		The base method does nothing and should be overridden if the user needs
		to do anything on a button hold.

		This method is called only when it is in either default viewport renderer
		or hardware viewport renderer, not viewport 2.0.

		The <b>event</b> can be used to get more explicit information
		about the hold such as the button number. See MEvent for
		more information.

		* event (MEvent) - The button hold event information.
		* drawManager (MUIDrawManager) - Draw manager to use to draw custom shape
		* frameContext (MFrameContext) - Context of the frame being rendered."""
	def doPress(self,event:MEvent,drawManager:omr.MUIDrawManager,frameContext:omr.MFrameContext)->None:
		"""doPress(event, drawManager, frameContext) -> None

		This method is called when any mouse button is pressed.
		The base method does nothing and should be overridden if
		the user needs to do anything on a button press.

		This method is called only when it is in either default viewport renderer
		or hardware viewport renderer, not viewport 2.0.

		The <b>event</b> can be used to get more explicit information
		about the press such as the button number. See MEvent for
		more information.

		* event (MEvent) - The button press event information.
		* drawManager (MUIDrawManager) - Draw manager to use to draw custom shape
		* frameContext (MFrameContext) - Context of the frame being rendered."""
	def doRelease(self,event:MEvent,drawManager:omr.MUIDrawManager,frameContext:omr.MFrameContext)->None:
		"""doRelease(event, drawManager, frameContext) -> None

		This method is called when any mouse button is released.
		The base method does nothing and should be overridden if
		the user needs to do anything on a button release.

		This method is called only when it is in either default viewport renderer
		or hardware viewport renderer, not viewport 2.0.

		The <b>event</b> can be used to get more explicit information
		about the release such as the button number. See MEvent for
		more information.

		* event (MEvent) - The button release event information.
		* drawManager (MUIDrawManager) - Draw manager to use to draw custom shape
		* frameContext (MFrameContext) - Context of the frame being rendered."""
	def helpStateHasChanged(self,event:MEvent)->None:
		"""helpStateHasChanged(event) -> None

		This method is called whenever the help state may need to be
		updated.
		The base method does nothing and should be overriden if
		the user needs to change the help information based on events.

		The <b>event</b> can be used to get more explicit information
		about the event. See MEvent for more information.

		* event (MEvent) - The event information."""
	def abortAction(self)->None:
		"""abortAction() -> None

		This method is called when the abort key is pressed.
		The default abort key in Maya is the <b>escape</b> key.
		Users can override this method if they wish to perform
		certain operations when the abort key is pressed."""
	def processNumericalInput(self,values:om.MDoubleArray,flags:om.MIntArray,isAbsolute:bool)->bool:
		"""processNumericalInput(values, flags, isAbsolute) -> bool

		This method processes the input from the numerical input field.
		Users can override this method if they wish to process numerical input.
		For a given entry in the numeric input field, if the user types a dot '.',
		this indicates that the entry should not be modified.
		The overridden version of this method should take this into account
		using the ignoreEntry method with the flags that are passed in.
		The overridden version of this method should also process the numeric
		input as an absolute input or relative input depending on whether
		the isAbsolute flag is true or not.
		The return value should indicate whether or not the numerical input has
		been processed.

		* values (MDoubleArray) - the values from the numerical input field.
		* flags (MIntArray) - used in conjunction with the ignoreEntry method,
		determines whether or not a given entry should be ignored.
		* isAbsolute (bool) - whether or not the input should be interpreted as absolute."""
	def feedbackNumericalInput(self)->bool:
		"""feedbackNumericalInput() -> bool

		This method is called to update the numerical feedback.
		The format and values for the feedback line can be set through the
		methods in MFeedbackLine, specifically setFormat and setValue.
		The return value should indicate whether or not the numerical feedback
		has been provided.  The default return value is false."""
	def argTypeNumericalInput(self,index:int)->int:
		"""argTypeNumericalInput(index) -> MSyntax.MArgType

		This method is used by the feedback line to determine what units to display.
		Users should override this method to return the appropriate
		argument type for the given index of the numeric input field.
		Specifically, this method should be overridden to return one of the following:

		    <b>MSyntax.kNoArg</b> for no argument
		    <b>MSyntax.kDistance</b> for linear units
		    <b>MSyntax.kAngle</b> for angular units

		* index (int) - the index of the numerical input whose argument type is requested."""
	def setImage(self,image:str,index:ImageIndex)->Self:
		"""setImage(image, index) -> self

		This method is used to set an XPM icon image that is to be
		used to represent this tool context in various places
		including the tool bar and can be queried from mel using the
		contextInfo command.

		* image (string) - the name of an XPM file to be used as the icon.
		* index (ImageIndex) - the index of the image being set; three image
		representations are permitted: kImage1, kImage2, kImage3."""
	def image(self,index:ImageIndex)->str:
		"""image(index) -> string

		This method is used to retrieve an XPM icon image that has
		previously been set for this tool context. This icon image will be
		used to represent this tool context in various places including
		the tool bar and can be queried from mel using the contextInfo
		command.

		* index (ImageIndex) - the index of the image being retrieved; three image
		representations are permitted: kImage1, kImage2, kImage3."""
	def isSelecting(self)->bool:
		"""isSelecting() -> bool

		Determines whether an object is selected.
		returns True if an object(s) is selected, False otherwise."""
	def startPoint(self)->om.MPoint:
		"""startPoint() -> MPoint

		Returns the position of the button press."""
	def lastDragPoint(self)->om.MPoint:
		"""lastDragPoint() -> MPoint

		Returns the position of the last drag point."""
	def newToolCommand(self)->MPxToolCommand:
		"""newToolCommand() -> MPxToolCommand

		Create a new instance of the tool command associated with this context.
		The tool command (derived from MPxToolCommand) is the command that was
		registered along with the context command in.

		Returns a new instance of the MPxToolCommand."""
class MPxSurfaceShapeUI:
	"""(Deprecated: Please use MHWRender::MPxGeometryOverride, MHWRender::MPxSubSceneOverride, or MHWRender::MPxDrawOverride instead.)
	Base class for the UI portion of all user defined shapes."""
	kSelectMeshUVs:int=0
	kSelectMeshVerts:int=1
	kSelectMeshFaces:int=2
	kSelectMeshEdges:int=3
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def canDrawUV(self)->bool:
		"""canDrawUV() -> bool

		Called by Maya to determine if this surface shape supports UV drawing."""
	def drawUV(self,view:M3dView,info:MTextureEditorDrawInfo)->Self:
		"""drawUV(view, info) -> self

		This method is called when the surface shape is selected and the texture view is open.  Users should override this method if their custom shape supports UVs.

		* view (M3dView) - Texture view in which to draw UVs.
		* info (MTextureEditorDrawInfo) - Drawing parameters."""
	def material(self,path:Any)->MMaterial:
		"""material(path) -> MMaterial

		COMMENT"""
	def materials(self,path:om.MDagPath,componentFilter:Any,materials:Any,componentSet:Any|None=None)->Self:
		"""materials(path, componentFilter, materials, componentSet=None) -> self

		Returns the material associated with this shape.
		The user must supply a DAG path as a shape can have several materials if instanced.

		* path (MDagPath) - the path for which to get the material"""
	def select(self,selectInfo:MSelectInfo,selectionList:Any,worldSpaceSelectPts:Any)->bool:
		"""select(selectInfo, selectionList, worldSpaceSelectPts) -> bool

		This routine must be overriden if the shape is to support interactive object and/or component selection. The implementation of this method should call selectInfo.addSelection with information about the selected item and its selection mask. For single click selection, detected using the selectInfo.singleSection() method, the hit point should also be passed as an argument to selectInfo.addSelection().

		Returns True if something was selected.

		* selectInfo (MSelectInfo) - the Selection state information.
		* selectionList [OUT] (MSelectionList) - List of items selected by this method. Do not update directly: use MSelectInfo.addSelection instead.
		* worldSpaceSelectPts [OUT] (MPointArray) - List of points used to sort corresponding selections in single-select mode. (Closest to camera wins.) Do not update directly: use MSelectInfo.addSelection instead."""
	def selectUV(self,view:M3dView,selType:int,xmin:int,ymin:int,xmax:int,ymax:int,singleSelect:bool,selList:Any)->bool:
		"""selectUV(view, selType, xmin, ymin, xmax, ymax, singleSelect, selList) -> bool

		This method is called when the user performs a selection within the texture view.  The method is called only when the surface shape is member of the active selection list.

		Maya provides the current viewport instance, the type of the selection, the extents of the selection rectangle (in viewport coordinates), and if the selection mode is single selection. The API user is expected to fill the selection list and return a result of True if 'something was selected'.

		To properly use this method, you must make sure that you have a valid component type that Maya can recognize. Selection tests can be done using a pick buffer or by spatially determining the selected objects.

		Currently Maya does not know how to manipulate custom UV components. This method only provides the facilities to visualize what has been selected in the viewport.  The API user is responsible for implementing commands that can manipulate the currently selected UVs.

		Returns True if something was selected.

		* view (M3dView) - the texture drawing view
		* selType (int) - the selection type
		* xmin (int) - minimum x coordinate value of the selection rectangle.
		* ymin (int) - minimum y coordinate value of the selection rectangle.
		* xmax (int) - maximum x coordinate value of the selection rectangle.
		* ymax (int) - maximum y coordinate value of the selection rectangle.
		* singleSelect (bool) - indicates if the user is in single selection mode.
		* selList [OUT] (MSelectionList) - the selection list to be populated.

		Valid selection types:
		  kSelectMeshUVs      The UV selection type is UVs.
		  kSelectMeshVerts    The UV selection type is vertices.
		  kSelectMeshFaces    The UV selection type is faces.
		  kSelectMeshEdges    The UV selection type is edges."""
	def snap(self,snapInfo:MSelectInfo)->bool:
		"""snap(snapInfo) -> bool

		Maya calls this method when snapping to the shape's vertices.
		If you wish your custom shape to support point snapping then you must override this method and have it call snapInfo's MSelectInfo.setSnapPoint() method to set the point to be snapped to.
		If setSnapPoint() is called multiple times then the point closest to the cursor will be used.

		Returns True if a vertex was found to be snapped to was selected.

		* snapInfo (MSelectInfo) - the Selection state information."""
	def surfaceShape(self)->om.MPxSurfaceShape:
		"""surfaceShape() -> MPxSurfaceShape

		Returns the non-ui shape associated with current instance."""
	@staticmethod
	def surfaceShapeUI(path:om.MDagPath)->MPxSurfaceShapeUI:
		"""surfaceShapeUI(path) -> MPxSurfaceShapeUI

		This is a static method that can be used to find the corresponding MPxSurfaceShapeUI for the specified path.  If an MPxSurfaceShapeUI does not exist then one is created.

		This function can only be used for custom surface shapes and the function will return NULL if the provided path is not a custom surface shape.

		* path (MDagPath) - The full path to a surface shape, including the shape."""
class MPxToolCommand(om.MPxCommand):
	"""Base class for custom tool commands."""
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def doIt(self,*args)->Any:
		"""Called by Maya to execute the command."""
	def cancel(self)->None:
		"""cancel() -> None

		This method cancels the command.
		The user should override this method when the original program state
		needs to be restored."""
	def finalize(self)->None:
		"""finalize() -> None

		This method is used to create a string representing the command
		and its arguments.
		Users should override this method and contruct an MArgList and
		then pass it to <b>doFinalize</b> for journalling."""
	def doFinalize(self)->None:
		"""doFinalize() -> None

		Call this method with an MArgList representing your command.
		This method will register the command with the undo manager
		for journalling.

		* command (MArgList) Reference representing an equivalent"""
class MSelectInfo(MDrawInfo):
	"""(Deprecated: Please use MHWRender::MPxGeometryOverride, MHWRender::MPxSubSceneOverride, or MHWRender::MPxDrawOverride instead.)
	Selection state information used in MPxSurfaceShapeUI.select."""
	@property
	def highestPriority(self)->Any:
		"""The highest selection priority value."""
	@highestPriority.setter
	def highestPriority(self,value:Any)->None:...
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def addSelection(self,item:om.MSelectionList,point:om.MPoint,list:list,points:Any,mask:om.MSelectionMask,isComponent:bool)->Self:
		"""addSelection(item, point, list, points, mask, isComponent) -> self

		Adds components or objects to the active selection list.

		* item (MSelectionList) - The component or object to add to the list
		* point (MPoint) - The world space point representing the selected object. This is used during single-click selection when the click overlaps multiple objects in order to determine which point is closest to the camera.
		* list [OUT] (MSelectionList) - The selection list to add the item(s) to
		* points [OUT] (MPointArray) - A copy of the points of all currently selected components in the list (if components are selected)
		* mask (MSelectionMask) - Mask used to determine selection priority
		* isComponent (bool) - Indicates whether item to be added is an object or a component"""
	def getAlignmentMatrix(self)->om.MMatrix:
		"""getAlignmentMatrix() -> MMatrix

		Returns the alignment matrix.
		This method is used to find ray object intersection."""
	def getLocalRay(self)->list[om.MPoint|om.MVector]:
		"""getLocalRay() -> [MPoint, MVector]

		Returns the selection ray defined by its starting point (MPoint) and its direction (MVector).
		This method is used to find ray object intersection."""
	def isRay(self)->bool:
		"""isRay() -> bool

		Returns True if there is a selection ray.
		This method isused to find ray object intersection."""
	def selectClosest(self)->bool:
		"""selectClosest() -> bool

		Returns True if we want to select the closest object."""
	def selectForHilite(self,mask:om.MSelectionMask)->bool:
		"""selectForHilite(mask) -> bool

		Given the selection mask, can this object be selected for the hilite list.

		* mask (MSelectionMask) - the mask to test"""
	def selectOnHilitedOnly(self)->bool:
		"""selectOnHilitedOnly() -> bool

		Returns True if you can only select components if the object is hilited."""
	def selectPath(self)->om.MDagPath:
		"""selectPath() -> MDagPath

		Returns a path to the item that is being selected."""
	def selectRect(self)->list[int]:
		"""selectRect() -> [int, int, int, int]

		Get the current selection rectangle dimensions, defined by:
		  its lower left corner - x coordinate,
		  its lower left corner - y coordinate,
		  its width,
		  its height."""
	def selectable(self,mask:om.MSelectionMask)->bool:
		"""selectable(mask) -> bool

		Given the selection mask, this method determines if the object is selectable.

		* mask (MSelectionMask) - the mask to test"""
	def selectableComponent(self,displayed:bool,mask:om.MSelectionMask)->bool:
		"""selectableComponent(displayed, mask) -> bool

		Given the selection mask, this method determines if the component is selectable.

		* displayed (bool) - is the component displayed
		* mask (MSelectionMask) - selection mask"""
	def setSnapPoint(self,point:om.MPoint)->bool:
		"""setSnapPoint(point) -> bool

		When a snapping operation is being performed the shape's overridden MPxSurfaceShapeUI.snap() method can call this method to set the point to be snapped to. If setSnapPoint() is called multiple times then the point passed in which is nearest to the current cursor location will be used. So the shape can either compute the snap point itself and call setSnapPoint() once or it can make a series of calls and let setSnapPoint() determine the closest of those for itself.

		* point (MPoint) - The point to be snapped to, must be given in world space coordinates."""
	def singleSelection(self)->bool:
		"""singleSelection() -> bool

		This method determines if we want to select a single object."""
	def view(self)->M3dView:
		"""view() -> M3dView

		Returns the view that the current selection is taking place in."""
class MTextureEditorDrawInfo:
	"""Drawing state for drawing to the UV texture window with custom shapes."""
	@property
	def drawingFunction(self)->Any:
		"""The current drawing state for a drawUV method call.
		Valid states:
		  kDrawWireframe         Draw wireframe only (default)
		  kDrawEverything        Draw vertices, uvs, faces, and edges
		  kDrawVertexForSelect   Draw vertices for selection
		  kDrawEdgeForSelect     Draw edges for selection
		  kDrawFacetForSelect    Draw faces for selection
		  kDrawUVForSelect       Draw uvs for selection"""
	@drawingFunction.setter
	def drawingFunction(self,value:Any)->None:...
	kDrawFunctionFirst:int=1
	kDrawWireframe:int=1
	kDrawEverything:int=2
	kDrawVertexForSelect:int=3
	kDrawEdgeForSelect:int=4
	kDrawFacetForSelect:int=5
	kDrawUVForSelect:int=6
	kDrawFunctionLast:int=6
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
class MTimeSliderCustomDrawManager:
	"""Manager to add drawing primitive to the time slider."""
	kAbove:int=0
	kBelow:int=1
	kOn:int=2
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def registerCustomDrawOn(self,*args)->Any:...
	def registerCustomDrawOutside(self,*args)->Any:...
	def setDrawPrimitives(self,*args)->Any:...
	def clearDrawPrimitives(self,*args)->Any:...
	def deregisterCustomDraw(self,*args)->Any:...
	def setDrawVisible(self,*args)->Any:...
	def requestTimeSliderRedraw(self,*args)->Any:...
	def setBackgroundColor(self,*args)->Any:...
	def setDrawLayer(self,*args)->Any:...
	def setDrawHeight(self,*args)->Any:...
	def setDrawLocation(self,*args)->Any:...
	def setDrawPriority(self,*args)->Any:...
	def setStartPrimitiveEditFunction(self,*args)->Any:...
	def setEditPrimitiveFunction(self,*args)->Any:...
	def setStopPrimitiveEditFunction(self,*args)->Any:...
	def setTooltip(self,*args)->Any:...
	def setSetCopyPrimitivesFunction(self,*args)->Any:...
class MTimeSliderDrawPrimitive:
	"""Primitive to be drawn set in a context with MTimeSiderCustomDrawManager."""
	@property
	def priority(self)->Any:
		"""The drawing priority.
		"""
	@priority.setter
	def priority(self,value:Any)->None:...
	@property
	def drawType(self)->Any:
		"""One of the primitive type.
		kFilledRect   Draws a filled rectangle with no border.
		kUpperOutline Draws an outline with no bottom side.
		kFullOutline  Draws an outline on all sides.
		kVerticalLine Draws a vertical line at startTime.
		kBracket      Draws a bracket from start to end time.
		kFrameFlag    Draws a flag at a specific frame.
		"""
	@drawType.setter
	def drawType(self,value:Any)->None:...
	@property
	def startTime(self)->Any:
		"""Start time of the primitive.
		"""
	@startTime.setter
	def startTime(self,value:Any)->None:...
	@property
	def endTime(self)->Any:
		"""End time of the primitive.
		"""
	@endTime.setter
	def endTime(self,value:Any)->None:...
	@property
	def height(self)->Any:
		"""The drawing height.
		"""
	@height.setter
	def height(self,value:Any)->None:...
	@property
	def bottom(self)->Any:
		"""Bottom offset.
		"""
	@bottom.setter
	def bottom(self,value:Any)->None:...
	@property
	def color(self)->Any:
		"""Color of the primitive.
		"""
	@color.setter
	def color(self,value:Any)->None:...
	@property
	def label(self)->Any:
		"""Label of the primitive.
		"""
	@label.setter
	def label(self,value:Any)->None:...
	@property
	def tooltip(self)->Any:
		"""Tooltip of the primitive.
		"""
	@tooltip.setter
	def tooltip(self,value:Any)->None:...
	kFilledRect:int=0
	kUpperOutline:int=1
	kFullOutline:int=2
	kVerticalLine:int=3
	kBracket:int=4
	kFrameFlag:int=5
	kNone:int=0
	kMovePrimitive:int=1
	kMoveStartTime:int=2
	kMoveEndTime:int=3
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
class MUiMessage(om.MMessage):
	"""Class used to register callbacks for UI related messages."""
	@staticmethod
	def addUiDeletedCallback(uiName:str,function:Callable,clientData:Any|None=None)->int:
		"""addUiDeletedCallback(uiName, function, clientData=None) -> id

		This method registers a callback for UI deleted messages.
		The callback function will be passed any client data that was
		provided when the callback was registered.

		 * uiName (string) - the name of the UI object to register the
		   callback for
		 * function - callable which will be passed the clientData object
		 * clientData - User defined data passed to the callback function

		 * return: Identifier used for removing the callback."""
	@staticmethod
	def addCameraChangedCallback(panelName:str,function:Callable,clientData:Any|None=None)->int:
		"""addCameraChangedCallback(panelName, function, clientData=None) -> id

		This method registers a callback for cameras being changed in
		3d views.  The callback is called when the camera changes for the
		given panel, not when attributes on the panel's camera change.

		The callback function will be passed any client data that was
		provided when the callback was registered.

		 * panelName (string) - the name of panel to which to attach the
		   callback.
		 * function - callable which will be passed a string indicating the
		   name of the panel that had the camera change, a MObject containing
		   the current camera used by the panel and the clientData object
		 * clientData - User defined data passed to the callback function

		 * return: Identifier used for removing the callback."""
	@staticmethod
	def add3dViewDestroyMsgCallback(panelName:str,function:Callable,clientData:Any|None=None)->int:
		"""add3dViewDestroyMsgCallback(panelName, function, clientData=None) -> id

		        This method registers a callback for when a particular 3d view gets
		destroyed. The callback is called before the destruction of the view.

		The callback function will be passed any client data that was
		provided when the callback was registered

		 * panelName (string) - Name of panel to which to attach the callback
		 * function - callable which will be passed a string indicating the name
		   of the panel that contain the 3d view and the clientData object
		 * clientData - User defined data passed to the callback function

		 * return: Identifier used for removing the callback."""
	@staticmethod
	def add3dViewPreRenderMsgCallback(panelName:str,function:Callable,clientData:Any|None=None)->int:
		"""add3dViewPreRenderMsgCallback(panelName, function, clientData=None) -> id

		This method registers a callback for when a particular 3d view is
		about to render it's contents. It is called before the scene is drawn,
		but after the background has been drawn.

		The callback function will be passed any client data that was
		provided when the callback was registered.

		 * panelName (string) - Name of panel to which to attach the callback
		 * function - callable which will be passed a string indicating the name
		   of the panel that contain the 3d view and the clientData object
		 * clientData - User defined data passed to the callback function

		 * return: Identifier used for removing the callback."""
	@staticmethod
	def add3dViewPostRenderMsgCallback(panelName:str,function:Callable,clientData:Any|None=None)->int:
		"""add3dViewPostRenderMsgCallback(panelName, function, clientData=None) -> id

		This method registers a callback for when the 3d view is
		about to display it's rendered contents to the viewport.
		It is called for every refresh of the view, after the scene is drawn,
		but before any 2d adornments are drawn.

		The callback function will be passed any client data that was
		provided when the callback was registered.

		 * panelName (string) - Name of panel to which to attach the callback
		 * function - callable which will be passed a string indicating the name
		   of the panel that contain the 3d view and the clientData object
		 * clientData - User defined data passed to the callback function

		 * return: Identifier used for removing the callback."""
	@staticmethod
	def add3dViewRendererChangedCallback(panelName:str,function:Callable,clientData:Any|None=None)->int:
		"""add3dViewRendererChangedCallback(panelName, function, clientData=None) -> id

		This method registers a callback for when the renderer for a particular 3d
		view changes.

		The callback function will be passed any client data that was
		provided when the callback was registered.

		 * panelName (string) - Name of panel to which to attach the callback
		 * function - callable which will be passed 3 strings indicating: the name
		   of the panel that contain the 3d view, the name of the old renderer used
		   to draw the 3d view, the name of the new renderer used to draw the 3d view
		   , and the clientData object
		 * clientData - User defined data passed to the callback function

		 * return: Identifier used for removing the callback."""
	@staticmethod
	def add3dViewRenderOverrideChangedCallback(panelName:str,function:Callable,clientData:Any|None=None)->int:
		"""add3dViewRenderOverrideChangedCallback(panelName, function, clientData=None) -> id

		This method registers a callback for when the render override for a
		particular 3d view changes.

		The callback function will be passed any client data that was
		provided when the callback was registered.

		 * panelName (string) - Name of panel to which to attach the callback
		 * function - callable which will be passed 3 strings indicating: the name of
		   the panel that contain the 3d view, the name of the old override used to draw
		   in the 3d view, the name of the new override used to draw in the 3d view
		   , and the clientData object
		 * clientData - User defined data passed to the callback function

		 * return: Identifier used for removing the callback."""
class RenderParameters:
	"""Provides information on how to render the image."""
	@property
	def baseColor(self)->Any:
		"""Base color"""
	@baseColor.setter
	def baseColor(self,value:Any)->None:...
	@property
	def unfiltered(self)->Any:
		"""Unfiltered state"""
	@unfiltered.setter
	def unfiltered(self,value:Any)->None:...
	@property
	def showAlphaMask(self)->Any:
		"""ShowAlphaMask state"""
	@showAlphaMask.setter
	def showAlphaMask(self,value:Any)->None:...
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
class ShaderContext:
	"""Provides contextual information about the current invocation of the shader."""
	@property
	def path(self)->Any:
		"""DAG path for the given invocation of the shader"""
	@path.setter
	def path(self,value:Any)->None:...
	@property
	def shadingEngine(self)->Any:
		"""Shading engine node for the given invocation of the shader"""
	@shadingEngine.setter
	def shadingEngine(self,value:Any)->None:...
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
