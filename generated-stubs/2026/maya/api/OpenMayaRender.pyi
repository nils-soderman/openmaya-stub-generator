"""
maya.api.OpenMayaRender stub file generated for Maya 2026 using:
https://github.com/nils-soderman/openmaya-stub-generator
"""
from __future__ import annotations

import collections.abc
import maya.api.OpenMaya as om
from typing import Any, Self, Sequence, overload

class MAttributeParameterMapping:
	"""Class for defining relationship between Maya attributes and fragment parameters."""
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def allowConnection(self)->bool:
		"""allowConnection() -> bool

		This method returns true if Maya is allowed to connect other shade fragments to the parameter named by this mapping."""
	def allowRename(self)->bool:
		"""allowRename() -> bool

		This method returns true if the parameter named by this mapping may be renamed in the final shading effect.
		If false, name collisions of parameters will be unresolved and results will be unpredictable."""
	def attributeName(self)->str:
		"""attributeName() -> string

		Get the attribute name for this mapping."""
	def parameterName(self)->str:
		"""parameterName() -> string

		Get the parameter name for this mapping."""
	def resolvedParameterName(self)->str:
		"""resolvedParameterName() -> string

		Get the resolved parameter name for this mapping. After the fragment has been joined with other
		fragments to form the final shading effect its parameters are renamed to prevent name collisions.
		This returns the name of the parameter on the final shading effect.
		This name is useful in MPxShadingNodeOverride::updateShader() for setting parameter values manually.

		If the fragment has not yet been joined with other fragments, this will return the same string as parameterName()."""
class MAttributeParameterMappingList:
	"""A list of MAttributeParameterMapping objects."""
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def __len__(self)->int:
		"""Return len(self)."""
	def __getitem__(self,index:int)->Any:
		"""Return self[key]."""
	def append(self,MAttributeParameterMapping:Any)->Self:
		"""append(MAttributeParameterMapping) -> self

		Add a mapping to the list. The list makes a copy; ownership of the original is left with the caller."""
	def clear(self)->Self:
		"""clear() -> self

		Clear all mappings from the list."""
	def findByAttributeName(self,attributeName:str)->MAttributeParameterMapping:
		"""findByAttributeName(attributeName) -> MAttributeParameterMapping

		Find a mapping by attribute name.
		This will return the first mapping found with a matching attribute name."""
	def findByParameterName(self,parameterName:str)->MAttributeParameterMapping:
		"""findByParameterName(parameterName) -> MAttributeParameterMapping

		Find a mapping by parameter name.
		This will return the first mapping found with a matching parameter name."""
class MBlendState:
	"""Container class for an acquired GPU blend state."""
	kAdd:int=1
	kSubtract:int=2
	kReverseSubtract:int=3
	kMin:int=4
	kMax:int=5
	kZero:int=1
	kOne:int=2
	kSourceColor:int=3
	kInvSourceColor:int=4
	kSourceAlpha:int=5
	kInvSourceAlpha:int=6
	kSourceAlphaSat:int=11
	kDestinationColor:int=9
	kInvDestinationColor:int=10
	kDestinationAlpha:int=7
	kInvDestinationAlpha:int=8
	kBothSourceAlpha:int=12
	kBothInvSourceAlpha:int=13
	kBlendFactor:int=14
	kInvBlendFactor:int=15
	kNoChannels:int=0
	kRedChannel:int=1
	kGreenChannel:int=2
	kBlueChannel:int=4
	kAlphaChannel:int=8
	kRGBChannels:int=7
	kRGBAChannels:int=15
	kMaxTargets:int=8
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def desc(self)->MBlendStateDesc:
		"""desc() -> MBlendStateDesc

		Get the blend state descriptor that was used to create the state object."""
	def resourceHandle(self)->int:
		"""resourceHandle() -> long

		Returns a long containing a C++ 'void' pointer which points to the draw API dependent handle for a blend state.
		For OpenGL, such a handle does not exist and a NULL pointer will be returned.
		For DirectX, a pointer to a Direct3D state will be returned."""
class MBlendStateDesc:
	"""Descriptor for a blend state for a single render target."""
	@property
	def alphaToCoverageEnable(self)->Any:
		"""Enable alpha to coverage. Default false"""
	@alphaToCoverageEnable.setter
	def alphaToCoverageEnable(self,value:Any)->None:...
	@property
	def independentBlendEnable(self)->Any:
		"""Use TargetBlends[0] if false or individual blend states if true. Default false"""
	@independentBlendEnable.setter
	def independentBlendEnable(self,value:Any)->None:...
	@property
	def blendFactor(self)->Any:
		"""Global blend factor, default (1,1,1,1)"""
	@blendFactor.setter
	def blendFactor(self,value:Any)->None:...
	@property
	def multiSampleMask(self)->Any:
		"""Each bit in this mask, starting at the least significant bit (LSB), controls modification of one of the samples in a multisample render target"""
	@multiSampleMask.setter
	def multiSampleMask(self,value:Any)->None:...
	@property
	def targetBlends(self)->Any:
		"""An array of 8 MTargetBlendDesc, one for each target"""
	@targetBlends.setter
	def targetBlends(self,value:Any)->None:...
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def setDefaults(self)->Self:
		"""setDefaults() -> self

		Set all values for the blend state to their default values."""
class MCameraOverride:
	"""Camera override description. Provides information for specifying a camera override for a render operation."""
	@property
	def mCameraPath(self)->Any:
		"""Camera path override"""
	@mCameraPath.setter
	def mCameraPath(self,value:Any)->None:...
	@property
	def mUseHiddenCameraList(self)->Any:
		"""Whether to use hidden camera list override"""
	@mUseHiddenCameraList.setter
	def mUseHiddenCameraList(self,value:Any)->None:...
	@property
	def mHiddenCameraList(self)->Any:
		"""List of cameras that should not be made visible when rendering"""
	@mHiddenCameraList.setter
	def mHiddenCameraList(self,value:Any)->None:...
	@property
	def mUseProjectionMatrix(self)->Any:
		"""Whether to use the projection matrix override"""
	@mUseProjectionMatrix.setter
	def mUseProjectionMatrix(self,value:Any)->None:...
	@property
	def mProjectionMatrix(self)->Any:
		"""Camera projection matrix override"""
	@mProjectionMatrix.setter
	def mProjectionMatrix(self,value:Any)->None:...
	@property
	def mUseViewMatrix(self)->Any:
		"""Whether to use the view matrix override"""
	@mUseViewMatrix.setter
	def mUseViewMatrix(self,value:Any)->None:...
	@property
	def mViewMatrix(self)->Any:
		"""Camera view matrix override"""
	@mViewMatrix.setter
	def mViewMatrix(self,value:Any)->None:...
	@property
	def mUseNearClippingPlane(self)->Any:
		"""Whether to use the near clipping plane override"""
	@mUseNearClippingPlane.setter
	def mUseNearClippingPlane(self,value:Any)->None:...
	@property
	def mNearClippingPlane(self)->Any:
		"""Near clipping plane override"""
	@mNearClippingPlane.setter
	def mNearClippingPlane(self,value:Any)->None:...
	@property
	def mUseFarClippingPlane(self)->Any:
		"""Whether to use the far clipping plane override"""
	@mUseFarClippingPlane.setter
	def mUseFarClippingPlane(self,value:Any)->None:...
	@property
	def mFarClippingPlane(self)->Any:
		"""Far clipping plane override"""
	@mFarClippingPlane.setter
	def mFarClippingPlane(self,value:Any)->None:...
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
class MClearOperation(MRenderOperation):
	"""Class which defines the operation of clearing render target channels."""
	kClearNone:int=0
	kClearColor:int=1
	kClearDepth:int=2
	kClearStencil:int=4
	kClearAll:int=-1
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def clearColor(self)->list[float]:
		"""clearColor() -> [float, float, float, float]

		Query the first clear color values."""
	def clearColor2(self)->list[float]:
		"""clearColor2() -> [float, float, float, float]

		Query the second clear color values."""
	def clearDepth(self)->float:
		"""clearDepth() -> float

		Query the clear depth value."""
	def clearGradient(self)->bool:
		"""clearGradient() -> bool

		Query if the clear should clear with a vertical color gradient."""
	def clearStencil(self)->int:
		"""clearStencil() -> int

		Query the stencil clear value."""
	def mask(self)->int:
		"""mask() -> int

		Query the clear mask."""
	def overridesColors(self)->bool:
		"""overridesColors() -> bool

		Query whether clear colors are set by the override or come from Maya's preferences."""
	def setClearColor(self,arg:list[float])->Self:
		"""setClearColor([float, float, float, float]) -> self

		Set the first clear color values."""
	def setClearColor2(self,arg:list[float])->Self:
		"""setClearColor2([float, float, float, float]) -> self

		Set the second clear color values."""
	def setClearDepth(self,float:float)->Self:
		"""setClearDepth(float) -> self

		Set the clear depth value."""
	def setClearGradient(self,bool:bool)->Self:
		"""setClearGradient(bool) -> self

		Set whether to clear with a vertical color gradient."""
	def setClearStencil(self,int:int)->Self:
		"""setClearStencil(int) -> self

		Set the clear stencil value."""
	def setMask(self,int:int)->Self:
		"""setMask(int) -> self

		Set the clear mask to define which channels to clear."""
	def setOverridesColors(self,bool:bool)->Self:
		"""setOverridesColors(bool) -> self

		Set the enabled state to control whether the clear operation overrides Maya's color preferences."""
class MColorManagementUtilities:
	"""Utilities class for color management"""
	@staticmethod
	def getColorTransformData()->tuple[size,data]:
		"""getColorTransformData() -> (size, data)

		Obtain a reference to opaque data containing the color transform
		information needed to render the scene.

		This block of data is meant to be written by a file translator
		plug-in to a renderer file.  With the help of the SynColor SDK and
		this block of data, the external renderer can  reproduce the same
		color transformations as in Maya

		Returns the color transform data block info (bytearray)."""
	@staticmethod
	def getColorTransformCacheIdForInputSpace(inputSpaceName:str)->transformId:
		"""getColorTransformCacheIdForInputSpace(inputSpaceName) -> transformId

		Utility function to retrieve the id of a color transform
		based on the input color space name provided.

		The color transform id corresponds to a color transform that
		converts colors from the input color space specified to the scene
		rendering space

		For example, given the name of the input color space of a node,
		this function retrieves the id of the color transform to be used
		for mapping colors from input space to rendering space.  For nodes
		that have such a color space attribute, the transform id is meant
		to be written by a file translator plug-in to a renderer file
		alongside the node information. This id corresponds to a color
		transform contained in the color transform data retrieved by
		MRenderUtilities::getColorTransformData.

		* inputSpaceName (string) - Name of the color space of the node.

		Returns identifier of the color transform required to be
		applied to the node."""
	@staticmethod
	def getColorTransformCacheIdForOutputTransform()->transformId:
		"""getColorTransformCacheIdForOutputTransform() -> transformId

		Utility function to retrieve the id of the color transform to be applied on the final output.

		The color transform id corresponds to a color transform that
		converts colors of the rendered image to a target color space.

		This id corresponds to a color transform contained in the color
		transform data retrieved by the MColorTransformData class.

		Returns identifier of the color transform required to be
		applied on the rendered image"""
	@staticmethod
	def isColorManagementEnabled()->bool:
		"""isColorManagementEnabled() -> Boolean

		Returns whether color management is enabled for the current scene.

		True if color management is enabled."""
	@staticmethod
	def isColorManagementAvailable()->bool:
		"""isColorManagementAvailable() -> Boolean

		Returns whether color management is available for the current scene.

		True if color management is enabled."""
class MComponentDataIndexing:
	"""Class for storing index mapping when vertices are shared."""
	kFaceVertex:int=0
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def indices(self)->om.MUintArray:
		"""indices() -> MUintArray

		Get the array of vertex indices for the component."""
	def componentType(self)->int:
		"""componentType() -> MComponentType

		Get the component type that the vertex indices represent."""
	def setComponentType(self,MComponentType:Any)->Self:
		"""setComponentType(MComponentType) -> self

		Set the component type that the vertex indices represent."""
class MComponentDataIndexingList:
	"""A list of MComponentDataIndexing objects."""
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def __len__(self)->int:
		"""Return len(self)."""
	def __getitem__(self,index:int)->Any:
		"""Return self[key]."""
	def append(self,MComponentDataIndexing:Any)->bool:
		"""append(MComponentDataIndexing) -> bool

		Add a MComponentDataIndexing to the list. Creates and stores a copy which is owned by the list."""
	def remove(self,index:int)->bool:
		"""remove(index) -> bool

		Remove a MComponentDataIndexing from the list."""
	def clear(self)->Self:
		"""clear() -> self

		Clear the list."""
class MDepthNormalizationDescription:
	"""Information required to perform normalization of values stored in the depth buffer of an MImage with respect to clipping plane range."""
	@property
	def fNearClipDistance(self)->Any:
		"""Near clip plane of a camera"""
	@fNearClipDistance.setter
	def fNearClipDistance(self,value:Any)->None:...
	@property
	def fFarClipDistance(self)->Any:
		"""Far clip plane of a camera"""
	@fFarClipDistance.setter
	def fFarClipDistance(self,value:Any)->None:...
	@property
	def fDepthScale(self)->Any:
		"""Scale to apply to depth values"""
	@fDepthScale.setter
	def fDepthScale(self,value:Any)->None:...
	@property
	def fDepthBias(self)->Any:
		"""Bias to apply to depth value"""
	@fDepthBias.setter
	def fDepthBias(self,value:Any)->None:...
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
class MDepthStencilState:
	"""Container class for an acquired complete GPU depth stencil state."""
	kKeepStencil:int=1
	kZeroStencil:int=2
	kReplaceStencil:int=3
	kIncrementStencilSat:int=4
	kDecrementStencilSat:int=5
	kInvertStencil:int=6
	kIncrementStencil:int=7
	kDecrementStencil:int=8
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def desc(self)->MDepthStencilStateDesc:
		"""desc() -> MDepthStencilStateDesc

		Get the depth-stencil state descriptor that was used to create the state object."""
	def resourceHandle(self)->int:
		"""resourceHandle() -> long

		Returns a long containing a C++ 'void' pointer which points to the draw API dependent handle for a depth-stencil state.
		For OpenGL, such a handle does not exist and a NULL pointer will be returned.
		For DirectX, a pointer to a Direct3D state will be returned."""
class MDepthStencilStateDesc:
	"""Descriptor for a complete depth-stencil state."""
	@property
	def depthEnable(self)->Any:
		"""Enables depth buffer reads and compares, default true"""
	@depthEnable.setter
	def depthEnable(self,value:Any)->None:...
	@property
	def depthWriteEnable(self)->Any:
		"""Enables depth buffer writes, default true"""
	@depthWriteEnable.setter
	def depthWriteEnable(self,value:Any)->None:...
	@property
	def depthFunc(self)->Any:
		"""Sets the depth buffer comparison function, default less than"""
	@depthFunc.setter
	def depthFunc(self,value:Any)->None:...
	@property
	def stencilEnable(self)->Any:
		"""Enables stencil buffer operation"""
	@stencilEnable.setter
	def stencilEnable(self,value:Any)->None:...
	@property
	def stencilReadMask(self)->Any:
		"""Sets a bitwise stencil buffer read mask, default 0xff"""
	@stencilReadMask.setter
	def stencilReadMask(self,value:Any)->None:...
	@property
	def stencilWriteMask(self)->Any:
		"""Sets a bitwise stencil buffer write mask, default 0xff"""
	@stencilWriteMask.setter
	def stencilWriteMask(self,value:Any)->None:...
	@property
	def stencilReferenceVal(self)->Any:
		"""Sets the stencil reference value"""
	@stencilReferenceVal.setter
	def stencilReferenceVal(self,value:Any)->None:...
	@property
	def frontFace(self)->Any:
		"""Sets the stencil op for the front facing fragments"""
	@frontFace.setter
	def frontFace(self,value:Any)->None:...
	@property
	def backFace(self)->Any:
		"""Sets the stencil op for the back facing fragments"""
	@backFace.setter
	def backFace(self,value:Any)->None:...
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def setDefaults(self)->Self:
		"""setDefaults() -> self

		Set all values for the depth stencil state to their default values."""
class MDrawContext(MFrameContext):
	"""Class to allow access to hardware draw context information."""
	kFilteredToLightLimit:int=0
	kFilteredIgnoreLightLimit:int=1
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def getFrameStamp(self)->int:
		"""getFrameStamp() -> long

		Returns the current frame stamp."""
	def getSceneBox(self)->om.MBoundingBox:
		"""getSceneBox() -> MBoundingBox

		Get a bounding box of the scene in world space."""
	def getFrustumBox(self)->om.MBoundingBox:
		"""getFrustumBox() -> MBoundingBox

		Get the bounding box of the current view frustum in world space."""
	def getRenderTargetSize(self)->list[int]:
		"""getRenderTargetSize() -> [int, int]

		Get the size of the render target (output buffer) being rendered into.
		The dimensions of the target are in pixels"""
	def getDepthRange(self)->list[float]:
		"""getDepthRange() -> [float, float]

		Get the depth range which specifies the mapping of depth values from normalized device coordinates to window coordinates.
		The depth range values are normally 0.0 and 1.0."""
	def viewDirectionAlongNegZ(self)->bool:
		"""viewDirectionAlongNegZ() -> bool

		Return whether the view direction is pointing down the -Z axis."""
	def numberOfActiveLights(self,lightFilter:int=MDrawContext.kFilteredToLightLimit)->int:
		"""numberOfActiveLights(lightFilter=kFilteredToLightLimit) -> int

		Return the number of available lights to render the scene,
		only considering lights which pass the filter option."""
	def getLightInformation(self,lightNumber:Any,lightFilter:int=MDrawContext.kFilteredToLightLimit)->list[positions|direction|intensity|color|hasDirection|hasPosition]:
		"""getLightInformation(lightNumber, lightFilter=kFilteredToLightLimit) -> [positions, direction, intensity, color, hasDirection, hasPosition]

		Return common lighting information for a given active light."""
	def getLightParameterInformation(self,lightNumber:Any,lightFilter:int=MDrawContext.kFilteredToLightLimit)->MLightParameterInformation:
		"""getLightParameterInformation(lightNumber, lightFilter=kFilteredToLightLimit) -> MLightParameterInformation

		Return parameter information for a given active light."""
	def getStateManager(self)->MStateManager:
		"""getStateManager() -> MStateManager

		Access the GPU state manager for the current draw context."""
	def getPassContext(self)->MPassContext:
		"""getPassContext() -> MPassContext

		Access the current pass context."""
	def copyCurrentColorRenderTarget(self,string:Any)->MRenderTarget:
		"""copyCurrentColorRenderTarget(string) -> MRenderTarget

		Get a copy of the current color render target.
		When the object is no longer needed, MRenderTargetManager::releaseRenderTarget() should be called
		to notify the target manager that the caller is done with the render target."""
	def copyCurrentDepthRenderTarget(self,string:Any)->MRenderTarget:
		"""copyCurrentDepthRenderTarget(string) -> MRenderTarget

		Get a copy of the current depth render target.
		When the object is no longer needed, MRenderTargetManager::releaseRenderTarget() should be called
		to notify the target manager that the caller is done with the render target."""
	def copyCurrentColorRenderTargetToTexture(self)->MTexture:
		"""copyCurrentColorRenderTargetToTexture() -> MTexture

		Get a copy of the current color render target as a texture.
		When the texture is no longer needed, MTextureManager::releaseTexture() should be called."""
	def copyCurrentDepthRenderTargetToTexture(self)->MTexture:
		"""copyCurrentDepthRenderTargetToTexture() -> MTexture

		Get a copy of the current depth render target as a texture.
		When the texture is no longer needed, MTextureManager::releaseTexture() should be called."""
class MDrawRegistry:
	"""Access the registry associating node types with custom draw classes"""
	@staticmethod
	def deregisterComponentConverter(renderItemName:str)->None:
		"""deregisterComponentConverter(renderItemName) -> None

		Deregister an implementation of MPxComponentConverter."""
	@staticmethod
	def deregisterDrawOverrideCreator(drawClassification:Any,registrantId:Any)->None:
		"""deregisterDrawOverrideCreator(drawClassification, registrantId) -> None

		Deregister an implementation of MPxDrawOverride."""
	@staticmethod
	def deregisterGeometryOverrideCreator(drawClassification:Any,registrantId:Any)->None:
		"""deregisterGeometryOverrideCreator(drawClassification, registrantId) -> None

		Deregister an implementation of MPxGeometryOverride."""
	@staticmethod
	def deregisterImagePlaneOverrideCreator(drawClassification:Any,registrantId:Any)->None:
		"""deregisterImagePlaneOverrideCreator(drawClassification, registrantId) -> None

		Deregister an implementation of MPxImagePlaneOverride."""
	@staticmethod
	def deregisterIndexBufferMutator(primitiveType:Any)->None:
		"""deregisterIndexBufferMutator(primitiveType) -> None

		Deregister an implementation of MPxIndexBufferMutator."""
	@staticmethod
	def deregisterPrimitiveGenerator(primitiveType:Any)->None:
		"""deregisterPrimitiveGenerator(primitiveType) -> None

		Deregister an implementation of MPxPrimitiveGenerator."""
	@staticmethod
	def deregisterShaderOverrideCreator(drawClassification:Any,registrantId:Any)->None:
		"""deregisterShaderOverrideCreator(drawClassification, registrantId) -> None

		Deregister an implementation of MPxShaderOverride."""
	@staticmethod
	def deregisterShadingNodeOverrideCreator(drawClassification:Any,registrantId:Any)->None:
		"""deregisterShadingNodeOverrideCreator(drawClassification, registrantId) -> None

		Deregister an implementation of MPxShadingNodeOverride."""
	@staticmethod
	def deregisterSubSceneOverrideCreator(drawClassification:Any,registrantId:Any)->None:
		"""deregisterSubSceneOverrideCreator(drawClassification, registrantId) -> None

		Deregister an implementation of MPxSubSceneOverride."""
	@staticmethod
	def deregisterSurfaceShadingNodeOverrideCreator(drawClassification:Any,registrantId:Any)->None:
		"""deregisterSurfaceShadingNodeOverrideCreator(drawClassification, registrantId) -> None

		Deregister an implementation of MPxSurfaceShadingNodeOverride."""
	@staticmethod
	def deregisterVertexBufferGenerator(bufferName:str)->None:
		"""deregisterVertexBufferGenerator(bufferName) -> None

		Deregister an implementation of MPxVertexBufferGenerator."""
	@staticmethod
	def deregisterVertexBufferMutator(bufferName:str)->None:
		"""deregisterVertexBufferMutator(bufferName) -> None

		Deregister an implementation of MPxVertexBufferMutator."""
	@staticmethod
	def registerComponentConverter(renderItemName:str,creator:Any)->None:
		"""registerComponentConverter(renderItemName, creator) -> None

		Register an implementation of MPxComponentConverter to use with render items that have the specified name."""
	@staticmethod
	def registerDrawOverrideCreator(drawClassification:Any,registrantId:Any,creator:Any)->None:
		"""registerDrawOverrideCreator(drawClassification, registrantId, creator) -> None

		Register an implementation of MPxDrawOverride to use with DAG objects that have the specified, draw-specific classification string."""
	@staticmethod
	def registerGeometryOverrideCreator(drawClassification:Any,registrantId:Any,creator:Any)->None:
		"""registerGeometryOverrideCreator(drawClassification, registrantId, creator) -> None

		Register an implementation of MPxGeometryOverride to use with nodes that have the specified, draw-specific classification string."""
	@staticmethod
	def registerImagePlaneOverrideCreator(drawClassification:Any,registrantId:Any,creator:Any)->None:
		"""registerImagePlaneOverrideCreator(drawClassification, registrantId, creator) -> None

		Register an implementation of MPxImagePlaneOverride to use with DAG objects that have the specified, draw-specific classification string."""
	@staticmethod
	def registerIndexBufferMutator(primitiveType:Any,creator:Any)->None:
		"""registerIndexBufferMutator(primitiveType, creator) -> None

		Register an implementation of MPxIndexBufferMutator to generate custom primitive types for shapes."""
	@staticmethod
	def registerPrimitiveGenerator(primitiveType:Any,creator:Any)->None:
		"""registerPrimitiveGenerator(primitiveType, creator) -> None

		Register an implementation of MPxPrimitiveGenerator to generate custom primitive types for shapes."""
	@staticmethod
	def registerShaderOverrideCreator(drawClassification:Any,registrantId:Any,creator:Any)->None:
		"""registerShaderOverrideCreator(drawClassification, registrantId, creator) -> None

		Register an implementation of MPxShaderOverride to use with nodes that have the specified, draw-specific classification string."""
	@staticmethod
	def registerShadingNodeOverrideCreator(drawClassification:Any,registrantId:Any,creator:Any)->None:
		"""registerShadingNodeOverrideCreator(drawClassification, registrantId, creator) -> None

		Register an implementation of MPxShadingNodeOverride to use with nodes that have the specified, draw-specific classification string."""
	@staticmethod
	def registerSubSceneOverrideCreator(drawClassification:Any,registrantId:Any,creator:Any)->None:
		"""registerSubSceneOverrideCreator(drawClassification, registrantId, creator) -> None

		Register an implementation of MPxSubSceneOverride to use with DAG objects that have the specified, draw-specific classification string."""
	@staticmethod
	def registerSurfaceShadingNodeOverrideCreator(drawClassification:Any,registrantId:Any,creator:Any)->None:
		"""registerSurfaceShadingNodeOverrideCreator(drawClassification, registrantId, creator) -> None

		Register an implementation of MPxSurfaceShadingNodeOverride to use with surface shaders that have the specified, draw-specific classification string."""
	@staticmethod
	def registerVertexBufferGenerator(bufferName:str,creator:Any)->None:
		"""registerVertexBufferGenerator(bufferName, creator) -> None

		Register an implementation of MPxVertexBufferGenerator to provide custom vertex streams for shapes."""
	@staticmethod
	def registerVertexBufferMutator(bufferName:str,creator:Any)->None:
		"""registerVertexBufferMutator(bufferName, creator) -> None

		Register an implementation of MPxVertexBufferMutator to provide custom vertex streams for shapes."""
class MFragmentManager:
	"""Provides facilities for managing fragments for use with Viewport 2.0."""
	kVertexShader:int=0
	kPixelShader:int=1
	kGeometryShader:int=2
	kHullShader:int=3
	kHullConstantShader:int=4
	kDomainShader:int=5
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def addFragmentGraphFromBuffer(self,buffer:Any)->str:
		"""addFragmentGraphFromBuffer(buffer) -> string

		Add a new fragment graph to the manager.
		The fragment graph is defined as XML stored in a string buffer.Returns name of the registered fragment graph, or empty string on failure.

		- buffer (string) - String containing an XML description of the fragment graph."""
	def addFragmentGraphFromFile(self,fileName:str)->str:
		"""addFragmentGraphFromFile(fileName) -> string

		Add a new fragment graph to the manager.
		The fragment graph is defined as XML stored in the given file.Returns name of the registered fragment graph, or empty string on failure.

		- fileName (string) - The name of the file containing the fragment graph description."""
	def addFragmentPath(self,path:Any)->bool:
		"""addFragmentPath(path) -> bool

		Add a path to the list of fragment search paths used when parsing the file path for any
		methods which add fragments to the manager from files on disk."""
	def addShadeFragmentFromBuffer(self,buffer:Any,hidden:Any)->str:
		"""addShadeFragmentFromBuffer(buffer, hidden) -> string

		Add a new fragment to the manager.
		The fragment is defined as XML stored in a string buffer.
		Returns name of the registered fragment, or empty string on failure.

		- buffer (string) - String containing an XML description of the fragment.
		- hidden (bool) - If True, this fragment will not appear in the list returned by fragmentList()
		                  and it will not be possible to query the XML for it using getFragmentXML()."""
	def addShadeFragmentFromFile(self,fileName:str,hidden:Any)->str:
		"""addShadeFragmentFromFile(fileName, hidden) -> string

		Add a new fragment to the manager.
		The fragment is defined as XML stored in the given file.
		Returns name of the registered fragment, or empty string on failure.

		- fileName (string) - The name of the file containing the fragment description.
		- hidden (bool) - If True, this fragment will not appear in the list returned by fragmentList()
		                  and it will not be possible to query the XML for it using getFragmentXML()."""
	def fragmentList(self)->list[str]:
		"""fragmentList() -> list of string

		Returns a list of the names of all registered fragments and fragment graphs."""
	def getEffectOutputDirectory(self)->str:
		"""getEffectOutputDirectory() -> string

		Get the directory to be used for effect file output."""
	@overload
	def getFragmentXML(self,fragmentName:str)->str:
		"""getFragmentXML(fragmentName) -> string
		getFragmentXML(shadingNode, includeUpstreamNodes=False, objectContext=None) -> string

		Get the XML representation of the named fragment or fragment graph.
		Return None if failed
		- fragmentName (string) - The name of the fragment to get the XML for.

		Get XML code for the fragment graph Maya would use to represent the given shading node in Viewport 2.0.
		Return None if failed
		- shadingNode (MObject) - The node to get the XML code for.
		- includeUpstreamNodes (bool) - Return the XML for the entire fragment graph rooted at the given shading node if True.
		- objectContext (MDagPath) - Optional path to an instance that is associated with the shading node to provide object context."""
	@overload
	def getFragmentXML(self,shadingNode:Any,includeUpstreamNodes:Any=False,objectContext:Any|None=None)->str:
		"""getFragmentXML(fragmentName) -> string
		getFragmentXML(shadingNode, includeUpstreamNodes=False, objectContext=None) -> string

		Get the XML representation of the named fragment or fragment graph.
		Return None if failed
		- fragmentName (string) - The name of the fragment to get the XML for.

		Get XML code for the fragment graph Maya would use to represent the given shading node in Viewport 2.0.
		Return None if failed
		- shadingNode (MObject) - The node to get the XML code for.
		- includeUpstreamNodes (bool) - Return the XML for the entire fragment graph rooted at the given shading node if True.
		- objectContext (MDagPath) - Optional path to an instance that is associated with the shading node to provide object context."""
	def getIntermediateGraphOutputDirectory(self)->str:
		"""getIntermediateGraphOutputDirectory() -> string

		Get the directory to be used for intermediate fragment graph output."""
	def hasFragment(self,string:Any)->bool:
		"""hasFragment(string) -> bool

		Returns True if a fragment of the given name has been registered with the fragment manager."""
	def removeFragment(self,fragmentName:str)->bool:
		"""removeFragment(fragmentName) -> bool

		Remove a named fragment or fragment graph from the fragment manager. This
		can be used to remove registered fragments on plug-in unload.

		Any fragment may be removed including those defined by Maya. In this way
		users may replace default Maya fragments with custom fragments. When
		replacing an existing Maya fragment it is important to maintain the same
		fragment interface (i.e. input and output parameters) otherwise Maya's
		behavior will be undefined. Maya's behavior will also be undefined if a
		default Maya fragment is removed without replacing it.

		Returns True if the fragment was successfuly removed from the fragment manager."""
	def setEffectOutputDirectory(self,string:Any)->Self:
		"""setEffectOutputDirectory(string) -> self

		Set the path to use for dumping final effect files."""
	def setIntermediateGraphOutputDirectory(self,string:Any)->Self:
		"""setIntermediateGraphOutputDirectory(string) -> self

		Set the path to use for dumping intermediate fragment graph XML files."""
	def addAutomaticShaderStageInput(self,int:int,string:Any,string2:Any,int2:int,bool:bool)->bool:
		"""addAutomaticShaderStageInput(int, string, string, int, bool) -> bool

		Add a parameter to the list of automatic input parameters for a specified
		shader stage. If an input parameter with the same name or semantic is found
		unconnected in a fragment graph during compilation, the parameter will be
		automatically connected with a matching source, which can be either a member
		in the shader stage input structure or a registered fragment, depending on
		whether or not the parameter is a varying input.

		The method will fail if the parameter name has been registered already. A
		plug-in can add a unique prefix to the parameter name to avoid conflicts.

		- shaderStage (int) - Shader stage
		- parameterName (string) - Name of the parameter
		- semantic (string) - Semantic of the parameter
		- parameterType (int) - Type of the parameter
		- isVaryingInput (bool) - Whether or not the parameter is a varying input"""
	def removeAutomaticShaderStageInput(self,int:int,string:Any)->bool:
		"""removeAutomaticShaderStageInput(int, string) -> bool

		Remove a parameter from the list of automatic input parameters for a
		specified shader stage.

		The method will fail if the parameter name hasn't been registered yet. A
		plug-in should keep track of its own parameters and clean them up at an
		appropriate time.

		- shaderStage (int) - Shader stage
		- parameterName (string) - Name of the parameter"""
	def addDomainShaderInputNameMapping(self,string:Any,string2:Any)->bool:
		"""addDomainShaderInputNameMapping(string, string) -> bool

		Add a mapping between a parameter name (realParamName) and a transient
		name (domainParamName) which is used in domain shader. If realParamName
		is found in the domain shader output struct when compiling a shader fragment
		graph, it will temporarily be treated as domainParamName to connect to a
		matching source, which can be either a member in the domain shader stage input
		struct or a registered tessellation evaluation fragment, depending on whether
		or not domainParamName has been registered as a varying input.

		The method will fail if a mapping has already been added for realParamName.

		- realParamName (string) - Real name of the parameter
		- domainParamName (string) - Transient name of the parameter in domain shader"""
	def removeDomainShaderInputNameMapping(self,string:Any)->bool:
		"""removeDomainShaderInputNameMapping(string) -> bool

		Remove a mapping between a parameter name (realParamName) and a transient
		name (domainParamName) which is used in domain shader.

		The method will fail if a mapping hasn't been added for realParamName yet.

		- realParamName (string) - Real name of the parameter"""
	def findDomainShaderInputName(self,string:Any)->str:
		"""findDomainShaderInputName(string) -> string

		Find the transient name which is used in domain shader.

		Returns transient name of the parameter, or empty string on failure.

		- realParamName (string) - Real name of the parameter"""
	def getColorManagementFragmentInfo(self,string:Any)->Any:
		"""getColorManagementFragmentInfo(string) -> tuple(string, string, string)

		Returns the name and parameters of a shader fragment that converts a color from the
		requested inputColorSpace to the current working color space.

		The returned information can be used to extend a shader via MShaderManager::addInputFragment
		 or MShaderManager::addInputFragmentForMultiParams.

		The fragment and output name will change, especially when the working color space changes.
		Please do not persist or cache values returned by this API.

		Returns a tuple containing the fragment, input, and output names, or None on failure.

		- inputColorSpace (string) - Input color space to be converted to the current working color space."""
class MFrameContext:
	"""This class contains some global information for the current render frame."""
	kWorldMtx:int=0
	kWorldTransposeMtx:int=1
	kWorldInverseMtx:int=2
	kWorldTranspInverseMtx:int=3
	kViewMtx:int=4
	kViewTransposeMtx:int=5
	kViewInverseMtx:int=6
	kViewTranspInverseMtx:int=7
	kProjectionMtx:int=8
	kProjectionTranposeMtx:int=9
	kProjectionInverseMtx:int=10
	kProjectionTranspInverseMtx:int=11
	kViewProjMtx:int=12
	kViewProjTranposeMtx:int=13
	kViewProjInverseMtx:int=14
	kViewProjTranspInverseMtx:int=15
	kWorldViewMtx:int=16
	kWorldViewTransposeMtx:int=17
	kWorldViewInverseMtx:int=18
	kWorldViewTranspInverseMtx:int=19
	kWorldViewProjMtx:int=20
	kWorldViewProjTransposeMtx:int=21
	kWorldViewProjInverseMtx:int=22
	kWorldViewProjTranspInverseMtx:int=23
	kViewPosition:int=0
	kViewDirection:int=1
	kViewUp:int=2
	kViewRight:int=3
	kViewportPixelSize:int=4
	kViewNearClipValue:int=5
	kViewFarClipValue:int=6
	kViewUnnormlizedNearClipValue:int=7
	kViewUnnormalizedFarClipValue:int=8
	kGouraudShaded:int=1
	kWireFrame:int=2
	kBoundingBox:int=4
	kTextured:int=8
	kDefaultMaterial:int=16
	kXrayJoint:int=32
	kXray:int=64
	kTwoSidedLighting:int=128
	kFlatShaded:int=256
	kShadeActiveOnly:int=512
	kXrayActiveComponents:int=1024
	kBackfaceCulling:int=2048
	kSmoothWireframe:int=4096
	kSelectionHighlighting:int=8192
	kNoLighting:int=0
	kAmbientLight:int=1
	kLightDefault:int=2
	kSelectedLights:int=3
	kSceneLights:int=4
	kCustomLights:int=5
	kAmbientOcclusion:int=0
	kMotionBlur:int=1
	kGammaCorrection:int=2
	kViewColorTransformEnabled:int=2
	kDepthOfField:int=3
	kAntiAliasing:int=4
	kUnsorted:int=0
	kObjectSorting:int=1
	kWeightedAverage:int=2
	kDepthPeeling:int=3
	kWireframeOnShadedFull:int=0
	kWireFrameOnShadedReduced:int=1
	kWireFrameOnShadedNone:int=2
	k3dViewport:int=0
	k2dViewport:int=1
	kImage:int=2
	kFogLinear:int=0
	kFogExp:int=1
	kFogExp2:int=2
	kExcludeNone:int=0
	kExcludeNurbsCurves:int=1
	kExcludeNurbsSurfaces:int=2
	kExcludeMeshes:int=4
	kExcludePlanes:int=8
	kExcludeLights:int=16
	kExcludeCameras:int=32
	kExcludeJoints:int=64
	kExcludeIkHandles:int=128
	kExcludeDeformers:int=256
	kExcludeDynamics:int=512
	kExcludeParticleInstancers:int=1024
	kExcludeLocators:int=2048
	kExcludeDimensions:int=4096
	kExcludeSelectHandles:int=8192
	kExcludePivots:int=16384
	kExcludeTextures:int=32768
	kExcludeGrid:int=65536
	kExcludeCVs:int=131072
	kExcludeHulls:int=262144
	kExcludeStrokes:int=524288
	kExcludeSubdivSurfaces:int=1048576
	kExcludeFluids:int=2097152
	kExcludeFollicles:int=4194304
	kExcludeHairSystems:int=8388608
	kExcludeImagePlane:int=16777216
	kExcludeNCloths:int=33554432
	kExcludeNRigids:int=67108864
	kExcludeDynamicConstraints:int=134217728
	kExcludeManipulators:int=268435456
	kExcludeNParticles:int=536870912
	kExcludeMotionTrails:int=1073741824
	kExcludeHoldOuts:int=2147483648
	kExcludePluginShapes:int=4294967296
	kExcludeHUD:int=8589934592
	kExcludeClipGhosts:int=17179869184
	kExcludeGreasePencils:int=34359738368
	kExcludeControllers:int=68719476736
	kExcludeAll:int=18446744073709551615
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	@staticmethod
	def semanticToMatrixType(string:Any)->int:
		"""semanticToMatrixType(string) -> int

		Given a semantic name return the corresponding matrix enumeration that can be used to retrieve a matrix value via the getMatrix() method.

		  MFrameContext.kWorldMtx                        Object to world matrix
		  MFrameContext.kWorldTransposeMtx               Object to world matrix transpose
		  MFrameContext.kWorldInverseMtx                 Object to world matrix inverse
		  MFrameContext.kWorldTranspInverseMtx           Object to world matrix transpose inverse (adjoint)
		  MFrameContext.kViewMtx                         World to view matrix
		  MFrameContext.kViewTransposeMtx                World to view matrix tranpose
		  MFrameContext.kViewInverseMtx                  World to view matrix inverse
		  MFrameContext.kViewTranspInverseMtx            World to view matrix transpose inverse (adjoint)
		  MFrameContext.kProjectionMtx                   Projection matrix
		  MFrameContext.kProjectionTranposeMtx           Projection matrix tranpose
		  MFrameContext.kProjectionInverseMtx            Projection matrix inverse
		  MFrameContext.kProjectionTranspInverseMtx      Projection matrix tranpose inverse (adjoint)
		  MFrameContext.kViewProjMtx                     View * projection matrix
		  MFrameContext.kViewProjTranposeMtx             View * projection matrix tranpose
		  MFrameContext.kViewProjInverseMtx              View * projection matrix inverse
		  MFrameContext.kViewProjTranspInverseMtx        View * projection matrix tranpose inverse (adjoint)
		  MFrameContext.kWorldViewMtx                    World * view matrix
		  MFrameContext.kWorldViewTransposeMtx           World * view matrix transpose
		  MFrameContext.kWorldViewInverseMtx             World * view matrix inverse
		  MFrameContext.kWorldViewTranspInverseMtx       World * view matrix transpose inverse (adjoint)
		  MFrameContext.kWorldViewProjMtx                World * view * projection matrix
		  MFrameContext.kWorldViewProjTransposeMtx       World * view * projection matrix transpose
		  MFrameContext.kWorldViewProjInverseMtx         World * view * projection matrix inverse
		  MFrameContext.kWorldViewProjTranspInverseMtx   World * view * projection matrix tranpose inverse (adjoint)"""
	def getMatrix(self,int:int)->om.MMatrix:
		"""getMatrix(int) -> MMatrix

		Get a matrix value of a certain type.
		Note that not all types are available for querying in MFrameContext.
		Return None if matrix type not available from MFrameContext.
		For a list of matrix type, see MDrawContext.semanticToMatrixType() description."""
	@staticmethod
	def semanticToTupleType(string:Any)->int:
		"""semanticToTupleType(string) -> int

		Given a semantic name return the corresponding tuple enumeration that can be used to retrieve a value via the getTuple() method.

		  MFrameContext.kViewPosition         View position
		  MFrameContext.kViewDirection        View direction vector
		  MFrameContext.kViewUp               View up vector
		  MFrameContext.kViewRight            View right vector
		  MFrameContext.kViewportPixelSize    Viewport size in pixels (single value)
		  MFrameContext.kViewNearClipValue    Camera near clip value (single value)
		  MFrameContext.kViewFarClipValue     Camera far clip value (single value)
		  MFrameContext.kViewUnnormlizedNearClipValue Unnormalized camera near clip value (single value)
		         MFrameContext.kViewUnnormalizedFarClipValue Unnormalized camera far clip value (single value)"""
	def getTuple(self,int:int)->om.MDoubleArray:
		"""getTuple(int) -> MDoubleArray

		Get a tuple (vector, position or single) value of a certain type.
		Note that not all types are available for querying in MFrameContext.
		Return None if unknown tuple type."""
	def getViewportDimensions(self)->list[originX|originY|width|height]:
		"""getViewportDimensions() -> [originX, originY, width, height]

		Get the viewport dimensions. The origin is the upper left corner of the viewport."""
	def getGlobalLineWidth(self)->float:
		"""getGlobalLineWidth() -> float

		Get global line width."""
	def getCurrentCameraPath(self)->om.MDagPath:
		"""getCurrentCameraPath() -> MDagPath

		Get the path to the camera being used to render the current frame."""
	def getCurrentColorRenderTarget(self)->MRenderTarget:
		"""getCurrentColorRenderTarget() -> MRenderTarget

		Get current color render target.
		Calling code is responsible for invoking MRenderTargetManager::releaseRenderTarget() to release the reference to the target after use."""
	def getCurrentDepthRenderTarget(self)->MRenderTarget:
		"""getCurrentDepthRenderTarget() -> MRenderTarget

		Get current depth render target.
		Calling code is responsible for invoking MRenderTargetManager::releaseRenderTarget() to release the reference to the target after use."""
	def objectTypeExclusions(self)->int:
		"""objectTypeExclusions() -> long

		Get the object type exclusions as a bitfield.
		        The bitfield can be tested using the bits defined by class statics starting with kExclude."""
	def classificationExclusions(self)->list[Any]:
		"""classificationExclusions() -> [classification strings]

		Get a list of drawdb strings for object which are excluded from display"""
	def getDisplayStyle(self)->int:
		"""getDisplayStyle() -> int

		The DisplayStyle enums can be use to test the bit field for the enabling of any
		of the listed display modes. For example to test for wireframe on shaded the test
		would be test against the bit for kGourandShaded or kFlatShaded as well as testing
		against the bit for kWireframe.

		  MFrameContext.kGouraudShaded        Shaded display.
		  MFrameContext.kWireFrame            Wire frame display.
		  MFrameContext.kBoundingBox          Bounding box display.
		  MFrameContext.kTextured             Textured display.
		  MFrameContext.kDefaultMaterial      Default material display.
		  MFrameContext.kXrayJoint            X-ray joint display.
		  MFrameContext.kXray                 X-ray display.
		  MFrameContext.kTwoSidedLighting     Two-sided lighting enabled.
		  MFrameContext.kFlatShaded              Flat shading display.
		  MFrameContext.kShadeActiveOnly      Shade active object only.
		  MFrameContext.kXrayActiveComponents X-ray active components.
		  MFrameContext.kBackfaceCulling                 Backface culling enabled.
		  MFrameContext.kSmoothWireframe             Smooth wireframe enabled."""
	def getLightingMode(self)->int:
		"""getLightingMode() -> int

		Get the current light mode.

		  MFrameContext.kNoLighting           Use no light
		  MFrameContext.kAmbientLight      Use global ambient light
		  MFrameContext.kLightDefault      Use default light
		  MFrameContext.kSelectedLights    Use lights which are selected
		  MFrameContext.kSceneLights       Use all lights in the scene
		  MFrameContext.kCustomLights      Use a custom set of lights which are not part of the scene. Currently this applies for use in the Hypershade Material Viewer panel"""
	def getLightLimit(self)->int:
		"""getLightLimit() -> int

		Get the current light limit."""
	def getPostEffectEnabled(self,int:int)->bool:
		"""getPostEffectEnabled(int) -> bool

		Returns if a given post effect is currently enabled.

		  MFrameContext.kAmbientOcclusion    Screen-space ambient occlusion
		  MFrameContext.kMotionBlur          2D Motion blur
		  MFrameContext.kGammaCorrection     Gamma correction
		  MFrameContext.kDepthOfField        Depth of field
		  MFrameContext.kAntiAliasing        Hardware multi-sampling"""
	def getTransparencyAlgorithm(self)->int:
		"""getTransparencyAlgorithm() -> int

		Get the current transparency algoritm.

		  MFrameContext.kUnsorted            Unsorted transparent object drawing
		  MFrameContext.kObjectSorting       Object sorting of transparent objects
		  MFrameContext.kWeightedAverage     Weight average transparency
		  MFrameContext.kDepthPeeling        Depth-peel transparency"""
	@staticmethod
	def inUserInteraction()->bool:
		"""inUserInteraction() -> bool

		Returns True during any interactive refresh, as when user is interacting with the scene
		in any way including camera changes, object or component TRS changes, etc."""
	@staticmethod
	def userChangingViewContext()->bool:
		"""userChangingViewContext() -> bool

		Returns True during any interactive refresh, as when user is    changing the view using view context
		tools such as tumble, dolly or track."""
	@staticmethod
	def wireOnShadedMode()->int:
		"""wireOnShadedMode() -> int

		Returns the global user display preference which indicates how wireframe should be drawn on top of objects while in shaded mode.

		Please refer to documentation on the 'Wireframe-on-shaded' option under the 'Display->View' tab in the preferences window.

		Note that 'viewport in wireframe on shaded mode' is a different option which is per viewport. This can be tested by testing if
		a shaded mode is set as well as wireframe mode. Refer to the enumerations DisplayStyle and the method getDisplayStyle().


		  MFrameContext.kWireframeOnShadedFull      Draw wireframe
		  MFrameContext.kWireFrameOnShadedReduced   Draw wireframe but with reduced quality
		  MFrameContext.kWireFrameOnShadedNone      Do not draw wireframe"""
	@staticmethod
	def shadeTemplates()->bool:
		"""shadeTemplates() -> bool

		Returns the display preference indicating whether templated objects should be drawn shaded."""
	def renderingDestination(self)->list[int|str]:
		"""renderingDestination() -> [int, destinationName]

		Return the destination (type and name) that the renderer is drawing to.

		  MFrameContext.k3dViewport    Rendering to an interactive 3d viewport
		  MFrameContext.k2dViewport    Rendering to an interactive 2d viewport such as the render view
		  MFrameContext.kImage         Rendering to an image"""
	def getEnvironmentParameters(self)->list[bool|str]:
		"""getEnvironmentParameters() -> [bool, string]

		Get parameters for currently used environment. Note that this information is set
		per viewport and so might change between draw calls if multiple viewports are
		displayed at the same time.
		Return the destination (type and name) that the renderer is drawing to."""
	def getDOFParameters(self)->list[enabled|focalDistance|alpha]:
		"""getDOFParameters() -> [enabled, focalDistance, alpha]

		Get the parameters generated by Maya for the circle-of-confusion depth shader used
		for a pass used when computing depth of field.


		This pass is indicated by the pass semantic MPassContext::kDOFPassSemantic.
		The shader fragment used is called cocDepthSurface.
		The XML wrapper can be queried from MFragmentManager or using the 'ogs -xml maya_CocDepthSurface' command."""
	def getBackgroundParameters(self)->list[displayGradient|clearColorFlag|clearDepthFlag|clearStencilFlag|clearColor1|clearColor2|clearDepthValue|clearStencilValue]:
		"""getBackgroundParameters() -> [displayGradient, clearColorFlag, clearDepthFlag, clearStencilFlag, clearColor1, clearColor2, clearDepthValue, clearStencilValue]

		Get parameters related to how the background is cleared"""
	def getHwFogParameters(self)->list[enabled|mode|start|end|density|color]:
		"""getHwFogParameters() -> [enabled, mode, start, end, density, color]

		Get all the hardware fog parameters.

		Hardware fog parameters include:

		- hardware fog enabled
		- hardware fog mode: Linear, Exponential, Exponential squared.
		  The possible values are:
		     MFrameContext::kFogLinear : Linear fog
		     MFrameContext::kFogExp : Exponential fog
		     MFrameContext::kFogExp2 : Exponential squared fog
		- hardware fog start: The near distance used in the linear fog.
		- hardware fog end: The far distance used in the linear fog.
		- hardware fog density: The density of the exponential fog.
		- hardware fog color: (r, g, b, a)."""
	def getRenderOverrideInformation(self)->list[str]:
		"""getRenderOverrideInformation() -> [overrideName]

		Get information about any render override"""
class MGeometry:
	"""Class for working with geometric structures used to draw objects."""
	kInvalidType:int=0
	kFloat:int=1
	kDouble:int=2
	kChar:int=3
	kUnsignedChar:int=4
	kInt16:int=5
	kUnsignedInt16:int=6
	kInt32:int=7
	kUnsignedInt32:int=8
	kInvalidSemantic:int=0
	kPosition:int=1
	kNormal:int=2
	kTexture:int=3
	kColor:int=4
	kTangent:int=5
	kBitangent:int=6
	kTangentWithSign:int=7
	kInvalidPrimitive:int=0
	kPoints:int=1
	kLines:int=2
	kLineStrip:int=3
	kTriangles:int=4
	kTriangleStrip:int=5
	kAdjacentTriangles:int=6
	kAdjacentTriangleStrip:int=7
	kAdjacentLines:int=8
	kAdjacentLineStrip:int=9
	kPatch:int=10
	kWireframe:int=1
	kShaded:int=2
	kTextured:int=4
	kBoundingBox:int=8
	kSelectionOnly:int=16
	kSelectionHighlighting:int=32
	kAll:int=15
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def addIndexBuffer(self,MIndexBuffer:Any)->bool:
		"""addIndexBuffer(MIndexBuffer) -> bool

		Buffers cannot be added to the same object twice.Adds a index buffer to this MGeometry object.
		The buffer can only be added to this object once but may be added to others."""
	def addVertexBuffer(self,MVertexBuffer:Any)->bool:
		"""addVertexBuffer(MVertexBuffer) -> bool

		Adds a vertex buffer to this MGeometry object.
		The buffer can only be added to this object once but may be added to others."""
	def createIndexBuffer(self,int:int)->MIndexBuffer:
		"""createIndexBuffer(int) -> MIndexBuffer

		Creates a index buffer which is bound to this MGeometry object and cannot be used with any other.
		The buffer is automatically added to the MGeometry object so there is no need to call addIndexBuffer().
		See MGeometry.dataTypeString() for a list of valid data types."""
	def createVertexBuffer(self,MVertexBufferDescriptor:Any)->MVertexBuffer:
		"""createVertexBuffer(MVertexBufferDescriptor) -> MVertexBuffer

		Creates a vertex buffer which is bound to this MGeometry object and cannot be used with any other.
		The buffer is automatically added to the MGeometry object so there is no need to call addVertexBuffer()."""
	@staticmethod
	def dataTypeString(int:int)->str:
		"""dataTypeString(int) -> string

		Get the string name (e.g. 'Unsigned Char') for the following data type values:

		  kInvalidType     Invalid element type (default value)
		  kFloat           IEEE single precision floating point
		  kDouble          IEEE double precision floating point
		  kChar            Signed char
		  kUnsignedChar    Unsigned char
		  kInt16           Signed 16-bit integer
		  kUnsignedInt16   Unsigned 16-bit integer
		  kInt32           Signed 32-bit integer
		  kUnsignedInt32   Unsigned 32-bit integer"""
	def deleteIndexBuffer(self,int:int)->bool:
		"""deleteIndexBuffer(int) -> bool

		Remove a index buffer from this object.
		If the buffer was bound to this object (see createIndexBuffer()) then it will become inactive and any attempt to call any of its methods will result in an exception."""
	def deleteVertexBuffer(self,int:int)->bool:
		"""deleteVertexBuffer(int) -> bool

		Remove a vertex buffer from this object.
		If the buffer was bound to this object (see createVertexBuffer()) then it will become inactive and any attempt to call any of its methods will result in an exception."""
	@staticmethod
	def drawModeString(int:int)->str:
		"""drawModeString(int) -> string

		Get the string name (e.g. 'Wireframe, Shaded, Textured') for a combination of the following draw mode values:

		  kWireframe      Draw in wireframe mode
		  kShaded         Draw in shaded mode
		  kTextured       Draw in textured mode
		  kBoundingBox    Draw in bounding box mode
		  kSelectionOnly  Draw only in selection mode

		The draw mode value kAll is a combination of the following modes: kWireframe, kShaded, kTextured, and kBoundingBox"""
	def indexBuffer(self,int:int)->MIndexBuffer:
		"""indexBuffer(int) -> MIndexBuffer

		Get the index buffer stored at the given index."""
	def indexBufferCount(self)->int:
		"""indexBufferCount() -> int

		Get the number of index buffers contained in this MGeometry object."""
	@staticmethod
	def primitiveString(int:int)->str:
		"""primitiveString(int) -> string

		Get the string name (e.g. 'Triangles') for the following primitive values:

		  kInvalidPrimitive        Default value is not valid
		  kPoints                  List of points
		  kLines                   List of lines
		  kLineStrip               A line strip
		  kTriangles               List of triangles
		  kTriangleStrip           A triangle strip
		  kAdjacentTriangles       A list of triangle with adjacency
		  kAdjacentTriangleStrip   A triangle strip with adjacency
		  kAdjacentLines           A list of lines with adjacency
		  kAdjacentLineStrip       A line strip with adjacency
		  kPatch                   A patch"""
	@staticmethod
	def semanticString(int:int)->str:
		"""semanticString(int) -> string

		Get the string name (e.g. 'Color') for the following semantic values:

		  kInvalidSemantic    Invalid data type (default value)
		  kPosition           Position vector
		  kNormal             Normal vector
		  kTexture            Texture coordinate tuple
		  kColor              Color tuple
		  kTangent            Tangent vector
		  kBitangent          Bi-normal vector
		  kTangentWithSign    Tangent vector with winding order sign"""
	def vertexBuffer(self,int:int)->MVertexBuffer:
		"""vertexBuffer(int) -> MVertexBuffer

		Get the vertex buffer stored at the given index."""
	def vertexBufferCount(self)->int:
		"""vertexBufferCount() -> int

		Get the number of vertex buffers contained in this MGeometry object."""
class MGeometryExtractor:
	"""Class for extracting renderable geometry.

	__init__(MGeometryRequirements, MDagObject, MPolyGeomOptions)
	    Initializes a new MGeometryExtractor attached to a MDagObject mesh shape.

	__init__(MGeometryRequirements, MObject   , MPolyGeomOptions)
	    Initializes a new MGeometryExtractor attached to a mesh data MObject
	    of type MFn::kMeshData or MFn::kMeshGeom.

	"""
	kPolyGeom_Normal:int=0
	kPolyGeom_NotSharing:int=1
	kPolyGeom_BaseMesh:int=2
	@overload
	def __init__(self,MGeometryRequirements:Any,MDagObject:Any,MPolyGeomOptions:Any)->None:
		"""Initializes a new MGeometryExtractor attached to a MDagObject mesh shape."""
	@overload
	def __init__(self,MGeometryRequirements:Any,MObject:Any,MPolyGeomOptions:Any)->None:
		"""Initializes a new MGeometryExtractor attached to a mesh data MObject
		    of type MFn::kMeshData or MFn::kMeshGeom."""
	@staticmethod
	def minimumBufferSize(primitiveCount:int,primitive:int,primitiveStride:int=0)->int:
		"""minimumBufferSize(primitiveCount, primitive, primitiveStride=0) -> int

		Get the minimum buffer size required by populateIndexBuffer().

		* primitiveCount (int) - The number of primitives.
		* primitive (int) - The primitive type. See MGeometry.primitiveString() for list of primitive types.
		* primitiveStride (int) - The number of control points in a patch when the type is kPatch."""
	def populateIndexBuffer(self,data:buffer,primitiveCount:int,indexDesc:MIndexBufferDescriptor)->Self:
		"""populateIndexBuffer(data, primitiveCount, indexDesc) -> self

		Fill a buffer with geometry indexing data.
		This method will use the information provided in the MIndexBufferDescriptor argument to populate the buffer with the desired indexing data.  The descriptor will describe the surface index type, the primitive type, and the data type.  The populateIndexBuffer method will generate a buffer that matches the request.
		The length of the buffer should be at least the as big as the value returned by minimumBufferSize().

		* data (buffer) - The buffer you want filled.
		* primitiveCount (int) - The number of primitives you expect to be filled in the buffer.
		* indexDesc (MIndexBufferDescriptor) - The description of the buffer you are requesting."""
	def populateVertexBuffer(self,data:buffer,vertexCount:int,bufferDesc:MVertexBufferDescriptor)->Self:
		"""populateVertexBuffer(data, vertexCount, bufferDesc) -> self

		Fill a buffer with vertex data.
		This method will use the information provided in the MVertexBufferDescriptor argument to populate the buffer with the desired vertex data.  The descriptor will describe the buffer's name, semantic, and data type.
		The populateVertexBuffer method will supply a buffer that matches the request.  The length of the buffer should be at least (vertexCount * bufferDesc.stride()).
		Values for normals, tangents and bitangents are all normalized.

		* data (buffer) - The buffer you want filled.
		* vertexCount (int) - The vertex count you expect to be filled in the buffer.
		* bufferDesc (MVertexBufferDescriptor) - The description of the buffer you are requesting."""
	def primitiveCount(self,indexDesc:MIndexBufferDescriptor)->int:
		"""primitiveCount(indexDesc) -> int

		Returns the number of primitives (triangles, lines, points, etc.) that will be produced for the given indexing requirements.
		Call this method before calling populateIndexBuffer to determine the minimum size the buffer passed into populateIndexBuffer needs to be.

		* indexDesc (MIndexBufferDescriptor) - The description of the index buffer you request the count for."""
	def vertexCount(self)->int:
		"""vertexCount() -> int

		Returns the number of vertices that will be produced for the vertex requirement.
		Call this method before calling populateVertexBuffer to determine the minimum size the buffer passed into populateVertexBuffer needs to be."""
class MGeometryIndexMapping:
	"""A mapping of geometry index."""
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def component(self,int:int)->om.MObject:
		"""component(int) -> MObject

		Get the component of a geometry."""
	def dagPath(self,int:int)->om.MDagPath:
		"""dagPath(int) -> MDagPath

		Get the MDagPath of a geometry."""
	def geometryCount(self)->int:
		"""geometryCount() -> int

		Get the number of geometry described by the mapping."""
	def indexLength(self,int:int)->int:
		"""indexLength(int) -> int

		Get the index length of a geometry.
		The index length represents the length of the geometry index data in the index buffer of the consolidated render item."""
	def indexStart(self,int:int)->int:
		"""indexStart(int) -> int

		Get the index start of a geometry.
		The index start represents the offset of the geometry index data in the index buffer of the consolidated render item."""
class MGeometryRequirements:
	"""Geometry requirements."""
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def addIndexingRequirement(self,MIndexBufferDescriptor:Any)->Self:
		"""addIndexingRequirement(MIndexBufferDescriptor) -> self

		Add a new indexing requirement to the list of indexing requirements."""
	def addVertexRequirement(self,MVertexBufferDescriptor:Any)->Self:
		"""addVertexRequirement(MVertexBufferDescriptor) -> self

		Add a new vertex requirement to the list of vertex requirements."""
	def indexingRequirements(self)->MIndexBufferDescriptorList:
		"""indexingRequirements() -> MIndexBufferDescriptorList

		Get a list of descriptors that specify the geometry indexing requirements of an object."""
	def vertexRequirements(self)->MVertexBufferDescriptorList:
		"""vertexRequirements() -> MVertexBufferDescriptorList

		Get a list of descriptors that specify the vertex geometry requirements of this object."""
class MGeometryUtilities:
	"""Utilities for Viewport 2.0"""
	kDefaultSphere:int=0
	kDefaultPlane:int=1
	kDefaultCube:int=2
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
	@staticmethod
	def acquireReferenceGeometry(shape:int,requirements:MGeometryRequirements)->MGeometry:
		"""acquireReferenceGeometry(shape, requirements) -> MGeometry

		Acquire reference geometry with required buffers.

		The user is responsible for releasing the geometry when it is no longer needed, by calling MGeometryUtilities::releaseReferenceGeometry().


		* shape (int) - The shape of the requested geometry.
		* requirements (MGeometryRequirements) - The list of required index and vertex buffers.

		Valid geometry shapes:
		  kDefaultSphere   Sphere with radius 1, centered at 0,0,0.
		  kDefaultPlane    Plane with width and height of 1, centered at 0,0,0. Assuming Y-Up orientation: width = x-axis, and height = y-axis.
		  kDefaultCube     Cube with width, height and depth of 1, centered at 0,0,0."""
	@staticmethod
	def displayStatus(path:om.MDagPath)->DisplayStatus:
		"""displayStatus(path) -> DisplayStatus

		Returns the display status of the given DAG path. Note that the last selected object will have status kLead
		instead of kActive and if only one object is selected the status will be kLead.

		* path (MDagPath) - The DAG path to get."""
	@staticmethod
	def releaseReferenceGeometry(geometry:MGeometry)->None:
		"""releaseReferenceGeometry(geometry) -> None

		Release a generated reference geometry.

		* geometry (MGeometry) - The geometry to delete."""
	@staticmethod
	def wireframeColor(path:om.MDagPath)->om.MColor:
		"""wireframeColor(path) -> MColor

		Returns the wireframe color used in Viewport 2.0 for the given DAG path.

		* path (MDagPath) - The DAG path to get wireframe color."""
class MHUDRender(MRenderOperation):
	"""Class which defines rendering the 2D heads-up-display."""
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def addUIDrawables(self,drawManager2D:MUIDrawManager,frameContext:MFrameContext)->Self:
		"""addUIDrawables(drawManager2D, frameContext) -> self

		Provides access to the 2D version of MUIDrawManager, which can be used to queue up operations to draw simple UI shapes like lines, circles, text, etc.

		This method will only be called when hasUIDrawables() is overridden to return true.

		* drawManager2D (MUIDrawManager) - A UI draw manager which can be used to draw simple 2D geometry, including text. When passing coordinates to the draw manager's methods, only X and Y have meaning. The origin (0, 0) is in the lower-left corner of the view.
		* frameContext (MFrameContext) - Frame level context information."""
	def hasUIDrawables(self)->bool:
		"""hasUIDrawables() -> bool

		Query whether addUIDrawables() should be called or not."""
	def name(self)->str:
		"""name() -> string

		Returns the unique name for a hud render operation.
		Note that all HUD operations share the same name since they need not be distinguished from one another."""
class MIndexBuffer:
	"""Index buffer for use with MGeometry."""
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def acquire(self,size:int,writeOnly:bool)->int:
		"""acquire(size, writeOnly) -> long

		Get a pointer to memory for the buffer.

		* size (int) - The size of the buffer to acquire.
		* writeOnly (bool) - Specified if the returned memory should be uninitialized or filled with actual buffer content.
		                     When the current buffer content is not needed, it is preferable to set the writeOnly flag to true for better performance."""
	def commit(self,long:Any)->Self:
		"""commit(long) -> self

		Commit the data stored in the memory given by acquire() to the buffer.
		If this method is not called, the acquired buffer will not be used in drawing.
		The pointer must be the same pointer returned from acquire()."""
	def dataType(self)->int:
		"""dataType() -> int

		Get the data type of the buffer.
		See MGeometry.dataTypeString() for a list of valid data types."""
	def hasCustomResourceHandle(self)->bool:
		"""hasCustomResourceHandle() -> bool

		Returns true if this index buffer is using a custom resource handle set
		by the plugin using MIndexBuffer.setResourceHandle(long, int)."""
	def lockResourceHandle(self)->Self:
		"""lockResourceHandle() -> self

		Lock the resource handle. The pointer returned from resourceHandle() is
		guaranteed to exist between lockResourceHandle() and unlockResourceHandle().

		MIndexBuffer may store data in system memory, GPU memory or both. Direct
		access to the GPU representation of the data is possible through the
		buffer's resourceHandle(). If the GPU representation of the data is to be
		directly modified using an external graphics or compute API, then
		lockResourceHandle() must be called on the MIndexBuffer once, before any
		modifications to the buffer are made.

		While a resource handle is locked, any external modifications to the GPU
		buffer will be recognized by Maya.

		While a resource handle is locked, consolidated world will take longer to
		consolidate the corresponding object. After unlocking a resource handle,
		consolidated world will take longer to consolidate the corresponding object
		one more time, the first time the unlocked resource handle is consolidated.

		Calling lockResourceHandle() and unlockResourceHandle() on a custom resource
		handle has no effect.

		Reallocating or deleting the GPU representation of the data between
		lockResourceHandle() and unlockResourceHandle() will result in undefined
		behavior. acquire(), commit() and update() may reallocate the GPU representation.
		unload() may delete the GPU representation.

		map() and unmap() will work if they are called between lockResourceHandle()
		and unlockResourceHandle(). They operate on the GPU representation."""
	def map(self)->int:
		"""map() -> long

		Get a read-only pointer to the existing content of the buffer.
		Writing new content in this memory block is not supported and can lead to unexpected behavior."""
	def resourceHandle(self)->int:
		"""resourceHandle() -> long

		Returns a long containing a C++ 'float' pointer which points to the graphics device dependent handle to the vertex indexing data."""
	def setResourceHandle(self,long:Any,int:int)->Any:
		"""setResourceHandle(long, int) -> selfset the graphics-device-dependent hardware buffer resource handle."""
	def size(self)->int:
		"""size() -> int

		Get the size of the buffer in units of dataType(). Returns 0 if unallocated."""
	def unload(self)->Self:
		"""unload() -> self

		If the buffer is resident in GPU memory, calling this method will move it to system memory and free the GPU memory."""
	def unlockResourceHandle(self)->Self:
		"""unlockResourceHandle() -> self

		Unlock the resource handle. The pointer returned from resourceHandle is not
		guaranteed to exist any more.
		See lockResourceHandle() for more details."""
	def unmap(self)->Self:
		"""unmap() -> self

		Release the data exposed by map(). If this method is not called, the buffer will not be recycled."""
	def update(self,buffer:int,destOffset:int,numIndices:int,truncateIfSmaller:bool)->Self:
		"""update(buffer, destOffset, numIndices, truncateIfSmaller) -> self

		Set a portion (or all) of the contents of the MIndexBuffer using the data in the provided software buffer.
		The internal hardware buffer will be allocated or reallocated to fit if required, according to the vertex size from the descriptor.

		* buffer (long) - The input data buffer, starting with the first vertex to copy.
		* destOffset (int) - The offset (in indices) from the beginning of the buffer to start writing to.
		* numIndices (int) - The number of indices to copy.
		* truncateIfSmaller (bool) - If true and offset+numVerts is less than the pre-existing size of the buffer,
		                             then the buffer contents will be truncated to the new size. Truncating the buffer size
		                             will not cause a reallocation and will not lose data before the destOffset."""
class MIndexBufferDescriptor:
	"""Describes an indexing scheme."""
	@property
	def name(self)->Any:
		"""The name used to describe the type when 'indexType' is set to kCustom."""
	@name.setter
	def name(self,value:Any)->None:...
	@property
	def indexType(self)->Any:
		"""The indexing type describing what the buffer is used for:
		  kVertexPoint
		  kEdgeLine
		  kTriangleEdge
		  kTriangle
		  kFaceCenter
		  kEditPoint
		  kControlVertex
		  kHullEdgeLine
		  kHullTriangle
		  kHullFaceCenter
		  kHullEdgeCenter
		  kHullUV
		  kSubDivEdge
		  kTangent
		  kCustom"""
	@indexType.setter
	def indexType(self,value:Any)->None:...
	@property
	def primitive(self)->Any:
		"""The primitive describing the input layout for each drawable.
		See MGeometry.primitiveString() for a list of valid primitive types."""
	@primitive.setter
	def primitive(self,value:Any)->None:...
	@property
	def primitiveStride(self)->Any:
		"""The number of control points used for patch primitives.
		Only meaningful when 'primitive' is set to kPatch."""
	@primitiveStride.setter
	def primitiveStride(self,value:Any)->None:...
	@property
	def component(self)->Any:
		"""The component associated with the index buffer."""
	@component.setter
	def component(self,value:Any)->None:...
	@property
	def dataType(self)->Any:
		"""The type of data expected to be in the index buffer.
		See MGeometry.dataTypeString() for a list of valid data types."""
	@dataType.setter
	def dataType(self,value:Any)->None:...
	kVertexPoint:int=0
	kEdgeLine:int=1
	kTriangleEdge:int=2
	kTriangle:int=3
	kFaceCenter:int=4
	kEditPoint:int=5
	kControlVertex:int=6
	kHullEdgeLine:int=7
	kHullTriangle:int=8
	kHullFaceCenter:int=9
	kHullEdgeCenter:int=10
	kHullUV:int=11
	kSubDivEdge:int=12
	kTangent:int=13
	kCustom:int=14
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
class MIndexBufferDescriptorList:
	"""A list of MIndexBufferDescriptor objects."""
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def __len__(self)->int:
		"""Return len(self)."""
	def __getitem__(self,index:int)->Any:
		"""Return self[key]."""
	def append(self,MIndexBufferDescriptor:Any)->bool:
		"""append(MIndexBufferDescriptor) -> bool

		Add a descriptor to the list. Creates and stores a copy which is owned by the list."""
	def clear(self)->Self:
		"""clear() -> self

		Clear the list."""
	def remove(self,index:int)->bool:
		"""remove(index) -> bool

		Remove a descriptor from the list and delete it."""
class MInitContext:
	"""Initialization context used by advanced initalization method."""
	@property
	def shader(self)->Any:
		"""The Maya shading node this override is used for"""
	@shader.setter
	def shader(self,value:Any)->None:...
	@property
	def dagPath(self)->Any:
		"""A path to the instance of the Maya DAG object for which the shader is being initialized"""
	@dagPath.setter
	def dagPath(self,value:Any)->None:...
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
class MInitFeedback:
	"""Data to pass back to Maya after initialization."""
	@property
	def customData(self)->Any:
		"""Optional user data to be associated with the render item for the shader assignment"""
	@customData.setter
	def customData(self,value:Any)->None:...
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
class MIntersection:
	"""This class gives a description of an intersection when a selection hit occurs."""
	@property
	def barycentricCoordinates(self)->Any:
		"""Get the barycentric coordinates (a, b). Only valid for triangles.
		Follows Tomas Moller & Ben Trumbore, jgt 97 "Fast minimum storage ray/triangle intersection" which means that a point, T(a,b), on a triangle is given by:
		   T(a,b) = (1-a-b)V0 + aV1 + bV2
		where V0, V1, and V2 are the triangle vertices."""
	@barycentricCoordinates.setter
	def barycentricCoordinates(self,value:Any)->None:...
	@property
	def edgeInterpolantValue(self)->Any:
		"""The edge interpolant value. Only valid for edges.
		It corresponds to the intersection position on the edge, from 0 to 1 starting at V0 going to V1."""
	@edgeInterpolantValue.setter
	def edgeInterpolantValue(self,value:Any)->None:...
	@property
	def index(self)->Any:
		"""The index of the hit vertex, edge or triangle.
		It is the position in the index buffer of the render item geometry when provided, and the position in the vertex buffer if not."""
	@index.setter
	def index(self,value:Any)->None:...
	@property
	def intersectionPoint(self)->Any:
		"""The intersection point."""
	@intersectionPoint.setter
	def intersectionPoint(self,value:Any)->None:...
	@property
	def instanceID(self)->Any:
		"""The draw instance ID of the render item. Only valid for instanced render items."""
	@instanceID.setter
	def instanceID(self,value:Any)->None:...
	@property
	def selectionLevel(self)->Any:
		"""The selection level of the intersection.
		See MSelectionContext::selectionLevel for list of valid level values."""
	@selectionLevel.setter
	def selectionLevel(self,value:Any)->None:...
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
class MLightParameterInformation:
	"""Class for providing lighting information that may be used with Viewport 2.0."""
	kInvalid:int=0
	kBoolean:int=1
	kInteger:int=2
	kFloat:int=3
	kFloat2:int=4
	kFloat3:int=5
	kFloat4:int=6
	kFloat4x4Row:int=7
	kFloat4x4Col:int=8
	kTexture2:int=9
	kSampler:int=10
	kTextureCube:int=11
	kNoSemantic:int=0
	kLightEnabled:int=1
	kWorldPosition:int=2
	kWorldDirection:int=3
	kIntensity:int=4
	kColor:int=5
	kEmitsDiffuse:int=6
	kEmitsSpecular:int=7
	kDecayRate:int=8
	kDropoff:int=9
	kCosConeAngle:int=10
	kStartShadowParameters:int=11
	kIrradianceIn:int=11
	kShadowMap:int=12
	kShadowSamp:int=13
	kShadowBias:int=14
	kShadowMapSize:int=15
	kShadowViewProj:int=16
	kShadowColor:int=17
	kGlobalShadowOn:int=18
	kShadowOn:int=19
	kShadowDirty:int=20
	kDepthRange:int=21
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def parameterList(self)->list[str]:
		"""parameterList() -> list of string

		Get the names of all light parameters that are accessible."""
	def parameterType(self,string:Any)->int:
		"""parameterType(string) -> int

		Get the type of the named parameter, returns kInvalid if parameter is not found.

		  MDrawContext.kInvalid        Invalid element type (default value)
		  MDrawContext.kBoolean        Boolean
		  MDrawContext.kInteger        Signed 32-bit integer
		  MDrawContext.kFloat          IEEE single precision floating point
		  MDrawContext.kFloat2         IEEE single precision floating point (x2)
		  MDrawContext.kFloat3         IEEE single precision floating point (x3)
		  MDrawContext.kFloat4         IEEE single precision floating point (x4)
		  MDrawContext.kFloat4x4Row    IEEE single precision floating point row-major matrix (4x4)
		  MDrawContext.kFloat4x4Col    IEEE single precision floating point column-major matrix (4x4)
		  MDrawContext.kTexture2       2D texture
		  MDrawContext.kSampler        Sampler"""
	def parameterSemantic(self,string:Any)->int:
		"""parameterSemantic(string) -> int

		Get the stock semantic for a named parameter:
		  MDrawContext.kNoSemantic       No semantic
		  MDrawContext.kLightEnabled     Light is enabled
		  MDrawContext.kWorldPosition    World space position
		  MDrawContext.kWorldDirection   World space direction
		  MDrawContext.kIntensity        Intensity
		  MDrawContext.kColor            Color
		  MDrawContext.kEmitsDiffuse     Emits diffuse lighting
		  MDrawContext.kEmitsSpecular    Emits specular lighting
		  MDrawContext.kDecayRate        Decay rate
		  MDrawContext.kDropoff          Dropoff
		  MDrawContext.kCosConeAngle     Cosine of the cone angle
		  MDrawContext.kIrradianceIn     Incoming irradiance
		  MDrawContext.kShadowMap        Shadow map
		  MDrawContext.kShadowSamp       Shadow map sampler
		  MDrawContext.kShadowBias       Shadow map bias
		  MDrawContext.kShadowMapSize    Shadow map size
		  MDrawContext.kShadowViewProj   Shadow map view projection matrix
		  MDrawContext.kShadowColor      Shadow color
		  MDrawContext.kGlobalShadowOn   Global toggle for whether shadows are enabled or not
		  MDrawContext.kShadowOn         Local toggle per light for whether shadows are enabled or not
		  MDrawContext.kShadowDirty      Indicates if the contents of the shadow map are out-of-date or uninitialized"""
	def parameterNames(self,int:int)->list[str]:
		"""parameterNames(int) -> list of string

		Get the name of all parameters on the light which are tagged with the stock semantic."""
	def arrayParameterCount(self,string:Any)->int:
		"""arrayParameterCount(string) -> int

		Return the array size of a parameter. If the parameter is not an array then a value of 0 is returned."""
	@overload
	def getParameter(self,int:int)->om.MIntArray:
		"""getParameter(int) -> MIntArraygetParameter(int) -> MFloatArraygetParameter(int) -> MMatrixgetParameter(int) -> MSamplerStateDescgetParameter(int) -> MTexturegetParameter(string) -> MIntArraygetParameter(string) -> MFloatArraygetParameter(string) -> MMatrixgetParameter(string) -> MSamplerStateDescgetParameter(string) -> MTexture

		Get parameter value by name or by semantic.
		If more than one parameter matches the semantic, the value of the first matching parameter found will be returned."""
	@overload
	def getParameter(self,int:int)->om.MFloatArray:
		"""getParameter(int) -> MIntArraygetParameter(int) -> MFloatArraygetParameter(int) -> MMatrixgetParameter(int) -> MSamplerStateDescgetParameter(int) -> MTexturegetParameter(string) -> MIntArraygetParameter(string) -> MFloatArraygetParameter(string) -> MMatrixgetParameter(string) -> MSamplerStateDescgetParameter(string) -> MTexture

		Get parameter value by name or by semantic.
		If more than one parameter matches the semantic, the value of the first matching parameter found will be returned."""
	@overload
	def getParameter(self,int:int)->om.MMatrix:
		"""getParameter(int) -> MIntArraygetParameter(int) -> MFloatArraygetParameter(int) -> MMatrixgetParameter(int) -> MSamplerStateDescgetParameter(int) -> MTexturegetParameter(string) -> MIntArraygetParameter(string) -> MFloatArraygetParameter(string) -> MMatrixgetParameter(string) -> MSamplerStateDescgetParameter(string) -> MTexture

		Get parameter value by name or by semantic.
		If more than one parameter matches the semantic, the value of the first matching parameter found will be returned."""
	@overload
	def getParameter(self,int:int)->MSamplerStateDesc:
		"""getParameter(int) -> MIntArraygetParameter(int) -> MFloatArraygetParameter(int) -> MMatrixgetParameter(int) -> MSamplerStateDescgetParameter(int) -> MTexturegetParameter(string) -> MIntArraygetParameter(string) -> MFloatArraygetParameter(string) -> MMatrixgetParameter(string) -> MSamplerStateDescgetParameter(string) -> MTexture

		Get parameter value by name or by semantic.
		If more than one parameter matches the semantic, the value of the first matching parameter found will be returned."""
	@overload
	def getParameter(self,int:int)->MTexture:
		"""getParameter(int) -> MIntArraygetParameter(int) -> MFloatArraygetParameter(int) -> MMatrixgetParameter(int) -> MSamplerStateDescgetParameter(int) -> MTexturegetParameter(string) -> MIntArraygetParameter(string) -> MFloatArraygetParameter(string) -> MMatrixgetParameter(string) -> MSamplerStateDescgetParameter(string) -> MTexture

		Get parameter value by name or by semantic.
		If more than one parameter matches the semantic, the value of the first matching parameter found will be returned."""
	@overload
	def getParameter(self,string:Any)->om.MIntArray:
		"""getParameter(int) -> MIntArraygetParameter(int) -> MFloatArraygetParameter(int) -> MMatrixgetParameter(int) -> MSamplerStateDescgetParameter(int) -> MTexturegetParameter(string) -> MIntArraygetParameter(string) -> MFloatArraygetParameter(string) -> MMatrixgetParameter(string) -> MSamplerStateDescgetParameter(string) -> MTexture

		Get parameter value by name or by semantic.
		If more than one parameter matches the semantic, the value of the first matching parameter found will be returned."""
	@overload
	def getParameter(self,string:Any)->om.MFloatArray:
		"""getParameter(int) -> MIntArraygetParameter(int) -> MFloatArraygetParameter(int) -> MMatrixgetParameter(int) -> MSamplerStateDescgetParameter(int) -> MTexturegetParameter(string) -> MIntArraygetParameter(string) -> MFloatArraygetParameter(string) -> MMatrixgetParameter(string) -> MSamplerStateDescgetParameter(string) -> MTexture

		Get parameter value by name or by semantic.
		If more than one parameter matches the semantic, the value of the first matching parameter found will be returned."""
	@overload
	def getParameter(self,string:Any)->om.MMatrix:
		"""getParameter(int) -> MIntArraygetParameter(int) -> MFloatArraygetParameter(int) -> MMatrixgetParameter(int) -> MSamplerStateDescgetParameter(int) -> MTexturegetParameter(string) -> MIntArraygetParameter(string) -> MFloatArraygetParameter(string) -> MMatrixgetParameter(string) -> MSamplerStateDescgetParameter(string) -> MTexture

		Get parameter value by name or by semantic.
		If more than one parameter matches the semantic, the value of the first matching parameter found will be returned."""
	@overload
	def getParameter(self,string:Any)->MSamplerStateDesc:
		"""getParameter(int) -> MIntArraygetParameter(int) -> MFloatArraygetParameter(int) -> MMatrixgetParameter(int) -> MSamplerStateDescgetParameter(int) -> MTexturegetParameter(string) -> MIntArraygetParameter(string) -> MFloatArraygetParameter(string) -> MMatrixgetParameter(string) -> MSamplerStateDescgetParameter(string) -> MTexture

		Get parameter value by name or by semantic.
		If more than one parameter matches the semantic, the value of the first matching parameter found will be returned."""
	@overload
	def getParameter(self,string:Any)->MTexture:
		"""getParameter(int) -> MIntArraygetParameter(int) -> MFloatArraygetParameter(int) -> MMatrixgetParameter(int) -> MSamplerStateDescgetParameter(int) -> MTexturegetParameter(string) -> MIntArraygetParameter(string) -> MFloatArraygetParameter(string) -> MMatrixgetParameter(string) -> MSamplerStateDescgetParameter(string) -> MTexture

		Get parameter value by name or by semantic.
		If more than one parameter matches the semantic, the value of the first matching parameter found will be returned."""
	@overload
	def getParameterTextureHandle(self,int:int)->int:
		"""getParameterTextureHandle(int) -> longgetParameterTextureHandle(string) -> long

		Get a resource handle for a texture parameter by name or by semantic.
		Returns a long containing a C++ 'void' pointer which points to the resource handle."""
	@overload
	def getParameterTextureHandle(self,string:Any)->int:
		"""getParameterTextureHandle(int) -> longgetParameterTextureHandle(string) -> long

		Get a resource handle for a texture parameter by name or by semantic.
		Returns a long containing a C++ 'void' pointer which points to the resource handle."""
	def lightType(self)->str:
		"""lightType() -> string

		Get the classification of the light node."""
	def lightPath(self)->om.MDagPath:
		"""lightPath() -> MDagPath

		Returns the DagPath to the scene light. Will return an unitialized DagPath for default lights."""
class MPassContext:
	"""Class to allow access to pass context information."""
	kColorPassSemantic:str='colorPass'
	kShadowPassSemantic:str='shadowPass'
	kDepthPassSemantic:str='depthPass'
	kNormalDepthPassSemantic:str='normalDepthPass'
	kOpaqueGeometrySemantic:str='opaqueGeometry'
	kPreUIGeometrySemantic:str='preUIGeometry'
	kPostUIGeometrySemantic:str='postUIGeometry'
	kUIGeometrySemantic:str='uiGeometry'
	kOpaqueUISemantic:str='opaqueUIList'
	kTransparentUISemantic:str='transparentUIList'
	kXrayUISemantic:str='xrayUIList'
	kTransparentGeometrySemantic:str='transparentGeometry'
	kCullBackSemantic:str='cullBack'
	kCullFrontSemantic:str='cullFront'
	kMaterialOverrideSemantic:str='materialOverride'
	kTransparentPeelSemantic:str='transparentPeel'
	kTransparentPeelAndAvgSemantic:str='transparentPeelAndAvg'
	kTransparentWeightedAvgSemantic:str='transparentWeightedAvg'
	kUserPassSemantic:str='userPass'
	kBeginRenderSemantic:str='beginRender'
	kBeginSceneRenderSemantic:str='beginSceneRender'
	kEndSceneRenderSemantic:str='endSceneRender'
	kEndRenderSemantic:str='endRender'
	kSelectionPassSemantic:str='selectionPass'
	kDOFPassSemantic:str='dofPass'
	kMotionVectorPassSemantic:str='motionVectorPass'
	kPEPatternPassSemantic:str='PEPatternPass'
	kNonPEPatternPassSemantic:str='nonPEPatternPass'
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def passIdentifier(self)->str:
		"""passIdentifier() -> string

		Return the identifier for the pass context."""
	def passSemantics(self)->list[str]:
		"""passSemantics() -> list of string

		Return an array of semantics for the pass context."""
	def hasShaderOverride(self)->bool:
		"""hasShaderOverride() -> bool

		Return if there is a shader instance override set for the current pass."""
	def shaderOverrideInstance(self)->MShaderInstance:
		"""shaderOverrideInstance() -> MShaderInstance

		Return the shader instance override set for the current pass.

		When the returned new shader instance is no longer needed, MShaderManager::releaseShader() should be called to notify the shader manager that the caller is done with the shader."""
class MPresentTarget(MRenderOperation):
	"""Class which defines the operation of presenting a target for final output."""
	kCenterBuffer:int=0
	kLeftBuffer:int=1
	kRightBuffer:int=2
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def presentDepth(self)->bool:
		"""presentDepth() -> bool

		Query whether the present operation will display depth values."""
	def setPresentDepth(self,bool:bool)->Self:
		"""setPresentDepth(bool) -> self

		Set whether the operation will present depth values."""
	def setTargetBackBuffer(self,int:int)->Self:
		"""setTargetBackBuffer(int) -> self

		Set the desired back-buffer to use on the output target.
		see MPresentTarget.targetBackBuffer() description for the list of available back-buffers."""
	def targetBackBuffer(self)->int:
		"""targetBackBuffer() -> int

		Query the desired back-buffer to use on the output target.

		  MPresentTarget.kCenterBuffer   Default or 'center' buffer
		  MPresentTarget.kLeftBuffer     Left back-buffer
		  MPresentTarget.kRightBuffer    Right back-buffer"""
class MPxComponentConverter:
	"""Base class for user defined component converter."""
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def addIntersection(self,intersection:MIntersection)->Self:
		"""addIntersection(intersection) -> self

		Maya calls this function for every selection hit on the render item.
		The intersection gives information on the component that was hit.

		* intersection (MIntersection) - The selection intersection."""
	def component(self)->om.MObject:
		"""component() -> MObject

		Once all of the geometry hits have been passed to the converter through calls to addIntersection(), Maya will call this method to retrieve the components corresponding to those hits.

		Returns the component selection."""
	def initialize(self,renderItem:MRenderItem)->Self:
		"""initialize(renderItem) -> self

		Maya calls this function to allow the converter to initialize itself for the selection on the given render item.

		* renderItem (MRenderItem) - The render item."""
	def selectionMask(self)->om.MSelectionMask:
		"""selectionMask() -> MSelectionMask

		Maya calls this function to allow the converter to specify the type of components it can handle..

		Returns the selection mask."""
class MPxDrawOverride:
	"""Base class for user defined drawing of nodes.


	Note the third parameter of the constructor is optional and defaults to true:
	MPxDrawOverride(obj, callback, isAlwaysDirty = True)"""
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def addUIDrawables(self,objPath:om.MDagPath,drawManager:MUIDrawManager,frameContext:MFrameContext,data:om.MUserData)->Self:
		"""addUIDrawables(objPath, drawManager, frameContext, data) -> self

		Provides access to the MUIDrawManager, which can be used to queue up operations to draw simple UI shapes like lines, circles, text, etc.

		This method will only be called when hasUIDrawables() is overridden to return True.
		It is called after prepareForDraw() and carries the same restrictions on the sorts of operations it can perform.

		* objPath (MDagPath) - The path to the object being drawn.
		* drawManager (MUIDrawManager) - The UI draw manager, it can be used to draw some simple geometry including text.
		* frameContext (MFrameContext) - Frame level context information.
		* data (MUserData) - Data cached by prepareForDraw()."""
	def boundingBox(self,objPath:om.MDagPath,cameraPath:om.MDagPath)->om.MBoundingBox:
		"""boundingBox(objPath, cameraPath) -> MBoundingBox

		Called by Maya whenever the bounding box of the drawable object is needed.
		This method should return the object space bounding box for the object to be drawn.

		Note that this method will not be called if the isBounded() method returns a value of False.

		* objPath (MDagPath) - The path to the object being drawn
		* cameraPath (MDagPath) - The path to the camera that is being used to draw

		Returns The object space bounding box of object drawn in the draw callback"""
	def disableInternalBoundingBoxDraw(self)->bool:
		"""disableInternalBoundingBoxDraw() -> bool

		Returns True to disable bounding box drawing. The default value is False.

		Indicates whether to disable the automatic drawing of bounding boxes when the display mode has been set to bounding box display.


		Note that bounding box drawing is also disabled if the isBounded() method has been set to False.
		As noted the boundingBox() method is never called under this condition.
		As such with no bounding box information provided it is not possible to automatically draw due to insufficient information provided."""
	def excludedFromPostEffects(self)->bool:
		"""excludedFromPostEffects() -> bool

		Returns False to indicate inclusion in post effects. The default value is true.

		Indicates whether or not the draw code should be called for any additional passes required to perform post effects.


		Note that the appropriate pass identifier and pass semantic can be queried at draw time via the MPassContext data structure.
		Also note that if the pass requires a shader override that it can be obtained from the MDrawContext data structure provided at draw time."""
	def isTransparent(self)->bool:
		"""isTransparent() -> bool

		Returns True to indicate inclusion in transparency passes. The default value is false.

		Indicates whether or not the draw method should be called for each transparency pass(front-culling and back-culling)."""
	def hasUIDrawables(self)->bool:
		"""hasUIDrawables() -> bool

		Query whether 'addUIDrawables()' will be called or not.

		In order for any override for the addUIDrawables() method to be called this method must also be overridden to return True.

		This method should not be overridden if addUIDrawables() has not also been overridden as there may be associated wasted overhead."""
	def isBounded(self,objPath:om.MDagPath,cameraPath:om.MDagPath)->bool:
		"""isBounded(objPath, cameraPath) -> bool

		Returns True if object is bounded.

		Called by Maya to determine if the drawable object is bounded or not. If the object is not bounded then it will never
		be culled by the current camera frustum used for drawing.

		The default implementation will always return True.
		This method can be overridden in derived classes to customize the behaviour.

		Note that if this method returns False then the boundingBox() method will not be called as no bounds are required in this case.

		* objPath (MDagPath) - The path to the object whose transform is needed.
		* cameraPath (MDagPath) - The path to the camera that is being used to draw."""
	def prepareForDraw(self,objPath:om.MDagPath,cameraPath:om.MDagPath,frameContext:MFrameContext,oldData:om.MUserData)->om.MUserData:
		"""prepareForDraw(objPath, cameraPath, frameContext, oldData) -> MUserData

		Called by Maya each time the object needs to be drawn. Any data needed from the Maya dependency graph must be retrieved and cached in this stage. It is invalid to pull data from the Maya dependency graph in the draw callback method and Maya may become unstable if that is attempted.

		Implementors may allow Maya to handle the data caching by returning a pointer to the data from this method. The pointer must be to a class derived from MUserData. This same pointer will be passed to the draw callback. On subsequent draws, the pointer will also be passed back into this method so that the data may be modified and reused instead of reallocated. If a different pointer is returned Maya will delete the old data. If the cache should not be maintained between draws, set the delete after use flag on the user data. In all cases, the lifetime and ownership of the user data is handled by Maya and the user should not try to delete the data themselves. Data caching occurs per-instance of the associated DAG object. The lifetime of the user data can be longer than the associated node, instance or draw override. Due to internal caching, the user data can be deleted after an arbitrary long time. One should therefore be careful to not access stale objects from the user data destructor. If it is not desirable to allow Maya to handle data caching, simply return NULL in this method and ignore the user data parameter in the draw callback method.

		* objPath (MDagPath) - The path to the object being drawn
		* cameraPath (MDagPath) - The path to the camera that is being used to draw
		* frameContext (MFrameContext) - Frame level context information
		* oldData (MUserData) - Data cached by the previous draw of the instance

		Returns the data to be passed to the draw callback method"""
	def refineSelectionPath(self,selectInfo:MSelectionInfo,hitItem:MRenderItem,path:Any,components:Any,objectMask:Any)->bool:
		"""refineSelectionPath(selectInfo, hitItem, path, components, objectMask) -> bool

		This method is called during the hit test phase of the viewport 2.0 selection and is used to override the selected path, the selected components or simply reject the selection.
		Should return True if the selection candidate is acceptable.

		One can decide to change the selected path (ie: select the bottom-most transform instead of the proposed path).
		One can decide to remove or add component to the proposed selected list.
		One can decide to change the selection mask of the object (ie: override the selection mask returned by a component converter).
		One can decide that the proposed selection (path or component) is not acceptable and discard it (ie: return False).

		The default implementation makes no changes to 'path', 'components' or 'objectMask' and returns True (i.e. the selection is accepted).

		* selectInfo (MSelectionInfo) - The selection info
		* hitItem (MRenderItem) - The render item hit
		* path [IN/OUT] (MDagPath) - The selected path
		* components [IN/OUT] (MObject) - The selected components
		* objectMask [IN/OUT] (MSelectionMask) - The object selection mask"""
	def supportedDrawAPIs(self)->DrawAPI:
		"""supportedDrawAPIs() -> DrawAPI

		Returns the draw API supported by this override."""
	def transform(self,objPath:om.MDagPath,cameraPath:om.MDagPath)->om.MMatrix:
		"""transform(objPath, cameraPath) -> MMatrix

		Returns The world space transformation matrix.

		Called by Maya whenever the world space transform is needed for the object to be drawn by the draw callback.
		The default implementation simply returns the transformation defined by the parent transform nodes in Maya.
		Override to get custom behaviour.

		* objPath (MDagPath) - The path to the object whose transform is needed.
		* cameraPath (MDagPath) - The path to the camera that is being used to draw."""
	def wantUserSelection(self)->bool:
		"""wantUserSelection() -> bool

		This method is called during the hit test phase of Viewport 2.0 selection and is used to indicate whether or not the userSelect() method should be called to override the default hit test implementation for the associated DAG object.

		This method returns false by default. In this case the draw callback method is invoked for the selection pass, with a special shader that encodes each entity with a different plain color, then the draw buffer is scanned and each color found inside the selection region is transformed into hit info that will be used by the later selection interpretation phase, including selected item and world-space hit point.

		If a custom hit test implementation is required, this method must be overridden to return true in order for userSelect() to be called. """
	def userSelect(self,selectInfo:Any,drawContext:Any,objPath:Any,data:Any,selectionList:Any,worldSpaceHitPts:Any)->bool:
		"""userSelect(selectInfo, drawContext, objPath, data, selectionList, worldSpaceHitPts) -> bool

		This method is called during the hit test phase of Viewport 2.0 selection if wantUserSelection() returns true, in order to override the default hit test implementation for the associated DAG object.

		The selection info encapsulates the selection states such as the selection region. The draw context along with the user data cached by prepareForDraw() provides information the same as that being passed to the draw callback, thus makes it possible for a draw override to match its custom hit test with its custom drawing (a.k.a. WYSIWYG selection).

		If the object is hit, the implementation should add the DAG path and if appropriate its component to selectionList. It is the responsibility of the implementation to add world-space coordinate of the intersection between the selected item and selection ray to worldSpaceHitPts.

		A custom hit test implementation can choose GPU-based approaches such as OpenGL selection mode, occlusion query etc., or CPU-based approaches which perform hit test for custom geometries. Note that a custom hit test implementation is an object-level override, thus the default hit test implementation can still work for other objects in the scene.

		After a scene traversal in the hit test phase, Maya records a list of selected items and hit points. During the selection interpretation phase, the hit points will be sorted for certain cases such as single selection; only the winning hit point(s) will have the corresponding selected item(s) to call the refineSelectionPath() method for final selection result that is used to adjust the global active selection list. Thus, for these cases, Maya can only guarantee correct behavior if the implementation returns a valid hit point.

		For cases such as marquee selection over multiple components, where hit points don't matter, instead of creating one component object for each selected component element, the implementation should create one component object for all selected component elements, to avoid any unnecessary performance overhead due to the frequency of calling refineSelectionPath().

		For cases such as point snapping, where multiple hit points are required, each hit point should be stored with the same array index as its selected item (typically a vertex component object), in order for Maya to associate each pair of selected item and hit point.

		This method should return true if at least one object was hit. The default value is false.

		* selectInfo [IN] (MSelectionInfo) - The selection info
		* context [IN] (MDrawContext) - The draw context
		* objPath [IN] (MDagPath) - The path to the associated DAG object
		* data [IN] (MUserData) - The data cached by prepareForDraw()
		* selectionList [OUT] (MSelectionList) - List of items selected by this method
		* worldSpaceHitPts [OUT] (MPointArray) - List of hit points"""
	def updateSelectionGranularity(self,path:Any,selectionContext:Any)->Self:
		"""updateSelectionGranularity(path, selectionContext) -> self

		This is method is called during the pre-filtering phase of the viewport 2.0 selection and is used to setup the selection context of the given DAG object.

		This is useful to specify the selection level, which defines what can be selected on the object :
		  MSelectionContext.kNone        Nothing can be selected
		  MSelectionContext.kObject      Object can be selected as a whole
		  MSelectionContext.kComponent   Parts of the object - such as vertex, edge or face - are selectable
		This is used to discard objects that are not selectable given the current selection mode (see MGlobal.selectionMode()).

		The default implementation leaves the selection level set at its default value, which is kObject.

		 path (MDagPath) - The path to the instance to update the selection context for
		 selectionContext [OUT] (MSelectionContext) - The selection context"""
	@staticmethod
	def pointSnappingActive()->bool:
		"""pointSnappingActive() -> bool

		This utility function can be called by a draw override to query whether Viewport 2.0 selection has been launched to find points for snapping. If so, in order for the associated DAG object to participate,

		- The MPxSurfaceShape::getComponentSelectionMask() method must be overridden to include MSelectionMask::kSelectPointsForGravity.

		- During the pre-filtering phase, updateSelectionGranularity() must be overridden to set the selection level to MSelectionContext::kComponent.

		- During the hit test phase, wantUserSelection() must be overridden to return true, userSelect() must be overridden to return points for snapping.

		The method returns true if snapping to points is active."""
	def traceCallSequence(self)->bool:
		"""traceCallSequence() -> bool

		This method allows a way for a plug-in to examine
		the basic call sequence for a draw override.

		The default implementation returns false meaning no
		tracing will occur."""
	def handleTraceMessage(self,message:Any)->Self:
		"""handleTraceMessage(message) -> self

		When debug tracing is enabled via MPxDrawOverride::traceCallSequence(),
		this method will be called for each trace message.

		The default implementation will print the message
		to stderr.

		* message - A string which will provide feedback on either an
		internal or plug-in call location. To help distinguish which
		draw override a message is associated with, the full path
		name for the DAG object (associated with the draw override) may
		be included as part of the string."""
class MPxGeometryOverride:
	"""Base for user-defined classes to prepare geometry for drawing."""
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def addUIDrawables(self,path:om.MDagPath,drawManager:MUIDrawManager,frameContext:MFrameContext)->Self:
		"""addUIDrawables(path, drawManager, frameContext) -> self

		For each instance of the object, besides the render items updated in updateRenderItems() there is also a render item list for rendering simple UI elements.
		This stage gives the plugin access to MUIDrawManager which aids in drawing simple geometry like line, circle, rectangle, text, etc.

		Overriding this methods is not always necessary, but if you want to override it, please also override 'hasUIDrawables()' to make it return True or the overridden method will not be called.

		If you are not going to override this function, please don't make 'hasUIDrawables()' return True or there may be some wasted performance overhead.

		Implementation of this method here is empty.

		* path (MDagPath) - The path to the instance to update auxiliary items for.
		* drawManager (MUIDrawManager) - The draw manager used to draw simple geometry.
		* frameContext (MFrameContext) - Frame level context information."""
	def cleanUp(self)->Self:
		"""cleanUp() -> self

		Called after all other stages are completed. Clean up any cached data stored from the updateDG() phase."""
	def hasUIDrawables(self)->bool:
		"""hasUIDrawables() -> bool

		Query whether 'addUIDrawables()' will be called or not.

		In order for any override for the addUIDrawables() method to be called this method must also be overridden to return True.

		This method should not be overridden if addUIDrawables() has not also been overridden as there may be associated wasted overhead."""
	def isIndexingDirty(self,item:MRenderItem)->bool:
		"""isIndexingDirty(item) -> bool

		Returns True if the index buffer needs to be updated.

		This method is called for each render item on the assocated DAG object whenever the object changes. This method is passed a render item. This method should return True if the indexing for the render item has changed since the last frame. Note that returning False from isIndexingDirty may NOT prevent populate geometry from requiring that an index buffer is updated.

		* item (MRenderItem) - The render item in question."""
	def isStreamDirty(self,desc:MVertexBufferDescriptor)->bool:
		"""isStreamDirty(desc) -> bool

		Returns True if the vertex buffer needs to be updated.

		This method is called for each geometry stream on the assocated DAG object whenever the object changes. This method is passed a vertex buffer descriptor representing one stream on the object to be updated. This method should return True if it is safe to reuse the existing buffer rather than filling a new buffer with data. Note that returning False from isStreamDirty may NOT prevent populateGeometry from requiring that a stream be updated.

		* desc (MVertexBufferDescriptor) - The description of the vertex buffer."""
	@staticmethod
	def pointSnappingActive()->bool:
		"""pointSnappingActive() -> bool

		Returns True if selection has been launched to find snap points.
		To participate, you need to have at least one render item with point geometry
		and MSelectionMask.kSelectPointsForGravity set in MRenderItem.selectableMask().
		- The granularity must be set to MSelectionContext.kComponent in updateSelectionGranularity()
		- A component converter is not necessary in this scenario.
		- refineSelectionPath() will not be called. All points present in the render item will be
		considered suitable locations for snapping."""
	def populateGeometry(self,requirements:MGeometryRequirements,renderItems:MRenderItemList,data:Any)->Self:
		"""populateGeometry(requirements, renderItems, data) -> self

		Implementations of this method should create and populate vertex and index buffers on the MGeometry instance 'data' in order to fulfill all of the geometry requirements defined by the 'requirements' parameter. Failure to do so will result in the object either drawing incorrectly or not drawing at all. See the documentation of MGeometryRequirements and MGeometry for more details on the usage of these classes. The geometry requirements will ask for index buffers on demand. Implementations can force the geometry requirements to update index buffers by calling MRenderer.setGeometryDrawDirty() with topologyChanged setting to True.

		* requirements (MGeometryRequirements) - The requirements that need to be satisfied.
		* renderItems (MRenderItemList) - The list of render items that need to be updated.
		* data [OUT] (MGeometry) - The container for the geometry data"""
	def refineSelectionPath(self,selectInfo:MSelectionInfo,hitItem:MRenderItem,path:Any,components:Any,objectMask:Any)->bool:
		"""refineSelectionPath(selectInfo, hitItem, path, components, objectMask) -> bool

		This method is called during the hit test phase of the viewport 2.0 selection and is used to override the selected path, the selected components or simply reject the selection.
		Should return True if the selection candidate is acceptable.

		One can decide to change the selected path (ie: select the bottom-most transform instead of the proposed path).
		One can decide to remove or add component to the proposed selected list.
		One can decide to change the selection mask of the object (ie: override the selection mask returned by a component converter).
		One can decide that the proposed selection (path or component) is not acceptable and discard it (ie: return False).

		The default implementation makes no changes to 'path', 'components' or 'objectMask' and returns True (i.e. the selection is accepted).

		* selectInfo (MSelectionInfo) - The selection info
		* hitItem (MRenderItem) - The render item hit
		* path [IN/OUT] (MDagPath) - The selected path
		* components [IN/OUT] (MObject) - The selected components
		* objectMask [IN/OUT] (MSelectionMask) - The object selection mask"""
	def supportedDrawAPIs(self)->DrawAPI:
		"""supportedDrawAPIs() -> DrawAPI

		Returns the draw API supported by this override."""
	def configCache(self,evalNode:om.MEvaluationNode,schema:om.MCacheSchema)->None:
		"""configCache(evalNode, schema) -> None

		Defines the node's behavior when participating in Cached Playback.

		This method will be called at EM partitioning time, after rules evaluation.

		* evalNode (MEvaluationNode)  - This node's evaluation node, contains animated plug information
		* schema (MCacheSchema)       - Specification about what attributes to cache"""
	def updateDG(self)->Self:
		"""updateDG() -> self

		Perform any work required to translate the geometry data that needs to get information from the dependency graph.  This should be the only place that dependency graph evaluation occurs. Any data retrieved should be cached for later stages."""
	def updateRenderItems(self,path:om.MDagPath,list:list)->Self:
		"""updateRenderItems(path, list) -> self

		This method is called for each instance of the associated DAG object whenever the object changes. The method is passed the path to the instance and the current list of render items associated with that instance. By default the list will contain one render item for each shader assigned to the instance. Implementations of this method method may add, remove or modify items in the list. Note that removal of items created by Maya for assigned shaders is not allowed and will fail. As an alternative this method can disable those items so that they do not draw.

		* path (MDagPath) - The path to the instance to update render items for
		* list [IN/OUT] (MRenderItemList) - The current render item list, items may be modified, added or removed."""
	def requiresUpdateRenderItems(self,path:om.MDagPath)->bool:
		"""requiresUpdateRenderItems(path) -> bool

		This method is called for each instance of the associated DAG object whenever the object changes.If, during a single draw - preparation phase this method returns false for all DAG instances of this MPxGeometryOverride then updateRenderItems() will not be called for the draw - preparation phase.

		* path (MDagPath) - The path to the instance to update render items for"""
	def requiresGeometryUpdate(self)->bool:
		"""requiresGeometryUpdate() -> bool

		This method is called one during each draw - preparation phase. If this method returns true then all of the other MPxGeometryOverride methods will be called for the associated DAG object this draw preparation phase.If this method returns false then all of the other MPxGeometryOverride methods may be called.This code has to be thread safe, non - blocking and work only on data owned by the associated DAG object."""
	def supportsEvaluationManagerParallelUpdate(self)->bool:
		"""supportsEvaluationManagerParallelUpdate() -> bool

		This method is called for each MPxGeometryOverride in the scene to determine if the MPxGeometryOverride is eligible for Evaluation Manager Parallel Update."""
	def supportsVP2CustomCaching(self)->bool:
		"""supportsVP2CustomCaching() -> bool

		This method is called for each MPxGeometryOverride in the scene to determine if the MPxGeometryOverride is eligible for VP2 Evaluation Caching."""
	def updateSelectionGranularity(self,path:Any,selectionContext:Any)->Self:
		"""updateSelectionGranularity(path, selectionContext) -> self

		This is method is called during the pre-filtering phase of the viewport 2.0 selection and is used to setup the selection context of the given DAG object.

		This is useful to specify the selection level, which defines what can be selected on the object :
		  MSelectionContext.kNone        Nothing can be selected
		  MSelectionContext.kObject      Object can be selected as a whole
		  MSelectionContext.kComponent   Parts of the object - such as vertex, edge or face - are selectable
		This is used to discard objects that are not selectable given the current selection mode (see MGlobal.selectionMode()).

		The default implementation leaves the selection level set at its default value, which is kObject.

		 path (MDagPath) - The path to the instance to update the selection context for
		 selectionContext [OUT] (MSelectionContext) - The selection context"""
	def traceCallSequence(self)->bool:
		"""traceCallSequence() -> bool

		This method allows a way for a plug-in to examine
		the basic call sequence for a geometry override.

		The default implementation returns false meaning no
		tracing will occur."""
	def handleTraceMessage(self,message:Any)->Self:
		"""handleTraceMessage(message) -> self

		When debug tracing is enabled via MPxGeometryOverride::traceCallSequence(),
		this method will be called for each trace message.

		The default implementation will print the message
		to stderr.

		* message - A string which will provide feedback on either an
		internal or plug-in call location. To help distinguish which
		geometry override a message is associated with, the full path
		name for the DAG object (associated with the geometry override) may
		be included as part of the string."""
	def getFrameContext(self)->MFrameContext:
		"""getFrameContext() -> MFrameContext

		Return a frame context. The context is not available if called before setup or after cleanup.
		The context should never be deleted by the plug-in as it is owned by the geometry override."""
class MPxImagePlaneOverride:
	"""(Deprecated: The class isn't required for MPxImagePlane to be supported in Viewport 2.0.) Base class for user defined Image Plane overrides."""
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def supportedDrawAPIs(self)->DrawAPI:
		"""supportedDrawAPIs() -> DrawAPI

		Returns the draw API supported by this override."""
class MPxIndexBufferMutator:
	"""Base class for user defined index buffer mutators."""
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def mutateIndexing(self,sourceIndexBuffers:MComponentDataIndexingList,vertexBuffers:MVertexBufferArray,indexBuffer:Any)->tuple[int,int]:
		"""mutateIndexing(sourceIndexBuffers, vertexBuffers, indexBuffer) -> (int, int)

		This method gets called to allow the generator to mutate the data for a custom index stream using information stored in the vertex buffers.

		* sourceIndexBuffers (MComponentDataIndexingList) - Current values for the index buffers.
		* vertexBuffers (MVertexBufferArray) - All vertex buffers generated for this primitive.
		* indexBuffer [OUT] (MIndexBuffer) - The index buffer to fill.

		Returns the type of primitive of the generated indexing and the stride of the generated indexing, only valid when the returned primitive type is kPatch
		See MGeometry.primitiveString() description for a list of valid primitive types."""
class MPxPrimitiveGenerator:
	"""Base class for user defined primitive generators."""
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def computeIndexCount(self,object:om.MObject,component:om.MObject)->int:
		"""computeIndexCount(object, component) -> int

		This function is called to allow the primitive generator to provide the number of vertices it will use.

		* object (MObject) - The object being evaluated.
		* component (MObject) - The components to use."""
	def generateIndexing(self,object:om.MObject,component:om.MObject,sourceIndexing:MComponentDataIndexingList,targetIndexing:MComponentDataIndexingList,indexBuffer:Any)->tuple[int,int]:
		"""generateIndexing(object, component, sourceIndexing, targetIndexing, indexBuffer) -> (int, int)

		This method gets called to allow the generator to fill in the data for a custom index stream.

		* object (MObject) - The object being evaluated.
		* component (MObject) - The components to use when building the index buffer.
		* sourceIndexing (MComponentDataIndexingList) - Vertex index mapping in the declared MComponentDataIndexing::MComponentType space.
		* targetIndexing (MComponentDataIndexingList) - Vertex index mapping from targetIndexing.getComponentType() space to vertex buffer space.
		* indexBuffer [OUT] (MIndexBuffer) - The index buffer to fill.

		Returns the type of primitive of the generated indexing and the stride of the generated indexing, only valid when the returned primitive type is kPatch
		See MGeometry.primitiveString() description for a list of valid primitive types."""
class MPxShaderOverride:
	"""Base class for user defined shading effect draw overrides."""
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def activateKey(self,context:Any,key:Any)->Self:
		"""activateKey(context, key) -> self

		This is the activateKey callback.

		This method is called during the draw phase before invoking any draw() callback that are sharing a common shader key.

		The default implementation is empty."""
	def addGeometryRequirement(self,MVertexBufferDescriptor:Any)->Self:
		"""addGeometryRequirement(MVertexBufferDescriptor) -> self

		During the initialization phase the geometry requirements for the shading effect can be updated. The update is
		accomplished by calling this method once for each new data stream that needs to be added to the list of requirements.

		If the geometry has multiple fields of the same type associated with it (e.g. multiple UV sets) the 'name' attribute
		of the vertex descriptor can be used to select the desired one. If that member is empty or does not match any of the
		fields then the default field of that type will be used."""
	def addGeometryRequirements(self,MVertexBufferDescriptorList:Any)->Self:
		"""addGeometryRequirements(MVertexBufferDescriptorList) -> self


		During the initialization phase the geometry requirements for the shading effect can be updated. The update is
		accomplished by calling this method with a list containing descriptions of all data streams that are required by the shader.

		If the geometry has multiple fields of the same type associated with it (e.g. multiple UV sets) the 'name' attribute
		of the vertex descriptor can be used to select the desired one. If that member is empty or does not match any of the
		fields then the default field of that type will be used.

		This method will attempt to add as many requirements as possible from the list, skipping invalid ones.
		If kInvalidParameter is returned it means at least one requirement failed to be added."""
	def addIndexingRequirement(self,MIndexBufferDescriptor:Any)->Self:
		"""addIndexingRequirement(MIndexBufferDescriptor) -> self

		During the initialization phase the indexing requirements for the shading effect can be updated. The update is accomplished by
		calling this method once for each new index stream required by the shader.

		A shader override can specify the type of primitive it supports.  If the shader relies on a special primitive type like kPatch
		it should use this method to indicate that requirement to the system.  Not all fields on the MIndexBufferDescriptor need to be
		filled in when using this method.  Only the name(), primitive(), and primitiveStride() values are important for a shader to report
		as requirements.

		The primitive type must be specified if the shader requires a primitive type different then a standard point, line, or triangle list
		or strip. The primitiveStride must be specified if using the kPatch primitive type. Valid values range from 1 - 32.
		The name can be specified to trigger a custom MPxPrimitiveGenerator plugin to be used to produce the desired primitive tessellation.
		When requesting custom primitives you should register an MPxPrimitiveGenerator that knows how to produce the custom primitive needed
		by the shader."""
	@overload
	def addShaderSignature(self,signature:Any,signatureSize:Any)->Self:
		"""addShaderSignature(signature, signatureSize) -> selfaddShaderSignature(MShaderInstance) -> self

		During the initialization phase, the "signature" for the shader may be set. Certain Draw APIs (like DirectX 11) require a
		signature to allow a shading effect to be properly activated. The signature will be used if the override uses
		MPxShaderOverride.drawGeometry() in the draw phase in order to perform drawing. If drawing is done manually, adding a shader
		signature is not necessary."""
	@overload
	def addShaderSignature(self,MShaderInstance:Any)->Self:
		"""addShaderSignature(signature, signatureSize) -> selfaddShaderSignature(MShaderInstance) -> self

		During the initialization phase, the "signature" for the shader may be set. Certain Draw APIs (like DirectX 11) require a
		signature to allow a shading effect to be properly activated. The signature will be used if the override uses
		MPxShaderOverride.drawGeometry() in the draw phase in order to perform drawing. If drawing is done manually, adding a shader
		signature is not necessary."""
	def boundingBoxExtraScale(self)->float:
		"""boundingBoxExtraScale() -> float

		Returns the Extra scale factor.

		Override this method to supply an extra scale factor to be applied to the object space bounding box of any objects
		which use the shader associated with this override. This is to allow the shader to indicate that the bounding box should
		be bigger than just the base geometry; normally due to shading effects like displacement. Note that the value returned
		here will only be used to put a lower bound on the extra scale applied to the bounding box. It may be made larger due to
		the demands of other shaders associated with the object.

		This method will be called any time a change occurs which may affect the bounding box of associated objects. It is acceptable
		to access the Maya dependency graph within calls to this method as it will never be called during draw.

		The default implementation returns the unit scale factor (1.0)."""
	def draw(self,context:Any,renderItemList:MRenderItemList)->bool:
		"""draw(context, renderItemList) -> bool

		This is the draw callback, the method is called during the draw phase.

		The expected implementation of this method is to do shader setup and then call drawGeometry() to allow Maya to handle the actual geometry drawing. It is however possible to do all shader setup and geometry draw here directly by accessing the hardware resource handles for geometry and index buffers through the geometry associated with each render item in the render item list.

		No dependency graph evaluation should occur during this phase. If data from Maya is needed here it must be cached on this object (or elsewhere) during the update phase.

		This method should return True on successful draw. If False is returned, Maya will attempt to draw using the default internal draw mechanism.

		Information about the current GPU state may be accessed through the MDrawContext object passed to this method. The MRenderItemList object contains one render item for each object that is meant to be drawn by this method.

		* context [IN/OUT] (MDrawContext) - The current draw context
		* renderItemList (MRenderItemList) - The list of renderable items to draw

		Returns True if draw was successful, False otherwise."""
	def drawGeometry(self,MDrawContext:Any)->Self:
		"""drawGeometry(MDrawContext) -> self

		This method may be called from draw() and will cause Maya to immediately draw the current geometry using the current state of the draw API."""
	def endUpdate(self)->Self:
		"""endUpdate() -> self

		This is the final part of the update phase.

		This method is called by Maya to allow the plugin to clean up any data or state from the previous update stages.
		No dependency graph evaluation, nor graphics device access should be performed during this phase."""
	def handlesConsolidatedGeometry(self)->bool:
		"""handlesConsolidatedGeometry() -> bool

		Returns True if the shader instance should enable the consolidation
		for the geometry it is applied to.

		Override this method if the shader instance should disable the consolidation
		for the geometry it is applied to.This is to prevent inconsistency between consolidated and non-consolidated geometry,
		particularly useful for shading effects that compute displacement based on
		the World position.

		The default implementation returns true indicating that the shader instance
		should enable the consolidation of the geometry."""
	def handlesDraw(self,context:Any)->bool:
		"""handlesDraw(context) -> bool

		Returns True if shader handles drawing.

		This method indicates whether the shader will handle the drawing based on the context passed in.

		The default implementation will check the pass context. If the pass semantic is specified to be a color pass
		and the pass has no shader override (MPassContext.hasShaderOverride() returns False) then this method will return True."""
	@overload
	def initialize(self,shader:Any)->str:
		"""initialize(shader) -> string
		initialize(initContext, initFeedback) -> string

		Initialization occurs when Maya determines that the hardware shader needs to be rebuilt. Any initialization
		work may be performed here. Also, this is the only time that calls to addGeometryRequirement() may occur.

		Note: There are two versions of the initialize method. Derived classes should override exactly one of them.

		The default implementation returns a constant string."""
	@overload
	def initialize(self,initContext:Any,initFeedback:Any)->str:
		"""initialize(shader) -> string
		initialize(initContext, initFeedback) -> string

		Initialization occurs when Maya determines that the hardware shader needs to be rebuilt. Any initialization
		work may be performed here. Also, this is the only time that calls to addGeometryRequirement() may occur.

		Note: There are two versions of the initialize method. Derived classes should override exactly one of them.

		The default implementation returns a constant string."""
	def initialize2(self,initContext:Any)->str|userData:
		"""initialize2(initContext) -> string, userData

		Initialization occurs when Maya determines that the hardware shader needs to be rebuilt. Any initialization
		work may be performed here. Also, this is the only time that calls to addGeometryRequirement() may occur.

		The default implementation returns a string and None MUserData"""
	def isTransparent(self)->bool:
		"""isTransparent() -> bool

		Returns True if semi-transparent drawing should occur.

		During the update phase the override will be called to return whether it will be drawing with semi-transparency.

		This call occurs after updateDevice() which allows for any device evaluation to occur to determine the transparency state.

		The default return value is False."""
	@overload
	def nonTexturedShaderInstance(self)->MShaderInstance:
		"""nonTexturedShaderInstance() -> MShaderInstancenonTexturedShaderInstance() -> (MShaderInstance, bool)

		Returns an override shader instance to be used when drawing in non-textured
		mode. If None is returned an internally defined non-modifiable shader
		instance is used.

		A second optional boolean value 'monitorNode' can be returned as well which will indicate
		that the associated shader node requires monitoring to call back to the override
		during the update phase.

		Note that if transparency is required at initialization time then
		the method setIsTransparent() should be called
		within this method.

		The default implementation returns None indicating that no shader instance will be used."""
	@overload
	def nonTexturedShaderInstance(self)->tuple[MShaderInstance,bool]:
		"""nonTexturedShaderInstance() -> MShaderInstancenonTexturedShaderInstance() -> (MShaderInstance, bool)

		Returns an override shader instance to be used when drawing in non-textured
		mode. If None is returned an internally defined non-modifiable shader
		instance is used.

		A second optional boolean value 'monitorNode' can be returned as well which will indicate
		that the associated shader node requires monitoring to call back to the override
		during the update phase.

		Note that if transparency is required at initialization time then
		the method setIsTransparent() should be called
		within this method.

		The default implementation returns None indicating that no shader instance will be used."""
	def overridesDrawState(self)->bool:
		"""overridesDrawState() -> bool

		Returns True if the override overrides the draw state.

		During the draw phase this method will be called to determine whether the override will override the draw state when drawing.

		This call occurs after updateDevice() which allows for any device evaluation to occur to determine if the override will
		override the draw state.

		The Viewport 2.0 renderer will skip setting the draw state for plugins that will override the draw state when drawing.
		Note that the MPxShaderOverride.terminateKey() should still return the draw state to the value it had when activateKey was called.

		The default return value is False."""
	def overridesNonMaterialItems(self)->bool:
		"""overridesNonMaterialItems() -> bool

		Returns True if the shader instance should also be used to render non material items.

		Override this method if the shader instance should also be used to render
		non material items such as the wireframe and the selected edges/vertices components.
		This is particularly useful for shading effects that compute displacement for
		which the object geometry will not match the rendered material, making selection
		difficult.

		The default implementation returns False indicating that the shader instance
		should not be used for non material items."""
	def rebuildAlways(self)->bool:
		"""rebuildAlways() -> bool

		Returns True if the shader and geometry should be rebuilt on every update.

		If this method returns True, it will force shader and geometry data to be rebuilt on any change to the shader.
		This may be necessary for shaders that request specific named data sets like UVs or CPVs.
		Any change to the required data set means that geometry needs to be rebuilt.

		The default return value is False."""
	def setGeometryRequirements(self,MShaderInstance:Any)->Self:
		"""setGeometryRequirements(MShaderInstance) -> self


		During the initialization phase the geometry requirements for the shading effect can be updated. The update can be
		accomplished by calling this method with a shader instance (MShaderInstance). The geometry requirements are copied
		from the MShaderInstance and used as the current shading effect requirements. If there are any requirements already
		specified for the shading effect, they will be replaced.

		This method should not be used in conjunction with addGeometryRequirement() and addGeometryRequirements() methods.
		The reason is that when rendering the vertex format used must exactly match the one used for the shader instance.
		If any additional requirements are added, the geometry may not draw properly.

		The corresponding addShaderSignature() method, which takes an MShaderInstance as an input argument, should also be
		called during initialization if the utility method drawGeometry() is used by the plug-in."""
	def shaderInstance(self)->MShaderInstance:
		"""shaderInstance() -> MShaderInstance

		Returns the Shader instance.

		Override this method if a shader instance (MShaderInstance) is to be used for drawing.

		The default implementation returns None indicating that no shader instance will be used."""
	def supportedDrawAPIs(self)->DrawAPI:
		"""supportedDrawAPIs() -> DrawAPI

		Returns The draw API supported by this override.

		Returns the draw API supported by this override. The returned value may be formed as the bitwise 'or'
		of render drawAPI elements to indicate that the override supports multiple draw APIs. See MRenderer.drawAPI().
		This method returns 'MRender.kOpenGL' by default."""
	def supportsAdvancedTransparency(self)->bool:
		"""supportsAdvancedTransparency() -> bool

		Returns True if advanced tranparency algorithm is supported.

		During the update phase the override will be called to return whether it supports advanced transparency algorithms
		(such as depth peeling)."""
	def terminateKey(self,context:Any,key:Any)->Self:
		"""terminateKey(context, key) -> self

		This is the terminateKey callback.

		This method is called during the draw phase after invoking draw() callbacks that are sharing a common shader key.

		The default implementation is empty."""
	def updateDG(self,object:Any)->Self:
		"""updateDG(object) -> self

		This is the first part of the update phase.

		Perform any work required to update the shading effect which is related to evaluating the dependency graph.
		This should be the only place that dependency graph evaluation occurs. Data retrieved from Maya may be cached
		on the override for use in later stages."""
	def updateDevice(self)->Self:
		"""updateDevice() -> self

		This is the second part of the update phase.

		Perform any work required to update the shading effect which is related to accessing the underlying graphics
		device. This is the only place that the graphics device may be safely accessed other than at draw time."""
class MPxShadingNodeOverride:
	"""Base class for user defined shading node overrides."""
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def allowConnections(self)->bool:
		"""allowConnections() -> bool

		Returns True if connections should be allowed to parameters of the fragment that do not have custom mappings that
		specifically prevent connections.

		An override may prevent Maya from connecting fragments to specific parameters of the fragment for this
		override by providing custom attribute parameter mappings. It is also possible to prevent connections to all
		parameters on the fragment by overriding this method to return False.
		In that case, the fragment for this override will become a final fragment, and nothing will be connected to it.
		This is equivalent to creating an attribute parameter mapping for every parameter on the fragment and setting
		the allowConnection flag on each mapping to False.

		This method is called once only, just after creation of the override."""
	@overload
	def fragmentName(self)->str:
		"""fragmentName() -> stringfragmentName(isTexturedShading) -> string

		Override this method to return the name of the fragment or fragment graph to use for rendering the shading node associated with this override. This fragment will be automatically connected to the other fragments for the other nodes in the shading network to produce a complete shading effect.

		A fragment with the returned name must already exist in the fragment manager for rendering to succeed. If the fragment does not exist, the associated node will not contribute to shading.

		The parameter values for the fragment will be automatically populated from the attribute values on the node wherever the name and type of a parameter on the fragment match the name and type of an attribute on the node.

		The fragment will only be connected to the other fragments in the graph if the output parameter of the fragment has the same name as the output attribute of the node that is connected to the rest of the shading network. To support multiple output attributes of a node, the fragment should return a "struct" type parameter. The names of the members of the struct should match the names of the output attributes for which support is desired. The fragment must compute all output attributes on every execution.

		This optional isTexturedShading parameter is to be used when the override can provide both a textured and an untextured version of itself. The flag will be set to true if this override is used with a textured drawing render item, false otherwise. Updates should be done using the corresponding updateShader(shader, mappings, isTexturedShading) function. The default behavior is to call the generic overload of the same name.

		* isTexturedShading (optional, bool) - specifies if we are requesting a textured or untextured shading fragment name.
		Returns the name of the fragment to use"""
	@overload
	def fragmentName(self,isTexturedShading:optional|bool)->str:
		"""fragmentName() -> stringfragmentName(isTexturedShading) -> string

		Override this method to return the name of the fragment or fragment graph to use for rendering the shading node associated with this override. This fragment will be automatically connected to the other fragments for the other nodes in the shading network to produce a complete shading effect.

		A fragment with the returned name must already exist in the fragment manager for rendering to succeed. If the fragment does not exist, the associated node will not contribute to shading.

		The parameter values for the fragment will be automatically populated from the attribute values on the node wherever the name and type of a parameter on the fragment match the name and type of an attribute on the node.

		The fragment will only be connected to the other fragments in the graph if the output parameter of the fragment has the same name as the output attribute of the node that is connected to the rest of the shading network. To support multiple output attributes of a node, the fragment should return a "struct" type parameter. The names of the members of the struct should match the names of the output attributes for which support is desired. The fragment must compute all output attributes on every execution.

		This optional isTexturedShading parameter is to be used when the override can provide both a textured and an untextured version of itself. The flag will be set to true if this override is used with a textured drawing render item, false otherwise. Updates should be done using the corresponding updateShader(shader, mappings, isTexturedShading) function. The default behavior is to call the generic overload of the same name.

		* isTexturedShading (optional, bool) - specifies if we are requesting a textured or untextured shading fragment name.
		Returns the name of the fragment to use"""
	def getCustomMappings(self,mappings:Any)->Self:
		"""getCustomMappings(mappings) -> self

		Maya will automatically match parameters on the shade fragment specified by this override with attributes on the
		associated Maya node as long as the names and types match. In order to specify custom attribute parameter mappings,
		override this method.

		This method will be called before Maya performs its automatic matching so it can be used to prevent that process by
		defining mappings for parameters that would normally be mapped automatically.
		Such mappings will take precedence over automatic mappings.

		It is an error to provide more than one mapping per fragment parameter.
		Only the first such mapping will be used.

		The same attribute may be used for multiple parameters.

		By default, this method defines no custom mappings.

		* mappings [OUT] (MAttributeParameterMappingList) - An attribute parameter mapping list; fill with any desired custom mappings."""
	def outputForConnection(self,sourcePlug:om.MPlug,destinationPlug:om.MPlug)->str:
		"""outputForConnection(sourcePlug, destinationPlug) -> string

		Returns the name of an output parameter on the fragment for the override.

		When Maya attempts to connect the fragment for this override to the fragment for another node in the shading network,
		it will call this method to get the name of the output on the fragment to use for the connection.
		By default, this will simply return the name of the output attribute on the node for the override that is driving the connection.
		Override this method to specify that a different output of the fragment should be used instead.
		This method may also be overridden to get information about how and where the fragment is being connected.

		If the output of the fragment is of "struct" type, this method should return the name of one of the members of the struct.

		This method is called after getCustomMappings().

		If the name returned does not match the name of any output parameter (or struct member in the case of struct output) on the
		fragment for this override then the fragment will not be connected to the overall shading effect.

		* sourcePlug (MPlug) - The plug on the node for this override which is the source of the connection.
		                       By default the name of the attribute for this plug is returned.
		* destinationPlug (MPlug) - The plug on the node which is the destination of the connection."""
	def supportedDrawAPIs(self)->DrawAPI:
		"""supportedDrawAPIs() -> DrawAPI

		Returns the draw API supported by this override."""
	def updateDG(self)->Self:
		"""updateDG() -> self

		This method is called every time Maya needs to update the parameter values on the final shading effect of which the fragment
		produced by this override is a part. In this method implementations should query and cache any values needed for setting
		parameters on the final shading effect in updateShader()."""
	@overload
	def updateShader(self,shader:MShaderInstance,mappings:MAttributeParameterMappingList)->Self:
		"""updateShader(shader, mappings) -> selfupdateShader(shader, mappings, isTexturedShading) -> self

		This method is called every time Maya needs to update the parameter values on the final shading effect of which the fragment
		produced by this override is a part. Implementations may use the information from the mappings list to set parameter values on
		the shader. The list contains all parameter mappings for the override, both automatic and custom. Although it is possible to set
		the value for any parameter on the shader it is an error to do so for parameters which are not defined by the fragment for this
		override and doing so may result in unpredictable behaviour.

		The default implementation does nothing. Note that values for parameters with valid attribute parameter mappings will be set
		automatically. This method need only be overridden if custom behaviour is required.

		For performance, consider caching the resolved parameter names of parameters needing update the first time this method is called.
		This will avoid searching the mappings list and then retrieving the resolved name from the mapping on each update. Resolved names
		are guaranteed to remain constant until the next time fragmentName() is called. Const pointers to individual mappings may also be
		cached in this way and are valid for the same duration.
		Do not attempt to cache mappings created in the getCustomMappings() method.

		It is an error to attempt to access the Maya dependency graph from within updateShader().
		Any attempt to do so will result in instability. Required data should be retrieved and cached in updateDG().

		This optional isTexturedShading is to be used when the override can provide both a textured and an untextured version of itself
		and implements fragmentName(bool isTexturedShading). The default behavior is to call the generic overload of the same name.

		* shader (MShaderInstance) - The shader instance.
		* mappings (MAttributeParameterMappingList) - The attribute parameter mappings for this override.
		* isTexturedShading (optional, bool) - Are we updating textured or untextured shading"""
	@overload
	def updateShader(self,shader:MShaderInstance,mappings:MAttributeParameterMappingList,isTexturedShading:optional|bool)->Self:
		"""updateShader(shader, mappings) -> selfupdateShader(shader, mappings, isTexturedShading) -> self

		This method is called every time Maya needs to update the parameter values on the final shading effect of which the fragment
		produced by this override is a part. Implementations may use the information from the mappings list to set parameter values on
		the shader. The list contains all parameter mappings for the override, both automatic and custom. Although it is possible to set
		the value for any parameter on the shader it is an error to do so for parameters which are not defined by the fragment for this
		override and doing so may result in unpredictable behaviour.

		The default implementation does nothing. Note that values for parameters with valid attribute parameter mappings will be set
		automatically. This method need only be overridden if custom behaviour is required.

		For performance, consider caching the resolved parameter names of parameters needing update the first time this method is called.
		This will avoid searching the mappings list and then retrieving the resolved name from the mapping on each update. Resolved names
		are guaranteed to remain constant until the next time fragmentName() is called. Const pointers to individual mappings may also be
		cached in this way and are valid for the same duration.
		Do not attempt to cache mappings created in the getCustomMappings() method.

		It is an error to attempt to access the Maya dependency graph from within updateShader().
		Any attempt to do so will result in instability. Required data should be retrieved and cached in updateDG().

		This optional isTexturedShading is to be used when the override can provide both a textured and an untextured version of itself
		and implements fragmentName(bool isTexturedShading). The default behavior is to call the generic overload of the same name.

		* shader (MShaderInstance) - The shader instance.
		* mappings (MAttributeParameterMappingList) - The attribute parameter mappings for this override.
		* isTexturedShading (optional, bool) - Are we updating textured or untextured shading"""
	def handlesConsolidatedGeometry(self)->bool:
		"""handlesConsolidatedGeometry() -> bool

		Returns True if the shading node should enable the consolidation
		for the shading network it belongs to.

		Override this method if the shading node should disable the consolidation
		for the shading network it belongs to.This is to prevent inconsistency between consolidated and non-consolidated geometry,
		particularly useful for shading effects that compute displacement based on
		the World position.


		Shading node is part of the shading network (a shader), the purpose to provide this method
		in the shading node is to give an ability to change the consolidation status in the shading node level.
		For exammple, if one shading node in the shading network is asking to disable the consolidation,
		Then the whole shading network will be disabled for consolidation.

		The default implementation returns true indicating that the shading node
		should enable the consolidation for the shading network."""
	def valueChangeRequiresFragmentRebuild(self,plug:om.MPlug)->bool:
		"""valueChangeRequiresFragmentRebuild(plug) -> bool

		Returns True if a change in attribute values should cause a rebuild of the complete shading effect.

		This method will be called by Maya when it detects changes in the attribute values of nodes in the shading network.
		If this method returns True, Maya will assume that the change means that a new configuration of the total fragment graph
		is necessary and it will trigger a rebuild of the complete shading effect. This will cause fragmentName() to be invoked
		again at which point a different fragment name could be returned.

		For example, if a texture node has multiple modes, each implemented with a different fragment, then a change to the active
		mode would require the shading effect to be rebuilt in order to switch which fragment is used.

		The plug parameter passed in is Maya's best attempt at informing the implementation of what changed. However due to the
		nature of the change management system a single source plug cannot always be determined in which case the plug may be NULL.

		The default implementation returns False.

		* plug (MPlug) - The plug that changed, may be None."""
class MPxSubSceneOverride:
	"""Base class for Viewport 2.0 drawing of DAG nodes which represent sub-scenes."""
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def areUIDrawablesDirty(self)->bool:
		"""areUIDrawablesDirty() -> bool

		Determines whether addUIDrawables() should be called on the next refresh.

		Return  True if addUIDrawables() should be called on the next refresh, false if not.The default is true.

		If you've overridden addUIDrawables() then at the start of each refresh Maya willdestroy the drawables added in the previous refresh and call addUIDrawables() again.If you override this method to return false then Maya will preserve the UI drawablesfrom the previous refresh until either the DAG object associated with the override isdestroyed, or the override is deregistered."""
	def hasUIDrawables(self)->bool:
		"""hasUIDrawables() -> bool

		Return Whether addUIDrawables() will be called or not.

		In order for any override for the addUIDrawables() method to be calledthis method must also be overridden to return true.This method should not be overridden if addUIDrawables() has not alsobeen overridden as there may be associated wasted overhead."""
	def addUIDrawables(self,drawManager:Any,frameContext:Any)->int:
		"""addUIDrawables(drawManager, frameContext) -> int

		Provides access to a MUIDrawManager, which can be used to queue upoperations to draw simple UI shapes like lines, circles, text, etc.If you override this method you must also override hasUIDrawables()to return true, otherwise this method will not be called.If you are not going to override this function, please don't make 'hasUIDrawables()' return trueor there may be some wasted performance overhead.By default the drawables will persist until either the DAG object associated with the overrideis destroyed or the override is deregistered.If you don't want them to be redrawn on each refresh,override areUIDrawablesDirty() to return false.That will cause the drawables to be destroyedon next refresh and this method called again to replace them.

		drawManager The UI draw manager, it can be used to draw some simple geometry including text
		frameContext Frame level context information"""
	def setAllowTransparentInstances(self,renderItem:Any,transform:Any)->int:
		"""setAllowTransparentInstances(renderItem, transform) -> int

		Instancing is disabled automatically by default when the shader is transparent.This achieves the best appearance because Maya can sort individual instances.

		In some cases, performance is more important than appearance.e.g.particlesThis method allows to override the default behavior.

		renderItem The render item to operate on.
		allow Whether to allow instancing with transparent shader."""
	def addInstanceTransform(self,renderItem:MRenderItem,transform:om.MMatrix)->int:
		"""addInstanceTransform(renderItem, transform) -> int

		Returns The instance ID for the new instance. This ID can be used to change the matrix or remove it. A return value of 0 indicates an error (render item does not support instancing or invalid state). 0 is never a valid instance ID.

		Add an additional instance for a render item.  Will convert the MRenderItem to instanced rendering if not already done. The render item should already have it's other properties set (including shader and geometry).  A render item converted to instanced rendering will ignore its typical matrix from setMatrix().

		* renderItem (MRenderItem) - The render item to add a new instance to.
		* transform (MMatrix) - The transformation matrix of the new instance."""
	def furtherUpdateRequired(self,frameContext:MFrameContext)->bool:
		"""furtherUpdateRequired(frameContext) -> bool

		Returns True if further update is required. The default value return is False.

		This method is called by Maya following update() to allow the override to indicate whether further processing is required.

		If so, then requiresUpdate() and update() will be called again at a later time. In general this will occur when no active processing is occuring (when "idle").

		It is the responsibility of the plug-in to ensure that this method does not continuously request further updates as it may block the execution of other idle time events.

		* frameContext (MFrameContext) - Context information for the current frame."""
	def getSelectionPath(self,renderItem:MRenderItem,dagPath:Any)->bool:
		"""getSelectionPath(renderItem, dagPath) -> bool

		Returns True if a dag path was found for the render item.

		This method is called by Maya following selection to allow specifying the selection path for a single render item. It will be called once for each MRenderItem submitted in MPxSubSceneOverride.update() that intersects the selection frustum. If none of the MRenderItem intersects, then this callback will remain silent.

		When selection filtering is active, or in case of single click selection it is possible that the item will not be in the final selection list.

		The default implementation will return the first path to the associated DAG object. Specialization is required to provide support for multiple instances of the DAG object.

		Note: If your SubScene override plugin supports instancing, then you should overload getInstancedSelectionPath() instead to get all the necessary information to be able to return a proper path.

		* renderItem (MRenderItem) - Render item found inside the selection frustum.
		* dagPath [OUT] (MDagPath) - the MDagPath associated with the provided render item."""
	def getInstancedSelectionPath(self,renderItem:MRenderItem,intersection:MIntersection,dagPath:Any)->bool:
		"""getInstancedSelectionPath(renderItem, intersection, dagPath) -> bool

		Returns True if a dag path was found for the instantiable render item.

		This method is called by Maya following selection to allow specifying the selection path for a single instantiable render item. It is identical to getSelectionPath() but includes MIntersection information to properly distinguish between instances when the viewport is in GPU acceleration mode.

		In GPU acceleration mode, the renderItem will be the one of the master instance and the value of intersection.instanceID() will match the value returned by addInstanceTransform(). In regular non GPU accelerated mode, the renderItem will be the one directly associated with the instance. If intersection.instanceID() is equal to -1, then the geometry was not GPU accelerated.

		* renderItem (MRenderItem) - Render item found inside the selection frustum, or master item in GPU accelerated mode.
		* intersection (MIntersection) - Extra information to help find out how the render item got selected.
		* dagPath [OUT] (MDagPath) - the MDagPath associated with the provided render item."""
	@staticmethod
	def pointSnappingActive()->bool:
		"""pointSnappingActive() -> bool

		Returns True if selection has been launched to find snap points.
		To participate, you need to have at least one render item with point geometry
		and MSelectionMask.kSelectPointsForGravity set in MRenderItem.selectableMask().
		- The granularity must be set to MSelectionContext.kComponent in updateSelectionGranularity()
		- A component converter is not necessary in this scenario.
		- getSelectionPath() will not be called. All points present in the render item will be
		considered suitable locations for snapping."""
	def removeAllInstances(self,renderItem:MRenderItem)->Self:
		"""removeAllInstances(renderItem) -> self

		Remove all instances for a render item. This render item will remain set up for instancing and will render nothing until new instances are added.

		* renderItem (MRenderItem) - The render item to operate on."""
	def removeExtraInstanceData(self,renderItem:MRenderItem,parameterName:str)->Self:
		"""removeExtraInstanceData(renderItem, parameterName) -> self

		Remove an entire extra instance data stream from the instanced render item.

		* renderItem (MRenderItem) - The render item to operate on.
		* parameterName (string) - The name of the parameter associated with the extra instance data stream."""
	def removeInstance(self,renderItem:MRenderItem,instanceId:int)->Self:
		"""removeInstance(renderItem, instanceId) -> self

		Remove one instance of a render item.

		* renderItem (MRenderItem) - The render item to operate on.
		* instanceId (int) - The instance ID of the instance to remove. This must be a value returned by addInstanceTransform."""
	def requiresUpdate(self,container:MSubSceneContainer,frameContext:MFrameContext)->bool:
		"""requiresUpdate(container, frameContext) -> bool

		On each frame Maya will give each instantiated MPxSubSceneOverride object a chance to update its set of render items. Before beginning the update process for a specific override, Maya will first call this method to give the override a chance to indicate whether or not an update is necessary. If this method returns False, MPxSubSceneOverride.update() will not be called.

		The set of render items for this override must not be modified in this method.

		* container (MSubSceneContainer) - The container for this override
		* frameContext (MFrameContext) - Context information for the current frame

		Returns True if Maya should trigger the update process for this override"""
	def setExtraInstanceData(self,renderItem:MRenderItem,parameterName:str,data:om.MFloatArray,instanceId:int|None=None)->Self:
		"""setExtraInstanceData(renderItem, parameterName, data, instanceId=None) -> self

		Adds an extra stream of instanced data to an instanced render item. Once a render item has been instanced, additional per-instance data may be bound to a parameter on the shader for that item. Supported shader parameter types for instanced data include: float, float2, float3 and float4. Once a stream of instanced data is specified for a shader parameter, the original value of that parameter will be ignored in favor of the per-instance data specified in this method.

		If the render item has not been set up for instancing or if an invalid parameter was specified this method will fail. The size of the data array must be x*numberOfInstances where x is the size of the channel (1-4). If the size is wrong, the method will fail.

		More than one stream of extra instance data may be specified for an instanced render item. The number of streams will be limited by the number of texture co-ordinate channels available from the underlying graphics system (and note that the instanced matrix occupies four streams). If too many streams are used then a red error shader will be displayed instead of the expected shader.

		* renderItem (MRenderItem) - The render item to operate on.
		* parameterName (string) - The name of the parameter on the shader to fill with the instanced data.
		* data (MFloatArray) - The instanced data stream.
		* instanceId (int) - The instance ID of the instance to set the data for."""
	def setGeometryForRenderItem(self,renderItem:MRenderItem,vertexBuffers:MVertexBufferArray,indexBuffer:MIndexBuffer|None=None,objectBox:om.MBoundingBox|None=None)->Self:
		"""setGeometryForRenderItem(renderItem, vertexBuffers, indexBuffer=None, objectBox=None) -> self

		Call this method to provide the geometry for a render item. Although the render item will add a reference to each buffer, ultimate ownership of the geometric data remains with the caller. This method may only be called on render items which have been generated by this override and it may only be called during update(). Buffers may be shared among multiple render items. This method will replace any geometry currently associated with the render item with the newly provided geometry.

		The bounding box parameter to this method is optional. If None, Maya will attempt to calculate the box automatically. Note that this may require a read-back of vertex data from the graphics card which can be a very slow operation. It is better to supply a correct bounding box whenever possible.

		It is the responsibility of the caller to ensure that the buffers provided fulfill the geometry requirements of the shader for the render item. If the requirements are not met, the render item will not draw. If there is no shader assigned to the render item, this method will fail.

		When a geometry is completely defined by its vertex buffers, like when drawing all points in a MGeometry.kPoints render item, it is possible to provide an empty MIndexBuffer or None for the indexBuffer parameter. The geometry will then be drawn using a non-indexed draw call like glDrawArrays() or ID3D11DeviceContext::Draw().

		* renderItem (MRenderItem) - The render item to provide geometry for.
		* vertexBuffers (MVertexBufferArray) - The vertex buffers for the geometry.
		* indexBuffer (MIndexBuffer) - The index buffer for the geometry, may be None.
		* objectBox (MBoundingBox) - Object-space bounding box, may be None."""
	def setInstanceTransformArray(self,renderItem:MRenderItem,matrixArray:om.MMatrixArray)->Self:
		"""setInstanceTransformArray(renderItem, matrixArray) -> self

		Sets the entire instance array for a render item.  Will convert the MRenderItem to instanced rendering if not already done.  Any pre-existing instances will be removed. The render item should already have it's other properties set (including shader and geometry). A render item converted to instanced rendering will ignore its typical matrix from setMatrix().
		This function is provided as a simpler alternative to addInstanceTransform() for when the ability to update or remove individual instances is not required. However additional instances may still be added via addInstanceTransform() and those may be individually updated or removed.

		* renderItem (MRenderItem) - The render item to set the instance matrix array for.
		* matrixArray (MMatrixArray) - The transformation matrix array for all the instances."""
	def supportedDrawAPIs(self)->DrawAPI:
		"""supportedDrawAPIs() -> DrawAPI

		Returns the draw API supported by this override."""
	def update(self,container:MSubSceneContainer,frameContext:MFrameContext)->Self:
		"""update(container, frameContext) -> self

		This method is called by Maya on each frame as long as the implementation of MPxSubSceneOverride.requiresUpdate() returns True. In this method, the MSubSceneContainer should be populated with the render items that are required to draw the associated DAG object. The render items will remain in the container until they are explicitly removed or the associated object is deleted. Render items in the container may also be modified at this time.

		All render items in the container upon completion of this method will be processed for drawing. Any such items which pass all filtering tests for the active viewport will draw. At a minimum, render items must be enabled, have a valid shader and valid geometry in order to draw in Viewport 2.0.

		It is the responsibility of this method to call MRenderer.setLightsAndShadowsDirty() to trigger recomputation of any shadow maps in the scene (if required).

		* container (MSubSceneContainer) - The container for this override
		* frameContext (MFrameContext) - Context information for the current frame"""
	def updateInstanceTransform(self,renderItem:MRenderItem,instanceId:int,transform:om.MMatrix)->Self:
		"""updateInstanceTransform(renderItem, instanceId, transform) -> self

		Update the instance transform matrix for one instance of a render item.

		* renderItem (MRenderItem) - The render item to operate on.
		* instanceId (int) - The instance ID of the instance to update. This must be a value returned by addInstanceTransform.
		* transform (MMatrix) - The new transformation matrix for the instance."""
	def updateSelectionGranularity(self,path:Any,selectionContext:Any)->Self:
		"""updateSelectionGranularity(path, selectionContext) -> self

		This method is called during the pre-filtering phase of the viewport 2.0 selection and is used to allow derived classes to modify the selection context of the given DAG object.

		This is useful to specify the selection level, which defines what can be selected on the object :
		  MSelectionContext.kNone        Nothing can be selected
		  MSelectionContext.kObject      Object can be selected as a whole
		  MSelectionContext.kComponent   Parts of the object - such as vertex, edge or face - are selectable
		This is used to discard objects that are not selectable given the current selection mode (see MGlobal.selectionMode()).

		Implementation of this method here is empty, and default selection level is set to kObject.

		 path (MDagPath) - The path to the instance to update the selection context for
		 selectionContext [OUT] (MSelectionContext) - The selection context"""
class MPxSurfaceShadingNodeOverride(MPxShadingNodeOverride):
	"""Base class for user defined surface shading node overrides."""
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def bumpAttribute(self)->str:
		"""bumpAttribute() -> string

		Returns the name of the attribute that accepts bump connections from bump nodes.

		This method is called after getCustomMappings() to allow the plugin to provide surface-shader specific information.
		If required, the override may return the name of the attribute on the node that accepts connections from bump nodes for
		doing bump or normal mapping (often this is "normalCamera"). A special mapping will be created linking this attribute
		to the parameter named "Nw" (world space normal) on the fragment. The special mapping will ensure that the extra fragments
		needed for bump mapping are set up correctly. If there is no "Nw" parameter on the fragment the mapping will not be created
		and bump mapping will not work for the associated shader.

		The default implementation returns the empty string (no bump)."""
	def primaryColorParameter(self)->str:
		"""primaryColorParameter() -> string

		Returns the name of the fragment parameter to use as the primary color.

		This method is called just after getCustomMappings() to allow the plugin to provide extra surface shader-specific
		information. If required, the override may return the name of a 3-float parameter on the fragment that should be marked
		as the primary color. If the viewport is set to hide textures (shaded mode) then the specified parameter will be set
		using the "default color" value from the texture which is connected to the associated attribute on the Maya node.

		The default implementation returns the empty string (no primary color).

		The name must correspond to a parameter on the fragment that is mapped to an attribute on the node either automatically
		or through custom attribute parameter mappings."""
	def transparencyParameter(self)->str:
		"""transparencyParameter() -> string

		Returns the name of the fragment parameter that should drive transparency.

		This method is called just after getCustomMappings() to allow the plugin to provide extra surface shader-specific
		information. If required, the override may return the name of a single float or 3-float parameter on the fragment that
		should be marked as the parameter that drives the transparency of the surface shader. The values of this parameter will
		be watched so that scene objects using this shader will be correctly marked and sorted for transparent drawing.

		The default implementation returns the empty string (no transparency).

		The name must correspond to a parameter on the fragment that is mapped to an attribute on the node either automatically
		or through custom attribute parameter mappings."""
class MPxVertexBufferGenerator:
	"""Base class for user defined vertex buffer generators."""
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def createVertexStream(self,object:om.MObject,vertexBuffer:Any,targetIndexing:MComponentDataIndexing,sharedIndexing:MComponentDataIndexing,sourceStreams:MVertexBufferArray)->Self:
		"""createVertexStream(object, vertexBuffer, targetIndexing, sharedIndexing, sourceStreams) -> self

		This method gets called to allow the generator to fill in the data for a custom vertex stream. Use the requirements in the vertexBuffer to get the description of the stream. Use vertexBuffer.acquire() and vertexBuffer.commit() to fill the buffer.

		* object (MObject) - The dag object being evaluated.
		* vertexBuffer [IN/OUT] (MVertexBuffer) - The vertex buffer to fill.
		* targetIndexing (MComponentDataIndexing) - Vertex index mapping from targetIndexing.getComponentType() space to vertex buffer space.
		* sharedIndexing (MComponentDataIndexing) - Vertex index mapping in the declared MComponentDataIndexing::MComponentType space.
		* sourceStreams (MVertexBufferArray) - Array of Vertex Buffers that can be used to create the new stream."""
	def getSourceIndexing(self,object:om.MObject,sourceIndexing:Any)->Self:
		"""getSourceIndexing(object, sourceIndexing) -> self

		This function is called to allow the vertex buffer generator to provide its vertex indexing information as well as the space the vertices are in.  The indexing and the component type are stored in the  sourceIndexing argument.  This indexing information is to allow the system to identify any potential  vertex sharing that is common across all vertex requirements.

		* object (MObject) - The object being evaluated.
		* sourceIndexing [OUT] (MComponentDataIndexing) - Vertex index mapping in the declared MComponentDataIndexing::MComponentType space."""
	def getSourceStreams(self,object:om.MObject,sourceStreams:Any)->Self:
		"""getSourceStreams(object, sourceStreams) -> self

		This function is called to allow the vertex buffer generator to provide the list of stream names that it requires. The names will be used to fill the array of vertex buffers that will be passed to createVertexStream.

		* object (MObject) - The dag object being evaluated.
		* sourceStreams [OUT] (list of strings) - Array of strings."""
class MPxVertexBufferMutator:
	"""Base class for user defined vertex buffer generators."""
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def modifyVertexStream(self,object:om.MObject,vertexBuffer:Any,targetIndexing:MComponentDataIndexing)->Self:
		"""modifyVertexStream(object, vertexBuffer, targetIndexing) -> self

		This method gets called to allow the mutator to alter the data for a custom vertex stream.
		Use the requirements in the vertexBuffer to get the description of the stream.
		Use vertexBuffer.aquire() and vertexBuffer.commit() to fill the buffer.

		* object (MObject) - The object being evaluated.
		* vertexBuffer [IN/OUT] (MVertexBuffer) - The vertex buffer to alter.
		* targetIndexing (MComponentDataIndexing) - Vertex index mapping from targetIndexing.getComponentType() space to vertex buffer space."""
class MQuadRender(MRenderOperation):
	"""Class which defines a 2d geometry quad render."""
	@property
	def mClearOperation(self)->Any:
		"""Clear operation"""
	@mClearOperation.setter
	def mClearOperation(self,value:Any)->None:...
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def blendStateOverride(self)->MBlendState:
		"""blendStateOverride() -> MBlendState

		Query if a blend state override is performed by this quad operation."""
	def clearOperation(self)->MClearOperation:
		"""clearOperation() -> MClearOperation

		Get the scene clear operation."""
	def depthStencilStateOverride(self)->MDepthStencilState:
		"""depthStencilStateOverride() -> MDepthStencilState

		Query if a depth-stencil state override is performed by this quad operation."""
	def rasterizerStateOverride(self)->MRasterizerState:
		"""rasterizerStateOverride() -> MRasterizerState

		Query if a rasterizer state override is performed by this quad operation."""
	def shader(self)->MShaderInstance:
		"""shader() -> MShaderInstance

		Get the shader to use when rendering a quad."""
class MRasterizerState:
	"""Container class for an acquired complete GPU rasterizer state."""
	kFillSolid:int=3
	kFillWireFrame:int=2
	kCullNone:int=1
	kCullFront:int=2
	kCullBack:int=3
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def desc(self)->MRasterizerStateDesc:
		"""desc() -> MRasterizerStateDesc

		Get the rasterizer state descriptor that was used to create the state object."""
	def resourceHandle(self)->int:
		"""resourceHandle() -> long

		Returns a long containing a C++ 'void' pointer which points to the draw API dependent handle for a rasterizer state.
		For OpenGL, such a handle does not exist and a NULL pointer will be returned.
		For DirectX, a pointer to a Direct3D state will be returned."""
class MRasterizerStateDesc:
	"""Descriptor for a complete rasterizer state."""
	@property
	def fillMode(self)->Any:
		"""Select the primitive fill mode, default kFillSolid"""
	@fillMode.setter
	def fillMode(self,value:Any)->None:...
	@property
	def cullMode(self)->Any:
		"""Select the face culling mode, default kCullNone"""
	@cullMode.setter
	def cullMode(self,value:Any)->None:...
	@property
	def frontCounterClockwise(self)->Any:
		"""Select whether CW or CCW winding is used for "_CSTRfront" face, default false"""
	@frontCounterClockwise.setter
	def frontCounterClockwise(self,value:Any)->None:...
	@property
	def depthBiasIsFloat(self)->Any:
		"""Indicates that DepthBias is a float value, default false"""
	@depthBiasIsFloat.setter
	def depthBiasIsFloat(self,value:Any)->None:...
	@property
	def depthBias(self)->Any:
		"""DepthBias adds the given bias value to the rasterizer z value prior to depth testing"""
	@depthBias.setter
	def depthBias(self,value:Any)->None:...
	@property
	def depthBiasClamp(self)->Any:
		"""Maximum value scaled depth bias can attain, default 0"""
	@depthBiasClamp.setter
	def depthBiasClamp(self,value:Any)->None:...
	@property
	def slopeScaledDepthBias(self)->Any:
		"""Slope scaled depth bias value, default 0"""
	@slopeScaledDepthBias.setter
	def slopeScaledDepthBias(self,value:Any)->None:...
	@property
	def depthClipEnable(self)->Any:
		"""Enables HW automatic depth clipping, default true"""
	@depthClipEnable.setter
	def depthClipEnable(self,value:Any)->None:...
	@property
	def scissorEnable(self)->Any:
		"""Enables HW scissor clip rectangle, default false"""
	@scissorEnable.setter
	def scissorEnable(self,value:Any)->None:...
	@property
	def multiSampleEnable(self)->Any:
		"""Enables HW full screen multi-sample anti-aliasing, default false"""
	@multiSampleEnable.setter
	def multiSampleEnable(self,value:Any)->None:...
	@property
	def antialiasedLineEnable(self)->Any:
		"""Enables HW anti-aliased lines, auto disabled by multi-sample AA, default false"""
	@antialiasedLineEnable.setter
	def antialiasedLineEnable(self,value:Any)->None:...
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def setDefaults(self)->Self:
		"""setDefaults() -> self

		Set all values for the rasterizer state to their default values."""
class MRenderItem:
	"""A single renderable entity."""
	sDormantFilledDepthPriority:int=0
	sDormantWireDepthPriority:int=2
	sHiliteWireDepthPriority:int=4
	sActiveWireDepthPriority:int=5
	sActiveLineDepthPriority:int=9
	sDormantPointDepthPriority:int=14
	sActivePointDepthPriority:int=17
	sSelectionDepthPriority:int=21
	MaterialSceneItem:int=0
	NonMaterialSceneItem:int=1
	DecorationItem:int=2
	InternalItem:int=3
	InternalMaterialItem:int=4
	InternalTexturedMaterialItem:int=5
	InternalUnsupportedMaterialItem:int=6
	OverrideNonMaterialItem:int=7
	IgnoreDefaultMaterialMode:int=0
	DrawOnlyWhenDefaultMaterialActive:int=1
	SkipWhenDefaultMaterialActive:int=2
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def associateWithIndexBuffer(self,MIndexBuffer:Any)->bool:
		"""associateWithIndexBuffer(MIndexBuffer) -> bool

		Use to indicate that a particular index buffer should be used with this render item.
		This method must be called from MPxGeometryOverride in order to link index buffers generated in
		the MGeometry class with specific render items.
		Without an index buffer, a render item cannot draw."""
	def availableShaderParameters(self)->list[str]:
		"""availableShaderParameters() -> list of string

		Returns the list of available shader parameters.
		This is useful for OverrideNonMaterialItem to retrieve default parameters."""
	def boundingBox(self,space:Space=MSelectionContext.kObject)->om.MBoundingBox:
		"""boundingBox(space=kObject) -> MBoundingBox

		Returns the bounding box for the geometry data of the render item.
		Returns None if the render item is unbounded or does not have a valid associated geometry.

		* space (Space) - The requested space of the bounding box."""
	def setBoundingBox(self,bounds:om.MBoundingBox)->Self:
		"""setBoundingBox(bounds) -> self

		Sets the bounding box for the render item.


		* bounds (MBoundingBox) - The new bounding box."""
	def castsShadows(self)->bool:
		"""castsShadows() -> bool

		Get the castsShadows state of the render item."""
	def wantConsolidation(self)->bool:
		"""wantConsolidation() -> bool

		Return whether or not this render item wants to participate in consolidation."""
	def getDefaultMaterialHandling(self)->MRenderItem.DefaultMaterialFiltering:
		"""getDefaultMaterialHandling() -> MRenderItem.DefaultMaterialFiltering

		Returns whether or not this render item will draw when default material mode is active."""
	def isCompatibleWithMayaInstancer(self)->bool:
		"""isCompatibleWithMayaInstancer() -> bool

		Returns whether or not this render item can be used as an instance object with Maya Instancer node."""
	def component(self)->om.MObject:
		"""component() -> MObject

		Get the optional component for the render item if the render item representsthe drawing of a component as a result of per - face shader assignment, componentselection highlighting etc.

		If the render item doesn't represent the drawing of a component, then a nullMObject will be returned. Use the isNull() method of the MObject to check."""
	def shadingComponent(self)->om.MObject:
		"""shadingComponent() -> MObject

		Get the optional shading component for the render item. It is different fromthe component() method only when a view selected filter is applied.

		Therefore, a typical use of this method is to query the isolate selectedcomponent on a render item created by Viewport 2.0 when a 3D model viewactivates Isolate Select for components. See setAllowIsolateSelectCopy()for more information.

		If the render item doesn't represent the drawing of a shading component,then a null MObject will be returned. Use the isNull() method of the MObjectto check."""
	def setAllowIsolateSelectCopy(self,bool:bool)->Self:
		"""setAllowIsolateSelectCopy(bool) -> self

		When a 3D model view activates Isolate Select for components, Viewport 2.0will create and maintain necessary render items to represent the drawingof the isolate selected components specifically for that view. These renderitems are copies of their original items and thus have the same propertiesincluding name, type, primitive type, draw mode etc., but their shadingcomponents are filtered from the view selected set of that view.

		By default, a custom render item doesn't allow its copies to be created forthe drawing of isolate selected components; plug-ins should call the methodto allow this. When this is allowed and multiple views have view selectedsets, the render item can have multiple copies and each copy represents thedrawing in only one view.

		Viewport 2.0 is responsible to update these copies for any changes appliedto the original item and the view selected set. It is the duty of the plug-into retrieve the isolate selected components by calling the shadingComponent()method and populate the geometric buffers appropriately.

		The lifetime of the copies is managed by Viewport 2.0, thus it is not safefor plug-ins to cache their pointers."""
	def allowIsolateSelectCopy(self)->bool:
		"""allowIsolateSelectCopy() -> bool

		Returns whether or not the render item allows its copies to be created forthe drawing of isolate selected components.

		See setAllowIsolateSelectCopy() for more information."""
	def isIsolateSelectCopy(self)->bool:
		"""isIsolateSelectCopy() -> bool

		Returns whether or not the render item is a copy created to represent thedrawing of an isolate selected component.

		See setAllowIsolateSelectCopy() for more information."""
	@staticmethod
	@overload
	def create(name:str,type:int,primitive:int)->MRenderItem:
		"""create(name, type, primitive) -> MRenderItem
		create(item) -> MRenderItem

		Static MRenderItem creation utility.

		Create new render item:
		* name (string) - The name of the render item (should be non-empty).
		* type (int) - The type of the render item.
		* primitive (int) - The primitive type of the render item.

		See MRenderItem.type() for a list of valid render item types.
		Internal types are not allowed and will result no item being created.
		See MGeometry.primitiveString() for a list of valid primitive types.

		Create new render item and copy all parameters from the incoming MRenderItem:
		* item (MRenderItem) - The item to copy."""
	@overload
	@staticmethod
	def create(item:MRenderItem)->MRenderItem:
		"""create(name, type, primitive) -> MRenderItem
		create(item) -> MRenderItem

		Static MRenderItem creation utility.

		Create new render item:
		* name (string) - The name of the render item (should be non-empty).
		* type (int) - The type of the render item.
		* primitive (int) - The primitive type of the render item.

		See MRenderItem.type() for a list of valid render item types.
		Internal types are not allowed and will result no item being created.
		See MGeometry.primitiveString() for a list of valid primitive types.

		Create new render item and copy all parameters from the incoming MRenderItem:
		* item (MRenderItem) - The item to copy."""
	def customData(self)->om.MUserData:
		"""customData() -> MUserData

		Retrieve custom data from the render item, returns None if no such data has ever been set on the render item.

		    DEPRECATED in 2022, use getCustomData instead."""
	def getCustomData(self)->om.MUserData:
		"""getCustomData() -> MUserData

		Retrieve custom data from the render item, returns None if no such data has ever been set on the render item."""
	def depthPriority(self)->int:
		"""depthPriority() -> int

		Get the depth priority of the render item.
		The higher the depth priority the closer it will be drawn to the camera."""
	@staticmethod
	def destroy(item:Any)->None:
		"""destroy(item) -> None

		Static MRenderItem destruction utility.
		Destroys the internal data structures associated with this MRenderItem.
		Any attempt to use the MRenderItem after this will result in an exception."""
	def drawMode(self)->int:
		"""drawMode() -> int

		Get the draw mode for the render item.
		See MGeometry.drawModeString() for a list of valid draw modes."""
	def enable(self,bool:bool)->Self:
		"""enable(bool) -> self

		Enable or disable the render item for rendering."""
	def excludedFromPostEffects(self)->bool:
		"""excludedFromPostEffects() -> bool

		Get whether this item is excluded from post-effects like SSAO and depth-of-field."""
	def excludedFromDefaultMaterialOverride(self)->bool:
		"""excludedFromDefaultMaterialOverride() -> bool

		Get whether this item is excluded from the default material mode."""
	def geometry(self)->MGeometry:
		"""geometry() -> MGeometry

		Access full geometry data for the render item.
		Returns None if geometry has not been generated yet."""
	def getShader(self)->MShaderInstance:
		"""getShader() -> MShaderInstance

		Get the shader used by this render item.
		The return value may be None if no shader is set on the render item."""
	def getShaderParameters(self,name:str)->bool|int|float|tuple[float,...]:
		"""getShaderParameters(name) -> bool / int / float / tuple of floats

		Get the value of a shader parameter.
		This is useful for OverrideNonMaterialItem to retrieve default parameters.
		Use availableShaderParameters() to get the list of available parameters."""
	def isConsolidated(self)->bool:
		"""isConsolidated() -> bool

		Get the consolidated state of the render item."""
	def isEnabled(self)->bool:
		"""isEnabled() -> bool

		Get the enable state of the render item."""
	def isShaderFromNode(self)->bool:
		"""isShaderFromNode() -> bool

		Return True if the shader instance was set by evaluating the shading network of
		a surface shader node (either standard or custom) in the scene via setShaderFromNode()."""
	def name(self)->str:
		"""name() -> string

		Get the name of the render item."""
	def primitive(self)->int:
		"""primitive() -> int

		Get the primitive type drawn by the render item.
		See MGeometry.primitiveString() for a list of valid primitive types."""
	def primitiveAndStride(self)->list[int]:
		"""primitiveAndStride() -> [int, int]

		Get the primitive type drawn by the render item, as well as its stride.
		See MGeometry.primitiveString() for a list of valid primitive types."""
	def setPrimitive(self,int:int,int2:int)->Self:
		"""setPrimitive(int, int) -> self

		Set the primitive type of the render item. If it is kPatch, stride will be required to specify the number of control points per patch and the valid values are [1, 32]; otherwise stride won't be used.

		If this item is consolidated, invoking this method may cause this item to be reconsolidated.

		This method only affects items explicitly created by the plug-in."""
	def receivesShadows(self)->bool:
		"""receivesShadows() -> bool

		Get the receivesShadows state of the render item."""
	def requiredVertexBuffers(self)->MVertexBufferDescriptorList:
		"""requiredVertexBuffers() -> MVertexBufferDescriptorList

		Get a list of vertex buffer descriptors that describe the buffers required to draw the given render item.
		These are determined by the shader that will be used to draw the render item and so this method will return
		a non-empty list as long as there is a shader assigned to the render item."""
	def selectionMask(self)->om.MSelectionMask:
		"""selectionMask() -> MSelectionMask

		Get the render item selection mask."""
	def setCastsShadows(self,bool:bool)->Self:
		"""setCastsShadows(bool) -> self

		Set the castsShadows state of the render item."""
	def setWantConsolidation(self,bool:bool)->Self:
		"""setWantConsolidation(bool) -> self

		Set whether or not this render item wants to participate in consolidation.

		This method only affects items explicitly created by the plug-in. The value is true by default, unless the item is added to an MSubSceneContainer. When it is true, the geometry of compatible render items will be consolidated into a single render item, to provide better performance.

		Render items that are already instanced cannot be consolidated.

		For render items added to an MSubSceneContainer, if wantConsolidation is set to true, this will prevent them from being instanced until wantConsolidation is set to false."""
	def setDefaultMaterialHandling(self,arg:Any)->Self:
		"""setDefaultMaterialHandling(MRenderItem.DefaultMaterialFiltering) -> self

		Set whether or not this object should be drawn when default material mode is active.
		Set this to DrawOnlyWhenDefaultMaterialActive on render items dedicated to rendering a default material and set it to SkipWhenDefaultMaterialActive on regular shader items that should not draw in that mode.
		If a render item is to be drawn regardless of the mode, leave it at IgnoreDefaultMaterialMode."""
	def setCompatibleWithMayaInstancer(self,bool:bool)->Self:
		"""setCompatibleWithMayaInstancer(bool) -> self

		Set whether or not this render item can be used as an instance object with Maya Instancer node."""
	def setCustomData(self,MUserData:Any)->Self:
		"""setCustomData(MUserData) -> self

		Associate custom user data with this render item.
		If deleteAfterUse() is true on the data, then the data object will automatically be deleted when the render item is deleted.
		Otherwise, the lifetime of the user data object is the responsibility of the caller."""
	def setDepthPriority(self,int:int)->Self:
		"""setDepthPriority(int) -> self

		Set the depth priority of the render item.
		The higher the depth priority the closer it will be drawn to the camera."""
	def setDrawMode(self,int:int)->Self:
		"""setDrawMode(int) -> self

		Set the draw mode for the render item.
		If the draw mode is all, the render item will be drawn regardless of the viewport draw mode.
		Otherwise the render item will only be drawn when the viewport is set to draw objects in the specified mode.
		See MGeometry.drawModeString() for a list of valid draw modes."""
	def setExcludedFromPostEffects(self,bool:bool)->Self:
		"""setExcludedFromPostEffects(bool) -> self

		Set whether this item should be excluded from post-effects like SSAO and depth-of-field.
		Render items default to being excluded from post-effects."""
	def setExcludedFromDefaultMaterialOverride(self,bool:bool)->Self:
		"""setExcludedFromDefaultMaterialOverride(bool) -> self

		Set whether this item should be excluded from the default material mode.
		Default value is false (included)."""
	def setMatrix(self,MMatrix:Any)->bool:
		"""setMatrix(MMatrix) -> bool

		Override the object to world transformation matrix to use when drawing this render item.
		If unset, the render item will draw using the transformation matrix of the associated Maya DAG node.
		Pass None to this method to remove the override"""
	def setReceivesShadows(self,bool:bool)->Self:
		"""setReceivesShadows(bool) -> self

		Set the receivesShadows state of the render item."""
	@overload
	def setSelectionMask(self,mask:om.MSelectionMask)->Self:
		"""setSelectionMask(mask) -> selfsetSelectionMask(type) -> self

		Set the render item selection mask.

		* mask (MSelectionMask) - The selection mask.
		* type (int) - The selection type (see MSelectionMask.addMask() for a list of values)."""
	@overload
	def setSelectionMask(self,type:int)->Self:
		"""setSelectionMask(mask) -> selfsetSelectionMask(type) -> self

		Set the render item selection mask.

		* mask (MSelectionMask) - The selection mask.
		* type (int) - The selection type (see MSelectionMask.addMask() for a list of values)."""
	def setShader(self,shader:MShaderInstance,customStreamName:str|None=None)->bool:
		"""setShader(shader, customStreamName=None) -> bool

		Set shader to use when drawing this render item.
		If no shader is ever set the render item will not draw.
		The render item makes a copy of the instance so it is safe to delete the instance after
		assignment without affecting any render items the instance was assigned to.

		* shader (MShaderInstance) - The shader to use when drawing this item.
		* customStreamName (string) - If specified, shader will generate geometry requirements with the given name."""
	def setShaderFromNode(self,shaderNode:om.MObject,shapePath:om.MDagPath,linkLostCb:callable|None=None,linkLostUserData:om.MUserData|None=None,nonTextured:bool=False)->Self:
		"""setShaderFromNode(shaderNode, shapePath, linkLostCb=None, linkLostUserData=None, nonTextured=False) -> self

		Set shader to use when drawing this render item. If no shader is ever set this render item will not draw. This method sets the shader instance to a render item by evaluating the shading network of a surface shader node (either standard or custom) in the scene.

		This method only affects items explicitly created by the plug-in.

		If the surface shader node is None or supported by neither Maya nor the plug-in, this method will clear the shader assignment on the render item, which will thus not be drawn.

		The shape path is used as the object context for shading network evaluation to ensure that the shader instance fits its requirements. If the shape path is invalid (e.g. an empty path), a shader instance to fit basic requirements is created but will not include any geometry-dependent requirements.

		The linkLostCb will be invoked whenever the link to the surface shader node is lost. The link can be lost in a number of ways, e.g. shader nodes are deleted or shading network connections are modified. However, the linkLostCb won't be invoked for a change to shading group level connection; if needed, it is the DG node's responsibility to monitor any changes to shading group level connection by MPxNode::connectionMade and MPxNode::connectionBroken.

		There is no guarantee that the surface shader node is still valid after the link is lost. The linkLostCb should check the validity and assign the render item with a shader instance appropriately.

		After the shader instance is set, its parameter values can be automatically updated by Viewport 2.0 whenever the related shading attributes changed, therefore access to the shader instance is not provided in order to avoid unexpected behavior.

		 * shaderNode (MObject) - The surface shader node.
		 * shapePath (MDagPath) - The DAG path of a shape to be used as the object context for shading network evaluation.
		 * linkLostCb (callable) - Function to be invoked whenever the link to the surface shader node is lost.
		 * linkLostUserData (MUserData) - User supplied data to be passed into the link lost callback.
		 * nonTextured (bool) - Whether or not a non-textured effect instance is needed. The default value is false."""
	def setTreatAsTransparent(self,bool:bool)->Self:
		"""setTreatAsTransparent(bool) -> self

		Set whether or not this object should be treated as a transparent item.Set this to true if the object has vertex colors with alpha or other inputsthat make it important to treat this object as if it were transparent."""
	def setWantSubSceneConsolidation(self,bool:bool)->Self:
		"""setWantSubSceneConsolidation(bool) -> self

		Sets whether or not this render item is eligible for consolidation in sub scene overrides.

		Render items that are already instanced cannot be consolidated. Setting a render item to
		want sub scene consolidation will prevent the render item from being instanced."""
	def sourceDagPath(self)->om.MDagPath:
		"""sourceDagPath() -> MDagPath

		Retrieve the MDagPath for the instance of the object that generated this render item.

		 If there are many object instances contributing due to consolidation then only one dag path out of all the objects is returned.

		The method sourceIndexMapping() should be used if the item is consolidatedto access the corresponding dag paths for the objects making up this item."""
	def sourceIndexMapping(self)->MGeometryIndexMapping:
		"""sourceIndexMapping() -> MGeometryIndexMapping

		Get the geometry index mapping of the objects contained by this consolidated render item.
		Multiple geometries can be concatenated to improve rendering performance.
		You can access the index mapping of the geometries in order to render them separately.
		The index mapping gives you the name, and index start and length of each geometry."""
	def type(self)->int:
		"""type() -> int

		Get the type of the render item.

		  MRenderItem.MaterialSceneItem
		     A render item which represents an object in the scene that should interact with the rest of the scene and viewport settings (e.g. a shaded piece of geometry which should be considered in processes like shadow computation, viewport effects, etc.). Inclusion in such processes can also still be controlled through the appropriate methods provided by this class.
		  MRenderItem.NonMaterialSceneItem
		     A render item which represents an object in the scene that should not interact with the rest of the scene and viewport settings, but that is also not part of the viewport UI (e.g. a curve or a bounding box which should not be hidden when 'Viewport UI' is hidden but which should also not participate in processes like shadow computation, viewport effects, etc.).
		  MRenderItem.DecorationItem
		     A render item which should be considered to be part of the viewport UI (e.g. selection wireframe, components, etc.).
		  MRenderItem.InternalItem
		     A render item which was created by Maya for internal purposes (e.g. A render item created as the result of a shader being assigned to a DAG node).
		  MRenderItem.InternalMaterialItem
		                An internally created MaterialSceneItem for non-textured mode display.
		  MRenderItem.InternalTexturedMaterialItem
		     An internally created MaterialSceneItem for textured mode display.
		  MRenderItem.InternalUnsupportedMaterialItem
		     An internally created MaterialSceneItem for showing an unsupported material"""
	def wantSubSceneConsolidation(self)->bool:
		"""wantSubSceneConsolidation() -> bool

		Returns True if this render item is eligible for consolidation in sub scene overrides."""
	def objectTypeExclusionFlag(self)->int:
		"""objectTypeExclusionFlag() -> long

		Query the bit flag which is used in display filtering based on object types.
		See setObjectTypeExclusionFlag() for details."""
	def setObjectTypeExclusionFlag(self,long:Any)->Self:
		"""setObjectTypeExclusionFlag(long) -> self

		Set a bit flag for use in display filtering based on object types. The
		valid bit flags are defined in MFrameContext with names starting with
		"kExclude", except the following ones:

		 - MFrameContext.kExcludeGrid
		 - MFrameContext.kExcludeHoldOuts
		 - MFrameContext.kExcludePluginShapes
		 - MFrameContext.kExcludeHUD
		 - MFrameContext.kExcludeAll

		When a render item is assigned with a bit flag that has been excluded by
		the current view, the render item will be excluded from display. The
		default value is MFrameContext.kExcludeNone, meaning the info is not to be
		considered when determining whether the render item should be excluded.

		This method only affects items explicitly created by the plug-in.

		 * val (long) - A "kExclude" bit flag defined in MFrameContext"""
class MRenderItemList:
	"""A list of MRenderItem objects."""
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def __len__(self)->int:
		"""Return len(self)."""
	def __getitem__(self,index:int)->Any:
		"""Return self[key]."""
	def append(self,MVertexBufferDescriptor:Any)->bool:
		"""append(MVertexBufferDescriptor) -> bool

		Add the item to the list. The list assumes ownership of the item."""
	def clear(self)->Self:
		"""clear() -> self

		Clear the list."""
	@overload
	def indexOf(self,name:str)->int:
		"""indexOf(name) -> int
		indexOf(name, type) -> int
		indexOf(name, primitive, mode) -> int

		Find the index of the first render item in the list matching the given search parameters.

		* name (string) - The name of the render item.
		* type (int) - The type of the render item.
		* primitive (int) - The primitive type of the render item.
		* mode (int) - The draw mode of the render item.

		See MRenderItem.type() for a list of valid render item types.
		See MGeometry.primitiveString() for a list of valid primitive types.
		See MGeometry.drawModeString() for a list of valid draw modes."""
	@overload
	def indexOf(self,name:str,type:int)->int:
		"""indexOf(name) -> int
		indexOf(name, type) -> int
		indexOf(name, primitive, mode) -> int

		Find the index of the first render item in the list matching the given search parameters.

		* name (string) - The name of the render item.
		* type (int) - The type of the render item.
		* primitive (int) - The primitive type of the render item.
		* mode (int) - The draw mode of the render item.

		See MRenderItem.type() for a list of valid render item types.
		See MGeometry.primitiveString() for a list of valid primitive types.
		See MGeometry.drawModeString() for a list of valid draw modes."""
	@overload
	def indexOf(self,name:str,primitive:int,mode:int)->int:
		"""indexOf(name) -> int
		indexOf(name, type) -> int
		indexOf(name, primitive, mode) -> int

		Find the index of the first render item in the list matching the given search parameters.

		* name (string) - The name of the render item.
		* type (int) - The type of the render item.
		* primitive (int) - The primitive type of the render item.
		* mode (int) - The draw mode of the render item.

		See MRenderItem.type() for a list of valid render item types.
		See MGeometry.primitiveString() for a list of valid primitive types.
		See MGeometry.drawModeString() for a list of valid draw modes."""
	def remove(self,index:int)->bool:
		"""remove(index) -> bool

		Remove the item at the specified index. Item is deleted."""
class MRenderOperation:
	"""Class which defines a rendering operation."""
	kClear:int=0
	kSceneRender:int=1
	kQuadRender:int=2
	kUserDefined:int=3
	kDataServer:int=4
	kHUDRender:int=5
	kPresentTarget:int=6
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def enableSRGBWrite(self)->bool:
		"""enableSRGBWrite() -> bool

		Return whether to enable GPU based gamma correction during pixel writes."""
	def name(self)->str:
		"""name() -> string

		Returns the name of the render operator."""
	def operationType(self)->int:
		"""operationType() -> int

		Returns the type of a render operator."""
	def targetOverrideList(self)->list[MRenderTarget]:
		"""targetOverrideList() -> list of MRenderTarget

		Return a list of render target which will be used as the target overrides for the operation."""
	def viewportRectangleOverride(self)->om.MFloatPoint:
		"""viewportRectangleOverride() -> MFloatPoint

		Query for a viewport rectangle override."""
class MRenderOverride:
	"""Class which defines a 2d geometry quad render."""
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def cleanup(self)->Self:
		"""cleanup() -> self

		Perform any cleanup required following the execution of render operations."""
	def name(self)->str:
		"""name() -> string

		Returns the name of the override."""
	def nextRenderOperation(self)->bool:
		"""nextRenderOperation() -> bool

		Iterate to the next operation. If there are no more operations then this method should return false."""
	def renderOperation(self)->MRenderOperation:
		"""renderOperation() -> MRenderOperation

		Return the current operation being iterated over."""
	def setup(self,destination:Any)->Self:
		"""setup(destination) -> self

		Perform any setup required before render operations are to be executed."""
	def startOperationIterator(self)->bool:
		"""startOperationIterator() -> bool

		Query if there are any operations to iterate over."""
	def supportedDrawAPIs(self)->int:
		"""supportedDrawAPIs() -> int

		Returns the draw APIs supported by this override.
		See MRenderer.drawAPI() description for the list of draw APIs."""
	def uiName(self)->str:
		"""uiName() -> string

		Returns the user interface name for the override."""
	def getFrameContext(self)->MFrameContext:
		"""getFrameContext() -> MFrameContext

		Return a frame context. The context is not available if called before setup() or after cleanup().
		The context should never be deleted by the plug-in as it is owned by the render override."""
	def select(self,frameContext:Any,selectInfo:Any,useDepth:Any,selectionList:Any,worldSpaceHitPts:Any)->bool:
		"""select(frameContext, selectInfo, useDepth, selectionList, worldSpaceHitPts) -> bool

		The method is called by Maya to override the default Viewport 2.0 selection. It returns false by default, meaning the default selection will be used. If an implementation returns true, selectionList and worldSpaceHitPts will be used to override the default selection.

		A complete implementation requires hit testing and selection interpretation. If an object is hit, the implementation should add its DAG path (and also its component when appropriate) to selectionList and add the world-space hit point between the selected item and selection ray to worldSpaceHitPts. The number of elements in selectionList and worldSpaceHitPts must be the same in any case, a selected item (typically a vertex component) and a hit point at the same array index will be associated.

		If the method is triggered for point snapping, the implementation needs to sort the hit points and return the one nearest to the cursor. The state of point snapping can be queried from selectInfo.

		When an implementation returns true to override the default behavior, the object-level selection override methods won't be triggered any more:

		* MPxGeometryOverride::refineSelectionPath * MPxSubSceneOverride::getInstancedSelectionPath * MPxDrawOverride::userSelect * MPxDrawOverride::refineSelectionPath

		* frameContext [IN] (MFrameContext) - The frame-level context information
		* selectInfo [IN] (MSelectionInfo) - The selection info
		* useDepth [IN] (bool) - Whether only the objects nearest to camera can be selected
		* selectionList [OUT] (MSelectionList) - List of items selected by this method
		* worldSpaceHitPts [OUT] (MPointArray) - List of hit points"""
class MRenderParameters:
	"""Base class for render operation functionsets."""
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def isArrayParameter(self,string:Any)->bool:
		"""isArrayParameter(string) -> bool

		Determine whether the named parameter is an array."""
	def parameterList(self)->list[str]:
		"""parameterList() -> list of string

		Get the names of all parameters that are settable on this shader instance."""
	def parameterType(self,string:Any)->int:
		"""parameterType(string) -> int

		Get the type of the named parameter, returns kInvalid if parameter is not found."""
	def semantic(self,string:Any)->str:
		"""semantic(string) -> string

		Return the semantic for a named parameter."""
	@overload
	def setArrayParameter(self,parameterName:str,arg:Sequence[bool],int:int)->Self:
		"""setArrayParameter(parameterName, sequence of bool, int) -> self
		setArrayParameter(parameterName, sequence of int, int) -> self
		setArrayParameter(parameterName, sequence of float, int) -> self
		setArrayParameter(parameterName, sequence of MMatrix, int) -> self

		Set the value of a named array parameter."""
	@overload
	def setArrayParameter(self,parameterName:str,arg:Sequence[int],int:int)->Self:
		"""setArrayParameter(parameterName, sequence of bool, int) -> self
		setArrayParameter(parameterName, sequence of int, int) -> self
		setArrayParameter(parameterName, sequence of float, int) -> self
		setArrayParameter(parameterName, sequence of MMatrix, int) -> self

		Set the value of a named array parameter."""
	@overload
	def setArrayParameter(self,parameterName:str,arg:Sequence[float],int:int)->Self:
		"""setArrayParameter(parameterName, sequence of bool, int) -> self
		setArrayParameter(parameterName, sequence of int, int) -> self
		setArrayParameter(parameterName, sequence of float, int) -> self
		setArrayParameter(parameterName, sequence of MMatrix, int) -> self

		Set the value of a named array parameter."""
	@overload
	def setArrayParameter(self,parameterName:str,arg:Sequence[om.MMatrix],int:int)->Self:
		"""setArrayParameter(parameterName, sequence of bool, int) -> self
		setArrayParameter(parameterName, sequence of int, int) -> self
		setArrayParameter(parameterName, sequence of float, int) -> self
		setArrayParameter(parameterName, sequence of MMatrix, int) -> self

		Set the value of a named array parameter."""
	@overload
	def setParameter(self,parameterName:str,bool:bool)->Self:
		"""setParameter(parameterName, bool) -> self
		setParameter(parameterName, int) -> self
		setParameter(parameterName, float) -> self
		setParameter(parameterName, list of float) -> self
		setParameter(parameterName, MFloatVector) -> self
		setParameter(parameterName, MMatrix) -> self
		setParameter(parameterName, MFloatMatrix) -> self
		setParameter(parameterName, MTextureAssignment) -> self
		setParameter(parameterName, MRenderTargetAssignment) -> self
		setParameter(parameterName, MSamplerState) -> self

		Set the value of the named parameter."""
	@overload
	def setParameter(self,parameterName:str,int:int)->Self:
		"""setParameter(parameterName, bool) -> self
		setParameter(parameterName, int) -> self
		setParameter(parameterName, float) -> self
		setParameter(parameterName, list of float) -> self
		setParameter(parameterName, MFloatVector) -> self
		setParameter(parameterName, MMatrix) -> self
		setParameter(parameterName, MFloatMatrix) -> self
		setParameter(parameterName, MTextureAssignment) -> self
		setParameter(parameterName, MRenderTargetAssignment) -> self
		setParameter(parameterName, MSamplerState) -> self

		Set the value of the named parameter."""
	@overload
	def setParameter(self,parameterName:str,float:float)->Self:
		"""setParameter(parameterName, bool) -> self
		setParameter(parameterName, int) -> self
		setParameter(parameterName, float) -> self
		setParameter(parameterName, list of float) -> self
		setParameter(parameterName, MFloatVector) -> self
		setParameter(parameterName, MMatrix) -> self
		setParameter(parameterName, MFloatMatrix) -> self
		setParameter(parameterName, MTextureAssignment) -> self
		setParameter(parameterName, MRenderTargetAssignment) -> self
		setParameter(parameterName, MSamplerState) -> self

		Set the value of the named parameter."""
	@overload
	def setParameter(self,parameterName:str,arg:list[float])->Self:
		"""setParameter(parameterName, bool) -> self
		setParameter(parameterName, int) -> self
		setParameter(parameterName, float) -> self
		setParameter(parameterName, list of float) -> self
		setParameter(parameterName, MFloatVector) -> self
		setParameter(parameterName, MMatrix) -> self
		setParameter(parameterName, MFloatMatrix) -> self
		setParameter(parameterName, MTextureAssignment) -> self
		setParameter(parameterName, MRenderTargetAssignment) -> self
		setParameter(parameterName, MSamplerState) -> self

		Set the value of the named parameter."""
	@overload
	def setParameter(self,parameterName:str,MFloatVector:Any)->Self:
		"""setParameter(parameterName, bool) -> self
		setParameter(parameterName, int) -> self
		setParameter(parameterName, float) -> self
		setParameter(parameterName, list of float) -> self
		setParameter(parameterName, MFloatVector) -> self
		setParameter(parameterName, MMatrix) -> self
		setParameter(parameterName, MFloatMatrix) -> self
		setParameter(parameterName, MTextureAssignment) -> self
		setParameter(parameterName, MRenderTargetAssignment) -> self
		setParameter(parameterName, MSamplerState) -> self

		Set the value of the named parameter."""
	@overload
	def setParameter(self,parameterName:str,MMatrix:Any)->Self:
		"""setParameter(parameterName, bool) -> self
		setParameter(parameterName, int) -> self
		setParameter(parameterName, float) -> self
		setParameter(parameterName, list of float) -> self
		setParameter(parameterName, MFloatVector) -> self
		setParameter(parameterName, MMatrix) -> self
		setParameter(parameterName, MFloatMatrix) -> self
		setParameter(parameterName, MTextureAssignment) -> self
		setParameter(parameterName, MRenderTargetAssignment) -> self
		setParameter(parameterName, MSamplerState) -> self

		Set the value of the named parameter."""
	@overload
	def setParameter(self,parameterName:str,MFloatMatrix:Any)->Self:
		"""setParameter(parameterName, bool) -> self
		setParameter(parameterName, int) -> self
		setParameter(parameterName, float) -> self
		setParameter(parameterName, list of float) -> self
		setParameter(parameterName, MFloatVector) -> self
		setParameter(parameterName, MMatrix) -> self
		setParameter(parameterName, MFloatMatrix) -> self
		setParameter(parameterName, MTextureAssignment) -> self
		setParameter(parameterName, MRenderTargetAssignment) -> self
		setParameter(parameterName, MSamplerState) -> self

		Set the value of the named parameter."""
	@overload
	def setParameter(self,parameterName:str,MTextureAssignment:Any)->Self:
		"""setParameter(parameterName, bool) -> self
		setParameter(parameterName, int) -> self
		setParameter(parameterName, float) -> self
		setParameter(parameterName, list of float) -> self
		setParameter(parameterName, MFloatVector) -> self
		setParameter(parameterName, MMatrix) -> self
		setParameter(parameterName, MFloatMatrix) -> self
		setParameter(parameterName, MTextureAssignment) -> self
		setParameter(parameterName, MRenderTargetAssignment) -> self
		setParameter(parameterName, MSamplerState) -> self

		Set the value of the named parameter."""
	@overload
	def setParameter(self,parameterName:str,MRenderTargetAssignment:Any)->Self:
		"""setParameter(parameterName, bool) -> self
		setParameter(parameterName, int) -> self
		setParameter(parameterName, float) -> self
		setParameter(parameterName, list of float) -> self
		setParameter(parameterName, MFloatVector) -> self
		setParameter(parameterName, MMatrix) -> self
		setParameter(parameterName, MFloatMatrix) -> self
		setParameter(parameterName, MTextureAssignment) -> self
		setParameter(parameterName, MRenderTargetAssignment) -> self
		setParameter(parameterName, MSamplerState) -> self

		Set the value of the named parameter."""
	@overload
	def setParameter(self,parameterName:str,MSamplerState:Any)->Self:
		"""setParameter(parameterName, bool) -> self
		setParameter(parameterName, int) -> self
		setParameter(parameterName, float) -> self
		setParameter(parameterName, list of float) -> self
		setParameter(parameterName, MFloatVector) -> self
		setParameter(parameterName, MMatrix) -> self
		setParameter(parameterName, MFloatMatrix) -> self
		setParameter(parameterName, MTextureAssignment) -> self
		setParameter(parameterName, MRenderTargetAssignment) -> self
		setParameter(parameterName, MSamplerState) -> self

		Set the value of the named parameter."""
	@overload
	def getParameter(self,parameterName:str,bool:bool)->Self:
		"""getParameter(parameterName, bool) -> self
		getParameter(parameterName, int) -> self
		getParameter(parameterName, float) -> self
		getParameter(parameterName, list of float) -> self
		getParameter(parameterName, MFloatVector) -> self
		getParameter(parameterName, MMatrix) -> self
		getParameter(parameterName, MFloatMatrix) -> self
		getParameter(parameterName, MTextureAssignment) -> self
		getParameter(parameterName, MRenderTargetAssignment) -> self
		getParameter(parameterName, MSamplerStateDesc) -> self

		Get the value of the named parameter."""
	@overload
	def getParameter(self,parameterName:str,int:int)->Self:
		"""getParameter(parameterName, bool) -> self
		getParameter(parameterName, int) -> self
		getParameter(parameterName, float) -> self
		getParameter(parameterName, list of float) -> self
		getParameter(parameterName, MFloatVector) -> self
		getParameter(parameterName, MMatrix) -> self
		getParameter(parameterName, MFloatMatrix) -> self
		getParameter(parameterName, MTextureAssignment) -> self
		getParameter(parameterName, MRenderTargetAssignment) -> self
		getParameter(parameterName, MSamplerStateDesc) -> self

		Get the value of the named parameter."""
	@overload
	def getParameter(self,parameterName:str,float:float)->Self:
		"""getParameter(parameterName, bool) -> self
		getParameter(parameterName, int) -> self
		getParameter(parameterName, float) -> self
		getParameter(parameterName, list of float) -> self
		getParameter(parameterName, MFloatVector) -> self
		getParameter(parameterName, MMatrix) -> self
		getParameter(parameterName, MFloatMatrix) -> self
		getParameter(parameterName, MTextureAssignment) -> self
		getParameter(parameterName, MRenderTargetAssignment) -> self
		getParameter(parameterName, MSamplerStateDesc) -> self

		Get the value of the named parameter."""
	@overload
	def getParameter(self,parameterName:str,arg:list[float])->Self:
		"""getParameter(parameterName, bool) -> self
		getParameter(parameterName, int) -> self
		getParameter(parameterName, float) -> self
		getParameter(parameterName, list of float) -> self
		getParameter(parameterName, MFloatVector) -> self
		getParameter(parameterName, MMatrix) -> self
		getParameter(parameterName, MFloatMatrix) -> self
		getParameter(parameterName, MTextureAssignment) -> self
		getParameter(parameterName, MRenderTargetAssignment) -> self
		getParameter(parameterName, MSamplerStateDesc) -> self

		Get the value of the named parameter."""
	@overload
	def getParameter(self,parameterName:str,MFloatVector:Any)->Self:
		"""getParameter(parameterName, bool) -> self
		getParameter(parameterName, int) -> self
		getParameter(parameterName, float) -> self
		getParameter(parameterName, list of float) -> self
		getParameter(parameterName, MFloatVector) -> self
		getParameter(parameterName, MMatrix) -> self
		getParameter(parameterName, MFloatMatrix) -> self
		getParameter(parameterName, MTextureAssignment) -> self
		getParameter(parameterName, MRenderTargetAssignment) -> self
		getParameter(parameterName, MSamplerStateDesc) -> self

		Get the value of the named parameter."""
	@overload
	def getParameter(self,parameterName:str,MMatrix:Any)->Self:
		"""getParameter(parameterName, bool) -> self
		getParameter(parameterName, int) -> self
		getParameter(parameterName, float) -> self
		getParameter(parameterName, list of float) -> self
		getParameter(parameterName, MFloatVector) -> self
		getParameter(parameterName, MMatrix) -> self
		getParameter(parameterName, MFloatMatrix) -> self
		getParameter(parameterName, MTextureAssignment) -> self
		getParameter(parameterName, MRenderTargetAssignment) -> self
		getParameter(parameterName, MSamplerStateDesc) -> self

		Get the value of the named parameter."""
	@overload
	def getParameter(self,parameterName:str,MFloatMatrix:Any)->Self:
		"""getParameter(parameterName, bool) -> self
		getParameter(parameterName, int) -> self
		getParameter(parameterName, float) -> self
		getParameter(parameterName, list of float) -> self
		getParameter(parameterName, MFloatVector) -> self
		getParameter(parameterName, MMatrix) -> self
		getParameter(parameterName, MFloatMatrix) -> self
		getParameter(parameterName, MTextureAssignment) -> self
		getParameter(parameterName, MRenderTargetAssignment) -> self
		getParameter(parameterName, MSamplerStateDesc) -> self

		Get the value of the named parameter."""
	@overload
	def getParameter(self,parameterName:str,MTextureAssignment:Any)->Self:
		"""getParameter(parameterName, bool) -> self
		getParameter(parameterName, int) -> self
		getParameter(parameterName, float) -> self
		getParameter(parameterName, list of float) -> self
		getParameter(parameterName, MFloatVector) -> self
		getParameter(parameterName, MMatrix) -> self
		getParameter(parameterName, MFloatMatrix) -> self
		getParameter(parameterName, MTextureAssignment) -> self
		getParameter(parameterName, MRenderTargetAssignment) -> self
		getParameter(parameterName, MSamplerStateDesc) -> self

		Get the value of the named parameter."""
	@overload
	def getParameter(self,parameterName:str,MRenderTargetAssignment:Any)->Self:
		"""getParameter(parameterName, bool) -> self
		getParameter(parameterName, int) -> self
		getParameter(parameterName, float) -> self
		getParameter(parameterName, list of float) -> self
		getParameter(parameterName, MFloatVector) -> self
		getParameter(parameterName, MMatrix) -> self
		getParameter(parameterName, MFloatMatrix) -> self
		getParameter(parameterName, MTextureAssignment) -> self
		getParameter(parameterName, MRenderTargetAssignment) -> self
		getParameter(parameterName, MSamplerStateDesc) -> self

		Get the value of the named parameter."""
	@overload
	def getParameter(self,parameterName:str,MSamplerStateDesc:Any)->Self:
		"""getParameter(parameterName, bool) -> self
		getParameter(parameterName, int) -> self
		getParameter(parameterName, float) -> self
		getParameter(parameterName, list of float) -> self
		getParameter(parameterName, MFloatVector) -> self
		getParameter(parameterName, MMatrix) -> self
		getParameter(parameterName, MFloatMatrix) -> self
		getParameter(parameterName, MTextureAssignment) -> self
		getParameter(parameterName, MRenderTargetAssignment) -> self
		getParameter(parameterName, MSamplerStateDesc) -> self

		Get the value of the named parameter."""
class MRenderProfile:
	"""The MRenderProfile class describes the rendering APIs and algorithms supported by a given rendering entity (e.g. a shading node, a renderer)."""
	kMayaSoftware:int=0
	kMayaOpenGL:int=1
	kMayaD3D:int=2
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	@overload
	def addRenderer(self,renderer:int)->Self:
		"""addRenderer(renderer) -> selfaddRenderer(name, version) -> self

		Add an internal renderer to this profile:
		* renderer (int) - One of Maya's internal renderers:
		  kMayaSoftware,
		  kMayaOpenGL,
		  kMayaD3D

		Or add a custom renderer to this profile:
		* name (string) - The name of the renderer,
		* version (float) = The version of the renderer or rendering API.
		The name and version specified must correspond to a renderer registered with Maya. Currently, only Maya's internal renderers (just named after the APIs they use: 'OpenGL', 'D3D', or 'Software') are supported. When registering support for Maya's internal renderers, it's simpler to use the other version of this method."""
	@overload
	def addRenderer(self,name:str,version:float)->Self:
		"""addRenderer(renderer) -> selfaddRenderer(name, version) -> self

		Add an internal renderer to this profile:
		* renderer (int) - One of Maya's internal renderers:
		  kMayaSoftware,
		  kMayaOpenGL,
		  kMayaD3D

		Or add a custom renderer to this profile:
		* name (string) - The name of the renderer,
		* version (float) = The version of the renderer or rendering API.
		The name and version specified must correspond to a renderer registered with Maya. Currently, only Maya's internal renderers (just named after the APIs they use: 'OpenGL', 'D3D', or 'Software') are supported. When registering support for Maya's internal renderers, it's simpler to use the other version of this method."""
	@overload
	def hasRenderer(self,renderer:int)->bool:
		"""hasRenderer(renderer) -> boolhasRenderer(name, version) -> bool

		Check if a Maya renderer is listed in this profile:
		* renderer (int) - One of Maya's internal renderers, see addRenderer().

		Or check if a custom renderer is in this render profile:
		* name (string) - The name of the renderer,
		* version (float) = The version of the renderer or rendering API.
		see addRenderer()"""
	@overload
	def hasRenderer(self,name:str,version:float)->bool:
		"""hasRenderer(renderer) -> boolhasRenderer(name, version) -> bool

		Check if a Maya renderer is listed in this profile:
		* renderer (int) - One of Maya's internal renderers, see addRenderer().

		Or check if a custom renderer is in this render profile:
		* name (string) - The name of the renderer,
		* version (float) = The version of the renderer or rendering API.
		see addRenderer()"""
	def numberOfRenderers(self)->int:
		"""numberOfRenderers() -> int

		Return the number of renderers in this profile."""
class MRenderTarget:
	"""An instance of a render target that may be used with Viewport 2.0."""
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def updateDescription(self,MRenderTargetDescription:Any)->Self:
		"""updateDescription(MRenderTargetDescription) -> self

		Change the description of a render target."""
	def targetDescription(self)->MRenderTargetDescription:
		"""targetDescription() -> MRenderTargetDescription

		Get target description."""
	def resourceHandle(self)->int:
		"""resourceHandle() -> long

		Returns a long containing a C++ 'void' pointer which points to the draw API dependent handle for a render target.
		For OpenGL, a pointer to an OpenGL texture identifier is returned.
		For DirectX, a reference to a Direct3D "view" of a target is returned."""
	def rawData(self)->list[int|rowPitch|slicePitch]:
		"""rawData() -> [long, rowPitch, slicePitch]

		Get a copy of the raw data mapped to the target.
		The caller must deallocate the system memory (using freeRawData()) as the target itself does not keep any references to it.

		* rowPitch [OUT] (int) - The row pitch of the data. It represents the number of bytes of one line of the target data.
		* slicePitch [OUT] (int) - The slice pitch of the data. It represents the number of bytes of the whole target data."""
	@staticmethod
	def freeRawData(long:Any)->None:
		"""freeRawData(long) -> None
		Deallocate system memory - retrieved from rawData()."""
class MRenderTargetAssignment:
	"""Structure to hold the information required to set a texture parameter on a shader using a render target as input."""
	@property
	def target(self)->Any:
		"""The render target"""
	@target.setter
	def target(self,value:Any)->None:...
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
class MRenderTargetDescription:
	"""Class which provides a description of a hardware render target."""
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def name(self)->str:
		"""name() -> string

		Query the name identifier for the target description."""
	def width(self)->int:
		"""width() -> int

		Query the width of a 2D render target slice."""
	def height(self)->int:
		"""height() -> int

		Query the height of a 2D render target slice."""
	def multiSampleCount(self)->int:
		"""multiSampleCount() -> int

		Query the multi-sample count defined by the description."""
	def rasterFormat(self)->int:
		"""rasterFormat() -> int

		Query the raster format defined by the description."""
	def arraySliceCount(self)->int:
		"""arraySliceCount() -> int

		Query the number of array slices defined by the description."""
	def isCubeMap(self)->bool:
		"""isCubeMap() -> bool

		Query whether this is a cube map target."""
	def allowsUnorderedAccess(self)->bool:
		"""allowsUnorderedAccess() -> bool

		Query whether unordered access is supported."""
	def setName(self,string:Any)->Self:
		"""setName(string) -> self

		Set name of the target."""
	def setWidth(self,int:int)->Self:
		"""setWidth(int) -> self

		Set width of the target."""
	def setHeight(self,int:int)->Self:
		"""setHeight(int) -> self

		Set height of the target."""
	def setMultiSampleCount(self,int:int)->Self:
		"""setMultiSampleCount(int) -> self

		Set multisample count of the target."""
	def setRasterFormat(self,int:int)->Self:
		"""setRasterFormat(int) -> self

		Set the raster format of the target."""
	def setArraySliceCount(self,int:int)->Self:
		"""setArraySliceCount(int) -> self

		Set array slice count of the target."""
	def setIsCubeMap(self,bool:bool)->Self:
		"""setIsCubeMap(bool) -> self

		Set cube map flag for the target."""
	def setAllowsUnorderedAccess(self,bool:bool)->Self:
		"""setAllowsUnorderedAccess(bool) -> self

		Set the flag for unordered data access for the target."""
	def compatibleWithDescription(self,MRenderTargetDescription:Any)->bool:
		"""compatibleWithDescription(MRenderTargetDescription) -> bool

		Determine if another target with a given description is 'compatible' with a target using this description."""
class MRenderTargetManager:
	"""Provides access to MRenderTarget objects for use in Viewport 2.0."""
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def acquireRenderTarget(self,MRenderTargetDescription:Any)->MRenderTarget:
		"""acquireRenderTarget(MRenderTargetDescription) -> MRenderTarget
		Acquire an instance of a render target.
		When the object is no longer needed, releaseRenderTarget() should be called
		to notify the target manager that the caller is done with the render target."""
	def acquireRenderTargetFromScreen(self,string:Any)->MRenderTarget:
		"""acquireRenderTargetFromScreen(string) -> MRenderTarget
		Acquire an instance of a render target with the same characteristics as the current on-screen target.
		When the object is no longer needed, releaseRenderTarget() should be called
		to notify the target manager that the caller is done with the render target."""
	def formatSupportsSRGBWrite(self,int:int)->bool:
		"""formatSupportsSRGBWrite(int) -> bool
		This method will perform a check to determine whether gamma correction can be performed
		by the GPU when writing pixels to a render target of a given format."""
	def releaseRenderTarget(self,MRenderTarget:Any)->Self:
		"""releaseRenderTarget(MRenderTarget) -> self
		Deletes the MRenderTarget and releases the reference to the underlying target which is held by the MRenderTarget object."""
class MRenderUtilities:
	"""Utilities class for rendering in Viewport 2.0"""
	kPerspectiveCamera:int=0
	kOrthogonalCameraWithMargin:int=1
	kOrthogonalCameraCloseUp:int=2
	kDefaultLights:int=0
	kSwatchLight:int=1
	kAmbientLight:int=2
	@staticmethod
	@overload
	def acquireSwatchDrawContext()->MDrawContext:
		"""acquireSwatchDrawContext() -> MDrawContext
		acquireSwatchDrawContext(colorTarget) -> MDrawContext
		acquireSwatchDrawContext(colorTarget, depthTarget) -> MDrawContext

		Acquire a draw context fit for rendering a swatch.
		The caller is responsible for releasing the draw context when it is no longer needed, by calling MRenderUtilities::releaseDrawContext().

		* colorTarget (MRenderTarget) -  The color target for swatch drawing.
		* depthTarget (MRenderTarget) -  The depth target for swatch drawing.
		If targets are not provided, the caller is responsible for properly setting up render targets.
		Specifying targets also insures that the proper GL context is made active when using GL devices."""
	@overload
	@staticmethod
	def acquireSwatchDrawContext(colorTarget:MRenderTarget)->MDrawContext:
		"""acquireSwatchDrawContext() -> MDrawContext
		acquireSwatchDrawContext(colorTarget) -> MDrawContext
		acquireSwatchDrawContext(colorTarget, depthTarget) -> MDrawContext

		Acquire a draw context fit for rendering a swatch.
		The caller is responsible for releasing the draw context when it is no longer needed, by calling MRenderUtilities::releaseDrawContext().

		* colorTarget (MRenderTarget) -  The color target for swatch drawing.
		* depthTarget (MRenderTarget) -  The depth target for swatch drawing.
		If targets are not provided, the caller is responsible for properly setting up render targets.
		Specifying targets also insures that the proper GL context is made active when using GL devices."""
	@overload
	@staticmethod
	def acquireSwatchDrawContext(colorTarget:MRenderTarget,depthTarget:MRenderTarget)->MDrawContext:
		"""acquireSwatchDrawContext() -> MDrawContext
		acquireSwatchDrawContext(colorTarget) -> MDrawContext
		acquireSwatchDrawContext(colorTarget, depthTarget) -> MDrawContext

		Acquire a draw context fit for rendering a swatch.
		The caller is responsible for releasing the draw context when it is no longer needed, by calling MRenderUtilities::releaseDrawContext().

		* colorTarget (MRenderTarget) -  The color target for swatch drawing.
		* depthTarget (MRenderTarget) -  The depth target for swatch drawing.
		If targets are not provided, the caller is responsible for properly setting up render targets.
		Specifying targets also insures that the proper GL context is made active when using GL devices."""
	@staticmethod
	@overload
	def acquireUVTextureDrawContext()->MDrawContext:
		"""acquireUVTextureDrawContext() -> MDrawContext
		acquireUVTextureDrawContext(colorTarget) -> MDrawContext
		acquireUVTextureDrawContext(colorTarget, depthTarget) -> MDrawContext

		Acquire a draw context fit for rendering a texture for the UV editor.
		The caller is responsible for releasing the draw context when it is no longer needed, by calling MRenderUtilities::releaseDrawContext().

		* colorTarget (MRenderTarget) -  The color target for UV texture drawing.
		* depthTarget (MRenderTarget) -  The depth target for UV texture drawing.
		If targets are not provided, the caller is responsible for properly setting up render targets.
		Specifying targets also insures that the proper GL context is made active when using GL devices."""
	@overload
	@staticmethod
	def acquireUVTextureDrawContext(colorTarget:MRenderTarget)->MDrawContext:
		"""acquireUVTextureDrawContext() -> MDrawContext
		acquireUVTextureDrawContext(colorTarget) -> MDrawContext
		acquireUVTextureDrawContext(colorTarget, depthTarget) -> MDrawContext

		Acquire a draw context fit for rendering a texture for the UV editor.
		The caller is responsible for releasing the draw context when it is no longer needed, by calling MRenderUtilities::releaseDrawContext().

		* colorTarget (MRenderTarget) -  The color target for UV texture drawing.
		* depthTarget (MRenderTarget) -  The depth target for UV texture drawing.
		If targets are not provided, the caller is responsible for properly setting up render targets.
		Specifying targets also insures that the proper GL context is made active when using GL devices."""
	@overload
	@staticmethod
	def acquireUVTextureDrawContext(colorTarget:MRenderTarget,depthTarget:MRenderTarget)->MDrawContext:
		"""acquireUVTextureDrawContext() -> MDrawContext
		acquireUVTextureDrawContext(colorTarget) -> MDrawContext
		acquireUVTextureDrawContext(colorTarget, depthTarget) -> MDrawContext

		Acquire a draw context fit for rendering a texture for the UV editor.
		The caller is responsible for releasing the draw context when it is no longer needed, by calling MRenderUtilities::releaseDrawContext().

		* colorTarget (MRenderTarget) -  The color target for UV texture drawing.
		* depthTarget (MRenderTarget) -  The depth target for UV texture drawing.
		If targets are not provided, the caller is responsible for properly setting up render targets.
		Specifying targets also insures that the proper GL context is made active when using GL devices."""
	@staticmethod
	def blitTargetToGL(target:MRenderTarget,region:float[2][2],unfiltered:bool)->None:
		"""blitTargetToGL(target, region, unfiltered) -> None

		Blit the data from a target to current GL context.

		* target (MRenderTarget) - The source target to get the data from.
		* region (float[2][2]) - Rectangular region to be rendered - [ [x1, y1], [x2, y2] ].
		* unfiltered (bool) - Render with hardware filtering or sharply defined pixels."""
	@staticmethod
	def blitTargetToImage(target:MRenderTarget,image:om.MImage)->None:
		"""blitTargetToImage(target, image) -> None

		Copy the data from a target to an image.

		* target (MRenderTarget) - The source target to get the data from.
		* image (MImage) - The destination image to copy the data to."""
	@staticmethod
	def drawSimpleMesh(context:MDrawContext,vertexBuffer:MVertexBuffer,indexBuffer:MIndexBuffer,primitiveType:int,start:int,count:int)->None:
		"""drawSimpleMesh(context, vertexBuffer, indexBuffer, primitiveType, start, count) -> None

		Render a simple mesh.

		* context (MDrawContext) - The draw context to use for render.
		* vertexBuffer (MVertexBuffer) - The vertex buffer for the mesh.
		* indexBuffer (MIndexBuffer) - The index buffer for the mesh.
		* primitiveType (int) - The primitive type of the mesh. See MGeometry.primitiveString()
		* start (int) - The location of the first index read from the index buffer.
		* count (int) - The number of indices to draw."""
	@staticmethod
	@overload
	def releaseDrawContext(context:MDrawContext)->None:
		"""releaseDrawContext(context) -> None
		releaseDrawContext(context, releaseTargets) -> None

		Release a draw context.

		* context (MDrawContext) - The draw context to release.
		* releaseTargets (bool) - Removes the current draw targets from the device, defaults to true.
		If releaseTargets is requested, the device will have NULL targets on function exit."""
	@overload
	@staticmethod
	def releaseDrawContext(context:MDrawContext,releaseTargets:bool)->None:
		"""releaseDrawContext(context) -> None
		releaseDrawContext(context, releaseTargets) -> None

		Release a draw context.

		* context (MDrawContext) - The draw context to release.
		* releaseTargets (bool) - Removes the current draw targets from the device, defaults to true.
		If releaseTargets is requested, the device will have NULL targets on function exit."""
	@staticmethod
	def renderMaterialViewerGeometry(shape:str,shaderNode:om.MObject,image:om.MImage,cameraMode:int=MRenderUtilities.kPerspectiveCamera,lightRig:int=MRenderUtilities.kDefaultLights)->None:
		"""renderMaterialViewerGeometry(shape, shaderNode, image, cameraMode=kPerspectiveCamera, lightRig=kDefaultLights) -> None

		Do an off-screen render replicating the results shown by the Material Viewer window of Hypershade..

		* shape (str) Shape to render. Valid values include "meshSphere", "meshPlane", "meshShaderball", "meshTeapot", and "meshCloth".
		* shaderNode (MObject) The shader node to use on the geometry.
		* image (MImage) The image where the result should be stored.
		* cameraMode (int) The camera to use for rendering. Defaults to MRenderUtilities.kPerspectiveCamera.
		* lightRig (int) The light rig to use for rendering. Defaults to MRenderUtilities.kDefaultLights."""
	@staticmethod
	def swatchBackgroundColor()->om.MColor:
		"""swatchBackgroundColor() -> MColor

		Returns the default background color for the hardware rendered swatch."""
class MRenderer:
	"""Main interface class to the Viewport 2.0 renderer"""
	kNone:int=0
	kOpenGL:int=1
	kDirectX11:int=2
	kOpenGLCoreProfile:int=4
	kAllDevices:int=7
	kD24S8:int=0
	kD24X8:int=1
	kD32_FLOAT:int=2
	kR24G8:int=3
	kR24X8:int=4
	kDXT1_UNORM:int=5
	kDXT1_UNORM_SRGB:int=6
	kDXT2_UNORM:int=7
	kDXT2_UNORM_SRGB:int=8
	kDXT2_UNORM_PREALPHA:int=9
	kDXT3_UNORM:int=10
	kDXT3_UNORM_SRGB:int=11
	kDXT3_UNORM_PREALPHA:int=12
	kDXT4_UNORM:int=13
	kDXT4_SNORM:int=14
	kDXT5_UNORM:int=15
	kDXT5_SNORM:int=16
	kBC6H_UF16:int=17
	kBC6H_SF16:int=18
	kBC7_UNORM:int=19
	kBC7_UNORM_SRGB:int=20
	kR9G9B9E5_FLOAT:int=21
	kR1_UNORM:int=22
	kA8:int=23
	kR8_UNORM:int=24
	kR8_SNORM:int=25
	kR8_UINT:int=26
	kR8_SINT:int=27
	kL8:int=28
	kR16_FLOAT:int=29
	kR16_UNORM:int=30
	kR16_SNORM:int=31
	kR16_UINT:int=32
	kR16_SINT:int=33
	kL16:int=34
	kR8G8_UNORM:int=35
	kR8G8_SNORM:int=36
	kR8G8_UINT:int=37
	kR8G8_SINT:int=38
	kB5G5R5A1:int=39
	kB5G6R5:int=40
	kR32_FLOAT:int=41
	kR32_UINT:int=42
	kR32_SINT:int=43
	kR16G16_FLOAT:int=44
	kR16G16_UNORM:int=45
	kR16G16_SNORM:int=46
	kR16G16_UINT:int=47
	kR16G16_SINT:int=48
	kR8G8B8A8_UNORM:int=49
	kR8G8B8A8_SNORM:int=50
	kR8G8B8A8_UINT:int=51
	kR8G8B8A8_SINT:int=52
	kR10G10B10A2_UNORM:int=53
	kR10G10B10A2_UINT:int=54
	kB8G8R8A8:int=55
	kB8G8R8X8:int=56
	kR8G8B8X8:int=57
	kA8B8G8R8:int=58
	kR32G32_FLOAT:int=59
	kR32G32_UINT:int=60
	kR32G32_SINT:int=61
	kR16G16B16A16_FLOAT:int=62
	kR16G16B16A16_UNORM:int=63
	kR16G16B16A16_SNORM:int=64
	kR16G16B16A16_UINT:int=65
	kR16G16B16A16_SINT:int=66
	kR32G32B32_FLOAT:int=67
	kR32G32B32_UINT:int=68
	kR32G32B32_SINT:int=69
	kR32G32B32A32_FLOAT:int=70
	kR32G32B32A32_UINT:int=71
	kR32G32B32A32_SINT:int=72
	kNumberOfRasterFormats:int=73
	@staticmethod
	def GPUDeviceHandle()->int:
		"""GPUDeviceHandle() -> long

		Returns a long containing a C++ 'void' pointer which points to the GPU "device".In the case that the drawing API is OpenGL then the "device" is a handle to an OpenGL context.
		In the case that the drawing API is DirectX then the "device" is a pointer to a DirectX device."""
	@staticmethod
	def GPUmaximumPrimitiveCount()->int:
		"""GPUmaximumPrimitiveCount() -> int

		Returns the maximum number of primitives that can be drawn per draw call by the GPU device.
		0 if device has not been initialized."""
	@staticmethod
	def GPUmaximumVertexBufferSize()->int:
		"""GPUmaximumVertexBufferSize() -> int

		Returns the maximum number of vertices allowed in a vertex buffer by the GPU device.
		0 if device has not been initialized."""
	@staticmethod
	def activeRenderOverride()->str:
		"""activeRenderOverride() -> string

		Returns the name of the active override."""
	@staticmethod
	def copyTargetToScreen(MRenderTarget:Any)->bool:
		"""copyTargetToScreen(MRenderTarget) -> bool

		Copy a render target to the screen.
		If the target's dimensions are not the same as the active viewport it will be scaled up or down as necessary to fill the entire viewport."""
	@staticmethod
	def render(sourceName:str,targetList:Any)->bool:
		"""render(sourceName, targetList) -> bool

		Render images from a panel to render targets.
		return True if render operation was successful.
		* sourceName (string) - The name of the source view want to render.
		* targetList (PyListObject:MRenderTarget) - Render target list want to render into. """
	@staticmethod
	def deregisterOverride(MRenderOverride:Any)->None:
		"""deregisterOverride(MRenderOverride) -> None

		Deregister an existing render override on the renderer.
		The renderer will remove this override from it's list of registered overrides."""
	@staticmethod
	def disableChangeManagementUntilNextRefresh()->None:
		"""disableChangeManagementUntilNextRefresh() -> None

		Calling this method will cause Viewport 2.0 to stop processing all changes to the Maya scene until the next viewport refresh."""
	@staticmethod
	def drawAPI()->int:
		"""drawAPI() -> int

		Returns the current drawing API. Returns 'kNone' if the renderer is not initialized.

		  MRenderer.kNone          Uninitialized device
		  MRenderer.kOpenGL        OpenGL
		  MRenderer.kDirectX11     Direct X 11
		  MRenderer.kAllDevices    All : OpenGL and Direct X 11"""
	@staticmethod
	def drawAPIIsOpenGL()->bool:
		"""drawAPIIsOpenGL() -> bool

		Returns whether the current drawing API is OpenGL or not"""
	@staticmethod
	def drawAPIVersion()->int:
		"""drawAPIVersion() -> int

		Returns the version of drawing API."""
	@staticmethod
	def findRenderOverride(string:Any)->MRenderOverride:
		"""findRenderOverride(string) -> MRenderOverride

		Returns a reference to an existing render override registered with the renderer."""
	@staticmethod
	def getFragmentManager()->MFragmentManager:
		"""getFragmentManager() -> MFragmentManager

		Returns the fragment manager or None if the renderer is not initialized properly."""
	@staticmethod
	def getRenderTargetManager()->MRenderTargetManager:
		"""getRenderTargetManager() -> MRenderTargetManager

		Returns the render target manager or None if the renderer is not initialized properly."""
	@staticmethod
	def getShaderManager()->MShaderManager:
		"""getShaderManager() -> MShaderManager

		Returns the shader manager or None if the renderer is not initialized properly."""
	@staticmethod
	def getTextureManager()->MTextureManager:
		"""getTextureManager() -> MTextureManager

		Returns the texture manager or None if the renderer is not initialized properly."""
	@staticmethod
	def setOutputTargetOverrideSize(width:Any,height:Any)->None:
		"""setOutputTargetOverrideSize(width, height) -> None

		This method allows rendering to occur to an offscreen target which differs from the interactive 3d viewport size."""
	@staticmethod
	def getOutputTargetOverrideSize()->list[int]:
		"""getOutputTargetOverrideSize() -> [int, int]

		Get the override dimensions set for the final output target in format [width, height]."""
	@staticmethod
	def unsetOutputTargetOverrideSize()->None:
		"""unsetOutputTargetOverrideSize() -> None

		Will unset any override dimensions set for the final output target."""
	@staticmethod
	def outputTargetSize()->list[int]:
		"""outputTargetSize() -> [int, int]

		Get target size in format [width, height]."""
	@staticmethod
	def registerOverride(MRenderOverride:Any)->None:
		"""registerOverride(MRenderOverride) -> None

		Register the override as being usable by the renderer.
		If the override is already registered it will not be registered again."""
	@staticmethod
	def renderOverrideCount()->int:
		"""renderOverrideCount() -> int

		Returns the number of registered render overrides."""
	@staticmethod
	def renderOverrideName()->str:
		"""renderOverrideName() -> string

		Get the current render override name used for batch rendering.
		If there is no override then an empty string will be returned."""
	@staticmethod
	def setGeometryDrawDirty(object:om.MObject,topologyChanged:bool=True)->None:
		"""setGeometryDrawDirty(object, topologyChanged=True) -> None

		Notify the Viewport 2.0 renderer that the geometry (size, shape, etc.) of object has changed, causing the object to be updated in the viewport.

		* object (MObject) - DAG object which has been modified.
		* topologyChanged (bool) - has the object topology changed"""
	@staticmethod
	def setLightRequiresShadows(object:om.MObject,flag:bool)->bool:
		"""setLightRequiresShadows(object, flag) -> bool

		This method allows for plug-in writers to indicate that the shadow map contents for a given light are required, regardless of the light limit.
		Returns True if the method added or removed the request successfully.

		* object (MObject) - Light to request shadow update for
		* flag (bool) - Indicate if an update is requested. When set to true a request is added, and when set false any existing request is removed."""
	@staticmethod
	def needEvaluateAllLights()->None:
		"""needEvaluateAllLights() -> None

		Notify the Viewport 2.0 renderer that it should evaluate all lights marked dirty, regardless of the light limit.For example, if there are 8 lights accessible because of the Viewport 2.0 light limit option, Only the first 8 non-ambient lights created will be evaluated.Call this method to instruct Viewport 2.0 to evaluate all dirty lights regardless of the light limit option.

		Note that this method does NOT perform any DG evaluation when it is called.The actual evaluation does not occur until the next viewport refresh. This method is threadsafe. The viewport refresh will occur asynchronously.Multiple calls to this method will get merged.

		Call this method may decrease performance in Viewport 2.0 during the next viewport refresh.Once this method is called, all unused lights that are marked dirty will be evaluated in the next viewport refresh.

		An example application of this method is to obtain light information while ignoring the light limit.If this method is not called, information on unused lights cannot be obtained via MDrawContext, even if LightFilter is set to kFilteredToLightLimit.This is because unused lights are not evaluated automatically by Viewport 2.0 by default."""
	@staticmethod
	def setLightsAndShadowsDirty()->None:
		"""setLightsAndShadowsDirty() -> None

		Notify the Viewport 2.0 renderer that something has changed which requires re-evaluation of lighting and shadows."""
	@staticmethod
	def setRenderOverrideName(string:Any)->bool:
		"""setRenderOverrideName(string) -> bool

		Set the name of a render override (MRenderOverride) for batch rendering."""
class MSamplerState:
	"""Container class for an acquired complete GPU sampler state."""
	kMinMagMipPoint:int=0
	kMinMagPoint_MipLinear:int=1
	kMinPoint_MagLinear_MipPoint:int=4
	kMinPoint_MagMipLinear:int=5
	kMinLinear_MagMipPoint:int=16
	kMinLinear_MagPoint_MipLinear:int=17
	kMinMagLinear_MipPoint:int=20
	kMinMagMipLinear:int=21
	kAnisotropic:int=85
	kTexWrap:int=1
	kTexMirror:int=2
	kTexClamp:int=3
	kTexBorder:int=4
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def desc(self)->MSamplerStateDesc:
		"""desc() -> MSamplerStateDesc

		Get the sampler state descriptor that was used to create the state object."""
	def resourceHandle(self)->int:
		"""resourceHandle() -> long

		Returns a long containing a C++ 'void' pointer which points to the draw API dependent handle for a sampler state.
		For OpenGL, such a handle does not exist and a NULL pointer will be returned.
		For DirectX, a pointer to a Direct3D state will be returned."""
class MSamplerStateDesc:
	"""Descriptor for a complete sampler state."""
	@property
	def filter(self)->Any:
		"""Selects how to filter a texture sample, default kMinMagMipPoint"""
	@filter.setter
	def filter(self,value:Any)->None:...
	@property
	def comparisonFn(self)->Any:
		"""Selects the filter comparison function, default kCompareAlways"""
	@comparisonFn.setter
	def comparisonFn(self,value:Any)->None:...
	@property
	def addressU(self)->Any:
		"""Select the u coordinate addressing mode, default kTexWrap"""
	@addressU.setter
	def addressU(self,value:Any)->None:...
	@property
	def addressV(self)->Any:
		"""Select the v coordinate addressing mode, default kTexWrap"""
	@addressV.setter
	def addressV(self,value:Any)->None:...
	@property
	def addressW(self)->Any:
		"""Select the w coordinate addressing mode, default kTexWrap"""
	@addressW.setter
	def addressW(self,value:Any)->None:...
	@property
	def borderColor(self)->Any:
		"""Set border color used for accesses beyond texture 0..1, default(0,0,0,0)"""
	@borderColor.setter
	def borderColor(self,value:Any)->None:...
	@property
	def mipLODBias(self)->Any:
		"""Set a float bias to be added to the computed mip LOD level, default 0"""
	@mipLODBias.setter
	def mipLODBias(self,value:Any)->None:...
	@property
	def minLOD(self)->Any:
		"""Set minimum mip LOD level accessed, default 0"""
	@minLOD.setter
	def minLOD(self,value:Any)->None:...
	@property
	def maxLOD(self)->Any:
		"""Set maximum mip LOD level accessed, default 16"""
	@maxLOD.setter
	def maxLOD(self,value:Any)->None:...
	@property
	def maxAnisotropy(self)->Any:
		"""Set the maximum anisotropy permitted for anisotropic filters. The range is 1..16, default 1"""
	@maxAnisotropy.setter
	def maxAnisotropy(self,value:Any)->None:...
	@property
	def coordCount(self)->Any:
		"""Set the number of texture coordinates, default 2"""
	@coordCount.setter
	def coordCount(self,value:Any)->None:...
	@property
	def elementIndex(self)->Any:
		"""When using texture arrays, selects array element, default 0"""
	@elementIndex.setter
	def elementIndex(self,value:Any)->None:...
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def setDefaults(self)->Self:
		"""setDefaults() -> self

		Set all values for the target blend state to their default values."""
class MSceneRender(MRenderOperation):
	"""Class which defines a scene render."""
	@property
	def mClearOperation(self)->Any:
		"""Default clear operation object."""
	@mClearOperation.setter
	def mClearOperation(self,value:Any)->None:...
	kExcludeNone:int=0
	kExcludeNurbsCurves:int=1
	kExcludeNurbsSurfaces:int=2
	kExcludeMeshes:int=4
	kExcludePlanes:int=8
	kExcludeLights:int=16
	kExcludeCameras:int=32
	kExcludeJoints:int=64
	kExcludeIkHandles:int=128
	kExcludeDeformers:int=256
	kExcludeDynamics:int=512
	kExcludeParticleInstancers:int=1024
	kExcludeLocators:int=2048
	kExcludeDimensions:int=4096
	kExcludeSelectHandles:int=8192
	kExcludePivots:int=16384
	kExcludeTextures:int=32768
	kExcludeGrid:int=65536
	kExcludeCVs:int=131072
	kExcludeHulls:int=262144
	kExcludeStrokes:int=524288
	kExcludeSubdivSurfaces:int=1048576
	kExcludeFluids:int=2097152
	kExcludeFollicles:int=4194304
	kExcludeHairSystems:int=8388608
	kExcludeImagePlane:int=16777216
	kExcludeNCloths:int=33554432
	kExcludeNRigids:int=67108864
	kExcludeDynamicConstraints:int=134217728
	kExcludeManipulators:int=268435456
	kExcludeNParticles:int=536870912
	kExcludeMotionTrails:int=1073741824
	kExcludeHoldOuts:int=-2147483648
	kExcludeAll:int=-1
	kNoSceneFilterOverride:int=0
	kRenderPreSceneUIItems:int=1
	kRenderOpaqueShadedItems:int=2
	kRenderTransparentShadedItems:int=4
	kRenderShadedItems:int=6
	kRenderPostSceneUIItems:int=8
	kRenderUIItems:int=9
	kRenderNonShadedItems:int=9
	kRenderAllItems:int=-1
	kNoDisplayModeOverride:int=0
	kWireFrame:int=1
	kShaded:int=2
	kFlatShaded:int=4
	kShadeActiveOnly:int=8
	kBoundingBox:int=16
	kDefaultMaterial:int=32
	kTextured:int=64
	kNoLightingModeOverride:int=0
	kNoLight:int=1
	kAmbientLight:int=2
	kLightDefault:int=3
	kSelectedLights:int=4
	kSceneLights:int=5
	kPostEffectDisableNone:int=0
	kPostEffectDisableSSAO:int=1
	kPostEffectDisableMotionBlur:int=2
	kPostEffectDisableDOF:int=4
	kPostEffectDisableAll:int=-1
	kNoCullingOverride:int=0
	kCullNone:int=1
	kCullBackFaces:int=2
	kCullFrontFaces:int=3
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def addPostUIDrawables(self,drawManager:MUIDrawManager,frameContext:MFrameContext)->Self:
		"""addPostUIDrawables(drawManager, frameContext) -> self

		Provides access to the MUIDrawManager, which can be used to queue up operations to draw simple UI shapes like lines, circles, text, etc.

		This method will only be called when hasUIDrawables() is overridden to return true and kRenderPostSceneUIItems is set in the MSceneFilterOption mask returned by renderFilterOverride().

		UI drawables added in this method will be rendered after the scene render.

		* drawManager (MUIDrawManager) - The UI draw manager, it can be used to draw some simple geometry including text.
		* frameContext (MFrameContext) - Frame level context information"""
	def addPreUIDrawables(self,drawManager:MUIDrawManager,frameContext:MFrameContext)->Self:
		"""addPreUIDrawables(drawManager, frameContext) -> self

		Provides access to the MUIDrawManager, which can be used to queue up operations to draw simple UI shapes like lines, circles, text, etc.

		This method will only be called when hasUIDrawables() is overridden to return true and kRenderPreSceneUIItems is set in the MSceneFilterOption mask returned by renderFilterOverride().

		UI drawables added in this method will be rendered before the scene render.

		* drawManager (MUIDrawManager) - The UI draw manager, it can be used to draw some simple geometry including text.
		* frameContext (MFrameContext) - Frame level context information"""
	def cameraOverride(self)->MCameraOverride:
		"""cameraOverride() -> MCameraOverride

		Query for a camera override."""
	def clearOperation(self)->MClearOperation:
		"""clearOperation() -> MClearOperation

		Get the scene clear operation."""
	def cullingOverride(self)->int:
		"""cullingOverride() -> int

		Query for a face culling override.

		  MSceneRender.kNoCullingOverride    No culling override
		  MSceneRender.kCullNone             Don't perform culling
		  MSceneRender.kCullBackFaces        Cull back faces
		  MSceneRender.kCullFrontFaces       Cull front faces"""
	def displayModeOverride(self)->int:
		"""displayModeOverride() -> int

		Query for any display mode override.

		  MSceneRender.kNoDisplayModeOverride  No display mode override
		  MSceneRender.kWireFrame              Display wireframe
		  MSceneRender.kShade                  Display shaded textured
		  MSceneRender.kFlatShaded             Display flat shaded
		  MSceneRender.kShadeActiveOnly        Shade active objects. Only applicable if kShade or kFlatShaded is enabled.
		  MSceneRender.kBoundingBox            Display bounding boxes
		  MSceneRender.kDefaultMaterial        Use default material. Only applicable if kShade or kFlatShaded is enabled.
		  MSceneRender.kTextured               Display textured. Only applicable if kShade or kFlatShaded is enabled."""
	def fragmentName(self)->str:
		"""fragmentName() -> String

		Query the name of the fragment used to render the scene."""
	def hasUIDrawables(self)->bool:
		"""hasUIDrawables() -> bool

		Query whether addUIDrawables() should be called or not."""
	def lightModeOverride(self)->int:
		"""lightModeOverride() -> int

		Query for any lighting mode override.

		  MSceneRender.kNoLightingModeOverride  No lighting mode override
		  MSceneRender.kNoLight                 Use no light
		  MSceneRender.kAmbientLight            Use global ambient light
		  MSceneRender.kLightDefault            Use default light
		  MSceneRender.kSelectedLights          Use lights which are selected
		  MSceneRender.kSceneLights             Use all lights in the scene"""
	def objectSetOverride(self)->om.MSelectionList:
		"""objectSetOverride() -> MSelectionList

		Query for override for the set of objects to view.

		Visibility takes into account the current states of each object, any displayfilters, and camera frustum culling.

		Note that the override only applies to rendering but not selection.

		By default NULL is returned which indicates that no override is present."""
	def getParameters(self)->MRenderParameters:
		"""getParameters() -> MRenderParameters

		Method to return the operation's parameter set."""
	def getObjectTypeExclusions(self)->int:
		"""getObjectTypeExclusions() -> long

		Query for any object type exclusions.

		  MFrameContext.kExcludeNone                 Exclude no object types
		  MFrameContext.kExcludeNurbsCurves          Exclude NURBS curves
		  MFrameContext.kExcludeNurbsSurfaces        Exclude NURBS surface
		  MFrameContext.kExcludeMeshes               Exclude polygonal meshes
		  MFrameContext.kExcludePlanes               Exclude planes
		  MFrameContext.kExcludeLights               Exclude lights
		  MFrameContext.kExcludeCameras              Exclude camera
		  MFrameContext.kExcludeJoints               Exclude joints
		  MFrameContext.kExcludeIkHandles            Exclude IK handles
		  MFrameContext.kExcludeDeformers            Exclude all deformations
		  MFrameContext.kExcludeDynamics             Exclude all dynamics objects (emiters, cloth)
		  MFrameContext.kExcludeParticleInstancers   Exclude all Particle Instancers
		  MFrameContext.kExcludeLocators             Exclude locators
		  MFrameContext.kExcludeDimensions           Exclude all measurement objects
		  MFrameContext.kExcludeSelectHandles        Exclude selection handles
		  MFrameContext.kExcludePivots               Exclude pivots
		  MFrameContext.kExcludeTextures             Exclude texure placement objects
		  MFrameContext.kExcludeGrid                 Exclude grid drawing
		  MFrameContext.kExcludeCVs                  Exclude NURBS control vertices
		  MFrameContext.kExcludeHulls                Exclude NURBS hulls
		  MFrameContext.kExcludeStrokes              Exclude PaintFX strokes
		  MFrameContext.kExcludeSubdivSurfaces       Exclude subdivision surfaces
		  MFrameContext.kExcludeFluids               Exclude fluid objects
		  MFrameContext.kExcludeFollicles            Exclude hair follicles
		  MFrameContext.kExcludeHairSystems          Exclude hair system
		  MFrameContext.kExcludeImagePlane           Exclude image planes
		  MFrameContext.kExcludeNCloths              Exclude N-cloth objects
		  MFrameContext.kExcludeNRigids              Exclude rigid-body objects
		  MFrameContext.kExcludeDynamicConstraints   Exclude rigid-body constraints
		  MFrameContext.kExcludeManipulators         Exclude manipulators
		  MFrameContext.kExcludeNParticles           Exclude N-particle objects
		  MFrameContext.kExcludeMotionTrails         Exclude motion trails
		  MFrameContext.kExcludeHoldOuts                                Exclude Hold-Outs
		  MFrameContext.kExcludePluginShapes                    Exclude plug-in shapes
		  MFrameContext.kExcludeHUD                                 Exclude HUD
		  MFrameContext.kExcludeClipGhosts                      Exclude animation clip ghosts
		  MFrameContext.kExcludeGreasePencils           Exclude grease-pencil draw
		  MFrameContext.kExcludeControllers                     Exclude controllers objects
		  MFrameContext.kExcludeAll                  Exclude all listed object types"""
	def objectTypeExclusions(self)->int:
		"""objectTypeExclusions() -> int

		Query for any object type exclusions.
		Refer to the MObjectTypeExclusions enumeration on MSceneRender for possible values

		This method is deprecated. Use getObjectTypeExclusions instead."""
	def postEffectsOverride(self)->int:
		"""postEffectsOverride() -> int

		Query for post effects override.

		  MSceneRender.kPostEffectDisableNone        Use current render settings options
		  MSceneRender.kPostEffectDisableSSAO        Disable SSAO post effect
		  MSceneRender.kPostEffectDisableMotionBlur  Disable motion blur post effect
		  MSceneRender.kPostEffectDisableDOF         Disable depth-of-field post effect
		  MSceneRender.kPostEffectDisableAll         Disable all post effects"""
	def postRender(self)->Self:
		"""postRender() -> self

		Method to allow for the operation to clean up itself after being executed.

		By default this method performs no action"""
	def postSceneRender(self,context:MDrawContext)->Self:
		"""postSceneRender(context) -> self

		Method to allow for the operation to update itself after a scene rendering ends.

		This method will be called after computing shadow maps, and after a color pass.

		* context (MDrawContext) - Draw context after rendering has completed

		By default this method performs no action"""
	def preRender(self)->Self:
		"""preRender() -> self

		Method to allow for the operation to update itself before being executed. In general this would be used to update any operation parameters.


		No context information is available at this point.

		By default this method performs no action"""
	def preSceneRender(self,context:MDrawContext)->Self:
		"""preSceneRender(context) -> self

		Method to allow for the operation to update itself before a scene rendering begins.

		This method will be called before computing shadow maps, and before a color pass.

		* context (MDrawContext) - Draw context before rendering begins

		By default this method performs no action"""
	def renderFilterOverride(self)->int:
		"""renderFilterOverride() -> int

		Query which elements of a scene render will be drawn based on semantic meaning.

		  MSceneRender.kNoSceneFilterOverride
		  MSceneRender.kRenderPreSceneUIItems             Render UI items before scene render like grid or user added pre-scene UI items
		  MSceneRender.kRenderOpaqueShadedItems           Render only opaque shaded objects but not their wireframe or components
		  MSceneRender.kRenderTransparentShadedItems      Render only transparent shaded objects but not their wireframe or components
		  MSceneRender.kRenderShadedItems                         Render only shaded (opaque and transparent) objects but not their wireframe or components
		  MSceneRender.kRenderPostSceneUIItems            Render UI items after scene render like wireframe and components for surfaces as well as non-surface objects.
		  MSceneRender.kRenderUIItems                             kRenderPreSceneUIItems | kRenderPostSceneUIItems
		  MSceneRender.kRenderAllItems                            Render all items."""
	def shaderOverride(self)->MShaderInstance:
		"""shaderOverride() -> MShaderInstance

		Query for a scene level shader override."""
	def shadowEnableOverride(self)->bool|None:
		"""shadowEnableOverride() -> bool/None

		Query for shadow display override.
		By default a None value is returned indicating that no override is specified."""
class MSelectionContext:
	"""This class gives control on the viewport 2.0 selection behavior."""
	@property
	def selectionLevel(self)->Any:
		"""The selection level used to pick items.
		  kNone        No selection available.
		  kObject      Object level.
		               Objects are selected as a whole. Components are not directly accessible.
		  kComponent   Component level.
		               Components such as vertices, edges and faces are selectable. Selection
		               level of each individual MIntersection object is determined by primitive
		               type of the render item.
		  kFace        Face level.
		  kEdge        Edge level.
		  kVertex      Vertex level.
		"""
	@selectionLevel.setter
	def selectionLevel(self,value:Any)->None:...
	kNone:int=0
	kObject:int=1
	kComponent:int=2
	kFace:int=3
	kEdge:int=4
	kVertex:int=5
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
class MSelectionInfo:
	"""This class gives informations on the selection."""
	@property
	def alignmentMatrix(self)->Any:
		"""The alignment matrix.
		This is used to find ray object intersection."""
	@alignmentMatrix.setter
	def alignmentMatrix(self,value:Any)->None:...
	@property
	def isRay(self)->Any:
		"""Whether or not there is a selection ray.
		This is used to find ray object intersection"""
	@isRay.setter
	def isRay(self,value:Any)->None:...
	@property
	def isSingleSelection(self)->Any:
		"""Whether or not we want to select a single shape or component."""
	@isSingleSelection.setter
	def isSingleSelection(self,value:Any)->None:...
	@property
	def localRay(self)->Any:
		"""The selection ray (starting point and direction).
		This is used to find ray object intersection"""
	@localRay.setter
	def localRay(self,value:Any)->None:...
	@property
	def selectClosest(self)->Any:
		"""Whether or not we want to select the closest shape or component."""
	@selectClosest.setter
	def selectClosest(self,value:Any)->None:...
	@property
	def selectOnHilitedOnly(self)->Any:
		"""Whether or not the components can only be selected if the shape is hilited."""
	@selectOnHilitedOnly.setter
	def selectOnHilitedOnly(self,value:Any)->None:...
	@property
	def selectRect(self)->Any:
		"""The current selection rectangle dimensions (x, y, width, height)."""
	@selectRect.setter
	def selectRect(self,value:Any)->None:...
	@property
	def cursorPoint(self)->Any:
		"""The cursor point (x, y) relative to the lower left corner of the viewport."""
	@cursorPoint.setter
	def cursorPoint(self,value:Any)->None:...
	@property
	def pointSnapping(self)->Any:
		"""Whether or not selection is launched to find snap points."""
	@pointSnapping.setter
	def pointSnapping(self,value:Any)->None:...
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def selectForHilite(self,mask:om.MSelectionMask)->bool:
		"""selectForHilite(mask) -> bool

		Given the selection mask, determines if this shape can be selected for the hilite list.

		* mask (MSelectionMask) - The mask to test."""
	def selectable(self,mask:om.MSelectionMask)->bool:
		"""selectable(mask) -> bool

		Given the selection mask, determines if the shape is selectable.

		* mask (MSelectionMask) - The mask to test."""
	def selectableComponent(self,displayed:bool,mask:om.MSelectionMask)->bool:
		"""selectableComponent(displayed, mask) -> bool

		Given the selection mask, determines if the component is selectable.

		* displayed (bool) - Is the component displayed.
		* mask (MSelectionMask) - The mask to test."""
class MShaderCompileMacro:
	"""Structure to define a shader compiler macro."""
	@property
	def name(self)->Any:
		"""Name of the macro"""
	@name.setter
	def name(self,value:Any)->None:...
	@property
	def definition(self)->Any:
		"""Macro definition"""
	@definition.setter
	def definition(self,value:Any)->None:...
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
class MShaderInstance:
	"""An instance of a shader that may be used with Viewport 2.0."""
	kInvalid:int=0
	kBoolean:int=1
	kInteger:int=2
	kFloat:int=3
	kFloat2:int=4
	kFloat3:int=5
	kFloat4:int=6
	kFloat4x4Row:int=7
	kFloat4x4Col:int=8
	kTexture1:int=9
	kTexture2:int=10
	kTexture3:int=11
	kTextureCube:int=12
	kSampler:int=13
	kPixelShader:int=0
	kNormalShader:int=1
	kNormalShader2:int=2
	kVertexShader:int=3
	kGeometryShader:int=4
	kGlossShader:int=5
	kGlossShader2:int=6
	kRotationAngleShader:int=7
	kRotationAngleShader2:int=8
	kReflectanceShader:int=9
	kReflectanceShader2:int=10
	kRoughnessShader:int=11
	kRoughnessShader2:int=12
	kAnisotropyShader:int=13
	kAnisotropyShader2:int=14
	kDisplacementPosShader:int=15
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def activatePass(self,MDrawContext:Any,int:int)->Self:
		"""activatePass(MDrawContext, int) -> self
		Activates the given pass of the shader.
		Must be called between calls to bind() and unbind()."""
	def addInputFragment(self,fragmentName:str,outputName:str,inputName:str,promotedInputName:str|None=None)->Self:
		"""addInputFragment(fragmentName, outputName, inputName, promotedInputName=None) -> self

		Connect a fragment that has been registered with the fragment manager to an input on the existing MShaderInstance.
		Use this method to add shader instructions to an existing MShaderInstance.
		The code defined in the fragment will be compiled and executed on the GPU to compute the value for the input parameter.

		* fragmentName (string) - The name of a fragment that has been registered with the MFragmentManager.
		* outputName (string) - The name of the output on the registered fragment to connect to.
		* inputName (string) - The name of the input parameter on the MShaderInstance to connect to.* promotedInputName (string) - The name of the input parameter on the new fragment that will be promoted to replace the input parameter being connected to."""
	def addInputFragmentForMultiParams(self,fragmentName:str,uniqueName:str,outputNames:list[str],inputNames:list[str],invalidParameterIndices:list[int]|None=None,fragmentUsage:int=MShaderInstance.kPixelShader)->Self:
		"""addInputFragmentForMultiParams(fragmentName, uniqueName, outputNames, inputNames, invalidParameterIndices=None, fragmentUsage=MShaderInstance.kPixelShader) -> self

		Connect a named fragment that has been registered with the MFragmentManager
		to this MShaderInstance. The code defined in the fragment will be included
		in the new shader and executed on GPU to compute values for input parameters
		specified by inputNames.

		To connect with fragments, this MShaderInstance needs to be created from a
		shader fragment or fragment graph as well. Thus, a shader instance created
		from a file-based effect cannot connect with any fragments.

		After the fragment is connected, all input parameters with the same name in
		the new fragment graph are mapped to a single parameter in the shader by
		default. If uniqueness is required for input parameters on the fragment,
		uniqueName can be used to prefix names of the input parameters.

		This method is particularly useful when plugin needs to make multiple
		connections from the input fragment to this MShaderInstance. It can be used
		to make a single connection, but addInputFragment() is more convenient in
		this case. The numbers of the output and input parameters must match. An
		output and an input parameter with the same index in the two string arrays
		will be connected. To specify fan-out connections, the same output name can
		be repeated in outputNames as need. Fan-in connections are not allowed.

		If the numbers of the output and input parameters don't match, or a
		parameter (either output or input) doesn't exist, or their types don't
		match, the relevant parameters will not be connected and the method will
		return MStatus::kInvalidParameter. In this case, the fragment may still be
		connected partially to this MShaderInstance through other connectable
		parameter pairs, and plugin can use invalidParameterIndices to query
		indices of those invalid parameters in outputNames and inputNames.

		* fragmentName (string) - Name of the input fragment.
		* uniqueName (string) - A unique name to prefix names of input parameters on the input fragment.
		* outputNames (list of strings) - Names of the output parameters on the input fragment to connect from.
		* inputNames (list of strings) - Names of the input parameters on the MShaderInstance to connect to.
		* invalidParameterIndices (list of ints) - Optional list to query indices of invalid parameters.
		* fragmentUsage (int) - Not implemented."""
	def addOutputFragment(self,fragmentName:str,inputName:str)->Self:
		"""addOutputFragment(fragmentName, inputName) -> self

		Connect a fragment that has been registered with the fragment manager to an output on the existing MShaderInstance.
		The code defined in the fragment will be compiled and executed on the GPU to modify the value returned by the original shader.
		For example, use this method to add additional alpha or conditionals to the output color.

		* fragmentName (string) - The name of a fragment that has been registered with the MFragmentManager.
		* inputName (string) - The name of the input parameter on the fragment to connect the shaders output to."""
	def annotation(self,parameterName:str,annotationName:str)->int|float|str:
		"""annotation(parameterName, annotationName) -> int / float / string

		Returns the value of a named parameter annotation.

		 * parameterName (string) - The name of the parameter.
		 * annotationName (string) - The name of the annotation."""
	def bind(self,MDrawContext:Any)->Self:
		"""bind(MDrawContext) -> self
		Binds the shader instance to the draw context, so that it is the active shader."""
	def clone(self)->MShaderInstance:
		"""clone() -> MShaderInstance

		Clone the shader. This will return a new MShaderInstance object which is identical to the existing shader."""
	def createShaderInstanceWithColorManagementFragment(self,inputColorSpace:str)->MShaderInstance:
		"""createShaderInstanceWithColorManagementFragment(inputColorSpace) -> MShaderInstance

		Return a new shader instance with Color Management fragment added, which is based on the callee.
		The callee shader instance is the one used for rendering a render item with image(a MPxNode with image, etc.)
		The new shader is completely independent of the original shader.
		Setting parameter values on either shader after calling this function will have no effect on the other.
		The function won't keep a copy of input parameter.


		When the returned new shader instance is no longer needed, MShaderManager.releaseShader()
		should be called to notify the shader manager that the caller is done with the shader.

		 * inputColorSpace (string) - The color space the current image is in"""
	def addColorManagementTextures(self)->Self:
		"""addColorManagementTextures() -> self

		Adds all the color management textures needed to render this shader instance.

		Required if your shader references a color managed fragment returned by
		MShaderInstance::getColorManagementFragmentInfo.

		Can be called even if no color management textures are required for the current
		shader instance."""
	def getPassCount(self,MDrawContext:Any)->int:
		"""getPassCount(MDrawContext) -> int
		Returns the number of draw passes defined by the shader.
		None if the shader instance or draw context was invalid."""
	def isArrayParameter(self,string:Any)->bool:
		"""isArrayParameter(string) -> bool

		Determine whether the named parameter is an array."""
	def getArraySize(self,string:Any)->int:
		"""getArraySize(string) -> int

		Return the size of an array if it is an array. Returns 0 if it is not an array"""
	def isTransparent(self)->bool:
		"""isTransparent() -> bool

		Return whether the shader will render with transparency."""
	def parameterDefaultValue(self,parameterName:str)->bool|int|float|tuple[float,...]:
		"""parameterDefaultValue(parameterName) -> bool / int / float / tuple of float

		Returns the default value of named parameter, None if no default value."""
	def parameterList(self)->list[str]:
		"""parameterList() -> list of string

		Get the names of all parameters that are settable on this shader instance."""
	def parameterSemantic(self,parameterName:str)->str:
		"""parameterSemantic(parameterName) -> string

		Returns the semantic associated to a named parameter."""
	def parameterType(self,string:Any)->int:
		"""parameterType(string) -> int

		Get the type of the named parameter, returns kInvalid if parameter is not found."""
	def passAnnotation(self,pass_:int,annotationName:str)->int|float|str:
		"""passAnnotation(pass, annotationName) -> int / float / string

		Returns the value of the current technique's pass annotation.

		 * pass (int) - The index of the pass.
		 * annotationName (string) - The name of the pass annotation."""
	def postDrawCallback(self)->function|None:
		"""postDrawCallback() -> function/None

		Returns the post-draw callback function set for the this shader instance.
		Returns None if the callback function is not set or is not a python function."""
	def preDrawCallback(self)->function|None:
		"""preDrawCallback() -> function/None

		Returns the pre-draw callback function set for the this shader instance.
		Returns None if the callback function is not set or is not a python function."""
	def resourceName(self,parameterName:str)->str:
		"""resourceName(parameterName) -> string

		Returns the resource name of a named texture parameter.
		The resource name of a texture parameter can be specified in the effect file using the 'ResourceName' annotation.
		It allows users to define a default texture using an external file.
		If no resource was defined for a texture, this function returns an empty string."""
	def semantic(self,string:Any)->str:
		"""semantic(string) -> string

		Return the semantic for a named parameter."""
	def isVaryingParameter(self,string:Any)->bool:
		"""isVaryingParameter(string) -> bool

		Return the true if a named parameter's values vary per vertex."""
	@overload
	def setArrayParameter(self,parameterName:str,arg:Sequence[bool],int:int)->Self:
		"""setArrayParameter(parameterName, sequence of bool, int) -> self
		setArrayParameter(parameterName, sequence of int, int) -> self
		setArrayParameter(parameterName, sequence of float, int) -> self
		setArrayParameter(parameterName, sequence of MMatrix, int) -> self

		Set the value of a named array parameter."""
	@overload
	def setArrayParameter(self,parameterName:str,arg:Sequence[int],int:int)->Self:
		"""setArrayParameter(parameterName, sequence of bool, int) -> self
		setArrayParameter(parameterName, sequence of int, int) -> self
		setArrayParameter(parameterName, sequence of float, int) -> self
		setArrayParameter(parameterName, sequence of MMatrix, int) -> self

		Set the value of a named array parameter."""
	@overload
	def setArrayParameter(self,parameterName:str,arg:Sequence[float],int:int)->Self:
		"""setArrayParameter(parameterName, sequence of bool, int) -> self
		setArrayParameter(parameterName, sequence of int, int) -> self
		setArrayParameter(parameterName, sequence of float, int) -> self
		setArrayParameter(parameterName, sequence of MMatrix, int) -> self

		Set the value of a named array parameter."""
	@overload
	def setArrayParameter(self,parameterName:str,arg:Sequence[om.MMatrix],int:int)->Self:
		"""setArrayParameter(parameterName, sequence of bool, int) -> self
		setArrayParameter(parameterName, sequence of int, int) -> self
		setArrayParameter(parameterName, sequence of float, int) -> self
		setArrayParameter(parameterName, sequence of MMatrix, int) -> self

		Set the value of a named array parameter."""
	def setIsTransparent(self,bool:bool)->Self:
		"""setIsTransparent(bool) -> self

		Set whether the shader will render with transparency."""
	def setAsVarying(self,parameterName:str,bool:bool)->Self:
		"""setAsVarying(parameterName, bool) -> self

		Set whether the named parameter's values will vary per vertex."""
	def setSemantic(self,parameterName:str,string:Any)->Self:
		"""setSemantic(parameterName, string) -> self

		Set the semantic of a named parameter."""
	def renameParameter(self,parameterName:str,string:Any)->Self:
		"""renameParameter(parameterName, string) -> self

		Rename a named parameter."""
	@overload
	def setParameter(self,parameterName:str,bool:bool)->Self:
		"""setParameter(parameterName, bool) -> self
		setParameter(parameterName, int) -> self
		setParameter(parameterName, float) -> self
		setParameter(parameterName, list of float) -> self
		setParameter(parameterName, MFloatVector) -> self
		setParameter(parameterName, MMatrix) -> self
		setParameter(parameterName, MFloatMatrix) -> self
		setParameter(parameterName, MTexture) -> self
		setParameter(parameterName, MRenderTarget) -> self
		setParameter(parameterName, MSamplerState) -> self

		Set the value of the named parameter."""
	@overload
	def setParameter(self,parameterName:str,int:int)->Self:
		"""setParameter(parameterName, bool) -> self
		setParameter(parameterName, int) -> self
		setParameter(parameterName, float) -> self
		setParameter(parameterName, list of float) -> self
		setParameter(parameterName, MFloatVector) -> self
		setParameter(parameterName, MMatrix) -> self
		setParameter(parameterName, MFloatMatrix) -> self
		setParameter(parameterName, MTexture) -> self
		setParameter(parameterName, MRenderTarget) -> self
		setParameter(parameterName, MSamplerState) -> self

		Set the value of the named parameter."""
	@overload
	def setParameter(self,parameterName:str,float:float)->Self:
		"""setParameter(parameterName, bool) -> self
		setParameter(parameterName, int) -> self
		setParameter(parameterName, float) -> self
		setParameter(parameterName, list of float) -> self
		setParameter(parameterName, MFloatVector) -> self
		setParameter(parameterName, MMatrix) -> self
		setParameter(parameterName, MFloatMatrix) -> self
		setParameter(parameterName, MTexture) -> self
		setParameter(parameterName, MRenderTarget) -> self
		setParameter(parameterName, MSamplerState) -> self

		Set the value of the named parameter."""
	@overload
	def setParameter(self,parameterName:str,arg:list[float])->Self:
		"""setParameter(parameterName, bool) -> self
		setParameter(parameterName, int) -> self
		setParameter(parameterName, float) -> self
		setParameter(parameterName, list of float) -> self
		setParameter(parameterName, MFloatVector) -> self
		setParameter(parameterName, MMatrix) -> self
		setParameter(parameterName, MFloatMatrix) -> self
		setParameter(parameterName, MTexture) -> self
		setParameter(parameterName, MRenderTarget) -> self
		setParameter(parameterName, MSamplerState) -> self

		Set the value of the named parameter."""
	@overload
	def setParameter(self,parameterName:str,MFloatVector:Any)->Self:
		"""setParameter(parameterName, bool) -> self
		setParameter(parameterName, int) -> self
		setParameter(parameterName, float) -> self
		setParameter(parameterName, list of float) -> self
		setParameter(parameterName, MFloatVector) -> self
		setParameter(parameterName, MMatrix) -> self
		setParameter(parameterName, MFloatMatrix) -> self
		setParameter(parameterName, MTexture) -> self
		setParameter(parameterName, MRenderTarget) -> self
		setParameter(parameterName, MSamplerState) -> self

		Set the value of the named parameter."""
	@overload
	def setParameter(self,parameterName:str,MMatrix:Any)->Self:
		"""setParameter(parameterName, bool) -> self
		setParameter(parameterName, int) -> self
		setParameter(parameterName, float) -> self
		setParameter(parameterName, list of float) -> self
		setParameter(parameterName, MFloatVector) -> self
		setParameter(parameterName, MMatrix) -> self
		setParameter(parameterName, MFloatMatrix) -> self
		setParameter(parameterName, MTexture) -> self
		setParameter(parameterName, MRenderTarget) -> self
		setParameter(parameterName, MSamplerState) -> self

		Set the value of the named parameter."""
	@overload
	def setParameter(self,parameterName:str,MFloatMatrix:Any)->Self:
		"""setParameter(parameterName, bool) -> self
		setParameter(parameterName, int) -> self
		setParameter(parameterName, float) -> self
		setParameter(parameterName, list of float) -> self
		setParameter(parameterName, MFloatVector) -> self
		setParameter(parameterName, MMatrix) -> self
		setParameter(parameterName, MFloatMatrix) -> self
		setParameter(parameterName, MTexture) -> self
		setParameter(parameterName, MRenderTarget) -> self
		setParameter(parameterName, MSamplerState) -> self

		Set the value of the named parameter."""
	@overload
	def setParameter(self,parameterName:str,MTexture:Any)->Self:
		"""setParameter(parameterName, bool) -> self
		setParameter(parameterName, int) -> self
		setParameter(parameterName, float) -> self
		setParameter(parameterName, list of float) -> self
		setParameter(parameterName, MFloatVector) -> self
		setParameter(parameterName, MMatrix) -> self
		setParameter(parameterName, MFloatMatrix) -> self
		setParameter(parameterName, MTexture) -> self
		setParameter(parameterName, MRenderTarget) -> self
		setParameter(parameterName, MSamplerState) -> self

		Set the value of the named parameter."""
	@overload
	def setParameter(self,parameterName:str,MRenderTarget:Any)->Self:
		"""setParameter(parameterName, bool) -> self
		setParameter(parameterName, int) -> self
		setParameter(parameterName, float) -> self
		setParameter(parameterName, list of float) -> self
		setParameter(parameterName, MFloatVector) -> self
		setParameter(parameterName, MMatrix) -> self
		setParameter(parameterName, MFloatMatrix) -> self
		setParameter(parameterName, MTexture) -> self
		setParameter(parameterName, MRenderTarget) -> self
		setParameter(parameterName, MSamplerState) -> self

		Set the value of the named parameter."""
	@overload
	def setParameter(self,parameterName:str,MSamplerState:Any)->Self:
		"""setParameter(parameterName, bool) -> self
		setParameter(parameterName, int) -> self
		setParameter(parameterName, float) -> self
		setParameter(parameterName, list of float) -> self
		setParameter(parameterName, MFloatVector) -> self
		setParameter(parameterName, MMatrix) -> self
		setParameter(parameterName, MFloatMatrix) -> self
		setParameter(parameterName, MTexture) -> self
		setParameter(parameterName, MRenderTarget) -> self
		setParameter(parameterName, MSamplerState) -> self

		Set the value of the named parameter."""
	def techniqueNames(self)->list[str]:
		"""techniqueNames() -> list of strings

		Returns a list of the technique names for the effect."""
	def techniqueAnnotation(self,annotationName:str)->int|float|str:
		"""techniqueAnnotation(annotationName) -> int / float / string

		Returns the value of the current technique annotation.

		 * annotationName (string) - The name of the technique annotation."""
	def uiName(self,parameterName:str)->str:
		"""uiName(parameterName) -> string

		Returns the UI name associated with a named parameter.
		The UI name can be specified in shader using the 'UIName' annotation.
		The UI name can be used to specify the name that will be displayed in the Attribute Editor."""
	def uiWidget(self,parameterName:str)->str:
		"""uiWidget(parameterName) -> string

		Returns the UI widget type associated with a named parameter.
		The UI widget type can be specified in shader using the 'UIWidget' annotation.The UI widget can be used to specify which widget should be used to control the parameter in the Attribute Editor."""
	def unbind(self,MDrawContext:Any)->Self:
		"""unbind(MDrawContext) -> self
		Unbinds the shader instance from the draw context."""
	def updateParameters(self,MDrawContext:Any)->Self:
		"""updateParameters(MDrawContext) -> self
		Updates the bound shader instance with the current parameter data."""
	def requiredVertexBuffers(self,MVertexBufferDescriptorList:Any)->Self:
		"""requiredVertexBuffers(MVertexBufferDescriptorList) -> self
		Get the vertex buffer descriptors that describe the buffers required
		by a given shader instance."""
	def writeEffectSourceToFile(self,filePath:Any)->Self:
		"""writeEffectSourceToFile(filePath) -> self
		Write the source of the final OGSFX/HLSL/CgFX effect to a specified file. Use
		this for debugging to see how fragments are turned into the final effect for
		the current drawing API.

		Note that the effect will not be written if the effect is not generated from
		shader fragments or any of the shader fragments is marked as hidden."""
class MShaderManager:
	"""Provides access to MShaderInstance objects for use in Viewport 2.0."""
	k3dSolidShader:int=0
	k3dBlinnShader:int=1
	k3dDefaultMaterialShader:int=2
	k3dSolidTextureShader:int=3
	k3dCPVFatPointShader:int=4
	k3dColorLookupFatPointShader:int=5
	k3dOpacityLookupFatPointShader:int=6
	k3dColorOpacityLookupFatPointShader:int=7
	k3dShadowerShader:int=8
	k3dFatPointShader:int=9
	k3dThickLineShader:int=10
	k3dCPVThickLineShader:int=11
	k3dDashLineShader:int=12
	k3dCPVDashLineShader:int=13
	k3dStippleShader:int=14
	k3dThickDashLineShader:int=15
	k3dCPVThickDashLineShader:int=16
	k3dDepthShader:int=17
	k3dCPVSolidShader:int=18
	k3dIntegerNumericShader:int=19
	k3dFloatNumericShader:int=20
	k3dFloat2NumericShader:int=21
	k3dFloat3NumericShader:int=22
	k3dPointVectorShader:int=23
	k3dPointLightShadowerShader:int=24
	k3dStandardSurfaceShader:int=25
	k3dIsotropicStandardSurfaceShader:int=26
	k3dOpenPBRSurfaceShader:int=27
	k3dIsotropicOpenPBRSurfaceShader:int=28
	k3dCPVShader:int=4
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def addShaderIncludePath(self,string:Any)->Self:
		"""addShaderIncludePath(string) -> self

		Add a path to the list of paths used for searching for shader include files."""
	def addShaderPath(self,string:Any)->Self:
		"""addShaderPath(string) -> self

		Add a path to the list of shader search paths."""
	def getEffectsBufferShader(self,buffer:Any,size:int,techniqueName:str,macros:Sequence[MShaderCompileMacro]|None=None,useEffectCache:bool=True,preCb:function|None=None,postCb:function|None=None)->MShaderInstance:
		"""getEffectsBufferShader(buffer, size, techniqueName, macros=None, useEffectCache=True, preCb=None, postCb=None) -> MShaderInstance

		Get a new instance of a shader generated from a block of memory containing device-specific source code (as char*).

		* buffer (const void*) - A pointer to the block of memory from which to load the effect.
		* size (unsigned int) - The size of the effect to load in bytes.
		* techniqueName (string) - The name of a technique in the effect. If an empty string is specified then the first technique in the effect will be used.
		* macros (sequence of MShaderCompileMacro) - Sequence of shader macros. The default value is None, meaning that no macros are specified.
		* useEffectCache (bool) - Use the internal effect cache to prevent reloading the effect every time it is requested. The default value is True.
		* preCb (function) - A function, or other Python callable, to be called before render items are drawn with this shader.
		* postCb (function) - A function, or other Python callable, to be called after render items are drawn with this shader.
		      see MShaderManager.getEffectsFileShader() for details on the preCb and postCb functions"""
	def getEffectsFileShader(self,effecsFileName:str,techniqueName:str,macros:Sequence[MShaderCompileMacro]|None=None,useEffectCache:bool=True,preCb:function|None=None,postCb:function|None=None)->MShaderInstance:
		"""getEffectsFileShader(effecsFileName, techniqueName, macros=None, useEffectCache=True, preCb=None, postCb=None) -> MShaderInstance

		Get a new instance of a shader generated from an effects file stored on disk.

		* effectsFileName (string) - The effects file.
		* techniqueName (string) - The name of a technique in the effects file. If an empty string is specified then the first technique in the effects file will be used.
		* macros (sequence of MShaderCompileMacro) - Sequence of shader macros. The default value is None, meaning that no macros are specified.
		* useEffectCache (bool) - Use the internal effect cache to prevent reloading the effect file every time it is requested. The default value is True.
		* preCb (function) - A function, or other Python callable, to be called before render items are drawn with this shader.
		          def preCb(MDrawContext, MRenderItemList, MShaderInstance)
		* postCb (function) - A function, or other Python callable, to be called after render items are drawn with this shader.
		          def postCb(MDrawContext, MRenderItemList, MShaderInstance)"""
	def getEffectsTechniques(self,effecsFileName:str,macros:Sequence[MShaderCompileMacro]|None=None,useEffectCache:bool=True)->tuple[str,...]:
		"""getEffectsTechniques(effecsFileName, macros=None, useEffectCache=True) -> tuple of strings

		Analyzes a given effect file to extract the names of the techniques that are defined.

		* effectsFileName (string) - The effects file.
		* macros (sequence of MShaderCompileMacro) - Sequence of shader macros. The default value is None, meaning that no macros are specified.
		* useEffectCache (bool) - Use the internal effect cache to prevent reloading the effect every time it is requested. The default value is True."""
	def getFragmentShader(self,fragmentName:str,structOutputName:str,decorateFragment:bool,preCb:function|None=None,postCb:function|None=None)->MShaderInstance:
		"""getFragmentShader(fragmentName, structOutputName, decorateFragment, preCb=None, postCb=None) -> MShaderInstance

		Get a new instance of a shader generated from a named shader fragment or fragment graph.

		* fragmentName (string) - The name of the fragment to generate a shader from.
		* structOutputName (string) - If the output of the fragment is a struct, use this parameter to specify which member of the struct to use.
		                                                                 This parameter is ignored if the output of the fragment is not a struct.
		* decorateFragment (bool) - If True, Maya state fragments will be added.
		* preCb (function) - A function, or other Python callable, to be called before render items are drawn with this shader.
		* postCb (function) - A function, or other Python callable, to be called after render items are drawn with this shader.
		      see MShaderManager.getEffectsFileShader() for details on the preCb and postCb functions"""
	def getShaderFromNode(self,shaderNode:om.MObject,shapePath:om.MDagPath,linkLostCb:function|None=None,linkLostUserData:om.MUserData|None=None,preCb:function|None=None,postCb:function|None=None,nonTextured:bool=False)->MShaderInstance:
		"""getShaderFromNode(shaderNode, shapePath, linkLostCb=None, linkLostUserData=None, preCb=None, postCb=None, nonTextured=False) -> MShaderInstance

		Get the shader instance by evaluating the shading network of a surface shader node (either standard or custom) in the scene.

		If the surface shader node is NULL or supported by neither Maya nor the plug-in, this method will return NULL.

		The shape path is used as the object context for shading network evaluation to ensure that the shader instance fits its requirements. If the shape path is invalid (e.g. an empty path), a shader instance to fit basic requirements is created but will not include any geometry-dependent requirements.

		The linkLostCb will be invoked whenever the link to the surface shader node is lost. The link can be lost in a number of ways, e.g. shader nodes are deleted or shading network connections are modified. However, the linkLostCb will not be invoked for changes to a shading group; if needed, it is the plug-in's responsibility to monitor any changes to the shading group (via MNodeMessage and/or MPxNode::connectionMade/connectionBroken).

		After the shader instance is created, its parameter values can be automatically updated by Viewport 2.0 whenever the related shading attributes are changed, thus no attempt should be made to override parameter values of the shader instance manually.

		* shaderNode (MObject) - The surface shader node.
		* shapePath (MDagPath) - The DAG path of a shape to be used as the object context for shading network evaluation.
		* linkLostCb (function) - A function, or other Python callable, to be called when this shader instance is no longer connected to the node it was translated for.
		          def linkLostCb(MShaderInstance, MUserData)
		* linkLostUserData (MUserData) - User supplied data to be passed into the link lost callback.
		       This data will not be deleted internally and the lifetime must be managed by the caller.
		       The link lost callback will only be called once so it is safe to delete this data anytime after the callback has been triggered.
		* preCb (function) - A function, or other Python callable, to be called before render items are drawn with this shader.
		* postCb (function) - A function, or other Python callable, to be called after render items are drawn with this shader.
		      see MShaderManager.getEffectsFileShader() for details on the preCb and postCb functions.
		* nonTextured (bool) - Whether or not a non-textured effect instance is needed. The default value is false."""
	def getStockShader(self,shaderId:int,preCb:function|None=None,postCb:function|None=None)->MShaderInstance:
		"""getStockShader(shaderId, preCb=None, postCb=None) -> MShaderInstance

		Get a new instance of a stock shader.

		* shaderId (int) - The Id of stock shader.
		* preCb (function) - A function, or other Python callable, to be called before render items are drawn with this shader.
		* postCb (function) - A function, or other Python callable, to be called after render items are drawn with this shader.
		      see MShaderManager.getEffectsFileShader() for details on the preCb and postCb functions

		List of available stock shader:
		  k3dSolidShader                  An instance of a solid color shader for 3d rendering
		  k3dBlinnShader                  An instance of a Blinn shader for 3d rendering
		  k3dDefaultMaterialShader        An instance of a stock "default material" shader for 3d rendering
		  k3dSolidTextureShader           An instance of a stock solid texture shader for 3d rendering
		  k3dCPVFatPointShader            An instance of a stock color per vertex fat point shader for 3d rendering
		  k3dColorLookupFatPointShader    An instance of a stock fat point shader using a 1D color texture lookup.
		  k3dShadowerShader               An instance of a stock shader which can be used when rendering shadow maps
		  k3dFatPointShader               An instance of a stock fat point shader for 3d rendering
		  k3dThickLineShader              An instance of a stock thick line shader for 3d rendering
		  k3dCPVThickLineShader           An instance of a color per vertex stock thick line shader for 3d rendering
		  k3dDashLineShader               An instance of a stock dash line shader for 3d rendering
		  k3dCPVDashLineShader            An instance of a color per vertex stock dash line shader for 3d rendering
		  k3dStippleShader                An instance of a stipple shader for drawing 3d filled triangles
		  k3dThickDashLineShader          An instance of a stock thick dash line shader for 3d rendering.
		  k3dCPVThickDashLineShader       An instance of a color per vertex stock thick dash line shader for 3d rendering.
		  k3dDepthShader                  An instance of a stock shader that can be used for 3d rendering of depth
		  k3dCPVSolidShader               An instance of a stock solid color per vertex shader for 3d rendering
		  k3dIntegerNumericShader         An instance of a stock shader for drawing single integer values per vertex for 3d rendering.
		  k3dFloatNumericShader           An instance of a stock shader for drawing single float values values per vertex for 3d rendering.
		  k3dFloat2NumericShader          An instance of a stock shader for drawing 2 float values per vertex for 3d rendering.
		  k3dFloat3NumericShader          An instance of a stock shader for drawing 3 float values per vertex for 3d rendering.
		  k3dPointVectorShader            An instance of a stock shader that can be used for 3d rendering of lines based on a point and a vector stream"""
	@staticmethod
	def isSupportedShaderSemantic(string:Any)->bool:
		"""isSupportedShaderSemantic(string) -> bool
		Return if a given string is a supported shader semantic."""
	def releaseShader(self,MShaderInstance:Any)->None:
		"""releaseShader(MShaderInstance) -> None
		Deletes the MShaderInstance and releases its reference to the underlying shader which is held by the MShaderInstance object."""
	def clearEffectCache(self)->Self:
		"""clearEffectCache() -> self
		Clear the effect cache.
		This will allow all relevant effects to be updated when the implementation of a shader fragment or fragment graph has been modified."""
	def removeEffectFromCache(self,effecsFileName:str,techniqueName:str,macros:Sequence[MShaderCompileMacro]|None=None)->Self:
		"""removeEffectFromCache(effecsFileName, techniqueName, macros=None) -> self
		Remove an effect from the cache.
		This is particulary useful when calling the getEffectsTechniques() and/or getEffectsFileShader() with the flag useEffectCache set to True for maximum performance, and will allow reloading the effect from the disk when the shader file has been modified.
		* effectsFileName (string) - The effects file.
		* techniqueName (string) - The name of a technique in the effects file. If an empty string is specified then the first technique in the effects file will be used.
		* macros (sequence of MShaderCompileMacro) - Sequence of shader macros. The default value is None, meaning that no macros are specified."""
	def shaderIncludePaths(self)->list[str]:
		"""shaderIncludePaths() -> list of strings

		Query the list of search paths user for searching for shader include files."""
	def shaderPaths(self)->list[str]:
		"""shaderPaths() -> list of strings

		Query the list of shader search paths."""
	@staticmethod
	def getLastError()->str:
		"""getLastError() -> string

		Get the description of the last error encountered by the shader manager regarding an effect.
		This includes fragment and effect loading, technique query, and shader binding."""
	@staticmethod
	def getLastErrorSource(displayLineNumber:bool=False,filterSource:bool=False,numSurroundingLines:int=2)->str:
		"""getLastErrorSource(displayLineNumber=False, filterSource=False, numSurroundingLines=2) -> string

		Get the source of the shader that generated the last error. See getLastError().
		 * displayLineNumber (bool) - If True, add the number line at the beginning of each line. The default is False.
		 * filterSource (bool) - If True, only display the lines surrounding the error(s). The default is False.
		 * numSurroundingLines (int) - The number of leading and trailing lines to display around filtered source. The default is 2."""
class MStateManager:
	"""Class to allow efficient access to GPU state information."""
	kCompareNever:int=1
	kCompareLess:int=2
	kCompareEqual:int=3
	kCompareLessEqual:int=4
	kCompareGreater:int=5
	kCompareNotEqual:int=6
	kCompareGreaterEqual:int=7
	kCompareAlways:int=8
	kNoShader:int=0
	kVertexShader:int=1
	kGeometryShader:int=2
	kPixelShader:int=3
	kHullShader:int=4
	kDomainShader:int=5
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	@staticmethod
	def acquireBlendState(MBlendStateDesc:Any)->MBlendState:
		"""acquireBlendState(MBlendStateDesc) -> MBlendState

		Acquires an immutable unique blend state matching the blend state descriptor."""
	@staticmethod
	def releaseBlendState(MBlendState:Any)->None:
		"""releaseBlendState(MBlendState) -> None

		Deletes the MBlendState and releases the reference to the underlying state object which is held by the MBlendState object."""
	def setBlendState(self,MBlendState:Any)->Self:
		"""setBlendState(MBlendState) -> self

		Sets the active blend state on the device."""
	def getBlendState(self)->MBlendState:
		"""getBlendState() -> MBlendState

		Gets the current active blend state from the device."""
	@staticmethod
	def acquireRasterizerState(MRasterizerStateDesc:Any)->MRasterizerState:
		"""acquireRasterizerState(MRasterizerStateDesc) -> MRasterizerState

		Acquires an immutable unique rasterizer state matching the rasterizer state descriptor."""
	@staticmethod
	def releaseRasterizerState(MRasterizerState:Any)->None:
		"""releaseRasterizerState(MRasterizerState) -> None

		Deletes the MRasterizerState and releases the reference to the underlying state object which is held by the MRasterizerState object."""
	def setRasterizerState(self,MRasterizerState:Any)->Self:
		"""setRasterizerState(MRasterizerState) -> self

		Sets the active rasterizer state on the device."""
	def getRasterizerState(self)->MRasterizerState:
		"""getRasterizerState() -> MRasterizerState

		Gets the current active rasterizer state from the device."""
	@staticmethod
	def acquireDepthStencilState(MDepthStencilStateDesc:Any)->MDepthStencilState:
		"""acquireDepthStencilState(MDepthStencilStateDesc) -> MDepthStencilState

		Acquires an immutable unique depth-stencil state matching the blend state descriptor."""
	@staticmethod
	def releaseDepthStencilState(MDepthStencilState:Any)->None:
		"""releaseDepthStencilState(MDepthStencilState) -> None

		Deletes the MDepthStencilState and releases the reference to the underlying state object which is held by the MDepthStencilState object."""
	def setDepthStencilState(self,MDepthStencilState:Any)->Self:
		"""setDepthStencilState(MDepthStencilState) -> self

		Sets the active depth-stencil state on the device."""
	def getDepthStencilState(self)->MDepthStencilState:
		"""getDepthStencilState() -> MDepthStencilState

		Gets the current depth-stencil blend state from the device."""
	@staticmethod
	def acquireSamplerState(MSamplerStateDesc:Any)->MSamplerState:
		"""acquireSamplerState(MSamplerStateDesc) -> MSamplerState

		Acquires an immutable unique sampler state matching the blend state descriptor."""
	@staticmethod
	def releaseSamplerState(MSamplerState:Any)->None:
		"""releaseSamplerState(MSamplerState) -> None

		Deletes the MSamplerState and releases the reference to the underlying state object which is held by the MSamplerState object."""
	def setSamplerState(self,shader:int,samplerIndex:int,samplerState:MSamplerState)->Self:
		"""setSamplerState(shader, samplerIndex, samplerState) -> self

		Sets the active sampler state for any of the texture samplers on the device.
		* shader (ShaderType) - The shader this sampler will apply to, e.g. kPixelShader.
		* samplerIndex (int) - The index of the sampler to set with the given shader state.
		* samplerState (MSamplerState) - The sampler state container object that was previously acquired."""
	def getSamplerState(self,shader:int,samplerIndex:int)->MSamplerState:
		"""getSamplerState(shader, samplerIndex) -> MSamplerState

		Gets the current active sampler state from the device.
		* shader (ShaderType) - The shader this sampler will apply to.
		* samplerIndex (int) - The index of the sampler to set with the given shader state."""
	@staticmethod
	def getMaxSamplerCount()->int:
		"""getMaxSamplerCount() -> int

		Get the maximum number of simulataneous texture coordinate interpolation channels."""
class MStencilOpDesc:
	"""Descriptor for a depth-stencil operation."""
	@property
	def stencilPassOp(self)->Any:
		"""Stencil op to use when the fragment passes the stencil test, default kKeepStencil"""
	@stencilPassOp.setter
	def stencilPassOp(self,value:Any)->None:...
	@property
	def stencilFailOp(self)->Any:
		"""Stencil op to use when the fragment fails the stencil test, default kKeepStencil"""
	@stencilFailOp.setter
	def stencilFailOp(self,value:Any)->None:...
	@property
	def stencilDepthFailOp(self)->Any:
		"""Stencil op to use when the fragment passes the depth test, default kKeepStencil"""
	@stencilDepthFailOp.setter
	def stencilDepthFailOp(self,value:Any)->None:...
	@property
	def stencilFunc(self)->Any:
		"""Sets the stencil buffer comparison function, default kCompareAlways"""
	@stencilFunc.setter
	def stencilFunc(self,value:Any)->None:...
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def setDefaults(self)->Self:
		"""setDefaults() -> self

		Set all values for the stencil operation state to their default values."""
class MSubSceneContainer:
	"""Container for render items generated by MPxSubSceneOverride."""
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def __len__(self)->int:
		"""Return len(self)."""
	def add(self,item:MRenderItem)->bool:
		"""add(item) -> bool

		Add a render item to the set of render items that will be used to draw the DAG object associated with the override that owns this container. Each item in the container must have a unique name and the same render item may not be used in the container more than once. When Viewport 2.0 draws the associated DAG object, it will process all render items in this container.
		Any items that have valid geometry and a valid shader will be drawn as long as they pass all filtering tests for the active viewport.

		On successful add, Maya assumes ownership of the render item and the caller should not call MRenderItem.destroy() on the item. Callers are free to hold the render item for easy access. Note that any MRenderItem objects added to MSubSceneContainer become invalid after the render item is removed from the container. Attempts to use such object will result in instability. Further note that it is invalid to modify any render item owned by this container outside of MPxSubSceneOverride.update().
		Attempts to do so will result in unpredictable behavior.

		* item (MRenderItem) - The item to add."""
	def clear(self)->Self:
		"""clear() -> self

		Remove all render items from this container. After calling, any render items owned by this container will be invalid."""
	def count(self)->int:
		"""count() -> int

		Get the number of render items in the container."""
	def find(self,name:str)->MRenderItem:
		"""find(name) -> MRenderItem

		Get a render item by name from the container. The ownership of the render item remains with the container and callers should not call MRenderItem.destroy() on it. The render items may be cached and will remain valid until removed from the container.

		* name (string) - The name of the render item to retrieve."""
	def getIterator(self)->MSubSceneContainerIterator:
		"""getIterator() -> MSubSceneContainerIterator

		Get an iterator for the container.
		Caller is responsible for deleting the iterator when it is no longer needed."""
	def remove(self,name:str)->bool:
		"""remove(name) -> bool

		Remove a render item by name from the set of render items used to draw the object associated with the override that owns this container. Note that on successful removal any render item that was removed become invalid and any attempts to use such items will result in instability.

		* name (string) - The name of the render item to remove."""
class MSubSceneContainerIterator:
	"""Iterator over render items of MSubSceneContainer object."""
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def destroy(self)->Self:
		"""destroy() -> self

		Call this method to delete the iterator. After calling, the iterator will be invalid.
		Users of MSubSceneContainer iterators are responsible for deleting the iterators after use."""
	def next(self)->MRenderItem:
		"""next() -> MRenderItem

		Advance the iterator to the next render item in the associated MSubSceneContainer and return it.

		Returns the next render item in the container or None if no more items."""
	def reset(self)->Self:
		"""reset() -> self

		Reset the iterator to the beginning of the associated MSubSceneContainer.
		The next call to the next() method will return the first render item in the container."""
class MSwatchRenderBase:
	"""Swatch Render Base class."""
	@property
	def renderQuality(self)->Any:
		"""The quality in which the swatch will be rendered (the larger the number is set, the better quality is applied)."""
	@renderQuality.setter
	def renderQuality(self,value:Any)->None:...
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	@staticmethod
	def cancelCurrentSwatchRender()->None:
		"""cancelCurrentSwatchRender() -> None

		The method cancels the swatch which is being rendered in parallel, and push the swatch render item back to the render queue after.

		The render plugins should make sure that MSwatchRenderBase.cancelParallelRendering() is implemented acoordingly."""
	def cancelParallelRendering(self)->Self:
		"""cancelParallelRendering() -> self

		Method to cancel the parallel rendering.
		The derived classes should provide the implementation accordingly if required."""
	def doIteration(self)->bool:
		"""doIteration() -> bool

		Method called from the MSwatchRenderRegister for generation of swatch image. The doIteration function is called repeatedly (during idle events) until it returns true. Using this swatch image can be generated in stages.

		This method should be overridden in derived classes which can compute the swatches in several steps.

		Returns False as long as the swatch computation is not completed."""
	def finishParallelRender(self)->Self:
		"""finishParallelRender() -> self

		Method to update the swatch image when the parallel rendering is finished.
		If swatch is rendered parallel, this method must be called after parallel rendering finished."""
	def image(self)->om.MImage:
		"""image() -> MImage

		This method returns the render swatch as an image."""
	def node(self)->om.MObject:
		"""node() -> MObject

		This method returns the node that is used to compute the swatch."""
	def renderParallel(self)->bool:
		"""renderParallel() -> bool

		Method indicates if the swatch is rendered parallel.
		Default is False."""
	def resolution(self)->int:
		"""resolution() -> int

		This method returns the expected resolution of the swatch."""
	def swatchNode(self)->om.MObject:
		"""swatchNode() -> MObject

		This method returns the node for which the swatch is required to be generated."""
class MTargetBlendDesc:
	"""Descriptor for a blend state for a single render target."""
	@property
	def blendEnable(self)->Any:
		"""Enable blending on this target, default is False"""
	@blendEnable.setter
	def blendEnable(self,value:Any)->None:...
	@property
	def sourceBlend(self)->Any:
		"""The blend factor for the source color, default is one"""
	@sourceBlend.setter
	def sourceBlend(self,value:Any)->None:...
	@property
	def destinationBlend(self)->Any:
		"""The blend factor for the destination color, default is zero"""
	@destinationBlend.setter
	def destinationBlend(self,value:Any)->None:...
	@property
	def blendOperation(self)->Any:
		"""The blend operation, default is add"""
	@blendOperation.setter
	def blendOperation(self,value:Any)->None:...
	@property
	def alphaSourceBlend(self)->Any:
		"""The blend factor for the source alpha, default is one"""
	@alphaSourceBlend.setter
	def alphaSourceBlend(self,value:Any)->None:...
	@property
	def alphaDestinationBlend(self)->Any:
		"""The blend factor for the destination alpha, default is zero"""
	@alphaDestinationBlend.setter
	def alphaDestinationBlend(self,value:Any)->None:...
	@property
	def alphaBlendOperation(self)->Any:
		"""The blend operation for alpha, default is add"""
	@alphaBlendOperation.setter
	def alphaBlendOperation(self,value:Any)->None:...
	@property
	def targetWriteMask(self)->Any:
		"""Indicates what color components(red, green, blue, alpha) are writable, the default is RGBA"""
	@targetWriteMask.setter
	def targetWriteMask(self,value:Any)->None:...
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def setDefaults(self)->Self:
		"""setDefaults() -> self

		Set all values for the target blend state to their default values."""
class MTexture:
	"""Class which includes texture data."""
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def hasAlpha(self)->bool:
		"""hasAlpha() -> bool

		Get whether the texture has an alpha channel."""
	def setHasAlpha(self,bool:bool)->Self:
		"""setHasAlpha(bool) -> self

		Specify that the texture has an alpha channel."""
	def hasZeroAlpha(self)->bool:
		"""hasZeroAlpha() -> bool

		Get whether the texture has any texels with an alpha value of 0.0."""
	def setHasZeroAlpha(self,bool:bool)->Self:
		"""setHasZeroAlpha(bool) -> self

		Specify that the texture has texels with an alpha value of 0.0."""
	def hasTransparentAlpha(self)->bool:
		"""hasTransparentAlpha() -> bool

		Get whether the texture has semi-transparent texels."""
	def setHasTransparentAlpha(self,bool:bool)->Self:
		"""setHasTransparentAlpha(bool) -> self

		Specify that the texture has texels with an alpha value greater than or equal to 0.0 and less than 1.0."""
	def resourceHandle(self)->int:
		"""resourceHandle() -> long

		Returns a long containing a C++ 'void' pointer which points to the texture."""
	def name(self)->str:
		"""name() -> string

		Get the name of the texture."""
	def bytesPerPixel(self)->int:
		"""bytesPerPixel() -> int

		Get the number of bytes per pixel in the texture."""
	def textureDescription(self)->MTextureDescription:
		"""textureDescription() -> MTextureDescription

		Get texture description."""
	def rawData(self)->tuple[int,rowPitch,slicePitch]:
		"""rawData() -> (long, rowPitch, slicePitch)

		Returns a long containing a C++ 'void' pointer which points to the raw data mapped to the texture.
		The caller must deallocate the system memory (using freeRawData()) as the texture itself does not keep any references to it.

		* rowPitch [OUT] (int) - The row pitch of the data. It represents the number of bytes of one line of the texture data.
		* slicePitch [OUT] (int) - The slice pitch of the data. It represents the number of bytes of the whole texture data."""
	@staticmethod
	def freeRawData(long:Any)->None:
		"""freeRawData(long) -> None
		Deallocate system memory - retrieved from rawData()."""
	@overload
	def update(self,pixelData:void,generateMipMaps:bool,rowPitch:int=0,region:MTextureUpdateRegion|None=None)->Self:
		"""update(pixelData, generateMipMaps, rowPitch=0, region=None) -> self
		update(image, generateMipMaps) -> selfupdate(textureNode) -> self

		Update the contents of an image with new data.

		From pixel data:
		* pixelData (void*) - Data to update the texture with.
		* generateMipMaps (bool) - Indicate if mip-maps levels for the texture be rebuilt.
		* rowPitch (int) The row pitch of the incoming data.
		* region (MTextureUpdateRegion) - Texture sub-region to update. If a None is passed in then the input data is assumed to be updating the entire texture.
		From an image:
		* image (MImage) - Image containing data to update the texture with.
		* generateMipMaps (bool) - Indicate if mip-maps levels for the texture be rebuilt.
		From a texture node:
		* textureNode (MObject) - File texture node"""
	@overload
	def update(self,image:om.MImage,generateMipMaps:bool)->Self:
		"""update(pixelData, generateMipMaps, rowPitch=0, region=None) -> self
		update(image, generateMipMaps) -> selfupdate(textureNode) -> self

		Update the contents of an image with new data.

		From pixel data:
		* pixelData (void*) - Data to update the texture with.
		* generateMipMaps (bool) - Indicate if mip-maps levels for the texture be rebuilt.
		* rowPitch (int) The row pitch of the incoming data.
		* region (MTextureUpdateRegion) - Texture sub-region to update. If a None is passed in then the input data is assumed to be updating the entire texture.
		From an image:
		* image (MImage) - Image containing data to update the texture with.
		* generateMipMaps (bool) - Indicate if mip-maps levels for the texture be rebuilt.
		From a texture node:
		* textureNode (MObject) - File texture node"""
	@overload
	def update(self,textureNode:om.MObject)->Self:
		"""update(pixelData, generateMipMaps, rowPitch=0, region=None) -> self
		update(image, generateMipMaps) -> selfupdate(textureNode) -> self

		Update the contents of an image with new data.

		From pixel data:
		* pixelData (void*) - Data to update the texture with.
		* generateMipMaps (bool) - Indicate if mip-maps levels for the texture be rebuilt.
		* rowPitch (int) The row pitch of the incoming data.
		* region (MTextureUpdateRegion) - Texture sub-region to update. If a None is passed in then the input data is assumed to be updating the entire texture.
		From an image:
		* image (MImage) - Image containing data to update the texture with.
		* generateMipMaps (bool) - Indicate if mip-maps levels for the texture be rebuilt.
		From a texture node:
		* textureNode (MObject) - File texture node"""
class MTextureAssignment:
	"""Structure to hold the information required to set a texture parameter on a shader using a texture as input."""
	@property
	def texture(self)->Any:
		"""The texture"""
	@texture.setter
	def texture(self,value:Any)->None:...
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
class MTextureDescription:
	"""Texture description. Provides sufficient information to describe how a block of data can be interpreted as a texture."""
	@property
	def fWidth(self)->Any:
		"""Width in pixels"""
	@fWidth.setter
	def fWidth(self,value:Any)->None:...
	@property
	def fHeight(self)->Any:
		"""Height in pixels"""
	@fHeight.setter
	def fHeight(self,value:Any)->None:...
	@property
	def fDepth(self)->Any:
		"""Depth in pixels. A 2D texture has depth of 1."""
	@fDepth.setter
	def fDepth(self,value:Any)->None:...
	@property
	def fBytesPerRow(self)->Any:
		"""Number of bytes in a row of pixels"""
	@fBytesPerRow.setter
	def fBytesPerRow(self,value:Any)->None:...
	@property
	def fBytesPerSlice(self)->Any:
		"""Number of bytes in a slice (if an array)"""
	@fBytesPerSlice.setter
	def fBytesPerSlice(self,value:Any)->None:...
	@property
	def fMipmaps(self)->Any:
		"""Number of mipmap levels. 0 means the entire mipmap chain."""
	@fMipmaps.setter
	def fMipmaps(self,value:Any)->None:...
	@property
	def fArraySlices(self)->Any:
		"""Number of array slices. e.g. 6 would be required for a cube-map"""
	@fArraySlices.setter
	def fArraySlices(self,value:Any)->None:...
	@property
	def fFormat(self)->Any:
		"""Pixel / raster format"""
	@fFormat.setter
	def fFormat(self,value:Any)->None:...
	@property
	def fTextureType(self)->Any:
		"""Type of texture"""
	@fTextureType.setter
	def fTextureType(self,value:Any)->None:...
	@property
	def fEnvMapType(self)->Any:
		"""Type of environment mapping"""
	@fEnvMapType.setter
	def fEnvMapType(self,value:Any)->None:...
	kImage1D:int=0
	kImage1DArray:int=1
	kImage2D:int=2
	kImage2DArray:int=3
	kCubeMap:int=4
	kVolumeTexture:int=5
	kDepthTexture:int=6
	kNumberOfTextureTypes:int=7
	kEnvNone:int=0
	kEnvSphere:int=1
	kEnvHemiSphere:int=2
	kEnvLatLong:int=3
	kEnvCrossVert:int=4
	kEnvCrossHoriz:int=5
	kEnvCubemap:int=6
	kNumberOfEnvMapTypes:int=7
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def setToDefault2DTexture(self)->Self:
		"""setToDefault2DTexture() -> self

		Utility to set texture description to describe a 0 size 2-dimensional texture."""
class MTextureManager:
	"""Class which manages texture."""
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def addImagePath(self,string:Any)->Self:
		"""addImagePath(string) -> self

		Adds an additional search path for looking up images on disk."""
	def imagePaths(self)->list[str]:
		"""imagePaths() -> list of strings

		Get the current set of image search paths."""
	@overload
	def acquireTexture(self,filePath:str,mipmapLevels:int=0,layerName:str="",alphaChannelIdx:int=-1)->MTexture:
		"""(Deprecated) acquireTexture(filePath, mipmapLevels=0, layerName="", alphaChannelIdx=-1) -> MTexture
		acquireTexture(filePath, contextNodeFullName, mipmapLevels=0, layerName="", alphaChannelIdx=-1) -> MTexture
		acquireTexture(textureName, plug, width, height, generateMipMaps=True) -> MTexture
		acquireTexture(textureName, textureDesc, pixelData, generateMipMaps=True) -> MTexture
		acquireTexture(fileNode, allowBackgroundLoad=False) -> MTexture

		Ask the renderer to acquire a hardware texture.

		Acquire a hardware texture from an image file:
		* filePath (string) - Image file name
		* contextNodeFullName (string) Full name of the texture owner Node to be provided as a context to the Maya resolver* mipmapLevels (int) - Mipmap generation levels
		* layerName (string) - The name of the layer to load, this is only relevant for PSD files, otherwise it will have no effect
		* alphaChannelIdx (int) - The index of the alpha channel to load, this is only relevant for PSD files, otherwise it will have no effect

		If a plug to a file texture node is provided then the name, width, height and
		generateMipMaps parameters will be ignored as this information will be
		based on the image on disk associated with texture node. If uv tiling is
		enabled, currently only the first tile will be returned.
		Otherwise, an attempt to bake a texture will be made using the Maya's software
		renderer convert-to-solid-texture functionality.
		* textureName (string) - Name of the texture to create
		* plug (MPlug) - Plug which is attached with a texture
		* width (int) - Width of the texture
		* height (int) - Height of the texture
		* generateMipMaps (bool) - Generate the mipmap levels

		Acquire a hardware texture by providing a texture description and a block of system memory data which matches the texture description:
		* textureName (string) - Name of the texture to create
		* textureDesc (MTextureDescription) - Description of the texture
		* pixelData (void*) - Block of system memory data which matches the texture description
		* generateMipMaps (bool) - Generate the mipmap levels
		Acquire the texture associated with a given texture node. Currently only file texture nodes are supported.
		If uv tiling is enabled, currently only the first tile will be returned.
		* textureNode (MObject) - Node to acquire texture from
		* allowBackgroundLoad (bool) - Allow for background texture loading. The default value is false."""
	@overload
	def acquireTexture(self,filePath:str,contextNodeFullName:str,mipmapLevels:int=0,layerName:str="",alphaChannelIdx:int=-1)->MTexture:
		"""(Deprecated) acquireTexture(filePath, mipmapLevels=0, layerName="", alphaChannelIdx=-1) -> MTexture
		acquireTexture(filePath, contextNodeFullName, mipmapLevels=0, layerName="", alphaChannelIdx=-1) -> MTexture
		acquireTexture(textureName, plug, width, height, generateMipMaps=True) -> MTexture
		acquireTexture(textureName, textureDesc, pixelData, generateMipMaps=True) -> MTexture
		acquireTexture(fileNode, allowBackgroundLoad=False) -> MTexture

		Ask the renderer to acquire a hardware texture.

		Acquire a hardware texture from an image file:
		* filePath (string) - Image file name
		* contextNodeFullName (string) Full name of the texture owner Node to be provided as a context to the Maya resolver* mipmapLevels (int) - Mipmap generation levels
		* layerName (string) - The name of the layer to load, this is only relevant for PSD files, otherwise it will have no effect
		* alphaChannelIdx (int) - The index of the alpha channel to load, this is only relevant for PSD files, otherwise it will have no effect

		If a plug to a file texture node is provided then the name, width, height and
		generateMipMaps parameters will be ignored as this information will be
		based on the image on disk associated with texture node. If uv tiling is
		enabled, currently only the first tile will be returned.
		Otherwise, an attempt to bake a texture will be made using the Maya's software
		renderer convert-to-solid-texture functionality.
		* textureName (string) - Name of the texture to create
		* plug (MPlug) - Plug which is attached with a texture
		* width (int) - Width of the texture
		* height (int) - Height of the texture
		* generateMipMaps (bool) - Generate the mipmap levels

		Acquire a hardware texture by providing a texture description and a block of system memory data which matches the texture description:
		* textureName (string) - Name of the texture to create
		* textureDesc (MTextureDescription) - Description of the texture
		* pixelData (void*) - Block of system memory data which matches the texture description
		* generateMipMaps (bool) - Generate the mipmap levels
		Acquire the texture associated with a given texture node. Currently only file texture nodes are supported.
		If uv tiling is enabled, currently only the first tile will be returned.
		* textureNode (MObject) - Node to acquire texture from
		* allowBackgroundLoad (bool) - Allow for background texture loading. The default value is false."""
	@overload
	def acquireTexture(self,textureName:str,plug:om.MPlug,width:int,height:int,generateMipMaps:bool=True)->MTexture:
		"""(Deprecated) acquireTexture(filePath, mipmapLevels=0, layerName="", alphaChannelIdx=-1) -> MTexture
		acquireTexture(filePath, contextNodeFullName, mipmapLevels=0, layerName="", alphaChannelIdx=-1) -> MTexture
		acquireTexture(textureName, plug, width, height, generateMipMaps=True) -> MTexture
		acquireTexture(textureName, textureDesc, pixelData, generateMipMaps=True) -> MTexture
		acquireTexture(fileNode, allowBackgroundLoad=False) -> MTexture

		Ask the renderer to acquire a hardware texture.

		Acquire a hardware texture from an image file:
		* filePath (string) - Image file name
		* contextNodeFullName (string) Full name of the texture owner Node to be provided as a context to the Maya resolver* mipmapLevels (int) - Mipmap generation levels
		* layerName (string) - The name of the layer to load, this is only relevant for PSD files, otherwise it will have no effect
		* alphaChannelIdx (int) - The index of the alpha channel to load, this is only relevant for PSD files, otherwise it will have no effect

		If a plug to a file texture node is provided then the name, width, height and
		generateMipMaps parameters will be ignored as this information will be
		based on the image on disk associated with texture node. If uv tiling is
		enabled, currently only the first tile will be returned.
		Otherwise, an attempt to bake a texture will be made using the Maya's software
		renderer convert-to-solid-texture functionality.
		* textureName (string) - Name of the texture to create
		* plug (MPlug) - Plug which is attached with a texture
		* width (int) - Width of the texture
		* height (int) - Height of the texture
		* generateMipMaps (bool) - Generate the mipmap levels

		Acquire a hardware texture by providing a texture description and a block of system memory data which matches the texture description:
		* textureName (string) - Name of the texture to create
		* textureDesc (MTextureDescription) - Description of the texture
		* pixelData (void*) - Block of system memory data which matches the texture description
		* generateMipMaps (bool) - Generate the mipmap levels
		Acquire the texture associated with a given texture node. Currently only file texture nodes are supported.
		If uv tiling is enabled, currently only the first tile will be returned.
		* textureNode (MObject) - Node to acquire texture from
		* allowBackgroundLoad (bool) - Allow for background texture loading. The default value is false."""
	@overload
	def acquireTexture(self,textureName:str,textureDesc:MTextureDescription,pixelData:void,generateMipMaps:bool=True)->MTexture:
		"""(Deprecated) acquireTexture(filePath, mipmapLevels=0, layerName="", alphaChannelIdx=-1) -> MTexture
		acquireTexture(filePath, contextNodeFullName, mipmapLevels=0, layerName="", alphaChannelIdx=-1) -> MTexture
		acquireTexture(textureName, plug, width, height, generateMipMaps=True) -> MTexture
		acquireTexture(textureName, textureDesc, pixelData, generateMipMaps=True) -> MTexture
		acquireTexture(fileNode, allowBackgroundLoad=False) -> MTexture

		Ask the renderer to acquire a hardware texture.

		Acquire a hardware texture from an image file:
		* filePath (string) - Image file name
		* contextNodeFullName (string) Full name of the texture owner Node to be provided as a context to the Maya resolver* mipmapLevels (int) - Mipmap generation levels
		* layerName (string) - The name of the layer to load, this is only relevant for PSD files, otherwise it will have no effect
		* alphaChannelIdx (int) - The index of the alpha channel to load, this is only relevant for PSD files, otherwise it will have no effect

		If a plug to a file texture node is provided then the name, width, height and
		generateMipMaps parameters will be ignored as this information will be
		based on the image on disk associated with texture node. If uv tiling is
		enabled, currently only the first tile will be returned.
		Otherwise, an attempt to bake a texture will be made using the Maya's software
		renderer convert-to-solid-texture functionality.
		* textureName (string) - Name of the texture to create
		* plug (MPlug) - Plug which is attached with a texture
		* width (int) - Width of the texture
		* height (int) - Height of the texture
		* generateMipMaps (bool) - Generate the mipmap levels

		Acquire a hardware texture by providing a texture description and a block of system memory data which matches the texture description:
		* textureName (string) - Name of the texture to create
		* textureDesc (MTextureDescription) - Description of the texture
		* pixelData (void*) - Block of system memory data which matches the texture description
		* generateMipMaps (bool) - Generate the mipmap levels
		Acquire the texture associated with a given texture node. Currently only file texture nodes are supported.
		If uv tiling is enabled, currently only the first tile will be returned.
		* textureNode (MObject) - Node to acquire texture from
		* allowBackgroundLoad (bool) - Allow for background texture loading. The default value is false."""
	@overload
	def acquireTexture(self,fileNode:Any,allowBackgroundLoad:bool=False)->MTexture:
		"""(Deprecated) acquireTexture(filePath, mipmapLevels=0, layerName="", alphaChannelIdx=-1) -> MTexture
		acquireTexture(filePath, contextNodeFullName, mipmapLevels=0, layerName="", alphaChannelIdx=-1) -> MTexture
		acquireTexture(textureName, plug, width, height, generateMipMaps=True) -> MTexture
		acquireTexture(textureName, textureDesc, pixelData, generateMipMaps=True) -> MTexture
		acquireTexture(fileNode, allowBackgroundLoad=False) -> MTexture

		Ask the renderer to acquire a hardware texture.

		Acquire a hardware texture from an image file:
		* filePath (string) - Image file name
		* contextNodeFullName (string) Full name of the texture owner Node to be provided as a context to the Maya resolver* mipmapLevels (int) - Mipmap generation levels
		* layerName (string) - The name of the layer to load, this is only relevant for PSD files, otherwise it will have no effect
		* alphaChannelIdx (int) - The index of the alpha channel to load, this is only relevant for PSD files, otherwise it will have no effect

		If a plug to a file texture node is provided then the name, width, height and
		generateMipMaps parameters will be ignored as this information will be
		based on the image on disk associated with texture node. If uv tiling is
		enabled, currently only the first tile will be returned.
		Otherwise, an attempt to bake a texture will be made using the Maya's software
		renderer convert-to-solid-texture functionality.
		* textureName (string) - Name of the texture to create
		* plug (MPlug) - Plug which is attached with a texture
		* width (int) - Width of the texture
		* height (int) - Height of the texture
		* generateMipMaps (bool) - Generate the mipmap levels

		Acquire a hardware texture by providing a texture description and a block of system memory data which matches the texture description:
		* textureName (string) - Name of the texture to create
		* textureDesc (MTextureDescription) - Description of the texture
		* pixelData (void*) - Block of system memory data which matches the texture description
		* generateMipMaps (bool) - Generate the mipmap levels
		Acquire the texture associated with a given texture node. Currently only file texture nodes are supported.
		If uv tiling is enabled, currently only the first tile will be returned.
		* textureNode (MObject) - Node to acquire texture from
		* allowBackgroundLoad (bool) - Allow for background texture loading. The default value is false."""
	def acquireTiledTexture(self,textureName:str,tilePaths:list[str],tilePositions:om.MFloatArray,undefinedColor:om.MColor,width:Any,height:Any)->list[MTexture|failedTilePaths|uvScaleOffset]:
		"""acquireTiledTexture(textureName, tilePaths, tilePositions, undefinedColor, width, height) -> [MTexture, failedTilePaths, uvScaleOffset]

		Ask the renderer to acquire a tiled hardware texture.

		* textureName (string) - Name to give to the texture
		* tilePaths (list of strings) - Set of path names to UV tiles
		* tilePositions (MFloatArray) - Set of lower left coordinates for each UV tile
		* undefinedColor (MColor) - Color to fill tile region with if the image for a given UV tile cannot be acquired
		* maxWidth (unsigned int) - Maximum width of the output texture. The value is clamped to a minimum of 256
		* maxHeight (unsigned int) - Maximum height of the output texture. The value is clamped to a minimum of 256
		* failedTilePaths [OUT] (list of strings) - List of files which were not written to the output texture
		* uvScaleOffset [OUT] (MFloatArray) - Transform to map to the uv range of the output texture"""
	@overload
	def acquireDepthTexture(self,textureName:str,image:om.MImage,generateMipMaps:bool=True,normalizationDesc:MDepthNormalizationDescription|None=None)->MTexture:
		"""acquireDepthTexture(textureName, image, generateMipMaps=True, normalizationDesc=None) -> MTexture
		acquireDepthTexture(textureName, pixelData, width, height, generateMipMaps=True, normalizationDesc=None) -> MTexture

		Ask the renderer to acquire a hardware texture.

		Acquire a hardware texture from an MImage's depth buffer:
		* textureName (string) - Name of the texture to create
		* image (MImage) - Contains block of system memory data containing depth map information
		* generateMipMaps (bool) - Generate the mipmap levels
		* normalizationDesc (MDepthNormalizationDescription) - Optional information to perform normalization on the depth values. Default value is None

		Acquire a hardware texture from an array of depth values:
		* textureName (string) - Name of the texture to create
		* pixelData (float*) - Contains block of system memory data containing depth information
		* width (unsigned int) - Width of the texture
		* height (unsigned int) - Height of the texture
		* generateMipMaps (bool) - Generate the mipmap levels
		* normalizationDesc (MDepthNormalizationDescription) - Optional information to perform normalization on the depth values. Default value is None"""
	@overload
	def acquireDepthTexture(self,textureName:str,pixelData:float,width:int,height:int,generateMipMaps:bool=True,normalizationDesc:MDepthNormalizationDescription|None=None)->MTexture:
		"""acquireDepthTexture(textureName, image, generateMipMaps=True, normalizationDesc=None) -> MTexture
		acquireDepthTexture(textureName, pixelData, width, height, generateMipMaps=True, normalizationDesc=None) -> MTexture

		Ask the renderer to acquire a hardware texture.

		Acquire a hardware texture from an MImage's depth buffer:
		* textureName (string) - Name of the texture to create
		* image (MImage) - Contains block of system memory data containing depth map information
		* generateMipMaps (bool) - Generate the mipmap levels
		* normalizationDesc (MDepthNormalizationDescription) - Optional information to perform normalization on the depth values. Default value is None

		Acquire a hardware texture from an array of depth values:
		* textureName (string) - Name of the texture to create
		* pixelData (float*) - Contains block of system memory data containing depth information
		* width (unsigned int) - Width of the texture
		* height (unsigned int) - Height of the texture
		* generateMipMaps (bool) - Generate the mipmap levels
		* normalizationDesc (MDepthNormalizationDescription) - Optional information to perform normalization on the depth values. Default value is None"""
	def releaseTexture(self,MTexture:Any)->Self:
		"""releaseTexture(MTexture) -> self

		Deletes the MTexture and releases the reference to the underlying texture which is held by the MTexture object."""
	def saveTexture(self,MTexture:Any,string:Any)->Self:
		"""saveTexture(MTexture, string) -> self

		Ask the renderer to save a hardware texture to disk."""
class MTextureUpdateRegion:
	"""Structure to represent an update region for a texture."""
	@property
	def fXRangeMin(self)->Any:
		"""X min value"""
	@fXRangeMin.setter
	def fXRangeMin(self,value:Any)->None:...
	@property
	def fXRangeMax(self)->Any:
		"""X max value"""
	@fXRangeMax.setter
	def fXRangeMax(self,value:Any)->None:...
	@property
	def fYRangeMin(self)->Any:
		"""Y min value"""
	@fYRangeMin.setter
	def fYRangeMin(self,value:Any)->None:...
	@property
	def fYRangeMax(self)->Any:
		"""Y max value"""
	@fYRangeMax.setter
	def fYRangeMax(self,value:Any)->None:...
	@property
	def fZRangeMin(self)->Any:
		"""Z min value"""
	@fZRangeMin.setter
	def fZRangeMin(self,value:Any)->None:...
	@property
	def fZRangeMax(self)->Any:
		"""Z max value"""
	@fZRangeMax.setter
	def fZRangeMax(self,value:Any)->None:...
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
class MUIDrawManager:
	"""Main interface for drawing basic UI drawables in Viewport 2.0 and Hardware Renderer 2.0."""
	kDefaultFontSize:int=12
	kSmallFontSize:int=9
	kLeft:int=0
	kCenter:int=1
	kRight:int=2
	kInclineNormal:int=0
	kInclineItalic:int=1
	kInclineOblique:int=2
	kWeightLight:int=300
	kWeightNormal:int=400
	kWeightDemiBold:int=600
	kWeightBold:int=700
	kWeightBlack:int=900
	kStretchUltraCondensed:int=50
	kStretchExtraCondensed:int=62
	kStretchCondensed:int=75
	kStretchSemiCondensed:int=87
	kStretchUnstretched:int=100
	kStretchSemiExpanded:int=112
	kStretchExpanded:int=125
	kStretchExtraExpanded:int=150
	kStretchUltraExpanded:int=200
	kLineNone:int=0
	kLineOverline:int=1
	kLineUnderline:int=2
	kLineStrikeoutLine:int=3
	kSolid:int=0
	kShortDotted:int=1
	kShortDashed:int=2
	kDashed:int=3
	kDotted:int=4
	kFlat:int=0
	kStippled:int=1
	kShaded:int=2
	kPoints:int=0
	kLines:int=1
	kLineStrip:int=2
	kClosedLine:int=3
	kTriangles:int=4
	kTriStrip:int=5
	kNonSelectable:int=0
	kSelectable:int=1
	kAutomatic:int=2
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def beginDrawable(self,selectability:int=MUIDrawManager.kAutomatic,selectionName:int=0)->Self:
		"""beginDrawable(selectability = kAutomatic, selectionName = 0) -> self

		Resets all draw state, such as color and line style, to defaults and indicates the start of a sequence of drawing operations.
		All drawing operations must take place between calls to beginDrawable() and endDrawable().

		The behavior when calling with no (default) parameters depends on the context:
		 - In MPxManipulatorNode.drawUI() context, the geometries will be marked as unselectable.
		 - In any other context, like MPxDrawOverride.addUIDrawables(), the geometries will be marked as selectable and can be used for shape selection.Provide parameters (kSelectable, selectionName) with manipulators to specify they are selectable and their selection handle names.
		Provide kNonSelectable as selectability to specify locators are not selectable.


		* selectability (int) - Selectability of the handle to be drawn.
		  kNonSelectable  Geometries cannot be used for selection
		  kSelectable     Use geometries for selection
		  kAutomatic      Use geometries for selection when not in manipulator context
		* selectionName (int) - Selection name for manipulators, usually derived from MPxManipulatorNode.glFirstHandle()."""
	def endDrawable(self)->Self:
		"""endDrawable() -> self

		Indicates the end of a sequence of drawing operations.
		All internal drawing state, such as color and line style, are reset to defaults."""
	def setColor(self,color:Any)->Self:
		"""setColor(color) -> self

		Set the draw color. This will remain in effect until the next call to setColor(), setColorIndex() or endDrawable().

		For text this color will be used as the foreground color. Background color can be specified directly in the call to text().


		Default: (0.7, 0.7, 0.7, 1)"""
	def setColorIndex(self,index:int)->Self:
		"""setColorIndex(index) -> self

		Set the color index for the later primitive and text drawing.
		For default, it will use (0.7, 0.7, 0.7, 1) as default color.

		* index (int) - Color index"""
	def setPointSize(self,value:float)->Self:
		"""setPointSize(value) -> self

		Set the point size for the point drawing.

		* value (float) - Point size in pixels."""
	def setLineWidth(self,value:float)->Self:
		"""setLineWidth(value) -> self

		Set the line width for the primitive drawing (line, rect, box...)

		* value (float) - Line width in pixels."""
	@overload
	def setLineStyle(self,style:int)->Self:
		"""setLineStyle(style) -> self
		setLineStyle(factor, pattern) -> self

		Set the line style for the primitive drawing (line, rect, box...)

		* style (int) - Line style type.
		  kSolid         Solid line
		  kShortDotted   Short Dotted line
		  kShortDashed   Short dashed line
		  kDashed        Dashed line
		  kDashed        Dotted line

		Or set the dashed line pattern for the primitive drawing (line, rect, box...)

		* factor (int) - a multiplier for each bit in the line stipple pattern.
		* pattern (int) - a bit pattern indicating which fragments of a line will be drawn"""
	@overload
	def setLineStyle(self,factor:int,pattern:int)->Self:
		"""setLineStyle(style) -> self
		setLineStyle(factor, pattern) -> self

		Set the line style for the primitive drawing (line, rect, box...)

		* style (int) - Line style type.
		  kSolid         Solid line
		  kShortDotted   Short Dotted line
		  kShortDashed   Short dashed line
		  kDashed        Dashed line
		  kDashed        Dotted line

		Or set the dashed line pattern for the primitive drawing (line, rect, box...)

		* factor (int) - a multiplier for each bit in the line stipple pattern.
		* pattern (int) - a bit pattern indicating which fragments of a line will be drawn"""
	def setPaintStyle(self,style:int)->Self:
		"""setPaintStyle(style) -> self

		Set the paint style for filled primitive drawing.

		* style (int) - Paint style type.
		  kFlat      Solid
		  kStippled  Stippled
		  kShaded    Shaded with lighting"""
	def depthPriority(self)->int:
		"""depthPriority() -> int

		Get the current depth priority value for primitive drawing.

		If the method failed to execute a value of 0 will be returned."""
	def setDepthPriority(self,priority:int)->Self:
		"""setDepthPriority(priority) -> self

		Set the depth priority for primitive drawing.

		The MRenderItem class lists some sample internal priorities which may be used.

		* priority (int) - Depth priority."""
	def line(self,startPoint:om.MPoint,endPoint:om.MPoint)->Self:
		"""line(startPoint, endPoint) -> self

		Draw a straight line between two points.

		* startPoint (MPoint) - The start point of the line.
		* endPoint (MPoint) - The end point of the line."""
	def line2d(self,startPoint:om.MPoint,endPoint:om.MPoint)->Self:
		"""line2d(startPoint, endPoint) -> self

		Draw a straight line between two points.

		* startPoint (MPoint) - The start point of the line, only x-y components(in pixels) are used.
		* endPoint (MPoint) - The end point of the line, only x-y components(in pixels) are used."""
	def lineList(self,points:om.MPointArray,draw2D:bool)->Self:
		"""lineList(points, draw2D) -> self

		Draw a series of line segments in 3D or 2D.

		* points (MPointArray) - Array of point positions. Pairs of points are interpreted as line segments.
		If an odd number of points is specified then the last point will not be drawn, as it
		does not form a line segment.
		* draw2D (bool) Draw in 2D or 3D."""
	def lineStrip(self,points:om.MPointArray,draw2D:bool)->Self:
		"""lineStrip(points, draw2D) -> self

		Draw a series of connected line segments in 3D or 2D

		* points (MPointArray) - Array of point positions. Each point in the array is connected
		to form a line strip.
		* draw2D (bool) Draw in 2D or 3D."""
	def point(self,point:om.MPoint)->Self:
		"""point(point) -> self

		Draw a point.

		* point (MPoint) - Position of the point."""
	def point2d(self,point:om.MPoint)->Self:
		"""point2d(point) -> self

		Draw a point.

		* point (MPoint) - Position of the point, only x-y components(in pixels) are used."""
	def points(self,points:om.MPointArray,draw2D:bool)->Self:
		"""points(points, draw2D) -> self

		Draw a series of points in 3D or 2D.

		* points (MPointArray) - Array of point positions.
		* draw2D (bool) Draw in 2D or 3D."""
	def rect(self,center:om.MPoint,up:om.MVector,normal:om.MVector,scaleX:float,scaleY:float,filled:bool=False)->Self:
		"""rect(center, up, normal, scaleX, scaleY, filled=False) -> self

		Draw a rectangle.
		The rectangle is within the plane determined by a normal vector, and a up vector is given to determine the X-Y direction.

		* center (MPoint) - Center of the rectangle.
		* up (MVector) - Up vector of the rectangle.
		* normal (MVector) - Normal vector of the rectangle plane.
		* scaleX (float) - Scale factor in X-direction.
		* scaleY (float) - Scale factor in Y-direction.
		* filled (bool) - If true the rectangle will be filled otherwise it will just be drawn as an outline."""
	def rect2d(self,center:om.MPoint,up:om.MVector,scaleX:float,scaleY:float,filled:bool=False)->Self:
		"""rect2d(center, up, scaleX, scaleY, filled=False) -> self

		Draw a 2D rectangle on the screen.
		The rectangle is always facing the camera, and a up vector is given to determine the X-Y direction

		* center (MPoint) - Center of the rectangle, only x-y components(in pixels) are used.
		* up (MVector) - Up vector of the rectangle, only x-y components are used.
		* scaleX (float) - Scale factor in X-direction.
		* scaleY (float) - Scale factor in Y-direction.
		* filled (bool) - If true the rectangle will be filled otherwise it will just be drawn as an outline."""
	@overload
	def sphere(self,center:om.MPoint,radius:float,subdivisionsAxis:int,subdivisionsHeight:int,filled:bool=False)->Self:
		"""sphere(center, radius, subdivisionsAxis, subdivisionsHeight, filled=False) -> selfsphere(center, radius, filled=False) -> self

		Draw a sphere.

		* center (MPoint) - Center of the sphere.
		* radius (float) - Radius of the sphere.
		* subdivisionsAxis (int) - Number of subdivisions along main axis.
		* subdivisionsHeight (int) - Number of subdivisions along height.
		* filled (bool) - If true the sphere will be filled otherwise it will just be drawn as a wireframe."""
	@overload
	def sphere(self,center:om.MPoint,radius:float,filled:bool=False)->Self:
		"""sphere(center, radius, subdivisionsAxis, subdivisionsHeight, filled=False) -> selfsphere(center, radius, filled=False) -> self

		Draw a sphere.

		* center (MPoint) - Center of the sphere.
		* radius (float) - Radius of the sphere.
		* subdivisionsAxis (int) - Number of subdivisions along main axis.
		* subdivisionsHeight (int) - Number of subdivisions along height.
		* filled (bool) - If true the sphere will be filled otherwise it will just be drawn as a wireframe."""
	@overload
	def circle(self,center:om.MPoint,normal:om.MVector,radius:float,numSubdivision:int,filled:bool)->Self:
		"""circle(center, normal, radius, numSubdivision, filled) -> selfcircle(center, normal, radius, filled=False) -> self

		Draw a circle.
		The circle is drawn within the plane determined by a normal vector.

		* center (MPoint) - Center of the circle.
		* normal (MVector) - Normal vector of the circle plane.
		* radius (float) - Radius of the circle.
		* numSubdivision (int) - Number of Subdivisions for the circle.
		* filled (bool) - If true the circle will be filled otherwise it will just be drawn as an outline."""
	@overload
	def circle(self,center:om.MPoint,normal:om.MVector,radius:float,filled:bool=False)->Self:
		"""circle(center, normal, radius, numSubdivision, filled) -> selfcircle(center, normal, radius, filled=False) -> self

		Draw a circle.
		The circle is drawn within the plane determined by a normal vector.

		* center (MPoint) - Center of the circle.
		* normal (MVector) - Normal vector of the circle plane.
		* radius (float) - Radius of the circle.
		* numSubdivision (int) - Number of Subdivisions for the circle.
		* filled (bool) - If true the circle will be filled otherwise it will just be drawn as an outline."""
	@overload
	def circle2d(self,center:om.MPoint,radius:float,numSubdivision:int,filled:bool)->Self:
		"""circle2d(center, radius, numSubdivision, filled) -> selfcircle2d(center, radius, filled=False) -> self

		Draw a 2D circle on the screen.
		The circle is always facing the camera.

		* center (MPoint) - Center of the circle, only x-y components(in pixels) are used.
		* radius (float) - Radius(in pixels) of the circle.
		* numSubdivision (int) - Number of Subdivisions for the circle.
		* filled (bool) - If true the circle will be filled otherwise it will just be drawn as an outline."""
	@overload
	def circle2d(self,center:om.MPoint,radius:float,filled:bool=False)->Self:
		"""circle2d(center, radius, numSubdivision, filled) -> selfcircle2d(center, radius, filled=False) -> self

		Draw a 2D circle on the screen.
		The circle is always facing the camera.

		* center (MPoint) - Center of the circle, only x-y components(in pixels) are used.
		* radius (float) - Radius(in pixels) of the circle.
		* numSubdivision (int) - Number of Subdivisions for the circle.
		* filled (bool) - If true the circle will be filled otherwise it will just be drawn as an outline."""
	@overload
	def arc(self,center:om.MPoint,start:om.MVector,end:om.MVector,normal:om.MVector,radius:float,numSubdivisions:Any,filled:bool)->Self:
		"""arc(center, start, end, normal, radius, numSubdivisions, filled) -> selfarc(center, start, end, normal, radius, filled=False) -> self

		Draw an arc. The arc is within the plane determined by a normal vector.
		The arc sweeps in CCW from the vector that is the projection of the given start vector onto the arc plane,
		and ends at the vector that is the projection of the given end vector onto the arc plane.

		* center (MPoint) - Center of the arc.
		* start (MVector) - Start vector, its projection onto the arc plane is the start of the arc.
		* end (MVector) - End vector, its projection onto the arc plane is the end of the arc.
		* normal (MVector) - Normal vector of the arc plane.
		* radius (float) - Radius of the arc.
		* subdivisions (int) - Number of subdivisions of the arc.
		* filled (bool) - If true the arc will be filled otherwise it will just be drawn as an outline."""
	@overload
	def arc(self,center:om.MPoint,start:om.MVector,end:om.MVector,normal:om.MVector,radius:float,filled:bool=False)->Self:
		"""arc(center, start, end, normal, radius, numSubdivisions, filled) -> selfarc(center, start, end, normal, radius, filled=False) -> self

		Draw an arc. The arc is within the plane determined by a normal vector.
		The arc sweeps in CCW from the vector that is the projection of the given start vector onto the arc plane,
		and ends at the vector that is the projection of the given end vector onto the arc plane.

		* center (MPoint) - Center of the arc.
		* start (MVector) - Start vector, its projection onto the arc plane is the start of the arc.
		* end (MVector) - End vector, its projection onto the arc plane is the end of the arc.
		* normal (MVector) - Normal vector of the arc plane.
		* radius (float) - Radius of the arc.
		* subdivisions (int) - Number of subdivisions of the arc.
		* filled (bool) - If true the arc will be filled otherwise it will just be drawn as an outline."""
	@overload
	def arc2d(self,center:om.MPoint,start:om.MVector,end:om.MVector,radius:float,numSubdivisions:Any,filled:bool)->Self:
		"""arc2d(center, start, end, radius, numSubdivisions, filled) -> selfarc2d(center, start, end, radius, filled=False) -> self

		Draw a 2D arc on the screen. The arc is always facing the camera.
		The arc sweeps in CCW from the start vector and ends at the end vector.

		* center (MPoint) - Center of the arc, only x-y components(in pixels) are used.
		* start (MVector) - Start vector, only x-y components are used.
		* end (MVector) - End vector, only x-y components are used.
		* radius (float) - Radius(in pixels) of the arc.
		* subdivisions (int) - Number of subdivisions of the arc.
		* filled (bool) - If true the arc will be filled otherwise it will just be drawn as an outline."""
	@overload
	def arc2d(self,center:om.MPoint,start:om.MVector,end:om.MVector,radius:float,filled:bool=False)->Self:
		"""arc2d(center, start, end, radius, numSubdivisions, filled) -> selfarc2d(center, start, end, radius, filled=False) -> self

		Draw a 2D arc on the screen. The arc is always facing the camera.
		The arc sweeps in CCW from the start vector and ends at the end vector.

		* center (MPoint) - Center of the arc, only x-y components(in pixels) are used.
		* start (MVector) - Start vector, only x-y components are used.
		* end (MVector) - End vector, only x-y components are used.
		* radius (float) - Radius(in pixels) of the arc.
		* subdivisions (int) - Number of subdivisions of the arc.
		* filled (bool) - If true the arc will be filled otherwise it will just be drawn as an outline."""
	def mesh(self,mode:int,position:om.MPointArray,normal:om.MVectorArray|None=None,color:om.MColorArray|None=None,index:om.MUintArray|None=None,texcoord:om.MPointArray|None=None)->Self:
		"""mesh(mode, position, normal=None, color=None, index=None, texcoord=None) -> self

		Draw custom geometric shapes from an array of vertices.

		If the optional normal or color arrays are provided they must contain a single value per element
		of the positions array (i.e. all three arrays must be the same length).

		The optional index array specifies the order in which the vertex positions (and their corresponding normals
		and colors) should be drawn. Vertices can be reused by having their indices appear multiple times, so the index
		array may be longer (or shorter) than the other three arrays.

		If the index array is not provided then the vertices will be drawn in the order in which they appear in the positions array.

		* mode (int) - Primitive mode
		  kPoints       Point list
		  kLines        Line list
		  kLineStrip    Line strip
		  kClosedLine   Closed line
		  kTriangles    Triangle list
		  kTriStrip     Triangle strip
		* position (MPointArray) - List of the vertex positions.
		* normal (MVectorArray) - List of the vertex normals.
		* color (MColorArray) - List of the vertex colors.
		* index (MUintArray) - List of the vertex indices.
		* texcoord (MPointArray) - List of the vertex texture coordinates."""
	def mesh2d(self,mode:int,position:om.MPointArray,color:om.MColorArray|None=None,index:om.MUintArray|None=None,texcoord:om.MPointArray|None=None)->Self:
		"""mesh2d(mode, position, color=None, index=None, texcoord=None) -> self

		Draw custom 2d geometric shapes from an array of vertices.

		If the optional color arrays are provided they must contain a single value per element of the positions
		array (i.e. both arrays must be the same length).

		The optional index array specifies the order in which the vertex positions (and their corresponding colors)
		should be drawn. Vertices can be reused by having their indices appear multiple times, so the index array may
		be longer (or shorter) than the other two arrays.

		If the index array is not provided then the vertices will be drawn in the order in which they appear in the positions array.

		* mode (int) - Primitive mode
		  kPoints       Point list
		  kLines        Line list
		  kLineStrip    Line strip
		  kClosedLine   Closed line
		  kTriangles    Triangle list
		  kTriStrip     Triangle strip
		* position (MPointArray) - List of the vertex positions, only x-y components of the point are used.
		* color (MColorArray) - List of the vertex colors.
		* index (MUintArray) - List of the vertex indices.
		* texcoord (MPointArray) - List of the vertex texture coordinates."""
	def beginDrawInXray(self)->Self:
		"""beginDrawInXray() -> self

		The drawables to be drawn between calls to beginDrawInXray() and endDrawInXray() will display
		on the top of other geometries in the scene, as the depth test is disabled for these drawables.
		These methods can be used to drawing objects such as locators.
		Note only the drawables meet following conditions would be affected by these two APIs.
		  1. Created by method MUIDrawManager::mesh();
		  2. The first input parameter in MUIDrawManager::mesh() must be one of kTriangles, kLines and kPoints.
		Any other drawables to be drawn between calls to beginDrawInXray() and endDrawInXray() would display as normal.
		If several meshes are drawn between these two APIs, occlusion order is decided by their specification order."""
	def endDrawInXray(self)->Self:
		"""endDrawInXray() -> self

		Pair with beginDrawInXray()."""
	@overload
	def cone(self,base:om.MPoint,direction:om.MVector,radius:float,height:float,subdivisionsCap:int,filled:bool)->Self:
		"""cone(base, direction, radius, height, subdivisionsCap, filled) -> selfcone(base, direction, radius, height, filled=False) -> self

		Draw a cone.

		* base (MPoint) - Base position for the cone.
		* direction (MVector) - The cone's tip will point in this direction.
		* radius (float) - Radius of the cone.
		* height (float) - Height of the cone.
		* subdivisionsCap (int) - Number of subdivisions of the cap.
		* filled (bool) - If true the cone will be filled otherwise it will just be drawn as an outline."""
	@overload
	def cone(self,base:om.MPoint,direction:om.MVector,radius:float,height:float,filled:bool=False)->Self:
		"""cone(base, direction, radius, height, subdivisionsCap, filled) -> selfcone(base, direction, radius, height, filled=False) -> self

		Draw a cone.

		* base (MPoint) - Base position for the cone.
		* direction (MVector) - The cone's tip will point in this direction.
		* radius (float) - Radius of the cone.
		* height (float) - Height of the cone.
		* subdivisionsCap (int) - Number of subdivisions of the cap.
		* filled (bool) - If true the cone will be filled otherwise it will just be drawn as an outline."""
	def cylinder(self,center:om.MPoint,up:om.MVector,radius:float,height:float,subdivisionsAxis:int,filled:bool=False)->Self:
		"""cylinder(center, up, radius, height, subdivisionsAxis, filled=False) -> self

		Draw a cylinder.

		* center (MPoint) - Center position for the cylinder.
		* up (MVector) - Direction of the Up vector.
		* radius (float) - Radius of the cylinder.
		* height (float) - Height of the cylinder.
		* subdivisionsAxis (int) - Number of subdivisions along the main axis.
		* filled (bool) - If true the cylinder will be filled otherwise it will just be drawn as an outline."""
	def capsule(self,center:om.MPoint,up:om.MVector,radius:float,height:float,subdivisionsAxis:int,subdivisionsHeight:int,filled:bool=False)->Self:
		"""capsule(center, up,radius, height, subdivisionsAxis, subdivisionsHeight, filled=False) -> self

		Draw a capsule.

		* center (MPoint) - Center position for the capsule.
		* up (MVector) - Direction of the Up vector.
		* radius (float) - Radius of the capsule.
		* height (float) - Height of the capsule.
		* subdivisionsAxis (int) - Subdivisions along the main axis.
		* subdivisionsHeight (int) - Subdivisions along height.
		* filled (bool) - If true the capsule will be filled otherwise it will just be drawn as an outline."""
	def box(self,center:om.MPoint,up:om.MVector,right:om.MVector,scaleX:float=1.0,scaleY:float=1.0,scaleZ:float=1.0,filled:bool=False)->Self:
		"""box(center, up, right, scaleX=1.0, scaleY=1.0, scaleZ=1.0, filled=False) -> self

		Draw a box.

		* center (MPoint) - Center position for the box.
		* up (MVector) - The top of the box will be facing this direction.
		* right (MVector) - The side of the box will be facing this direction.
		* scaleX (float) - X size of the box.
		* scaleY (float) - Y size of the box.
		* scaleZ (float) - Z size of the box.
		* filled (bool) - If true the box will be filled otherwise it will just be drawn as an outline."""
	@staticmethod
	def getFontList()->list[str]:
		"""getFontList() -> list of strings

		Get the names of all font faces that are available on current system.
		The names can then be used for MUIDrawManager::setFontName()."""
	def setFontIncline(self,fontIncline:int)->Self:
		"""setFontIncline(fontIncline) -> self

		Set the incline of font to be used when drawing text.

		* fontIncline (int) - The font incline to use."""
	def setFontWeight(self,fontWeight:Any)->Self:
		"""setFontWeight(fontWeight) -> self

		Set the weight of font to be used when drawing text.

		* weight (int) - The font weight to use."""
	def setFontStretch(self,fontStretch:int)->Self:
		"""setFontStretch(fontStretch) -> self

		Set the stretch of font to be used when drawing text.

		* fontStretch (int) - The font stretch to use."""
	def setFontLine(self,fontLine:int)->Self:
		"""setFontLine(fontLine) -> self

		Set the line of font to be used when drawing text.

		* fontLine (int) - The font line to use."""
	def setFontSize(self,fontSize:int)->Self:
		"""setFontSize(fontSize) -> self

		Set the size of font to be used when drawing text.

		* fontSize (int) - The font height(in pixel) to use."""
	def setFontName(self,faceName:str)->Self:
		"""setFontName(faceName) -> self

		Set the face name of font to be used when drawing text.

		* faceName (string) - The font face name(case-insensitive) to use, All system font faces are supported. "helvetica" is the default for invalid input."""
	def text(self,position:om.MPoint,text:str,alignment:TextAlignment=MUIDrawManager.kLeft,backgroundSize:list[int]|None=None,backgroundColor:om.MColor|None=None,dynamic:bool=False)->Self:
		"""text(position, text, alignment=kLeft, backgroundSize=None, backgroundColor=None, dynamic=False) -> self

		Draw a screen facing and horizontal aligned text in viewport 2.0.
		It has a fixed size in screen space.

		* position (MPoint) - Position of the text to be drawn, it is 3d object space.
		* text (string) - Content of the text string.
		* alignment (TextAlignment) - Alignment of the text.
		         - "kLeft", background box's left bottom will be located at "position".         In width direction, text area will be aligned to the left side of background.
		         In height direction, text are will be aligned in the middle of background.
		         - "kCenter", background box' center bottom will be located at "position".         Text area's center and background box's center will be the same point.
		         - "kRight", background box's right bottom will be located at "position".         In width direction, text area will be aligned to the right side of background.
		         In height direction, text are will be aligned in the middle of background.
		* backgroundSize ([int, int]) - The background box size of the text.
		         Default is None, in this case there will be no background, just shows the text.
		         If it is specified with smaller size than text, the text will be clipped.
		         It is a int array with size 2, like "backgroundSize = [ width, height ]"
		         Size unit is the screen pixel.
		* backgroundColor (MColor) - The color of the background, it can be transparent.
		         If None is passed, background will be fully transparent.
		* dynamic (bool) - This is mostly used for performance.
		         If the text draw is not changed frequently, we can leave it as default value false.
		                        If the text draw is changing very often like it is showing some dynamic numbers,
		         in this case making dynamic true will give better performance."""
	def text2d(self,position:om.MPoint,text:Any,alignment:TextAlignment=MUIDrawManager.kLeft,backgroundSize:list[int]|None=None,backgroundColor:om.MColor|None=None,dynamic:bool=False)->Self:
		"""text2d(position, text, alignment=kLeft, backgroundSize=None, backgroundColor=None, dynamic=False) -> self

		Draw a text on the screen.

		* position (MPoint) - Position of the text to be drawn, it is in screen space, only x-y components are used.
		* text Content of the text string.
		* alignment (TextAlignment) - Alignment of the text.
		         - "kLeft", background box's left bottom will be located at "position".         In width direction, text area will be aligned to the left side of background.
		         In height direction, text are will be aligned in the middle of background.
		         - "kCenter", background box' center bottom will be located at "position".         Text area's center and background box's center will be the same point.
		         - "kRight", background box's right bottom will be located at "position".         In width direction, text area will be aligned to the right side of background.
		         In height direction, text are will be aligned in the middle of background.
		* backgroundSize ([int, int]) - The background box size of the text.
		         Default is None, in this case there will be no background, just shows the text.
		         If it is specified with smaller size than text, the text will be clipped.
		         It is a int array with size 2, like "backgroundSize = [ width, height ]"
		         Size unit is the screen pixel.
		* backgroundColor (MColor) - The color of the background, it can be transparent.
		         If None is passed, background will be fully transparent.
		* dynamic (bool) - This is mostly used for performance.
		         If the text draw is not changed frequently, we can leave it as default value false.
		                        If the text draw is changing very often like it is showing some dynamic numbers,
		         in this case making dynamic true will give better performance."""
	def setTexture(self,texture:MTexture)->Self:
		"""setTexture(texture) -> self

		Set the active texture to apply when drawing a mesh.
		This will remain in effect until the next call to setTexture().

		* texture (MTexture) - The texture which will affect the later drawing."""
	def setTextureSampler(self,filter:int,address:int)->Self:
		"""setTextureSampler(filter, address) -> self

		Set the filter and address mode used when applying a texture to a mesh.
		This will remain in effect until the next call to setTextureSampler().

		Fails when filter and address combination is not supported.

		* filter (int) - The filter which will affect the later drawing.
		        Currently, only MSamplerState.kMinMagMipPoint and MSamplerState.kMinMagMipLinear are supported.
		* address (int) - The canonical range which will affect the later drawing.
		        Currently, only MSamplerState.kTexWrap and MSamplerState.kTexClamp are supported."""
	def setTextureMask(self,mask:int)->Self:
		"""setTextureMask(mask) -> self

		Set the channel mask to used when applying a texture to a mesh.
		This will remain in effect until the next call to setTextureMask().

		Fails when mask is not supported.

		* mask (int) - The channel mask which will affect the later drawing.
		        Currently, only MBlendState.kRGBAChannels, MBlendState.kRGBChannels and MBlendState.kAlphaChannel are supported."""
	def icon(self,position:om.MPoint,name:str,scale:float)->None:
		"""icon(position, name, scale)) -> self

		Draw an icon at a given 3d position.

		* position (MPoint) - 3d location of the icon..
		* name (MString) - The name of an icon. The list
		 of available icon names can be found using the
		MUIDrawManager::getIconNames() method.
		* scale (float) - Uniform scaling factor for the icon."""
	@staticmethod
	def getIconNames()->list[str]:
		"""getIconNames() -> list of strings

		Get list of icon names. The names can be used
		for drawing icons using the MUIDrawManager::icon() method."""
class MUniformParameter:
	"""The MUniformParameter class provides a high-level interface to hardware shader uniform parameters. By defining your shader's uniform parameters through this class, you allow Maya to handle the attributes, editing, serialisation, and caching for you in a standard way that ensure you'll be able to leverage future performance and functionlity improvements."""
	@property
	def uiHidden(self)->Any:
		"""The hidden state of this parameter"""
	@uiHidden.setter
	def uiHidden(self,value:Any)->None:...
	@property
	def keyable(self)->Any:
		"""The keyable state of this parameter"""
	@keyable.setter
	def keyable(self,value:Any)->None:...
	@property
	def rangeMin(self)->Any:
		"""The hard range lower bound for a numeric uniform parameter."""
	@rangeMin.setter
	def rangeMin(self,value:Any)->None:...
	@property
	def rangeMax(self)->Any:
		"""The hard range upper bound for a numeric uniform parameter."""
	@rangeMax.setter
	def rangeMax(self,value:Any)->None:...
	@property
	def softRangeMin(self)->Any:
		"""The soft range lower bound for a numeric uniform parameter."""
	@softRangeMin.setter
	def softRangeMin(self,value:Any)->None:...
	@property
	def softRangeMax(self)->Any:
		"""The soft range upper bound for a numeric uniform parameter."""
	@softRangeMax.setter
	def softRangeMax(self,value:Any)->None:...
	@property
	def enumFieldNames(self)->Any:
		"""The field names of an enum attribute."""
	@enumFieldNames.setter
	def enumFieldNames(self,value:Any)->None:...
	@property
	def uiNiceName(self)->Any:
		"""The UI Nice Name for the attribute."""
	@uiNiceName.setter
	def uiNiceName(self,value:Any)->None:...
	kTypeUnknown:int=0
	kTypeBool:int=1
	kTypeInt:int=2
	kTypeFloat:int=3
	kType1DTexture:int=4
	kType2DTexture:int=5
	kType3DTexture:int=6
	kTypeCubeTexture:int=7
	kTypeEnvTexture:int=8
	kTypeString:int=9
	kTypeEnum:int=10
	kSemanticUnknown:int=0
	kSemanticObjectDir:int=1
	kSemanticWorldDir:int=2
	kSemanticViewDir:int=3
	kSemanticProjectionDir:int=4
	kSemanticObjectPos:int=5
	kSemanticWorldPos:int=6
	kSemanticViewPos:int=7
	kSemanticProjectionPos:int=8
	kSemanticColor:int=9
	kSemanticNormal:int=10
	kSemanticBump:int=11
	kSemanticEnvironment:int=12
	kSemanticWorldMatrix:int=13
	kSemanticWorldInverseMatrix:int=14
	kSemanticWorldInverseTransposeMatrix:int=15
	kSemanticViewMatrix:int=16
	kSemanticViewInverseMatrix:int=17
	kSemanticViewInverseTransposeMatrix:int=18
	kSemanticProjectionMatrix:int=19
	kSemanticProjectionInverseMatrix:int=20
	kSemanticProjectionInverseTransposeMatrix:int=21
	kSemanticWorldViewMatrix:int=22
	kSemanticWorldViewInverseMatrix:int=23
	kSemanticWorldViewInverseTransposeMatrix:int=24
	kSemanticWorldViewProjectionMatrix:int=25
	kSemanticWorldViewProjectionInverseMatrix:int=26
	kSemanticWorldViewProjectionInverseTransposeMatrix:int=27
	kSemanticColorTexture:int=28
	kSemanticNormalTexture:int=29
	kSemanticBumpTexture:int=30
	kSemanticNormalizationTexture:int=31
	kSemanticTranspDepthTexture:int=32
	kSemanticOpaqueDepthTexture:int=33
	kSemanticTime:int=34
	kSemanticWorldTransposeMatrix:int=35
	kSemanticViewTransposeMatrix:int=36
	kSemanticProjectionTransposeMatrix:int=37
	kSemanticWorldViewTransposeMatrix:int=38
	kSemanticWorldViewProjectionTransposeMatrix:int=39
	kSemanticViewProjectionMatrix:int=40
	kSemanticViewProjectionInverseMatrix:int=41
	kSemanticViewProjectionTransposeMatrix:int=42
	kSemanticViewProjectionInverseTransposeMatrix:int=43
	kSemanticLocalViewer:int=44
	kSemanticViewportPixelSize:int=45
	kSemanticBackgroundColor:int=46
	kSemanticFrameNumber:int=47
	kSemanticNearClipPlane:int=48
	kSemanticFarClipPlane:int=49
	kSemanticHWSPrimitiveBase:int=50
	kSemanticHWSPrimitiveCountPerInstance:int=51
	kSemanticHWSObjectLevel:int=52
	kSemanticHWSFaceLevel:int=53
	kSemanticHWSEdgeLevel:int=54
	kSemanticHWSVertexLevel:int=55
	kSemanticHWSOccluder:int=56
	kSemanticHWSFrontCCW:int=57
	kSemanticHWSInstancedDraw:int=58
	kSemanticHWSHighlighting:int=59
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def asBool(self,context:MDrawContext)->bool:
		"""asBool(context) -> bool

		Get the value of this uniform parameter as a boolean value.
		Because some parameters can be shape-dependent, the method requires access to the current context being rendered.

		* context (MDrawContext) - Draw context being used for render."""
	def asFloat(self,context:MDrawContext)->float:
		"""asFloat(context) -> float

		Get the value of this uniform parameter as a float.
		Because some parameters can be shape-dependent, the method requires access to the current context being rendered.

		* context (MDrawContext) - Draw context being used for render."""
	def asFloatArray(self,context:MDrawContext)->tuple[float,...]:
		"""asFloatArray(context) -> tuple of floats

		Get the value of this uniform parameter as one or more floating point values.
		Because some parameters can be shape-dependent, the method requires access to the current context being rendered.

		* context (MDrawContext) - Draw context being used for render."""
	def asInt(self,context:MDrawContext)->int:
		"""asInt(context) -> int

		Get the value of this uniform parameter as an integer.
		Because some parameters can be shape-dependent, the method requires access to the current context being rendered.

		* context (MDrawContext) - Draw context being used for render."""
	def asString(self,context:MDrawContext)->str:
		"""asString(context) -> string

		Get the value of this uniform parameter as a string.
		Because some parameters can be shape-dependent, the method requires access to the current context being rendered.

		* context (MDrawContext) - Draw context being used for render."""
	def copy(self,source:MUniformParameter)->Self:
		"""copy(source) -> self

		Copy data from source parameter.

		* source (MUniformParameter) - The source parameter to copy from"""
	def hasChanged(self,context:MDrawContext)->bool:
		"""hasChanged(context) -> bool

		Has the value of this parameter changed since the last time it was accessed?
		This allows your shader to minimise state changes by only updating modified parameters.

		* context (MDrawContext) - Draw context being used for render."""
	def isATexture(self)->bool:
		"""isATexture() -> bool

		Returns True if this parameter represents a texture, False otherwise."""
	def name(self)->str:
		"""name() -> string

		Get the name of this parameter."""
	def numColumns(self)->int:
		"""numColumns() -> int

		Get the number of columns in this parameter."""
	def numElements(self)->int:
		"""numElements() -> int

		Get the number of elements in this parameter (including rows and columns)."""
	def numRows(self)->int:
		"""numRows() -> int

		Get the number of rows in this parameter."""
	def plug(self)->om.MPlug:
		"""plug() -> MPlug

		Get the plug managed by this parameter."""
	def semantic(self)->int:
		"""semantic() -> int

		Get the semantic of this parameter.

		The list of available semantic values can be obtained with the following commands:
		  print filter(lambda k: k.startswith('kSemantic'), dir(maya.api.OpenMayaRender.MUniformParameter))"""
	def setBool(self,value:bool)->Self:
		"""setBool(value) -> self

		Set the value of this uniform parameter as a boolean value.
		Note that it is not possible to set shape-dependent parameters.

		* value (bool) - the new value for this parameter."""
	def setDirty(self)->Self:
		"""setDirty() -> self

		Mark the data for this parameter as dirty. This will force the parameter to report that it has been changed the next time it is accessed. This allows external events (e.g. device lost, texture management, etc) to force a shader to re-set parameters tied to externally managed resources."""
	def setFloat(self,value:float)->Self:
		"""setFloat(value) -> self

		Set the value of this uniform parameter as a float.
		Note that it is not possible to set shape-dependent parameters.

		* value (float) - the new float value for this parameter."""
	def setFloatArray(self,value:tuple[float,...])->Self:
		"""setFloatArray(value) -> self

		Set the value of this uniform parameter as one or more floating point values.
		Note that it is not possible to set shape-specific parameters.

		* value (tuple of floats) - a tuple of floats holding the new floating point value(s) for this parameter."""
	def setInt(self,value:int)->Self:
		"""setInt(value) -> self

		Set the value of this uniform parameter as an integer value.
		Note that it is not possible to set shape-dependent parameters.

		* value (int) - the new value for this parameter."""
	def setString(self,value:str)->Self:
		"""setString(value) -> self

		Set the value of this uniform parameter as a string.
		Note that it is not possible to set shape-dependent parameters.

		 * value (string) - the new string value for this parameter."""
	def source(self)->om.MPlug:
		"""source() -> MPlug

		Get the source plug connected to this parameter. Other than textures, this will typically be an invalid plug."""
	def type(self)->int:
		"""type() -> int

		Get the type of this parameter.

		Available values:
		  kTypeUnknown,
		  kTypeBool,
		  kTypeInt,
		  kTypeFloat,
		  kType1DTexture,
		  kType2DTexture,
		  kType3DTexture,
		  kTypeCubeTexture,
		  kTypeEnvTexture,
		  kTypeString,
		  kTypeEnum"""
	def userData(self)->int:
		"""userData() -> int

		Get the user data for this parameter. User data can be used to store plugin specific information that you want to associate with this parameter. Typically this will be used to store a handle to the effect parameter."""
class MUniformParameterList:
	"""MUniformParameterList specify the list of uniform shader parameters used by a hardware shader, allowing Maya to handle setting up the node and user interfaces to the data, the population and access of cached data, etc."""
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def __len__(self)->int:
		"""Return len(self)."""
	def __getitem__(self,index:int)->Any:
		"""Return self[key]."""
	def append(self,element:MUniformParameter)->bool:
		"""append(element) -> bool

		Append a new parameter to this end of this list.

		* element (MUniformParameter) - The new parameter to append"""
	def copy(self,source:MUniformParameterList)->Self:
		"""copy(source) -> self

		Copy data from source list.

		* source (MUniformParameterList) - The source list to copy from"""
	def setElement(self,n:int,element:MUniformParameter)->bool:
		"""setElement(n, element) -> bool

		Set the nth parameter in this list.

		* n (int) - The index of the element to set
		* element (MUniformParameter) - The value to set"""
	def setLength(self,length:int)->bool:
		"""setLength(length) -> bool

		Set the number of parameters in this list. If this is greater than the current number of parameters in the list, the caller is responsible for setting the new parameters to valid values using setElement.

		* length (int) - The number of parameters in this list."""
class MUserRenderOperation(MRenderOperation):
	"""Class which defines a user defined rendering operation."""
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def addUIDrawables(self,drawManager:MUIDrawManager,frameContext:MFrameContext)->Self:
		"""addUIDrawables(drawManager, frameContext) -> self

		Provides access to the MUIDrawManager, which can be used to queue up operations to draw simple UI shapes like lines, circles, text, etc.

		This method will only be called when hasUIDrawables() is overridden to return true.

		* drawManager (MUIDrawManager) - The UI draw manager, it can be used to draw some simple geometry including text.
		* frameContext (MFrameContext) - Frame level context information"""
	def cameraOverride(self)->MCameraOverride:
		"""cameraOverride() -> MCameraOverride

		Query for a camera override."""
	def hasUIDrawables(self)->bool:
		"""hasUIDrawables() -> bool

		Query whether addUIDrawables() should be called or not."""
	def requiresLightData(self)->bool:
		"""requiresLightData() -> bool

		Indicates whether light data from the renderer is required for this user operation."""
	def requiresResetDeviceStates(self)->bool:
		"""requiresResetDeviceStates() -> bool

		Indicates whether reset of device states is required for this user operation."""
class MVaryingParameter:
	"""The MVaryingParameter class provides a high-level interface to hardware shader varying parameters. By defining your shader's varying data through this class, you allow Maya to handle the attributes, editing, serialisation, requirements setup, and cache management for you in a standard way that ensure you'll be able to leverage future performance and functionality improvements.

	To remove any ambiguity between constructors, the mandatory parameters of the third one have been swizzled:
	MVaryingParameter()
	MVaryingParameter(
	       name,
	       type,
	       minDimension=1,
	       maxDimension=1,
	       semantic=kNoSemantic,
	       invertTexCoords=False,
	       semanticName=None)
	MVaryingParameter(
	       dimension,
	       minDimension,
	       maxDimension,
	       name,
	       type,
	       semantic=kNoSemantic,
	       destinationSet=None,
	       invertTexCoords=False,
	       semanticName=None)"""
	kInvalidParameter:int=-1
	kStructure:int=0
	kFloat:int=1
	kDouble:int=2
	kChar:int=3
	kUnsignedChar:int=4
	kInt16:int=5
	kUnsignedInt16:int=6
	kInt32:int=7
	kUnsignedInt32:int=8
	kNoSemantic:int=0
	kPosition:int=1
	kNormal:int=2
	kTexCoord:int=3
	kColor:int=4
	kWeight:int=5
	kTangent:int=7
	kBinormal:int=8
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def addElement(self,child:MVaryingParameter)->Self:
		"""addElement(child) -> self

		Add a child element to this parameter.
		This operation is only valid for parameters of type kStructure.

		* child (MVaryingParameter) - the parameter to add to the structure."""
	def copy(self,source:MVaryingParameter)->Self:
		"""copy(source) -> self

		Copy data from source parameter.

		* source (MVaryingParameter) - The source parameter to copy from"""
	def destinationSetName(self)->str:
		"""destinationSetName() -> string

		Get the destination Set of this parameter."""
	def dimension(self)->int:
		"""dimension() -> int

		Get the dimension of this parameter."""
	def elementSize(self)->int:
		"""elementSize() -> int

		Get the size in bytes of one element of this parameter."""
	def getElement(self,index:int)->MVaryingParameter:
		"""getElement(index) -> MVaryingParameter

		Get an element within a structure.
		This operation is only valid for parameters of type kStructure.

		* index (int) - The index of the structure element to return."""
	def maximumStride(self)->int:
		"""maximumStride() -> int

		Get the maximum stride of this parameter in bytes.
		For parameter that accept a range of element counts, this corresponds to the maximum number of elements the parameter supports."""
	def name(self)->str:
		"""name() -> string

		Get the name of this parameter."""
	def numElements(self)->int:
		"""numElements() -> int

		Get the number of elements in this structure.
		This operation is only valid for parameters of type kStructure."""
	def removeElements(self)->Self:
		"""removeElements() -> self

		Remove all child elements from a structure.
		This operation is only valid for parameters of type kStructure."""
	def semantic(self)->int:
		"""semantic() -> int

		Get the semantic of this parameter.

		Available values:
		  kNoSemantic,
		  kPosition,
		  kNormal,
		  kTexCoord,
		  kColor,
		  kWeight,
		  kTangent,
		  kBinormal"""
	def semanticName(self)->str:
		"""semanticName() -> string

		Get the semantic name assigned to this parameter.
		The semanticName is used to identify a custom vertex stream request in order to fill the stream with the appropriate data requested by a shader override."""
	def setSource(self,semantic:Any,name:str)->Self:
		"""setSource(semantic, name) -> self

		While the source of geometry parameters is usually configured by the artist through Maya's user interface, this method allows you to programatically set the source of a geometry parameter, including both the data type (e.g. position, normal, etc) and an optional set name (e.g. UV set 'map1'). This is useful for implementing custom default values or shader operations.

		* type (int) - the type of data to populate this parameter with (see semantic())
		* name (string) - the specific data set to use for parameter types which support data sets, such as UV and color."""
	def sourceSetName(self)->str:
		"""sourceSetName() -> string

		If the current data type supports data sets (e.g. uv sets, color sets), get the name of the data set populating this parameter. This method will only return a useful value when called on leaf-level parameters (e.g. structures do not have sources, only the elements of a structure have sources)."""
	def sourceSemantic(self)->int:
		"""sourceSemantic() -> int

		Get the type of data (e.g. position, normal, uv) currently populating this parameter.
		This method will only return a useful value when called on leaf-level parameters (e.g. structures do not have sources, only the elements of a structure have sources).
		See semantic() for the list of values."""
	def type(self)->int:
		"""type() -> int

		Get the type of this parameter.

		Available values:
		  kInvalidParameter,
		  kStructure,
		  kFloat,
		  kDouble,
		  kChar,
		  kUnsignedChar,
		  kInt16,
		  kUnsignedInt16,
		  kInt32,
		  kUnsignedInt32"""
	def updateId(self)->int:
		"""updateId() -> int

		Get the update id.
		The update id is increased every time the parameter sources or sourceSet are changed. A plugin can compare the update id value between subsequent calls to this function to know if the source has changed since the last call."""
class MVaryingParameterList:
	"""MVaryingParameterList specify the surface component level data used by a hardware shader, allowing Maya to handle setting up the node and user interfaces to the data, the population and access of cached data, etc."""
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def __len__(self)->int:
		"""Return len(self)."""
	def __getitem__(self,index:int)->Any:
		"""Return self[key]."""
	def append(self,element:MVaryingParameter)->bool:
		"""append(element) -> bool

		Append a new parameter to this end of this list.

		* element (MVaryingParameter) - The new parameter to append"""
	def copy(self,source:MVaryingParameterList)->Self:
		"""copy(source) -> self

		Copy data from source list.

		* source (MVaryingParameterList) - The source list to copy from"""
	def setElement(self,n:int,element:MVaryingParameter)->bool:
		"""setElement(n, element) -> bool

		Set the nth parameter in this list.

		* n (int) - The index of the element to set
		* element (MVaryingParameter) - The value to set"""
	def setLength(self,length:int)->bool:
		"""setLength(length) -> bool

		Set the number of parameters in this list. If this is greater than the current number of parameters in the list, the caller is responsible for setting the new parameters to valid values using setElement.

		* length (int) - The number of parameters in this list."""
class MVertexBuffer:
	"""Vertex buffer for use with MGeometry."""
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def acquire(self,size:int,writeOnly:bool)->int:
		"""acquire(size, writeOnly) -> long

		Get a pointer to memory for the buffer.

		* size (int) - The size of the buffer to acquire.
		* writeOnly (bool) - Specified if the returned memory should be uninitialized or filled with actual buffer content.
		                     When the current buffer content is not needed, it is preferable to set the writeOnly flag to true for better performance."""
	def commit(self,long:Any)->Self:
		"""commit(long) -> self

		Commit the data stored in the memory given by acquire() to the buffer.
		If this method is not called, the acquired buffer will not be used in drawing.
		The pointer must be the same pointer returned from acquire()."""
	def descriptor(self)->MVertexBufferDescriptor:
		"""descriptor() -> MVertexBufferDescriptor

		Get the the buffer descriptor."""
	def hasCustomResourceHandle(self)->bool:
		"""hasCustomResourceHandle() -> bool

		Returns true if this vertex buffer is using a custom resource handle set
		by the plugin using MVertexBuffer.setResourceHandle(long, int)."""
	def lockResourceHandle(self)->Self:
		"""lockResourceHandle() -> self

		Lock the resource handle. The pointer returned from resourceHandle() is
		guaranteed to exist between lockResourceHandle() and unlockResourceHandle().

		MVertexBuffer may store data in system memory, GPU memory or both. Direct
		access to the GPU representation of the data is possible through the
		buffer's resourceHandle(). If the GPU representation of the data is to be
		directly modified using an external graphics or compute API, then
		lockResourceHandle() must be called on the MVertexBuffer once, before any
		modifications to the buffer are made.

		While a resource handle is locked, any external modifications to the GPU
		buffer will be recognized by Maya.

		While a resource handle is locked, consolidated world will take longer to
		consolidate the corresponding object. After unlocking a resource handle,
		consolidated world will take longer to consolidate the corresponding object
		one more time, the first time the unlocked resource handle is consolidated.

		Calling lockResourceHandle() and unlockResourceHandle() on a custom resource
		handle has no effect.

		Reallocating or deleting the GPU representation of the data between
		lockResourceHandle() and unlockResourceHandle() will result in undefined
		behavior. acquire(), commit() and update() may reallocate the GPU representation.
		unload() may delete the GPU representation.

		map() and unmap() will work if they are called between lockResourceHandle()
		and unlockResourceHandle(). They operate on the GPU representation."""
	def map(self)->int:
		"""map() -> long

		Get a read-only pointer to the existing content of the buffer.
		Writing new content in this memory block is not supported and can lead to unexpected behavior."""
	def resourceHandle(self)->int:
		"""resourceHandle() -> long

		Returns a long containing a C++ 'float' pointer which points to the graphics device dependent handle to the vertex buffer."""
	def setResourceHandle(self,long:Any,int:int)->Self:
		"""setResourceHandle(long, int) -> self

		Set the graphics-device-dependent hardware buffer resource handle."""
	def unload(self)->Self:
		"""unload() -> self

		If the buffer is resident in GPU memory, calling this method will move it to system memory and free the GPU memory."""
	def unlockResourceHandle(self)->Self:
		"""unlockResourceHandle() -> self

		Unlock the resource handle. The pointer returned from resourceHandle is not
		guaranteed to exist any more.
		See lockResourceHandle() for more details."""
	def unmap(self)->Self:
		"""unmap() -> self

		Release the data exposed by map(). If this method is not called, the buffer will not be recycled."""
	def update(self,buffer:int,destOffset:int,numVerts:int,truncateIfSmaller:bool)->Self:
		"""update(buffer, destOffset, numVerts, truncateIfSmaller) -> self

		Set a portion (or all) of the contents of the MVertexBuffer using the data in the provided software buffer.
		The internal hardware buffer will be allocated or reallocated to fit if required, according to the vertex size from the descriptor.

		* buffer (long) - The input data buffer, starting with the first vertex to copy.
		* destOffset (int) - The offset (in vertices) from the beginning of the buffer to start writing to.
		* numVerts (int) - The number of vertices to copy.
		* truncateIfSmaller (bool) - If true and offset+numVerts is less than the pre-existing size of the buffer,
		                             then the buffer contents will be truncated to the new size. Truncating the buffer size
		                             will not cause a reallocation and will not lose data before the destOffset."""
	def vertexCount(self)->int:
		"""vertexCount() -> int

		Get the size of the vertex buffer."""
class MVertexBufferArray(collections.abc.Sequence[MVertexBuffer]):
	"""Array of Vertex buffers."""
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def __len__(self)->int:
		"""Return len(self)."""
	def __getitem__(self,index:int)->MVertexBuffer:
		"""Return self[key]."""
	def append(self,MVertexBuffer:Any,name:str)->Self:
		"""append(MVertexBuffer, name) -> self

		Add a new vertex buffer to the list."""
	def clear(self)->Self:
		"""clear() -> self

		Clear the array."""
	def getBuffer(self,string:Any)->MVertexBuffer:
		"""getBuffer(string) -> MVertexBuffer

		Get vertex buffer by name."""
	def getName(self,int:int)->str:
		"""getName(int) -> string

		Get the name of the buffer at desired index."""
class MVertexBufferDescriptor:
	"""Describes properties of a vertex buffer."""
	@property
	def name(self)->Any:
		"""The name of the buffer.
		The buffer name is used to determine which render item this buffer belongs to.
		This name is typically set by the evaluator of the geometry."""
	@name.setter
	def name(self,value:Any)->None:...
	@property
	def semantic(self)->Any:
		"""The semantic of the buffer.
		See MGeometry.semanticString() for a list of valid semantic types."""
	@semantic.setter
	def semantic(self,value:Any)->None:...
	@property
	def semanticName(self)->Any:
		"""The semantic name of the buffer.
		The semanticName is used to identify a custom vertex stream request in order to fill
		the stream with the appropriate data requested by a shader override."""
	@semanticName.setter
	def semanticName(self,value:Any)->None:...
	@property
	def dataType(self)->Any:
		"""The data type of the buffer.
		See MGeometry.dataTypeString() for a list of valid data types."""
	@dataType.setter
	def dataType(self,value:Any)->None:...
	@property
	def dataTypeSize(self)->Any:
		"""The size in bytes of the data type of the buffer."""
	@dataTypeSize.setter
	def dataTypeSize(self,value:Any)->None:...
	@property
	def dimension(self)->Any:
		"""The dimension of the buffer."""
	@dimension.setter
	def dimension(self,value:Any)->None:...
	@property
	def offset(self)->Any:
		"""The offset of the vertex element in an interleaved vertex buffer.
		The value is currently only valid in the context of MPxShaderOverride.draw(), and only supported when using custom client buffers via resourceHandle(long)."""
	@offset.setter
	def offset(self,value:Any)->None:...
	@property
	def stride(self)->Any:
		"""The number of points per primitive."""
	@stride.setter
	def stride(self,value:Any)->None:...
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
class MVertexBufferDescriptorList:
	"""A list of MVertexBufferDescriptor objects."""
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def __len__(self)->int:
		"""Return len(self)."""
	def __getitem__(self,index:int)->Any:
		"""Return self[key]."""
	def append(self,MVertexBufferDescriptor:Any)->bool:
		"""append(MVertexBufferDescriptor) -> bool

		Add a descriptor to the list. Creates and stores a copy which is owned by the list."""
	def clear(self)->Self:
		"""clear() -> self

		Clear the list."""
	def remove(self,index:int)->bool:
		"""remove(index) -> bool

		Remove a descriptor from the list and delete it."""
