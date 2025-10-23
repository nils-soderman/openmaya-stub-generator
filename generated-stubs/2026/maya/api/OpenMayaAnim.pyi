"""
maya.api.OpenMayaAnim stub file generated for Maya 2026 using:
https://github.com/nils-soderman/openmaya-stub-generator
"""
from __future__ import annotations

import maya.api.OpenMaya as om
from typing import Any, Callable, Self, overload

class MAnimControl:
	"""Control over animation playback and values"""
	kPlaybackOnce:int=0
	kPlaybackLoop:int=1
	kPlaybackOscillate:int=2
	kPlaybackViewAll:int=0
	kPlaybackViewActive:int=1
	@staticmethod
	def playbackMode()->int:
		"""playbackMode() -> int

		Return the playback mode currently in effect:
		  MAnimControl.kPlaybackOnce         Play once then stop.
		  MAnimControl.kPlaybackLoop         Play continuously.
		  MAnimControl.kPlaybackOscillate    Play forwards, then backwards continuously."""
	@staticmethod
	def setPlaybackMode(int:int)->None:
		"""setPlaybackMode(int) -> None

		Set the current playback mode."""
	@staticmethod
	def viewMode()->int:
		"""viewMode() -> int

		Return the viewing mode currently in effect:
		  MAnimControl.kPlaybackViewAll      Playback in all views.
		  MAnimControl.kPlaybackViewActive   Playback in only the active view."""
	@staticmethod
	def setViewMode(int:int)->None:
		"""setViewMode(int) -> None

		Set the current viewing mode.
		Controls whether the animation is run in only the active view, or simultaneously in all views."""
	@staticmethod
	def playbackBy()->float:
		"""playbackBy() -> float

		Return a float specifying the increment between times viewed during the playing of the animation."""
	@staticmethod
	def setPlaybackBy(float:float)->None:
		"""setPlaybackBy(float) -> None

		Specify the increment between times viewed during the playing of the animation."""
	@staticmethod
	def minTime()->om.MTime:
		"""minTime() -> MTime

		Return an MTime specifying the first frame of the current playback time range."""
	@staticmethod
	def maxTime()->om.MTime:
		"""maxTime() -> MTime

		Return an MTime specifying the last frame of the current playback time range."""
	@staticmethod
	def setMinTime(MTime:Any)->None:
		"""setMinTime(MTime) -> None

		Set the value of the first frame of the current playback time range."""
	@staticmethod
	def setMaxTime(MTime:Any)->None:
		"""setMaxTime(MTime) -> None

		Set the value of the last frame of the current playback time range."""
	@staticmethod
	def setMinMaxTime(MTime:Any,MTime2:Any)->None:
		"""setMinMaxTime(MTime, MTime) -> None

		Set the values of the first and last frames of the playback time range."""
	@staticmethod
	def animationStartTime()->om.MTime:
		"""animationStartTime() -> MTime

		Return an MTime specifying the first frame of the animation, as specified by the Maya user in the Range Slider UI."""
	@staticmethod
	def animationEndTime()->om.MTime:
		"""animationEndTime() -> MTime

		Return an MTime specifying the last frame of the animation, as specified by the Maya user in the Range Slider UI."""
	@staticmethod
	def setAnimationStartTime(MTime:Any)->None:
		"""setAnimationStartTime(MTime) -> None

		Set the value of the first frame in the animation."""
	@staticmethod
	def setAnimationEndTime(MTime:Any)->None:
		"""setAnimationEndTime(MTime) -> None

		Set the value of the last frame in the animation."""
	@staticmethod
	def setAnimationStartEndTime(MTime:Any,MTime2:Any)->None:
		"""setAnimationStartEndTime(MTime, MTime) -> None

		Set the values of the first and last frames in the animation."""
	@staticmethod
	def currentTime()->om.MTime:
		"""currentTime() -> MTime

		Return an MTime instance containing the current animation frame."""
	@staticmethod
	def setCurrentTime(*args)->Any:
		"""setMinTime(MTime) -> None

		Set the current animation frame."""
	@staticmethod
	def playbackSpeed()->float:
		"""playbackSpeed() -> float

		Return the speed with with to play the animation."""
	@staticmethod
	def setPlaybackSpeed(float:float)->None:
		"""setPlaybackSpeed(float) -> None

		Set the desired speed factor at which the animation will play back."""
	@staticmethod
	def playForward()->None:
		"""playForward() -> None

		Start playing the current animation forwards."""
	@staticmethod
	def playBackward()->None:
		"""playBackward() -> None

		Start playing the current animation backwards."""
	@staticmethod
	def isPlaying()->bool:
		"""isPlaying() -> bool

		Return a value indicating whether Maya is currently playing the animation"""
	@staticmethod
	def isScrubbing()->bool:
		"""isScrubbing() -> bool

		Return a value indicating whether interactive scrubbing is occuring while Maya is not currently playing an animation."""
	@staticmethod
	def stop()->None:
		"""stop() -> None

		Stop playing the current animation."""
	@staticmethod
	def autoKeyMode()->bool:
		"""autoKeyMode() -> bool

		Return the autoKeyMode."""
	@staticmethod
	def setAutoKeyMode(bool:bool)->None:
		"""setAutoKeyMode(bool) -> None

		Set the autoKeyMode."""
	@staticmethod
	def globalInTangentType()->int:
		"""globalInTangentType() -> int

		Return the current global in tangent type."""
	@staticmethod
	def setGlobalInTangentType(int:int)->None:
		"""setGlobalInTangentType(int) -> None

		Set the current global in tangent type"""
	@staticmethod
	def globalOutTangentType()->int:
		"""globalOutTangentType() -> int

		Return the current global out tangent type."""
	@staticmethod
	def setGlobalOutTangentType(int:int)->None:
		"""setGlobalOutTangentType(int) -> None

		Set the current global out tangent type."""
	@staticmethod
	def weightedTangents()->bool:
		"""weightedTangents() -> bool

		Determine whether or not the tangents on the Anim Curve are weighted."""
	@staticmethod
	def setWeightedTangents(bool:bool)->None:
		"""setWeightedTangents(bool) -> None

		Sets whether or not the tangents on the Anim Curve are weighted."""
class MAnimCurveChange:
	"""Anim curve change cache."""
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def redoIt(self,*args)->Any:
		"""Redo all of the Anim Curve changes in this cache."""
	def undoIt(self,*args)->Any:
		"""Undo all of the Anim Curve changes in this cache."""
class MAnimCurveClipboard:
	"""Provides control over the animation clipboard.

	__init__()
	Initializes a new, empty MAnimCurveClipboard object."""
	@property
	def isEmpty(self)->Any:
		"""Whether the clipboard is empty."""
	@isEmpty.setter
	def isEmpty(self,value:Any)->None:...
	@property
	def startTime(self)->Any:
		"""The start time of the clipboard."""
	@startTime.setter
	def startTime(self,value:Any)->None:...
	@property
	def endTime(self)->Any:
		"""The end time of the clipboard."""
	@endTime.setter
	def endTime(self,value:Any)->None:...
	@property
	def startUnitlessInput(self)->Any:
		"""The start unitless input of the clipboard."""
	@startUnitlessInput.setter
	def startUnitlessInput(self,value:Any)->None:...
	@property
	def endUnitlessInput(self)->Any:
		"""The end unitless input of the clipboard."""
	@endUnitlessInput.setter
	def endUnitlessInput(self,value:Any)->None:...
	theAPIClipboard:MAnimCurveClipboard
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def clear(self)->Self:
		"""clear() -> self

		Clears the clipboard."""
	def clipboardItems(self)->MAnimCurveClipboardItemArray:
		"""clipboardItems() -> MAnimCurveClipboardItemArray

		Returns the clipboard items."""
	@overload
	def set(self,clipboard:Any)->Self:
		"""set( clipboard ) -> self
		set( items ) -> self
		set( items, startTime, endTime, startUnitlessInput, endUnitlessInput, strictValidation=True ) -> self

		Sets the content of the clipboard.
		'items' may be either an MAnimClipboardItemArray or a sequence of MAnimClipboardItems."""
	@overload
	def set(self,items:Any)->Self:
		"""set( clipboard ) -> self
		set( items ) -> self
		set( items, startTime, endTime, startUnitlessInput, endUnitlessInput, strictValidation=True ) -> self

		Sets the content of the clipboard.
		'items' may be either an MAnimClipboardItemArray or a sequence of MAnimClipboardItems."""
	@overload
	def set(self,items:Any,startTime:Any,endTime:Any,startUnitlessInput:Any,endUnitlessInput:Any,strictValidation:Any=True)->Self:
		"""set( clipboard ) -> self
		set( items ) -> self
		set( items, startTime, endTime, startUnitlessInput, endUnitlessInput, strictValidation=True ) -> self

		Sets the content of the clipboard.
		'items' may be either an MAnimClipboardItemArray or a sequence of MAnimClipboardItems."""
class MAnimCurveClipboardItem:
	"""This class provides a wrapper for a clipboard item.

	__init__()
	Initializes a new, empty MAnimCurveClipboardItem object."""
	@property
	def animCurve(self)->Any:
		"""The anim curve."""
	@animCurve.setter
	def animCurve(self,value:Any)->None:...
	@property
	def fullAttributeName(self)->Any:
		"""The full attribute name."""
	@fullAttributeName.setter
	def fullAttributeName(self,value:Any)->None:...
	@property
	def leafAttributeName(self)->Any:
		"""The leaf attribute name."""
	@leafAttributeName.setter
	def leafAttributeName(self,value:Any)->None:...
	@property
	def nodeName(self)->Any:
		"""The node name."""
	@nodeName.setter
	def nodeName(self,value:Any)->None:...
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def getAddressingInfo(self)->tuple[int,int,int]:
		"""getAddressingInfo() -> (unsigned int, unsigned int, unsigned int)

		Returns the addressing information for this clipboard item
		as (rowCount, childCount, attributeCount)."""
	def setAnimCurve(self,object:Any)->Self:
		"""setAnimCurve(object) -> self

		Sets the anim curve MObject."""
	def setAddressingInfo(self,rowCount:Any,childCount:Any,attributeCount:Any)->Self:
		"""setAddressingInfo(rowCount, childCount, attributeCount) -> self

		Sets the addressing information for this clipboard item."""
	def setNameInfo(self,nodeName:Any,fullName:Any,leafName:Any)->Self:
		"""setNameInfo(nodeName, fullName, leafName) -> self

		Sets the name information for this clipboard item."""
	def animCurveType(self)->MFnAnimCurve.AnimCurveType:
		"""animCurveType() -> MFnAnimCurve.AnimCurveType

		Returns the type of the item's anim curve."""
class MAnimCurveClipboardItemArray:
	"""Array of MAnimCurveClipboardItem values."""
	@property
	def sizeIncrement(self)->Any:
		"""Number of elements by which to grow the array when necessary."""
	@sizeIncrement.setter
	def sizeIncrement(self,value:Any)->None:...
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def __len__(self)->int:
		"""Return len(self)."""
	def __getitem__(self,index:int)->Any:
		"""Return self[key]."""
	def __setitem__(self,index:int,value)->None:
		"""Set self[key] to value."""
	def __delitem__(self,index:int)->None:
		"""Delete self[key]."""
	def __add__(self,other)->Any:
		"""Return self+value."""
	def __mul__(self,other)->Any:
		"""Return self*value."""
	def __rmul__(self,other)->Any:
		"""Return value*self."""
	def __contains__(self,item)->bool:
		"""Return key in self."""
	def __iadd__(self,other)->Any:
		"""Implement self+=value."""
	def __imul__(self,other)->Any:
		"""Implement self*=value."""
	def append(self,item)->None:
		"""Add a value to the end of the array."""
	def copy(self,*args)->Any:
		"""Replace the array contents with that of another or of a compatible Python sequence."""
	def clear(self)->None:
		"""Remove all elements from the array."""
	def insert(self,index:int,item)->None:
		"""Insert a new value into the array at the given index."""
	def remove(self,item)->None:
		"""Remove an element from the array."""
	def setLength(self,*args)->Any:
		"""Grow or shrink the array to contain a specific number of elements."""
class MAnimMessage(MMessage):
	"""Class used to register callbacks for anim related messages."""
	@staticmethod
	def addAnimCurveEditedCallback(function:Callable,clientData:Any|None=None)->int:
		"""addAnimCurveEditedCallback(function, clientData=None) -> id

		This method registers a callback that is called whenever an
		AnimCurve is edited.

		 * function - callable which will be passed a MObjectArray object containing
		   an array of AnimCurves which have been edited, and the clientData object
		 * clientData - User defined data passed to the callback function

		 * return: Identifier used for removing the callback."""
	@staticmethod
	def addAnimKeyframeEditedCallback(function:Callable,clientData:Any|None=None)->int:
		"""addAnimKeyframeEditedCallback(function, clientData=None) -> id

		This method registers a callback that is called whenever an
		a group of keys are modified.  The callback is invoked once per
		atomic change to single or group of keyframes. For example, if
		a user selects a group 5 of keys and moves them 5 units in the value
		axis, then a single callback event will be invoked with a MObject
		for each of the 5 keyframes.  The MObjects can then be used in the
		MFnKeyframeDelta function set. Refer to MFnKeyframeDelta function set
		documentation for more info.

		 * function - callable which will be passed a MObjectArray object containing
		   an array of keyframes that were edited, and the clientData object
		 * clientData - User defined data passed to the callback function

		 * return: Identifier used for removing the callback."""
	@staticmethod
	def addAnimKeyframeEditCheckCallback(function:Callable,clientData:Any|None=None)->int:
		"""addAnimKeyframeEditCheckCallback(function, clientData=None) -> id

		This method registers a callback that is used by the setKeyframe command
		to allow a user to consider the set keyframe request and cancel it if
		needed. The callback method should return False to abort the keyframe
		setting.

		 * function - callable which will be passed a MPlug indicating the
		   plug being keyframed and the clientData object.
		   Return False to abort the keyframe action, otherwise return True
		 * clientData - User defined data passed to the callback function

		 * return: Identifier used for removing the callback."""
	@staticmethod
	def addNodeAnimKeyframeEditedCallback(animNode:om.MObject,function:Callable,clientData:Any|None=None)->int:
		"""addNodeAnimKeyframeEditedCallback(animNode, function, clientData=None) -> id

		This method registers a callback that is called whenever an a
		group of keys are modified.  The callback is invoked once per
		atomic change to single or group of keyframes on the specified
		animation curve node. For example, if a user selects a group 5
		of keys and moves them 5 units in the value axis, then a single
		callback event will be invoked with a MObject for each of the 5
		keyframes.  The MObjects can then be used in the MFnKeyframeDelta
		function set. Refer to MFnKeyframeDelta function set documentation
		for more info.

		 * animNode (MObject) - the param curve node you want to watch.
		 * function - callable which will be passed a MObject indicating the
		   edited animation node, a MObjectArray containing an array of keyframes
		   that were edited and the clientData object.
		 * clientData - User defined data passed to the callback function

		 * return: Identifier used for removing the callback."""
	@staticmethod
	def addPreBakeResultsCallback(function:Callable,clientData:Any|None=None)->int:
		"""addPreBakeResultsCallback(function, clientData=None) -> id

		This method registers a callback that is called from bakeResults
		command before the simulation. One example usage is handle the runup to
		the first frame in a dynamic system. If plugArray is set to zero
		length in the callback, the baking will be aborted.

		 * function - callable which will be passed a MPlugArray containing the plugs
		   to be baked (they can be replaced but must have the same number of plugs)
		   ,a MDGModifier used if bakeResults command is undone or redone and the
		   clientData object.
		 * clientData - User defined data passed to the callback function

		 * return: Identifier used for removing the callback."""
	@staticmethod
	def addPostBakeResultsCallback(function:Callable,clientData:Any|None=None)->int:
		"""addPostBakeResultsCallback(function, clientData=None) -> id

		This method registers a callback that is called from bakeResults
		command after the simulation. If the plugArray is replaced, then
		the anim curves created from baking will be connected to the new
		plugs.

		 * function - callable which will be passed a MPlugArray containing the baked
		   plugs to which the resulting anim curves will be connected (they can be
		   replaced but must have the same number of plugs),a MDGModifier used if
		   bakeResults command is undone or redone and the clientData object.
		 * clientData - User defined data passed to the callback function

		 * return: Identifier used for removing the callback."""
	@staticmethod
	def addDisableImplicitControlCallback(function:Callable,clientData:Any|None=None)->int:
		"""addDisableImplicitControlCallback(function, clientData=None) -> id

		This method registers a callback that is called from bakeResults
		command after baking operation is completed, if disableImplicitControl
		is enabled. One example usage of this callback is to create the anim curve
		that is used to drive Maya rigidbody's bakeSimulationIndex, which defines
		if the rigid body should take its input from anim curve or rigid body
		simulation.

		 * function - callable which will be passed a MPlugArray containing the baked plugs
		   (they can be replaced but must have the same number of plugs), a MDGModifier used
		   if bakeResults command is undone or redone and the clientData object.
		 * clientData - User defined data passed to the callback function

		 * return: Identifier used for removing the callback."""
	@staticmethod
	def flushAnimKeyframeEditedCallbacks()->None:
		"""flushAnimKeyframeEditedCallbacks() -> None

		Animation keyframe edited callbacks are queued to only be issued on an
		idle event. There may be times when it is desired to issue the callback
		at a specific time. This method provides this functionality. It will
		flush all animation keyframe edited callbacks and force them to issue
		their callbacks with the data contained within."""
class MAnimUtil:
	"""Static class providing common animation helper methods.
	"""
	@staticmethod
	@overload
	def isAnimated(MObject:Any,bool:bool)->bool:
		"""isAnimated(MObject, bool) -> bool
		isAnimated(MDagPath, bool) -> bool
		isAnimated(MPlug, bool) -> bool
		isAnimated(MSelectionList selectionList, bool checkParent) -> bool

		Determine whether or not an MObject is animated.
		If the MObject is a hierarchical object (such as a dag node) then
		you may also specify whether or not the input object's parents are examined."""
	@overload
	@staticmethod
	def isAnimated(MDagPath:Any,bool:bool)->bool:
		"""isAnimated(MObject, bool) -> bool
		isAnimated(MDagPath, bool) -> bool
		isAnimated(MPlug, bool) -> bool
		isAnimated(MSelectionList selectionList, bool checkParent) -> bool

		Determine whether or not an MObject is animated.
		If the MObject is a hierarchical object (such as a dag node) then
		you may also specify whether or not the input object's parents are examined."""
	@overload
	@staticmethod
	def isAnimated(MPlug:Any,bool:bool)->bool:
		"""isAnimated(MObject, bool) -> bool
		isAnimated(MDagPath, bool) -> bool
		isAnimated(MPlug, bool) -> bool
		isAnimated(MSelectionList selectionList, bool checkParent) -> bool

		Determine whether or not an MObject is animated.
		If the MObject is a hierarchical object (such as a dag node) then
		you may also specify whether or not the input object's parents are examined."""
	@overload
	@staticmethod
	def isAnimated(selectionList:om.MSelectionList,checkParent:bool)->bool:
		"""isAnimated(MObject, bool) -> bool
		isAnimated(MDagPath, bool) -> bool
		isAnimated(MPlug, bool) -> bool
		isAnimated(MSelectionList selectionList, bool checkParent) -> bool

		Determine whether or not an MObject is animated.
		If the MObject is a hierarchical object (such as a dag node) then
		you may also specify whether or not the input object's parents are examined."""
	@staticmethod
	@overload
	def findAnimatedPlugs(MObject:Any,bool:bool)->om.MPlugArray:
		"""findAnimatedPlugs(MObject, bool) -> MPlugArray
		findAnimatedPlugs(MDagPath, bool) -> MPlugArray
		findAnimatedPlugs(MSelectionList selectionList, bool checkParent) -> MPlugArray

		Find the list of attributes (MPlugs) on the input object that is animated."""
	@overload
	@staticmethod
	def findAnimatedPlugs(MDagPath:Any,bool:bool)->om.MPlugArray:
		"""findAnimatedPlugs(MObject, bool) -> MPlugArray
		findAnimatedPlugs(MDagPath, bool) -> MPlugArray
		findAnimatedPlugs(MSelectionList selectionList, bool checkParent) -> MPlugArray

		Find the list of attributes (MPlugs) on the input object that is animated."""
	@overload
	@staticmethod
	def findAnimatedPlugs(selectionList:om.MSelectionList,checkParent:bool)->om.MPlugArray:
		"""findAnimatedPlugs(MObject, bool) -> MPlugArray
		findAnimatedPlugs(MDagPath, bool) -> MPlugArray
		findAnimatedPlugs(MSelectionList selectionList, bool checkParent) -> MPlugArray

		Find the list of attributes (MPlugs) on the input object that is animated."""
	@staticmethod
	def findAnimation(MPlug:Any)->om.MObjectArray:
		"""findAnimation(MPlug) -> MObjectArray

		Find the animCurve(s) that are animating a given attribute (MPlug).
		In most cases an attribute is animated by a single animCurve and so
		just that animCurve will be returned.  It is possible to setup a
		series of connections where an attribute is animated by more than
		one animCurve, although Maya does not currently offer a UI to do so.
		Compound attributes are not expanded to include any child attributes."""
	@staticmethod
	def findSetDrivenKeyAnimation(MPlug:Any)->tuple[om.MObjectArray,om.MPlugArray]:
		"""findSetDrivenKeyAnimation(MPlug) -> (MObjectArray, MPlugArray)

		Find any driven keyframe animCurves, the blendWeighted node and the
		driver attribute(s) that are animating a given attribute (MPlug).
		Or return false if no driven keyframe exists on the attribute.

		A driven keyframe is similar to a regular keyframe. However, while a
		standard keyframe always has an x-axis of time in the graph editor,
		for a drivenkeyframe the user may choose any attribute
		as the x-axis of the graph editor. This attribute is called the driver.

		In the case where there is only one driver, the animation curve
		will be connected directly to the driven attribute. When there are
		multiple drivers, the driven keyframe animCurves feed into a
		blendWeighted node which drives the attribute.

		Compound attributes are not expanded to include any child attributes."""
	@staticmethod
	def findConstraint(Mplug:Any)->tuple[om.MObject,om.MObjectArray]:
		"""findConstraint(Mplug) -> (MObject, MObjectArray)

		Find any constraint that is directly driving the specified attribute.
		If a constraint is found, this method will also find the constraint
		targets. Return false if no constraint exists on the attribute.

		Compound attributes are not expanded to include any child attributes."""
	@staticmethod
	def findAnimatablePlugs(MSelectionList:Any)->om.MPlugArray:
		"""findAnimatablePlugs(MSelectionList) -> MPlugArray

		Find the list of attributes (MPlugs) on any member of an MSelectionList
		that is animatable.

		In addition to normal objects, components such as mesh vertices or
		faces can be easily described on an MSelectionList, making this a
		good way to determine if parts of a shape are animatable or not."""
class MFnAnimCurve(MFnDependencyNode):
	"""Function set for operations on anim curves.

	__init__()
	Initializes a new, empty MFnAnimCurve object.

	__init__(MObject object)
	Initializes a new MFnAnimCurve and attaches it
	to an animCurve object.

	__init__(MPlug plug)
	Initializes a new MFnAnimCurve and attaches it
	to the single animCurve node connected to the given MPlug."""
	@property
	def animCurveType(self)->Any:
		"""Anim curve type."""
	@animCurveType.setter
	def animCurveType(self,value:Any)->None:...
	@property
	def isStatic(self)->Any:
		"""Whether the curve is static."""
	@isStatic.setter
	def isStatic(self,value:Any)->None:...
	@property
	def numKeys(self)->Any:
		"""Number of keys."""
	@numKeys.setter
	def numKeys(self,value:Any)->None:...
	@property
	def isTimeInput(self)->Any:
		"""Whether the curve has time as an input."""
	@isTimeInput.setter
	def isTimeInput(self,value:Any)->None:...
	@property
	def isUnitlessInput(self)->Any:
		"""Whether the curve has unitless input."""
	@isUnitlessInput.setter
	def isUnitlessInput(self,value:Any)->None:...
	@property
	def isWeighted(self)->Any:
		"""Whether the curve has weighted tangents."""
	@isWeighted.setter
	def isWeighted(self,value:Any)->None:...
	@property
	def preInfinityType(self)->Any:
		"""The curve's pre-infinity type."""
	@preInfinityType.setter
	def preInfinityType(self,value:Any)->None:...
	@property
	def postInfinityType(self)->Any:
		"""The curve's post-infinity type."""
	@postInfinityType.setter
	def postInfinityType(self,value:Any)->None:...
	kAnimCurveTA:int=0
	kAnimCurveTL:int=1
	kAnimCurveTT:int=2
	kAnimCurveTU:int=3
	kAnimCurveUA:int=4
	kAnimCurveUL:int=5
	kAnimCurveUT:int=6
	kAnimCurveUU:int=7
	kAnimCurveUnknown:int=8
	kTangentGlobal:int=0
	kTangentFixed:int=1
	kTangentLinear:int=2
	kTangentFlat:int=3
	kTangentSmooth:int=4
	kTangentStep:int=5
	kTangentSlow:int=6
	kTangentFast:int=7
	kTangentClamped:int=8
	kTangentPlateau:int=9
	kTangentStepNext:int=10
	kTangentAuto:int=11
	kTangentShared1:int=19
	kTangentShared2:int=20
	kTangentShared3:int=21
	kTangentShared4:int=22
	kTangentShared5:int=23
	kTangentShared6:int=24
	kTangentShared7:int=25
	kTangentShared8:int=26
	kTangentAutoMix:int=27
	kTangentAutoEase:int=28
	kTangentAutoCustom:int=29
	kTangentCustomStart:int=64
	kTangentCustomEnd:int=32767
	kTangentTypeCount:int=32768
	kConstant:int=0
	kLinear:int=1
	kCycle:int=3
	kCycleRelative:int=4
	kOscillate:int=5
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	@overload
	def create(self,node:Any,attribute:Any,animCurveType:int=MFnAnimCurve.kAnimCurveUnknown,modifier:Any=...)->om.MObject:
		"""create(node, attribute, animCurveType=kAnimCurveUnknown [, modifier] ) -> MObject
		create(plug, animCurveType=kAnimCurveUnknown [, modifier] ) -> MObject
		create(animCurveType [, modifier] ) -> MObject

		Creates a new animCurve node.
		If node and attribute (MObject) are supplied, the animCurvewill be connected to the given attribute on the given node.
		If plug (MPlug) is supplied, the animCurvewill be connected to the given plug.
		modifier is an optional MDGModifier which can be used to later undo the operation.
		animCurveType specifies the type of animCurve to create. Valid values are:
		kAnimCurveTA            Time to Angular
		kAnimCurveTL            Time to Linear
		kAnimCurveTT            Time to Time
		kAnimCurveTU            Time to Unitless
		kAnimCurveUA            Unitless to Angular
		kAnimCurveUL            Unitless to Linear
		kAnimCurveUT            Unitless to Time
		kAnimCurveUU            Unitless to Unitless
		kAnimCurveUnknown       Unknown type"""
	@overload
	def create(self,plug:Any,animCurveType:int=MFnAnimCurve.kAnimCurveUnknown,modifier:Any=...)->om.MObject:
		"""create(node, attribute, animCurveType=kAnimCurveUnknown [, modifier] ) -> MObject
		create(plug, animCurveType=kAnimCurveUnknown [, modifier] ) -> MObject
		create(animCurveType [, modifier] ) -> MObject

		Creates a new animCurve node.
		If node and attribute (MObject) are supplied, the animCurvewill be connected to the given attribute on the given node.
		If plug (MPlug) is supplied, the animCurvewill be connected to the given plug.
		modifier is an optional MDGModifier which can be used to later undo the operation.
		animCurveType specifies the type of animCurve to create. Valid values are:
		kAnimCurveTA            Time to Angular
		kAnimCurveTL            Time to Linear
		kAnimCurveTT            Time to Time
		kAnimCurveTU            Time to Unitless
		kAnimCurveUA            Unitless to Angular
		kAnimCurveUL            Unitless to Linear
		kAnimCurveUT            Unitless to Time
		kAnimCurveUU            Unitless to Unitless
		kAnimCurveUnknown       Unknown type"""
	@overload
	def create(self,animCurveType:Any,modifier:Any=...)->om.MObject:
		"""create(node, attribute, animCurveType=kAnimCurveUnknown [, modifier] ) -> MObject
		create(plug, animCurveType=kAnimCurveUnknown [, modifier] ) -> MObject
		create(animCurveType [, modifier] ) -> MObject

		Creates a new animCurve node.
		If node and attribute (MObject) are supplied, the animCurvewill be connected to the given attribute on the given node.
		If plug (MPlug) is supplied, the animCurvewill be connected to the given plug.
		modifier is an optional MDGModifier which can be used to later undo the operation.
		animCurveType specifies the type of animCurve to create. Valid values are:
		kAnimCurveTA            Time to Angular
		kAnimCurveTL            Time to Linear
		kAnimCurveTT            Time to Time
		kAnimCurveTU            Time to Unitless
		kAnimCurveUA            Unitless to Angular
		kAnimCurveUL            Unitless to Linear
		kAnimCurveUT            Unitless to Time
		kAnimCurveUU            Unitless to Unitless
		kAnimCurveUnknown       Unknown type"""
	def timedAnimCurveTypeForPlug(self,plug:Any)->AnimCurveType:
		"""timedAnimCurveTypeForPlug(plug) -> AnimCurveType

		Returns the timed animCurve type appropriate for the specified plug."""
	def unitlessAnimCurveTypeForPlug(self,plug:Any)->AnimCurveType:
		"""unitlessAnimCurveTypeForPlug(plug) -> AnimCurveType

		Returns the unitless animCurve type appropriate for the specified plug."""
	def evaluate(self,at:Any)->float:
		"""evaluate(at) -> value

		Evalutes the curve.
		For curves of type kAnimCurveTA, kAnimCurveTL and kAnimCurveTU,the at parameter is an MTime, otherwise it is a double.
		For curves of type kAnimCurveTT and kAnimCurveUT,the value is an MTime, otherwise it is a double."""
	def remove(self,index:Any,change:Any|None=None)->Self:
		"""remove(index, change=None) -> self

		Removes the key at the specified index.
		change is an optional MAnimCurveChange."""
	def addKey(self,at:Any,value:Any,tangentInType:int=MFnAnimCurve.kTangentGlobal,tangentOutType:int=MFnAnimCurve.kTangentGlobal,change:Any|None=None)->int:
		"""addKey(at, value, tangentInType=kTangentGlobal, tangentOutType=kTangentGlobal, change=None) -> unsigned int

		Adds a new key with the given value at the specified time.
		at and value can both be either MTime or double,depending on what is appropriate for the animCurve type.
		change is an optional MAnimCurveChange."""
	def addKeys(self,times:Any,values:Any,tangentInType:int=MFnAnimCurve.kTangentGlobal,tangentOutType:int=MFnAnimCurve.kTangentGlobal,keepExistingKeys:Any=False,change:Any|None=None)->Self:
		"""addKeys(times, values, tangentInType=kTangentGlobal, tangentOutType=kTangentGlobal, keepExistingKeys=False, change=None) -> self

		Add a set of new keys with the given corresponding values and tangent typesat the specified times.  This method only works for animCurves of typekAnimCurveTA, kAnimCurveTL and kAnimCurveTU."""
	def insertKey(self,*args)->Any:
		"""addKey(time, breakdown=False, change=None) -> unsigned int

		Inserts a new key at the specified time adjusting neighboring
		tangents to maintain curve shape. This method is the API equivalent
		to maya.cmds.setKeyframe(insert=True).
		breakdown specifies the breakdown state of the newly inserted key.
		change is an optional MAnimCurveChange.
		Returns the index of the newly inserted key."""
	def addKeysWithTangents(self,times:Any,values:Any,tangentInType:int=MFnAnimCurve.kTangentGlobal,tangentOutType:int=MFnAnimCurve.kTangentGlobal,tangentInTypeArray:Any|None=None,tangentOutTypeArray:Any|None=None,tangentInXArray:Any|None=None,tangentInYArray:Any|None=None,tangentOutXArray:Any|None=None,tangentOutYArray:Any|None=None,tangentsLockedArray:Any|None=None,weightsLockedArray:Any|None=None,convertUnits:Any=True,keepExistingKeys:Any=False,change:Any|None=None)->Self:
		"""addKeysWithTangents(times, values, tangentInType=kTangentGlobal, tangentOutType=kTangentGlobal, tangentInTypeArray=None, tangentOutTypeArray=None, tangentInXArray=None, tangentInYArray=None, tangentOutXArray=None, tangentOutYArray=None, tangentsLockedArray=None, weightsLockedArray=None, convertUnits=True, keepExistingKeys=False, change=None) -> self

		Add a set of new keys with the given corresponding values, tangent types and tangents at the specified times.  This method only works for animCurves of typekAnimCurveTA, kAnimCurveTL and kAnimCurveTU."""
	def find(self,at:Any)->int:
		"""find(at) -> unsigned int

		Determines the index of the key which is set at the specifiedMTime (time-input curves) or double (unitless-input curves).
		Returns None if the key is not found."""
	def findClosest(self,at:Any)->int:
		"""findClosest(at) -> unsigned int

		Determines the index of the key which is set at theMTime (time-input curves) or double (unitless-input curves)closest to the specified time."""
	def input(self,index:Any)->om.MTime|float:
		"""input(index) -> MTime or double

		Determines the input (MTime for T* curves or double for U* curves) of the key at the specified index."""
	def value(self,index:Any)->float:
		"""value(index) -> double

		Determines the value of the key at the specified index.  This methodshould only be used on Anim Curves of type kAnimCurve*A, kAnimCurve*Lor kAnimCurve*U."""
	def quaternionW(self,index:Any)->float:
		"""quaternionW(index) -> double

		Returns the quaternionW of the key at the specified index.  This methodshould only be used on Anim Curves of type kAnimCurveTA."""
	def setValue(self,index:Any,value:Any,change:Any|None=None)->Self:
		"""setValue(index, value, change=None) -> self

		Sets the value of the key at the specified index.  This methodshould only be used on Anim Curves of type kAnimCurve*A, kAnimCurve*Lor kAnimCurve*U."""
	def setQuaternionW(self,index:Any,quaternionW:Any,change:Any|None=None)->Self:
		"""setQuaternionW(index, quaternionW, change=None) -> self

		Sets the quaternionW of the key at the specified index.  This methodshould only be used on Anim Curves of type kAnimCurve*A."""
	def setInput(self,index:Any,at:Any,change:Any|None=None)->Self:
		"""setInput(index, at, change=None) -> self

		Sets the input (MTime for T* curves or double for U* curves) of the key at the specified index.  This will fail ifsetting the input would require re-ordering of the keys."""
	def inTangentType(self,index:Any)->TangentType:
		"""inTangentType(index) -> TangentType

		Determines the type of the tangent to the curve entering the current key."""
	def outTangentType(self,index:Any)->TangentType:
		"""outTangentType(index) -> TangentType

		Determines the type of the tangent to the curve leaving the current key."""
	def setInTangentType(self,index:Any,tangentType:Any,change:Any|None=None)->Self:
		"""setInTangentType(index, tangentType, change=None) -> self

		Sets the type of the tangent to the curve entering the key at thespecified index.
		Valid values for tangentType are:
		kTangentGlobal          Global
		kTangentFixed           Fixed
		kTangentLinear          Linear
		kTangentFlat            Flag
		kTangentSmooth          Smooth
		kTangentStep            Step
		kTangentSlow            OBSOLETE kTangentSlow should not be used. Using this tangent type may produce unwanted and unexpected results.
		kTangentFast            OBSOLETE kTangentFast should not be used. Using this tangent type may produce unwanted and unexpected results.
		kTangentClamped Clamped
		kTangentPlateau Plateau
		kTangentStepNext        StepNext
		kTangentAuto            AutokTangentAutoMix             AutoMixkTangentAutoEase         AutoEasekTangentAutoCustom              AutoCustom"""
	def setOutTangentType(self,index:Any,tangentType:Any,change:Any|None=None)->Self:
		"""setOutTangentType(index, tangentType, change=None) -> self

		Sets the type of the tangent to the curve leaving the key at thespecified index."""
	def setTangentTypes(self,indexArray:Any,tangentInType:int=MFnAnimCurve.kTangentGlobal,tangentOutType:int=MFnAnimCurve.kTangentGlobal,change:Any|None=None)->Self:
		"""setTangentTypes(indexArray, tangentInType=kTangentGlobal, tangentOutType=kTangentGlobal, change=None) -> self

		Sets the tangent types for multiple keys."""
	def getTangentXY(self,index:Any,isInTangent:Any)->tuple[float,float]:
		"""getTangentXY(index, isInTangent) -> (x,y)

		Determines the x,y value representing the vector of the in- orout-tangent (depending on the value of the isInTangent parameter) tothe curve for the key at the specified index.  The values returnedwill be in Maya's internal units (seconds for time, centimeters forlinear, radians for angles)."""
	def getTangentAngleWeight(self,index:Any,isInTangent:Any)->tuple[om.MAngle,float]:
		"""getTangentAngleWeight(index, isInTangent) -> (MAngle,double)

		Determines the angle and weight of the in- or out-tangent to the curvefor the key at the specified index"""
	def setTangent(self,index:Any,xOrAngle:Any,yOrWeight:Any,isInTangent:Any,change:Any|None=None,convertUnits:Any=True)->Self:
		"""setTangent(index, xOrAngle, yOrWeight, isInTangent, change=None, convertUnits=True) -> self

		Sets the tangent for the key at the specified index.
		The tangent can be specified as an x/y pair, oras an MAngle and a weight.
		isInTangent is True to modify the inTangent or False to modify the outTangent."""
	def setAngle(self,index:Any,setAngle:Any,isInTangent:Any,change:Any|None=None)->Self:
		"""setAngle(index, setAngle, isInTangent, change=None) -> self

		Sets the in- or out-angle of the tangent for the key at the given index.
		isInTangent is True to modify the inTangent or False to modify the outTangent."""
	def setWeight(self,index:Any,weight:Any,isInTangent:Any,change:Any|None=None)->Self:
		"""setWeight(index, weight, isInTangent, change=None) -> self

		Sets the in- or out-weight of the tangent for the key at the given index.
		isInTangent is True to modify the inTangent or False to modify the outTangent."""
	def weightsLocked(self,index:Any)->bool:
		"""weightsLocked(index) -> bool

		Determines whether the weights are locked at the given key."""
	def tangentsLocked(self,index:Any)->bool:
		"""tangentsLocked(index) -> bool

		Determines whether the tangents are locked at the given key."""
	def setWeightsLocked(self,index:Any,locked:Any,change:Any|None=None)->Self:
		"""setWeightsLocked(index, locked, change=None) -> self

		Lock or unlock the weights at the given key."""
	def setTangentsLocked(self,index:Any,locked:Any,change:Any|None=None)->Self:
		"""setTangentsLocked(index, locked, change=None) -> self

		Lock or unlock the tangents at the given key."""
	def setIsWeighted(self,isWeighted:Any,change:Any|None=None)->Self:
		"""setIsWeighted(isWeighted, change=None) -> self

		Sets whether or not the curve has weighted tangents."""
	def isBreakdown(self,index:Any)->bool:
		"""isBreakdown(index) -> bool

		Determines whether or not a key is a breakdown."""
	def setIsBreakdown(self,index:Any,isBreakdown:Any,change:Any|None=None)->Self:
		"""setIsBreakdown(index, isBreakdown, change=None) -> self

		Sets the breakdown state of a key at a given index."""
	def setPreInfinityType(self,infinityType:Any,change:Any|None=None)->Self:
		"""setPreInfinityType(infinityType, change=None) -> self

		Sets the behaviour of the curve for the range occurring before the first key.
		Valid values for infinityType are:
		kConstant                       Constant
		kLinear                 Linear
		kCycle                          Cycle
		kCycleRelative          Cycle relative
		kOscillate                      Oscillate"""
	def setPostInfinityType(self,infinityType:Any,change:Any|None=None)->Self:
		"""setPostInfinityType(infinityType, change=None) -> self

		Sets the behaviour of the curve for the range occurring after the last key."""
class MFnGeometryFilter(MFnDependencyNode):
	"""Function set for operating on geometryFilter nodes.
	geometryFilter is the abstract node type from which all
	deformer node types derive.

	__init__()
	Initializes a new, empty MFnGeometryFilter functionset.

	__init__(MObject)
	Initializes a new MFnGeometryFilter functionset and attaches it
	to a geometryFilter node."""
	@property
	def deformerSet(self)->Any:
		"""Object set containing the objects that are deformed. Adding new
		components to the deformer set will cause them to be deformed.
		Removing components from the deformer set will prevent them from
		being influenced by the deformer.

		Note that the wrap deformer and the skinCluster deformers are
		special cases: they allow only a single object to be deformed per
		wrap/skinCluster, so adding additional geometries to them will have
		no effect."""
	@deformerSet.setter
	def deformerSet(self,value:Any)->None:...
	@property
	def envelope(self)->Any:
		"""A global scale factor that is applied to all the values."""
	@envelope.setter
	def envelope(self,value:Any)->None:...
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def getInputGeometry(self)->om.MObjectArray:
		"""getInputGeometry() -> MObjectArray

		Returns the DAG nodes which provide input geometry to the deformer.
		These are found by traversing the graph to find upstream shape nodes.
		It is possible for there to be nodes in between the shape and the
		deformer so that the returned shape may have a different topology or
		tweaks then the input data to the deformer. If the actual input
		geometry data for the deformer is required, this information can be
		accessed by using MPlug::getValue() to query the inputGeometry
		attribute on the deformer."""
	def getOutputGeometry(self)->om.MObjectArray:
		"""getOutputGeometry() -> MObjectArray

		Returns the DAG nodes which receive output geometry from the deformer."""
	def getPathAtIndex(self,plugIndex:int)->om.MDagPath:
		"""getPathAtIndex(plugIndex) -> MDagPath

		Returns the DAG path of the specified output geometry.

		* plugIndex (unsigned int) - Plug index of the desired geometry."""
	def groupIdAtIndex(self,plugIndex:int)->int:
		"""groupIdAtIndex(plugIndex) -> long

		Returns the groupId associated with the specified geometry.

		* plugIndex (unsigned int) - Plug index of the desired geometry."""
	def indexForGroupId(self,groupId:int)->plugIndex:
		"""indexForGroupId(groupId) -> plugIndex

		Returns the plug index of the geometry associated with the specified groupId.

		* groupId (unsigned int) - groupId of the desired geometry."""
	def indexForOutputConnection(self,connIndex:int)->plugIndex:
		"""indexForOutputConnection(connIndex) -> plugIndex

		Returns the plug index corresponding to a connection index. The
		connection index is the contiguous (physical) index of the output
		connection, ranging from 0 to numOutputConnections()-1. The plug
		index is the sparse (logical) index of the connection.

		* connIndex (unsigned int) - Connection index of the desired geometry."""
	def indexForOutputShape(self,shape:om.MObject)->plugIndex:
		"""indexForOutputShape(shape) -> plugIndex

		Returns the plug index for the specified output shape.

		* shape (MObject) - Shape for which the plug index is requested."""
	def inputShapeAtIndex(self,plugIndex:int)->om.MObject:
		"""inputShapeAtIndex(plugIndex) -> MObject

		Returns the input shape corresponding to the plug index.

		* plugIndex (unsigned int) - Plug index of the desired shape."""
	def numOutputConnections(self)->int:
		"""numOutputConnections() -> long

		Returns the number of output geometries connected to this node. This
		is typically equal to the number of input geometries unless an input
		or output geometry has been deleted, or a connection to an input or
		output geometry has been broken.

		This method is useful in conjunction with indexForOutputConnection()
		to iterate through the affected objects."""
	def outputShapeAtIndex(self,index:Any)->om.MObject:
		"""outputShapeAtIndex(index) -> MObject

		Returns the DAG path to which this function set is attached, or the first path to the node if the function set is attached to an MObject."""
	def getComponentAtIndex(self,index:Any)->om.MObject:
		"""getComponentAtIndex(index) -> MObject

		Returns the component which contains the members of the deformer
		at the given index."""
class MFnIkJoint(MFnTransform):
	"""Function set joints.

	__init__()
	Initializes a new, empty MFnIKJoint object.

	"""
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def create(self,parent:Any=MObject.kNullObj)->Any:
		"""create(parent=MObject.kNullObj) -> new joint node MObject


		Create a new joint in a skeleton.  In maya, skeletons are defined
		entirely by DAG hierarchy.  So, giving the joint you want to attach
		to as a parent will add this joint to that skeleton.

		parent: the parent object for this in the dag.  A value of
		                                        NULL specifies the world dag node as parent.
		Return: The parent transform of the new joint"""
	def degreesOfFreedom(self,*args)->Any:
		"""Gets degrees of freedom for this joint, that is, which axes are free
		to rotate"""
	def hikJointName(self,*args)->Any:
		"""Get the name that HIK uses to identify this joint"""
	def maxRotateDampXRange(self,*args)->Any:
		"""Get the maximum of the damping range in X. This corresponds to the
		maxRotateDampXRange attribute on the joint"""
	def maxRotateDampXStrength(self,*args)->Any:
		"""Get the maximum of the damping strength in X. This corresponds to the
		maxRotateDampXStrength attribute on the joint"""
	def maxRotateDampYRange(self,*args)->Any:
		"""Get the maximum of the damping range in Y. This corresponds to the
		maxRotateDampYRange attribute on the joint"""
	def maxRotateDampYStrength(self,*args)->Any:
		"""Get the maximum of the damping strength in Y. This corresponds to the
		maxRotateDampYStrength attribute on the joint"""
	def maxRotateDampZRange(self,*args)->Any:
		"""Get the maximum of the damping range in Z. This corresponds to the
		maxRotateDampZRange attribute on the joint"""
	def maxRotateDampZStrength(self,*args)->Any:
		"""Get the maximum of the damping strength in Z. This corresponds to the
		maxRotateDampZStrength attribute on the joint"""
	def minRotateDampXRange(self,*args)->Any:
		"""Get the minimum of the damping range in X. This corresponds to the
		minRotateDampXRange attribute on the joint"""
	def minRotateDampXStrength(self,*args)->Any:
		"""Get the minimum of the damping strength in X. This corresponds to the
		minRotateDampXStrength attribute on the joint"""
	def minRotateDampYRange(self,*args)->Any:
		"""Get the minimum of the damping range in Y. This corresponds to the
		minRotateDampYRange attribute on the joint"""
	def minRotateDampYStrength(self,*args)->Any:
		"""Get the minimum of the damping strength in Y. This corresponds to the
		minRotateDampYStrength attribute on the joint"""
	def minRotateDampZRange(self,*args)->Any:
		"""Get the minimum of the damping range in Z. This corresponds to the
		minRotateDampZRange attribute on the joint"""
	def minRotateDampZStrength(self,*args)->Any:
		"""Get the minimum of the damping strength in Z. This corresponds to the
		minRotateDampZStrength attribute on the joint"""
	def orientation(self,*args)->Any:
		"""Gets the joint orientation as either an Euler rotation or a
		quaternion"""
	def orientationComponents(self,*args)->Any:
		"""Get the joint orientation

		Return: rotation angles and rotation order"""
	def preferredAngle(self,*args)->Any:
		"""Get the preferred orientation angle for the joint.

		Return: preferred angle"""
	def scaleOrientation(self,*args)->Any:
		"""Gets the orientation of the coordinate axes, as either a quaternion
		or a sequence of 4 values, namely, the Euler rotation components and
		the order"""
	def segmentScale(self,*args)->Any:
		"""Get the local space scale values for the joint segment (bone). This is
		equivalent to calling MFnTransform::getScale.

		Return: segment scale"""
	def setDegreesOfFreedom(self,*args)->Any:
		"""Set the degrees of freedom for this joint by specifying which axes
		are allowed to rotate"""
	def setMaxRotateDampXRange(self,*args)->Any:
		"""Set the maximum of the damping range in X. This corresponds to the
		setMaxRotateDampXRange attribute on the joint"""
	def setMaxRotateDampXStrength(self,*args)->Any:
		"""Set the maximum of the damping strength in X. This corresponds to the
		setMaxRotateDampXStrength attribute on the joint"""
	def setMaxRotateDampYRange(self,*args)->Any:
		"""Set the maximum of the damping range in Y. This corresponds to the
		setMaxRotateDampYRange attribute on the joint"""
	def setMaxRotateDampYStrength(self,*args)->Any:
		"""Set the maximum of the damping strength in Y. This corresponds to the
		setMaxRotateDampYStrength attribute on the joint"""
	def setMaxRotateDampZRange(self,*args)->Any:
		"""Set the maximum of the damping range in Z. This corresponds to the
		setMaxRotateDampZRange attribute on the joint"""
	def setMaxRotateDampZStrength(self,*args)->Any:
		"""Set the maximum of the damping strength in Z. This corresponds to the
		setMaxRotateDampZStrength attribute on the joint"""
	def setMinRotateDampXRange(self,*args)->Any:
		"""Set the minimum of the damping range in X. This corresponds to the
		setMinRotateDampXRange attribute on the joint"""
	def setMinRotateDampXStrength(self,*args)->Any:
		"""Set the minimum of the damping strength in X. This corresponds to the
		setMinRotateDampXStrength attribute on the joint"""
	def setMinRotateDampYRange(self,*args)->Any:
		"""Set the minimum of the damping range in Y. This corresponds to the
		setMinRotateDampYRange attribute on the joint"""
	def setMinRotateDampYStrength(self,*args)->Any:
		"""Set the minimum of the damping strength in Y. This corresponds to the
		setMinRotateDampYStrength attribute on the joint"""
	def setMinRotateDampZRange(self,*args)->Any:
		"""Set the minimum of the damping range in Z. This corresponds to the
		setMinRotateDampZRange attribute on the joint"""
	def setMinRotateDampZStrength(self,*args)->Any:
		"""Set the minimum of the damping strength in Z. This corresponds to the
		setMinRotateDampZStrength attribute on the joint"""
	def setOrientation(self,*args)->Any:
		"""Sets the joint orientation, which can be specified as either an Euler
		rotation, a quaternion, or a sequence of 4 values, namely, the Euler
		rotation components and the order"""
	def setPreferredAngle(self,*args)->Any:
		"""Set the preferred orientation angle for the joint."""
	def setScaleOrientation(self,*args)->Any:
		"""Sets the orientation of the coordinate axes, which can be specified as either an Euler
		rotation, a quaternion, or a sequence of 4 values, namely, the Euler
		rotation components and the order"""
	def setSegmentScale(self,*args)->Any:
		"""Set the segment scale for the joint."""
	def setStiffness(self,*args)->Any:
		"""Set the stiffness for the joint. This is equivalent to calling
		MFnTransform::setScale"""
	def stiffness(self,*args)->Any:
		"""Get the stiffness for the joint.

		Return: stiffness"""
class MFnSkinCluster(MFnGeometryFilter):
	"""Function set for operating on skinCluster nodes.
	SkinCluster nodes are created during a smooth bindSkin. They
	store a weight per influence object for each component of the
	geometry that is deformed. Influence objects can be joints or
	any transform.

	Unlike most deformers, a skinCluster node can deform only a
	single geometry. Therefore, if additional geometries are added
	to the skinCluster set, they will be ignored.

	__init__()
	Initializes a new, empty MFnSkinCluster functionset.

	__init__(MObject)
	Initializes a new MFnSkinCluster functionset and attaches it to
	a skinCluster node."""
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def getBlendWeights(self,shape:om.MDagPath,components:om.MObject)->om.MDoubleArray:
		"""getBlendWeights(shape, components) -> MDoubleArray

		Returns blend weights for the specified components of the deformed
		shape. Blend weights are used to determine the blending between
		classical linear skinning and dual quaternion bases skinning on a
		per vertex basis. The returned array contains one weight per component
		in the order given by 'components'.

		* shape     (MDagPath) - the object being deformed by the skinCluster
		* components (MObject) - components for which weights should be returned"""
	def getPointsAffectedByInfluence(self,influence:om.MDagPath)->tuple[om.MSelectionList,om.MDoubleArray]:
		"""getPointsAffectedByInfluence(influence) -> (MSelectionList, MDoubleArray)

		During deformation, the skinCluster algorithm is applied for a given
		influence object on all points in the deformer's set whose weights
		are non-zero. This returns the non-zero weights for a particular
		influence object.

		The return value is a tuple consisting of a selection list, which
		contains the dag path and components that are affected by the
		specified influence object, and the corresponding weights for the
		components. If no components are weighted for a specified influence
		the selection list will be empty.

		* influence (MDagPath) - the influence object of interest"""
	@overload
	def getWeights(self,shape:om.MDagPath,components:om.MObject)->tuple[om.MDoubleArray,int]:
		"""getWeights(shape, components) -> (MDoubleArray, int)
		getWeights(shape, components, influence) -> MDoubleArray
		getWeights(shape, components, influences) -> MDoubleArray

		Returns the skinCluster weights of the given influence objects on
		the specified components of the deformed shape.


		If no influence index is provided then a tuple containing the weights
		and the number of influence objects will be returned.

		If a single influence index is provided the an array of weights will
		be returned, one per component in the same order as in 'components'.

		If an array of influence indices is provided an array of weights will
		be returned containing as many weights for each component as there
		are influences in the 'influenceIndices' array. The weights will be
		in component order: i.e. all of the weight values for the first
		component, followed by all the weight values for the second component,
		and so on.

		* shape       (MDagPath) - the object being deformed by the skinCluster
		* components   (MObject) - components to return weights for
		* influence        (int) - index of the single influence to return weights for
		* influences (MIntArray) - indices of multiple influences to return weights for"""
	@overload
	def getWeights(self,shape:om.MDagPath,components:om.MObject,influence:int)->om.MDoubleArray:
		"""getWeights(shape, components) -> (MDoubleArray, int)
		getWeights(shape, components, influence) -> MDoubleArray
		getWeights(shape, components, influences) -> MDoubleArray

		Returns the skinCluster weights of the given influence objects on
		the specified components of the deformed shape.


		If no influence index is provided then a tuple containing the weights
		and the number of influence objects will be returned.

		If a single influence index is provided the an array of weights will
		be returned, one per component in the same order as in 'components'.

		If an array of influence indices is provided an array of weights will
		be returned containing as many weights for each component as there
		are influences in the 'influenceIndices' array. The weights will be
		in component order: i.e. all of the weight values for the first
		component, followed by all the weight values for the second component,
		and so on.

		* shape       (MDagPath) - the object being deformed by the skinCluster
		* components   (MObject) - components to return weights for
		* influence        (int) - index of the single influence to return weights for
		* influences (MIntArray) - indices of multiple influences to return weights for"""
	@overload
	def getWeights(self,shape:om.MDagPath,components:om.MObject,influences:om.MIntArray)->om.MDoubleArray:
		"""getWeights(shape, components) -> (MDoubleArray, int)
		getWeights(shape, components, influence) -> MDoubleArray
		getWeights(shape, components, influences) -> MDoubleArray

		Returns the skinCluster weights of the given influence objects on
		the specified components of the deformed shape.


		If no influence index is provided then a tuple containing the weights
		and the number of influence objects will be returned.

		If a single influence index is provided the an array of weights will
		be returned, one per component in the same order as in 'components'.

		If an array of influence indices is provided an array of weights will
		be returned containing as many weights for each component as there
		are influences in the 'influenceIndices' array. The weights will be
		in component order: i.e. all of the weight values for the first
		component, followed by all the weight values for the second component,
		and so on.

		* shape       (MDagPath) - the object being deformed by the skinCluster
		* components   (MObject) - components to return weights for
		* influence        (int) - index of the single influence to return weights for
		* influences (MIntArray) - indices of multiple influences to return weights for"""
	def indexForInfluenceObject(self,influenceObj:om.MObject)->int:
		"""indexForInfluenceObject(influenceObj) -> long

		Returns the logical index of the matrix array attribute where the
		specified influence object is attached.

		* influenceObj (MObject) - influence object for which the index is requested."""
	def influenceObjects(self)->om.MDagPathArray:
		"""influenceObjects() -> MDagPathArray

		Returns an array of paths to the influence objects for the skinCluster."""
	def setBlendWeights(self,shape:om.MDagPath,components:om.MObject,weights:om.MDoubleArray)->Self:
		"""setBlendWeights(shape, components, weights) -> self

		Sets blend weights for the specified components of the shape being
		deformed by the skinCluster. Blend weights are used to determine the
		blending between classical linear skinning and dual quaternion bases
		skinning on a per vertex basis.

		* shape       (MDagPath) - object being deformed by the skinCluster
		* components   (MObject) - components of 'shape' to set blend weights for
		* weights (MDoubleArray) - weights to set, one per component. If the
		                           length of this array does match the number
		                           of components provided then the lesser of
		                           the two will be used."""
	@overload
	def setWeights(self,shape:om.MDagPath,components:om.MObject,influence:int,weight:float,normalize:bool=True,returnOldWeights:bool=False)->None|om.MDoubleArray:
		"""setWeights(shape, components, influence, weight, normalize=True, returnOldWeights=False) -> None or MDoubleArray
		setWeights(shape, components, influences, weights, normalize=True, returnOldWeights=False) -> None or MDoubleArray

		Sets the skinCluster weights for one or more influence objects on
		the specified components of the given shape. If 'returnOldWeights'
		is True then the old weights will be returned, otherwise None will
		be returned

		If only a single influence index and weight are specified then that
		weight is applied to all of the specified components. The returned
		array of old weights, if requested, will contain weights for ALL of
		the skinCluster's influence objects, not just the one specified by
		the 'influence' parameter.

		If arrays of influence indices and weights are provided then the
		behaviour depends upon the number of elements in the 'weights' array.
		If it's equal to the number of influences specified then each weight
		will be used for all of components for the corresponding influence
		object. If it's equal to the number of influences times the number of
		components provided, then a separate weight will be used for each
		component, with all of the weights for the first component coming
		first in the 'weights' array, followed by all of the weights for the
		second component, and so on. Within each component the weights will
		will correspond with the ordering of influence indices in the
		'influences' array. The returned old weights, if requested, will
		consist of a separate weight for

		The returned old weights will be ordered by influence within
		component, i.e. all of the influence weights for the first component
		will come first in the array, followed by all the weights for the
		second component, and so on.

		* shape       (MDagPath) - object being deformed by the skinCluster
		* components   (MObject) - the components to set weights on
		* influence        (int) - physical index of a single influence object
		* weight         (float) - single weight to be applied to all components.
		* influences (MIntArray) - physical indices of several influence objects.
		* weights (MDoubleArray) - weights to be used with several influence objects.
		* normalize       (bool) - if True, normalize weights on other influence objects
		* returnOldWeights(bool) - if True, return the old weights, otherwise return None"""
	@overload
	def setWeights(self,shape:om.MDagPath,components:om.MObject,influences:om.MIntArray,weights:om.MDoubleArray,normalize:bool=True,returnOldWeights:bool=False)->None|om.MDoubleArray:
		"""setWeights(shape, components, influence, weight, normalize=True, returnOldWeights=False) -> None or MDoubleArray
		setWeights(shape, components, influences, weights, normalize=True, returnOldWeights=False) -> None or MDoubleArray

		Sets the skinCluster weights for one or more influence objects on
		the specified components of the given shape. If 'returnOldWeights'
		is True then the old weights will be returned, otherwise None will
		be returned

		If only a single influence index and weight are specified then that
		weight is applied to all of the specified components. The returned
		array of old weights, if requested, will contain weights for ALL of
		the skinCluster's influence objects, not just the one specified by
		the 'influence' parameter.

		If arrays of influence indices and weights are provided then the
		behaviour depends upon the number of elements in the 'weights' array.
		If it's equal to the number of influences specified then each weight
		will be used for all of components for the corresponding influence
		object. If it's equal to the number of influences times the number of
		components provided, then a separate weight will be used for each
		component, with all of the weights for the first component coming
		first in the 'weights' array, followed by all of the weights for the
		second component, and so on. Within each component the weights will
		will correspond with the ordering of influence indices in the
		'influences' array. The returned old weights, if requested, will
		consist of a separate weight for

		The returned old weights will be ordered by influence within
		component, i.e. all of the influence weights for the first component
		will come first in the array, followed by all the weights for the
		second component, and so on.

		* shape       (MDagPath) - object being deformed by the skinCluster
		* components   (MObject) - the components to set weights on
		* influence        (int) - physical index of a single influence object
		* weight         (float) - single weight to be applied to all components.
		* influences (MIntArray) - physical indices of several influence objects.
		* weights (MDoubleArray) - weights to be used with several influence objects.
		* normalize       (bool) - if True, normalize weights on other influence objects
		* returnOldWeights(bool) - if True, return the old weights, otherwise return None"""
class MFnWeightGeometryFilter(MFnGeometryFilter):
	"""Function set for operating on weightGeometryFilter nodes.
	weightGeometryFilter is the abstract node type from which
	weighted deformer node types derive.

	__init__()
	Initializes a new, empty MFnWeightGeometryFilter functionset.

	__init__(MObject)
	Initializes a new MFnWeightGeometryFilter functionset and attaches it
	to a geometryFilter node."""
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	@overload
	def getWeights(self,index:Any,components:om.MObject)->om.MFloatArray:
		"""getWeights(index, components) -> MFloatArray
		getWeights(path, components) -> MFloatArray


		Returns the weight values of the components.
		* plugIndex (unsigned int) - Plug index of the desired geometry.
		* path (MDagPath) - The path of the DAG object that has the components.
		* components (MObject) - The components whose weights are requested."""
	@overload
	def getWeights(self,path:om.MDagPath,components:om.MObject)->om.MFloatArray:
		"""getWeights(index, components) -> MFloatArray
		getWeights(path, components) -> MFloatArray


		Returns the weight values of the components.
		* plugIndex (unsigned int) - Plug index of the desired geometry.
		* path (MDagPath) - The path of the DAG object that has the components.
		* components (MObject) - The components whose weights are requested."""
	@overload
	def setWeight(self,path:om.MDagPath,index:int,components:om.MObject,weight:float,oldValues:om.MFloatArray|None=None)->None:
		"""setWeight(path, index, components, weight, oldValues=None)
		setWeight(path, index, components, values)
		setWeight(path, components, weight, oldValues=None)
		setWeight(path, components, values)


		Returns the status of the operation.
		* path (MDagPath) - The path of the DAG object that has the components.
		* index (unsigned int) - Plug index of the desired geometry.
		* components (MObject) - The components of the object.
		* weight (float) - Weight weight value for the components.
		* values (MFloatArray) -  An array of new values for the components.
		* oldValues (MFloatArray) -  An array of old values for the components."""
	@overload
	def setWeight(self,path:om.MDagPath,index:int,components:om.MObject,values:om.MFloatArray)->None:
		"""setWeight(path, index, components, weight, oldValues=None)
		setWeight(path, index, components, values)
		setWeight(path, components, weight, oldValues=None)
		setWeight(path, components, values)


		Returns the status of the operation.
		* path (MDagPath) - The path of the DAG object that has the components.
		* index (unsigned int) - Plug index of the desired geometry.
		* components (MObject) - The components of the object.
		* weight (float) - Weight weight value for the components.
		* values (MFloatArray) -  An array of new values for the components.
		* oldValues (MFloatArray) -  An array of old values for the components."""
	@overload
	def setWeight(self,path:om.MDagPath,components:om.MObject,weight:float,oldValues:om.MFloatArray|None=None)->None:
		"""setWeight(path, index, components, weight, oldValues=None)
		setWeight(path, index, components, values)
		setWeight(path, components, weight, oldValues=None)
		setWeight(path, components, values)


		Returns the status of the operation.
		* path (MDagPath) - The path of the DAG object that has the components.
		* index (unsigned int) - Plug index of the desired geometry.
		* components (MObject) - The components of the object.
		* weight (float) - Weight weight value for the components.
		* values (MFloatArray) -  An array of new values for the components.
		* oldValues (MFloatArray) -  An array of old values for the components."""
	@overload
	def setWeight(self,path:om.MDagPath,components:om.MObject,values:om.MFloatArray)->None:
		"""setWeight(path, index, components, weight, oldValues=None)
		setWeight(path, index, components, values)
		setWeight(path, components, weight, oldValues=None)
		setWeight(path, components, values)


		Returns the status of the operation.
		* path (MDagPath) - The path of the DAG object that has the components.
		* index (unsigned int) - Plug index of the desired geometry.
		* components (MObject) - The components of the object.
		* weight (float) - Weight weight value for the components.
		* values (MFloatArray) -  An array of new values for the components.
		* oldValues (MFloatArray) -  An array of old values for the components."""
	def getEnvelopeWeights(self,index:int)->om.MFloatArray:
		"""getEnvelopeWeights(index) -> MFloatArray


		Returns the weights the deformer uses for the geometry at the specified plug index.
		* index (unsigned int) - Plug index of the desired geometry."""
	def weightPlugStrings(self,list:om.MSelectionList)->str:
		"""weightPlugStrings(list) -> MString


		Returns a string (separated by spaces) containing the names of the plugs on this node that correspond to the components in the selection list.
		* list (MSelectionList) - selection list that contains components."""
	def getWeightPlugStrings(self,*args)->Any:
		"""weightPlugStrings(list) -> MStringArray


		Returns the names of the plugs on this node that correspond to the components in the selection list.
		* list (MSelectionList) - selection list that contains components."""
