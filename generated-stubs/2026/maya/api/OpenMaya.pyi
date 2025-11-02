"""
maya.api.OpenMaya stub file generated for Maya 2026 using:
https://github.com/nils-soderman/openmaya-stub-generator
"""
from __future__ import annotations

import collections.abc
import sys
from typing import Any, Callable, Literal, Self, Sequence, overload

class MAngle:
	"""Manipulate angular data."""
	@property
	def unit(self)->int:
		"""Angular units used by the angle."""
	@unit.setter
	def unit(self,value:int)->None:...
	@property
	def value(self)->float:
		"""Value of the angle."""
	@value.setter
	def value(self,value:float)->None:...
	kInvalid:int=0
	kRadians:int=1
	kDegrees:int=2
	kAngMinutes:int=3
	kAngSeconds:int=4
	kLast:int=5
	@overload
	def __init__(self)->None:
		"""Default constructor. Returns a new MAngle with a value of 0.0 radians."""
	@overload
	def __init__(self,src:MAngle)->None:
		"""Copy constructor. Returns a new MAngle having the same value and unit as src ."""
	@overload
	def __init__(self,value:float,unit:int)->None:
		"""Returns a new MAngle having the specified value and unit ."""
	def asUnits(self,unit:int)->float:
		"""Returns the angular value converted to the specified unit ."""
	def asRadians(self)->float:
		"""Returns the angular value converted to radians."""
	def asDegrees(self)->float:
		"""Returns the angular value converted to degrees."""
	def asAngMinutes(self)->float:
		"""Returns the angular value converted to minutes of arc."""
	def asAngSeconds(self)->float:
		"""Returns the angular value converted to seconds of arc."""
	@staticmethod
	def uiUnit()->int:
		"""Returns the units currently used by Maya's UI when entering and displaying angular values."""
	@staticmethod
	def setUIUnit(newUnit:int)->None:
		"""Sets the units used by Maya's UI when entering and displaying angular values."""
	@staticmethod
	def internalUnit()->int:
		"""Returns the unit type used by Maya to store angular values internally (e.g. in plugs and binary files)."""
	@staticmethod
	def internalToUI(internalValue:float)->float:
		"""Interprets internalValue as an angular value in Maya's internal units and returns it converted to UI units."""
	@staticmethod
	def uiToInternal(uiValue:float)->float:
		"""Interprets uiValue as an angular value in Maya's UI units and returns it converted to UI units."""
class MArgDatabase(MArgParser):
	"""Command argument list parser which extends MArgParser with the
	ability to return arguments and objects as MSelectionLists"""
	def __init__(self,syntax:MSyntax,args:MArgList)->None:
		"""Creates a new MArgDatabase object which will parse args using the provided syntax ."""
	def commandArgumentMSelectionList(self,index:int)->MSelectionList:
		"""Returns the specified command argument in an MSelectionList . Raises TypeError if the argument cannot be placed in an MSelectionList . Raises IndexError if index is out of range."""
	def flagArgumentMSelectionList(self,flag:str,index:int)->MSelectionList:
		"""Returns the index 'th argument of the specified flag in an MSelectionList . Raises TypeError if the argument cannot be placed in an MSelectionList . Raises IndexError if index is out of range."""
	def getObjectList(self)->MSelectionList:
		"""Returns the list of objects passed to the command as an MSelectionList ."""
class MArgList:
	"""Argument list for passing to commands."""
	kInvalidArgIndex:int=-1
	@overload
	def __init__(self)->None:
		"""Default constructor. Returns a new, empty MArgList object."""
	@overload
	def __init__(self,src:MArgList)->None:
		"""Copy constructor. Returns a new MArgList object with the same args as src ."""
	def __len__(self)->int:
		"""Return len(self)."""
	def addArg(self,arg:bool|int|float|str|MAngle|MDistance|MPoint|MTime|MVector)->Any:
		"""Add an argument to the end of the arg list."""
	def asAngle(self,index:int)->MAngle:
		"""Return an argument as an MAngle . IndexError will be raised if index is out of bounds."""
	def asBool(self,index:int)->bool:
		"""Return an argument as a boolean. IndexError will be raised if index is out of bounds."""
	def asDistance(self,index:int)->MDistance:
		"""Return an argument as an MDistance . IndexError will be raised if index is out of bounds."""
	def asDouble(self,index:int)->float:
		"""Alias for asFloat() ."""
	def asDoubleArray(self,index:int)->MDoubleArray:
		"""Return a sequence of arguments as an MDoubleArray . IndexError will be raised if index is out of bounds."""
	def asFloat(self,index:int)->float:
		"""Return an argument as a float. IndexError will be raised if index is out of bounds."""
	def asInt(self,index:int)->int:
		"""Return an argument as an integer. IndexError will be raised if index is out of bounds."""
	def asIntArray(self,index:int)->MIntArray:
		"""Return a sequence of arguments as an MIntArray . IndexError will be raised if index is out of bounds."""
	def asMatrix(self,index:int)->MMatrix:
		"""Return a sequence of arguments as an MMatrix . IndexError will be raised if index is out of bounds."""
	def asPoint(self,index:int,numElements:int=3)->MPoint:
		"""Return a sequence of arguments as an MPoint . ValueError will be raised if numElements is greater than 4 as that is the maximum dimension for an MPoint . IndexError will be raised if index is out of bounds"""
	def asString(self,index:int)->str:
		"""Return an argument as a string. IndexError will be raised if index is out of bounds."""
	def asStringArray(self,index:int)->list[str]:
		"""Return a sequence of arguments as a list of strings. IndexError will be raised if index is out of bounds."""
	def asTime(self,index:int)->MTime:
		"""Return an argument as an MTime . IndexError will be raised if index is out of bounds."""
	def asVector(self,index:int,numElements:int=3)->MVector:
		"""Return a sequence of arguments as an MVector . ValueError will be raised if numElements is greater than 3 as that is the maximum dimension for an MVector . IndexError will be raised if index is out of bounds."""
	def flagIndex(self,shortName:str,longName:str|None=None)->int:
		"""Return the index of the first occurrence of the specified flag or kInvalidFlagIndex if the flag is not in the arg list."""
	def lastArgUsed(self)->int:
		"""Return the index of the last argument used by the most recent as*() method call, or -1 if no arguments have been used yet."""
class MArgParser:
	"""Command argument list parser."""
	@property
	def isEdit(self)->bool:
		"""True if the edit flag is present."""
	@property
	def isQuery(self)->bool:
		"""True if the query flag is present."""
	@property
	def numberOfFlagsUsed(self)->int:
		"""Number of different flags used on the command line. If the same flag appears multiple times it is only counted once."""
	def __init__(self,syntax:MSyntax,args:MArgList)->None:
		"""Creates a new MArgParser object which will parse args using the provided syntax ."""
	def commandArgumentBool(self,index:int)->bool:
		"""Returns the specified command argument as a bool."""
	def commandArgumentDouble(self,index:int)->float:
		"""This is an alternate name for commandArgumentFloat()"""
	def commandArgumentFloat(self,index:int)->float:
		"""Returns the specified command argument as a float."""
	def commandArgumentInt(self,index:int)->int:
		"""Returns the specified command argument as an int."""
	def commandArgumentMAngle(self,index:int)->MAngle:
		"""Returns the specified command argument as an MAngle ."""
	def commandArgumentMDistance(self,index:int)->MDistance:
		"""Returns the specified command argument as an MDistance ."""
	def commandArgumentMTime(self,index:int)->MTime:
		"""Returns the specified command argument as an MTime ."""
	def commandArgumentString(self,index:int)->str:
		"""Returns the specified command argument as a string."""
	def flagArgumentBool(self,flag:str,index:int)->bool:
		"""Returns the index 'th argument of the specified flag as a bool. Raises RuntimeError if the flag has been enabled for multi-use."""
	def flagArgumentDouble(self,flag:str,index:int)->float:
		"""This is an alternate name for flagArgumentFloat() ."""
	def flagArgumentFloat(self,flag:str,index:int)->float:
		"""Returns the index 'th argument of the specified flag as a float. Raises RuntimeError if the flag has been enabled for multi-use."""
	def flagArgumentInt(self,flag:str,index:int)->int:
		"""Returns the index 'th argument of the specified flag as a int. Raises RuntimeError if the flag has been enabled for multi-use."""
	def flagArgumentMAngle(self,flag:str,index:int)->MAngle:
		"""Returns the index 'th argument of the specified flag as an MAngle . Raises RuntimeError if the flag has been enabled for multi-use."""
	def flagArgumentMDistance(self,flag:str,index:int)->MDistance:
		"""Returns the index 'th argument of the specified flag as an MDistance . Raises RuntimeError if the flag has been enabled for multi-use."""
	def flagArgumentMTime(self,flag:str,index:int)->MTime:
		"""Returns the index 'th argument of the specified flag as an MTime . Raises RuntimeError if the flag has been enabled for multi-use."""
	def flagArgumentString(self,flag:str,index:int)->str:
		"""Returns the index 'th argument of the specified flag as a string. Raises RuntimeError if the flag has been enabled for multi-use."""
	def getFlagArgumentList(self,flag:str,occurrence:int)->MArgList:
		"""Returns the arguments for the specified occurrence of the given multi-use flag as an MArgList . Raises RuntimeError if the flag has not been enabled for multi-use. Raises IndexError if occurrence is out of range."""
	def getFlagArgumentPosition(self,flag:str,index:int)->int:
		"""Returns the position in the argument list of the specified occurrence of the given flag . Raises IndexError if occurrence is out of range."""
	def getObjectStrings(self)->tuple[str,...]:
		"""If the command's MSyntax has set the object format to kStringObjects then this method will return the objects passed to the command as a tuple of strings. If any other object format is set then an empty tuple will be returned."""
	def isFlagSet(self,flag:str)->bool:
		"""Returns True if the given flag appears on the command line."""
	def numberOfFlagUses(self,flag:str)->int:
		"""Returns the number of times that the flag appears on the command line."""
class MArrayDataBuilder:
	"""Array builder for arrays in data blocks."""
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def __len__(self)->int:
		"""Return len(self)."""
	def addElement(self,index:int)->MDataHandle:
		"""addElement(index) -> MDataHandle

		Adds a new element to the array at the given index.

		* index (int) - the index at which we wish to add the new element

		Returns The handle for the new element"""
	def addElementArray(self,index:int)->MArrayDataHandle:
		"""addElementArray(index) -> MArrayDataHandle

		Adds a new element to the array at the given index.  The added element is also an array.

		* index (int) - the index at which we wish to add the new element

		Returns The handle for the new array element"""
	def addLast(self)->MDataHandle:
		"""addLast() -> MDataHandle

		Adds a new element to the end of the array.  The index of the element will be the current highest index + 1.

		Returns The handle for the new element"""
	def addLastArray(self)->MArrayDataHandle:
		"""addLastArray() -> MArrayDataHandle

		Adds a new element to the end of the array.  The added element is also an array.  The index of the element will the current highest index + 1.

		Returns The handle for the new array element"""
	def copy(self,source:MArrayDataBuilder)->Self:
		"""copy(source) -> self

		Copy data from source builder.

		* source (MArrayDataBuilder) - The source object to copy from"""
	def growArray(self,amount:int)->Self:
		"""growArray(amount) -> self

		Grows the array storage by the given amount.

		* amount (int) - the amount to grow the array by"""
	def removeElement(self,index:int)->Self:
		"""removeElement(index) -> self

		Removes the specified element from the array

		* index (int) - the element of the array to remove"""
	def setGrowSize(self,size:int)->Self:
		"""setGrowSize(size) -> self

		Sets the grow size of the array.  As elements are added to the array, the builder will allocate memory in chunks.  This method tells the builder how many elements to allocate each time it grows the array.

		* size (int) - the number of elements to allocate when growing the array"""
class MArrayDataHandle:
	"""Data block handle for array data."""
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def __len__(self)->int:
		"""Return len(self)."""
	def builder(self)->MArrayDataBuilder:
		"""builder() -> MArrayDataBuilder

		Returns a builder for this handle's array so that it can be expanded.

		This method will raise an exception if the current array does not support array data builders. This can be changed in a node's initialize routine using the usesArrayDataBuilder attribute in MFnAttribute.

		Do not use with an MArrayDataHandle which was returned by MPlug.asMDataHandle()."""
	def copy(self,source:MArrayDataHandle)->Self:
		"""copy(source) -> self

		Copy data from source array.

		* source (MArrayDataHandle) - The source object to copy from"""
	def elementLogicalIndex(self)->int:
		"""elementLogicalIndex() -> int

		Returns the index that we are currently at in the array.  It is possible for the index to be invalid, in which case the return status will report an error.  These may be sparse arrays so the element index returned will be a logical index.

		Raises an exception if there is no current element (e.g. if there are no elements)."""
	def inputArrayValue(self)->MArrayDataHandle:
		"""inputArrayValue() -> MArrayDataHandle

		Gets a handle into this data block for the current array element.  This method should be used when the array elements are also arrays.  The data represented by the handle will be valid.  If the data is from an dirty connection, then the connection will be evaluated.

		Do not use with an MArrayDataHandle which was returned by MPlug.asMDataHandle()."""
	def inputValue(self)->MDataHandle:
		"""inputValue() -> MDataHandle

		Gets a handle into this data block for the current array element.  The data represented by the handle will be valid.  If the data is from an dirty connection, then the connection will be evaluated.

		Do not use with an MArrayDataHandle which was returned by MPlug.asMDataHandle()."""
	def isDone(self)->bool:
		"""isDone() -> bool

		Specifies whether or not there are more elements to iterate over."""
	def jumpToPhysicalElement(self,position:int)->Self:
		"""jumpToPhysicalElement(position) -> self

		Jump to a specific physical element in the array.
		Since physical elements are contiguous no search is required.

		* position (int) - the array position to jump to"""
	def jumpToLogicalElement(self,index:int)->Self:
		"""jumpToLogicalElement(index) -> self

		Jump to a specific logical element in the array.
		Since the logical array is sparse its indices may not be consecutive and a binary search is used internally to find the element.
		Thus when iterating through the elements of the array it is much faster to do so using physical indices.

		* index (int) - the logical index to jump to"""
	def next(self)->bool:
		"""next() -> bool

		Advance to the next element in the array.
		Return True if there was a next element and False if there wasn't."""
	def outputArrayValue(self)->MArrayDataHandle:
		"""outputArrayValue() -> MArrayDataHandle

		Gets a handle into this data block for the current array element.  This method should be used when the array elements are also arrays. The array's elements are not evaluated and may no longer be valid. Therefore, this handle should only be used for writing over the data.

		Do not use with an MArrayDataHandle which was returned by MPlug.asMDataHandle()."""
	def outputValue(self)->MDataHandle:
		"""outputValue() -> MDataHandle

		Gets a handle into this data block for the current array element. The element is not evaluated so its data may not be valid. Therefore, this handle should only be used for writing over the data.

		This method can also be used to retrieve handles to individual elements of  non-datablock array handles, such as those returned by MPlug.getValue() and MPlug.asMDataHandle()."""
	def set(self,builder:MArrayDataBuilder)->Self:
		"""set(builder) -> self

		Sets the data for this array from the data in the builder object

		Do not use with an MArrayDataHandle which was returned by MPlug.asMDataHandle().

		* builder (MArrayDataBuilder) - the builder object"""
	def setAllClean(self)->Self:
		"""setAllClean() -> self

		Marks every element of the array attribute represented by the handle as clean.  This method should be used if a compute function is asked to compute a single element of a multi, but instead calculates all the elements.  Calling <i>setAllClean</i> in this situation will prevent further calls to the node's compute method for the other elements of the multi.

		Do not use with an MArrayDataHandle which was returned by MPlug.asMDataHandle()"""
	def setClean(self)->Self:
		"""setClean() -> self

		Marks the data that is represented by this handle as being clean.  This should be done after recalculating the data from the inputs.

		Do not use with an MArrayDataHandle which was returned by MPlug.asMDataHandle()."""
class MAttributeIndex:
	"""The index information for an attribute specification."""
	__hash__:None=None
	kInteger:int=0
	kFloat:int=1
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
	def copy(self,source:MAttributeIndex)->Self:
		"""copy(source) -> self

		Copy data from source index.

		* source (MAttributeIndex) - The source index to copy from"""
	def getLower(self)->int|float:
		"""getLower() -> int/float

		Returns the lower bound of the index."""
	def getUpper(self)->int|float:
		"""getUpper() -> int/float

		Returns the upper bound of the index."""
	def getValue(self)->int|float:
		"""getValue() -> int/float

		Returns the current value of the index.
		Raises an exception if the index is a range."""
	def hasLowerBound(self)->bool:
		"""hasLowerBound() -> bool

		Returns True if a lower bound is specified."""
	def hasRange(self)->bool:
		"""hasRange() -> bool

		Returns True if a range was specified."""
	def hasUpperBound(self)->bool:
		"""hasUpperBound() -> bool

		Returns True if an upper bound is specified."""
	def hasValidRange(self)->bool:
		"""hasValidRange() -> bool

		Returns True if upper bound is greater than lower bound."""
	def isBounded(self)->bool:
		"""isBounded() -> bool

		Returns True if the index is bounded."""
	def setLower(self,value:Any)->Self:
		"""setLower(value) -> self

		Sets the lower bound of the index."""
	def setType(self,type:int)->Self:
		"""setType(type) -> self

		Sets the type of attribute index.
		See type() for a list of valid index types.

		* type (int) - the index type to set"""
	def setUpper(self,value:Any)->Self:
		"""setUpper(value) -> self

		Sets the upper bound of the index."""
	def setValue(self,value:Any)->Self:
		"""setValue(value) -> self

		Sets the value of the index.

		Remark: calling this method with an integer value will change its type to kInteger, and subsequently calling with a float value will change it to kFloat."""
	def type(self)->int:
		"""type() -> int

		Returns the type of attribute index.

		Valid index types:
		  kInteger      Integer index (e.g. mesh.cp[5])
		  kFloat                Floating-poing index (e.g. curve.u[1.3])"""
class MAttributePattern:
	"""Manipulate attribute structure patterns."""
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def name(self,*args)->Any:
		"""Return the name of the attribute pattern."""
	def rootAttrCount(self,*args)->Any:
		"""Return the number of root attributes in this pattern."""
	def rootAttr(self,*args)->Any:
		"""Return the nth root attribute in this pattern."""
	def removeRootAttr(self,*args)->Any:
		"""Return the nth or passed-in root attribute from this pattern."""
	def addRootAttr(self,*args)->Any:
		"""Add the given root attribute to this pattern."""
	@staticmethod
	def attrPatternCount(*args)->Any:
		"""Return the global number of patterns created."""
	@staticmethod
	def attrPattern(*args)->Any:
		"""Return the specified pattern indexed from the global list."""
	@staticmethod
	def findPattern(*args)->Any:
		"""Return a pattern with the given name, None if not found."""
class MAttributeSpec:
	"""Class that encapsulates component/attribute information for generating selection items."""
	@property
	def name(self)->Any:
		"""The name of the attribute specification."""
	@name.setter
	def name(self,value:Any)->None:...
	@property
	def dimensions(self)->Any:
		"""The dimensions of the attribute specification."""
	@dimensions.setter
	def dimensions(self,value:Any)->None:...
	__hash__:None=None
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
	def __len__(self)->int:
		"""Return len(self)."""
	def __getitem__(self,index:int)->Any:
		"""Return self[key]."""
	def copy(self,source:MAttributeSpec)->Self:
		"""copy(source) -> self

		Copy data from source specification.

		* source (MAttributeSpec) - The source specification to copy from"""
class MAttributeSpecArray(collections.abc.Sequence[MAttributeSpec]):
	"""Array of MAttributeSpec values."""
	@property
	def sizeIncrement(self)->Any:
		"""Number of elements by which to grow the array when necessary."""
	@sizeIncrement.setter
	def sizeIncrement(self,value:Any)->None:...
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def __len__(self)->int:
		"""Return len(self)."""
	def __getitem__(self,index:int)->MAttributeSpec:
		"""Return self[key]."""
	def __setitem__(self,index:int,value:MAttributeSpec)->None:
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
class MBoundingBox:
	"""3D axis-aligned bounding box."""
	@property
	def min(self)->MPoint:
		"""Minimum corner point"""
	@property
	def max(self)->MPoint:
		"""Maximum corner point"""
	@property
	def center(self)->MPoint:
		"""Center point"""
	@property
	def width(self)->float:
		"""Size in X"""
	@property
	def height(self)->float:
		"""Size in Y"""
	@property
	def depth(self)->float:
		"""Size in Z"""
	@overload
	def __init__(self)->None:
		"""Default constructor. Returns a new, empty bounding box with, with both corners set to (0, 0, 0)."""
	@overload
	def __init__(self,src:MBoundingBox)->None:
		"""Copy constructor. Returns a new bounding box with the same corners as src"""
	@overload
	def __init__(self,min:MPoint,max:MPoint)->None:
		"""Returns a new bounding box whose minimum and maximum values are specified by min and max , respectively."""
	def clear(self)->Self:
		"""Empties bounding box, setting its corners to (0, 0, 0)."""
	def transformUsing(self,matrix:MMatrix)->Self:
		"""Multiplies bounding box's corners by matrix and returns the smallest bounding box which contains the results."""
	@overload
	def expand(self,point:MPoint)->Self:
		"""Expands bounding box to include point ."""
	@overload
	def expand(self,box:MBoundingBox)->Self:
		"""Expands bounding box to include all of box ."""
	def contains(self,point:MPoint)->bool:
		"""Returns True if point lies within bounding box."""
	def intersects(self,box:MBoundingBox,tolerance:float=0.0)->bool:
		"""Returns True if any part of box lies within a distance of tolerance of this bounding box."""
class MCacheSchema:
	"""Defines a node's cached data when participant in EM Cached Playback.
	Can be used to query or modify the attributes being cached.
	"""
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def add(self,attribute:MObject)->Self:
		"""add(attribute) -> self

		Force the attribute to be cached

		this method allows you to cache input attributes or other animatedattributes that are not fully understood by EM

		* attribute (MObject) - Attribute to cache"""
	def reset(self)->None:
		"""reset()

		Reset this schema to the minimal."""
class MCallbackIdArray(collections.abc.Sequence[int]):
	"""Array of MCallbackId values."""
	@property
	def sizeIncrement(self)->Any:
		"""Number of elements by which to grow the array when necessary."""
	@sizeIncrement.setter
	def sizeIncrement(self,value:Any)->None:...
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def __len__(self)->int:
		"""Return len(self)."""
	def __getitem__(self,index:int)->int:
		"""Return self[key]."""
	def __setitem__(self,index:int,value:int)->None:
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
class MCameraMessage(MMessage):
	"""Class used to register callbacks for Camera Manipulation Begin and End related messages."""
	@staticmethod
	def addBeginManipulationCallback(node:MObject,function:Callable,clientData:Any|None=None)->int:
		"""addBeginManipulationCallback(node, function, clientData=None) -> id

		Registers callbacks for camera manipulation beginning messages.

		 * node (MObject) - The node to register the callback for.
		 * function (MMessage::MNodeFunction) - the callback function
		 * clientData - User defined data passed to the callback function

		 * return: Identifier used for removing the callback."""
	@staticmethod
	def addEndManipulationCallback(node:MObject,function:Callable,clientData:Any|None=None)->int:
		"""addEndManipulationCallback(node, function, clientData=None) -> id

		Registers callbacks for camera manipulation ending messages.

		 * node (MObject) - The node to register the callback for.
		 * function (MMessage::MNodeFunction) - the callback function
		 * clientData - User defined data passed to the callback function

		 * return: Identifier used for removing the callback."""
class MColor(collections.abc.Sequence[float]):
	"""Manipulate color data."""
	@property
	def r(self)->float:
		"""red component"""
	@r.setter
	def r(self,value:float)->None:...
	@property
	def g(self)->float:
		"""green component"""
	@g.setter
	def g(self,value:float)->None:...
	@property
	def b(self)->float:
		"""blue component"""
	@b.setter
	def b(self,value:float)->None:...
	@property
	def a(self)->float:
		"""alpha component"""
	@a.setter
	def a(self,value:float)->None:...
	__hash__:None=None
	kRGB:int=0
	kHSV:int=1
	kCMY:int=2
	kCMYK:int=3
	kFloat:int=0
	kByte:int=1
	kShort:int=2
	kOpaqueBlack:MColor
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
	@overload
	def __init__(self)->None:
		"""Default constructor. Returns a new MColor with red, blue and green set to 0.0 and alpha set to 1.0."""
	@overload
	def __init__(self,src:MColor)->None:
		"""Copy constructor. Returns a new MColor with the same color components as src ."""
	@overload
	def __init__(self,components:Sequence[Literal[3]|float],model:int,dataType:int)->None:
		"""Returns a new MColor using the specified color components . The interpretation of the components depends upon the color model specified. For example, if model is kHSV then the values of components are interpreted as hue, saturation, value and alpha, respectively. The normal range of values for each component is determined by the specified component dataType , although values may exceed that range. If only 3 component values are provided then the fourth will be set to the maximum value of the range for dataType . The resulting color is converted to the kRGB model before being stored. If dataType was other than kFloat then the components will be converted to Float by dividing by the maximum value of dataType 's range. For example, if the red component was given as a value of 100 and dataType was kByte then the stored red value will be approximately 0.39215 (100 divided by 255)."""
	def __add__(self,other:MColor)->MColor:
		"""Returns a new MColor with the first MColor 's RGB values added to the second MColor 's RGB values. The first MColor 's alpha is passed through unchanged."""
	def __radd__(self,other:MColor)->MColor:
		"""Returns a new MColor with the first MColor 's RGB values added to the second MColor 's RGB values. The first MColor 's alpha is passed through unchanged."""
	@overload
	def __mul__(self,other:float)->MColor:
		"""Returns a new MColor with given MColor 's RGB values multiplied by the float. The given MColor 's alpha value is passed through unchanged."""
	@overload
	def __mul__(self,other:MColor)->MColor:
		"""Returns a new MColor with the first MColor 's RGB values multiplied by the second MColor 's RGB values. The first MColor 's alpha is passed through unchanged."""
	@overload
	def __rmul__(self,other:float)->MColor:
		"""Returns a new MColor with given MColor 's RGB values multiplied by the float. The given MColor 's alpha value is passed through unchanged."""
	@overload
	def __rmul__(self,other:MColor)->MColor:
		"""Returns a new MColor with the first MColor 's RGB values multiplied by the second MColor 's RGB values. The first MColor 's alpha is passed through unchanged."""
	def __iadd__(self,other:MColor)->Self:
		"""Adds the second MColor 's RGB values to the first MColor 's RGB values and returns a new reference to the first MColor . Alpha is unchanged."""
	@overload
	def __imul__(self,other:float)->Self:
		"""Multiplies the given MColor 's RGB values in-place by the float and returns a new reference to the given MColor . Alpha is unchanged."""
	@overload
	def __imul__(self,other:MColor)->Self:
		"""Multiplies the first MColor 's RGB values by the second MColor 's RGB values and returns a new reference to the first MColor . Alpha is unchanged."""
	def __truediv__(self,other:float)->MColor:
		"""Returns a new MColor with given MColor 's RGB values divided by the float. The given MColor 's alpha value is passed through unchanged."""
	def __rtruediv__(self,other)->Any:
		"""Return value/self."""
	def __itruediv__(self,other:float)->Self:
		"""Divides the given MColor 's RGB values in-place by the float and returns a new reference to the given MColor . Alpha is unchanged."""
	def __len__(self)->int:
		"""Return len(self)."""
	def __getitem__(self,index:int)->float:
		"""Return self[key]."""
	def __setitem__(self,index:int,value:float)->None:
		"""Set self[key] to value."""
	def __delitem__(self,index:int)->None:
		"""Delete self[key]."""
	def getColor(self,model:int=MColor.kRGB)->list[float]:
		"""Returns a list containing the color's components, in the specified color model ."""
	def setColor(self,components:Sequence[float],model:int=MColor.kRGB,dataType:int=MAttributeIndex.kFloat)->Self:
		"""Sets the color. The interpretation of the parameters is the same as for the MColor(components,model,dataType) constructor."""
class MColorArray(collections.abc.Sequence[MColor]):
	"""Array of MColor values."""
	@property
	def sizeIncrement(self)->Any:
		"""Number of elements by which to grow the array when necessary."""
	@sizeIncrement.setter
	def sizeIncrement(self,value:Any)->None:...
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def __len__(self)->int:
		"""Return len(self)."""
	def __getitem__(self,index:int)->MColor:
		"""Return self[key]."""
	def __setitem__(self,index:int,value:MColor)->None:
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
class MCommandMessage(MMessage):
	"""Class used to register callbacks for command related messages.

	The class also provides the following MessageType constants which
	describe the different types of output messages:
	  kHistory		#Command history
	  kDisplay		#String to display unmodified
	  kInfo		#General information
	  kWarning		#Warning message
	  kError		#Error message
	  kResult		#Result from a command execution in the command window
	  kStackTrace	#Stack trace"""
	kHistory:int=0
	kDisplay:int=1
	kInfo:int=2
	kWarning:int=3
	kError:int=4
	kResult:int=5
	kStackTrace:int=6
	kMELProc:int=0
	kMELCommand:int=1
	@staticmethod
	def addCommandCallback(function:Callable,clientData:Any|None=None)->int:
		"""addCommandCallback(function, clientData=None) -> id

		This method registers a callback for command messages that are
		issued every time a MEL command is executed. It is only called
		when actual commands are executed and not when scripts are
		executed.

		NOTE: Setting up a callback using this method will
		degrade the performance of Maya since the installed callback will be
		invoked repeatedly as MEL operations are processed.

		 * function - callable which will be passed a string containing the
		   MEL command being executed, and the clientData object
		 * clientData - User defined data passed to the callback function

		 * return: Identifier used for removing the callback."""
	@staticmethod
	def addProcCallback(function:Callable,clientData:Any|None=None)->int:
		"""addProcCallback(function, clientData=None) -> id

		This method registers a callback that is executed every time a MEL
		procedure is run. The callback will be executed once when the procedure
		is about to be executed, and again when it has exited. If a non-existent
		procedure is called the callback will be called once for entry but there
		will be no call on exit.

		The callback cannot be registered multiple times. To register a new
		callback function for this, please de-register the original callback first

		NOTE: Setting up a callback using this method can potentially degrade the
		performance of Maya since the installed callback will be invoked
		repeatedly as MEL procedures are executed.

		 * function - callable which will be passed a string containing the name
		   of the procedure being invoked, an integer indicating the ID for the
		   procedure's invocation, a bool set to True if the procedure is being entered,
		   false otherwise, a ProcType constant (see below for a list) indicating the
		   type of call this is (MEL proc or MEL command), and the clientData object
		   ProcType constant can take the folowing values:
		     kMELProc
		     kMELCommand
		 * clientData - User defined data passed to the callback function

		 * return: Identifier used for removing the callback."""
	@staticmethod
	def addCommandOutputCallback(function:Callable,clientData:Any|None=None)->int:
		"""addCommandOutputCallback(function, clientData=None) -> id

		This method registers a callback for whenever commands generate
		output such as that which is printed into the command window.

		 * function - callable which will be passed a string containing the
		   MEL command being executed, a MessageType constant (see class docs
		   for a list) indicating the message type and the clientData object
		 * clientData - User defined data passed to the callback function

		 * return: Identifier used for removing the callback."""
	@staticmethod
	def addCommandOutputFilterCallback(function:Callable,clientData:Any|None=None)->int:
		"""addCommandOutputFilterCallback(function, clientData=None) -> id

		This method registers a callback for whenever commands generate
		output such as that which is printed into the command window.

		Returning True in the callback will filter the output from the
		script editor and command line., returning False will keep the output.

		 * function - callable which will be passed a string containing the
		   MEL command being executed, a MessageType constant (see class docs
		   for a list) indicating the message type and the clientData object
		 * clientData - User defined data passed to the callback function

		 * return: Identifier used for removing the callback."""
class MConditionMessage(MMessage):
	"""Class used to register callbacks for condition related messages."""
	@staticmethod
	def addConditionCallback(conditionName:str,function:Callable,clientData:Any|None=None)->int:
		"""addConditionCallback(conditionName, function, clientData=None) -> id

		This method registers a callback for condition changed messages.
		The callback function will be passed the new state of the
		condition and any client data that the user wishes to pass in.

		 * conditionName (string) - the condition to register the
		callback for
		 * function - callable which will be passed a bool indicating
		   the new state of the condition, and the clientData object.
		 * clientData - User defined data passed to the callback function

		 * return: Identifier used for removing the callback."""
	@staticmethod
	def getConditionNames()->tuple[str,...]:
		"""getConditionNames() -> (string, string, ...)

		This method returns the list of available condition names.

		 * return: tuple of available condition names."""
	@staticmethod
	def getConditionState(name:str)->bool:
		"""getConditionState(name) -> bool

		This method returns the current state of a condition.

		 * name (string) - the name of the condition.


		 * return: The current state of the condition."""
class MContainerMessage(MMessage):
	"""Class used to register callbacks for container related messages."""
	@staticmethod
	def addPublishAttrCallback(function:Callable,clientData:Any|None=None)->int:
		"""addPublishAttrCallback(function, clientData=None) -> id

		This method registers a callback that is called whenever an attribute
		is published or unpublished from a container.

		 * function - callable which will be passed a Node (the container)
		   ,a string indicating the name of the published attr, and
		   the clientData object.
		 * clientData - User defined data passed to the callback function

		 * return: Identifier used for removing the callback."""
	@staticmethod
	def addBoundAttrCallback(function:Callable,clientData:Any|None=None)->int:
		"""addBoundAttrCallback(function, clientData=None) -> id

		This method registers a callback that is called whenever an attribute
		is bound or unbound on a container.

		 * function - callable which will be passed a Node (the container)
		   ,a string indicating the name of the bound attr, and
		   the clientData object.
		 * clientData - User defined data passed to the callback function

		 * return: Identifier used for removing the callback."""
class MDAGDrawOverrideInfo:
	"""A data structure to store the per path draw override information."""
	@property
	def overrideEnabled(self)->Any:
		"""Draw override enabled or not"""
	@overrideEnabled.setter
	def overrideEnabled(self,value:Any)->None:...
	@property
	def displayType(self)->Any:
		"""Display type (kDisplayTypeNormal, kDisplayTypeReference or kDisplayTypeTemplate)"""
	@displayType.setter
	def displayType(self,value:Any)->None:...
	@property
	def lod(self)->Any:
		"""Level of detail (kLODFull or kLODBoundingBox)"""
	@lod.setter
	def lod(self,value:Any)->None:...
	@property
	def enableShading(self)->Any:
		"""Whether allow to draw shaded item"""
	@enableShading.setter
	def enableShading(self,value:Any)->None:...
	@property
	def enableTexturing(self)->Any:
		"""Whether allow to draw textured item"""
	@enableTexturing.setter
	def enableTexturing(self,value:Any)->None:...
	@property
	def enableVisible(self)->Any:
		"""Whether the whole geometry is visible"""
	@enableVisible.setter
	def enableVisible(self,value:Any)->None:...
	@property
	def playbackVisible(self)->Any:
		"""Whether the object is visible during playback"""
	@playbackVisible.setter
	def playbackVisible(self,value:Any)->None:...
	kDisplayTypeNormal:int=0
	kDisplayTypeReference:int=1
	kDisplayTypeTemplate:int=2
	kLODFull:int=0
	kLODBoundingBox:int=1
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
class MDGContext:
	"""Dependency graph context."""
	kNormal:MDGContext
	kTimed:MDGContext
	kManaged:MDGContext
	@overload
	def __init__(self)->None:
		"""Default constructor. Returns a new MDGContext object using the default context."""
	@overload
	def __init__(self,src:MDGContext)->None:
		"""Copy constructor. Returns a new MDGContext object with the same value as src ."""
	@overload
	def __init__(self,time:MTime)->None:
		"""Returns a new MDGContext object which will evaluate at the given time ."""
	def copy(self,source:MDGContext)->Self:
		"""copy(source) -> self

		Copy data from source context.

		* source (MDGContext) - The source object to copy from"""
	def getTime(self)->MTime:
		"""Returns the time at which this context is set to evaluate. If the context does not have a specific time (i.e. it's a "normal" context) then a ValueError will be raised."""
	def isCurrent(self,*args)->Any:
		"""Returns True if the context is currently being used for evaluation. Returns False if some other context is being used for evaluation."""
	def isNormal(self)->bool:
		"""Returns True if the context is set to evaluate normally. Returns False if the context is set to evaluate at a specific time."""
	def isTimed(self,*args)->Any:
		"""Returns True if the context is used for evaluating at a time that is different than the current time."""
	def isManaged(self,*args)->Any:
		"""Returns True if the context is for cached playback background evaluation."""
	@staticmethod
	def current(*args)->Any:
		"""Returns the current context being used for evaluation."""
	def makeCurrent(self,*args)->Any:
		"""Makes this context the new current one being used for evaluation. Returns the previous evaluation context."""
class MDGMessage(MMessage):
	"""Class used to register callbacks for Dependency Graph related messages."""
	@staticmethod
	def addTimeChangeCallback(function:Callable,clientData:Any|None=None)->int:
		"""addTimeChangeCallback(function, clientData=None) -> id

		This method registers a callback that is called whenever the time
		changes in the dependency graph.

		 * function - callable which will be passed a MTime object indicating
		   the new time and the clientData object
		 * clientData - User defined data passed to the callback function

		 * return: Identifier used for removing the callback."""
	@staticmethod
	def addDelayedTimeChangeCallback(function:Callable,clientData:Any|None=None)->int:
		"""addDelayedTimeChangeCallback(function, clientData=None) -> id

		This method registers a callback that is called whenever the time
		changes in the dependency graph, but after the time changed callback.

		 * function - callable which will be passed a MTime object indicating
		   the new time and the clientData object
		 * clientData - User defined data passed to the callback function

		 * return: Identifier used for removing the callback."""
	@staticmethod
	def addDelayedTimeChangeRunupCallback(function:Callable,clientData:Any|None=None)->int:
		"""addDelayedTimeChangeRunupCallback(function, clientData=None) -> id

		This method registers a callback that is called whenever the time
		changes in the dependency graph, but after the other time changed callbacks
		which can be used to invoke a dynamics solve or runup if needed

		 * function - callable which will be passed a MTime object indicating
		   the new time and the clientData object
		 * clientData - User defined data passed to the callback function

		 * return: Identifier used for removing the callback."""
	@staticmethod
	def addForceUpdateCallback(function:Callable,clientData:Any|None=None)->int:
		"""addForceUpdateCallback(function, clientData=None) -> id

		This method registers a callback that is called after the time
		changes and after all nodes have been evaluated in the
		dependency graph.

		 * function - callable which will be passed a MTime object indicating
		   the new time and the clientData object
		 * clientData - User defined data passed to the callback function

		 * return: Identifier used for removing the callback."""
	@staticmethod
	def addNodeAddedCallback(function:Callable,nodeType:str,clientData:Any|None=None)->int:
		"""addNodeAddedCallback(function, nodeType, clientData=None) -> id

		This method registers a callback that is called whenever a new node
		is added to the dependency graph.
		The nodeType argument allows you to specify the type of nodes that
		will trigger the callback. The default node type is "dependNode" which
		matches all nodes.

		 * function - callable which will be passed a MObject indicating
		   the new node and the clientData object
		 * nodeType (MString) - type of node that will trigger the callback
		 * clientData - User defined data passed to the callback function

		 * return: Identifier used for removing the callback."""
	@staticmethod
	def addNodeRemovedCallback(function:Callable,nodeType:str,clientData:Any|None=None)->int:
		"""addNodeRemovedCallback(function, nodeType, clientData=None) -> id

		This method registers a callback that is called whenever a new node
		is removed from the dependency graph.
		The nodeType argument allows you to specify the type of nodes that
		will trigger the callback. The default node type is "dependNode" which
		matches all nodes.

		 * function - callable which will be passed a MObject indicating
		   the node being removed and the clientData object
		 * nodeType (MString) - type of node that will trigger the callback
		 * clientData - User defined data passed to the callback function

		 * return: Identifier used for removing the callback."""
	@staticmethod
	def addPreConnectionCallback(function:Callable,clientData:Any|None=None)->int:
		"""addPreConnectionCallback(function, clientData=None) -> id

		This method registers a callback that is called whenever any connection
		is made or broken in the dependency graph. This callback is triggered before
		the given connection has been made or broken, unlike the addConnectionCallback
		which is triggered after the operation.

		 * function - callable which will be passed a MPlug indicating the source
		   plug of the connection, a MPlug indicating the destination plug of the
		   connection, a boolean set to True if a new connection will be made,
		   False if it will be broken and the clientData object.
		 * clientData - User defined data passed to the callback function

		 * return: Identifier used for removing the callback."""
	@staticmethod
	def addConnectionCallback(function:Callable,clientData:Any|None=None)->int:
		"""addConnectionCallback(function, clientData=None) -> id

		This method registers a callback that is called whenever a connection
		is made or broken in the dependency graph. This callback is triggered
		after the given connection has been made or broken, unlike the addPreConnectionCallback
		which is triggered before the operation.

		 * function - callable which will be passed a MPlug indicating the source
		   plug of the connection, a MPlug indicating the destination plug of the
		   connection, a boolean set to True if a new connection will be made,
		   False if it will be broken and the clientData object.
		 * clientData - User defined data passed to the callback function

		 * return: Identifier used for removing the callback."""
	@staticmethod
	def addNodeChangeUuidCheckCallback(function:Callable,clientData:Any|None=None)->int:
		"""addNodeChangeUuidCheckCallback(function, clientData=None) -> id

		This method registers a callback that is called whenever a node
		may have its UUID changed. Possible causes include the 'rename' command,
		and the UUID for a node being read from a file during file I/O.

		Note that nodes are assigned a UUID when they are created; this does
		not invoke this callback. During file I/O the stored UUID is applied as
		a separate step after creation (which does invoke this callback).

		Depending on the situation Maya may or may not use the new UUID by default.
		For example, when importing a file, Maya reads the UUID from the file
		but does not use it. The boolean argument to the callback function lets
		the callback know whether Maya is intending to use the UUID or not.

		The callback returns a MMessage.Action constant:
		        * kDefaultAction - The callback does not want to change whether the
		          UUID is used or not.
		        * kDoNotDoAction - Do not use the new UUID.
		        * kDoAction - Use the new UUID.

		In any case, the callback may leave the new uuid as is, or may provide
		a new uuid of its own choosing to be used instead.

		 * function - callable which will be passed a boolean indicating whether
		   the UUID will be applied, a MObject indicating the node whose UUID may
		   be changed, the MUuid that may be applied to the node (typically the one
		   read from the file, during file I/O) - the callback may provide its own
		   uuid to be applied by changing this parameter - and the clientData object.
		 * clientData - User defined data passed to the callback function

		 * return: Identifier used for removing the callback."""
class MDGModifier:
	"""Used to change the structure of the dependency graph."""
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def addAttribute(self,node:MObject,attribute:MObject)->Self:
		"""addAttribute(MObject node, MObject attribute) -> self

		Adds an operation to the modifier to add a new dynamic attribute to the
		given dependency node. If the attribute is a compound its children will
		be added as well, so only the parent needs to be added using this method."""
	def addExtensionAttribute(self,nodeClass:MNodeClass,attribute:MObject)->Self:
		"""addExtensionAttribute(MNodeClass nodeClass, MObject attribute) -> self

		Adds an operation to the modifier to add a new extension attribute to
		the given node class. If the attribute is a compound its children will be
		added as well, so only the parent needs to be added using this method."""
	def commandToExecute(self,command:Any)->Self:
		"""commandToExecute(command) -> self

		Adds an operation to the modifier to execute a MEL command. The command
		should be fully undoable otherwise unexpected results may occur. If
		the command contains no undoable portions whatsoever, the call to
		doIt() may fail, but only after executing the command. It is best to
		use multiple commandToExecute() calls rather than batching multiple
		commands into a single call to commandToExecute(). They will still be
		undone together, as a single undo action by the user, but Maya will
		better be able to recover if one of the commands fails."""
	@overload
	def connect(self,source:MPlug,dest:MPlug)->Self:
		"""connect(MPlug source, MPlug dest) -> self
		connect(MObject sourceNode, MObject sourceAttr,
		        MObject destNode,   MObject destAttr) -> self

		Adds an operation to the modifier that connects two plugs in the
		dependency graph. It is the user's responsibility to ensure that the
		source and destination attributes are of compatible types. For instance,
		if the source attribute is a nurbs surface then the destination must
		also be a nurbs surface.
		Plugs can either be specified with node and attribute MObjects or with
		MPlugs."""
	@overload
	def connect(self,sourceNode:MObject,sourceAttr:MObject,destNode:MObject,destAttr:MObject)->Self:
		"""connect(MPlug source, MPlug dest) -> self
		connect(MObject sourceNode, MObject sourceAttr,
		        MObject destNode,   MObject destAttr) -> self

		Adds an operation to the modifier that connects two plugs in the
		dependency graph. It is the user's responsibility to ensure that the
		source and destination attributes are of compatible types. For instance,
		if the source attribute is a nurbs surface then the destination must
		also be a nurbs surface.
		Plugs can either be specified with node and attribute MObjects or with
		MPlugs."""
	@overload
	def createNode(self,typeName:str)->MObject:
		"""createNode(typeName) -> MObject
		createNode(MTypeId typeId) -> MObject

		Adds an operation to the modifier to create a node of the given type.
		The new node is created and returned but will not be added to the
		Dependency Graph until the modifier's doIt() method is called. Raises
		TypeError if the named node type does not exist or if it is a DAG node
		type."""
	@overload
	def createNode(self,typeId:MTypeId)->MObject:
		"""createNode(typeName) -> MObject
		createNode(MTypeId typeId) -> MObject

		Adds an operation to the modifier to create a node of the given type.
		The new node is created and returned but will not be added to the
		Dependency Graph until the modifier's doIt() method is called. Raises
		TypeError if the named node type does not exist or if it is a DAG node
		type."""
	@overload
	def deleteNode(self,node:MObject)->Self:
		"""deleteNode(MObject node) -> selfdeleteNode(MObject node, bool includeParents) -> self

		Adds an operation to the modifier which deletes the specified node from
		the Dependency Graph. If deleteNode() is called to delete nodes in a graph
		while other items are also in the queue, it might end up deleting the nodes
		before all the other tasks in the queue.

		In order to prevent unexpected outcomes, the modifier's doIt() should be called
		before the deleteNode operation is added so that the queue is emptied. Then,
		deleteNode() can be called and added to the queue. doIt() should be called
		immediately after to ensure that the queue is emptied before any other
		operations are added to it.

		The default behaviour when deleting a DAG node is to also include empty
		parents of the DAG node in the delete operation. If you do not want this
		behaviour set the includeParents argument to False."""
	@overload
	def deleteNode(self,node:MObject,includeParents:bool)->Self:
		"""deleteNode(MObject node) -> selfdeleteNode(MObject node, bool includeParents) -> self

		Adds an operation to the modifier which deletes the specified node from
		the Dependency Graph. If deleteNode() is called to delete nodes in a graph
		while other items are also in the queue, it might end up deleting the nodes
		before all the other tasks in the queue.

		In order to prevent unexpected outcomes, the modifier's doIt() should be called
		before the deleteNode operation is added so that the queue is emptied. Then,
		deleteNode() can be called and added to the queue. doIt() should be called
		immediately after to ensure that the queue is emptied before any other
		operations are added to it.

		The default behaviour when deleting a DAG node is to also include empty
		parents of the DAG node in the delete operation. If you do not want this
		behaviour set the includeParents argument to False."""
	@overload
	def disconnect(self,source:MPlug,dest:MPlug)->Self:
		"""disconnect(MPlug source, MPlug dest) -> self
		disconnect(MObject sourceNode, MObject sourceAttr,
		           MObject destNode,   MObject destAttr) -> self

		Adds an operation to the modifier that breaks a connection between two
		plugs in the dependency graph.
		Plugs can either be specified with node and attribute MObjects or with
		MPlugs."""
	@overload
	def disconnect(self,sourceNode:MObject,sourceAttr:MObject,destNode:MObject,destAttr:MObject)->Self:
		"""disconnect(MPlug source, MPlug dest) -> self
		disconnect(MObject sourceNode, MObject sourceAttr,
		           MObject destNode,   MObject destAttr) -> self

		Adds an operation to the modifier that breaks a connection between two
		plugs in the dependency graph.
		Plugs can either be specified with node and attribute MObjects or with
		MPlugs."""
	def doIt(self)->Self:
		"""doIt() -> self

		Executes the modifier's operations. If doIt() is called multiple times
		in a row, without any intervening calls to undoIt(), then only the
		operations which were added since the previous doIt() call will be
		executed. If undoIt() has been called then the next call to doIt() will
		do all operations."""
	def linkExtensionAttributeToPlugin(self,plugin:MObject,attribute:MObject)->Self:
		"""linkExtensionAttributeToPlugin(MObject plugin, MObject attribute) -> self

		The plugin can call this method to indicate that the extension attribute
		defines part of the plugin, regardless of the node type to which it
		attaches itself. This requirement is used when the plugin is checked to
		see if it is in use or if is able to be unloaded or if it is required as
		part of a stored file. For compound attributes only the topmost parent
		attribute may be passed in and all of its children will be included,
		recursively. Thus it's not possible to link a child attribute to a
		plugin by itself. Note that the link is established immediately and is
		not affected by the modifier's doIt() or undoIt() methods."""
	def newPlugValue(self,plug:MPlug,value:MObject)->Self:
		"""newPlugValue(MPlug plug, MObject value) -> self

		Adds an operation to the modifier to set the value of a plug, where
		value is an MObject data wrapper, such as created by the various
		MFn*Data classes."""
	def newPlugValueBool(self,plug:MPlug,value:bool)->Self:
		"""newPlugValueBool(MPlug plug, bool value) -> self

		Adds an operation to the modifier to set a value onto a bool plug."""
	def newPlugValueChar(self,plug:MPlug,value:int)->Self:
		"""newPlugValueChar(MPlug plug, int value) -> self

		Adds an operation to the modifier to set a value onto a char (single
		byte signed integer) plug."""
	def newPlugValueDouble(self,plug:MPlug,value:float)->Self:
		"""newPlugValueDouble(MPlug plug, float value) -> self

		Adds an operation to the modifier to set a value onto a double-precision
		float plug."""
	def newPlugValueFloat(self,plug:MPlug,value:float)->Self:
		"""newPlugValueFloat(MPlug plug, float value) -> self

		Adds an operation to the modifier to set a value onto a single-precision
		float plug."""
	def newPlugValueInt(self,plug:MPlug,value:int)->Self:
		"""newPlugValueInt(MPlug plug, int value) -> self

		Adds an operation to the modifier to set a value onto an int plug."""
	def newPlugValueMAngle(self,plug:MPlug,value:MAngle)->Self:
		"""newPlugValueMAngle(MPlug plug, MAngle value) -> self

		Adds an operation to the modifier to set a value onto an angle plug."""
	def newPlugValueMDistance(self,plug:MPlug,value:MDistance)->Self:
		"""newPlugValueMDistance(MPlug plug, MDistance value) -> self

		Adds an operation to the modifier to set a value onto a distance plug."""
	def newPlugValueMTime(self,plug:MPlug,value:MTime)->Self:
		"""newPlugValueMTime(MPlug plug, MTime value) -> self

		Adds an operation to the modifier to set a value onto a time plug."""
	def newPlugValueShort(self,plug:MPlug,value:int)->Self:
		"""newPlugValueShort(MPlug plug, int value) -> self

		Adds an operation to the modifier to set a value onto a short
		integer plug."""
	def newPlugValueString(self,plug:MPlug,value:str)->Self:
		"""newPlugValueString(MPlug plug, string value) -> self

		Adds an operation to the modifier to set a value onto a string plug."""
	@overload
	def pythonCommandToExecute(self,callable:Any)->Self:
		"""pythonCommandToExecute(callable) -> selfpythonCommandToExecute(commandString) -> self

		Adds an operation to the modifier to execute a Python command, which
		can be passed as either a Python callable or a string containing the
		text of the Python code to be executed. The command should be fully
		undoable otherwise unexpected results may occur. If the command
		contains no undoable portions whatsoever, the call to doIt() may fail,
		but only after executing the command. It is best to use multiple calls
		rather than batching multiple commands into a single call to
		pythonCommandToExecute(). They will still be undone together, as a
		single undo action by the user, but Maya will better be able to
		recover if one of the commands fails."""
	@overload
	def pythonCommandToExecute(self,commandString:Any)->Self:
		"""pythonCommandToExecute(callable) -> selfpythonCommandToExecute(commandString) -> self

		Adds an operation to the modifier to execute a Python command, which
		can be passed as either a Python callable or a string containing the
		text of the Python code to be executed. The command should be fully
		undoable otherwise unexpected results may occur. If the command
		contains no undoable portions whatsoever, the call to doIt() may fail,
		but only after executing the command. It is best to use multiple calls
		rather than batching multiple commands into a single call to
		pythonCommandToExecute(). They will still be undone together, as a
		single undo action by the user, but Maya will better be able to
		recover if one of the commands fails."""
	def removeAttribute(self,node:MObject,attribute:MObject)->Self:
		"""removeAttribute(MObject node, MObject attribute) -> self

		Adds an operation to the modifier to remove a dynamic attribute from the
		given dependency node. If the attribute is a compound its children will
		be removed as well, so only the parent needs to be removed using this
		method. The attribute MObject passed in will be set to kNullObj. There
		should be no function sets attached to the attribute at the time of the
		call as their behaviour may become unpredictable."""
	def removeExtensionAttribute(self,nodeClass:MNodeClass,attribute:MObject)->Self:
		"""removeExtensionAttribute(MNodeClass nodeClass, MObject attribute) -> self

		Adds an operation to the modifier to remove an extension attribute from
		the given node class. If the attribute is a compound its children will
		be removed as well, so only the parent needs to be removed using this
		method. The attribute MObject passed in will be set to kNullObj. There
		should be no function sets attached to the attribute at the time of the
		call as their behaviour may become unpredictable."""
	def removeExtensionAttributeIfUnset(self,nodeClass:MNodeClass,attribute:MObject)->Self:
		"""removeExtensionAttributeIfUnset(MNodeClass nodeClass,
		                                MObject attribute) -> self

		Adds an operation to the modifier to remove an extension attribute from
		the given node class, but only if there are no nodes in the graph with
		non-default values for this attribute. If the attribute is a compound
		its children will be removed as well, so only the parent needs to be
		removed using this method. The attribute MObject passed in will be set
		to kNullObj. There should be no function sets attached to the attribute
		at the time of the call as their behaviour may become unpredictable."""
	def removeMultiInstance(self,plug:MPlug,breakConnections:bool)->Self:
		"""removeMultiInstance(MPlug plug, bool breakConnections) -> self

		Adds an operation to the modifier to remove an element of a multi (array) plug."""
	def renameAttribute(self,node:MObject,attribute:MObject,newShortName:str,newShortName2:str)->Self:
		"""renameAttribute(MObject node, MObject attribute,
		string newShortName, string newShortName) -> self

		Adds an operation to the modifer that renames a dynamic attribute on the given dependency node."""
	def renameNode(self,node:MObject,newName:str)->Self:
		"""renameNode(MObject node, string newName) -> self

		Adds an operation to the modifer to rename a node."""
	def setNodeLockState(self,node:MObject,newState:bool)->Self:
		"""setNodeLockState(MObject node, bool newState) -> self

		Adds an operation to the modifier to set the lockState of a node."""
	def undoIt(self)->Self:
		"""undoIt() -> self

		Undoes all of the operations that have been given to this modifier. It
		is only valid to call this method after the doIt() method has been
		called."""
	def unlinkExtensionAttributeFromPlugin(self,plugin:MObject,attribute:MObject)->Self:
		"""unlinkExtensionAttributeFromPlugin(MObject plugin,
		                                   MObject attribute) -> self

		The plugin can call this method to indicate that it no longer requires
		an extension attribute for its operation. This requirement is used when
		the plugin is checked to see if it is in use or if is able to be unloaded
		or if it is required as part of a stored file. For compound attributes
		only the topmost parent attribute may be passed in and all of its
		children will be unlinked, recursively. Thus it's not possible to unlink
		a child attribute from a plugin by itself. Note that the link is broken
		immediately and is not affected by the modifier's doIt() or undoIt()
		methods."""
class MDagMessage(MMessage):
	"""Class used to register callbacks for Dag related messages.

	The class also provides the following DagMessage constants which describe the different types of DAG operations:
	  kParentAdded
	  kParentRemoved
	  kChildAdded
	  kChildRemoved
	  kChildReordered
	  kInstanceAdded
	  kInstanceRemoved
	  kInvalidMsg
	"""
	kInvalidMsg:int=-1
	kParentAdded:int=0
	kParentRemoved:int=1
	kChildAdded:int=2
	kChildRemoved:int=3
	kChildReordered:int=4
	kInstanceAdded:int=5
	kInstanceRemoved:int=6
	kLast:int=7
	kScaleX:int=1
	kScaleY:int=2
	kScaleZ:int=4
	kShearXY:int=8
	kShearXZ:int=16
	kShearYZ:int=32
	kRotateX:int=64
	kRotateY:int=128
	kRotateZ:int=256
	kTranslateX:int=512
	kTranslateY:int=1024
	kTranslateZ:int=2048
	kScalePivotX:int=4096
	kScalePivotY:int=8192
	kScalePivotZ:int=16384
	kRotatePivotX:int=32768
	kRotatePivotY:int=65536
	kRotatePivotZ:int=131072
	kScaleTransX:int=262144
	kScaleTransY:int=524288
	kScaleTransZ:int=1048576
	kRotateTransX:int=2097152
	kRotateTransY:int=4194304
	kRotateTransZ:int=8388608
	kRotateOrientX:int=16777216
	kRotateOrientY:int=33554432
	kRotateOrientZ:int=67108864
	kRotateOrder:int=134217728
	kAll:int=268435455
	kScale:int=7
	kShear:int=56
	kRotation:int=448
	kTranslation:int=3584
	kScalePivot:int=28672
	kRotatePivot:int=229376
	kScalePivotTrans:int=1835008
	kRotatePivotTrans:int=14680064
	kRotateOrient:int=117440512
	@staticmethod
	def addParentAddedCallback(function:Callable,clientData:Any|None=None)->int:
		"""addParentAddedCallback(function, clientData=None) -> id

		This method registers a callback that is called whenever a parent is
		added in the DAG.

		 * function - callable which will be passed a MDagPath to the parent,
		   a MDagPath to the child, and the clientData object
		 * clientData - User defined data passed to the callback function

		 * return: Identifier used for removing the callback."""
	@staticmethod
	def addParentAddedDagPathCallback(node:MDagPath,function:Callable,clientData:Any|None=None)->int:
		"""addParentAddedDagPathCallback(node, function, clientData=None) -> id

		This method registers a callback that is called whenever a parent is
		added to the specified DAG node.

		 * node (MDagPath) - the DAG node to register the callback for
		 * function - callable which will be passed a MDagPath to the parent,
		   a MDagPath to the child, and the clientData object
		 * clientData - User defined data passed to the callback function

		 * return: Identifier used for removing the callback."""
	@staticmethod
	def addParentRemovedCallback(function:Callable,clientData:Any|None=None)->int:
		"""addParentRemovedCallback(function, clientData=None) -> id

		This method registers a callback that is called whenever a parent is
		removed in the DAG.

		 * function - callable which will be passed a MDagPath to the parent,
		   a MDagPath to the child, and the clientData object
		 * clientData - User defined data passed to the callback function

		 * return: Identifier used for removing the callback."""
	@staticmethod
	def addParentRemovedDagPathCallback(node:MDagPath,function:Callable,clientData:Any|None=None)->int:
		"""addParentRemovedDagPathCallback(node, function, clientData=None) -> id

		This method registers a callback that is called whenever a parent is
		removed from the specified DAG node.

		 * node (MDagPath) - the DAG node to register the callback for
		 * function - callable which will be passed a MDagPath to the parent,
		   a MDagPath to the child, and the clientData object
		 * clientData - User defined data passed to the callback function

		 * return: Identifier used for removing the callback."""
	@staticmethod
	def addChildAddedCallback(function:Callable,clientData:Any|None=None)->int:
		"""addChildAddedCallback(function, clientData=None) -> id

		This method registers a callback that is called whenever a child is
		added in the DAG.

		 * function - callable which will be passed a MDagPath to the parent,
		   a MDagPath to the child, and the clientData object
		 * clientData - User defined data passed to the callback function

		 * return: Identifier used for removing the callback."""
	@staticmethod
	def addChildAddedDagPathCallback(node:MDagPath,function:Callable,clientData:Any|None=None)->int:
		"""addChildAddedDagPathCallback(node, function, clientData=None) -> id

		This method registers a callback that is called whenever a child is
		added to the specified DAG node.

		 * node (MDagPath) - the DAG node to register the callback for
		 * function - callable which will be passed a MDagPath to the parent,
		   a MDagPath to the child, and the clientData object
		 * clientData - User defined data passed to the callback function

		 * return: Identifier used for removing the callback."""
	@staticmethod
	def addChildRemovedCallback(function:Callable,clientData:Any|None=None)->int:
		"""addChildRemovedCallback(function, clientData=None) -> id

		This method registers a callback that is called whenever a child is
		removed in the DAG.

		 * function - callable which will be passed a MDagPath to the parent,
		   a MDagPath to the child, and the clientData object
		 * clientData - User defined data passed to the callback function

		 * return: Identifier used for removing the callback."""
	@staticmethod
	def addChildRemovedDagPathCallback(node:MDagPath,function:Callable,clientData:Any|None=None)->int:
		"""addChildRemovedDagPathCallback(node, function, clientData=None) -> id

		This method registers a callback that is called whenever a child is
		removed from the specified DAG node.

		 * node (MDagPath) - the DAG node to register the callback for
		 * function - callable which will be passed a MDagPath to the parent,
		   a MDagPath to the child, and the clientData object
		 * clientData - User defined data passed to the callback function

		 * return: Identifier used for removing the callback."""
	@staticmethod
	def addChildReorderedCallback(function:Callable,clientData:Any|None=None)->int:
		"""addChildReorderedCallback(function, clientData=None) -> id

		This method registers a callback that is called whenever a child is
		reordered in the DAG.

		 * function - callable which will be passed a MDagPath to the parent,
		   a MDagPath to the child, and the clientData object
		 * clientData - User defined data passed to the callback function

		 * return: Identifier used for removing the callback."""
	@staticmethod
	def addChildReorderedDagPathCallback(node:MDagPath,function:Callable,clientData:Any|None=None)->int:
		"""addChildReorderedDagPathCallback(node, function, clientData=None) -> id

		This method registers a callback that is called whenever a child of
		the specified DAG node is reordered

		 * node (MDagPath) - the DAG node to register the callback for
		 * function - callable which will be passed a MDagPath to the parent,
		   a MDagPath to the child, and the clientData object
		 * clientData - User defined data passed to the callback function

		 * return: Identifier used for removing the callback."""
	@staticmethod
	def addDagCallback(msgType:int,function:Callable,clientData:Any|None=None)->int:
		"""addDagCallback(msgType, function, clientData=None) -> id

		This method registers a callback that is called for specified
		DAG changes on all nodes. The callback will also receive the
		DagMessage

		 * msgType (DagMessage) - The type of DAG change to trigger the callback
		 * function - callable which will be passed a DagMessage constant
		   indicating the operation which triggered the callback (see class
		          docs for a list), a MDagPath to the parent, a MDagPath to the child
		   ,and the clientData object
		 * clientData - User defined data passed to the callback function

		 * return: Identifier used for removing the callback."""
	@staticmethod
	def addDagDagPathCallback(node:MDagPath,msgType:int,function:Callable,clientData:Any|None=None)->int:
		"""addDagDagPathCallback(node, msgType, function, clientData=None) -> id

		This method registers a callback that is called for specified a DAG
		change is made to the specified DAG path. The callback receives the
		DagMessage as well.

		 * node (MDagPath) - the DAG node to register the callback for
		 * msgType (DagMessage) - The type of DAG change to trigger the callback
		  (see class docs for a list)
		 * function - callable which will be passed a DagMessage constant
		   indicating the operation which triggered the callback, a MDagPath
		   to the parent, a MDagPath to the child
		   ,and the clientData object
		 * clientData - User defined data passed to the callback function

		 * return: Identifier used for removing the callback."""
	@staticmethod
	def addAllDagChangesCallback(function:Callable,clientData:Any|None=None)->int:
		"""addAllDagChangesCallback(function, clientData=None) -> id

		This method registers a callback that is called whenever any
		DAG change is made to any DAG node.

		 * function - callable which will be passed a DagMessage constant
		   indicating the operation which triggered the callback (see class
		          docs for a list), a MDagPath to the parent, a MDagPath to the child
		   ,and the clientData object
		 * clientData - User defined data passed to the callback function

		 * return: Identifier used for removing the callback."""
	@staticmethod
	def addAllDagChangesDagPathCallback(node:MDagPath,function:Callable,clientData:Any|None=None)->int:
		"""addAllDagChangesDagPathCallback(node, function, clientData=None) -> id

		This method registers a callback that is called whenever a DAG
		change is made to the specified DAG path.

		 * node (MDagPath) - the DAG node to register the callback for
		 * function - callable which will be passed a DagMessage constant
		   indicating the operation which triggered the callback (see class
		          docs for a list), a MDagPath to the parent, a MDagPath to the child
		   ,and the clientData object
		 * clientData - User defined data passed to the callback function

		 * return: Identifier used for removing the callback."""
	@staticmethod
	def addInstanceAddedCallback(function:Callable,clientData:Any|None=None)->int:
		"""addInstanceAddedCallback(function, clientData=None) -> id

		This method registers a callback that is called whenever any node in the DAG
		is instanced.

		 * function - callable which will be passed a MDagPath to the parent,
		   a MDagPath to the child, and the clientData object
		 * clientData - User defined data passed to the callback function

		 * return: Identifier used for removing the callback."""
	@staticmethod
	def addInstanceAddedDagPathCallback(node:MDagPath,function:Callable,clientData:Any|None=None)->int:
		"""addInstanceAddedDagPathCallback(node, function, clientData=None) -> id

		This method registers a callback that is called whenever the specified node
		is instanced

		 * node (MDagPath) - the DAG node to register the callback for
		 * function - callable which will be passed a MDagPath to the parent,
		   a MDagPath to the child, and the clientData object
		 * clientData - User defined data passed to the callback function

		 * return: Identifier used for removing the callback."""
	@staticmethod
	def addInstanceRemovedCallback(function:Callable,clientData:Any|None=None)->int:
		"""addInstanceRemovedCallback(function, clientData=None) -> id

		This method registers a callback that is called whenever an instance of any DAG
		node is removed or deleted.

		 * function - callable which will be passed a MDagPath to the parent,
		   a MDagPath to the child, and the clientData object
		 * clientData - User defined data passed to the callback function

		 * return: Identifier used for removing the callback."""
	@staticmethod
	def addInstanceRemovedDagPathCallback(node:MDagPath,function:Callable,clientData:Any|None=None)->int:
		"""addInstanceRemovedDagPathCallback(node, function, clientData=None) -> id

		This method registers a callback that is called whenever an instance of the specified
		node is removed.

		 * node (MDagPath) - the DAG node to register the callback for
		 * function - callable which will be passed a MDagPath to the parent,
		   a MDagPath to the child, and the clientData object
		 * clientData - User defined data passed to the callback function

		 * return: Identifier used for removing the callback."""
	@staticmethod
	def addWorldMatrixModifiedCallback(node:Any,function:Callable,clientData:Any|None=None)->int:
		"""addWorldMatrixModifiedCallback(node, function, clientData=None) -> id

		This method registers a callback that is called when a parent matrix of the
		specified DAG node changes.

		Since a node's worldMatrix is affected by the transforms of its ancestors in
		the DAG, it's possible for there to be two different nodes involved: the
		"trigger" node, whose transform has changed, and the "affected" node, whose
		worldMatrix is affected by the change to the trigger.

		The callback is placed on the affected node, but it is the trigger node which
		is passed to the callback.

		If the trigger node's transformation is already dirty (i.e. it has not been
		evaluated since it was last changed) then the callback will not be triggered.
		So if the trigger node's transformation is modified multiple times between
		evaluations, only the first one will result in the callback being called.

		 * affectedNode (MDagPath) - the DAG node to register the callback for
		 * function - callable which will be passed a MObject indicating the node
		   whose transformation has changed, a MatrixModifiedFlags constant showing
		   what has changed (see below for complete list) and the clientData object
		 * clientData - User defined data passed to the callback function

		Available MatrixModifiedFlags constants:
		Individual flags:
		  kScaleX               kScaleY                 kScaleZ
		  kShearXY              kShearXZ                kShearYZ
		  kRotateX              kRotateY                kRotateZ
		  kTranslateX   kTranslateY             kTranslateZ
		  kScalePivotX  kScalePivotY    kScalePivotZ
		  kRotatePivotX kRotatePivotY   kRotatePivotZ
		  kScaleTransX  kScaleTransY    kScaleTransZ
		  kRotateTransX kRotateTransY   kRotateTransZ
		  kRotateOrientX        kRotateOrientY  kRotateOrientZ
		  kRotateOrder
		Composite flags
		  kAll
		  kScale                = kScaleX        | kScaleY        | kScaleZ
		  kShear                = kShearXY       | kShearXZ       | kShearYZ
		  kRotation             = kRotateX       | kRotateY       | kRotateZ
		  kTranslation          = kTranslateX    | kTranslateY    | kTranslateZ
		  kScalePivot           = kScalePivotX   | kScalePivotY   | kScalePivotZ
		  kRotatePivot          = kRotatePivotX  | kRotatePivotY  | kRotatePivotZ
		  kScalePivotTrans      = kScaleTransX   | kScaleTransY   | kScaleTransZ
		  kRotatePivotTrans     = kRotateTransX  | kRotateTransY  | kRotateTransZ
		  kRotateOrient         = kRotateOrientX | kRotateOrientY | kRotateOrientZ

		 * return: Identifier used for removing the callback."""
	@staticmethod
	def addMatrixModifiedCallback(node:Any,function:Callable,clientData:Any|None=None)->int:
		"""addMatrixModifiedCallback(node, function, clientData=None) -> id

		This method registers a callback that is called when the local matrix
		on the specified DAG node changes.

		If the node's transformation is already dirty (i.e. it has not been
		evaluated since it was last changed) then the callback will not be triggered.
		So if the node's transformation is modified multiple times between
		evaluations, only the first one will result in the callback being called.

		 * affectedNode (MDagPath) - the DAG node to register the callback for
		 * function - callable which will be passed a MObject indicating the node
		   whose transformation has changed, a MatrixModifiedFlags constant showing
		   what has changed (see below for complete list) and the clientData object
		 * clientData - User defined data passed to the callback function

		Available MatrixModifiedFlags constants:
		Individual flags:
		  kScaleX               kScaleY                 kScaleZ
		  kShearXY              kShearXZ                kShearYZ
		  kRotateX              kRotateY                kRotateZ
		  kTranslateX   kTranslateY             kTranslateZ
		  kScalePivotX  kScalePivotY    kScalePivotZ
		  kRotatePivotX kRotatePivotY   kRotatePivotZ
		  kScaleTransX  kScaleTransY    kScaleTransZ
		  kRotateTransX kRotateTransY   kRotateTransZ
		  kRotateOrientX        kRotateOrientY  kRotateOrientZ
		  kRotateOrder
		Composite flags
		  kAll
		  kScale                = kScaleX        | kScaleY        | kScaleZ
		  kShear                = kShearXY       | kShearXZ       | kShearYZ
		  kRotation             = kRotateX       | kRotateY       | kRotateZ
		  kTranslation          = kTranslateX    | kTranslateY    | kTranslateZ
		  kScalePivot           = kScalePivotX   | kScalePivotY   | kScalePivotZ
		  kRotatePivot          = kRotatePivotX  | kRotatePivotY  | kRotatePivotZ
		  kScalePivotTrans      = kScaleTransX   | kScaleTransY   | kScaleTransZ
		  kRotatePivotTrans     = kRotateTransX  | kRotateTransY  | kRotateTransZ
		  kRotateOrient         = kRotateOrientX | kRotateOrientY | kRotateOrientZ

		 * return: Identifier used for removing the callback."""
class MDagModifier(MDGModifier):
	"""Used to change the structure of the DAG"""
	def __init__(self)->None:
		"""Default constructor. Returns a new, empty MDagModifier object."""
	@overload
	def createNode(self,typeName:str,parent:MObject=MObject.kNullObj)->MObject:
		"""Adds an operation to the modifier to create a DAG node of the specified type. If a parent DAG node is provided the new node will be parented under it. If no parent is provided and the new DAG node is a transform type then it will be parented under the world. In both of these cases the method returns the new DAG node<br> If no parent is provided and the new DAG node is not a transform type then a transform node will be created and the child parented under that. The new transform will be parented under the world and it is the transform node which will be returned by the method, not the child. None of the newly created nodes will be added to the DAG until the modifier's doIt() method is called. Raises TypeError if the node type does not exist or if the parent is not a transform type."""
	@overload
	def createNode(self,typeName:MTypeId,parent:MObject=MObject.kNullObj)->MObject:
		"""Adds an operation to the modifier to create a DAG node of the specified type. If a parent DAG node is provided the new node will be parented under it. If no parent is provided and the new DAG node is a transform type then it will be parented under the world. In both of these cases the method returns the new DAG node. If no parent is provided and the new DAG node is not a transform type then a transform node will be created and the child parented under that. The new transform will be parented under the world and it is the transform node which will be returned by the method, not the child. None of the newly created nodes will be added to the DAG until the modifier's doIt() method is called. Raises TypeError if the node type does not exist or if the parent is not a transform type<span>."""
	def reparentNode(self,node:MObject,newParent:MObject=MObject.kNullObj)->Self:
		"""Adds an operation to the modifier to reparent a DAG node under a specified parent. Raises TypeError if the node is not a DAG node or the parent is not a transform type. If no parent is provided then the DAG node will be reparented under the world, so long as it is a transform type. If it is not a transform type then the doIt() will raise a RuntimeError."""
class MDagPath:
	"""Path to a DAG node from the top of the DAG."""
	__hash__:None=None
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
	@overload
	def __init__(self)->None:
		"""Default constructor. Returns a new, empty MDagPath object."""
	@overload
	def __init__(self,src:MDagPath)->None:
		"""Copy constructor. Returns a new MDagPath object with the same value as src ."""
	@staticmethod
	def getAllPathsTo(node:MObject)->MDagPathArray:
		"""Returns all paths to the given node ."""
	@staticmethod
	def getAPathTo(node:MObject)->MDagPath:
		"""Returns the first path found to the given node ."""
	@staticmethod
	def matchTransform(*args)->Any:
		"""Returns the transformationMatrix which, when applied to the source object, will bring the source object to the location of the target object."""
	@staticmethod
	def matchLocalMatrix(*args)->Any:
		"""Returns the transformationMatrix which, when applied to the source object, will have the source object match the local matrix."""
	def apiType(self)->int:
		"""Returns the type of the object at the end of the path."""
	def child(self,childNum:int)->MObject:
		"""The childNum 'th object parented directly beneath the object at the end of the path."""
	def childCount(self)->int:
		"""Returns the number of objects parented directly beneath the object at the end of the path."""
	def exclusiveMatrix(self)->MMatrix:
		"""Returns the matrix for all transforms in the path, excluding the end object."""
	def exclusiveMatrixInverse(self)->MMatrix:
		"""Returns the inverse of exclusiveMatrix() ."""
	def extendToShape(self,shapeNum:int=0)->Self:
		"""Extends the path to the shapeNum 'th shape node parented directly beneath the transform at the current end of the path."""
	def fullPathName(self)->str:
		"""Returns a string representation of the path from the DAG root to the path's last node."""
	def getDisplayStatus(self,*args)->Any:
		"""Returns the display status for this path."""
	def getDrawOverrideInfo(self,*args)->Any:
		"""Returns the draw override information for this path."""
	def getPath(self,pathNum:int=0)->MDagPath:
		"""The pathNum 'th sub-path of this path."""
	def hasFn(self,type:int)->bool:
		"""Returns True if the object at the end of the path supports the function set represented by type ."""
	def inclusiveMatrix(self)->MMatrix:
		"""Returns the matrix for all transforms in the path, including the end object, if it is a transform."""
	def inclusiveMatrixInverse(self)->MMatrix:
		"""Returns the inverse of inclusiveMatrix() ."""
	def instanceNumber(self)->int:
		"""Returns the instance number of this path to the object at the end."""
	def isInstanced(self)->bool:
		"""Returns True if the object at the end of the path can be reached by more than one path."""
	def isTemplated(self,*args)->Any:
		"""Returns true if the DAG Node at the end of the path is templated."""
	def isValid(self)->bool:
		"""True if this is a valid path."""
	def isVisible(self,*args)->Any:
		"""Returns true if the DAG Node at the end of the path is visible."""
	def length(self)->int:
		"""Returns the number of nodes on the path, not including the DAG's root node."""
	def node(self)->MObject:
		"""Returns the DAG node at the end of the path."""
	def numberOfShapesDirectlyBelow(self)->int:
		"""Returns the number of shape nodes parented directly beneath the transform at the end of the path. If the path does not end at a transform, or if the transform has no shape nodes directly beneath it, 0 will be returned."""
	def partialPathName(self)->str:
		"""Returns the minimum string representation which will uniquely identify the path."""
	def pathCount(self)->int:
		"""Returns the number of sub-paths which make up this path."""
	def pop(self,num:int=1)->Self:
		"""Removes num objects from the end of the path."""
	def push(self,child:MObject)->Self:
		"""Extends the path to the specified child object, which must be parented directly beneath the object currently at the end of the path."""
	def set(self,path:MDagPath)->Self:
		"""Replaces the current path held by this object with that of path ."""
	def transform(self)->MObject:
		"""Returns the last transform node on the path."""
class MDagPathArray(collections.abc.Sequence[MDagPath]):
	"""Array of MDagPath values."""
	@property
	def sizeIncrement(self)->Any:
		"""Number of elements by which to grow the array when necessary."""
	@sizeIncrement.setter
	def sizeIncrement(self,value:Any)->None:...
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def __len__(self)->int:
		"""Return len(self)."""
	def __getitem__(self,index:int)->MDagPath:
		"""Return self[key]."""
	def __setitem__(self,index:int,value:MDagPath)->None:
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
class MDataBlock:
	"""Dependency node data block."""
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def context(self)->MDGContext:
		"""context() -> MDGContext

		Returns a copy of the dependecy graph context for which this data block was created. The context is used to specify how a dependency node is going to be evaluated."""
	@overload
	def inputArrayValue(self,plug:MPlug)->MArrayDataHandle:
		"""inputArrayValue(plug) -> MArrayDataHandle
		inputArrayValue(attribute) -> MArrayDataHandle

		Gets an array handle to this data block for the given plug/attribute's data.  This is only valid if the given plug has array data.  The data represented by the handle will be valid.  If the data is from a dirty connection, then the connection will be evaluated.  If no connection is present, then the value that the plug has been set to will be returned.  If the plug has not been set to a particular value, then the default value will be returned.

		* plug (MPlug) - the plug whose data you wish to access
		 OR
		* attribute (MObject) - the attribute whose data you wish to access"""
	@overload
	def inputArrayValue(self,attribute:MObject)->MArrayDataHandle:
		"""inputArrayValue(plug) -> MArrayDataHandle
		inputArrayValue(attribute) -> MArrayDataHandle

		Gets an array handle to this data block for the given plug/attribute's data.  This is only valid if the given plug has array data.  The data represented by the handle will be valid.  If the data is from a dirty connection, then the connection will be evaluated.  If no connection is present, then the value that the plug has been set to will be returned.  If the plug has not been set to a particular value, then the default value will be returned.

		* plug (MPlug) - the plug whose data you wish to access
		 OR
		* attribute (MObject) - the attribute whose data you wish to access"""
	@overload
	def inputValue(self,plug:MPlug)->MDataHandle:
		"""inputValue(plug) -> MDataHandle
		inputValue(attribute) -> MDataHandle

		Gets a handle to this data block for the given plug/attribute's data.  The data represented by the handle is guaranteed to be valid for reading.  If the data is from a dirty connection, then the connection will be evaluated.  If no connection is present, then the value that the plug has been set to will be returned. If the plug has not been set to a particular value, then the default value will be returned.

		* plug (MPlug) - the plug whose data you wish to access
		 OR
		* attribute (MObject) - the attribute of the node that you want to access"""
	@overload
	def inputValue(self,attribute:MObject)->MDataHandle:
		"""inputValue(plug) -> MDataHandle
		inputValue(attribute) -> MDataHandle

		Gets a handle to this data block for the given plug/attribute's data.  The data represented by the handle is guaranteed to be valid for reading.  If the data is from a dirty connection, then the connection will be evaluated.  If no connection is present, then the value that the plug has been set to will be returned. If the plug has not been set to a particular value, then the default value will be returned.

		* plug (MPlug) - the plug whose data you wish to access
		 OR
		* attribute (MObject) - the attribute of the node that you want to access"""
	@overload
	def isClean(self,plug:MPlug)->bool:
		"""isClean(plug) -> bool
		isClean(attribute) -> bool

		Queries the dependency graph to see whether the given plug/attribute is clean.

		* plug (MPlug) - the plug that is to be query
		 OR
		* attribute (MObject) - the attribute that is to be query."""
	@overload
	def isClean(self,attribute:MObject)->bool:
		"""isClean(plug) -> bool
		isClean(attribute) -> bool

		Queries the dependency graph to see whether the given plug/attribute is clean.

		* plug (MPlug) - the plug that is to be query
		 OR
		* attribute (MObject) - the attribute that is to be query."""
	@overload
	def outputArrayValue(self,plug:MPlug)->MArrayDataHandle:
		"""outputArrayValue(plug) -> MArrayDataHandle
		outputArrayValue(attribute) -> MArrayDataHandle

		Gets a handle to this data block for the given plug/attribute's data.  No dependency graph evaluations will be done, and therefore the data is not guaranteed to be valid (i.e. it may be dirty).  Typically, this method is used to get the handle during compute in order to write output data to it.

		Another usage of this method is to access an input array attribute without evaluating any of its array elements. One can then use MArrayDataHandle.jumpToElement() to get to the particular element of interest, and evaluate its value using MArrayDataHandle.inputValue().

		* plug (MPlug) - the plug whose data you wish to access
		 OR
		* attribute (MObject) - the attribute whose data you wish to access"""
	@overload
	def outputArrayValue(self,attribute:MObject)->MArrayDataHandle:
		"""outputArrayValue(plug) -> MArrayDataHandle
		outputArrayValue(attribute) -> MArrayDataHandle

		Gets a handle to this data block for the given plug/attribute's data.  No dependency graph evaluations will be done, and therefore the data is not guaranteed to be valid (i.e. it may be dirty).  Typically, this method is used to get the handle during compute in order to write output data to it.

		Another usage of this method is to access an input array attribute without evaluating any of its array elements. One can then use MArrayDataHandle.jumpToElement() to get to the particular element of interest, and evaluate its value using MArrayDataHandle.inputValue().

		* plug (MPlug) - the plug whose data you wish to access
		 OR
		* attribute (MObject) - the attribute whose data you wish to access"""
	@overload
	def outputValue(self,plug:MPlug)->MDataHandle:
		"""outputValue(plug) -> MDataHandle
		outputValue(attribute) -> MDataHandle

		Gets a handle to this data block for the given plug/attribute's data.  The data is not guaranteed to be valid.  No dependency graph evaluations will be done. Therefore, this handle should be used only for writing.

		* plug (MPlug) - the plug whose data you wish to access
		 OR
		* attribute (MObject) - the attribute of the node that you want to access"""
	@overload
	def outputValue(self,attribute:MObject)->MDataHandle:
		"""outputValue(plug) -> MDataHandle
		outputValue(attribute) -> MDataHandle

		Gets a handle to this data block for the given plug/attribute's data.  The data is not guaranteed to be valid.  No dependency graph evaluations will be done. Therefore, this handle should be used only for writing.

		* plug (MPlug) - the plug whose data you wish to access
		 OR
		* attribute (MObject) - the attribute of the node that you want to access"""
	@overload
	def setClean(self,plug:MPlug)->Self:
		"""setClean(plug) -> self
		setClean(attribute) -> self

		Tells the dependency graph that the given plug/attribute has been updated and is now clean.  This should be called after the data in the plug has been recalculated from the inputs of the node.

		* plug (MPlug) - the plug that is to be marked clean
		 OR
		* attribute (MObject) - the attribute that is to be marked clean"""
	@overload
	def setClean(self,attribute:MObject)->Self:
		"""setClean(plug) -> self
		setClean(attribute) -> self

		Tells the dependency graph that the given plug/attribute has been updated and is now clean.  This should be called after the data in the plug has been recalculated from the inputs of the node.

		* plug (MPlug) - the plug that is to be marked clean
		 OR
		* attribute (MObject) - the attribute that is to be marked clean"""
	def setContext(self,ctx:MDGContext)->Self:
		"""setContext(ctx) -> self

		Set the dependency graph context for this data block. The context is used to specify how a dependency node is going to be evaluated, thus replacing the context for the given datablock. This does not modify the dirty state of the datablock so that they apply to the new context.

		This function should not be used for timed evaluation.

		* ctx (MDGContext) - the dependency graph context"""
class MDataHandle:
	"""Data handle for information contained in a data block."""
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def acceptedTypeIds(self)->Any:
		"""acceptedTypeIds() -> array of MTypeIds

		This method returns an array of MTypeIds."""
	def asAddr(self)->int:
		"""asAddr() -> long

		Returns the data represented by this handle in the data block."""
	def asAngle(self)->MAngle:
		"""asAngle() -> MAngle

		Returns the data represented by this handle in the data block."""
	def asBool(self)->bool:
		"""asBool() -> bool

		Returns the data represented by this handle in the data block."""
	def asChar(self)->int:
		"""asChar() -> int

		Returns the data represented by this handle in the data block."""
	def asDistance(self)->MDistance:
		"""asDistance() -> MDistance

		Returns the data represented by this handle in the data block."""
	def asDouble(self)->float:
		"""asDouble() -> float

		Returns the data represented by this handle in the data block."""
	def asDouble2(self)->list[float]:
		"""asDouble2() -> [float, float]

		Returns the data represented by this handle in the data block."""
	def asDouble3(self)->list[float]:
		"""asDouble3() -> [float, float, float]

		Returns the data represented by this handle in the data block."""
	def asDouble4(self)->list[float]:
		"""asDouble4() -> [float, float, float, float]

		Returns the data represented by this handle in the data block."""
	def asFloat(self)->float:
		"""asFloat() -> float

		Returns the data represented by this handle in the data block."""
	def asFloat2(self)->list[float]:
		"""asFloat2() -> [float, float]

		Returns the data represented by this handle in the data block."""
	def asFloat3(self)->list[float]:
		"""asFloat3() -> [float, float, float]

		Returns the data represented by this handle in the data block."""
	def asFloatMatrix(self)->MFloatMatrix:
		"""asFloatMatrix() -> MFloatMatrix

		Returns the data represented by this handle in the data block."""
	def asFloatVector(self)->MFloatVector:
		"""asFloatVector() -> MFloatVector

		Returns the data represented by this handle in the data block."""
	def asGenericBool(self)->bool:
		"""asGenericBool() -> bool

		Returns the generic data represented by this handle in the data block."""
	def asGenericChar(self)->int:
		"""asGenericChar() -> int

		Returns the generic data represented by this handle in the data block."""
	def asGenericDouble(self)->float:
		"""asGenericDouble() -> float

		Returns the generic data represented by this handle in the data block."""
	def asGenericFloat(self)->float:
		"""asGenericFloat() -> float

		Returns the generic data represented by this handle in the data block."""
	def asGenericInt(self)->int:
		"""asGenericInt() -> int

		Returns the generic data represented by this handle in the data block."""
	def asGenericShort(self)->int:
		"""asGenericShort() -> int

		Returns the generic data represented by this handle in the data block."""
	def asInt(self)->int:
		"""asInt() -> int

		Returns the data represented by this handle in the data block."""
	def asInt2(self)->list[int]:
		"""asInt2() -> [int, int]

		Returns the data represented by this handle in the data block."""
	def asInt3(self)->list[int]:
		"""asInt3() -> [int, int, int]

		Returns the data represented by this handle in the data block."""
	def asMatrix(self)->MMatrix:
		"""asMatrix() -> MMatrix

		Returns the data represented by this handle in the data block.This method is only valid for attributes created using the MFnMatrixAttribute function set."""
	def asMesh(self)->MObject:
		"""asMesh() -> MObject

		Returns the data represented by this handle in the data block.  The object returned by this call may be used directly with the mesh function set and iterators.  Even though this method does not return a reference to an MObject, modifications to the MObject instance will update the contents of the handle in the data block.  The method MDataHandle.setClean() should be called after the data block has been modified.

		The surface returned by this method will be in local space even if the connection is supplying world space geometry.  This occurs mostly for efficiency reasons.  In the case of a world space geometry connection, the MObject returned by this method will also contain the world space transformation matrix. This means that world space operations may be performed on this object using the mesh function set and iterators.

		It is possible to get the matrix that defines the local to world transformation for this geometry using the MDataHandle.geometryTransformMatrix() method."""
	def asMeshTransformed(self)->MObject:
		"""asMeshTransformed() -> MObject

		Returns the data represented by this handle in the data block.  The object returned by this call may be used directly with the mesh function set (MFnMesh) or any of the mesh iterators.

		If the incoming mesh comes with world space transformation data, then it will be applied to the data that is returned.  In other words, the mesh that is returned will be the mesh as it exists in world space.

		The mesh that is returned from this method should not be modified.  This method is only provided to make it easier to take world space geometry as input."""
	def asNurbsCurve(self)->MObject:
		"""asNurbsCurve() -> MObject

		Returns the data represented by this handle in the data block.  The object returned by this call may be used directly with the nurbs curve function set and iterator.  Even though this method does not return a reference to an MObject, modifications to the MObject instance will update the contents of the handle in the data block.  The method MDataHandle.setClean() should be called after the data block has been modified.

		The curve returned by this method will be in local space even if the connection is supplying world space geometry.  This occurs mostly for efficiency reasons.  In the case of a world space geometry connection, the MObject returned by this method will also contain the world space transformation matrix. This means that world space operations may be performed on this object using the nurbs curve function set and iterator.

		It is possible to get the matrix that defines the local to world transformation for this geometry using the MDataHandle.geometryTransformMatrix() method."""
	def asNurbsCurveTransformed(self)->MObject:
		"""asNurbsCurveTransformed() -> MObject

		Returns the data represented by this handle in the data block.  The object returned by this call may be used directly with the nurbs curve function set (MFnNurbsCurve) or the nurbs curve CV iterator (MItCurveCV).

		If the incoming curve comes with world space transformation data, then it will be applied to the data that is returned.  In other words, the curve that is returned will be the curve as it exists in world space.

		The curve that is returned from this method should not be modified.  This method is only provided to make it easier to take world space geometry as input."""
	def asNurbsSurface(self)->MObject:
		"""asNurbsSurface() -> MObject

		Returns the data represented by this handle in the data block.  The object returned by this call may be used directly with the nurbs surface function set and iterator.  Even though this method does not return a reference to an MObject, modifications to the MObject instance will update the contents of the handle in the data block.  The method MDataHandle.setClean() should be called after the data block has been modified.

		The surface returned by this method will be in local space even if the connection is supplying world space geometry.  This occurs mostly for efficiency reasons.  In the case of a world space geometry connection, the MObject returned by this method will also contain the world space transformation matrix.  This means that world space operations may be performed on this object using the nurbs surface function set and iterator.

		It is possible to get the matrix that defines the local to world transformation for this geometry using the MDataHandle.geometryTransformMatrix() method."""
	def asNurbsSurfaceTransformed(self)->MObject:
		"""asNurbsSurfaceTransformed() -> MObject

		Returns the data represented by this handle in the data block.  The object returned by this call may be used directly with the nurbs surface function set (MFnNurbsSurface) or the nurbs surface CV iterator (MItSurfaceCV).

		If the incoming surface comes with world space transformation data, then it will be applied to the data that is returned.  In other words, the surface that is returned will be the surface as it exists in world space.

		The surface that is returned from this method should not be modified.  This method is only provided to make it easier to take world space geometry as input."""
	def asPluginData(self)->MPxData:
		"""asPluginData() -> MPxData

		Returns the data represented by this handle in the data block.  The object is returned as plugin data.  This should be used to access data types defined by plugins."""
	def asShort(self)->int:
		"""asShort() -> int

		Returns the data represented by this handle in the data block."""
	def asShort2(self)->list[int]:
		"""asShort2() -> [int, int]

		Returns the data represented by this handle in the data block."""
	def asShort3(self)->list[int]:
		"""asShort3() -> [int, int, int]

		Returns the data represented by this handle in the data block."""
	def asString(self)->str:
		"""asString() -> MString

		Returns the data represented by this handle in the data block."""
	def asSubdSurface(self)->MObject:
		"""asSubdSurface() -> MObject

		Returns the data represented by this handle in the data block.  The object returned by this call may be used directly with the subdivision surface function set and iterator.  Even though this method does not return a reference to an MObject, modifications to the MObject instance will update the contents of the handle in the data block.  The method MDataHandle.setClean() should be called after the data block has been modified.

		The subdivision surface returned by this method will be in local space even if the connection is supplying world space geometry.  This occurs mostly for efficiency reasons.  In the case of a world space geometry connection, the MObject returned by this method will also contain the world space   transformation matrix. This means that world space operations may be performed on this object using the subdivision surface function set and iterator.

		It is possible to get the matrix that defines the local to world transformation for this geometry using the MDataHandle.geometryTransformMatrix() method."""
	def asSubdSurfaceTransformed(self)->MObject:
		"""asSubdSurfaceTransformed() -> MObject

		Returns the data represented by this handle in the data block.  The object returned by this call may be used directly with the subdivision surface function set (MFnSubdSurface) or the subdivision surface iterators (MItSubdVertex, MItSubdFace, MItSubdEdge).

		If the incoming surface comes with world space transformation data, then it will be applied to the data that is returned.  In other words, the surface that is returned will be the surface as it exists in world space.

		The surface that is returned from this method should not be modified.  This method is only provided to make it easier to take world space geometry as input."""
	def asTime(self)->MTime:
		"""asTime() -> MTime

		Returns the data represented by this handle in the data block."""
	def asUChar(self)->int:
		"""asUChar() -> int

		Returns the data represented by this handle in the data block."""
	def asVector(self)->MVector:
		"""asVector() -> MVector

		Returns the data represented by this handle in the data block."""
	@overload
	def child(self,MPlug:Any)->MDataHandle:
		"""child(MPlug) -> MDataHandle
		child(MObject) -> MDataHandle

		Get a handle to a child of this handle.  This is used if you have a handle to a compound attribute."""
	@overload
	def child(self,MObject:Any)->MDataHandle:
		"""child(MPlug) -> MDataHandle
		child(MObject) -> MDataHandle

		Get a handle to a child of this handle.  This is used if you have a handle to a compound attribute."""
	def copy(self,src:MDataHandle)->Self:
		"""copy(src) -> self

		Copies the attribute from the src attribute to the attribute referenced by this handle.  This is the only method which can completely copy a compound attribute from one handle to another.  The construct outputHandle.set (inputHandle.data()) will not work for compound or multi attributes.

		* src (MDataHandle) - the handle to the attribute to copy."""
	def copyWritable(self,src:MDataHandle)->Self:
		"""copyWritable(src) -> self

		Copies the attribute from the <i>src</i> attribute to the attribute referenced by this handle.  When the copy is made it ensures that the data in this handle is writable. That is, if the src handle has a writable copy of the data then it will be duplicated, otherwise this handle will claim the writer status for the data.

		* src (MDataHandle) - the handle to the attribute to copy."""
	def data(self)->MObject:
		"""data() -> MObject

		Returns the data object from this handle.  The object returned should be used with the appropriate data function set.  This method is not valid for simple numeric types."""
	def geometryTransformMatrix(self)->MMatrix:
		"""geometryTransformMatrix() -> MMatrix

		This method returns a reference to the local-to-world transformation matrix that can accompany a geometry data object.  Only use this method on handles to geometry data (curves, surfaces, and meshes).

		If no local-to-world transformation information has been provided then this will be an identity matrix."""
	def isGeneric(self)->list[bool]:
		"""isGeneric() -> [bool, isNumeric, isNull]

		Returns True if this handle is for generic data.  There are 2 forms of generic data.  The first is for simple data and is used if the isNumeric parameter returns True.  In this case, the asGeneric*() and setGeneric*() methods of this class are used to query and set values.
		The second form of generic data is for more complex attribute types.  As a result the type of the object must be checked and an appropriate attribute function set initialized with the object.Returns isNumeric True if this handle is for simple generic numeric data.
		Returns isNull True if this handle is not set."""
	def isNumeric(self)->bool:
		"""isNumeric() -> bool

		Returns True if this handle is for simple numeric data. That means that the numeric data is directly accessible through the non-generic as*() and set*() methods of this handle. For example, depending on handle initialization, the asBool() may be called but the asGenericBool() should not be called."""
	def numericType(self)->int:
		"""numericType() -> int

		Returns the type of data represented by this handle.  This method is only valid for data handles of simple numeric types."""
	def set2Double(self,float:float,float2:float)->Self:
		"""set2Double(float, float) -> self

		Set the data that this handle represents in the data block."""
	def set2Float(self,float:float,float2:float)->Self:
		"""set2Float(float, float) -> self

		Set the data that this handle represents in the data block."""
	def set2Int(self,int:int,int2:int)->Self:
		"""set2Int(int, int) -> self

		Set the data that this handle represents in the data block."""
	def set2Short(self,int:int,int2:int)->Self:
		"""set2Short(int, int) -> self

		Set the data that this handle represents in the data block."""
	def set3Double(self,float:float,float2:float,float3:float)->Self:
		"""set3Double(float, float, float) -> self

		Set the data that this handle represents in the data block."""
	def set4Double(self,float:float,float2:float,float3:float,float4:float)->Self:
		"""set4Double(float, float, float, float) -> self

		Set the data that this handle represents in the data block."""
	def set3Float(self,float:float,float2:float,float3:float)->Self:
		"""set3Float(float, float, float) -> self

		Set the data that this handle represents in the data block."""
	def set3Int(self,int:int,int2:int,int3:int)->Self:
		"""set3Int(int, int, int) -> self

		Set the data that this handle represents in the data block."""
	def set3Short(self,int:int,int2:int,int3:int)->Self:
		"""set3Short(int, int, int) -> self

		Set the data that this handle represents in the data block."""
	def setBool(self,bool:bool)->Self:
		"""setBool(bool) -> self

		Set the data that this handle represents in the data block."""
	def setChar(self,int:int)->Self:
		"""setChar(int) -> self

		Set the data that this handle represents in the data block."""
	def setClean(self)->Self:
		"""setClean() -> self

		Marks the data that is represented by this handle as being clean.  This should be done after recalculating the data from the inputs."""
	def setDouble(self,float:float)->Self:
		"""setDouble(float) -> self

		Set the data that this handle represents in the data block."""
	def setFloat(self,float:float)->Self:
		"""setFloat(float) -> self

		Set the data that this handle represents in the data block."""
	def setGenericBool(self,bool:bool,force:Any)->Self:
		"""setGenericBool(bool, force) -> self

		Set the data that this handle represents in the data block."""
	def setGenericChar(self,int:int,force:Any)->Self:
		"""setGenericChar(int, force) -> self

		Set the data that this handle represents in the data block."""
	def setGenericDouble(self,float:float,force:Any)->Self:
		"""setGenericDouble(float, force) -> self

		Set the data that this handle represents in the data block."""
	def setGenericFloat(self,float:float,force:Any)->Self:
		"""setGenericFloat(float, force) -> self

		Set the data that this handle represents in the data block."""
	def setGenericInt(self,int:int,force:Any)->Self:
		"""setGenericInt(int, force) -> self

		Set the data that this handle represents in the data block."""
	def setGenericShort(self,int:int,force:Any)->Self:
		"""setGenericShort(int, force) -> self

		Set the data that this handle represents in the data block."""
	def setInt(self,int:int)->Self:
		"""setInt(int) -> self

		Set the data that this handle represents in the data block."""
	def setMAngle(self,MAngle:Any)->Self:
		"""setMAngle(MAngle) -> self

		Set the data that this handle represents in the data block."""
	def setMDistance(self,MDistance:Any)->Self:
		"""setMDistance(MDistance) -> self

		Set the data that this handle represents in the data block."""
	def setMFloatMatrix(self,MFloatMatrix:Any)->Self:
		"""setMFloatMatrix(MFloatMatrix) -> self

		Set the data that this handle represents in the data block."""
	def setMFloatVector(self,MFloatVector:Any)->Self:
		"""setMFloatVector(MFloatVector) -> self

		Set the data that this handle represents in the data block."""
	def setMMatrix(self,MMatrix:Any)->Self:
		"""setMMatrix(MMatrix) -> self

		Set the data that this handle represents in the data block."""
	def setMObject(self,MObject:Any)->Self:
		"""setMObject(MObject) -> self

		Set the data that this handle represents in the data block.  This method assumes that the MObject is a dependency graph data object.  These objects can be created using the appropriate MFn..Data function set.
		Note that this method cannot be used to copy compound or multi attributes from one handle to another via the construct outputHandle.set (inputHandle.data()).
		To copy these user defined attributes, the method MDataHandle.copy() must be used."""
	def setMPxData(self,MPxData:Any)->Self:
		"""setMPxData(MPxData) -> self

		Set the data that this handle represents in the data block.  This method takes a pointer to a user defined data object.  The data block will become the new owner of the data object that you pass in.  Do not delete it."""
	def setMTime(self,MTime:Any)->Self:
		"""setMTime(MTime) -> self

		Set the data that this handle represents in the data block."""
	def setMVector(self,MVector:Any)->Self:
		"""setMVector(MVector) -> self

		Set the data that this handle represents in the data block."""
	def setShort(self,int:int)->Self:
		"""setShort(int) -> self

		Set the data that this handle represents in the data block."""
	def setString(self,string:str)->Self:
		"""setString(string) -> self

		Set the data that this handle represents in the data block."""
	def type(self)->int:
		"""type() -> int

		Returns the type of data represented by this handle."""
	def typeId(self)->MTypeId:
		"""typeId() -> MTypeId

		Returns the type of data represented by this handle as a type id.  A type id is a four character code that is used to identify the data type.
		If no data exists for this handle, the type id will be 0x0."""
	def datablock(self)->MDataBlock:
		"""datablock() -> MDataBlock

		Returns a reference to the datablock assigned to this data handle."""
class MDistance:
	"""Manipulate distance data."""
	@property
	def unit(self)->int:
		"""Distance units currently in use."""
	@unit.setter
	def unit(self,value:int)->None:...
	@property
	def value(self)->float:
		"""Value of the distance in the current units."""
	@value.setter
	def value(self,value:float)->None:...
	kInvalid:int=0
	kInches:int=1
	kFeet:int=2
	kYards:int=3
	kMiles:int=4
	kMillimeters:int=5
	kCentimeters:int=6
	kKilometers:int=7
	kMeters:int=8
	kLast:int=9
	@overload
	def __init__(self)->None:
		"""Default constructor. Returns a new MDistance with a value of 0.0 centimeters."""
	@overload
	def __init__(self,src:MDistance)->None:
		"""Copy constructor. Returns a new MDistance with the same value and unit type as src ."""
	@overload
	def __init__(self,value:float,unit:int)->None:
		"""Returns a new MDistance using the given value and unit ."""
	@staticmethod
	def uiUnit()->int:
		"""Returns the type of units currently being used to enter and display distances in Maya's UI."""
	@staticmethod
	def setUIUnit(newUnit:int)->None:
		"""Sets the type of units to be used to enter and display distances in Maya's UI"""
	@staticmethod
	def internalUnit()->int:
		"""Returns the type of units in which Maya stores distance values internally (e.g. in plugs and binary file formats)."""
	@staticmethod
	def internalToUI(internalValue:float)->float:
		"""Interprets internalValue as a distance in Maya's internal units and returns it converted to UI units."""
	@staticmethod
	def uiToInternal(uiValue:float)->float:
		"""Interprets uiValue as a distance in Maya's UI units and returns it converted to internal units."""
	def asUnits(self,unit:int)->float:
		"""Returns the distance value, converted to the specified unit ."""
	def asInches(self)->float:
		"""Returns the distance value, converted to inches."""
	def asFeet(self)->float:
		"""Returns the distance value, converted to feet."""
	def asYards(self)->float:
		"""Returns the distance value, converted to yards."""
	def asMiles(self)->float:
		"""Returns the distance value, converted to miles."""
	def asMillimeters(self)->float:
		"""Returns the distance value, converted to millimeters."""
	def asCentimeters(self)->float:
		"""Returns the distance value, converted to centimeters."""
	def asKilometers(self)->float:
		"""Returns the distance value, converted to kilometers."""
	def asMeters(self)->float:
		"""Returns the distance value, converted to meters."""
class MDoubleArray(collections.abc.Sequence[float]):
	"""Array of double values."""
	@property
	def sizeIncrement(self)->Any:
		"""Number of elements by which to grow the array when necessary."""
	@sizeIncrement.setter
	def sizeIncrement(self,value:Any)->None:...
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def __len__(self)->int:
		"""Return len(self)."""
	def __getitem__(self,index:int)->float:
		"""Return self[key]."""
	def __setitem__(self,index:int,value:float)->None:
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
class MEulerRotation(collections.abc.Sequence[float]):
	"""X, Y and Z rotations, applied in a specified order."""
	@property
	def x(self)->float:
		"""X rotation in radians"""
	@x.setter
	def x(self,value:float)->None:...
	@property
	def y(self)->float:
		"""Y rotation in radians"""
	@y.setter
	def y(self,value:float)->None:...
	@property
	def z(self)->float:
		"""Z rotation in radians"""
	@z.setter
	def z(self,value:float)->None:...
	@property
	def order(self)->int:
		"""Rotation order"""
	@order.setter
	def order(self,value:int)->None:...
	__hash__:None=None
	kIdentity:MEulerRotation
	kTolerance:float=1e-10
	kXYZ:int=0
	kYZX:int=1
	kZXY:int=2
	kXZY:int=3
	kYXZ:int=4
	kZYX:int=5
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
	@overload
	def __init__(self)->None:
		"""Default constructor. Returns a new MEulerRotation object, initialized to the identity rotation."""
	@overload
	def __init__(self,src:MEulerRotation)->None:
		"""Copy constructor. Returns a new MEulerRotation object with the same value as src ."""
	@overload
	def __init__(self,vec:MVector,order:int)->None:
		"""Returns a new MEulerRotation with the given order and its X, Y and Z rotations set to the corresponding elements of vec ."""
	@overload
	def __init__(self,seq:Sequence[float],order:int)->None:
		"""Returns a new MEulerRotation with the given order and its X, Y and Z rotations set to the corresponding elements of seq ."""
	@overload
	def __init__(self,x:float,y:float,z:float,order:int)->None:
		"""Returns a new MEulerRotation with the specified x , y and z rotations and the given rotation order ."""
	def __add__(self,other:MEulerRotation)->MEulerRotation:
		"""Component-by-component addition. Right operand is first reordered to match left, if necessary."""
	def __radd__(self,other:MEulerRotation)->MEulerRotation:
		"""Component-by-component addition. Right operand is first reordered to match left, if necessary."""
	def __sub__(self,other:MEulerRotation)->MEulerRotation:
		"""Component-by-component subtraction. Right operand is first reordered to match left, if necessary."""
	def __rsub__(self,other:MEulerRotation)->MEulerRotation:
		"""Component-by-component subtraction. Right operand is first reordered to match left, if necessary."""
	@overload
	def __mul__(self,other:MEulerRotation)->MEulerRotation:
		"""Multiplication of rotations. Rotation order of left operand is preserved."""
	@overload
	def __mul__(self,other:MQuaternion)->MEulerRotation:
		"""Multiplication of rotation by a quaternion. Rotation order of left operand is preserved."""
	@overload
	def __mul__(self,other:float)->MEulerRotation:
		"""Component-by-component multiplication by a scalar."""
	def __rmul__(self,other:MEulerRotation)->MEulerRotation:
		"""Multiplication of rotations. Rotation order of left operand is preserved."""
	def __neg__(self)->Self:
		"""-self"""
	def __iadd__(self,other:MEulerRotation)->Self:
		"""In-place addition. Right operand is first reordered to match left, if necessary. Returns a new reference to the rotation."""
	def __isub__(self,other:MEulerRotation)->Self:
		"""In-place subtraction. Right operand is first reordered to match left, if necessary. Returns a new reference to the rotation."""
	@overload
	def __imul__(self,other:MEulerRotation)->Self:
		"""In-place multiplication of rotations. Rotation order of left operand is preserved. Returns a new reference to the rotation."""
	@overload
	def __imul__(self,other:MQuaternion)->Self:
		"""In-place multiplication of rotation by a quaternion. Rotation order of left operand is preserved. Returns a new reference to the rotation."""
	@overload
	def __imul__(self,other:float)->Self:
		"""In-place multiplication by a scalar. Returns a new reference to the rotation."""
	def __len__(self)->int:
		"""Return len(self)."""
	def __getitem__(self,index:int)->float:
		"""Return self[key]."""
	def __setitem__(self,index:int,value:float)->None:
		"""Set self[key] to value."""
	def __delitem__(self,index:int)->None:
		"""Delete self[key]."""
	@staticmethod
	def computeAlternateSolution(rot:MEulerRotation)->MEulerRotation:
		"""Returns a rotation equivalent to rot which is not simply a multiple of it."""
	@staticmethod
	def computeBound(rot:MEulerRotation)->MEulerRotation:
		"""Returns a rotation equivalent to rot but bound within +/- PI."""
	@staticmethod
	def computeClosestCut(src:MEulerRotation,target:MEulerRotation)->MEulerRotation:
		"""Returns the rotation which is full spin multiples of src and comes closest to target ."""
	@staticmethod
	def computeClosestSolution(src:MEulerRotation,target:MEulerRotation)->MEulerRotation:
		"""Returns the rotation equivalent to src which comes closest to target ."""
	@staticmethod
	def decompose(matrix:MMatrix,order:int)->MEulerRotation:
		"""Extracts from matrix a valid rotation having the specified rotation order . Note that this may be just one of several different rotations which could each give rise to the same matrix."""
	def alternateSolution(self)->MEulerRotation:
		"""Returns a new MEulerRotation with a different rotation which is equivalent to this one and has the same rotation order. Each rotation component will lie within +/- PI."""
	def asMatrix(self)->MMatrix:
		"""Returns the rotation as an equivalent matrix."""
	def asQuaternion(self)->MQuaternion:
		"""Returns the rotation as an equivalent quaternion."""
	def asVector(self)->MVector:
		"""Returns the X, Y and Z rotations as a vector. Rotation order is ignored."""
	def bound(self)->MEulerRotation:
		"""Returns a new MEulerRotation having this rotation, but with each rotation component bound within +/- PI."""
	@overload
	def boundIt(self)->Self:
		"""In-place bounding of each rotation component to lie wthin +/- PI."""
	@overload
	def boundIt(self,rot:MEulerRotation)->Self:
		"""Replace this rotation with the bound version of rot ."""
	def closestCut(self,target:MEulerRotation)->MEulerRotation:
		"""Returns a new MEulerRotation containing the rotation which is full spin multiples of this one and comes closest to target ."""
	def closestSolution(self,target:MEulerRotation)->MEulerRotation:
		"""Returns a new MEulerRotation containing the rotation equivalent to this one which comes closest to target ."""
	def incrementalRotateBy(self,axis:MVector,angle:float)->Self:
		"""Increase this rotation by angle radians around the specified axis . The update is done in series of small increments to avoid flipping."""
	def inverse(self)->MEulerRotation:
		"""Returns a new MEulerRotation containing the inverse rotation of this one and reversed rotation order."""
	def invertIt(self)->Self:
		"""In-place inversion of the rotation. Rotation order is also reversed."""
	def isEquivalent(self,other:MEulerRotation,tolerance:float=MEulerRotation.kTolerance)->bool:
		"""Inexact equality test. Returns true if this rotation has the same order as other and their X, Y and Z components are within tolerance of each other."""
	def isZero(self,tolerance:float=MEulerRotation.kTolerance)->bool:
		"""Inexact zero test. Returns true if the X, Y and Z components are each within tolerance of 0.0."""
	def reorder(self,order:int)->MEulerRotation:
		"""Returns a new MEulerRotation having this rotation, reordered to use the given rotation order ."""
	def reorderIt(self,order:int)->Self:
		"""In-place reordering to use the given rotation order ."""
	@overload
	def setToAlternateSolution(self)->Self:
		"""Replace with a different but equivalent rotation, having the same rotation order and with each rotation component lying wthin +/- PI."""
	@overload
	def setToAlternateSolution(self,rot:MEulerRotation)->Self:
		"""Replace this rotation with the alternate solution for rot ."""
	@overload
	def setToClosestCut(self,target:MEulerRotation)->Self:
		"""Replace this rotation with the one which is full spin multiples of this one and comes closest to target ."""
	@overload
	def setToClosestCut(self,src:MEulerRotation,target:MEulerRotation)->Self:
		"""Replace this rotation with the closest cut of src to target ."""
	@overload
	def setToClosestSolution(self,target:MEulerRotation)->Self:
		"""Replace this rotation with the equivalent rotation which comes closest to target ."""
	@overload
	def setToClosestSolution(self,src:MEulerRotation,target:MEulerRotation)->Self:
		"""Replace this rotation with the closest solution of src to target ."""
	@overload
	def setValue(self,rot:MEulerRotation)->Self:
		"""Set the rotation and order to match that of rot ."""
	@overload
	def setValue(self,quat:MQuaternion)->Self:
		"""Set the rotation and order to provide a rotation equivalent to that of rot ."""
	@overload
	def setValue(self,mat:MMatrix)->Self:
		"""Set the rotation order and the X, Y and Z rotations to those extracted from mat , as per the decompose() method, using the current order."""
	@overload
	def setValue(self,vec:MVector,order:int=MEulerRotation.kXYZ)->Self:
		"""Set the rotation order to order and set the X, Y and Z rotations to the corresponding components of vec ."""
	@overload
	def setValue(self,seq:Sequence[float],order:int=MEulerRotation.kXYZ)->Self:
		"""Set the rotation order to order and the X, Y and Z rotations to the corresponding components of seq ."""
	@overload
	def setValue(self,x:float,y:float,z:float,order:int=MEulerRotation.kXYZ)->Self:
		"""Set the given rotation order and x , y and z rotation components."""
class MEvaluationNode:
	"""A class providing access to Evaluation Manager node information."""
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def iterator(self,*args)->Any:
		"""Returns an iterator at the beginning of the dirty plug list."""
	def dirtyPlugExists(self,*args)->Any:
		"""Returns true if the specified attribute has a dirty plug. This call should be made from MPxNode::preEvaluation() and MPxNode::postEvaluation() to verify which plugs are going to be dirty and computed."""
	def dirtyPlug(self,*args)->Any:
		"""Returns the top-most plug for the specified attribute if the attribute has dirty plugs. This call should be made from MPxNode::preEvaluation() and MPxNode::postEvaluation() to access a networked plug which is going to be dirty and computed."""
	def dependencyNode(self,*args)->Any:
		"""Returns the dependency node this evaluation node represents."""
	def datablock(self,*args)->Any:
		"""Returns the datablock for this node."""
class MEvaluationNodeIterator:
	"""A class providing access to the Evaluation Manager node dirty plug list."""
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def plug(self,*args)->Any:
		"""Returns the dirty plug at the current iterator position. Returns an empty plug if the iterator is illegal."""
	def isDone(self,*args)->Any:
		"""Checks to see if the iterator has reached the end of the iteration."""
	def next(self,*args)->Any:
		"""Advances the iterator to the next position in the dirty plug list."""
	def reset(self,*args)->Any:
		"""Resets the iterator to the first position in the dirty plug list."""
class MEventMessage(MMessage):
	"""Class used to register callbacks for event related messages.

	The first parameter passed to the add callback method is the name
	of the event that will trigger the callback.  The list of
	available event names can be retrieved by calling the
	getEventNames method or by using the -listEvents flag on the
	scriptJob command.
	The addEventCallback method returns an id which is used to remove the
	callback.

	To remove a callback use OpenMaya.MMessage.removeCallback.

	All callbacks that are registered by a plug-in must be removed by
	that plug-in when it is unloaded.  Failure to do so will result in
	a fatal error.

	Idle event callbacks should be removed immediately after running.
	Otherwise they will continue to use up CPU resources. They will also
	prevent idleVeryLow event callbacks from running - which are required
	for Maya to function properly.
	"""
	@staticmethod
	def addEventCallback(eventName:str,function:Callable,clientData:Any|None=None)->int:
		"""addEventCallback(eventName, function, clientData=None) -> id

		This method registers a callback for event occurred messages.
		The callback function will be passed the any client data that
		was provided when the callback was registered.

		 * eventName (string) - the event to register the
		callback for
		 * function - callable which will be passed the clientData object
		 * clientData - User defined data passed to the callback function

		 * return: Identifier used for removing the callback."""
	@staticmethod
	def getEventNames()->tuple[str,...]:
		"""getEventNames() -> (string, string, ...)

		This method returns the list of available event names.

		 * return: tuple of available event names."""
class MExternalContentInfoTable:
	"""This is a table of all the external content for a given node."""
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def __len__(self)->int:
		"""Return len(self)."""
	def __getitem__(self,index:int)->Any:
		"""Return self[key]."""
	def addResolvedEntry(self,key:str,unresolvedLocation:str,resolvedLocation:str,contextNodeFullName:str,roles:list[str])->Self:
		"""addResolvedEntry(key, unresolvedLocation, resolvedLocation, contextNodeFullName, roles) -> self

		Add an entry in the table.

		* key (string) - An arbitrary string defined by the caller. This will typically be an attribute name for situations where the content location is stored verbatim in a plug's value.
		* unresolvedLocation (string) - Path as stored in the node (i.e. without any token replacement performed).
		* resolvedLocation (string) - Full path to the content if it exists at the time of creation of this object.
		* contextNodeFullName (string) - The fullname of the URI owner (node) if it applies, an empty string otherwise.
		* roles (list of strings) - An enumeration of all roles this content plays in the context of the node. The actual strings are not rigidly defined as of this writing. This is mostly for offline browsing of the content info: to assist in sorting content by role.  A better content type system may be introduced later on to        formalize this."""
	def addUnresolvedEntry(self,key:str,unresolvedLocation:str,contextNodeFullName:str,roles:list[str]|None=None)->Self:
		"""addUnresolvedEntry(key, unresolvedLocation, contextNodeFullName, roles=None) -> self

		Add an entry in the table. The resolved location will be inferred from the application's built-in file resolving for the specified file type. This will automatically add entries into the roles vector that correspond to the search rules for this file type.

		* key (string) - See documentation of MExternalContentInfoTable.addResolvedEntry().
		* unresolvedLocation (string) - See documentation of MExternalContentInfoTable.addResolvedEntry().
		* contextNodeFullName (string) - See documentation of MExternalContentInfoTable.addResolvedEntry().
		* roles (list of strings) - See documentation of MExternalContentInfoTable.addResolvedEntry()."""
	def getEntry(self,index:int)->list[key|unresolvedLocation|resolvedLocation|str|roles]:
		"""getEntry(index) -> [key, unresolvedLocation, resolvedLocation, contextNodeFullName, roles]

		Retrieves external content entry based on its position in the table.

		* index (unsigned int) - Position of the entry to retrieve information from."""
	def getInfo(self,key:str)->list[unresolvedLocation|resolvedLocation|str|roles]:
		"""getInfo(key) -> [unresolvedLocation, resolvedLocation, contextNodeFullName, roles]

		Retrieves external content information based on its key.

		* key (string) - See documentation of MExternalContentInfoTable.addResolvedEntry()."""
class MExternalContentLocationTable:
	"""This is a table of the all the external content locations for a given node."""
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def __len__(self)->int:
		"""Return len(self)."""
	def __getitem__(self,index:int)->Any:
		"""Return self[key]."""
	def addEntry(self,key:str,location:str)->Self:
		"""addEntry(key, location) -> self

		Adds an external content location and its key to the table.

		* key (string) - An arbitrary string defined by the node. This will typically be an attribute name for situations where the content location is stored verbatim in a plug's value.* location (string) - Full path to the content referenced by the key."""
	def getEntry(self,index:int)->list[key|location]:
		"""getEntry(index) -> [key, location]

		Retrieves external content entry based on its position in the table.

		* index (unsigned int) - Position of the entry to retrieve information from."""
	def getLocation(self,key:str)->str:
		"""getLocation(key) -> string

		Retrieves an entry's location based on the associated key.

		* key (string) - See documentation of MExternalContentLocationTable.addEntry()."""
class MFileObject:
	"""Manipulate filenames and search paths."""
	@property
	def resolveMethod(self)->Any:
		"""The file-path resolution steps this file object will use."""
	@resolveMethod.setter
	def resolveMethod(self,value:Any)->None:...
	kNone:int=1
	kExact:int=2
	kDirMap:int=4
	kReferenceMappings:int=8
	kRelative:int=16
	kBaseName:int=32
	kInputFile:int=54
	kInputReference:int=62
	kStrict:int=6
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def copy(self,source:MFileObject)->Self:
		"""copy(source) -> self

		Copy data from source file object.

		* source (MFileObject) - The source file object to copy from"""
	def exists(self,index:int|None=None)->bool:
		"""exists(index=None) -> bool

		Checks to see if the file exists and is readable.
		If index is None tests for the fullName file, else tests the file constructed from the indicated portion of the path element and filename element.

		* index (int) - Index of the path element to be used in searching for the file."""
	def expandedFullName(self)->str:
		"""expandedFullName() -> string

		Returns the pathname of a file constructed from the unresolved file object values. The file name will consist of the the expanded raw path and raw name elements.
		All variables in the path element are expanded, and the first path (the part before the first separator (':') in the path) is prepended to the filename element to construct the fullName.

		After expanding environment variables Maya may perform additional modifications to the full file name in order to resolve it to a valid location on disk. This resolved full file name can be accessed through resolvedFullName()."""
	def expandedPath(self)->str:
		"""expandedPath() -> string

		Returns the raw path element of the unresolved file object with all environment variables expanded. In the case that the path expands to multiple paths, the first expanded path will be returned.

		After expanding environment variables Maya may perform additional modifications to the path in order to resolve it to a valid location on disk. This resolved path can be accessed through resolvedPath()."""
	def fullName(self,index:int)->str:
		"""fullName(index) -> string

		Returns the pathname of a file constructed from the indicated portion of the path element and filename element.
		All variables in the path element are expanded, and the indicated path portion is prepended to the filename element to construct the fullName.

		* index (int) - the index of the desired path portion."""
	@staticmethod
	def getResolvedFullName(rawFullName:str)->str:
		"""getResolvedFullName(rawFullName) -> string

		Returns the full path to the resolved file, or an empty string if the resolution was unsuccessful.

		* rawFullName (string) - The fully specified unresolved path."""
	@staticmethod
	def getResolvedFullNameAndExistsStatus(rawFullName:str,method:int=MFileObject.kNone)->tuple[str,bool]:
		"""getResolvedFullNameAndExistsStatus(rawFullName, method=kNone) -> (string, bool)

		Returns the full path to the resolved file, or an empty string if the resolution was unsuccessful, and a boolean that indicate if the resolved path exists or not.

		* rawFullName (string) - The fully specified unresolved path
		* resolveMethod (int) - To resolve method to use, default is kNone.

		Valid resolve methods:
		  kNone                    The resolved path is simply the resulting path after converting
		                           the raw value to its expanded form. If the path contains environment variables,
		                           the resolved value will be the first path returned from their expansion.
		                           Relative paths will be considered to be relative to root of the current project.
		                           The resolution algorithm will not check if this file actually exists - the
		                           resolution will be considered successful whether it exists or not.
		                           With this mode, the resolver will not continue on to attempt to resolve
		                           using any other resolve method.
		                           The user must explicitly check MFileObject.exists() to determine if it is an
		                           existing path.
		  kExact                   Checks if expanded paths exist. If paths are relative, assume it's relative to
		                           the current workspace (so check workspace current directory, file-rule directory and
		                           root directory).
		  kDirMap                  Checks path against mappings defined with the dirmap command. Only for absolute paths
		  kReferenceMappings       Check path against any previously re-mapped reference locations. If kRelative/kBaseName
		                           are set, then even if we have an absolute path, convert to relative and/or baseName and
		                           look for them in directories provided to the missing reference dialog.
		  kRelative                Strips away the project directory, and treats path as relative. Relative to the current
		                           workspace, that is. So look in the workspace current directory, file-rules directory
		                           and the root directory.
		  kBaseName                Strips away everything but the base file name and look in the current workspace,
		  kInputFile               This mode is the default on file open and import, and is suitable for
		                           files that are to be used as input files.  The file will be checked for
		                           existence.
		                           Combination of kExact, kDirMap, kRelative and kBaseName.
		  kInputReference          This mode is the default on file reference. In addition to the checks done for
		                           a regular input file, it will also check the reference mappings.
		                           Combination of kInputFile and kReferenceMappings.
		  kStrict                  Combination of kExact and kDirMap."""
	@staticmethod
	def isAbsolutePath(fileName:str)->bool:
		"""isAbsolutePath(fileName) -> bool

		Checks a file path string and determines if it represents an absolute file path. An absolute path can uniquely identify a directory or file.

		* fileName (string) - the string used to check if it is absolute"""
	def isSet(self)->bool:
		"""isSet() -> bool

		Checks to see if both file and path elements of the file object have been set."""
	def overrideResolvedFullName(self,fullFileName:str,reresolveType:Any=False)->Self:
		"""overrideResolvedFullName(fullFileName, reresolveType=False) -> self

		Normally when a raw file name is set, Maya will perform a series of operations on it in an attempt to resolve it to a valid file name. This final resolved file name can be accessed through the resolvedName(), resolvedPath(), and resolvedFullFileName() methods and can be quite different from the originally specified raw file name.

		This method will override the normal Maya path resolution process and explicitly set the resolved file name. This path does not have to be a valid file path, but if any '/' characters appear in the given name then the resolved path element of the file object is set to everything in name up to, but not including the last '/'. The resolved filename is set to the part of name after the final '/'.

		Once the resolved file name is set, it is only guaranteed to be retained in the file object so long as the raw file path is not updated. Once the rawPath, rawName or rawFullName are set, the normal Maya path resolution process will be re-invoked and the resolved path and filename will be updated.

		- fullFileName (string) - the string used to override the path and filename.- reresolveType (bool) - if Maya should re-resolve the file type/translator."""
	def path(self,index:int)->str:
		"""path(index) -> string

		Returns the indicated portion of the path element of the file object.  All variables in the path element are expanded, and the portion indicated by the argument is extracted and returned.

		* index (int) - the index of the desired path portion."""
	def pathCount(self)->int:
		"""pathCount() -> int

		Returns the number of paths in the path element of the file object.
		This will be equal to one more than the number of ':' characters specified of the rawPath attribute."""
	def rawFullName(self)->str:
		"""rawFullName() -> string

		Returns the unresolved full file name (path plus filename) of the MFileObject with all environment variables unexpanded.

		This method differs from expandedFullName() in that it returns the unexpanded instead of expanded values."""
	def rawName(self)->str:
		"""rawName() -> string

		Returns the unresolved filename element of the MFileObject."""
	def rawPath(self)->str:
		"""rawPath() -> string

		Returns the path element of the MFileObject with all environment variables unexpanded."""
	def rawURI(self)->MURI:
		"""rawURI() -> MURI

		Returns the unresolved URI of the MFileObject, if any.

		This will be empty if the MFileObject was not resolved from a URI."""
	def resolvedFullName(self)->str:
		"""resolvedFullName() -> string

		Returns the first pathname of a file constructed from the path and filename elements.  All variables in the path element are expanded, and the first path (the part before the first ':' in the path) is prepended to the filename element. After expanding all environment     variables Maya may then perform additional modifications, such  as prepending directories to a relative path name, in order to resolve the path to a valid location on disk.

		The resolution is performed using the ResolveMethod of the file object.
		By default, this will be set to kNone. While this is suitable in many situations, it may not be appropriate if the file is expected to exist.
		Refer to getResolvedFullNameAndExistsStatus() for more information about how the  resolution mode is used.

		Failure to resolve the path according to the specifications of the file object will result in an empty return value."""
	def resolvedName(self)->str:
		"""resolvedName() -> string

		Returns the resolved filename element of the file object."""
	def resolvedPath(self)->str:
		"""resolvedPath() -> string

		Returns the resolved path element of the file object. In order to build the resolved path, Maya first expands all environment variables and then may perform additional modifications, such as prepending directories to a relative path name, in order to resolve the path to a valid location on disk."""
	def setRawFullName(self,fullFileName:str)->Self:
		"""setRawFullName(fullFileName) -> self

		This method combines the functions of the setRawName and setRawPath methods in that it sets both the path and filename from the given name.

		If any '/' characters appear in the given name then the path element of the MFileObject is set to everything in name up to, but not including the last '/'.  The filename is set to the part of name after the final '/'.

		If no '/' characters appear in the given name then the path element is set to "." and the filename is set to the given name.

		Note that if the specified fullFileName is relative, contains environment variables, or does not exist, the full names returned by resolvedFullName() and expandedFullName() may not match the fullFileName. See the description of resolvedFullName() and expandedFullName() for more information.

		Also note that for URI-based file paths (e.g. "arrow:uri_path_to_file"),  setRawFullName will not call setRawName and setRawPath (raw name and path will remain empty). Use resolvedName and resolvedPath to retrieve the resolved file path, or rawFullName to retrieve the unresolved file path.

		* fullFileName (string) - The string used to initialize the path and filename."""
	def setRawName(self,fileName:str)->Self:
		"""setRawName(fileName) -> self

		Set the unresolved filename element of the MFileObject instance.  This name should not contain any '/' characters, it should indicate simply the name of a file.  The directories in which this name will be searched for are specified by setRawPath.

		* fileName (string) - The filename to set."""
	def setRawPath(self,pathName:str)->Self:
		"""setRawPath(pathName) -> self

		Set the unresolved path element of the MFileObject instance.  This should contain a list of directories, each separated by a single ':' character.  The pathnames can contain Unix environment variables in the form $VARNAME.  These will be expanded when paths to actual filenames are constructed.

		Note that if the specified pathName is relative, contains environment variables, or does not exist, the paths returned by resolvedPath() and expandedPath() may not match the rawPath. See the description of resolvedPath() and expandedPath() for more information.

		* pathName (string) - The path string."""
	def setRawURI(self,uri:str|MURI)->Self:
		"""setRawURI(uri) -> self

		Set the unresolved URI of the MFileObject instance.

		* uri (string or MURI) - The unresolved URI."""
class MFloatArray(collections.abc.Sequence[float]):
	"""Array of float values."""
	@property
	def sizeIncrement(self)->Any:
		"""Number of elements by which to grow the array when necessary."""
	@sizeIncrement.setter
	def sizeIncrement(self,value:Any)->None:...
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def __len__(self)->int:
		"""Return len(self)."""
	def __getitem__(self,index:int)->float:
		"""Return self[key]."""
	def __setitem__(self,index:int,value:float)->None:
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
class MFloatMatrix(collections.abc.Sequence[float]):
	"""4x4 matrix with single-precision elements."""
	__hash__:None=None
	kTolerance:float=9.999999747378752e-06
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
	@overload
	def __init__(self)->None:
		"""Default constructor. Returns a new matrix set to the identity matrix."""
	@overload
	def __init__(self,src:MFloatMatrix)->None:
		"""Copy constructor. Returns a new matrix with the same value as src ."""
	@overload
	def __init__(self,values:Sequence[Any|tuple[Any,...]])->None:
		"""Returns a new matrix whose elements are set to those given by values . Values are interpreted in row order, so the first four values make up the first row of the matrix, the second four values the second row of the matrix, and so on."""
	def __add__(self,other:MFloatMatrix)->MFloatMatrix:
		"""Returns a new matrix which is the sum of the two matrices."""
	def __radd__(self,other:MFloatMatrix)->MFloatMatrix:
		"""Returns a new matrix which is the sum of the two matrices."""
	def __sub__(self,other:MFloatMatrix)->MFloatMatrix:
		"""Returns a new matrix which is the result of subtracting the second matrix from the first."""
	def __rsub__(self,other:MFloatMatrix)->MFloatMatrix:
		"""Returns a new matrix which is the result of subtracting the second matrix from the first."""
	@overload
	def __mul__(self,other:MFloatMatrix)->MFloatMatrix:
		"""Returns a new matrix which is the product of the two matrices."""
	@overload
	def __mul__(self,other:float)->MFloatMatrix:
		"""Returns a new matrix in which all of the elements of the given matrix have been multiplied by the given Float."""
	@overload
	def __rmul__(self,other:MFloatMatrix)->MFloatMatrix:
		"""Returns a new matrix which is the product of the two matrices."""
	@overload
	def __rmul__(self,other:float)->MFloatMatrix:
		"""Returns a new matrix in which all of the elements of the given matrix have been multiplied by the given Float."""
	def __iadd__(self,other:MFloatMatrix)->Self:
		"""Adds the second matrix to the first and returns a new reference to the first."""
	def __isub__(self,other:MFloatMatrix)->Self:
		"""Subtracts the second matrix from the first and returns a new reference to the first."""
	@overload
	def __imul__(self,other:MFloatMatrix)->Self:
		"""Multiplies the first matrix by the second and returns a new reference to the first."""
	@overload
	def __imul__(self,other:float)->Self:
		"""Multiplies all the elements of the matrix by the Float and returns a new reference to the matrix."""
	def __len__(self)->int:
		"""Return len(self)."""
	def __getitem__(self,index:int)->float:
		"""Return self[key]."""
	def __setitem__(self,index:int,value:float)->None:
		"""Set self[key] to value."""
	def __delitem__(self,index:int)->None:
		"""Delete self[key]."""
	def getElement(self,row:int,col:int)->float:
		"""Returns the matrix element specified by row and col . For retrieving single elements this is faster than indexing into the matrix as a sequence because it does not require the creation of an entire row tuple simply to retrieve one element from that row."""
	def setElement(self,row:int,col:int,value:float)->Self:
		"""Set the matrix element specified by row and col to the given value ."""
	def setToIdentity(self)->Self:
		"""Sets this matrix to the identity."""
	def setToProduct(self,left:MFloatMatrix,right:MFloatMatrix)->Self:
		"""Sets this matrix to the product of left and right ."""
	def transpose(self)->MFloatMatrix:
		"""Returns a new matrix containing this matrix's transpose."""
	def inverse(self)->MFloatMatrix:
		"""Returns a new matrix containing this matrix's nverse."""
	def adjoint(self)->MFloatMatrix:
		"""Returns a new matrix containing this matrix's adjoint."""
	def homogenize(self)->MFloatMatrix:
		"""Returns a new matrix containing the homogenized version of this matrix."""
	def det4x4(self)->float:
		"""Returns this matrix's determinant."""
	def det3x3(self)->float:
		"""Returns the determinant of the 3x3 matrix formed by the first 3 elements of the first 3 rows of this matrix."""
	def isEquivalent(self,other:MFloatMatrix,tol:float=MEulerRotation.kTolerance)->bool:
		"""Inexact equality test. Returns True if each element of this matrix is within tolerance of the corresponding element of other ."""
class MFloatPoint(collections.abc.Sequence[float]):
	"""3D point with single-precision coordinates."""
	@property
	def x(self)->float:
		"""X coordinate"""
	@x.setter
	def x(self,value:float)->None:...
	@property
	def y(self)->float:
		"""Y coordinate"""
	@y.setter
	def y(self,value:float)->None:...
	@property
	def z(self)->float:
		"""Z coordinate"""
	@z.setter
	def z(self,value:float)->None:...
	@property
	def w(self)->float:
		"""W coordinate"""
	@w.setter
	def w(self,value:float)->None:...
	__hash__:None=None
	kOrigin:MFloatPoint
	kTolerance:float=9.999999747378752e-06
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
	@overload
	def __init__(self)->None:
		"""Default constructor. Returns a new MFloatPoint object, initialized to the origin."""
	@overload
	def __init__(self,src:MFloatPoint|MPoint|MFloatVector|MVector)->None:
		"""Copy constructor. Returns a new MFloatPoint object with its x, y, z and w coords set to the same values as src . If src is a vector then the new MFloatPoint 's w coordinate is set to 1.0."""
	@overload
	def __init__(self,seq:Sequence[two|three|float])->None:
		"""Returns a new MFloatPoint object whose x, y, z and w coordinates are set to the elements of seq . If the sequence contains fewer than four values w will be set to 1.0. If the sequence contains fewer than three values z will be set to 0.0."""
	@overload
	def __init__(self,x:float,y:float,z:float,w:float)->None:
		"""Returns a new MFloatPoint object with the specified x , y , z and w coordinates."""
	def __add__(self,other:MFloatVector)->MFloatPoint:
		"""Addition of a vector to a point."""
	def __radd__(self,*args)->Any:
		"""Return value+self."""
	@overload
	def __sub__(self,other:MFloatVector)->MFloatPoint:
		"""Subtraction of a vector from a point."""
	@overload
	def __sub__(self,other:MFloatPoint)->MFloatVector:
		"""Vector difference between two points."""
	def __rsub__(self,other:MFloatPoint)->MFloatVector:
		"""Vector difference between two points."""
	@overload
	def __mul__(self,other:MFloatMatrix)->MFloatPoint:
		"""Post-multiplication of a point by a matrix."""
	@overload
	def __mul__(self,other:float)->MFloatPoint:
		"""Multiplication of a point by a scalar. The scalar must be convertable to Float."""
	def __rmul__(self,other:MFloatMatrix)->MFloatPoint:
		"""Pre-multiplication of a point by a matrix."""
	def __iadd__(self,other:MFloatVector)->Self:
		"""In-place addition of a vector to the point. Returns a new reference to the point."""
	def __isub__(self,other:MFloatVector)->Self:
		"""In-place subtraction of a vector from a point. Returns a new reference to the point."""
	def __imul__(self,other:MFloatMatrix)->Self:
		"""In-place post-multiplication of a point by a matrix. Returns a new reference to the point."""
	def __truediv__(self,other:float)->MFloatPoint:
		"""Division of a point by a scalar. The scalar must be convertable to Float."""
	def __rtruediv__(self,other)->Any:
		"""Return value/self."""
	def __len__(self)->int:
		"""Return len(self)."""
	def __getitem__(self,index:int)->float:
		"""Return self[key]."""
	def __setitem__(self,index:int,value:float)->None:
		"""Set self[key] to value."""
	def __delitem__(self,index:int)->None:
		"""Delete self[key]."""
	def cartesianize(self)->Self:
		"""Converts this point to cartesian form."""
	def rationalize(self)->Self:
		"""Converts this point to rational form."""
	def homogenize(self)->Self:
		"""Converts this point to homogenous form."""
	def distanceTo(self,other:MFloatPoint)->float:
		"""Returns the distance between this point and other ."""
	def isEquivalent(self,other:MFloatPoint,tol:float=MEulerRotation.kTolerance)->bool:
		"""Returns True if the coordinates of this point and other are equal to within a tolerance of tol ."""
class MFloatPointArray(collections.abc.Sequence[MFloatPoint]):
	"""Array of MFloatPoint values."""
	@property
	def sizeIncrement(self)->Any:
		"""Number of elements by which to grow the array when necessary."""
	@sizeIncrement.setter
	def sizeIncrement(self,value:Any)->None:...
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def __len__(self)->int:
		"""Return len(self)."""
	def __getitem__(self,index:int)->MFloatPoint:
		"""Return self[key]."""
	def __setitem__(self,index:int,value:MFloatPoint)->None:
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
class MFloatVector(collections.abc.Sequence[float]):
	"""3D vector with single-precision coordinates."""
	@property
	def x(self)->float:
		"""X coordinate"""
	@x.setter
	def x(self,value:float)->None:...
	@property
	def y(self)->float:
		"""Y coordinate"""
	@y.setter
	def y(self,value:float)->None:...
	@property
	def z(self)->float:
		"""Z coordinate"""
	@z.setter
	def z(self,value:float)->None:...
	__hash__:None=None
	kTolerance:float=9.999999747378752e-06
	kZeroVector:MFloatVector
	kOneVector:MFloatVector
	kXaxisVector:MFloatVector
	kYaxisVector:MFloatVector
	kZaxisVector:MFloatVector
	kXnegAxisVector:MFloatVector
	kYnegAxisVector:MFloatVector
	kZnegAxisVector:MFloatVector
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
	@overload
	def __init__(self)->None:
		"""Default constructor. Returns a new MFloatVector object initialized to the zero vector."""
	@overload
	def __init__(self,src:MVector|MFloatVector|MPoint|MFloatPoint)->None:
		"""Copy constructor. Returns a new MFloatVector object whose x, y and z coordinates are set to the x, y and z coordinates of src ."""
	@overload
	def __init__(self,seq:Sequence[Any])->None:
		"""Returns a new MFloatVector object whose x, y and z coordinates are set to the elements of seq . If the sequence only contains two values, z will be set to 0.0."""
	@overload
	def __init__(self,x:float,y:float,z:float)->None:
		"""Returns a new MFloatVector object with the specified x , y and z coordinates."""
	def __add__(self,other:MFloatVector)->MFloatVector:
		"""Vector addition."""
	def __radd__(self,other:MFloatVector)->MFloatVector:
		"""Vector addition."""
	def __sub__(self,other:MFloatVector)->MFloatVector:
		"""Vector subtraction."""
	def __rsub__(self,other:MFloatVector)->MFloatVector:
		"""Vector subtraction."""
	@overload
	def __mul__(self,other:MFloatVector)->float:
		"""Dot product of the two vectors."""
	@overload
	def __mul__(self,other:float)->MFloatVector:
		"""Returns a new vector whose components are those of the given vector, each multiplied by scalar , which can be of any type which is convertable to float."""
	@overload
	def __mul__(self,other:MFloatMatrix)->MFloatVector:
		"""Postmultiplying a vector by a matrix."""
	@overload
	def __rmul__(self,other:MFloatVector)->float:
		"""Dot product of the two vectors."""
	@overload
	def __rmul__(self,other:float)->MFloatVector:
		"""Returns a new vector whose components are those of the given vector, each multiplied by scalar , which can be of any type which is convertable to float."""
	@overload
	def __rmul__(self,other:MFloatMatrix)->MFloatVector:
		"""Premultiplying a vector by a matrix."""
	def __neg__(self)->Self:
		"""-self"""
	def __xor__(self,other:MFloatVector)->MFloatVector:
		"""Cross product of two vectors."""
	def __rxor__(self,other:MFloatVector)->MFloatVector:
		"""Cross product of two vectors."""
	def __iadd__(self,other:MFloatVector)->Self:
		"""In-pace vector addition."""
	def __isub__(self,other:MFloatVector)->Self:
		"""In-place vector subtraction."""
	@overload
	def __imul__(self,other:float)->Self:
		"""Multiplies each component of the vector by scalar , which can be of any type which is convertable to float, and returns a new reference to the vector."""
	@overload
	def __imul__(self,other:MFloatMatrix)->Self:
		"""Postmultiplies the vector by the matrix and returns a new reference to the vector."""
	def __truediv__(self,other:float)->MFloatVector:
		"""Returns a new vector whose components are those of the given vector, each divided by scalar , which can be of any type which is convertable to float."""
	def __rtruediv__(self,other)->Any:
		"""Return value/self."""
	def __itruediv__(self,other:float)->Self:
		"""Divides each component of the vector by scalar , which can be of any type which is convertable to float, and returns a new reference to the vector."""
	def __len__(self)->int:
		"""Return len(self)."""
	def __getitem__(self,index:int)->float:
		"""Return self[key]."""
	def __setitem__(self,index:int,value:float)->None:
		"""Set self[key] to value."""
	def __delitem__(self,index:int)->None:
		"""Delete self[key]."""
	def length(self)->float:
		"""Returns the magnitude of this vector."""
	def normal(self)->MFloatVector:
		"""Returns a new vector containing the normalized version of this vector."""
	def normalize(self)->Self:
		"""Normalizes this vector in-place and returns a new reference to it."""
	def transformAsNormal(self,matrix:MFloatMatrix)->MFloatVector:
		"""Returns a new vector which is calculated by postmultiplying this vector by the transpose of matrix and then normalizing it."""
	def angle(self,other:MFloatVector)->float:
		"""Returns the angle, in radians, between this vector and other ."""
	def isEquivalent(self,other:MFloatVector,tolerance:float=MEulerRotation.kTolerance)->bool:
		"""Returns True if this vector and other are within the given tolerance of being equal."""
	def isParallel(self,other:MFloatVector,tolerance:float=MEulerRotation.kTolerance)->bool:
		"""Returns True if this vector and other are within the given tolerance of being parallel."""
class MFloatVectorArray(collections.abc.Sequence[MFloatVector]):
	"""Array of MFloatVector values."""
	@property
	def sizeIncrement(self)->Any:
		"""Number of elements by which to grow the array when necessary."""
	@sizeIncrement.setter
	def sizeIncrement(self,value:Any)->None:...
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def __len__(self)->int:
		"""Return len(self)."""
	def __getitem__(self,index:int)->MFloatVector:
		"""Return self[key]."""
	def __setitem__(self,index:int,value:MFloatVector)->None:
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
class MFn:
	"""Static class providing constants for all API types."""
	kInvalid:int=0
	kBase:int=1
	kNamedObject:int=2
	kModel:int=3
	kDependencyNode:int=4
	kAddDoubleLinear:int=5
	kAffect:int=6
	kAnimCurve:int=7
	kAnimCurveTimeToAngular:int=8
	kAnimCurveTimeToDistance:int=9
	kAnimCurveTimeToTime:int=10
	kAnimCurveTimeToUnitless:int=11
	kAnimCurveUnitlessToAngular:int=12
	kAnimCurveUnitlessToDistance:int=13
	kAnimCurveUnitlessToTime:int=14
	kAnimCurveUnitlessToUnitless:int=15
	kResultCurve:int=16
	kResultCurveTimeToAngular:int=17
	kResultCurveTimeToDistance:int=18
	kResultCurveTimeToTime:int=19
	kResultCurveTimeToUnitless:int=20
	kAngleBetween:int=21
	kAudio:int=22
	kBackground:int=23
	kColorBackground:int=24
	kFileBackground:int=25
	kRampBackground:int=26
	kBlend:int=27
	kBlendTwoAttr:int=28
	kBlendWeighted:int=29
	kBlendDevice:int=30
	kBlendColors:int=31
	kBump:int=32
	kBump3d:int=33
	kCameraView:int=34
	kChainToSpline:int=35
	kChoice:int=36
	kCondition:int=37
	kContrast:int=38
	kClampColor:int=39
	kCreate:int=40
	kAlignCurve:int=41
	kAlignSurface:int=42
	kAttachCurve:int=43
	kAttachSurface:int=44
	kAvgCurves:int=45
	kAvgSurfacePoints:int=46
	kAvgNurbsSurfacePoints:int=47
	kBevel:int=48
	kBirailSrf:int=49
	kDPbirailSrf:int=50
	kMPbirailSrf:int=51
	kSPbirailSrf:int=52
	kBoundary:int=53
	kCircle:int=54
	kCloseCurve:int=55
	kClosestPointOnSurface:int=56
	kCloseSurface:int=57
	kCurveFromSurface:int=58
	kCurveFromSurfaceBnd:int=59
	kCurveFromSurfaceCoS:int=60
	kCurveFromSurfaceIso:int=61
	kCurveInfo:int=62
	kDetachCurve:int=63
	kDetachSurface:int=64
	kExtendCurve:int=65
	kExtendSurface:int=66
	kExtrude:int=67
	kFFblendSrf:int=68
	kFFfilletSrf:int=69
	kFilletCurve:int=70
	kFitBspline:int=71
	kFlow:int=72
	kHardenPointCurve:int=73
	kIllustratorCurve:int=74
	kInsertKnotCrv:int=75
	kInsertKnotSrf:int=76
	kIntersectSurface:int=77
	kNurbsTesselate:int=78
	kNurbsPlane:int=79
	kNurbsCube:int=80
	kOffsetCos:int=81
	kOffsetCurve:int=82
	kPlanarTrimSrf:int=83
	kPointOnCurveInfo:int=84
	kPointOnSurfaceInfo:int=85
	kPrimitive:int=86
	kProjectCurve:int=87
	kProjectTangent:int=88
	kRBFsurface:int=89
	kRebuildCurve:int=90
	kRebuildSurface:int=91
	kReverseCurve:int=92
	kReverseSurface:int=93
	kRevolve:int=94
	kRevolvedPrimitive:int=95
	kCone:int=96
	kRenderCone:int=97
	kCylinder:int=98
	kSphere:int=99
	kSkin:int=100
	kStitchSrf:int=101
	kSubCurve:int=102
	kSurfaceInfo:int=103
	kTextCurves:int=104
	kTrim:int=105
	kUntrim:int=106
	kDagNode:int=107
	kProxy:int=108
	kUnderWorld:int=109
	kTransform:int=110
	kAimConstraint:int=111
	kLookAt:int=112
	kGeometryConstraint:int=113
	kGeometryVarGroup:int=114
	kAnyGeometryVarGroup:int=115
	kCurveVarGroup:int=116
	kMeshVarGroup:int=117
	kSurfaceVarGroup:int=118
	kIkEffector:int=119
	kIkHandle:int=120
	kJoint:int=121
	kManipulator3D:int=122
	kArrowManip:int=123
	kAxesActionManip:int=124
	kBallProjectionManip:int=125
	kCircleManip:int=126
	kScreenAlignedCircleManip:int=127
	kCircleSweepManip:int=128
	kConcentricProjectionManip:int=129
	kCubicProjectionManip:int=130
	kCylindricalProjectionManip:int=131
	kDiscManip:int=132
	kFreePointManip:int=133
	kCenterManip:int=134
	kLimitManip:int=135
	kEnableManip:int=136
	kFreePointTriadManip:int=137
	kPropMoveTriadManip:int=138
	kTowPointManip:int=139
	kPolyCreateToolManip:int=140
	kPolySplitToolManip:int=141
	kGeometryOnLineManip:int=142
	kCameraPlaneManip:int=143
	kToggleOnLineManip:int=144
	kStateManip:int=145
	kIsoparmManip:int=146
	kLineManip:int=147
	kManipContainer:int=148
	kAverageCurveManip:int=149
	kBarnDoorManip:int=150
	kBevelManip:int=151
	kBlendManip:int=152
	kButtonManip:int=153
	kCameraManip:int=154
	kCoiManip:int=155
	kCpManip:int=156
	kCreateCVManip:int=157
	kCreateEPManip:int=158
	kCurveEdManip:int=159
	kCurveSegmentManip:int=160
	kDirectionManip:int=161
	kDofManip:int=162
	kDropoffManip:int=163
	kExtendCurveDistanceManip:int=164
	kExtrudeManip:int=165
	kIkSplineManip:int=166
	kIkRPManip:int=167
	kJointClusterManip:int=168
	kLightManip:int=169
	kMotionPathManip:int=170
	kOffsetCosManip:int=171
	kOffsetCurveManip:int=172
	kProjectionManip:int=173
	kPolyProjectionManip:int=174
	kProjectionUVManip:int=175
	kProjectionMultiManip:int=176
	kProjectTangentManip:int=177
	kPropModManip:int=178
	kQuadPtOnLineManip:int=179
	kRbfSrfManip:int=180
	kReverseCurveManip:int=181
	kReverseCrvManip:int=182
	kReverseSurfaceManip:int=183
	kRevolveManip:int=184
	kRevolvedPrimitiveManip:int=185
	kSpotManip:int=186
	kSpotCylinderManip:int=187
	kTriplanarProjectionManip:int=188
	kTrsManip:int=189
	kDblTrsManip:int=190
	kPivotManip2D:int=191
	kManip2DContainer:int=192
	kPolyMoveUVManip:int=193
	kPolyMappingManip:int=194
	kPolyModifierManip:int=195
	kPolyMoveVertexManip:int=196
	kPolyVertexNormalManip:int=197
	kTexSmudgeUVManip:int=198
	kTexLatticeDeformManip:int=199
	kTexLattice:int=200
	kTexSmoothManip:int=201
	kTrsTransManip:int=202
	kTrsInsertManip:int=203
	kTrsXformManip:int=204
	kManipulator2D:int=205
	kTranslateManip2D:int=206
	kPlanarProjectionManip:int=207
	kPointOnCurveManip:int=208
	kTowPointOnCurveManip:int=209
	kMarkerManip:int=210
	kPointOnLineManip:int=211
	kPointOnSurfaceManip:int=212
	kTranslateUVManip:int=213
	kRotateBoxManip:int=214
	kRotateManip:int=215
	kHandleRotateManip:int=216
	kRotateLimitsManip:int=217
	kScaleLimitsManip:int=218
	kScaleManip:int=219
	kScalingBoxManip:int=220
	kScriptManip:int=221
	kSphericalProjectionManip:int=222
	kTextureManip3D:int=223
	kToggleManip:int=224
	kTranslateBoxManip:int=225
	kTranslateLimitsManip:int=226
	kTranslateManip:int=227
	kTrimManip:int=228
	kJointTranslateManip:int=229
	kManipulator:int=230
	kCirclePointManip:int=231
	kDimensionManip:int=232
	kFixedLineManip:int=233
	kLightProjectionGeometry:int=234
	kLineArrowManip:int=235
	kPointManip:int=236
	kTriadManip:int=237
	kNormalConstraint:int=238
	kOrientConstraint:int=239
	kPointConstraint:int=240
	kSymmetryConstraint:int=241
	kParentConstraint:int=242
	kPoleVectorConstraint:int=243
	kScaleConstraint:int=244
	kTangentConstraint:int=245
	kUnknownTransform:int=246
	kWorld:int=247
	kShape:int=248
	kBaseLattice:int=249
	kCamera:int=250
	kCluster:int=251
	kSoftMod:int=252
	kCollision:int=253
	kDummy:int=254
	kEmitter:int=255
	kField:int=256
	kAir:int=257
	kDrag:int=258
	kGravity:int=259
	kNewton:int=260
	kRadial:int=261
	kTurbulence:int=262
	kUniform:int=263
	kVortex:int=264
	kGeometric:int=265
	kCurve:int=266
	kNurbsCurve:int=267
	kNurbsCurveGeom:int=268
	kDimension:int=269
	kAngle:int=270
	kAnnotation:int=271
	kDistance:int=272
	kArcLength:int=273
	kRadius:int=274
	kParamDimension:int=275
	kDirectedDisc:int=276
	kRenderRect:int=277
	kEnvFogShape:int=278
	kLattice:int=279
	kLatticeGeom:int=280
	kLocator:int=281
	kDropoffLocator:int=282
	kMarker:int=283
	kOrientationMarker:int=284
	kPositionMarker:int=285
	kOrientationLocator:int=286
	kTrimLocator:int=287
	kPlane:int=288
	kSketchPlane:int=289
	kGroundPlane:int=290
	kOrthoGrid:int=291
	kSprite:int=292
	kSurface:int=293
	kNurbsSurface:int=294
	kNurbsSurfaceGeom:int=295
	kMesh:int=296
	kMeshGeom:int=297
	kRenderSphere:int=298
	kFlexor:int=299
	kClusterFlexor:int=300
	kGuideLine:int=301
	kLight:int=302
	kAmbientLight:int=303
	kNonAmbientLight:int=304
	kAreaLight:int=305
	kLinearLight:int=306
	kNonExtendedLight:int=307
	kDirectionalLight:int=308
	kPointLight:int=309
	kSpotLight:int=310
	kParticle:int=311
	kPolyToolFeedbackShape:int=312
	kRigidConstraint:int=313
	kRigid:int=314
	kSpring:int=315
	kUnknownDag:int=316
	kDefaultLightList:int=317
	kDeleteComponent:int=318
	kDispatchCompute:int=319
	kShadingEngine:int=320
	kDisplacementShader:int=321
	kDistanceBetween:int=322
	kDOF:int=323
	kDummyConnectable:int=324
	kDynamicsController:int=325
	kGeoConnectable:int=326
	kExpression:int=327
	kExtract:int=328
	kFilter:int=329
	kFilterClosestSample:int=330
	kFilterEuler:int=331
	kFilterSimplify:int=332
	kGammaCorrect:int=333
	kGeometryFilt:int=334
	kBendLattice:int=335
	kBlendShape:int=336
	kCombinationShape:int=337
	kBulgeLattice:int=338
	kFFD:int=339
	kFfdDualBase:int=340
	kRigidDeform:int=341
	kSculpt:int=342
	kTextureDeformer:int=343
	kTextureDeformerHandle:int=344
	kTweak:int=345
	kWeightGeometryFilt:int=346
	kClusterFilter:int=347
	kSoftModFilter:int=348
	kJointCluster:int=349
	kDeltaMush:int=350
	kTension:int=351
	kMorph:int=352
	kSolidify:int=353
	kProximityWrap:int=354
	kWire:int=355
	kGroupId:int=356
	kGroupParts:int=357
	kGuide:int=358
	kHsvToRgb:int=359
	kHyperGraphInfo:int=360
	kHyperLayout:int=361
	kHyperView:int=362
	kIkSolver:int=363
	kMCsolver:int=364
	kPASolver:int=365
	kSCsolver:int=366
	kRPsolver:int=367
	kSplineSolver:int=368
	kIkSystem:int=369
	kImagePlane:int=370
	kLambert:int=371
	kReflect:int=372
	kBlinn:int=373
	kPhong:int=374
	kPhongExplorer:int=375
	kLayeredShader:int=376
	kStandardSurface:int=377
	kLightInfo:int=378
	kLeastSquares:int=379
	kLightFogMaterial:int=380
	kEnvFogMaterial:int=381
	kLightList:int=382
	kLightSource:int=383
	kLuminance:int=384
	kMakeGroup:int=385
	kMaterial:int=386
	kDiffuseMaterial:int=387
	kLambertMaterial:int=388
	kBlinnMaterial:int=389
	kPhongMaterial:int=390
	kLightSourceMaterial:int=391
	kMaterialInfo:int=392
	kMaterialTemplate:int=393
	kMatrixAdd:int=394
	kMatrixHold:int=395
	kMatrixMult:int=396
	kMatrixPass:int=397
	kMatrixWtAdd:int=398
	kMidModifier:int=399
	kMidModifierWithMatrix:int=400
	kPolyBevel:int=401
	kPolyTweak:int=402
	kPolyAppend:int=403
	kPolyChipOff:int=404
	kPolyCloseBorder:int=405
	kPolyCollapseEdge:int=406
	kPolyCollapseF:int=407
	kPolyCylProj:int=408
	kPolyDelEdge:int=409
	kPolyDelFacet:int=410
	kPolyDelVertex:int=411
	kPolyExtrudeFacet:int=412
	kPolyMapCut:int=413
	kPolyMapDel:int=414
	kPolyMapSew:int=415
	kPolyMergeEdge:int=416
	kPolyMergeFacet:int=417
	kPolyMoveEdge:int=418
	kPolyMoveFacet:int=419
	kPolyMoveFacetUV:int=420
	kPolyMoveUV:int=421
	kPolyMoveVertex:int=422
	kPolyMoveVertexUV:int=423
	kPolyNormal:int=424
	kPolyPlanProj:int=425
	kPolyProj:int=426
	kPolyQuad:int=427
	kPolySmooth:int=428
	kPolySoftEdge:int=429
	kPolySphProj:int=430
	kPolySplit:int=431
	kPolySubdEdge:int=432
	kPolySubdFacet:int=433
	kPolyTriangulate:int=434
	kPolyCreator:int=435
	kPolyPrimitive:int=436
	kPolyCone:int=437
	kPolyCube:int=438
	kPolyCylinder:int=439
	kPolyMesh:int=440
	kPolySphere:int=441
	kPolyTorus:int=442
	kPolyCreateFacet:int=443
	kPolyUnite:int=444
	kMotionPath:int=445
	kPluginMotionPathNode:int=446
	kMultilisterLight:int=447
	kMultiplyDivide:int=448
	kOldGeometryConstraint:int=449
	kOpticalFX:int=450
	kParticleAgeMapper:int=451
	kParticleCloud:int=452
	kParticleColorMapper:int=453
	kParticleIncandecenceMapper:int=454
	kParticleTransparencyMapper:int=455
	kPartition:int=456
	kPlace2dTexture:int=457
	kPlace3dTexture:int=458
	kPluginDependNode:int=459
	kPluginLocatorNode:int=460
	kPlusMinusAverage:int=461
	kPointMatrixMult:int=462
	kPolySeparate:int=463
	kPostProcessList:int=464
	kProjection:int=465
	kRecord:int=466
	kRenderUtilityList:int=467
	kReverse:int=468
	kRgbToHsv:int=469
	kRigidSolver:int=470
	kSet:int=471
	kTextureBakeSet:int=472
	kVertexBakeSet:int=473
	kSetRange:int=474
	kShaderGlow:int=475
	kShaderList:int=476
	kShadingMap:int=477
	kSamplerInfo:int=478
	kShapeFragment:int=479
	kSimpleVolumeShader:int=480
	kSl60:int=481
	kSnapshot:int=482
	kStoryBoard:int=483
	kSummaryObject:int=484
	kSuper:int=485
	kControl:int=486
	kSurfaceLuminance:int=487
	kSurfaceShader:int=488
	kTextureList:int=489
	kTextureEnv:int=490
	kEnvBall:int=491
	kEnvCube:int=492
	kEnvChrome:int=493
	kEnvSky:int=494
	kEnvSphere:int=495
	kTexture2d:int=496
	kBulge:int=497
	kChecker:int=498
	kCloth:int=499
	kFileTexture:int=500
	kFractal:int=501
	kGrid:int=502
	kMountain:int=503
	kRamp:int=504
	kStencil:int=505
	kWater:int=506
	kTexture3d:int=507
	kBrownian:int=508
	kCloud:int=509
	kCrater:int=510
	kGranite:int=511
	kLeather:int=512
	kMarble:int=513
	kRock:int=514
	kSnow:int=515
	kSolidFractal:int=516
	kStucco:int=517
	kTxSl:int=518
	kWood:int=519
	kTime:int=520
	kTimeToUnitConversion:int=521
	kRenderSetup:int=522
	kRenderGlobals:int=523
	kRenderGlobalsList:int=524
	kRenderQuality:int=525
	kResolution:int=526
	kHardwareRenderGlobals:int=527
	kArrayMapper:int=528
	kUnitConversion:int=529
	kUnitToTimeConversion:int=530
	kUseBackground:int=531
	kUnknown:int=532
	kVectorProduct:int=533
	kVolumeShader:int=534
	kComponent:int=535
	kCurveCVComponent:int=536
	kCurveEPComponent:int=537
	kCurveKnotComponent:int=538
	kCurveParamComponent:int=539
	kIsoparmComponent:int=540
	kPivotComponent:int=541
	kSurfaceCVComponent:int=542
	kSurfaceEPComponent:int=543
	kSurfaceKnotComponent:int=544
	kEdgeComponent:int=545
	kLatticeComponent:int=546
	kSurfaceRangeComponent:int=547
	kDecayRegionCapComponent:int=548
	kDecayRegionComponent:int=549
	kMeshComponent:int=550
	kMeshEdgeComponent:int=551
	kMeshPolygonComponent:int=552
	kMeshFrEdgeComponent:int=553
	kMeshVertComponent:int=554
	kMeshFaceVertComponent:int=555
	kOrientationComponent:int=556
	kSubVertexComponent:int=557
	kMultiSubVertexComponent:int=558
	kSetGroupComponent:int=559
	kDynParticleSetComponent:int=560
	kSelectionItem:int=561
	kDagSelectionItem:int=562
	kNonDagSelectionItem:int=563
	kItemList:int=564
	kAttribute:int=565
	kNumericAttribute:int=566
	kDoubleAngleAttribute:int=567
	kFloatAngleAttribute:int=568
	kDoubleLinearAttribute:int=569
	kFloatLinearAttribute:int=570
	kTimeAttribute:int=571
	kEnumAttribute:int=572
	kUnitAttribute:int=573
	kTypedAttribute:int=574
	kCompoundAttribute:int=575
	kGenericAttribute:int=576
	kLightDataAttribute:int=577
	kMatrixAttribute:int=578
	kFloatMatrixAttribute:int=579
	kMessageAttribute:int=580
	kOpaqueAttribute:int=581
	kPlugin:int=582
	kData:int=583
	kComponentListData:int=584
	kDoubleArrayData:int=585
	kIntArrayData:int=586
	kUintArrayData:int=587
	kLatticeData:int=588
	kMatrixData:int=589
	kMeshData:int=590
	kNurbsSurfaceData:int=591
	kNurbsCurveData:int=592
	kNumericData:int=593
	kData2Double:int=594
	kData2Float:int=595
	kData2Int:int=596
	kData2Short:int=597
	kData3Double:int=598
	kData3Float:int=599
	kData3Int:int=600
	kData3Short:int=601
	kPluginData:int=602
	kPointArrayData:int=603
	kMatrixArrayData:int=604
	kSphereData:int=605
	kStringData:int=606
	kStringArrayData:int=607
	kVectorArrayData:int=608
	kSelectionList:int=609
	kTransformGeometry:int=610
	kCommEdgePtManip:int=611
	kCommEdgeOperManip:int=612
	kCommEdgeSegmentManip:int=613
	kCommCornerManip:int=614
	kCommCornerOperManip:int=615
	kPluginDeformerNode:int=616
	kTorus:int=617
	kPolyBoolOp:int=618
	kSingleShadingSwitch:int=619
	kDoubleShadingSwitch:int=620
	kTripleShadingSwitch:int=621
	kNurbsSquare:int=622
	kAnisotropy:int=623
	kNonLinear:int=624
	kDeformFunc:int=625
	kDeformBend:int=626
	kDeformTwist:int=627
	kDeformSquash:int=628
	kDeformFlare:int=629
	kDeformSine:int=630
	kDeformWave:int=631
	kDeformBendManip:int=632
	kDeformTwistManip:int=633
	kDeformSquashManip:int=634
	kDeformFlareManip:int=635
	kDeformSineManip:int=636
	kDeformWaveManip:int=637
	kSoftModManip:int=638
	kDistanceManip:int=639
	kScript:int=640
	kCurveFromMeshEdge:int=641
	kCurveCurveIntersect:int=642
	kNurbsCircular3PtArc:int=643
	kNurbsCircular2PtArc:int=644
	kOffsetSurface:int=645
	kRoundConstantRadius:int=646
	kRoundRadiusManip:int=647
	kRoundRadiusCrvManip:int=648
	kRoundConstantRadiusManip:int=649
	kThreePointArcManip:int=650
	kTwoPointArcManip:int=651
	kTextButtonManip:int=652
	kOffsetSurfaceManip:int=653
	kImageData:int=654
	kImageLoad:int=655
	kImageSave:int=656
	kImageNetSrc:int=657
	kImageNetDest:int=658
	kImageRender:int=659
	kImageAdd:int=660
	kImageDiff:int=661
	kImageMultiply:int=662
	kImageOver:int=663
	kImageUnder:int=664
	kImageColorCorrect:int=665
	kImageBlur:int=666
	kImageFilter:int=667
	kImageDepth:int=668
	kImageDisplay:int=669
	kImageView:int=670
	kImageMotionBlur:int=671
	kViewColorManager:int=672
	kMatrixFloatData:int=673
	kSkinShader:int=674
	kComponentManip:int=675
	kSelectionListData:int=676
	kObjectFilter:int=677
	kObjectMultiFilter:int=678
	kObjectNameFilter:int=679
	kObjectTypeFilter:int=680
	kObjectAttrFilter:int=681
	kObjectRenderFilter:int=682
	kObjectScriptFilter:int=683
	kSelectionListOperator:int=684
	kSubdiv:int=685
	kPolyToSubdiv:int=686
	kSkinClusterFilter:int=687
	kKeyingGroup:int=688
	kCharacter:int=689
	kCharacterOffset:int=690
	kDagPose:int=691
	kStitchAsNurbsShell:int=692
	kExplodeNurbsShell:int=693
	kNurbsBoolean:int=694
	kStitchSrfManip:int=695
	kForceUpdateManip:int=696
	kPluginManipContainer:int=697
	kPolySewEdge:int=698
	kPolyMergeVert:int=699
	kPolySmoothFacet:int=700
	kSmoothCurve:int=701
	kGlobalStitch:int=702
	kSubdivCVComponent:int=703
	kSubdivEdgeComponent:int=704
	kSubdivFaceComponent:int=705
	kUVManip2D:int=706
	kTranslateUVManip2D:int=707
	kRotateUVManip2D:int=708
	kScaleUVManip2D:int=709
	kPolyTweakUV:int=710
	kMoveUVShellManip2D:int=711
	kPluginShape:int=712
	kGeometryData:int=713
	kSingleIndexedComponent:int=714
	kDoubleIndexedComponent:int=715
	kTripleIndexedComponent:int=716
	kExtendSurfaceDistanceManip:int=717
	kSquareSrf:int=718
	kSquareSrfManip:int=719
	kSubdivToPoly:int=720
	kDynBase:int=721
	kDynEmitterManip:int=722
	kDynFieldsManip:int=723
	kDynBaseFieldManip:int=724
	kDynAirManip:int=725
	kDynNewtonManip:int=726
	kDynTurbulenceManip:int=727
	kDynSpreadManip:int=728
	kDynAttenuationManip:int=729
	kDynArrayAttrsData:int=730
	kPluginFieldNode:int=731
	kPluginEmitterNode:int=732
	kPluginSpringNode:int=733
	kDisplayLayer:int=734
	kDisplayLayerManager:int=735
	kPolyColorPerVertex:int=736
	kCreateColorSet:int=737
	kDeleteColorSet:int=738
	kCopyColorSet:int=739
	kBlendColorSet:int=740
	kPolyColorMod:int=741
	kPolyColorDel:int=742
	kCharacterMappingData:int=743
	kDynSweptGeometryData:int=744
	kWrapFilter:int=745
	kMeshVtxFaceComponent:int=746
	kBinaryData:int=747
	kAttribute2Double:int=748
	kAttribute2Float:int=749
	kAttribute2Short:int=750
	kAttribute2Int:int=751
	kAttribute3Double:int=752
	kAttribute3Float:int=753
	kAttribute3Short:int=754
	kAttribute3Int:int=755
	kReference:int=756
	kBlindData:int=757
	kBlindDataTemplate:int=758
	kPolyBlindData:int=759
	kPolyNormalPerVertex:int=760
	kNurbsToSubdiv:int=761
	kPluginIkSolver:int=762
	kInstancer:int=763
	kMoveVertexManip:int=764
	kStroke:int=765
	kBrush:int=766
	kStrokeGlobals:int=767
	kPluginGeometryData:int=768
	kLightLink:int=769
	kDynGlobals:int=770
	kPolyReduce:int=771
	kLodThresholds:int=772
	kChooser:int=773
	kLodGroup:int=774
	kMultDoubleLinear:int=775
	kFourByFourMatrix:int=776
	kTowPointOnSurfaceManip:int=777
	kSurfaceEdManip:int=778
	kSurfaceFaceComponent:int=779
	kClipScheduler:int=780
	kClipLibrary:int=781
	kSubSurface:int=782
	kSmoothTangentSrf:int=783
	kRenderPass:int=784
	kRenderPassSet:int=785
	kRenderLayer:int=786
	kRenderLayerManager:int=787
	kPassContributionMap:int=788
	kPrecompExport:int=789
	kRenderTarget:int=790
	kRenderedImageSource:int=791
	kImageSource:int=792
	kPolyFlipEdge:int=793
	kPolyExtrudeEdge:int=794
	kAnimBlend:int=795
	kAnimBlendInOut:int=796
	kPolyAppendVertex:int=797
	kUvChooser:int=798
	kSubdivCompId:int=799
	kVolumeAxis:int=800
	kDeleteUVSet:int=801
	kSubdHierBlind:int=802
	kSubdBlindData:int=803
	kCharacterMap:int=804
	kLayeredTexture:int=805
	kSubdivCollapse:int=806
	kParticleSamplerInfo:int=807
	kCopyUVSet:int=808
	kCreateUVSet:int=809
	kClip:int=810
	kPolySplitVert:int=811
	kSubdivData:int=812
	kSubdivGeom:int=813
	kUInt64ArrayData:int=814
	kInt64ArrayData:int=815
	kPolySplitEdge:int=816
	kSubdivReverseFaces:int=817
	kMeshMapComponent:int=818
	kSectionManip:int=819
	kXsectionSubdivEdit:int=820
	kSubdivToNurbs:int=821
	kEditCurve:int=822
	kEditCurveManip:int=823
	kCrossSectionManager:int=824
	kCreateSectionManip:int=825
	kCrossSectionEditManip:int=826
	kDropOffFunction:int=827
	kSubdBoolean:int=828
	kSubdModifyEdge:int=829
	kModifyEdgeCrvManip:int=830
	kModifyEdgeManip:int=831
	kScalePointManip:int=832
	kTransformBoxManip:int=833
	kSymmetryLocator:int=834
	kSymmetryMapVector:int=835
	kSymmetryMapCurve:int=836
	kCurveFromSubdivEdge:int=837
	kCreateBPManip:int=838
	kModifyEdgeBaseManip:int=839
	kSubdExtrudeFace:int=840
	kSubdivSurfaceVarGroup:int=841
	kSfRevolveManip:int=842
	kCurveFromSubdivFace:int=843
	kUnused1:int=844
	kUnused2:int=845
	kUnused3:int=846
	kUnused4:int=847
	kUnused5:int=848
	kUnused6:int=849
	kPolyTransfer:int=850
	kPolyAverageVertex:int=851
	kPolyAutoProj:int=852
	kPolyLayoutUV:int=853
	kPolyMapSewMove:int=854
	kSubdModifier:int=855
	kSubdMoveVertex:int=856
	kSubdMoveEdge:int=857
	kSubdMoveFace:int=858
	kSubdDelFace:int=859
	kSnapshotShape:int=860
	kSubdivMapComponent:int=861
	kJiggleDeformer:int=862
	kGlobalCacheControls:int=863
	kDiskCache:int=864
	kSubdCloseBorder:int=865
	kSubdMergeVert:int=866
	kBoxData:int=867
	kBox:int=868
	kRenderBox:int=869
	kSubdSplitFace:int=870
	kVolumeFog:int=871
	kSubdTweakUV:int=872
	kSubdMapCut:int=873
	kSubdLayoutUV:int=874
	kSubdMapSewMove:int=875
	kOcean:int=876
	kVolumeNoise:int=877
	kSubdAutoProj:int=878
	kSubdSubdivideFace:int=879
	kNoise:int=880
	kAttribute4Double:int=881
	kData4Double:int=882
	kSubdPlanProj:int=883
	kSubdTweak:int=884
	kSubdProjectionManip:int=885
	kSubdMappingManip:int=886
	kHardwareReflectionMap:int=887
	kPolyNormalizeUV:int=888
	kPolyFlipUV:int=889
	kHwShaderNode:int=890
	kPluginHardwareShader:int=891
	kPluginHwShaderNode:int=892
	kSubdAddTopology:int=893
	kSubdCleanTopology:int=894
	kImplicitCone:int=895
	kImplicitSphere:int=896
	kRampShader:int=897
	kVolumeLight:int=898
	kOceanShader:int=899
	kBevelPlus:int=900
	kStyleCurve:int=901
	kPolyCut:int=902
	kPolyPoke:int=903
	kPolyWedgeFace:int=904
	kPolyCutManipContainer:int=905
	kPolyCutManip:int=906
	kPolyMirrorManipContainer:int=907
	kPolyPokeManip:int=908
	kFluidTexture3D:int=909
	kFluidTexture2D:int=910
	kPolyMergeUV:int=911
	kPolyStraightenUVBorder:int=912
	kAlignManip:int=913
	kPluginTransformNode:int=914
	kFluid:int=915
	kFluidGeom:int=916
	kFluidData:int=917
	kSmear:int=918
	kStringShadingSwitch:int=919
	kStudioClearCoat:int=920
	kFluidEmitter:int=921
	kHeightField:int=922
	kGeoConnector:int=923
	kSnapshotPath:int=924
	kPluginObjectSet:int=925
	kQuadShadingSwitch:int=926
	kPolyExtrudeVertex:int=927
	kPairBlend:int=928
	kTextManip:int=929
	kViewManip:int=930
	kXformManip:int=931
	kMute:int=932
	kConstraint:int=933
	kTrimWithBoundaries:int=934
	kCurveFromMeshCoM:int=935
	kFollicle:int=936
	kHairSystem:int=937
	kRemapValue:int=938
	kRemapColor:int=939
	kRemapHsv:int=940
	kHairConstraint:int=941
	kTimeFunction:int=942
	kMentalRayTexture:int=943
	kObjectBinFilter:int=944
	kPolySmoothProxy:int=945
	kPfxGeometry:int=946
	kPfxHair:int=947
	kHairTubeShader:int=948
	kPsdFileTexture:int=949
	kKeyframeDelta:int=950
	kKeyframeDeltaMove:int=951
	kKeyframeDeltaScale:int=952
	kKeyframeDeltaAddRemove:int=953
	kKeyframeDeltaBlockAddRemove:int=954
	kKeyframeDeltaInfType:int=955
	kKeyframeDeltaTangent:int=956
	kKeyframeDeltaWeighted:int=957
	kKeyframeDeltaBreakdown:int=958
	kPolyMirror:int=959
	kPolyCreaseEdge:int=960
	kPolyPinUV:int=961
	kHikEffector:int=962
	kHikIKEffector:int=963
	kHikFKJoint:int=964
	kHikSolver:int=965
	kHikHandle:int=966
	kProxyManager:int=967
	kPolyAutoProjManip:int=968
	kPolyPrism:int=969
	kPolyPyramid:int=970
	kPolySplitRing:int=971
	kPfxToon:int=972
	kToonLineAttributes:int=973
	kPolyDuplicateEdge:int=974
	kFacade:int=975
	kMaterialFacade:int=976
	kEnvFacade:int=977
	kAISEnvFacade:int=978
	kLineModifier:int=979
	kPolyArrow:int=980
	kPolyPrimitiveMisc:int=981
	kPolyPlatonicSolid:int=982
	kPolyPipe:int=983
	kHikFloorContactMarker:int=984
	kHikGroundPlane:int=985
	kPolyComponentData:int=986
	kPolyHelix:int=987
	kCacheFile:int=988
	kHistorySwitch:int=989
	kClosestPointOnMesh:int=990
	kUVPin:int=991
	kProximityPin:int=992
	kTransferAttributes:int=993
	kDynamicConstraint:int=994
	kNComponent:int=995
	kPolyBridgeEdge:int=996
	kCacheableNode:int=997
	kNucleus:int=998
	kNBase:int=999
	kCacheBase:int=1000
	kCacheBlend:int=1001
	kCacheTrack:int=1002
	kKeyframeRegionManip:int=1003
	kCurveNormalizerAngle:int=1004
	kCurveNormalizerLinear:int=1005
	kHyperLayoutDG:int=1006
	kPluginImagePlaneNode:int=1007
	kNCloth:int=1008
	kNParticle:int=1009
	kNRigid:int=1010
	kPluginParticleAttributeMapperNode:int=1011
	kCameraSet:int=1012
	kPluginCameraSet:int=1013
	kContainer:int=1014
	kFloatVectorArrayData:int=1015
	kNObjectData:int=1016
	kNObject:int=1017
	kPluginConstraintNode:int=1018
	kAsset:int=1019
	kPolyEdgeToCurve:int=1020
	kAnimLayer:int=1021
	kBlendNodeBase:int=1022
	kBlendNodeBoolean:int=1023
	kBlendNodeDouble:int=1024
	kBlendNodeDoubleAngle:int=1025
	kBlendNodeDoubleLinear:int=1026
	kBlendNodeEnum:int=1027
	kBlendNodeFloat:int=1028
	kBlendNodeFloatAngle:int=1029
	kBlendNodeFloatLinear:int=1030
	kBlendNodeInt16:int=1031
	kBlendNodeInt32:int=1032
	kBlendNodeAdditiveScale:int=1033
	kBlendNodeAdditiveRotation:int=1034
	kPluginManipulatorNode:int=1035
	kNIdData:int=1036
	kNId:int=1037
	kFloatArrayData:int=1038
	kMembrane:int=1039
	kMergeVertsToolManip:int=1040
	kUint64SingleIndexedComponent:int=1041
	kPolyToolFeedbackManip:int=1042
	kPolySelectEditFeedbackManip:int=1043
	kWriteToFrameBuffer:int=1044
	kWriteToColorBuffer:int=1045
	kWriteToVectorBuffer:int=1046
	kWriteToDepthBuffer:int=1047
	kWriteToLabelBuffer:int=1048
	kStereoCameraMaster:int=1049
	kSequenceManager:int=1050
	kSequencer:int=1051
	kShot:int=1052
	kBlendNodeTime:int=1053
	kCreateBezierManip:int=1054
	kBezierCurve:int=1055
	kBezierCurveData:int=1056
	kNurbsCurveToBezier:int=1057
	kBezierCurveToNurbs:int=1058
	kPolySpinEdge:int=1059
	kPolyHoleFace:int=1060
	kPointOnPolyConstraint:int=1061
	kPolyConnectComponents:int=1062
	kSkinBinding:int=1063
	kVolumeBindManip:int=1064
	kVertexWeightSet:int=1065
	kNearestPointOnCurve:int=1066
	kColorProfile:int=1067
	kAdskMaterial:int=1068
	kContainerBase:int=1069
	kDagContainer:int=1070
	kPolyUVRectangle:int=1071
	kHardwareRenderingGlobals:int=1072
	kPolyProjectCurve:int=1073
	kRenderingList:int=1074
	kPolyExtrudeManip:int=1075
	kPolyExtrudeManipContainer:int=1076
	kThreadedDevice:int=1077
	kClientDevice:int=1078
	kPluginClientDevice:int=1079
	kPluginThreadedDevice:int=1080
	kTimeWarp:int=1081
	kAssembly:int=1082
	kClipGhostShape:int=1083
	kClipToGhostData:int=1084
	kMandelbrot:int=1085
	kMandelbrot3D:int=1086
	kGreasePlane:int=1087
	kGreasePlaneRenderShape:int=1088
	kGreasePencilSequence:int=1089
	kEditMetadata:int=1090
	kCreaseSet:int=1091
	kPolyEditEdgeFlow:int=1092
	kFosterParent:int=1093
	kSnapUVManip2D:int=1094
	kToolContext:int=1095
	kNLE:int=1096
	kShrinkWrapFilter:int=1097
	kEditsManager:int=1098
	kPolyBevel2:int=1099
	kPolyCBoolOp:int=1100
	kGeomBind:int=1101
	kColorMgtGlobals:int=1102
	kPolyBevel3:int=1103
	kTimeEditorClipBase:int=1104
	kTimeEditorClipEvaluator:int=1105
	kTimeEditorClip:int=1106
	kTimeEditor:int=1107
	kTimeEditorTracks:int=1108
	kTimeEditorInterpolator:int=1109
	kTimeEditorAnimSource:int=1110
	kCaddyManipBase:int=1111
	kPolyCaddyManip:int=1112
	kPolyModifierManipContainer:int=1113
	kPolyRemesh:int=1114
	kPolyContourProj:int=1115
	kContourProjectionManip:int=1116
	kNodeGraphEditorInfo:int=1117
	kNodeGraphEditorBookmarks:int=1118
	kNodeGraphEditorBookmarkInfo:int=1119
	kPluginSkinCluster:int=1120
	kPluginGeometryFilter:int=1121
	kPluginBlendShape:int=1122
	kPolyPassThru:int=1123
	kTrackInfoManager:int=1124
	kPolyClean:int=1125
	kShapeEditorManager:int=1126
	kOceanDeformer:int=1127
	kPoseInterpolatorManager:int=1128
	kControllerTag:int=1129
	kReForm:int=1130
	kCustomEvaluatorClusterNode:int=1131
	kPolyCircularize:int=1132
	kArubaTesselate:int=1133
	kReorderUVSet:int=1134
	kUfeProxyTransform:int=1135
	kDecomposeMatrix:int=1136
	kComposeMatrix:int=1137
	kBlendMatrix:int=1138
	kPickMatrix:int=1139
	kAimMatrix:int=1140
	kPrimitiveFalloff:int=1141
	kBlendFalloff:int=1142
	kUniformFalloff:int=1143
	kTransferFalloff:int=1144
	kComponentFalloff:int=1145
	kProximityFalloff:int=1146
	kSubsetFalloff:int=1147
	kWeightFunctionData:int=1148
	kFalloffEval:int=1149
	kComponentMatch:int=1150
	kPolyUnsmooth:int=1151
	kPolySmartExtrude:int=1152
	kPolySmartExtrudeManip:int=1153
	kPolyReFormManipContainer:int=1154
	kPolyReFormManip:int=1155
	kPolyAxis:int=1156
	kAngleToDoubleNode:int=1157
	kDoubleToAngleNode:int=1158
	kAbsolute:int=1159
	kACos:int=1160
	kAnd:int=1161
	kASin:int=1162
	kATan:int=1163
	kATan2:int=1164
	kAverage:int=1165
	kCeil:int=1166
	kClampRange:int=1167
	kCos:int=1168
	kDeterminant:int=1169
	kEqual:int=1170
	kFloor:int=1171
	kGreaterThan:int=1172
	kInverseLinearInterpolation:int=1173
	kLength:int=1174
	kLessThan:int=1175
	kLinearInterpolation:int=1176
	kLog:int=1177
	kMax:int=1178
	kMin:int=1179
	kModulo:int=1180
	kMultiply:int=1181
	kNegate:int=1182
	kNormalize:int=1183
	kNot:int=1184
	kOr:int=1185
	kPIConstant:int=1186
	kPower:int=1187
	kRotateVector:int=1188
	kRound:int=1189
	kSin:int=1190
	kSmoothStep:int=1191
	kSum:int=1192
	kTan:int=1193
	kTruncate:int=1194
	kDotProduct:int=1195
	kCrossProduct:int=1196
	kMultiplyPointByMatrix:int=1197
	kMultiplyVectorByMatrix:int=1198
	kAxisFromMatrix:int=1199
	kDivide:int=1200
	kSubtract:int=1201
	kTranslationFromMatrix:int=1202
	kRowFromMatrix:int=1203
	kColumnFromMatrix:int=1204
	kScaleFromMatrix:int=1205
	kRotationFromMatrix:int=1206
	kParentMatrix:int=1207
	kPolySmartBevel:int=1208
	kOpenPBRSurface:int=1209
	kAnimInContextNode:int=1210
class MFnAssembly(MFnDagNode):
	"""Function set for assemblies."""
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	@staticmethod
	def getTopLevelAssemblies()->MObjectArray:
		"""getTopLevelAssemblies() -> MObjectArray

		Returns a list containing top-level assemblies. These are assembliesthat are not nested inside another assembly."""
	@overload
	def createRepresentation(self,input:Any,type:Any,undoRedo:Any=...)->str:
		"""createRepresentation(input, type[, undoRedo]) -> MString
		createRepresentation(input, type, representation[, undoRedo]) -> MString


		Create a representation and add it to the list of those managed by this node.
		The input argument string is used as input data to the representation creation process. The semantics of this input are defined by the assembly derived class.
		The type of the representation is a property of the representation that expresses its commonality with other representations of this assembly type, for example a "Bounding Box" representation type. See the getRepType() method.
		If specified, the representation argument is used as a starting point for the representation name. This string value can be modified to meet uniqueness, or other constraints.
		The representation return value string is the representation name, after it has been added.

		* input          - Input data for representation creation.
		* type           - Type of representation to create.
		* representation - Representation name starting point.
		* undoRedo       - Optional MDagModifier object, for undo/redo purposes."""
	@overload
	def createRepresentation(self,input:Any,type:Any,representation:Any,undoRedo:Any=...)->str:
		"""createRepresentation(input, type[, undoRedo]) -> MString
		createRepresentation(input, type, representation[, undoRedo]) -> MString


		Create a representation and add it to the list of those managed by this node.
		The input argument string is used as input data to the representation creation process. The semantics of this input are defined by the assembly derived class.
		The type of the representation is a property of the representation that expresses its commonality with other representations of this assembly type, for example a "Bounding Box" representation type. See the getRepType() method.
		If specified, the representation argument is used as a starting point for the representation name. This string value can be modified to meet uniqueness, or other constraints.
		The representation return value string is the representation name, after it has been added.

		* input          - Input data for representation creation.
		* type           - Type of representation to create.
		* representation - Representation name starting point.
		* undoRedo       - Optional MDagModifier object, for undo/redo purposes."""
	def getRepresentations(self)->list[str]:
		"""getRepresentations() -> [MString]

		Returns an array of the representations managed by the node attached to this function set."""
	def getParentAssembly(self)->MObject:
		"""getParentAssembly() -> MObject

		Return the immediate parent assembly of this assembly if there is one, otherwise returns None. An assembly with no parent is a top level assembly."""
	def getSubAssemblies(self)->MObjectArray:
		"""getSubAssemblies() -> MObjectArray

		Returns a list containing direct children of this assembly that are themselves assemblies, for the currently active representation. The returned list will be empty if there are no assembly children of the currently active representation."""
	def postLoad(self)->Self:
		"""postLoad() -> self

		Initialize assemblies after their creation.
		In general, postLoad() does not need to be called explicity by a plugin. Maya will call it automatically on any assembly node created by representation activation, to initialize the assembly node.
		However, if an existing assembly needs to be re-initialized, because of a parameter change for example, the representation activation code path is obviously not involved. In such a case, the postLoad() re-initialization can be done by calling this method explicitly, so that Maya is made aware that the node is being re-initialized, and that for example, no edits should be recorded during this re-initialization."""
	def activate(self,arg:list[representation])->Self:
		"""activate([representation]) -> self

		Activate a representation. The representation to activate is specified as a string name. If no representation is specified then the previously-active representation (if any) will be inactivated and no representation will be active. This method will fail if canActivate() returns False.

		* representation - representation to activate."""
	def getActive(self)->str:
		"""getActive() -> MString

		Get the active representation in the list of representations. If the list of representations is empty, the return string will be empty."""
	def activateNonRecursive(self,arg:list[representation])->Self:
		"""activateNonRecursive([representation]) -> self

		Activate a representation, but prevent any nested assemblies created and initialized during this activation from activating any of their representations.

		Normal activation of a representation can create nested assemblies in the representation.  Maya will call MPxAssembly::postLoad() automatically on these nested assemblies to initialize them.  This initialization of nested assemblies can, in turn, call activate on a representation. activateNonRecursive() causes canActivate() to return False on these nested assemblies.  An implementation of MPxAssembly::postLoad() should check canActivate() to determine whether it can activate a representation. Stopping the activation at the current assembly prunes recursive activation of representations.

		If canActivate() is False, activateNonRecursive() will return failure.

		The representation is specified as a string identifier.  Passing in an empty string argument means inactivate the previously-active representation (if any), and activate no representation.  * representation - Representation to activate."""
	def canActivate(self)->bool:
		"""canActivate() -> bool

		Determines whether this assembly can activate a representation, for the node attached to this function set. For example, this method will return False for a nested assembly, during a call to activateNonRecursive() on the parent assembly. If canActivate() returns False, activate() and activateNonRecursive() will fail."""
	def isActive(self,representation:Any)->bool:
		"""isActive(representation) -> bool

		Determines whether the given representation is the active representation for the node attached to this function set.

		* representation - Representation to query."""
	def getInitialRep(self)->tuple[str,bool]:
		"""getInitialRep() -> (MString, bool)

		Get the initial representation to use when the assembly is first loaded.

		This method returns the representation which should be activated when the assembly is first initialized and a boolean that indicates whether the assembly has an initial representation. If both an empty string and True is returned it means that assembly has been explicitly set to have no initial representation"""
	def getRepType(self,representation:Any)->str:
		"""getRepType(representation) -> MString

		Get the type of the specified representation. The type string does not have to be user-readable, and does not have to be localized; the type label should be used for UI purposes. If the specified representation is not found in this assembly, an empty string is returned.

		* representation - Representation whose type must be returned."""
	def getRepLabel(self,representation:Any)->str:
		"""getRepLabel(representation) -> MString

		Get the label of the specified representation. The label of a representation is a string that is meant to be shown in the UI and identify the representation meaningfully to a user. The representation label should support localization requirements. If the specified representation is not found in this assembly, an empty string is returned.

		* representation - Representation whose label must be returned."""
	def setRepName(self,representation:Any,newName:str)->str:
		"""setRepName(representation, newName) -> MString

		Rename a representation. The newName argument is used as a starting point for the new representation name. This string value can be modified by the derived implementation to meet representation name uniqueness, or other constraints. This method returns the final representation name.

		* representation - Current representation name.
		* newName        - New representation name starting point.
		* status         - Return status.

		Returns new representation name."""
	def setRepLabel(self,representation:Any,label:Any)->Self:
		"""setRepLabel(representation, label) -> self

		Change the representation label.

		* representation - Representation name.
		* label          - New representation label."""
	def repTypes(self)->list[str]:
		"""repTypes() -> [MString]

		Return the list of representation types that can be created for this assembly node."""
	def canRepApplyEdits(self,representation:Any)->bool:
		"""canRepApplyEdits(representation) -> bool

		Determines whether the given representation can apply edits to its data, for the node attached to this function set. If an empty string is passed in as the representation name, this method will return False, since an invalid (or 'None') representation does not have any data and thus, cannot have edits applied to it.

		* representation - Representation to query.
		* status         - Return status.

		Returns True if the representation can apply edits, False otherwise."""
	def deleteRepresentation(self,representation:Any)->Self:
		"""deleteRepresentation(representation) -> self

		Delete a representation managed by the node attached to this function set."""
	def deleteAllRepresentations(self)->Self:
		"""deleteAllRepresentations() -> self

		Delete all representations managed by the node attached to this function set."""
	def isTopLevel(self)->bool:
		"""isTopLevel() -> bool

		Returns whether this assembly node is a top-level assembly. An assembly node is a top-level assembly if no container in its (possibly empty) chain of nesting parent containers is an assembly. Of course, this includes the trivial case of its immediate parent container being null.

		Returns True if the assembly node is a top-level assembly."""
	def supportsEdits(self)->bool:
		"""supportsEdits() -> bool

		Returns True if this assembly supports tracking of edits on its nodes."""
	def supportsMemberChanges(self)->bool:
		"""supportsMemberChanges() -> bool

		If the assembly does not use Maya's edit tracking system (see supportsEdits()), does it support changes to its member nodes, outside of activation? If so, this means that any mutatingoperation on Maya nodes (parenting, connecting, disconnecting, renaming, deleting, setting attributes, adding attributes, removing attributes, locking) can be performed on member nodes of the assembly.

		This method is only used if supportsEdits() returns False. If supportsEdits() returns True, Maya will track edits to assembly members, and the return value of supportsMemberChanges() will have no meaning.When this method returns False, any mutating operation to member nodes of the assembly is prevented, and the assembly behaves as a read-only container of nodes. When this method returns True, the assembly supports changes to its member nodes.

		This predicate is only used outside of representation activation. During activation, all types of changes to the assembly's members are allowed, including of course deleting the previous representation's nodes, and creating nodes for the new representation.

		Returns True if the assembly supports changes to its nodes"""
	def getRepNamespace(self)->str:
		"""getRepNamespace() -> MString

		Get the representations namespace of this assembly node. This is the namespace where nodes created by the activation of a representation will be added. This namespace is shared by all representations. The name can be updated by Maya if a name clash occurs when the namespace is added to its parent namespace (see MPxAssembly::updateRepNamespace() for details).

		Returns the namespace for representations."""
	def importFile(self,fileName:str,type:Any=...,preserveReferences:Any=...,nameSpace:Any=...,ignoreVersion:Any=...)->Self:
		"""importFile(fileName[, type][, preserveReferences][, nameSpace][, ignoreVersion]) -> self

		Import the scene elements from the given file into this assembly. See MFileIO::importFile() for more information.  All elements imported from the file become members of the assembly. DAG nodes in the imported file that are parented to world are parented to the assembly. DAG nodes in the imported file whose parent is not world keep their existing parenting relationship.

		* fileName           - name of the file from which to import objects
		* type               - if not specified, Maya will try to deduce the type of the
		                       file. If specified, it must contain a file type to use
		                       when importing the file.
		* preserveReferences - Boolean to indicate whether the
		                       references need to be preserved.
		* nameSpace          - optional name of the namespace to use when importing
		                       objects. If empty defaults tp no namespace.
		* ignoreVersion      - Boolean to control whether to ignore version when
		                       importing a file."""
	def getAbsoluteRepNamespace(self)->str:
		"""getAbsoluteRepNamespace() -> MString

		Get the fully-qualified (absolute) namespace for representations of this assembly node. This is the namespace where nodes created by the activation of a representation will be added. This namespace is shared by all representations.

		This namespace starts at the root namespace, contains the namespace of the assembly node, and ends (inclusively) with the representation namespace.

		Two namespaces are optionally involved when dealing with an assembly node: the namespace of the assembly node itself, and the namespace of its representations. The representation namespace is a child of its assembly node's namespace. The assembly node's namespace is set by its containing assembly, if it is nested, or by the top-level file. Either the assembly node's namespace, or the representation namespace, or both, can be the empty string.

		It should be noted that if the assembly node is nested, the assembly node's namespace will be (by virtue of its nesting) the representation namespace of its containing assembly.

		Returns the fully-qualified (absolute) namespace for representations of this assembly node. The name can be empty if the namespace has not been created yet."""
	def handlesAddEdits(self)->bool:
		"""handlesAddEdits() -> bool

		Determines whether the assembly supplies edits to its data, for the node attached to this function set.

		If this method returns True, Maya will call MPxAssembly::addEdits(). These edits will later be applied, either by Maya, or by the assembly through MPxAssembly::applyEdits(), if MPxAssembly::handlesApplyEdits() returns True.

		Adding edits can be done by a plugin that implements its own persistency scheme. When an assembly node is brought into Maya through activation of a representation, this assembly can carry edits and make them known to Maya through the addEdits() method.

		Edits can be added for any node in the assembly's representations, which includes edits to any nested assembly of this assembly. In a scene with multiple levels of nested assemblies, if more than one nested assembly has edits to a given lower-level nested assembly, edits are applied by Maya starting at the most nested assembly level, moving up the chain of nesting assemblies. In this way, the most nested assembly's edit are overridden by less nested assembly edits, if they edit the same attribute or connection.

		Returns True if the assembly adds edits, False if no edits are added."""
class MFnAttribute(MFnBase):
	"""Base class for attribute functionsets."""
	@property
	def affectsAppearance(self)->bool:
		"""Does the attribute affect how the node is drawn in Maya's viewport?"""
	@affectsAppearance.setter
	def affectsAppearance(self,value:bool)->None:...
	@property
	def isProxyAttribute(self)->Any:
		"""Does the attribute is a proxy attribute?"""
	@isProxyAttribute.setter
	def isProxyAttribute(self,value:Any)->None:...
	@property
	def affectsWorldSpace(self)->bool:
		"""Does the attribute affect the node's worldSpace matrix?"""
	@affectsWorldSpace.setter
	def affectsWorldSpace(self,value:bool)->None:...
	@property
	def array(self)->bool:
		"""Is the attribute an array?"""
	@array.setter
	def array(self,value:bool)->None:...
	@property
	def cached(self)->bool:
		"""Should the attribute's value be cached in the datablock?"""
	@cached.setter
	def cached(self,value:bool)->None:...
	@property
	def channelBox(self)->bool:
		"""Should the attribute be displayed in the Channel Box?"""
	@channelBox.setter
	def channelBox(self,value:bool)->None:...
	@property
	def connectable(self)->bool:
		"""Can connections be made to the attribute?"""
	@connectable.setter
	def connectable(self,value:bool)->None:...
	@property
	def disconnectBehavior(self)->int:
		"""What should happen when the attribute loses an incoming connection?"""
	@disconnectBehavior.setter
	def disconnectBehavior(self,value:int)->None:...
	@property
	def dynamic(self)->bool:
		"""Is the attribute a dynamic attribute?"""
	@property
	def extension(self)->bool:
		"""Is the attribute an extension attribute?"""
	@property
	def hidden(self)->bool:
		"""If True the attribute will not be displayed in the Attribute Editor."""
	@hidden.setter
	def hidden(self,value:bool)->None:...
	@property
	def indeterminant(self)->bool:
		"""Hint to DG that this attribute may not always be used when computing the attributes which are dependent upon it."""
	@indeterminant.setter
	def indeterminant(self,value:bool)->None:...
	@property
	def indexMatters(self)->bool:
		"""If False, connectAttr -nextAvailable can be used with this attribute. If True then an explicit index must be provided."""
	@indexMatters.setter
	def indexMatters(self,value:bool)->None:...
	@property
	def internal(self)->bool:
		"""Will the node handle the attribute's data storage itself, outside of the node's data block?"""
	@internal.setter
	def internal(self,value:bool)->None:...
	@property
	def keyable(self)->bool:
		"""Can keys be set on the attribute?"""
	@keyable.setter
	def keyable(self,value:bool)->None:...
	@property
	def name(self)->str:
		"""Attribute's long name."""
	@property
	def parent(self)->MObject:
		"""Parent attribute. MObject::kNullObj if attr has no parent."""
	@parent.setter
	def parent(self,value:MObject)->None:...
	@property
	def readable(self)->bool:
		"""Is the attribute readable?"""
	@readable.setter
	def readable(self,value:bool)->None:...
	@property
	def renderSource(self)->bool:
		"""Is the attribute a render source?"""
	@renderSource.setter
	def renderSource(self,value:bool)->None:...
	@property
	def shortName(self)->str:
		"""Attribute's short name."""
	@property
	def storable(self)->bool:
		"""Should the attribute's value be preserved when the node is written to file?"""
	@storable.setter
	def storable(self,value:bool)->None:...
	@property
	def usedAsColor(self)->bool:
		"""Should the attribute be treated as a color in the UI?"""
	@usedAsColor.setter
	def usedAsColor(self,value:bool)->None:...
	@property
	def usedAsFilename(self)->bool:
		"""Should the attribute be treated as a file name in the UI?"""
	@usedAsFilename.setter
	def usedAsFilename(self,value:bool)->None:...
	@property
	def usesArrayDataBuilder(self)->bool:
		"""Array attributes only: does the attribute create elements using MArrayDataBuilder?"""
	@usesArrayDataBuilder.setter
	def usesArrayDataBuilder(self,value:bool)->None:...
	@property
	def worldSpace(self)->bool:
		"""DAG nodes only: if the node is instanced, will the attribute have separate values for each instance?"""
	@worldSpace.setter
	def worldSpace(self,value:bool)->None:...
	@property
	def writable(self)->bool:
		"""Is the attribute writable?"""
	@writable.setter
	def writable(self,value:bool)->None:...
	@property
	def enforcingUniqueName(self)->Any:
		"""Is the attribute enforcing to have a unique name?"""
	@enforcingUniqueName.setter
	def enforcingUniqueName(self,value:Any)->None:...
	kDelete:int=0
	kReset:int=1
	kNothing:int=2
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def acceptsAttribute(self,*args)->Any:
		"""Returns True if this attribute can accept a connection with the given attribute."""
	def accepts(self,type:MTypeId|int)->bool:
		"""Returns True if this attribute can accept a connection of the given type."""
	def addToCategory(self,*args)->Any:
		"""Adds the attribute to a category"""
	def getAddAttrCmd(self,longFlags:bool=False)->str:
		"""Returns a string containing the addAttr command which would be required to recreate the attribute. The command includes the terminating semicolon and is formatted as if for use with a selected node, meaning that it contains no node name. If longFlags is True then the long flag names will be used, otherwise their short names will be used."""
	def pathName(self,*args)->Any:
		"""Returns the pathName for the attribute."""
	def hasCategory(self,*args)->Any:
		"""Checks to see if the attribute has a given category"""
	def setNiceNameOverride(self,*args)->Any:
		"""Sets a nice UI name for this attribute rather than using the default derived from it's long name."""
class MFnBase:
	"""Base class for function sets."""
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	@overload
	def hasObj(self,type:int)->bool:
		"""True if the function set is compatible with the specified type of Maya object."""
	@overload
	def hasObj(self,object:MObject)->bool:
		"""True if the function set is compatible with the specified Maya object ."""
	def object(self)->MObject:
		"""Returns a reference to the object to which the function set is currently attached, or MObject.kNullObj if none."""
	def setObject(self,object:MObject)->Self:
		"""Attaches the function set to the specified Maya object ."""
	def type(self)->int:
		"""Returns the type of the function set."""
class MFnCamera(MFnDagNode):
	"""Function set for cameras."""
	@property
	def horizontalFilmAperture(self)->Any:
		"""The horizontal film aperture for the camera."""
	@horizontalFilmAperture.setter
	def horizontalFilmAperture(self,value:Any)->None:...
	@property
	def verticalFilmAperture(self)->Any:
		"""The vertical film aperture for the camera."""
	@verticalFilmAperture.setter
	def verticalFilmAperture(self,value:Any)->None:...
	@property
	def isVerticalLock(self)->Any:
		"""Determines if vertical lock is turned on for the camera."""
	@isVerticalLock.setter
	def isVerticalLock(self,value:Any)->None:...
	@property
	def horizontalFilmOffset(self)->Any:
		"""The horizontal offset of the film. Unit used is inches."""
	@horizontalFilmOffset.setter
	def horizontalFilmOffset(self,value:Any)->None:...
	@property
	def verticalFilmOffset(self)->Any:
		"""The vertical offset of the film. Unit used is inches."""
	@verticalFilmOffset.setter
	def verticalFilmOffset(self,value:Any)->None:...
	@property
	def shakeEnabled(self)->Any:
		"""The toggle value for the camera shake enabled attribute.
		If this attribute is False, the horizontalShake and verticalShake values are ignored by the camera."""
	@shakeEnabled.setter
	def shakeEnabled(self,value:Any)->None:...
	@property
	def horizontalShake(self)->Any:
		"""The horizontal offset of the film due to the shake attribute. Unit used is inches."""
	@horizontalShake.setter
	def horizontalShake(self,value:Any)->None:...
	@property
	def verticalShake(self)->Any:
		"""The vertical film-based camera shake value. Unit used is inches."""
	@verticalShake.setter
	def verticalShake(self,value:Any)->None:...
	@property
	def shakeOverscanEnabled(self)->Any:
		"""The toggle value for the camera shake overscan attribute.
		If this attribute is False, the shakeOverscan value is ignored by the camera."""
	@shakeOverscanEnabled.setter
	def shakeOverscanEnabled(self,value:Any)->None:...
	@property
	def shakeOverscan(self)->Any:
		"""The camera shake overscan value. Unit is a multiplier to the film aperture."""
	@shakeOverscan.setter
	def shakeOverscan(self,value:Any)->None:...
	@property
	def panZoomEnabled(self)->Any:
		"""The toggle value for the camera 2D pan/zoom enabled attribute.
		If this attribute is False, the 2D pan/zoom values are ignored by the camera."""
	@panZoomEnabled.setter
	def panZoomEnabled(self,value:Any)->None:...
	@property
	def renderPanZoom(self)->Any:
		"""The toggle value for the camera render 2D pan/zoom attribute.
		If this attribute is False, the 2D pan/zoom values will not affect the output render."""
	@renderPanZoom.setter
	def renderPanZoom(self,value:Any)->None:...
	@property
	def horizontalPan(self)->Any:
		"""The camera 2D horizontal pan value. Unit is inches."""
	@horizontalPan.setter
	def horizontalPan(self,value:Any)->None:...
	@property
	def verticalPan(self)->Any:
		"""The camera 2D vertical pan value. Unit is inches."""
	@verticalPan.setter
	def verticalPan(self,value:Any)->None:...
	@property
	def zoom(self)->Any:
		"""The camera 2D zoom value, which is the percent over the film viewable frustum to display"""
	@zoom.setter
	def zoom(self,value:Any)->None:...
	@property
	def stereoHITEnabled(self)->Any:
		"""The toggle value for the stereo HIT enabled attribute.
		If this attribute is False, the stereoHIT value is ignored by the camera."""
	@stereoHITEnabled.setter
	def stereoHITEnabled(self,value:Any)->None:...
	@property
	def stereoHIT(self)->Any:
		"""The camera stereo horizontal image translation (stereo HIT) value.  Unit is inches."""
	@stereoHIT.setter
	def stereoHIT(self,value:Any)->None:...
	@property
	def filmFit(self)->Any:
		"""How the digital image is to be fitted to the film back.
		Valid values:
		* kFillFilmFit           The system calculates both horizontal and vertical fits and then applies the one that makes the digital image larger than the film back.
		* kHorizontalFilmFit     The digital image is made to fit the film back exactly in the horizontal direction. This then gives each pixel a horizontal size = (film back width) / (horizontal resolution). The pixel height is then = (pixel width) / (pixel aspect ratio). Now that the pixel has a size, resolution gives us a complete image. That image will match the film back exactly in width. It will almost never match in height, either being too tall or too short. By playing with the numbers you can get it pretty close though.
		* kVerticalFilmFit       The same idea as horizontal fit, only applied vertically. Thus the digital image will match the film back exactly in height, but miss in width.
		* kOverscanFilmFit       Over-scanning the film gate in the camera view allows us to choreograph action outside of the frustum from within the camera view without having to resort to a dolly or zoom. This feature is also essential for animating image planes."""
	@filmFit.setter
	def filmFit(self,value:Any)->None:...
	@property
	def filmFitOffset(self)->Any:
		"""The film fit offset for the camera."""
	@filmFitOffset.setter
	def filmFitOffset(self,value:Any)->None:...
	@property
	def overscan(self)->Any:
		"""The percent of overscan for this camera."""
	@overscan.setter
	def overscan(self,value:Any)->None:...
	@property
	def horizontalRollPivot(self)->Any:
		"""The horizontal roll pivot for film back roll."""
	@horizontalRollPivot.setter
	def horizontalRollPivot(self,value:Any)->None:...
	@property
	def verticalRollPivot(self)->Any:
		"""The vertical roll pivot for film back roll."""
	@verticalRollPivot.setter
	def verticalRollPivot(self,value:Any)->None:...
	@property
	def filmRollValue(self)->Any:
		"""The film roll value for film back."""
	@filmRollValue.setter
	def filmRollValue(self,value:Any)->None:...
	@property
	def filmRollOrder(self)->Any:
		"""The order in which the film back rotation is applied with respect to the pivot point.
		Valid values:
		* kRotateTranslate      The film back is first rotated before it is translated by the pivot value.
		* kTranslateRotate      The film back is translated by the pivot before it is rotated."""
	@filmRollOrder.setter
	def filmRollOrder(self,value:Any)->None:...
	@property
	def preScale(self)->Any:
		"""The post projection matrix's pre-scale value."""
	@preScale.setter
	def preScale(self,value:Any)->None:...
	@property
	def postScale(self)->Any:
		"""The post projection matrix's post-scale value."""
	@postScale.setter
	def postScale(self,value:Any)->None:...
	@property
	def filmTranslateH(self)->Any:
		"""The horizontal film translate value.  This value corresponds to the normalized viewport."""
	@filmTranslateH.setter
	def filmTranslateH(self,value:Any)->None:...
	@property
	def filmTranslateV(self)->Any:
		"""The vertical film translate value. This value corresponds to the normalized viewport, [-1,1]."""
	@filmTranslateV.setter
	def filmTranslateV(self,value:Any)->None:...
	@property
	def isDisplayGateMask(self)->Any:
		"""Whether or not the film gate is displayed shaded."""
	@isDisplayGateMask.setter
	def isDisplayGateMask(self,value:Any)->None:...
	@property
	def isDisplayFilmGate(self)->Any:
		"""Whether or not the film gate icons are displayed when looking through the camera."""
	@isDisplayFilmGate.setter
	def isDisplayFilmGate(self,value:Any)->None:...
	@property
	def focalLength(self)->Any:
		"""The focal length for the camera.
		This is the distance along the lens axis between the lens and the film plane when "focal distance" is infinitely large. This is an optical property of the lens. Specified in millimeters."""
	@focalLength.setter
	def focalLength(self,value:Any)->None:...
	@property
	def lensSqueezeRatio(self)->Any:
		"""The lens squeeze ratio for the camera"""
	@lensSqueezeRatio.setter
	def lensSqueezeRatio(self,value:Any)->None:...
	@property
	def isClippingPlanes(self)->Any:
		"""Whether or not manual clipping planes are activated."""
	@isClippingPlanes.setter
	def isClippingPlanes(self,value:Any)->None:...
	@property
	def nearClippingPlane(self)->Any:
		"""The distance to the near clipping plane."""
	@nearClippingPlane.setter
	def nearClippingPlane(self,value:Any)->None:...
	@property
	def farClippingPlane(self)->Any:
		"""The distance to the far clipping plane."""
	@farClippingPlane.setter
	def farClippingPlane(self,value:Any)->None:...
	@property
	def isDepthOfField(self)->Any:
		"""Whether or not the depth of field calculation is performed for the camera."""
	@isDepthOfField.setter
	def isDepthOfField(self,value:Any)->None:...
	@property
	def fStop(self)->Any:
		"""The f-stop value for the camera."""
	@fStop.setter
	def fStop(self,value:Any)->None:...
	@property
	def focusDistance(self)->Any:
		"""The focus distance for the camera. This value sets the focus at a certain distance in front of the camera."""
	@focusDistance.setter
	def focusDistance(self,value:Any)->None:...
	@property
	def nearFocusDistance(self)->Any:
		"""The nearest distance within the well-focus region"""
	@nearFocusDistance.setter
	def nearFocusDistance(self,value:Any)->None:...
	@property
	def farFocusDistance(self)->Any:
		"""The farthest distance within the well-focus region"""
	@farFocusDistance.setter
	def farFocusDistance(self,value:Any)->None:...
	@property
	def isMotionBlur(self)->Any:
		"""Wheter or not motion blur is on/off for the camera."""
	@isMotionBlur.setter
	def isMotionBlur(self,value:Any)->None:...
	@property
	def shutterAngle(self)->Any:
		"""The shutter angle which is one of the variables used to compute motion blur. The shutter angle is specified in radians."""
	@shutterAngle.setter
	def shutterAngle(self,value:Any)->None:...
	@property
	def centerOfInterest(self)->Any:
		"""The linear distance from the camera's eye point to the center of interest."""
	@centerOfInterest.setter
	def centerOfInterest(self,value:Any)->None:...
	@property
	def orthoWidth(self)->Any:
		"""The orthographic projection width."""
	@orthoWidth.setter
	def orthoWidth(self,value:Any)->None:...
	@property
	def cameraScale(self)->Any:
		"""The camera scale."""
	@cameraScale.setter
	def cameraScale(self,value:Any)->None:...
	@property
	def tumblePivot(self)->Any:
		"""The tumble pivot value for the camera. The pivot value will be in world space coordinates unless usePivotAsLocalSpace is True in which case the pivot is a relative offset."""
	@tumblePivot.setter
	def tumblePivot(self,value:Any)->None:...
	@property
	def usePivotAsLocalSpace(self)->Any:
		"""The local axis tumble setting for this camera.True if using local space tumbling for this camera, or False if using the current global tumble setting in Maya."""
	@usePivotAsLocalSpace.setter
	def usePivotAsLocalSpace(self,value:Any)->None:...
	kFillFilmFit:int=0
	kHorizontalFilmFit:int=1
	kVerticalFilmFit:int=2
	kOverscanFilmFit:int=3
	kInvalid:int=4
	kRotateTranslate:int=0
	kTranslateRotate:int=1
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def aspectRatio(self)->float:
		"""aspectRatio() -> float

		Returns the aspect ratio for the camera."""
	def centerOfInterestPoint(self,space:int=MSpace.kObject)->MPoint:
		"""centerOfInterestPoint(space=kObject) -> MPoint

		Returns the center of interest point for the camera.

		* space (int) - Specifies the coordinate system for this operation"""
	def computeDepthOfField(self,nearLimit:float|None=None)->Self:
		"""computeDepthOfField(nearLimit=None) -> self

		Compute the depth of field

		* nearLimit (float) - the near limit"""
	def copyViewFrom(self,otherCamera:MDagPath)->Self:
		"""copyViewFrom(otherCamera) -> self

		Copy the camera settings related to the perspective from the given camera view.

		This method will only work when the world space information for the camera is available, i.e. when the function set has been initialized with a DAG path.

		* otherCamera (MDagPath) - Camera to copy view from"""
	def create(self,parent:MObject|None=None)->MObject:
		"""create(parent=None) -> MObject

		Creates a perspective camera. A parent can be specified for the new camera, otherwise a transform is created.

		The camera is positioned at (0, 0, 0), its center of interest at (0, 0, -1), which implies that the view-direction is pointing in the direction of the negative z-axis, and its up-direction along the positive Y axis.

		* parent (MObject) - The parent of the new camera"""
	def eyePoint(self,space:int=MSpace.kObject)->MPoint:
		"""eyePoint(space=kObject) -> MPoint

		Returns the eye point for the camera.

		* space (int) - Specifies the coordinate system for this operation"""
	def getAspectRatioLimits(self)->tuple[float,float]:
		"""getAspectRatioLimits() -> (float, float)

		Returns the minimum and maximum aspect ratio limits for the camera."""
	def getFilmApertureLimits(self)->tuple[float,float]:
		"""getFilmApertureLimits() -> (float, float)

		Returns the maximum and minimum film aperture limits for the camera."""
	def getFilmFrustum(self,distance:float,applyPanZoom:bool=False)->tuple[float,float,float,float]:
		"""getFilmFrustum(distance, applyPanZoom=False) -> (float, float, float, float)

		Returns the film frustum for the camera (horizontal size, vertical size, horizontal offset and vertical offset). The frustum defines the projective transformation.

		* distance (float) - Specifies the focal length
		* applyPanZoom (bool) - specifies whether to apply 2D pan/zoom"""
	def getFilmFrustumCorners(self,distance:float,applyPanZoom:bool=False)->MPointArray:
		"""getFilmFrustumCorners(distance, applyPanZoom=False) -> MPointArray

		Returns the film frustum for the camera. The frustum defines the projective transformation.

		 element 0 is the bottom left
		 element 1 is the top left
		 element 2 is the top right
		 element 3 is the bottom right

		* distance (float) - Specifies the focal length
		* applyPanZoom (bool) - specifies whether to apply 2D pan/zoom"""
	def getFocalLengthLimits(self)->tuple[float,float]:
		"""getFocalLengthLimits() -> (float, float)

		Returns the maximum and minimum focal length limits for the camera."""
	def getPortFieldOfView(self,int:int,int2:int)->tuple[float,float]:
		"""getPortFieldOfView(int, int) -> (float, float)

		Returns the horizontal and vertical field of view in radians from the given viewport width and height.

		* width (int) - width of viewport
		* height (int) - height of viewport"""
	def getRenderingFrustum(self,windowAspect:float)->tuple[float,float,float,float]:
		"""getRenderingFrustum(windowAspect) -> (float, float, float, float)

		Returns the rendering frustum (left, right, bottom and top) for the camera.
		This is the frustum that the maya renderer uses.

		* windowAspect (float) - windowAspect"""
	def getViewParameters(self,windowAspect:float,applyOverscan:bool=False,applySqueeze:bool=False,applyPanZoom:bool=False)->tuple[float,float,float,float]:
		"""getViewParameters(windowAspect, applyOverscan=False, applySqueeze=False, applyPanZoom=False) -> (float, float, float, float)

		Returns the intermediate viewing frustum (apertureX, apertureY, offsetX and offsetY) parameters for the camera. The aperture and offset are used by getViewingFrustum() and getRenderingFrustum() to compute the extent (left, right, top, bottom) of the frustum in the following manner:

		 left = focal_to_near * (-0.5*apertureX + offsetX)
		 right = focal_to_near * (0.5*apertureX + offsetX)
		 bottom = focal_to_near * (-0.5*apertureY + offsetY)
		 top = focal_to_near * (0.5*apertureY + offsetY)

		Here, focal_to_near is equal to cameraScale if the camera is orthographic, or it is equal to ((nearClippingPlane / (focalLength * MM_TO_INCH)) * cameraScale) where MM_TO_INCH equals 0.03937.

		* windowAspect (float) - windowAspect
		* applyOverscan (bool) - specifies whether to apply overscan
		* applySqueeze (bool) - specifies whether to apply the lens squeeze ratio of the camera
		* applyPanZoom (bool) - specifies whether to apply 2D pan/zoom"""
	def getViewingFrustum(self,windowAspect:float,applyOverscan:bool=False,applySqueeze:bool=False,applyPanZoom:bool=False)->tuple[float,float,float,float]:
		"""getViewingFrustum(windowAspect, applyOverscan=False, applySqueeze=False, applyPanZoom=False) -> (float, float, float, float)

		Returns the viewing frustum (left, right, bottom and top) for the camera.

		* windowAspect (float) - windowAspect
		* applyOverscan (bool) - specifies whether to apply overscan
		* applySqueeze (bool) - specifies whether to apply the lens squeeze ratio of the camera
		* applyPanZoom (bool) - specifies whether to apply 2D pan/zoom"""
	def hasSamePerspective(self,otherCamera:MDagPath)->bool:
		"""hasSamePerspective(otherCamera) -> bool

		Returns True if the camera has same perspective settings as the given camera.

		This method will only work when the world space information for the camera is available, i.e. when the function set has been initialized with a DAG path.

		* otherCamera (MDagPath) - Camera to compare perspective with"""
	def horizontalFieldOfView(self)->float:
		"""horizontalFieldOfView() -> float

		Returns the horizontal field of view for the camera."""
	def isOrtho(self)->bool:
		"""isOrtho() -> bool

		Returns True if the camera is in orthographic mode."""
	def postProjectionMatrix(self,context:MDGContext|None=None)->MFloatMatrix:
		"""postProjectionMatrix(context=None) -> MFloatMatrix

		Returns the post projection matrix used to compute film roll on the film back plane.

		* context (MDGContext) - DG time-context to specify time of evaluation"""
	def projectionMatrix(self,context:MDGContext|None=None)->MFloatMatrix:
		"""projectionMatrix(context=None) -> MFloatMatrix

		Returns the orthographic or perspective projection matrix for the camera.
		The projection matrix that maya's software renderer uses is almost identical to the OpenGL projection matrix. The difference is that maya uses a left hand coordinate system and so the entries [2][2] and [3][2] are negated.

		* context (MDGContext) - DG time-context to specify time of evaluation"""
	def rightDirection(self,space:int=MSpace.kObject)->MVector:
		"""rightDirection(space=kObject) -> MVector

		Returns the right direction vector for the camera.

		* space (int) - Specifies the coordinate system for this operation"""
	def set(self,wsEyeLocation:MPoint,wsViewDirection:MVector,wsUpDirection:MVector,horizFieldOfView:float,aspectRatio:float)->Self:
		"""set(wsEyeLocation, wsViewDirection, wsUpDirection, horizFieldOfView, aspectRatio) -> self

		Convenience routine to set the camera viewing parameters. The specified values should be in world space where applicable.

		This method will only work when the world space information for the camera is available, i.e. when the function set has been initialized with a DAG path.

		* wsEyeLocation (MPoint) - Eye location to set in world space
		* wsViewDirection (MVector) - View direction to set in world space
		* wsUpDirection (MVector) - Up direction to set in world space
		* horizFieldOfView (float) - The horizontal field of view to set
		* aspectRatio (float) - The aspect ratio to set"""
	def setAspectRatio(self,aspectRatio:float)->Self:
		"""setAspectRatio(aspectRatio) -> self

		Set the aspect ratio of the View.  The aspect ratio is expressed as width/height.  This also modifies the entity's scale transformation to reflect the new aspect ratio.

		* aspectRatio (float) - The aspect ratio to be set"""
	def setCenterOfInterestPoint(self,centerOfInterest:MPoint,space:int=MSpace.kObject)->Self:
		"""setCenterOfInterestPoint(centerOfInterest, space=kObject) -> self

		Positions the center-of-interest of the camera keeping the eye-point fixed in space. This method changed the orientation and translation of the camera's transform attributes as well as the center-of-interest distance.

		This method will only work when the world space information for the camera is available, i.e. when the function set has been initialized with a DAG path.

		* centerOfInterest (MPoint) - Center of interest point to be set
		* space (int) - Specifies the coordinate system for this operation"""
	def setEyePoint(self,eyeLocation:MPoint,space:int=MSpace.kObject)->Self:
		"""setEyePoint(eyeLocation, space=kObject) -> self

		Positions the eye-point of the camera keeping the center of interest fixed in space. This method changed the orientation and translation of the camera's transform attributes as well as the center-of-interest distance.

		This method will only work when the world space information for the camera is available, i.e. when the function set has been initialized with a DAG path.

		* eyeLocation (MPoint) - The eye location to set
		* space (int) - Specifies the coordinate system for this operation"""
	def setHorizontalFieldOfView(self,fov:float)->Self:
		"""setHorizontalFieldOfView(fov) -> self

		Sets the horizontal field of view for the camera.

		* fov (float) - The horizontal field of view value to be set"""
	def setIsOrtho(self,orthoState:bool,useDist:float|None=None)->Self:
		"""setIsOrtho(orthoState, useDist=None) -> self

		Switch the camera in and out of orthographic mode.  When the switch happens, the camera has to calculate a new fov or ortho width, each of which is based on the other and a set distance.  The caller can specify the distance; otherwise the center of interest is used.

		* orthoState (bool) - If True then the camera will be orthographic
		* useDist (float) - distance to use."""
	def setNearFarClippingPlanes(self,near:float,far:float)->Self:
		"""setNearFarClippingPlanes(near, far) -> self

		Set the distances to the Near and Far Clipping Planes.

		* near (float) - The near clipping plane value to be set
		* far (float) - The far clipping plane value to be set"""
	def setVerticalFieldOfView(self,fov:float)->Self:
		"""setVerticalFieldOfView(fov) -> self

		Sets the vertical field of view for the camera.

		* fov (float) - The vertical field of view value to be set"""
	def upDirection(self,space:int=MSpace.kObject)->MVector:
		"""upDirection(space=kObject) -> MVector

		Returns the up direction vector for the camera.

		* space (int) - Specifies the coordinate system for this operation"""
	def verticalFieldOfView(self)->float:
		"""verticalFieldOfView() -> float

		Returns the vertical field of view for the camera."""
	def viewDirection(self,space:int=MSpace.kObject)->MVector:
		"""viewDirection(space=kObject) -> MVector

		Returns the view direction for the camera

		* space (int) - Specifies the coordinate system for this operation"""
class MFnComponent(MFnBase):
	"""This is the base class for all function sets which deal with
	component objects.

	__init__()
	Initializes a new, empty MFnComponent object
	__init__(MObject component)
	Initializes a new MFnComponent function set, attached to the specified component."""
	@property
	def componentType(self)->int:
		"""Type of the component. (MFn Type constant)"""
	@property
	def elementCount(self)->int:
		"""Number of elements in the component."""
	@property
	def hasWeights(self)->bool:
		"""True if the component has weights associated with its elements."""
	@property
	def isComplete(self)->bool:
		"""Marking a component as complete means that it represents a full set
		of indices from 0 to elementCount-1"""
	@isComplete.setter
	def isComplete(self,value:bool)->None:...
	@property
	def isEmpty(self)->bool:
		"""True if the component contains no elements."""
	@overload
	def __init__(self)->None:
		"""Default constructor. Returns a new, empty MFnComponent object."""
	@overload
	def __init__(self,component:MObject)->None:
		"""Returns a new MFnComponent function set, attached to the specified component ."""
	def isEqual(self,other:MObject)->bool:
		"""Returns true if other refers to the same component as the one to which the function set is currently attached."""
	def weight(self,index:int)->MWeight:
		"""Returns the weight associated with the specified element, where index can range from 0 to elementCount-1."""
class MFnComponentListData(MFnData):
	"""MFnComponentListData allows the creation and manipulation of component list
	(represented as MObjects) data objects for use in the dependency graph.

	__init__()
	Initializes a new, empty MFnComponentListData object.

	__init__(MObject)
	Initializes a new MFnComponentListData function set, attached
	to the specified object."""
	@overload
	def __init__(self)->None:
		"""Default constructor. Returns a new, empty MFnComponentListData object."""
	@overload
	def __init__(self,object:MObject)->None:
		"""Returns a new MFnComponentListData function set, with the specified Maya object attached."""
	def add(self,component:MObject)->Self:
		"""Adds the specified component to the end of the list."""
	def clear(self)->Self:
		"""Removes all of the components from the list."""
	def create(self)->MObject:
		"""Creates a new, empty component list, attaches it to the function set and returns an MObject which references it."""
	def get(self,index:int)->MObject:
		"""Returns a copy of the component at the specified index . Raises IndexError if the index is out of range."""
	def length(self)->int:
		"""Returns the number of components in the list."""
	def has(self,component:MObject)->bool:
		"""Returns True if the list contains the specified component , False otherwise."""
	@overload
	def remove(self,component:MObject)->Self:
		"""Removes the specified component from the list. No exception is raised if the component is not in the list."""
	@overload
	def remove(self,index:int)->Self:
		"""Removes the component at the specified index from the list. Raises IndexError if the index is out of range."""
class MFnCompoundAttribute(MFnAttribute):
	"""Functionset for creating and working with compound attributes."""
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def addChild(self,child:MObject)->Self:
		"""Add a child attribute."""
	def child(self,index:int)->MObject:
		"""Returns the index 'th child attribute of this compound."""
	def create(self,longName:str,shortName:str)->MObject:
		"""Create a new compound attribute with the given longName and shortName , attach it to the function set and return it in an MObject ."""
	def getAddAttrCmds(self,longNames:bool=False)->list[str]:
		"""Returns a list of strings containing the addAttr commands necessary to recreate the compound attribute and all of its children. The attributes are returned in depth-first order, meaning that element 0 of the array will contain this attribute's addAttr command, element 1 will contain the command for its first child, element 2 will contain the command for its first child's child, if one exists, and so on. Each command is returned with the terminating semicolon and is formatted as if for use with a selected node, meaning that no node name is supplied."""
	def numChildren(self)->int:
		"""Returns number of child attributes currently parented under this compound attribute."""
	def removeChild(self,child:MObject)->Self:
		"""Remove a child attribute."""
class MFnContainerNode(MFnDependencyNode):
	"""Function set for containers."""
	kParentAnchor:int=0
	kChildAnchor:int=1
	kGeneric:int=2
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	@staticmethod
	def getCurrentAsMObject()->MObject:
		"""getCurrentAsMObject() -> MObject

		Retrieve the current container node."""
	def getPublishedPlugs(self)->tuple[Any,Any]:
		"""getPublishedPlugs() -> (MPlugArray publishedPlugs, [MString] publishedNames)

		Return a tuple of plugs that have been published on this container and the names of those plugs."""
	def getPublishedNames(self,unboundOnly:Any=bool)->list[str]:
		"""getPublishedNames(unboundOnly=bool) -> [MString]

		Return a list of published names on the container. Depending on the arguments, either all published names or only unbound published names will be returned."""
	def getMembers(self)->MObjectArray:
		"""getMembers() -> MObjectArray

		Return an array of the nodes included in this container."""
	def getSubcontainers(self)->MObjectArray:
		"""getSubcontainers() -> MObjectArray

		Return an array of the container nodes included in this container."""
	def getParentContainer(self)->MObject:
		"""getParentContainer() -> MObject

		Return the parent container, if there is one. Otherwise return an empty MObject."""
	def getRootTransform(self)->MObject:
		"""getRootTransform() -> MObject

		Return the root transform, if there is one. Otherwise return an empty MObject."""
	def getPublishedNodes(self,publishNodeType:Any=Any)->tuple[Any,Any]:
		"""getPublishedNodes(publishNodeType=MPublishNodeType) -> ([MString] publishedNames, MObjectArray publishedNodes)

		Return a list of the published nodes of a given type. For any names that have assigned nodes, return the node at the corresponding array index. For any names that do not have assigned nodes, a NULL MObject will be at the corresponding array index."""
	def isCurrent(self)->bool:
		"""isCurrent() -> bool

		Return whether the container node managed by this function set is the current container."""
	def makeCurrent(self,isCurrent:Literal[True]|Literal[False])->Self:
		"""makeCurrent(isCurrent) -> self

		Set or clear whether the container managed by this function set is denoted as the
		the current container.  If the flag is true and the container is allowed to be
		current, then the current container is set to be the container.  Otherwise, if the
		container managed by the function set is the current container, then the current
		container is cleared.

		* isCurrent (True/False) - Specifies whether this container shall be current."""
	def clear(self)->None:
		"""clear()

		Delete all members of the container."""
class MFnDagNode(MFnDependencyNode):
	"""Function set for operating on DAG nodes.

	__init__()
	Initializes a new, empty MFnDagNode functionset.

	__init__(MObject)
	Initializes a new MFnDagNode functionset and attaches it to a
	DAG node.

	__init__(MDagPath)
	Initializes a new MFnDagNode functionset and attaches it to a
	DAG path."""
	@property
	def boundingBox(self)->MBoundingBox:
		"""Node's bounding box, in object space."""
	@property
	def inModel(self)->bool:
		"""True if the node has been added to the model."""
	@property
	def inUnderWorld(self)->bool:
		"""True if this node is in the underworld of another node (e.g. a curve on surface is in the underworld of the surface)."""
	@property
	def isInstanceable(self)->bool:
		"""True if instancing is allowed for this node."""
	@isInstanceable.setter
	def isInstanceable(self,value:bool)->None:...
	@property
	def isIntermediateObject(self)->bool:
		"""True if this node is just an intermediate in part of a larger calculation (e.g. input to a deformer)."""
	@isIntermediateObject.setter
	def isIntermediateObject(self,value:bool)->None:...
	@property
	def objectColor(self)->int:
		"""Index from 0 to 7 indicating the color in which the node is to be drawn when inactive, assuming that it is drawable."""
	@objectColor.setter
	def objectColor(self,value:int)->None:...
	@property
	def objectColorRGB(self)->Any:
		"""RGB value indicating the color in which the node is to be drawn when inactive, assuming that it is drawable."""
	@objectColorRGB.setter
	def objectColorRGB(self,value:Any)->None:...
	@property
	def useObjectColor(self)->bool:
		"""If True then the node will be drawn using its 'objectColor', otherwise it will be drawn using Maya's default color. Thismethod is deprecated, use objectColorType instead."""
	@useObjectColor.setter
	def useObjectColor(self,value:bool)->None:...
	@property
	def objectColorType(self)->Any:
		"""Determines whether the default color, indexed object color, orRGB object color is used for this object."""
	@objectColorType.setter
	def objectColorType(self,value:Any)->None:...
	kNextPos:int=255
	@overload
	def __init__(self)->None:
		"""Default constructor. Returns a new MFnDagNode function set with no Maya object attached."""
	@overload
	def __init__(self,object:MObject)->None:
		"""Returns a new MFnDagNode function set, attached to the specified Maya object ."""
	@overload
	def __init__(self,path:MDagPath)->None:
		"""Returns a new MFnDagNode function set, attached to the object at the end of the specified DAG path ."""
	def addChild(self,node:MObject,index:int=MFnAssembly.kNextPos,keepExistingParents:bool=False)->Self:
		"""Parent's node under this node, making it the index 'th child and moving other children down to make room, if necessary. If index is kNextPos then it is added to the end of the list of children. If keepExistingParents is False the child node will be removed from its existing parents, otherwise they will be retained."""
	def child(self,index:int)->MObject:
		"""Returns the node's index 'th child."""
	def childCount(self)->int:
		"""Returns the number of nodes which are parented under this one."""
	def create(self,type:str|MTypeId,name:str|None=None,parent:MObject=MObject.kNullObj)->MObject:
		"""Creates a new DAG node of the specified type , with the given name . type may be either a type name or a type ID. If no name is given then a unique name will be generated by combining the type name with an integer. If a parent is given then the new node will be parented under it and the functionset will be attached to the newly-created node. The newly-created node will be returned. If no parent is given and the new node is a transform, it will be parented under the world and the functionset will be attached to the newly-created transform. The newly-created transform will bereturned. If no parent is given and the new node is not a transform then a transform node will be created under the world, the new node will be parented under it, and the functionset will be attached to the transform. The transform will be returned."""
	def dagPath(self)->MDagPath:
		"""Returns the DAG path to which this function set is attached. Raises a TypeError if the function set is not attached to a path (e.g. it was initialized with an MObject )."""
	def dagRoot(self)->MObject:
		"""Returns the root node of the first path leading to this node."""
	def duplicate(self,instance:bool=False,instanceLeaf:bool=False)->MObject:
		"""Duplicates the DAG hierarchy rooted at the current node. The copy will have the same parent, if any, as the original node. If instance is false then a true copy will be made, otherwise a new node will be created which instances the child nodes of the original node. If instance is false then instanceLeaf is ignored. If instance is true and instanceLeaf is false then the child nodes of the original node are instanced. If instanceLeaf is true, then the results are similar to a copy, but the leaf level objects are instanced. Returns the new node at the top of the duplicated hierarchy."""
	def fullPathName(self)->str:
		"""Returns the full path of the attached object, from the root of the DAG on down."""
	def getAllPaths(self)->MDagPathArray:
		"""Returns all of the DAG paths which lead to the object to which this function set is attached."""
	def getConnectedSetsAndMembers(self,instance:Any,renderableSetsOnly:Any)->tuple[MObjectArray,MObjectArray]:
		"""getConnectedSetsAndMembers(instance, renderableSetsOnly) -> (MObjectArray, MObjectArray)

		Returns a tuple containing an array of sets and an array of the
		components of the DAG object which are in those sets. If the entire object is in a set, then the corresponding entry in the comps array will have no elements in it."""
	def getPath(self)->MDagPath:
		"""Returns the DAG path to which this function set is attached. If the function set is attached to an MObject rather tha a DAG path then the first path to the object will be returned."""
	def hasChild(self,node:MObject)->bool:
		"""Returns True if node is a child of this node."""
	def hasParent(self,node:MObject)->bool:
		"""Returns True if node is a parent of this node."""
	def instanceCount(self,indirect:bool)->int:
		"""Returns the number of instances for this node. If indirect is True then the instancing of ancestor nodes further up the DAG path is included, otherwise only the immediate instancing of this node is counted."""
	def isChildOf(self,node:MObject)->bool:
		"""Alias for hasParent() ."""
	def isInstanced(self,indirect:bool=True)->bool:
		"""Returns True if this node is instanced (i.e. has multiple parents). If indirect is True then the instancing of ancestor nodes further up the DAG path is included, otherwise not."""
	def isInstancedAttribute(self,attr:MObject)->bool:
		"""Returns True if attr is an instanced attribute of this node."""
	def isParentOf(self,node:MObject)->bool:
		"""Alias for hasChild() ."""
	def parent(self,index:int)->MObject:
		"""Returns the node's index 'th parent."""
	def parentCount(self)->int:
		"""Returns the number of different nodes under which this one is parented."""
	def partialPathName(self)->str:
		"""Returns the minimum path necessary to uniquely identify the attached object."""
	def removeChild(self,node:MObject)->Self:
		"""Removes node as a child of this node."""
	def removeChildAt(self,index:int)->Self:
		"""Removes the index 'th child from this node."""
	@overload
	def setObject(self,object:MObject)->Self:
		"""Attaches the function set to the specified object ."""
	@overload
	def setObject(self,object:MDagPath)->Self:
		"""Attaches the function set to the specified DAG path ."""
	def transformationMatrix(self)->MMatrix:
		"""Returns the object space transformation matrix for this DAG node. In general, only transform nodes have matrices associated with them. Nodes such as shapes (geometry nodes) do not have transform matrices. The identity matrix will be returned if this node does not have a transformation matrix."""
class MFnData(MFnBase):
	"""Base class for dependency graph data function sets."""
	kInvalid:int=0
	kNumeric:int=1
	kPlugin:int=2
	kPluginGeometry:int=3
	kString:int=4
	kMatrix:int=5
	kStringArray:int=6
	kDoubleArray:int=7
	kFloatArray:int=8
	kIntArray:int=9
	kPointArray:int=10
	kVectorArray:int=11
	kMatrixArray:int=12
	kComponentList:int=13
	kMesh:int=14
	kLattice:int=15
	kNurbsCurve:int=16
	kNurbsSurface:int=17
	kSphere:int=18
	kDynArrayAttrs:int=19
	kDynSweptGeometry:int=20
	kSubdSurface:int=21
	kNObject:int=22
	kNId:int=23
	kAny:int=24
	kFalloffFunction:int=25
	kLast:int=26
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
class MFnDependencyNode(MFnBase):
	"""Function set for operating on dependency nodes."""
	@property
	def isDefaultNode(self)->bool:
		"""True if this is a default node, created automatically by Maya."""
	@property
	def isFromReferencedFile(self)->bool:
		"""True if the node is from a referenced file, False if the node is part of the main scene."""
	@property
	def isLocked(self)->bool:
		"""True if the node is locked against changes."""
	@isLocked.setter
	def isLocked(self,value:bool)->None:...
	@property
	def isShared(self)->bool:
		"""True if the node is shared."""
	@property
	def namespace(self)->str:
		"""Name of the namespace which contains the node."""
	@property
	def pluginName(self)->str:
		"""Name of the plugin which registered the node type, if any."""
	@property
	def typeId(self)->MTypeId:
		"""MTypeId for the node's type."""
	@property
	def typeName(self)->str:
		"""Name of the node's type."""
	kLocalDynamicAttr:int=1
	kNormalAttr:int=2
	kExtensionAttr:int=3
	kInvalidAttr:int=4
	kTimerOff:int=0
	kTimerOn:int=1
	kTimerUninitialized:int=2
	kTimerInvalidState:int=3
	kTimerMetric_callback:int=0
	kTimerMetric_compute:int=1
	kTimerMetric_dirty:int=2
	kTimerMetric_draw:int=3
	kTimerMetric_fetch:int=4
	kTimerMetric_callbackViaAPI:int=5
	kTimerMetric_callbackNotViaAPI:int=6
	kTimerMetric_computeDuringCallback:int=7
	kTimerMetric_computeNotDuringCallback:int=8
	kTimerMetrics:int=9
	kTimerType_self:int=0
	kTimerType_inclusive:int=1
	kTimerType_count:int=2
	kTimerTypes:int=3
	@overload
	def __init__(self)->None:
		"""Default constructor. Returns a new MFnDependencyNode function set with no node attached."""
	@overload
	def __init__(self,object:MObject)->None:
		"""Returns a new MFnDependencyNode function set, attached to the specified Maya node ."""
	@staticmethod
	def allocateFlag(plugin:str)->int:
		"""Allocates a flag on all nodes for use by the named plugin . Returns the flag's index. Raises a ValueError if there are no unallocated node flags available."""
	@staticmethod
	def classification(nodeType:str)->str:
		"""Returns the classification string for the named nodeType ."""
	@staticmethod
	def deallocateAllFlags(plugin:str)->None:
		"""Deallocates all node flags which are currently allocated to the named plugin ."""
	@staticmethod
	def deallocateFlag(plugin:str,flag:int)->None:
		"""Deallocates the specified node flag , which was previously allocated by the named plugin using allocateFlag() ."""
	def absoluteName(self,*args)->Any:
		"""Returns the absolute name of this node.  The absolute name of a node is the full namespace path starting at (and including) the root namespace, down to (and including) the node itself.  Regardless of relative name mode, absoluteName() will always return a full namespace path prefixed with a leading colon (the root namespace).  If the underlying node is a DAG node, then absoluteName() does not guarantee uniqueness, that is, two dependency nodes could have the same absoluteName().  In cases like this the uniqueName() method will guarantee that the name uniquely identifies the node."""
	def uniqueName(self,*args)->Any:
		"""For a DAG node, the unique name of a node is the full namespace path starting at (and including) the root namespace, down to (and including) the node itself. For a non-DAG node, the uniqueName is just its name."""
	def addAttribute(self,attribute:MObject)->Self:
		"""Adds a new dynamic attribute to the node."""
	def affectsAnimation(self,*args)->Any:
		"""Returns true if the changes to the node may affect animation."""
	@overload
	def attribute(self,index:int)->MObject:
		"""Returns the node's index 'th attribute, based on the order in which they were added to the node."""
	@overload
	def attribute(self,name:str)->MObject:
		"""Returns the attribute with the given name ."""
	def attributeClass(self,attribute:MObject)->int:
		"""Returns the class of the specified attribute ."""
	def attributeCount(self)->int:
		"""Returns the number of attributes on the node."""
	def canBeWritten(self)->bool:
		"""Returns true if the node will be written to file."""
	@overload
	def create(self,typeId:MTypeId,nodeName:str|None=None)->MObject:
		"""Creates a new node of the given type, using the nodeName provided, attaches it to the function set and returns it in an MObject . If no nodeName is given the node's type name will be used, followed by a number to ensure uniqueness."""
	@overload
	def create(self,typeName:str,nodeName:str|None=None)->MObject:
		"""Creates a new node of the given type, using the nodeName provided, attaches it to the function set and returns it in an MObject . If no nodeName is given the node's type name will be used, followed by a number to ensure uniqueness."""
	def dgCallbackIds(self,timerType:int,callbackName:str)->tuple[MCallbackIdArray,MDoubleArray]:
		"""Returns a tuple containing an array of callback ids as its first element and an array of doubles as its second element. These represent the callback timer values for the specified timerType and callbackName , separated out per callback ID."""
	def dgCallbacks(self,type:int)->tuple[list[str],MDoubleArray]:
		"""Returns a tuple containing a list of callback type names as its first element and an array of doubles as its second element. These represent the callback timer values for the specified timer type , grouped by type of callback."""
	def dgTimer(self,metric:int,type:int)->float:
		"""Returns the timer value for the given metric and type ."""
	def dgTimerOff(self)->Self:
		"""Turns DG timing off for this node."""
	def dgTimerOn(self)->Self:
		"""Turns DG timing on for this node."""
	def dgTimerQueryState(self)->int:
		"""Returns the current DG timer state for this node."""
	def dgTimerReset(self)->Self:
		"""Resets all DG timers for this node."""
	def findAlias(self,alias:str)->MObject:
		"""Returns the attribute which has the given alias or MObject::kNullObj if none."""
	def findPlug(self,attr:str|MObject,wantNetworkedPlug:bool)->MPlug:
		"""Returns a plug for the given attribute, which may be specified either by name or by MObject ."""
	def getAffectedAttributes(self,attribute:MObject)->MObjectArray:
		"""Returns all of the attributes which are affected by the specified attribute ."""
	def getAffectingAttributes(self,attribute:MObject)->MObjectArray:
		"""Returns all of the attributes which affect the specified attribute ."""
	def getAliasAttr(self,force:bool)->MObject:
		"""Returns the node's alias attribute, which is a special attribute used to store information about the node's attribute aliases."""
	def getAliasList(self)->tuple[tuple[str,...],...]:
		"""Returns all of the node's attribute aliases in a tuple. Each element of the tuple is itself a tuple containing a pair of strings representing the attribute's alias and its real name."""
	def getConnections(self)->MPlugArray:
		"""Returns all the plugs which are connected to attributes of this node."""
	def hasAttribute(self,name:str)->bool:
		"""Returns True if the node has an attribute with the given name ."""
	def hasUniqueName(self)->bool:
		"""Returns True if the node's name is unique."""
	def isFlagSet(self,flag:int)->bool:
		"""Returns the state of the specified node flag , which must previously have been allocated by a call to allocateFlag() ."""
	def isNewAttribute(self,attribute:MObject)->bool:
		"""Returns True if the specified attribute was added in the current scene, and not by by one of its referenced files."""
	def isTrackingEdits(self,*args)->Any:
		"""Returns True if the node is referenced or in an assembly that is tracking edits."""
	def name(self)->str:
		"""Returns the node's name."""
	def plugsAlias(self,plug:MPlug)->str:
		"""Returns the alias for the plug's attribute or the empty string if that attribute has no alias."""
	def removeAttribute(self,attribute:MObject)->Self:
		"""Removes a dynamic attribute from the node."""
	def reorderedAttribute(self,index:int)->MObject:
		"""Returns the node's index 'th attribute, based on the order in which they are written to file."""
	def setAffectsAnimation(self,*args)->Any:
		"""Specifies that modifications to a node could potentially affect the animation."""
	def setAlias(self,alias:str,attrName:str,plug:MPlug,add:bool=True)->bool:
		"""Adds or removes an attribute alias. Returns False if the alias to be added already exists, or if the alias to be removed does not exist."""
	def setDoNotWrite(self,flag:bool)->Self:
		"""Used to prevent the node from being written to file."""
	def setFlag(self,flag:int,state:bool)->Self:
		"""Sets the state of the specified node flag , which must previously have been allocated by a call to allocateFlag() ."""
	def setName(self,name:str)->str:
		"""Sets the node's name. If there is a conflict with another node the name will be modified to make it unique. The name actually used is returned."""
	def setUuid(self,*args)->Any:
		"""Sets the node's UUID."""
	def userNode(self)->MPxNode|None:
		"""If the node is a plug-in node, its proxy object is returned, otherwise None is returned."""
	def uuid(self,*args)->Any:
		"""Returns the node's UUID."""
	def addExternalContentForFileAttr(self,*args)->Any:
		"""Adds content info to the specified table from a file path attribute."""
	def getExternalContent(self,*args)->Any:
		"""Gets the external content (files) that this node depends on."""
	def setExternalContent(self,*args)->Any:
		"""Changes the location of external content."""
	def setExternalContentForFileAttr(self,*args)->Any:
		"""Sets content info in the specified attribute from the table."""
class MFnDisplayLayer(MFnDependencyNode):
	"""Function set display layer.

	__init__()
	Initializes a new, empty MFnDisplayLayer object.

	"""
	def __init__(self)->None:
		"""Initializes a new, empty MFnDisplayLayer object."""
	def getMembers(self,members:Any)->status:
		"""getMembers(members) -> status
		Get the members of the display layer"""
	def add(self,item:Any)->status:
		"""add(item) -> status
		Adds the item to the display layer, where item can be a Ufe path string
		(MString) or a Maya path (MDagPath)."""
	def remove(self,item:Any)->status:
		"""remove(item) -> status
		Removes the item to the display layer, where item can be a Ufe path string
		(MString) or a Maya path (MDagPath)."""
	def contains(self,item:Any)->bool:
		"""contains(item) -> bool
		Returns true if the item is in the display layer, where item can be a Ufe
		path string (MString) or a Maya path (MDagPath)."""
	def containsAncestorInclusive(self,item:Any)->status:
		"""containsAncestorInclusive(item) -> status
		Returns true if the item or one of its ancestors is in the display layer,
		 where item can be a Ufe path string (MString) or a Maya path (MDagPath)."""
class MFnDisplayLayerManager(MFnDependencyNode):
	"""Function set display layer.

	__init__()
	Initializes a new, empty MFnDisplayLayerManager object.

	"""
	def __init__(self)->None:
		"""Initializes a new, empty MFnDisplayLayerManager object."""
	@staticmethod
	def currentDisplayLayerManager()->MObject:
		"""currentDisplayLayerManager() -> MObject
		Get the current display layer manager"""
	def getAllDisplayLayers(self)->Any:
		"""getAllDisplayLayers() -> object array
		Get all the display layers managed by the display layer manager
		(MString) or a Maya path (MDagPath)."""
	def getLayer(self,item:Any)->status:
		"""getLayer(item) -> status
		Finds the layer the item is in, where item can be a Ufe
		path string (MString) or a Maya object (MObject)."""
	def getAncestorLayersInclusive(self,item:Any)->status:
		"""getAncestorLayersInclusive(item) -> status
		Finds the layers the item and it's ancestors are in, where item can be a Ufe
		path string (MString) or a Maya object (MObject)."""
class MFnDoubleArrayData(MFnData,collections.abc.Sequence[float]):
	"""Function set for node data consisting of an array of doubles."""
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def __len__(self)->int:
		"""Return len(self)."""
	def __getitem__(self,index:int)->float:
		"""Return self[key]."""
	def __setitem__(self,index:int,value:float)->None:
		"""Set self[key] to value."""
	def __delitem__(self,index:int)->None:
		"""Delete self[key]."""
	def array(self)->MDoubleArray:
		"""Returns the encapsulated array as an MDoubleArray . For performance reasons the returned array is a live reference to the encapsulated array so changes made to one directly affect the other. The returned array is only valid for as long as the function set retains the same data object. If the function set is destroyed or attached to a different object then the returned array should be discarded. Failure to do so could result in Maya becoming unstable."""
	def copyTo(self,array:MDoubleArray)->Self:
		"""Replaces the elements of array with those in the encapsulated array."""
	@overload
	def create(self)->MObject:
		"""Creates a new, empty double array data object, attaches it to the function set and returns an MObject which references it."""
	@overload
	def create(self,array:MDoubleArray|Sequence[float])->MObject:
		"""Creates a new, double array data object, initializes it with the elements from array , attaches it to the function set and returns an MObject which references it."""
	@overload
	def set(self,array:MDoubleArray|Sequence[float])->Self:
		"""Replaces the elements in the encapsulated array with those from the supplied array ."""
	@overload
	def set(self,value:float,index:int)->Self:
		"""Sets the value of the index 'th element of the array."""
class MFnDoubleIndexedComponent(MFnComponent):
	"""This function set allows you to create, edit, and query double indexed
	components. Double indexed components store 2 dimensional index values.

	__init__()
	Initializes a new, empty MFnDoubleIndexedComponent object

	__init__(MObject component)
	Initializes a new MFnDoubleIndexedComponent function set, attached
	to the specified component."""
	@overload
	def __init__(self)->None:
		"""Initializes a new, empty MFnDoubleIndexedComponent object"""
	@overload
	def __init__(self,component:MObject)->None:
		"""Initializes a new MFnDoubleIndexedComponent function set, attached
		to the specified component."""
	@overload
	def addElement(self,uIndex:int,vIndex:int)->Self:
		"""addElement(uIndex, vIndex) -> self
		addElement([uIndex, vIndex]) -> self

		Adds the element identified by (uIndex, vIndex) to the component."""
	@overload
	def addElement(self,arg:list[int])->Self:
		"""addElement(uIndex, vIndex) -> self
		addElement([uIndex, vIndex]) -> self

		Adds the element identified by (uIndex, vIndex) to the component."""
	def addElements(self,arg:Sequence[int])->Self:
		"""addElements(sequence of [uIndex, vIndex]) -> self

		Adds the specified elements to the component. Each item in the
		elements sequence is itself a sequence of two ints which are the U and
		V indices of an element to be added."""
	def create(self,arg:int)->MObject:
		"""create(MFn Type constant) -> MObject

		Creates a new, empty component, attaches it to the function set and
		returns an MObject which references it."""
	def getCompleteData(self)->tuple[int,int]:
		"""getCompleteData() -> (numU, numV)

		Returns a tuple containing the number of U and V indices in the complete
		component, or (0,0) if the component is not complete."""
	def getElement(self,index:int)->tuple[int,int]:
		"""getElement(index) -> (uIndex, vIndex)

		Returns the index'th element of the component as a tuple containing the
		element's U and V indices."""
	def getElements(self)->list[int]:
		"""getElements() -> list of (uIndex, vIndex)

		Returns all of the component's elements as a list of tuples with each
		tuple containing the U and V indices of a single element."""
	def setCompleteData(self,numU:int,numV:int)->Self:
		"""setCompleteData(numU, numV) -> self

		Marks the component as complete (i.e. contains all possible elements).
		numU and numV indicate the number of U and V indices in the complete
		component (i.e. the max U index is numU-1 and the max V index is numV-1)."""
class MFnEnumAttribute(MFnAttribute):
	"""Functionset for creating and working with enumeration attributes."""
	@property
	def default(self)->int:
		"""Default value"""
	@default.setter
	def default(self,value:int)->None:...
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def addField(self,name:str,value:int)->Self:
		"""Add an item to the enumeration with the specified UI name and corresponding attribute value ."""
	def create(self,longName:str,shortName:str,defaultValue:int=0)->MObject:
		"""Create a new enum attribute with the given longName , shortName and defaultValue , attach it to the function set and return it in an MObject ."""
	def fieldName(self,value:int)->str:
		"""Returns the name of the enumeration item which has the given value ."""
	def fieldValue(self,name:str)->int:
		"""Returns the value of the enumeration item which has the given name ."""
	def getMax(self)->int:
		"""Returns the maximum value of all the enumeration items."""
	def getMin(self)->int:
		"""Returns the minimum value of all the enumeration items."""
	def setDefaultByName(self,name:str)->Self:
		"""Set the default value using the name of an enumeration item. Equivalent to attr.default = attr.fieldValue(name) ."""
class MFnGenericAttribute(MFnAttribute):
	"""Functionset for creating and working with attributes which can accept several different types of data."""
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def addDataType(self,type:int)->Self:
		"""Adds the specified Maya data type to the list of those accepted by the attribute."""
	def addNumericType(self,type:int)->Self:
		"""Adds the specified numeric type to the list of those accepted by the attribute."""
	def addTypeId(self,typeId:MTypeId)->Self:
		"""Adds the specified MPxData or MPxGeometryData typeId to the list of those accepted by the attribute."""
	def create(self,longName:str,shortName:str)->MObject:
		"""Create a new message attribute with the given longName and shortName , attach it to the function set and return it in an MObject ."""
	def removeDataType(self,type:int)->Self:
		"""Removes the specified Maya data type from the list of those accepted by the attribute."""
	def removeNumericType(self,type:int)->Self:
		"""Removes the specified numeric type from the list of those accepted by the attribute."""
	def removeTypeId(self,typeId:MTypeId)->Self:
		"""Removes the specified data typeId from the list of those accepted by the attribute."""
class MFnGeometryData(MFnData):
	"""This class is the function set for geometry data.

	Geometry data adds matrix and grouping (set) information to regular
	data and is used to pass geometry types such as mesh, lattice, and
	NURBS shape data through DG connections.

	__init__()
	Initializes a new, empty MFnGeometryData object

	__init__(MObject)
	Initializes a new MFnGeometryData function set, attached
	to the specified object."""
	@property
	def matrix(self)->MMatrix:
		"""MMatrix used to convert the object into local space."""
	@matrix.setter
	def matrix(self,value:MMatrix)->None:...
	@property
	def isIdentity(self)->bool:
		"""True if the matrix for the geometry is the identity."""
	@property
	def isNotIdentity(self)->bool:
		"""True if the matrix for the geometry is not the identity."""
	@property
	def objectGroupCount(self)->int:
		"""The number of object groups contained by the object."""
	kAuto:int=0
	kNull:int=1
	kVerts:int=2
	kEdges:int=3
	kFaces:int=4
	kUnsupported:int=5
	kInvalidGroup:int=0
	kEmptyGroup:int=1
	kCompleteGroup:int=2
	kPartialGroup:int=3
	@overload
	def __init__(self)->None:
		"""Default constructor. Returns a new, empty MFnGeometryData object."""
	@overload
	def __init__(self,obj:MObject)->None:
		"""Returns a new MFnGeometryData function set, attached to the specified object."""
	def addObjectGroup(self,id:int)->Self:
		"""Adds an object group with the given id to the object."""
	def addObjectGroupComponent(self,id:int,component:MObject)->Self:
		"""Adds the members of the given component to the object group with the given id."""
	def changeObjectGroupId(self,sourceId:int,destId:int)->Self:
		"""Changes the id of the object group with the given id to the new id."""
	def copyObjectGroups(self,inGeom:MObject)->Self:
		"""Copies the object groups from the given geometry data object."""
	def hasObjectGroup(self,id:int)->bool:
		"""Returns True if an object group with the given id is contained in the data."""
	def objectGroup(self,index:int)->Any:
		"""Returns the id of the index'th object group contained by the object."""
	def objectGroupComponent(self,id:int)->MObject:
		"""Returns a component which contains the members of the object group with the given id."""
	def objectGroupType(self,id:int)->int:
		"""Returns the type of the component that the object group with the given id contains."""
	def removeObjectGroup(self,id:int)->Self:
		"""Removes an object group with the given id from the object."""
	def removeObjectGroupComponent(self,id:int,component:MObject)->Self:
		"""Removes the members of the given component from the object group with the given id."""
	def setObjectGroupComponent(self,id:int,component:MObject)->Self:
		"""Sets the members of the object group with the given id to be only those in the given component."""
	def hasComponentTag(self,key:Any)->bool:
		"""hasComponentTag(key) -> bool

		Returns True if a componentTag with the given key exists."""
	def addComponentTag(self,key:Any)->Self:
		"""addComponentTag(key) -> self

		Adds a componentTag with the given key to the object."""
	def removeComponentTag(self,key:Any)->Self:
		"""removeComponentTag(key) -> self

		Removes a componentTag with the given key from the object."""
	def renameComponentTag(self,key:Any,newKey:Any)->Self:
		"""renameComponentTag(key, newKey) -> self

		Renames a componentag with the given key the object."""
	def componentTagType(self,key:Any)->int:
		"""componentTagType(key) -> MFn Type constant

		Returns the type of the component that the componentTag with the
		given key contains."""
	def setComponentTagContents(self,key:Any,component:MObject)->Self:
		"""setComponentTagContents(key, MObject component) -> self

		Sets the members of the componentTag with the given key
		to be those in the given component."""
	def componentTagContents(self,key:Any)->MObject:
		"""componentTagContents(key) -> MObject

		Returns a component which contains the members of the componentTag
		with the given key."""
	def componentTags(self)->MObject:
		"""componentTags() -> MObject

		Returns the componentTag keys contained in the object."""
	def objectGroupSubsetState(self,id:Any)->int:
		"""objectGroupSubsetState(id) -> MFnGeometryData::SubsetState type constant

		Returns the state of the group contents of the object group with the
		given id."""
	def componentTagExpressionSubsetState(self,expr:Any,ctg:Any)->int:
		"""componentTagExpressionSubsetState(expr,ctg) -> MFnGeometryData::SubsetState type constant

		Returns the state of the contents of the resolved componentTag expression."""
	def resolveComponentTagExpression(self,key:Any,ctg:Any)->MObject:
		"""resolveComponentTagExpression(key, ctg) -> MObject

		Returns a component which is the result of the resolved componentTag expression
		with the given key."""
class MFnIntArrayData(MFnData,collections.abc.Sequence[int]):
	"""Function set for node data consisting of an array of ints."""
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def __len__(self)->int:
		"""Return len(self)."""
	def __getitem__(self,index:int)->int:
		"""Return self[key]."""
	def __setitem__(self,index:int,value:int)->None:
		"""Set self[key] to value."""
	def __delitem__(self,index:int)->None:
		"""Delete self[key]."""
	def array(self)->MIntArray:
		"""Returns the encapsulated array as an MIntArray . For performance reasons the returned array is a live reference to the encapsulated array so changes made to one directly affect the other. The returned array is only valid for as long as the function set retains the same data object. If the function set is destroyed or attached to a different object then the returned array should be discarded. Failure to do so could result in Maya becoming unstable."""
	def copyTo(self,array:MIntArray)->Self:
		"""Replaces the elements of array with those in the encapsulated array."""
	@overload
	def create(self)->MObject:
		"""Creates a new, empty int array data object, attaches it to the function set and returns an MObject which references it."""
	@overload
	def create(self,array:MIntArray|Sequence[int])->MObject:
		"""Creates a new, int array data object, initializes it with the elements from array , attaches it to the function set and returns an MObject which references it."""
	@overload
	def set(self,array:MIntArray|Sequence[int])->Self:
		"""Replaces the elements in the encapsulated array with those from the supplied array ."""
	@overload
	def set(self,value:int,index:int)->Self:
		"""Sets the value of the index 'th array element."""
class MFnLightDataAttribute(MFnAttribute):
	"""Functionset for creating and working with light data attributes."""
	@property
	def default(self)->tuple[tuple[float, float, float], tuple[int, int, int], bool, bool, bool, float, float, int]:
		"""Default values for the light data attribute's child attributes."""
	@default.setter
	def default(self,value:tuple[tuple[float, float, float], tuple[int, int, int], bool, bool, bool, float, float, int])->None:...
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def child(self,index:int)->MObject:
		"""Returns the specified child attribute."""
	def create(self,longName:str,shortName:str,direction:MObject,intensity:MObject,ambient:MObject,diffuse:MObject,specular:MObject,shadowFraction:MObject,preShadowIntensity:MObject,blindData:MObject)->MObject:
		"""Creates a new light data attribute having the child attributes provided, attaches it to the function set and returns it in an MObject ."""
class MFnMatrixArrayData(MFnData,collections.abc.Sequence[MMatrix]):
	"""Function set for node data consisting of an array of MMatrix."""
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def __len__(self)->int:
		"""Return len(self)."""
	def __getitem__(self,index:int)->MMatrix:
		"""Return self[key]."""
	def __setitem__(self,index:int,value:MMatrix)->None:
		"""Set self[key] to value."""
	def __delitem__(self,index:int)->None:
		"""Delete self[key]."""
	def array(self,*args)->Any:
		"""Returns the encapsulated array as an MMatrixArray."""
	def copyTo(self,*args)->Any:
		"""Replaces the elements of an array with those in the encapsulated array."""
	def create(self,*args)->Any:
		"""Creates a new MMatrix array data object."""
	def set(self,*args)->Any:
		"""Sets values in the encapsulated array."""
class MFnMatrixAttribute(MFnAttribute):
	"""Functionset for creating and working with matrix attributes."""
	@property
	def default(self)->Any:
		"""Default value"""
	@default.setter
	def default(self,value:Any)->None:...
	kFloat:int=0
	kDouble:int=1
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def create(self,longName:str,shortName:str,type:int=MFnMatrixAttribute.kDouble)->MObject:
		"""Create a new float or double matrix attribute with the given longName and shortName , attach it to the function set and return it in an MObject ."""
class MFnMatrixData(MFnData):
	"""Function set for matrix node data."""
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	@overload
	def create(self)->MObject:
		"""Creates a new MMatrix data object, initializes it to the identity matrix, attaches it to the function set and returns an MObject which references it."""
	@overload
	def create(self,matrix:MMatrix)->MObject:
		"""Creates a new MMatrix data object, initializes it from the given matrix , attaches it to the function set and returns an MObject which references it."""
	@overload
	def create(self,tm:MTransformationMatrix)->MObject:
		"""Creates a new MTransformationMatrix data object, initializes it from transformation matrix tm , attaches it to the function set and returns an MObject which references it."""
	def isTransformation(self)->bool:
		"""Returns True if the attached object is an MTransformationMatrix , False if it is an MMatrix ."""
	def matrix(self)->MMatrix:
		"""Returns the encapsulated MMatrix . If the function set was previously encapsulating an MTransformationMatrix it will be converted to an MMatrix and any previously returned references (e.g. from the transformation() method) will no longer be invalid."""
	@overload
	def set(self,matrix:MMatrix)->Self:
		"""Replaces the contents of the encapsulated matrix with that of the supplied matrix . If the function set was previously encapsulating an MTransformationMatrix it will be switched to an MMatrix and any previously returned references (e.g. from the transformation() method) will no longer be invalid."""
	@overload
	def set(self,tm:MTransformationMatrix)->Self:
		"""Replaces the contents of the encapsulated matrix with that of the supplied transformation matrix tm . If the function set was previously encapsulating an MMatrix it will be switched to an MTransformationMatrix and any previously returned references (e.g. from the matrix() method) will no longer be invalid."""
	def transformation(self)->MTransformationMatrix:
		"""Returns the encapsulated MTransformationMatrix . If the function set was previously encapsulating an MMatrix it will be converted to an MTransformationMatrix and any previously returned references (e.g. from the matrix() method) will no longer be invalid."""
class MFnMesh(MFnDagNode):
	"""Function set for operation on meshes (polygonal surfaces).

	__init__()
	Initializes a new, empty MFnMesh object.

	__init__(MDagPath path)
	Initializes a new MFnMesh object and attaches it to the DAG path
	of a mesh node.

	__init__(MObject nodeOrData)
	Initializes a new MFnMesh object and attaches it to a mesh
	node or mesh data object."""
	@property
	def checkSamePointTwice(self)->bool:
		"""Controls whether polygons created or added through the functionset
		are checked for duplicate points."""
	@checkSamePointTwice.setter
	def checkSamePointTwice(self,value:bool)->None:...
	@property
	def displayColors(self)->bool:
		"""Determines if the mesh's colors are displayed. Attempting to turn
		color display on when the functionset is attached to mesh data (as
		opposed to a mesh node) will raise TypeError."""
	@displayColors.setter
	def displayColors(self,value:bool)->None:...
	@property
	def numColorSets(self)->int:
		"""Number of color sets."""
	@property
	def numEdges(self)->int:
		"""Number of edges."""
	@property
	def numFaceVertices(self)->int:
		"""Total number of vertices within faces. Shared vertices are counted
		for each face which uses them."""
	@property
	def numNormals(self)->int:
		"""Number of per-polygon per-vertex normals."""
	@property
	def numPolygons(self)->int:
		"""Number of polygons (faces)."""
	@property
	def numUVSets(self)->int:
		"""Number of UV (texture coordinate) sets."""
	@property
	def numVertices(self)->int:
		"""Number of distinct vertices. Shared vertices are only counted once."""
	kAlpha:int=1
	kRGB:int=3
	kRGBA:int=4
	kOnEdge:int=0
	kInternalPoint:int=1
	kInvalid:int=2
	kUnion:int=1
	kDifference:int=2
	kIntersection:int=3
	kBooleanUnion:int=1
	kBooleanDifferenceAB:int=2
	kBooleanIntersection:int=3
	kBooleanDifferenceBA:int=4
	kBooleanSplit:int=5
	kBooleanSplitEdges:int=6
	kBooleanHolePunch:int=7
	kBooleanCutOut:int=8
	kEdgeClassification:int=1
	kNormalClassification:int=2
	kMeshGeometryMode:int=0
	kLegacyMeshGeometryMode:int=1
	kVolumeGeometryMode:int=2
	kGeomBorder:int=-2
	kUVBorder:int=-1
	kSharedUV:int=0
	kUnsharedUV:int=1
	kInstanceUnspecified:int=-1
	kIntersectTolerance:float=1e-06
	kPointTolerance:float=1e-10
	@overload
	def __init__(self)->None:
		"""Default constructor. Returns a new MFnMesh functionset with no Maya object attached."""
	@overload
	def __init__(self,MObject:Any)->None:
		"""Returns a new MFnMesh object attached to the given mesh node or mesh geometry data."""
	@overload
	def __init__(self,MDagPath:Any)->None:
		"""Returns a new MFnMesh object attached to the given mesh node."""
	@staticmethod
	def autoUniformGridParams()->MMeshIsectAccelParams:
		"""Creates an object which specifies a uniform voxel grid structure which can be used by the intersection routines to speed up their operation. The number of voxel cells to use will be determined automatically based on the density of triangles in the mesh. The grid acceleration structure will be cached with the mesh, so that if the same MMeshIsectAccelParams configuration is used on the next intersect call, the acceleration structure will not need to be rebuilt."""
	@staticmethod
	def clearGlobalIntersectionAcceleratorInfo()->Any:
		"""Clears the "total count", "total build time", and "peak memory" fields from the information string returned by globalIntersectionAcceleratorsInfo() . It will not cause information about currently existing accelerators to be lost."""
	@staticmethod
	def globalIntersectionAcceleratorsInfo()->str:
		"""Returns a string that describes the systemwide resource usage for cached mesh intersection accelerators. The string will be of the following form: total 10 accelerators created (2 currently active - total current memory = 10000KB), total build time = 10.2s, peak memory = 14567.1KB This means that: a total of 10 intersection accelerators have been created as instructed by calls to closestIntersection() , allIntersections() , or anyIntersection() with non-NULL accelParams values. These structures are destroyed and re-created when intersection requests with differing acceleration parameters are passed in for the same mesh, so it is useful to see this value, which is the total count of how many have been created. In this case, 8 of the 10 created have been destroyed, either automatically or via calls to the freeCachedIntersectionAccelerator() method the total memory footprint for the 2 accelerators currently in existence is 10,000KB the total build time for all 10 structures that have been created is 10.2 seconds the peak of total memory usage for all accelerators in the system was 14567.1KB Calling clearGlobalIntersectionAcceleratorInfo() will clear the "total count", "total build time", and "peak memory" fields from this information. It will not cause information about currently existing accelerators to be lost."""
	@staticmethod
	def uniformGridParams(xDiv:int,yDiv:int,zDiv:int)->MMeshIsectAccelParams:
		"""Creates an object which specifies a uniform voxel grid structure which can be used by the intersection routines to speed up their operation. This object specifies the number of voxel cells to be used in the x, y, and z dimensions. The grid acceleration structure will be cached with the mesh, so that if the same MMeshIsectAccelParams configuration is used on the next intersect call, the acceleration structure will not need to be rebuilt."""
	def addHoles(self,faceIndex:int,vertices:Any,loopCounts:Any,mergeVertices:Any=True,pointTolerance:float=MFnMesh.kPointTolerance)->Self:
		"""addHoles(faceIndex, vertices, loopCounts, mergeVertices=True, pointTolerance=kPointTolerance) -> self

		Adds holes to a mesh polygon.
		loopCounts is an array of vertex counts.
		The first entry gives the count of vertices that make up the
		first hole to add to the polygon (using that many entries in vertexArray). The following
		entries in loopCounts give the count of vertices that make up each remaining hole,
		using the following entries in vertexArray.
		Therefore the sum of the entries of loopCounts should equal the total
		length of vertexArray.
		Note that holes should normally be specified with the opposite winding order
		to the exterior polygon."""
	def addPolygon(self,vertices:Sequence[MPoint],mergeVertices:bool=True,pointTolerance:float=MFnMesh.kPointTolerance)->int:
		"""Adds a new polygon to the mesh, returning the index of the new polygon. If mergeVertices is True and a new vertex is within pointTolerance of an existing one, then they are "merged" by reusing the existing vertex and discarding the new one."""
	def allIntersections(self,raySource:MFloatPoint,rayDirection:MFloatVector,space:int,maxParam:float,testBothDirections:bool,faceIds:Sequence[int]|None=None,triIds:Sequence[int]|None=None,idsSorted:bool=False,accelParams:MMeshIsectAccelParams|None=None,tolerance:float=MFnMesh.kIntersectTolerance,sortHits:bool=False)->tuple[hitPoints,hitRayParams,hitFaces,hitTriangles,hitBary1s,hitBay2s]:
		"""Finds all intersection of a ray starting at raySource and travelling in rayDirection with the mesh. If faceIds is specified, then only those faces will be considered for intersection. If both faceIds and triIds are given, then the triIds will be interpreted as face-relative and each pair of entries will be taken as a (face,triangle) pair to be considered for intersection. Thus, the face-triangle pair (10,0) means the first triangle on face 10. If neither faceIds nor triIds is given, then all face-triangles in the mesh will be considered. The maxParam and testBothDirections flags can be used to control the radius of the search around the raySource point. The search proceeds by testing all applicable face-triangles looking for intersections. If the accelParams parameter is given then the mesh builds an intersection acceleration structure based on it. This acceleration structure is used to speed up the intersection operation, sometimes by a factor of several hundred over the non-accelerated case. Once created, the acceleration structure is cached, and will be reused the next time this method (or anyIntersection() or allIntersections() ) is called with an identically-configured MMeshIsectAccelParams object. If a different MMeshIsectAccelParams object is used, then the acceleration structure will be deleted and re-created according to the new settings. Once created, the acceleration structure will persist until either the object is destroyed (or rebuilt by a construction history operation), or the freeCachedIntersectionAccelerator() method is called. The cachedIntersectionAcceleratorInfo() and globalIntersectionAcceleratorsInfo() methods provide useful information about the resource usage of individual acceleration structures, and of all such structures in the system. If the ray hits the mesh, the details of the intersection points will be returned as a tuple containing the following: hitPoints ( MFloatPointArray ) - coordinates of the points hit, in the space specified by the caller. hitRayParams ( MFloatArray ) - parametric distances along the ray to the points hit. hitFaces ( MIntArray ) - IDs of the faces hit hitTriangles ( MIntArray ) - face-relative IDs of the triangles hit hitBary1s ( MFloatArray ) - first barycentric coordinate of the points hit. If the vertices of the hitTriangle are (v1, v2, v3) then the barycentric coordinates are such that the hitPoint = (*hitBary1)*v1 + (*hitBary2)*v2 + (1-*hitBary1-*hitBary2)*v3. hitBary2s ( MFloatArray ) - second barycentric coordinate of the points hit. If no point was hit then the arrays will all be empty."""
	def anyIntersection(self,raySource:MFloatPoint,rayDirection:MFloatVector,space:int,maxParam:float,testBothDirections:bool,faceIds:Sequence[int]|None=None,triIds:Sequence[int]|None=None,idsSorted:bool=False,accelParams:MMeshIsectAccelParams|None=None,tolerance:float=MFnMesh.kIntersectTolerance)->tuple[hitPoint,hitRayParam,hitFace,hitTriangle,hitBary1,hitBay2]|None:
		"""Finds any intersection of a ray starting at raySource and travelling in rayDirection with the mesh. If faceIds is specified, then only those faces will be considered for intersection. If both faceIds and triIds are given, then the triIds will be interpreted as face-relative and each pair of entries will be taken as a (face,triangle) pair to be considered for intersection. Thus, the face-triangle pair (10,0) means the first triangle on face 10. If neither faceIds nor triIds is given, then all face-triangles in the mesh will be considered. The maxParam and testBothDirections flags can be used to control the radius of the search around the raySource point. The search proceeds by testing all applicable face-triangles looking for intersections. If the accelParams parameter is given then the mesh builds an intersection acceleration structure based on it. This acceleration structure is used to speed up the intersection operation, sometimes by a factor of several hundred over the non-accelerated case. Once created, the acceleration structure is cached, and will be reused the next time this method (or anyIntersection() or allIntersections() ) is called with an identically-configured MMeshIsectAccelParams object. If a different MMeshIsectAccelParams object is used, then the acceleration structure will be deleted and re-created according to the new settings. Once created, the acceleration structure will persist until either the object is destroyed (or rebuilt by a construction history operation), or the freeCachedIntersectionAccelerator() method is called. The cachedIntersectionAcceleratorInfo() and globalIntersectionAcceleratorsInfo() methods provide useful information about the resource usage of individual acceleration structures, and of all such structures in the system. If the ray hits the mesh, the details of the intersection point will be returned as a tuple containing the following: hitPoint ( MFloatPoint ) - coordinate of the point hit, in the space specified by the caller. hitRayParam (float) - parametric distance along the ray to the point hit. hitFace (int) - ID of the face hit hitTriangle (int) - face-relative ID of the triangle hit hitBary1 (float) - first barycentric coordinate of the point hit. If the vertices of the hitTriangle are (v1, v2, v3) then the barycentric coordinates are such that hitPoint = (*hitBary1)*v1 + (*hitBary2)*v2 + (1-*hitBary1-*hitBary2)*v3. hitBary2 (float) - second barycentric coordinate of the point hit. If no point was hit then None will be returned."""
	def assignColor(self,faceId:int,vertexIndex:int,colorId:int,colorSet:str='')->Self:
		"""Assigns a color from a colorSet to a specified vertex of a face."""
	def assignColors(self,colorIds:Sequence[int],colorSet:str='')->Self:
		"""Assigns colors to all of the mesh's face-vertices. The colorIds sequence must contain an entry for every vertex of every face, in face order, meaning that the entries for all the vertices of face 0 come first, followed by the entries for the vertices of face 1, etc."""
	def assignUV(self,faceId:int,vertexIndex:int,uvId:int,uvSet:str='')->Self:
		"""Assigns a UV coordinate to a specified vertex of a polygon."""
	def assignUVs(self,uvCounts:Sequence[int],uvIds:Sequence[int],uvSet:str='')->Self:
		"""Assigns UV coordinates to the mesh's face-vertices."""
	def booleanOp(self,op:int,mesh1:MFnMesh,mesh2:MFnMesh)->Self:
		"""Replaces this mesh's geometry with the result of a boolean operation on the two specified meshes."""
	def booleanOps(self,arg:int,MObjectArray:Any,bool:bool)->Self:
		"""booleanOps(Boolean Operation constant, MObjectArray, bool) -> self

		Replaces this mesh's geometry with the result of a boolean operation
		on the specified meshes."""
	def booleanOperations(self,arg:int,MObjectArray:Any)->Self:
		"""booleanOperations(Boolean Operation constant, MObjectArray) -> self

		Replaces this mesh's geometry with the result of a boolean operation
		on the specified meshes."""
	def cachedIntersectionAcceleratorInfo(self)->str:
		"""Retrieves a string that describes the intersection acceleration structure for this object, if any. The string will be of the following form: 10x10x10 uniform grid, (build time 0.5s), (memory footprint 2000KB) It describes the configuration of the cached intersection accelerator, as well as how long it took to build it, and how much memory it is currently occupying. If the mesh has no cached intersection accelerator, the empty string is returned."""
	def cleanupEdgeSmoothing(self)->Self:
		"""Updates the mesh after setEdgeSmoothing has been done. This should be called only once, after all the desired edges have been had their smoothing set. If you don't call this method, the normals may not be correct, and the object will look odd in shaded mode"""
	@overload
	def clearBlindData(self,compType:int)->Self:
		"""Deletes all blind data from all the mesh's components of a given type."""
	@overload
	def clearBlindData(self,compType:int,blindDataId:int,compId:int|None=None,attr:str='')->Self:
		"""Deletes values of the specified blind data type from the mesh's components of a given type. If a component ID is provided then the data is only deleted from that component, otherwise it is deleted from all of the mesh's components of the specified type. If a blind data attribute name is provided then only data for that attribute is deleted, otherwise data for all of the blind data type's attributes is deleted."""
	def clearColors(self,colorSet:str='')->Self:
		"""Clears out all colors from a colorSet, and leaves behind an empty colorset. This method should be used if it is needed to shrink the actual size of the color set. In this case, the user should call clearColors() , setColors() and then assignColors() to rebuild the mapping info. When called on mesh data, the colors are removed. When called on a shape with no history, the colors are removed and the attributes are set on the shape. When called on a shape with history, the polyColorDel command is invoked and a polyColorDel node is created."""
	def clearUVs(self,uvSet:str='')->Self:
		"""Clears out all texture coordinates from the mesh, and leaves behind an empty UVset. This method should be used if it is needed to shrink the actual size of the UV table. In this case, the user should call clearUVs() , setUVs() and then assignUVs() to rebuild the mapping info. When called on mesh data, the UVs are removed. When called on a shape with no history, the UVs are removed and the attributes are set on the shape. When called on a shape with history, the polyMapDel command is invoked and a polyMapDel node is created."""
	def closestIntersection(self,raySource:MFloatPoint,rayDirection:MFloatVector,space:int,maxParam:float,testBothDirections:bool,faceIds:Sequence[int]|None=None,triIds:Sequence[int]|None=None,idsSorted:bool=False,accelParams:MMeshIsectAccelParams|None=None,tolerance:float=MFnMesh.kIntersectTolerance)->tuple[hitPoint,hitRayParam,hitFace,hitTriangle,hitBary1,hitBay2]|None:
		"""Finds the closest intersection of a ray starting at raySource and travelling in rayDirection with the mesh. If faceIds is specified, then only those faces will be considered for intersection. If both faceIds and triIds are given, then the triIds will be interpreted as face-relative and each pair of entries will be taken as a (face,triangle) pair to be considered for intersection. Thus, the face-triangle pair (10,0) means the first triangle on face 10. If neither faceIds nor triIds is given, then all face-triangles in the mesh will be considered. The maxParam and testBothDirections flags can be used to control the radius of the search around the raySource point. The search proceeds by testing all applicable face-triangles looking for intersections. If the accelParams parameter is given then the mesh builds an intersection acceleration structure based on it. This acceleration structure is used to speed up the intersection operation, sometimes by a factor of several hundred over the non-accelerated case. Once created, the acceleration structure is cached, and will be reused the next time this method (or anyIntersection() or allIntersections() ) is called with an identically-configured MMeshIsectAccelParams object. If a different MMeshIsectAccelParams object is used, then the acceleration structure will be deleted and re-created according to the new settings. Once created, the acceleration structure will persist until either the object is destroyed (or rebuilt by a construction history operation), or the freeCachedIntersectionAccelerator() method is called. The cachedIntersectionAcceleratorInfo() and globalIntersectionAcceleratorsInfo() methods provide useful information about the resource usage of individual acceleration structures, and of all such structures in the system. If the ray hits the mesh, the details of the closest intersection point to the raySource will be returned as a tuple containing the following: hitPoint ( MFloatPoint ) - coordinate of the point hit, in the space specified by the caller. hitRayParam (float) - parametric distance along the ray to the point hit. hitFace (int) - ID of the face hit hitTriangle (int) - face-relative ID of the triangle hit hitBary1 (float) - first barycentric coordinate of the point hit. If the vertices of the hitTriangle are (v1, v2, v3) then the barycentric coordinates are such that hitPoint = (*hitBary1)*v1 + (*hitBary2)*v2 + (1-*hitBary1-*hitBary2)*v3. hitBary2 (float) - second barycentric coordinate of the point hit. If no point was hit then None will be returned."""
	def collapseEdges(self,edges:Sequence[int])->Self:
		"""Collapses edges into vertices. The two vertices that create each given edge are replaced in turn by one vertex placed at the average of the two initial vertex."""
	def collapseFaces(self,faces:Sequence[int])->Self:
		"""Collapses faces into vertices. Adjacent faces will be collapsed together into a single vertex. Non-adjacent faces will be collapsed into their own, separate vertices."""
	def copy(self,source:MObject,parent:MObject=MObject.kNullObj)->MObject:
		"""Creates a new mesh with the same geometry as the source. Raises TypeError if the source is not a mesh node or mesh data object or it contains an empty mesh. If the parent is a kMeshData wrapper (e.g. from MFnMeshData.create() ) then a mesh data object will be created and returned and the wrapper will be set to reference it. If the parent is a transform type node then a mesh node will be created and parented beneath it and the return value will be the mesh node. If the parent is any other type of node a TypeError will be raised. If no parent is provided then a transform node will be created and returned and a mesh node will be created and parented under the transform."""
	def copyInPlace(self,source:MObject)->Self:
		"""Replaces the current mesh's geometry with that from the source. Raises TypeError if the source is not a mesh node or mesh data object or it contains an empty mesh."""
	def copyUVSet(self,fromName:str,toName:str,modifier:MDGModifier|None=None)->str:
		"""Copies the contents of one UV set into another. If the source UV set does not exist, or if it has the same name as the destination, then no copy will be made. If the destination UV set exists then its contents will be replace by a copy of the source UV set. If the destination UV set does not exist then a new UV set will be created and the source UV set will be copied into it. The name of the UV set will be that provided with a number appended to the end to ensure uniqueness. The final name of the destination UV set will be returned. This method is only valid for functionsets which are attached to mesh nodes, not mesh data."""
	def create(self,vertices:Sequence[MPoint|MFloatPoint],polygonCounts:Sequence[int],polygonConnects:Sequence[int],uValues:Sequence[float]|None=None,vValues:Sequence[float]|None=None,parent:MObject=MObject.kNullObj)->MObject:
		"""Creates a new polygonal mesh and sets this function set to operate on it. This method is meant to be as efficient as possible and thus assumes that all the given data is topologically correct. If UV values are supplied both parameters must be given and they must contain the same number of values, otherwise IndexError will be raised. Note that the UVs are simply stored in the mesh, not assigned to any vertices. To assign them use assignUVs() . If the parent is a kMeshData wrapper (e.g. from MFnMeshData.create() ) then a mesh data object will be created and returned and the wrapper will be set to reference it. If the parent is a transform type node then a mesh node will be created and parented beneath it and the return value will be the mesh node. If the parent is any other type of node a TypeError will be raised. If no parent is provided then a transform node will be created and returned and a mesh node will be created and parented under the transform."""
	def createBlindDataType(self,blindDataId:int,attrs:Sequence[tuple[str|str|str,...]])->Self:
		"""Create a new blind data type with the specified attributes. Each element of the attrs sequence is a tuple containing the long name, short name and type name of the attribute. Valid type names are "int", "float", "double", "boolean", "string" or "binary". Raises RuntimeError if the blind data id is already in use or an invalid format was specified."""
	def createColorSet(self,name:str,clamped:bool,rep:int=MFnMesh.kRGBA,modifier:MDGModifier|None=None,instances:Sequence[int]|None=None)->str:
		"""Creates a new, empty color set for this mesh. If no name is provided "colorSet#" will be used, where # is a number that makes the name unique for this mesh. If a name is provided but it conflicts with that of an existing color set then a number will be appended to the proposed name to make it unique. The return value is the final name used for the new color set. This method will only work when the functionset is attached to a mesh node, not mesh data."""
	def createInPlace(self,vertices:Sequence[MPoint|MFloatPoint],polygonCounts:Sequence[int],polygonConnects:Sequence[int])->Self:
		"""Replaces the existing polygonal mesh with a new one. This method is meant to be as efficient as possible and thus assumes that all the given data is topologically correct."""
	def createUVSet(self,name:str,modifier:MDGModifier|None=None,instances:Sequence[int]|None=None)->str:
		"""Creates a new, empty UV set for this mesh. If a UV set with proposed name already exists then a number will be appended to the proposed name to name it unique. If the proposed name is empty then a name of the form uvSet# will be used where '#' is a number chosen to ensure that the name is unique. The name used for the UV set will be returned. This method is only valid for functionsets which are attached to mesh nodes, not mesh data."""
	def currentColorSetName(self,instance:int=MFnMesh.kInstanceUnspecified)->str:
		"""Get the name of the "current" color set. The current color set is the one used for color operations when no color set is explicitly specified. On instanced meshes, color sets may be applied on a per-instance basis or may be shared across all instances. When the color sets are per-instance, the concept of the current color set has two levels of granularity. Namely, the current color set applies to one or more instances, plus there are other color sets in the same color set family that apply to different instances. The instance arguement is used to indicate that if this is a per-instance color set, you are interested in the name of the color set that applies to the specified instance. When the index is not specified, the current color set will be returned regardless of which instance it is for. If there is no current color set, then an empty string will be returned."""
	def currentUVSetName(self,instance:int=MFnMesh.kInstanceUnspecified)->str:
		"""Get the name of the "current" uv set. The current uv set is the one used for uv operations when no uv set is explicitly specified. On instanced meshes, uv sets may be applied on a per-instance basis or may be shared across all instances. When the uv sets are per-instance, the concept of the current uv set has two levels of granularity. Namely, the current uv set applies to one or more instances, plus there are other uv sets in the same uv set family that apply to different instances. The instance arguement is used to indicate that if this is a per-instance uv set, you are interested in the name of the uv set that applies to the specified instance. When the index is not specified, the current uv set will be returned regardless of which instance it is for. If there is no current uv set, then an empty string will be returned."""
	def deleteColorSet(self,colorSet:str,modifier:MDGModifier|None=None,currentSelection:MSelectionList|None=None)->Self:
		"""Deletes a color set from the mesh. This method is only valid for functionsets which are attached to mesh nodes, not mesh data."""
	def deleteUVSet(self,uvSet:str,modifier:MDGModifier|None=None,currentSelection:MSelectionList|None=None)->Self:
		"""Deletes a named uv set from the mesh. This method is only valid for functionsets which are attached to mesh nodes, not mesh data."""
	def deleteEdge(self,edgeId:int,modifier:MDGModifier|None=None)->Self:
		"""Deletes the specified edge."""
	def deleteFace(self,faceId:int,modifier:MDGModifier|None=None)->Self:
		"""Deletes the specified face."""
	def deleteVertex(self,vertexId:int,modifier:MDGModifier|None=None)->Self:
		"""Deletes the specified vertex."""
	def duplicateFaces(self,faces:Sequence[int],translation:MFloatVector|None=None)->Self:
		"""Duplicates a set of faces and detaches them from the rest of the mesh. The resulting mesh will contain one more independant piece of geometry."""
	def extractFaces(self,faces:Sequence[int],translation:MFloatVector|None=None)->Self:
		"""Detaches a set of faces from the rest of the mesh. The resulting mesh will contain one more independant piece of geometry."""
	def extrudeEdges(self,edges:Sequence[int],extrusionCount:int=1,translation:MFloatVector|None=None,extrudeTogether:bool=True)->Self:
		"""Extrude the given edges along a vector. The resulting mesh will have extra parallelograms coming out of the given edges and going to the new extruded edges. The length of the new polygon is determined by the length of the vector. The extrusionCount parameter is the number of subsequent extrusions per edges and represents the number of polygons that will be created from each given edge to the extruded edges."""
	def extrudeFaces(self,faces:Sequence[int],extrusionCount:int=1,translation:MFloatVector|None=None,extrudeTogether:bool=True)->Self:
		"""Extrude the given faces along a vector. The resulting mesh will have extra parallelograms coming out of the given faces and going to the new extruded faces. The length of the new polygon is determined by the length of the vector. The extrusionCount parameter is the number of subsequent extrusions per faces and represents the number of polygons that will be created from each given face to the extruded faces."""
	def freeCachedIntersectionAccelerator(self)->Self:
		"""If the mesh has a cached intersection accelerator structure, then this routine forces it to be deleted. Ordinarily, these structures are cached so that series of calls to the closestIntersection() , allIntersections() , and anyIntersection() methods can reuse the same structure. Once the client is finished with these intersection operations, however, they are responsible for freeing the acceleration structure, which is what this method does."""
	def generateSmoothMesh(self,parent:MObject=MObject.kNullObj,options:MMeshSmoothOptions|None=None)->MObject:
		"""Creates a new polygonal mesh which is a smoothed version of the one to which the functionset is attached. If an options object is supplied it will be used to direct the smoothing operation, otherwise the mesh's Smooth Mesh Preview attributes will be used. If the parent is a kMeshData wrapper (e.g. from MFnMeshData.create() ) then a mesh data object will be created and returned. If the parent is a transform type node then a mesh node will be created and parented beneath it and the return value will be the mesh node. If the parent is any other type of node a TypeError will be raised. If no parent is provided then a transform node will be created and returned and a mesh node will be created and parented under the transform. Note that, unlike the create functions, this function does not set the functionset to operate on the new mesh, but leaves it attached to the original mesh."""
	def getAssignedUVs(self,uvSet:str='')->tuple[MIntArray,MIntArray]:
		"""Returns a tuple containing all of the UV assignments for the specified UV set. The first element of the tuple is an array of counts giving the number of UVs assigned to each face of the mesh. The count will either be zero, indicating that that face's vertices do not have UVs assigned, or else it will equal the number of the face's vertices. The second element of the tuple is an array of UV IDs for all of the face-vertices which have UVs assigned."""
	def getAssociatedColorSetInstances(self,colorSet:str)->MIntArray:
		"""Returns the instance numbers associated with the specified Color set. If the color map is shared across all instances, an empty array will be returned. This method will only work if the functionset is attached to a mesh node. It will raise RuntimeError if the functionset is attached to mesh data."""
	def getAssociatedUVSetInstances(self,uvSet:str)->MIntArray:
		"""Returns the instance numbers associated with the specified UV set. If the uv map is shared across all instances, an empty array will be returned. This method will only work if the functionset is attached to a mesh node. It will raise RuntimeError if the functionset is attached to mesh data."""
	def getAssociatedUVSetTextures(self,uvSet:str)->MObjectArray:
		"""Returns the texture nodes which are using the specified UV set. If the texture has a 2d texture placement, the texture, and not the placement will be returned. This method will only work if the functionset is attached to a mesh node. It will raise RuntimeError if the functionset is attached to mesh data."""
	@overload
	def getBinaryBlindData(self,compId:int,compType:int,blindDataId:int,attr:str)->str:
		"""Returns the value of the specified blind data attribute from the specified mesh component. Raises RuntimeError if the attribute is not of "binary" type."""
	@overload
	def getBinaryBlindData(self,compType:int,blindDataId:int,attr:str)->tuple[MIntArray,list[str]]:
		"""Returns a tuple containing an array of component IDs and an array of values for the specified blind data attribute for all of the mesh's components of the specified type. Raises RuntimeError if the attribute is not of "binary" type."""
	def getBinormals(self,space:int=MSpace.kObject,uvSet:str='')->MFloatVectorArray:
		"""Returns the binormal vectors for all face vertices. This method is not threadsafe."""
	def getBlindDataAttrNames(self,blindDataId:int)->tuple[tuple[str,str,str],...]:
		"""Returns a tuple listing the attributes of the given blind data type. Each element of the tuple is itself a tuple containing the long name, short name and type name of the attribute. Type names can be "int", "float", "double", "boolean", "string" or "binary\""""
	def getBlindDataTypes(self,compType:int)->MIntArray:
		"""Returns all the blind data ID's associated with the given component type on this mesh."""
	@overload
	def getBoolBlindData(self,compId:int,compType:int,blindDataId:int,attr:str)->bool:
		"""Returns the value of the specified blind data attribute from the specified mesh component. Raises RuntimeError if the attribute is not of "bool" type."""
	@overload
	def getBoolBlindData(self,compType:int,blindDataId:int,attr:str)->tuple[MIntArray,MIntArray]:
		"""Returns a tuple containing an array of component IDs and an array of values for the specified blind data attribute for all of the mesh's components of the specified type. Raises RuntimeError if the attribute is not of "bool" type."""
	def getClosestUVs(self,u:Any,v:Any,uvSet:Any='')->MIntArray:
		"""getClosestUVs(u, v, uvSet='') -> MIntArray

		Returns the IDs of the UVs which are nearest in uv space to the
		given texture coordinate in the specified UV set. All these UVs
		locate at the same distance to the given coordinate."""
	def intersectFaceAtUV(self,u:Any,v:Any,uvSet:Any='')->int:
		"""intersectFaceAtUV(u, v, uvSet='') -> int

		Returns the IDs of the UVs on this surface which are nearest
		in uv space to the given uv set and coordinate.All these UVs
		locate at the same distance to the given coordinate.

		This method is not threadsafe."""
	def getClosestNormal(self,point:MPoint,space:int=MSpace.kObject)->tuple[MVector,int]:
		"""Returns a tuple containing the normal at the closest point on the mesh to the given point and the ID of the face in which that closest point lies."""
	def getClosestPoint(self,point:MPoint,space:int=MSpace.kObject)->tuple[MPoint,int]:
		"""Returns a tuple containing the closest point on the mesh to the given point and the ID of the face in which that closest point lies. This method is not threadsafe."""
	def getClosestPointAndNormal(self,point:MPoint,space:int=MSpace.kObject)->tuple[MPoint,MVector,int]:
		"""Returns a tuple containing the closest point on the mesh to the given point, the normal at that point, and the ID of the face in which that point lies. This method is not threadsafe."""
	def getColor(self,colorId:int,colorSet:str='')->MColor:
		"""Returns a color from a colorSet. Raises IndexError if the colorId is out of range."""
	def getColorIndex(self,faceId:int,localVertexIndex:int,colorSet:str='')->int:
		"""Returns the index into the specified colorSet of the color used by a specific face-vertex. This can be used to index into the sequence returned by getColors() ."""
	def getColorRepresentation(self,colorSet:str)->int:
		"""Returns the Color Representation used by the specified color set."""
	def getColors(self,colorSet:str='')->MColorArray:
		"""Returns all of the colors in a colorSet. If no colorSet is specified then the default colorSet is used. Use the index returned by getColorIndex() to access the returned array."""
	def getColorSetFamilyNames(self)->tuple[str,...]:
		"""Returns the names of all of the color set families on this object. A color set family is a set of per-instance sets with the same name with each individual set applying to one or more instances. A set which is shared across all instances will be the sole member of its family. Given a color set family name, getColorSetsInFamily() may be used to determine the names of the associated individual sets."""
	def getColorSetNames(self)->tuple[str,...]:
		"""Returns the names of all the color sets on this object."""
	def getColorSetsInFamily(self,familyName:str)->tuple[str,...]:
		"""Returns the names of all of the color sets that belong to the specified family. Per-instance sets will have multiple sets in a family, with each individual set applying to one or more instances. A set which is shared across all instances will be the sole member of its family and will share the same name as its family."""
	def getConnectedShaders(self,instance:int)->tuple[MObjectArray,MIntArray]:
		"""Returns a tuple containing an array of shaders (sets) and an array of ints mapping the mesh's polygons onto those shaders. For each polygon in the mesh there will be corresponding value in the second array. If it is -1 that means that the polygon is not assigned to a shader, otherwise it indicates the index into the first array of the shader to which that polygon is assigned. This method will only work if the functionset is attached to a mesh node. It will raise RuntimeError if the functionset is attached to mesh data."""
	def getCreaseEdges(self)->tuple[MUintArray,MDoubleArray]:
		"""Returns a tuple containing two arrays. The first contains the mesh-relative/global IDs of the mesh's creased edges and the second contains the associated crease data. Please note that to make effective use of the creasing variable in software outside of Maya may require a license under patents owned by Pixar(R)."""
	def getCreaseVertices(self)->tuple[MUintArray,MDoubleArray]:
		"""Returns a tuple containing two arrays. The first contains the mesh-relative/global IDs of the mesh's creased vertices and the second contains the associated crease data. Please note that to make effective use of the creasing variable in software outside of Maya may require a license under patents owned by Pixar(R)."""
	@overload
	def getDoubleBlindData(self,compId:int,compType:int,blindDataId:int,attr:str)->float:
		"""Returns the value of the specified blind data attribute from the specified mesh component. Raises RuntimeError if the attribute is not of "double" type."""
	@overload
	def getDoubleBlindData(self,compType:int,blindDataId:int,attr:str)->tuple[MIntArray,MDoubleArray]:
		"""Returns a tuple containing an array of component IDs and an array of values for the specified blind data attribute for all of the mesh's components of the specified type. Raises RuntimeError if the attribute is not of "double" type."""
	def getEdgeVertices(self,edgeId:int)->tuple[int,int]:
		"""Returns a tuple containing the mesh-relative/global IDs of the edge's two vertices. The indices can be used to refer to the elements in the array returned by the getPoints() method."""
	def getFaceAndVertexIndices(self,faceVertexIndex:int,localVertex:bool=True)->tuple[faceId,int]:
		"""Returns a tuple containg the faceId and vertexIndex represented by the given face-vertex index. This is the reverse of the operation performed by getFaceVertexIndex() . If localVertex is True then the returned vertexIndex is the face-relative/local index, otherwise it is the mesh-relative/global index."""
	def getFaceNormalIds(self,faceId:int)->MIntArray:
		"""Returns the IDs of the normals for all the vertices of a given face. These IDs can be used to index into the arrays returned by getNormals() ."""
	def getFaceUVSetNames(self,faceId:int)->tuple[str,...]:
		"""Returns the names of all of the uv sets mapped to the specified face. This method is not threadsafe."""
	def getFaceVertexBinormal(self,faceId:int,vertexId:int,space:int=MSpace.kObject,uvSet:str='')->MVector:
		"""Returns the binormal vector at a given face vertex. This method is not threadsafe."""
	def getFaceVertexBinormals(self,faceId:int,space:int=MSpace.kObject,uvSet:str='')->MFloatVectorArray:
		"""Returns all the per-vertex-per-face binormals for a given face. This method is not threadsafe."""
	def getFaceVertexColors(self,colorSet:str='',defaultUnsetColor:MColor|None=None)->MColorArray:
		"""Returns colors for all the mesh's face-vertices. The colors are returned in face order: e.g. F0V0, F0V1.. F0Vn, F1V0, etc... Use the index returned by getFaceVertexIndex() if you wish to index directly into the returned color array. If no face has color for that vertex, the entry returned will be defaultUnsetColor. If a color was set for some but not all the faces for that vertex, the ones where the color has not been explicitly set will return (0,0,0). If a vertex has shared color, the same value will be set for all its vertes/faces. If the colorSet is not specified, the default color set will be used. If the defaultUnsetColor is not given, then (-1, -1, -1, -1) will be used."""
	def getFaceVertexIndex(self,faceId:int,vertexIndex:int,localVertex:bool=True)->int:
		"""Returns the index for a specific face-vertex into an array of face-vertex values, such as those returned by getFaceVertexBinormals() , getFaceVertexColors() , getFaceVertexNormals() , etc. The values in the target arrays are presumed to be in face order: e.g. F0V0, F0V1.. F0Vn, F1V0, etc... If localVertex is True then vertexIndex must be a face-relative/local index. If localVertex is False then vertexIndex must be a mesh-relative/global index. The opposite operation is performed by the getFaceAndVertexIndices() method."""
	def getFaceVertexNormal(self,faceId:int,vertexId:int,space:int=MSpace.kObject)->MVector:
		"""Returns the per-vertex-per-face normal for a given face and vertex. This method is not threadsafe."""
	def getFaceVertexNormals(self,faceId:int,space:int=MSpace.kObject)->MFloatVectorArray:
		"""Returns the normals for a given face. This method is not threadsafe."""
	def getFaceVertexTangent(self,faceId:int,vertexId:int,space:int=MSpace.kObject,uvSet:str='')->MVector:
		"""Return the normalized tangent vector at a given face vertex. The tangent is defined as the surface tangent of the polygon running in the U direction defined by the uv map. This method is not threadsafe."""
	def getFaceVertexTangents(self,faceId:int,space:int=MSpace.kObject,uvSet:str='')->MFloatVectorArray:
		"""Returns all the per-vertex-per-face tangents for a given face. The tangent is defined as the surface tangent of the polygon running in the U direction defined by the uv map. This method is not threadsafe."""
	@overload
	def getFloatBlindData(self,compId:int,compType:int,blindDataId:int,attr:str)->float:
		"""Returns the value of the specified blind data attribute from the specified mesh component. Raises RuntimeError if the attribute is not of "float" type."""
	@overload
	def getFloatBlindData(self,compType:int,blindDataId:int,attr:str)->tuple[MIntArray,MFloatArray]:
		"""Returns a tuple containing an array of component IDs and an array of values for the specified blind data attribute for all of the mesh's components of the specified type. Raises RuntimeError if the attribute is not of "float" type."""
	def getFloatPoints(self,space:int=MSpace.kObject)->MFloatPointArray:
		"""Returns a copy of the mesh's vertex positions as an MFloatPointArray ."""
	def getHoles(self)->tuple[tuple[face,tuple[v1,...]],...]:
		"""Returns a tuple describing the holes in the mesh. Each element of the tuple is itself a tuple. The first element of the sub-tuple is the integer ID of the face in which the hole occurs. The second element of the sub-tuple is another tuple containing the mesh-relative/global IDs of the vertices which make up the hole. Take the following return value as an example: ((3, (7, 2, 6)), (5, (11, 10, 3, 4))) This says that the mesh has two holes. The first hole is in face 3 and consists of vertices 7, 2 and 6. The second hole is in face 5 and consists of vertices 11, 10, 3 and 4."""
	@overload
	def getIntBlindData(self,compId:int,compType:int,blindDataId:int,attr:str)->int:
		"""Returns the value of the specified blind data attribute from the specified mesh component. Raises RuntimeError if the attribute is not of "int" type."""
	@overload
	def getIntBlindData(self,compType:int,blindDataId:int,attr:str)->tuple[MIntArray,MIntArray]:
		"""Returns a tuple containing an array of component IDs and an array of values for the specified blind data attribute for all of the mesh's components of the specified type. Raises RuntimeError if the attribute is not of "int" type."""
	def getInvisibleFaces(self)->MUintArray:
		"""Returns the invisible faces of the mesh. Invisible faces are like lightweight holes in that they are not rendered but do not require additional geometry the way that holes do. They have the advantage over holes that if the mesh is smoothed then their edges will be smoothed as well, while holes will retain their hard edges. Invisible faces can be set using the setInvisibleFaces() method or the polyHole command."""
	def getNormalIds(self)->tuple[MIntArray,MIntArray]:
		"""Returns the normal IDs for all of the mesh's polygons as a tuple of two int arrays. The first array contains the number of vertices for each polygon and the second contains the normal IDs for each polygon-vertex. These IDs can be used to index into the array returned by getNormals() ."""
	def getNormals(self,space:int=MSpace.kObject)->MFloatVectorArray:
		"""Returns a copy of the mesh's normals. The normals are the per-polygon per-vertex normals. To find the normal for a particular vertex-face, use getFaceNormalIds() to get the index into the array. This method is not threadsafe."""
	def getPoint(self,vertexId:int,space:int=MSpace.kObject)->MPoint:
		"""Returns the position of specified vertex."""
	def getPointAtUV(self,faceId:int,u:float,v:float,space:int=MSpace.kObject,uvSet:str='',tolerance:float=0.0)->MPoint:
		"""Returns the position of the point at the give UV value in the specified face. This method is not threadsafe."""
	def getPointsAtUV(self,u:Any,v:Any,space:Any=MSpace.kObject,uvSet:Any='',tolerance:Any=0.001)->tuple[MIntArray,MPointArray]:
		"""getPointsAtUV(u, v, space=MSpace.kObject, uvSet='', tolerance=0.001) -> (MIntArray, MPointArray)

		Returns the polygon ids and positions of points at the given UV position on the mesh."""
	def getPoints(self,space:int=MSpace.kObject)->MPointArray:
		"""Returns a copy of the mesh's vertex positions as an MPointArray ."""
	def getPolygonNormal(self,polygonId:int,space:int=MSpace.kObject)->MVector:
		"""Returns the per-polygon normal for the given polygon. This method is not threadsafe."""
	def getPolygonTriangleVertices(self,polygonId:int,triangleId:int)->tuple[int,int,int]:
		"""Returns the mesh-relative/global IDs of the 3 vertices of the specified triangle of the specified polygon. These IDs can be used to index into the arrays returned by getPoints() and getFloatPoints() ."""
	def getPolygonUV(self,polygonId:int,vertexId:int,uvSet:str='')->tuple[float,float]:
		"""Returns a tuple containing the U and V values at a specified vertex of a specified polygon. This method is not threadsafe."""
	def getPolygonUVid(self,polygonId:int,vertexId:int,uvSet:str='')->int:
		"""Returns the ID of the UV at a specified vertex of a specified polygon. This method is not threadsafe."""
	def getPolygonVertices(self,polygonId:int)->MIntArray:
		"""Returns the mesh-relative/global vertex IDs the specified polygon. These IDs can be used to index into the arrays returned by getPoints() and getFloatPoints() ."""
	def getSmoothMeshDisplayOptions(self)->MMeshSmoothOptions:
		"""Returns the options currently in use when smoothing the mesh for display."""
	@overload
	def getStringBlindData(self,compId:int,compType:int,blindDataId:int,attr:str)->str:
		"""Returns the value of the specified blind data attribute from the specified mesh component. Raises RuntimeError if the attribute is not of "string" type."""
	@overload
	def getStringBlindData(self,compType:int,blindDataId:int,attr:str)->tuple[MIntArray,list[str]]:
		"""Returns a tuple containing an array of component IDs and an array of values for the specified blind data attribute for all of the mesh's components of the specified type. Raises RuntimeError if the attribute is not of "string" type."""
	def getTangentId(self,faceId:int,vertexId:int)->int:
		"""Returns the ID of the tangent for a given face and vertex."""
	def getTangents(self,space:int=MSpace.kObject,uvSet:str='')->MFloatVectorArray:
		"""Return the tangent vectors for all face vertices. The tangent is defined as the surface tangent of the polygon running in the U direction defined by the uv map. This method is not threadsafe."""
	def getTriangles(self)->tuple[MIntArray,MIntArray]:
		"""Returns a tuple describing the mesh's triangulation. The first element of the tuple is an array giving the number of triangles for each of the mesh's polygons. The second tuple gives the ids of the vertices of all the triangles."""
	def getUV(self,uvId:int,uvSet:str='')->tuple[float,float]:
		"""Returns a tuple containing the u and v values of the specified UV."""
	def getUVAtPoint(self,point:MPoint,space:int=MSpace.kObject,uvSet:str='')->tuple[float,float,int]:
		"""Returns a tuple containing the u and v coordinates of the point on the mesh closest to the given point, and the ID of the face containing that closest point. This method is not threadsafe."""
	def getUVs(self,uvSet:str='')->tuple[MFloatArray,MFloatArray]:
		"""Returns a tuple containing an array of U values and an array of V values, representing all of the UVs for the given UV set."""
	def getUVSetFamilyNames(self)->tuple[str,...]:
		"""Returns the names of all of the uv set families on this object. A uv set family is a set of per-instance sets with the same name with each individual set applying to one or more instances. A set which is shared across all instances will be the sole member of its family. Given a uv set family name, getUVSetsInFamily() may be used to determine the names of the associated individual sets."""
	def getUVSetNames(self)->tuple[str,...]:
		"""Returns the names of all the uv sets on this object."""
	def getUVSetsInFamily(self,familyName:str)->tuple[str,...]:
		"""Returns the names of all of the uv sets that belong to the specified family. Per-instance sets will have multiple sets in a family, with each individual set applying to one or more instances. A set which is shared across all instances will be the sole member of its family and will share the same name as its family."""
	def getUvShellsIds(self,uvSet:str='')->tuple[int,MIntArray]:
		"""Returns a tuple containing describing how the specified UV set's UVs are grouped into shells. The first element of the tuple is the number of distinct shells. The second element of the tuple is an array of shell indices, one per uv, indicating which shell that uv is part of."""
	def getMeshShellsIds(self,compType:Any)->tuple[int,MIntArray]:
		"""getMeshShellsIds(compType) -> (int, MIntArray)

		Returns a tuple containing describing how the specified component type items
		are grouped into shells. The first element of the tuple is the number
		of distinct shells. The second element of the tuple is an array of
		shell indices, one per component, indicating which shell that component is part of."""
	def getVertexColors(self,colorSet:str='',defaultUnsetColor:MColorArray|None=None)->MColorArray:
		"""Gets colors for all vertices of the given colorSet. If no face has color for that vertex, the entry returned will be defaultUnsetColor. If a color was set for some or all the faces for that vertex, an average of those vertex/face values where the color has been set will be returned. If the colorSet is not specified, the default color set will be used. If the defaultUnsetColor is not given, then (-1, -1, -1, -1) will be used."""
	def getVertexNormal(self,vertexId:int,angleWeighted:bool,space:int=MSpace.kObject)->MVector:
		"""Returns the normal at the given vertex. The returned normal is a single per-vertex normal, so unshared normals at a vertex will be averaged. If angleWeighted is set to true, the normals are computed by an average of surrounding face normals weighted by the angle subtended by the face at the vertex. If angleWeighted is set to false, a simple average of surround face normals is returned. The simple average evaluation is significantly faster than the angle-weighted average. This method is not threadsafe."""
	def getVertexNormals(self,angleWeighted:bool,space:int=MSpace.kObject)->MFloatVectorArray:
		"""Returns all the vertex normals. The returned normals are per-vertex normals, so unshared normals at a vertex will be averaged. If angleWeighted is set to True, the normals are computed by an average of surrounding face normals weighted by the angle subtended by the face at the vertex. If angleWeighted is set to false, a simple average of surround face normals is returned. The simple average evaluation is significantly faster than the angle-weighted average. This method is not threadsafe."""
	def getVertices(self)->tuple[MIntArray,MIntArray]:
		"""Returns the mesh-relative/global vertex IDs for all of the mesh's polygons as a tuple of two int arrays. The first array contains the number of vertices for each polygon and the second contains the mesh-relative IDs for each polygon-vertex. These IDs can be used to index into the arrays returned by getPoints() and getFloatPoints() ."""
	def getTriangleOffsets(self)->tuple[MIntArray,MIntArray]:
		"""getTriangleOffsets() -> (MIntArray, MIntArray)

		Returns the number of triangles for every polygon face and the
		offset into the vertex indices array for each triangle vertex (see getVertices()).
		The triangleVertices array holds each vertex for each triangle in sequence,
		so it has three times as many elements as there are triangles.
		(i.e. three times the sum of the elements of the triangleCounts array)"""
	def hasAlphaChannels(self,colorSet:str)->bool:
		"""Returns True if the color set has an alpha channel."""
	def hasBlindData(self,compId:int,compType:int|None=None,blindDataId:int|None=None)->bool:
		"""Returns true if any component of the given type on this mesh has blind data. If a component ID is provided then only that particular component is checked. If a blind data ID is provided then only blind data of that type is checked."""
	def hasColorChannels(self,colorSet:str)->bool:
		"""Returns True if the color set has RGB channels."""
	def isBlindDataTypeUsed(self,blindDataId:int)->bool:
		"""Returns True if the blind data type is already in use anywhere in the scene."""
	def isColorClamped(self,colorSet:str)->bool:
		"""Returns True if the color sets RGBA components are clamped to the range 0 to 1."""
	def isColorSetPerInstance(self,name:str)->bool:
		"""Returns True if the color set is per-instance, and False if it is shared across all instances."""
	def edgeBorderInfo(self,edgeId:Any,setId:Any=0)->Any:
		"""edgeBorderInfo(edgeId, setId=0) -> MFnMesh::BorderInfo

		Returns if the specified edge is on geom/UV shell border or has shared/unshared UVs."""
	def getUVBorderEdges(self,setId:Any)->MIntArray:
		"""getUVBorderEdges(setId) -> MIntArray

		Retrieves the edge indices for edges lying on a UV border."""
	def isEdgeSmooth(self,edgeId:int)->bool:
		"""Returns True if the edge is smooth, False if it is hard."""
	def isNormalLocked(self,normalId:int)->bool:
		"""Returns True if the normal is locked, False otherwise."""
	def isPolygonConvex(self,faceId:int)->bool:
		"""Returns True if the polygon is convex, False if it is concave."""
	def isPolygonUVReversed(self,faceId:Any)->bool:
		"""isPolygonUVReversed(faceId) -> bool

		Returns True if the texture coordinates (uv's) for specified polygon are
		reversed (clockwise), False if they are not reversed (counter clockwise)."""
	def isRightHandedTangent(self,tangentId:Any,uvSet:Any='')->bool:
		"""isRightHandedTangent(tangentId, uvSet='') -> bool

		Returns True if the normal, tangent, and binormal form a right handed
		coordinate system, False otherwise."""
	def isUVSetPerInstance(self,name:str)->bool:
		"""Returns True if the UV set is per-instance, and False if it is shared across all instances."""
	def lockFaceVertexNormals(self,faceIds:Sequence[int],vertexIds:Sequence[int])->Self:
		"""Locks the normals for the given face/vertex pairs."""
	def lockVertexNormals(self,vertexIdx:Sequence[int])->Self:
		"""Locks the shared normals for the specified vertices."""
	def numColors(self,colorSet:str='')->int:
		"""Returns the number of colors in the given color set. If no color set is specified then the mesh's current color set will be used."""
	def numUVs(self,uvSet:str='')->int:
		"""Returns the number of UVs (texture coordinates) in the given UV set. If no UV set is specified then the mesh's current UV set will be used."""
	def onBoundary(self,faceId:int)->bool:
		"""Returns true if the face is on the border of the mesh, meaning that one or more of its edges is a border edge."""
	def polygonVertexCount(self,faceId:int)->int:
		"""Returns the number of vertices in the given polygon. Raises ValueError if the polygon ID is invalid."""
	def removeFaceColors(self,faceIds:Sequence[int])->Self:
		"""Removes colors from all vertices of the specified faces."""
	def removeFaceVertexColors(self,faceIds:Sequence[int],vertexIds:Sequence[int])->Self:
		"""Removes colors from the specified face/vertex pairs."""
	def removeVertexColors(self,vertexIds:Sequence[int])->Self:
		"""Removes colors from the specified vertices in all of the faces which share those vertices."""
	def renameUVSet(self,origName:str,newName:str,modifier:MDGModifier|None=None)->Self:
		"""Renames a UV set. The set must exist and the new name cannot be the same as that of an existing set. This method is only valid for functionsets which are attached to mesh nodes, not mesh data."""
	@overload
	def setBinaryBlindData(self,compId:int,compType:int,blindDataId:int,attr:str,data:str)->Self:
		"""Sets the value of a "binary" blind data attribute on a component of the mesh."""
	@overload
	def setBinaryBlindData(self,compIds:Sequence[int],compType:int,blindDataId:int,attr:str,data:str|Sequence[str])->Self:
		"""Sets the value of a "binary" blind data attribute on multiple components of the mesh. If the data is a sequence of strings then it must provide a value for each component in compIds. If it is a single string then all of the specified components will have their blind data set to that value."""
	@overload
	def setBoolBlindData(self,compId:int,compType:int,blindDataId:int,attr:str,data:bool|int)->Self:
		"""Sets the value of a "boolean" blind data attribute on a component of the mesh."""
	@overload
	def setBoolBlindData(self,compIds:Sequence[int],compType:int,blindDataId:int,attr:str,data:bool|int|Sequence[bool]|ints)->Self:
		"""Sets the value of a "boolean" blind data attribute on multiple components of the mesh. If the data is a sequence then it must provide a value for each component in compIds. If it is a single value then all of the specified components will have their blind data set to that value."""
	def setColor(self,colors:Sequence[MColor],color:MColor,colorSet:str='',rep:int=MFnMesh.kRGBA)->Self:
		"""Sets a color in the specified colorSet. If no colorSet is given the current colorSet will be used. If the colorId is greater than or equal to numColors() then the colorSet will be grown to accommodate the specified color."""
	def setColors(self,colors:Sequence[MColor],colorSet:str='',rep:int=MFnMesh.kRGBA)->Self:
		"""Sets all the colors of the specified colorSet. If no colorSet is given the current colorSet will be used. After using this method to set the color values, you can call assignColors() to assign the corresponding color ids to the geometry. The color sequence must be at least as large as the current color set size. You can determine the color set size by calling numColors() for the default color set, or numColors(colorSet) for a named color set. If the sequence is larger than the color set size, then the color set for this mesh will be expanded to accommodate the new color values. In order to shrink the colorSet you have to clear its existing colors. E.g: clearColors() setColors( ... ) assignColors()"""
	def setCreaseEdges(self,edgeIds:Sequence[int],creaseData:Sequence[float])->Self:
		"""Sets the specified edges of the mesh as crease edges. Please note that to make effective use of the creasing variable in software outside of Maya may require a license under patents owned by Pixar(R)."""
	def setCreaseVertices(self,vertexIds:Sequence[int],creaseData:Sequence[float])->Self:
		"""Sets the specified vertices of the mesh as crease vertices. Please note that to make effective use of the creasing variable in software outside of Maya may require a license under patents owned by Pixar(R)."""
	def setCurrentColorSetName(self,colorSet:str,modifier:MDGModifier|None=None,currentSelection:MSelectionList|None=None)->Self:
		"""Sets the "current" color set for this object. The current color set is the one used when no color set name is specified for a color operation. If the specified color set does not exist then the current color set will not be changed. This method is only valid for functionsets which are attached to mesh nodes, not mesh data."""
	def setCurrentUVSetName(self,uvSet:str,modifier:MDGModifier|None=None,currentSelection:MSelectionList|None=None)->Self:
		"""Sets the "current" uv set for this object. The current uv set is the one used when no uv set name is specified for a uv set operation. If the specified uv set does not exist then the current uv set will not be changed. This method is only valid for functionsets which are attached to mesh nodes, not mesh data."""
	@overload
	def setDoubleBlindData(self,compId:int,compType:int,blindDataId:int,attr:str,data:float)->Self:
		"""Sets the value of a "double" blind data attribute on a component of the mesh."""
	@overload
	def setDoubleBlindData(self,compIds:Sequence[int],compType:int,blindDataId:int,attr:str,data:float|Sequence[float])->Self:
		"""Sets the value of a "double" blind data attribute on multiple components of the mesh. If the data is a sequence then it must provide a value for each component in compIds. If it is a single value then all of the specified components will have their blind data set to that value."""
	def setEdgeSmoothing(self,edgeId:int,smooth:bool=True)->Self:
		"""Sets the specified edge to be hard or smooth. You must use the cleanupEdgeSmoothing() method after all the desired edges on your mesh have had setEdgeSmoothing() done. Use the updateSurface() method to indicate the mesh needs to be redrawn."""
	def setEdgeSmoothings(self,edgeIds:Any,smooths:Any)->Self:
		"""setEdgeSmoothings(edgeIds, smooths) -> self

		Sets the specified edges to be hard or smooth. You must use the
		cleanupEdgeSmoothing() method after all the desired edges on your
		mesh have had setEdgeSmoothings() done. Use the updateSurface() method
		to indicate the mesh needs to be redrawn."""
	def setFaceColor(self,color:MColor,faceId:int,rep:int=MFnMesh.kRGBA)->Self:
		"""Sets the face-vertex color for all vertices on this face."""
	def setFaceColors(self,colors:Sequence[MColor],faceIds:Sequence[int],rep:int=MFnMesh.kRGBA)->Self:
		"""Sets the colors of the specified faces. For each face in the faceIds sequence the corresponding color from the colors sequence will be applied to all of its vertices."""
	def setFaceVertexColor(self,color:MColor,faceId:int,vertexId:int,modifier:MDGModifier|None=None,rep:int=MFnMesh.kRGBA)->Self:
		"""Sets a face-specific normal at a vertex."""
	def setFaceVertexColors(self,colors:Sequence[MColor],faceIds:Sequence[int],vertexIds:Sequence[int],modifier:MDGModifier|None=None,rep:int=MFnMesh.kRGBA)->Self:
		"""Sets the colors of the specified face/vertex pairs."""
	def setFaceVertexNormal(self,normal:MVector,faceId:int,vertexId:int,space:int=MSpace.kObject,modifier:MDGModifier|None=None)->Self:
		"""Sets a face-specific normal at a vertex."""
	def setFaceVertexNormals(self,normals:Sequence[MVector],faceIds:Sequence[int],vertexIds:Sequence[int],space:int=MSpace.kObject)->Self:
		"""Sets normals for the given face/vertex pairs."""
	@overload
	def setFloatBlindData(self,compId:int,compType:int,blindDataId:int,attr:str,data:float)->Self:
		"""Sets the value of a "float" blind data attribute on a component of the mesh."""
	@overload
	def setFloatBlindData(self,compIds:Sequence[int],compType:int,blindDataId:int,attr:str,data:float|Sequence[float])->Self:
		"""Sets the value of a "float" blind data attribute on multiple components of the mesh. If the data is a sequence then it must provide a value for each component in compIds. If it is a single value then all of the specified components will have their blind data set to that value."""
	@overload
	def setIntBlindData(self,compId:int,compType:int,blindDataId:int,attr:str,data:int)->Self:
		"""Sets the value of an "int" blind data attribute on a component of the mesh."""
	@overload
	def setIntBlindData(self,compIds:Sequence[int],compType:int,blindDataId:int,attr:str,data:int|Sequence[int])->Self:
		"""Sets the value of an "int" blind data attribute on multiple components of the mesh. If the data is a sequence then it must provide a value for each component in compIds. If it is a single value then all of the specified components will have their blind data set to that value."""
	def setInvisibleFaces(self,faceIds:Sequence[int],makeVisible:bool=False)->Self:
		"""Sets the specified faces of the mesh to be visible or invisible. See the getInvisibleFaces() method for a description of invisible faces."""
	def setIsColorClamped(self,colorSet:str,clamped:bool)->Self:
		"""Sets whether the color set's RGBA components should be clamped to the range 0 to 1."""
	def setNormals(self,normals:Sequence[MFloatVector],space:int=MSpace.kObject)->Self:
		"""Sets the mesh's normals (user normals)."""
	def setPoint(self,vertexId:int,point:MPoint,space:int=MSpace.kObject)->Self:
		"""Sets the position of specified vertex. Note that if you modify the position of a vertex for a mesh node (as opposed to mesh data), a tweak will be created. If you have a node with no history, the first time that a tweak is created, the underlying pointers under the MFnMesh object may change. You will need to call syncObject() to make sure that the object is valid. Subsequent calls to setPoint() on the same object do not require a syncObject() call."""
	def setPoints(self,points:Sequence[MPoint|MFloatPoint],space:int=MSpace.kObject)->Self:
		"""Sets the positions of the mesh's vertices."""
	def setSmoothMeshDisplayOptions(self,options:MMeshSmoothOptions)->Self:
		"""Sets the options to use when smoothing the mesh for display."""
	def setSomeColors(self,colorIds:Sequence[int],colors:Sequence[MColor],colorSet:str='',rep:int=MFnMesh.kRGBA)->Self:
		"""Sets selected colors in a colorSet. If the largest colorId in the sequence is larger than numColors() then the colorSet will be grown to accommodate the new color values. If you have added new colorIds, you can call assignColors to assign the colorIds to the geometry. If you are modifying existing colors, they will already be referenced by the existing mesh data."""
	def setSomeUVs(self,uvIds:Sequence[int],uValues:Sequence[float],vValues:Sequence[float],uvSet:str='')->Self:
		"""Sets the specified texture coordinates (uv's) for this mesh. The uv value sequences and the uvIds sequence must all be of equal size. If the largest uvId in the array is larger than numUVs() then the uv list for this mesh will be grown to accommodate the new uv values. If a named uv set is given, the array will be grown when the largest uvId is larger than numUVs(uvSet). If you have added new uvIds, you must call one of the assignUV methods to assign the uvIds to the geometry. If you are modifying existing UVs, you do not need to call one of the assignUV methods."""
	@overload
	def setStringBlindData(self,compId:int,compType:int,blindDataId:int,attr:str,data:str)->Self:
		"""Sets the value of a "string" blind data attribute on a component of the mesh."""
	@overload
	def setStringBlindData(self,compIds:Sequence[int],compType:int,blindDataId:int,attr:str,data:str|Sequence[str])->Self:
		"""Sets the value of a "string" blind data attribute on multiple components of the mesh. If the data is a sequence of strings then it must provide a value for each component in compIds. If it is a single string then all of the specified components will have their blind data set to that value."""
	def setUV(self,uvId:int,u:float,v:float,uvSet:str='')->Self:
		"""Sets the specified texture coordinate. The uvId is the element in the uv list that will be set. If the uvId is greater than or equal to numUVs() then the uv list will be grown to accommodate the specified uv. If the UV being added is new, then you must call one of the assignUV methods in order to update the geometry."""
	def setUVs(self,uValues:Sequence[float],vValues:Sequence[float],uvSet:str='')->Self:
		"""Sets all of the texture coordinates (uv's) for this mesh. The uv value sequences must be of equal size and must be at least as large as the current UV set size. You can determine the UV set size by calling numUVs() for the default UV set, or numUVs(uvSet) for a named UV set. If the sequences are larger than the UV set size, then the uv list for this mesh will be grown to accommodate the new uv values. After using this method to set the UV values, you must call one of the assignUV methods to assign the corresponding UV ids to the geometry. In order to shrink the uvs array, do the following: clearUVs() setUVs( ... ) assignUVs() These steps will let you to create an array of uvs which is smaller than the original one."""
	def setVertexColor(self,color:MColor,vertexId:int,modifier:MDGModifier|None=None,rep:int=MFnMesh.kRGBA)->Self:
		"""Sets the color for a vertex in all the faces which share it."""
	def setVertexColors(self,color:Sequence[MColor],vertexIds:Sequence[int],modifier:MDGModifier|None=None,rep:int=MFnMesh.kRGBA)->Self:
		"""Sets the colors of the specified vertices. For each vertex in the vertexIds sequence, the corresponding color from the colors sequence will be applied to the vertex in all of the faces which share it."""
	def setVertexNormal(self,normal:MVector,vertexId:int,space:int=MSpace.kObject,modifier:MDGModifier|None=None)->Self:
		"""Sets the shared normal at a vertex."""
	def setVertexNormals(self,normals:Sequence[MVector],vertexIds:Sequence[int],space:int=MSpace.kObject)->Self:
		"""Sets the shared normals for the given vertices."""
	def sortIntersectionFaceTriIds(self,faceIds:MIntArray,triIds:MIntArray=none)->Self:
		"""Convenience routine for sorting faceIds or face/triangle ids before passing them into the closestIntersection() , allIntersections() , or anyIntersection() methods. When using an acceleration structure with an intersection operation it is essential that any faceId or faceId/triId arrays be sorted properly to ensure optimal performance."""
	def split(self,placements:Sequence[tuple])->Self:
		"""Each tuple in the placements sequence consists of a Split Placement constant followed by one or two parameters. If the Split Placement is kOnEdge then the tuple will contain two more elements giving the int id of the edge to split, and a float value between 0 and 1 indicating how far along the edge to do the split. The same edge cannot be split more than once per call. If the Split Placement is kInternalPoint then the tuple will contain just one more element giving an MFloatPoint within the face. All splits must begin and end on an edge meaning that the first and last tuples in the placements sequence must be kOnEdge placements."""
	def subdivideEdges(self,edges:Sequence[int],numDivisions:int)->Self:
		"""Subdivides edges at regular intervals. For example, if numDivisions is 2 then two equally-spaced vertices will be added to each of the specified edges: one 1/3 of the way along the edge and a second 2/3 of the way along the edge."""
	def subdivideFaces(self,faces:Sequence[int],numDivisions:int)->Self:
		"""Subdivides each specified face into a grid of smaller faces. Triangles are subdivided into a grid of smaller triangles and quads are subdivided into a grid of smaller quads. Faces with more than four edges are ignored. The numDivisions parameter tells how many times to subdivide each edge of the face. Internal points and edges are introduced as needed to create a grid of smaller faces."""
	def syncObject(self)->Self:
		"""If a non-api operation happens that many have changed the underlying Maya object attached to this functionset, calling this method will make sure that the functionset picks up those changes. In particular this call should be used after calling mel commands which might affect the mesh. Note that this only applies when the functionset is attached to a mesh node. If it's attached to mesh data the it is not necessary to call this method."""
	def unlockFaceVertexNormals(self,faceIds:Sequence[int],vertexIds:Sequence[int])->Self:
		"""Unlocks the normals for the given face/vertex pairs."""
	def unlockVertexNormals(self,vertexIdx:Sequence[int])->Self:
		"""Unlocks the shared normals for the specified vertices."""
	def updateSurface(self)->Self:
		"""Signal that this polygonal mesh has changed and needs to be redrawn."""
class MFnMeshData(MFnGeometryData):
	"""MFnMeshData allows the creation and manipulation of Mesh
	data objects for use in the dependency graph.

	__init__()
	Initializes a new, empty MFnMeshData object

	__init__(MObject)
	Initializes a new MFnMeshData function set, attached
	to the specified object."""
	@overload
	def __init__(self)->None:
		"""Default constructor. Returns a new, empty MFnMeshData object."""
	@overload
	def __init__(self,obj:MObject)->None:
		"""Returns a new MFnMeshData function set, attached to the specified object."""
	def create(self)->MObject:
		"""Creates a new mesh data object, attaches it to this function set and returns an MObject which references it."""
class MFnMessageAttribute(MFnAttribute):
	"""Functionset for creating and working with message attributes."""
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def create(self,longName:str,shortName:str)->MObject:
		"""Create a new message attribute with the given longName and shortName , attach it to the function set and return it in an MObject ."""
class MFnNumericAttribute(MFnAttribute):
	"""Functionset for creating and working with numeric attributes."""
	@property
	def default(self)->float|tuple[float,...]:
		"""Default value"""
	@default.setter
	def default(self,value:float|tuple[float,...])->None:...
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def child(self,index:int)->MObject:
		"""Returns the specified child attribute of the parent attribute currently attached to the function set."""
	def create(self,longName:str,shortName:str,type:int,defaultValue:float=0)->MObject:
		"""Creates a new numeric attribute of the given type with the given longName , shortName and defaultValue , attaches it to the function set and returns it in an MObject ."""
	def createAddr(self,longName:str,shortName:str,defaultValue:int=0)->MObject:
		"""Creates a new address attribute with the given longName , shortName and defaultValue , attaches it to the function set and returns it in an MObject ."""
	def createColor(self,longName:str,shortName:str)->MObject:
		"""Creates a new color attribute with the given longName , shortName , attaches it to the function set and returns it in an MObject ."""
	def createPoint(self,longName:str,shortName:str)->MObject:
		"""Creates a new 3D point attribute with the given longName , shortName , attaches it to the function set and returns it in an MObject ."""
	def getMax(self)->float|tuple[float,...]:
		"""Returns a float representing the attribute's hard maximum value. If the attribute consists of multiple components (e.g. a k3Float attribute) then a tuple containing a separate maximum value for each component will be returned.Raises a RuntimeError if the attribute does not have a hard maximum."""
	def getMin(self)->float|tuple[float,...]:
		"""Returns a float representing the attribute's hard minimum value. If the attribute consists of multiple components (e.g. a k3Float attribute) then a tuple containing a separate minimum value for each component will be returned.Raises a RuntimeError if the attribute does not have a hard minimum."""
	def getSoftMax(self)->float:
		"""Returns the attribute's soft maximum value.Raises a RuntimeError if the attribute does not have a soft maximum."""
	def getSoftMin(self)->float:
		"""Returns the attribute's soft minimum value.Raises a RuntimeError if the attribute does not have a soft minimum."""
	def hasMax(self)->bool:
		"""Returns True if a hard maximum value has been specified for the attribute."""
	def hasMin(self)->bool:
		"""Returns True if a hard minimum value has been specified for the attribute."""
	def hasSoftMax(self)->bool:
		"""Returns True if a soft maximum value has been specified for the attribute."""
	def hasSoftMin(self)->bool:
		"""Returns True if a soft minimum value has been specified for the attribute."""
	def numericType(self)->int:
		"""Returns the numeric type of the attribute currently attached to the function set."""
	def setMax(self,maxValue:float|Sequence[float])->Self:
		"""Sets the attribute's hard maximum to maxValue . If the attribute consists of multiple components (e.g. a k3Float or color attribute) then maxValue must be a sequence providing a maximum value for each component."""
	def setMin(self,minValue:float|Sequence[float])->Self:
		"""Sets the attribute's hard minimum to minValue . If the attribute consists of multiple components (e.g. a k3Float or color attribute) then minValue must be a sequence providing a minimum value for each component."""
	def setSoftMax(self,maxValue:float)->Self:
		"""Sets the attribute's soft maximum to maxValue ."""
	def setSoftMin(self,minValue:float)->Self:
		"""Sets the attribute's soft minimum to minValue ."""
class MFnNumericData(MFnData):
	"""Function set for non-simple numeric node data."""
	kInvalid:int=0
	kBoolean:int=1
	kByte:int=2
	kChar:int=3
	kShort:int=4
	k2Short:int=5
	k3Short:int=6
	kLong:int=7
	kInt:int=7
	k2Long:int=8
	k2Int:int=8
	k3Long:int=9
	k3Int:int=9
	kInt64:int=10
	kFloat:int=11
	k2Float:int=12
	k3Float:int=13
	kDouble:int=14
	k2Double:int=15
	k3Double:int=16
	k4Double:int=17
	kAddr:int=18
	kLast:int=19
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def create(self,type:int)->MObject:
		"""Creates a new numeric data object of the given type, attaches it to the function set and returns an MObject which references it. Only the multi-value numeric types (e.g. k2Short, k3Short) are accepted. Single-value numeric types (e.g. kShort) can be accessed directly through MPlug and MDataHandle and thus do not require a data object to encapsulate them."""
	def getData(self)->list:
		"""Returns a list containing the encapsulated numeric data's elements. k*Short, k*Int and k*Long types will be returned as Python integers. k*Float and k*Double types will be returned as Python floats."""
	def numericType(self)->int:
		"""Returns the type of numeric data in the object currently attached to the function set."""
	def setData(self,seq:Sequence[Any])->Self:
		"""Replaces the encapsulated data with the elements of the supplied sequence. k*Short, k*Int and k*Long types will accept sequences of Python integers. k*Float and k*Double types will accept sequences of Python floats, integers or a mix of the two. If the sequence contains the wrong number or type of elements then a TypeError will be raised."""
class MFnNurbsCurve(MFnDagNode):
	"""NURBS (Non-Uniform Rational B-Spline) curve function set.

	The shape of a NURBS curve is defined by an array of CVs
	(control vertices), an array of knot values, a degree, and a
	form.  There are 3 possible 'forms' for the curve: open,
	closed and periodic.

	The open and closed forms are quite similar, and in fact a
	closed curve will become an open curve if either the first
	or last CV is moved so that they are no longer coincident.
	To create an open or closed curve of degree N with M spans,
	you must provide M+N CVs.  This implies that for a degree N
	curve, you must specify at least N+1 CVs to get a curve with
	a single span.

	The number of knots required for a curve is M + 2N - 1. If
	you want the curve to start exactly at the first CV and end
	exactly at the last CV, then the knot vector must be
	structured to have degree N 'multiplicity' at the beginning
	and end.  This means that the first N knots must be
	identical, and the last N knots must be identical.

	A periodic curve is a special case of a closed curve.
	Instead of having just the first and last CVs coincident,
	the last N CVs in the curve must overlap the first N CVs.
	This results in a curve with no tangent break at the seam
	where the ends meet.  The last N CVs in a periodic curve are
	permanently bound to the first N CVs, and Maya will not
	allow those last N CVs to be repositioned.  If one or more
	of the first N CVs of the curve are repositioned, the
	overlapping CV's will remain bound, and will also be moved.

	In order to create a periodic curve, you must specify at
	least 2N+1 CVs, so that that last N can overlap the first N
	and you still have 1 non-overlapping CV left.  The number of
	CVs required to create a periodic curve is still N+M (with a
	lower limit of 2N+1), but you must ensure that the positions
	of the last N CVs are identical to the positions of the
	first N.

	You still need M + 2N - 1 knots for a periodic curve, but
	the knot values required are more restrictive than for open
	or closed curves because of the overlap at the ends, The
	difference between the first N pairs of knots values should
	be equal to the difference between the last N pairs.
	Additionally there can be no knot multiplicity at the ends
	of the curve, because that would compromise the tangent
	continuity property. So an example knot sequence could begin
	with knots at { -(N-2), -(N-1), ... , 0}.

	Note that some third party applications use a different
	format for knots, where the number of knots required for a
	curve is M+2N+1 rather than M+2N-1 as used in Maya. Both
	knot representations are equivalent mathematically. To
	convert from one of these external representations into the
	Maya representation, simply omit the first and last knots
	from the external representation when creating the Maya
	representation. To convert from the Maya representation into
	the external representation, add two new knots at the
	beginning and end of the Maya knot sequence. The value of
	these new knots depends on the existing knot sequence. For a
	knot sequence with multiple end knots, simply duplicate the
	existing first and last knots once more, for example:

	Maya representation: {0,0,0,...,N,N,N}
	External representation: {0,0,0,0,...,N,N,N,N}

	For a knot sequence with uniform end knots, create the new
	knots offset at an interval equal to the existing first and
	last knot intervals, for example:

	Maya representation: {0,1,2,...,N,N+1,N+2}
	External representation: {-1,0,1,2,...,N,N+1,N+2,N+3}"""
	@property
	def degree(self)->Any:
		"""The degree of the curve or 0 if the degree cannot be determined."""
	@degree.setter
	def degree(self,value:Any)->None:...
	@property
	def form(self)->Any:
		"""The form of the curve: kOpen, kClosed, kPeriodic or kInvalid"""
	@form.setter
	def form(self,value:Any)->None:...
	@property
	def hasHistoryOnCreate(self)->Any:
		"""True if the curve was created with history."""
	@hasHistoryOnCreate.setter
	def hasHistoryOnCreate(self,value:Any)->None:...
	@property
	def isPlanar(self)->Any:
		"""True if the curve is planar."""
	@isPlanar.setter
	def isPlanar(self,value:Any)->None:...
	@property
	def knotDomain(self)->Any:
		"""A tuple containing a pair of floats corresponding to the maximum and
		minimum parameter values for this curve."""
	@knotDomain.setter
	def knotDomain(self,value:Any)->None:...
	@property
	def numCVs(self)->Any:
		"""Number of CVs in the curve or 0 if the number of CVs cannot be
		determined."""
	@numCVs.setter
	def numCVs(self,value:Any)->None:...
	@property
	def numKnots(self)->Any:
		"""Number of knots in the curve or 0 if the number of knots cannot be
		determined."""
	@numKnots.setter
	def numKnots(self,value:Any)->None:...
	@property
	def numSpans(self)->Any:
		"""Number of spans in the curve or 0 if the number of spans cannot be
		determined."""
	@numSpans.setter
	def numSpans(self,value:Any)->None:...
	@property
	def planeNormal(self)->Any:
		"""MVector of the normal to the plane of the curve, if the curve is
		planar, or None if the curve is not planar."""
	@planeNormal.setter
	def planeNormal(self,value:Any)->None:...
	kInvalid:int=0
	kOpen:int=1
	kClosed:int=2
	kPeriodic:int=3
	kLast:int=4
	kPointTolerance:float=0.001
	kFindParamTolerance:float=1e-06
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def area(self,tolerance:float=MFnMesh.kPointTolerance)->float:
		"""area(tolerance=kPointTolerance) -> float

		Returns the area bounded by the curve. The curve must be closed and
		planar. A value of 0.0 will be returned if area cannot be determined.

		* tolerance (float) - Amount of error allowed in the calculation"""
	def closestPoint(self,testPoint:MPoint,guess:float|None=None,tolerance:float=MFnMesh.kPointTolerance,space:int=MSpace.kObject)->tuple[MPoint,float]:
		"""closestPoint(testPoint, guess=None, tolerance=kPointTolerance,
		    space=kObject) -> (MPoint, float)

		Returns a tuple containing the point on the curve which is closest
		to 'testPoint', and the parameter value at which that point occurs.

		* testPoint (MPoint) - point to get closest to
		* guess      (float) - a guess as to roughly where on the curve the
		                       closest point will be. If the guess is in the
		                       correct span than it can significantly speed
		                       up the search. If not then it may slow down
		                       the search a bit. If no guess is supplied
		                       then the search will begin at the start of
		                       the curve.
		* tolerance  (float) - maximum allowed distance between the curve
		                       and the returned point.
		* space (MSpace constant) - coordinate space to use for the points"""
	def copy(self,source:Any,parent:MObject=MObject.kNullObj)->MObject:
		"""copy(source, parent=MObject.kNullObj) -> MObject

		Returns a new NURBS curve which is a copy of 'source' and resets
		the functionset to operate on it.

		* parent (MObject)
		             - the parent/owner of the new curve. If it's a NURBS
		               curve data wrapper (MFn.kNurbsCurveData) then the
		               created curve will be returned as a geometry object
		               (MFn.kNurbsCurveGeom) owned by the wrapper. If
		               'parent' is a DAG node then the new curve will be
		               returned as nurbsCurve node parented under it. If
		               'parent' is not provided then a new top-level
		               transform will be created with the new curve parented
		               beneath it as a nurbsCurve node. In this last case it
		               will be the transform node which is returned."""
	@overload
	def create(self,cvs:MPointArray|Sequence[MPoint],knots:Any,degree:int,form:int,is2D:Any,rational:bool,parent:MObject=MObject.kNullObj)->Self:
		"""create(cvs, knots, degree, form, is2D, rational, parent=kNullObj)
		    -> self
		create(subCurves, parent=kNullObj) -> self

		Returns a newly created curve and resets the functionset to operate
		on it. The first version creates the curve based on the control
		vertices and knots provided while the second creates the curve as a
		copy of the provided subCurves, all joined together.

		* cvs (MPointArray or seq of MPoint)
		             - positions of the control vertices
		* knots (MDoubleArray seq of float)
		             - parameter values of the knots. There must be
		               (# spans + 2*degree - 1) knots provided and they must
		               appear in non-decreasing order.
		* degree (int) - degree of the curve to create
		* form (int) - one of kOpen, kClosed or kPeriodic
		* is2d (bool)- if True the Z-coordinates of 'cvs' will be ignored,
		               giving a curve in the local XY plane.
		* rational (bool)
		             - set True if you want the new curve to be rational
		* parent (MObject)
		             - the parent/owner of the new curve. If it's a NURBS
		               curve data wrapper (MFn.kNurbsCurveData) then the
		               created curve will be returned as a geometry object
		               (MFn.kNurbsCurveGeom) owned by the wrapper. If
		               'parent' is a DAG node then the new curve will be
		               returned as nurbsCurve node parented under it. If
		               'parent' is not provided then a new top-level
		               transform will be created with the new curve parented
		               beneath it as a nurbsCurve node. In this last case it
		               will be the transform node which is returned.
		* subCurves (MObjectArray or seq of MObject)
		             - array of curves from which the new curve will be built
		               The curves must all be in the same direction, must not
		               intersect themselves or each other, the start of each
		               curve in the array must be coincident with the end of
		               the previous curve in the array, and the curves must be
		               be at least C0 continuous (i.e. tangent breaks are okay)."""
	@overload
	def create(self,subCurves:MObjectArray|Sequence[MObject],parent:MObject=MObject.kNullObj)->Self:
		"""create(cvs, knots, degree, form, is2D, rational, parent=kNullObj)
		    -> self
		create(subCurves, parent=kNullObj) -> self

		Returns a newly created curve and resets the functionset to operate
		on it. The first version creates the curve based on the control
		vertices and knots provided while the second creates the curve as a
		copy of the provided subCurves, all joined together.

		* cvs (MPointArray or seq of MPoint)
		             - positions of the control vertices
		* knots (MDoubleArray seq of float)
		             - parameter values of the knots. There must be
		               (# spans + 2*degree - 1) knots provided and they must
		               appear in non-decreasing order.
		* degree (int) - degree of the curve to create
		* form (int) - one of kOpen, kClosed or kPeriodic
		* is2d (bool)- if True the Z-coordinates of 'cvs' will be ignored,
		               giving a curve in the local XY plane.
		* rational (bool)
		             - set True if you want the new curve to be rational
		* parent (MObject)
		             - the parent/owner of the new curve. If it's a NURBS
		               curve data wrapper (MFn.kNurbsCurveData) then the
		               created curve will be returned as a geometry object
		               (MFn.kNurbsCurveGeom) owned by the wrapper. If
		               'parent' is a DAG node then the new curve will be
		               returned as nurbsCurve node parented under it. If
		               'parent' is not provided then a new top-level
		               transform will be created with the new curve parented
		               beneath it as a nurbsCurve node. In this last case it
		               will be the transform node which is returned.
		* subCurves (MObjectArray or seq of MObject)
		             - array of curves from which the new curve will be built
		               The curves must all be in the same direction, must not
		               intersect themselves or each other, the start of each
		               curve in the array must be coincident with the end of
		               the previous curve in the array, and the curves must be
		               be at least C0 continuous (i.e. tangent breaks are okay)."""
	def createWithEditPoints(self,eps:MPointArray|Sequence[MPoint],degree:int,form:int,is2D:Any,rational:bool,uniform:bool,parent:MObject=MObject.kNullObj)->MObject:
		"""createWithEditPoints(eps, degree, form, is2D, rational, uniform,
		    parent=kNullObj) -> MObject

		Returns a new curve based on the given edit points (i.e. points
		which lie on the curve) and resets the functionset to operate on it.

		* eps (MPointArray or seq of MPoint)
		             - positions of the edit points
		* degree (int) - degree of the curve to create
		* form (int) - one of kOpen, kClosed or kPeriodic
		* is2d (bool)- if True the Z-coordinates of 'eps' will be ignored,
		               giving a curve in the local XY plane.
		* rational (bool)
		             - set True if you want the new curve to be rational
		* uniform (bool)
		             - if True then parameter values of the knots will be
		               uniformly spaced, otherwise they will be based on
		               chord length.
		* parent (MObject)
		             - the parent/owner of the new curve. If it's a NURBS
		               curve data wrapper (MFn.kNurbsCurveData) then the
		               created curve will be returned as a geometry object
		               (MFn.kNurbsCurveGeom) owned by the wrapper. If
		               'parent' is a DAG node then the new curve will be
		               returned as nurbsCurve node parented under it. If
		               'parent' is not provided then a new top-level
		               transform will be created with the new curve parented
		               beneath it as a nurbsCurve node. In this last case it
		               will be the transform node which is returned."""
	def cvPosition(self,index:int,space:int=MSpace.kObject)->MPoint:
		"""cvPosition(index, space=kObject) -> MPoint

		Returns the position of a single control vertex.

		* index (int) - index of the CV to return
		* space (int) - an MSpace constant giving the coordinate space in
		                which the point is given"""
	def cvPositions(self,space:int=MSpace.kObject)->MPointArray:
		"""cvPositions(space=kObject) -> MPointArray

		Returns the positions of all of the curve's control vertices.

		* space (int) - an MSpace constant giving the coordinate space in
		                which the point is given"""
	def cvs(self,startIndex:int,endIndex:int=...)->MObject:
		"""cvs(startIndex[, endIndex]) -> MObject

		Returns a CV or a range of CVs as a component. MItCurveCV can be
		used to examine or modify the CVs in the component. Any modifications
		made to them will affect the curve. After all modifications are done,
		updateCurve() should be called to have the curve recalculate its
		cached geometry.

		* startIndex (int) - start of the range of CVs to return.
		* endIndex   (int) - end of the range of CVs to return. If not
		                     provided then only the CV specified by
		                     startIndex will be returned."""
	def distanceToPoint(self,point:MPoint,space:int=MSpace.kObject)->float:
		"""distanceToPoint(point, space=kObject) -> float

		Returns the distance from the given point to the point on the curve
		which is closest to it.

		* point (MPoint) - the point to calculate the distance to
		* space (int)    - an MSpace constant giving the coordinate space in
		                   which the point is given"""
	def findParamFromLength(self,length:float,tolerance:float=MFnNurbsCurve.kFindParamTolerance)->float:
		"""findParamFromLength(length, tolerance=kFindParamTolerance) -> float

		Returns the parameter value corresponding to a given length along
		the curve. If the parameter value cannot be determined then the value
		for the end point of the curve is returned.

		* length (float) - distance along the curve
		* tolerance (float) - search tolerance"""
	def findLengthFromParam(self,param:float)->float:
		"""findLengthFromParam(param) -> float

		Returns the length along the curve corresponding to a given
		parameter value on the curve. If the length cannot be found for
		the given parameter value then a length of zero is returned.

		* param (float) - parameter value on the curve"""
	def getDerivativesAtParam(self,param:float,space:int=MSpace.kObject)->tuple[MPoint,Any]:
		"""getDerivativesAtParam(param, space=kObject) -> (MPoint, MVector[, MVector])

		Evaluates the curve at the given parameter value, returning a tuple
		containing the position and first derivative at that value. If 'dUU'
		is True then the returned tuple will include the second derivative
		as well as its third element.

		* param (float) - parameter value at which to do the evaluation
		* space   (int) - an MSpace constant giving the coordinate space in
		                  which the point is given
		* dUU    (bool) - if True include the second derivative in the result."""
	def getParamAtPoint(self,point:MPoint,tolerance:float=MFnMesh.kPointTolerance,space:int=MSpace.kObject)->float:
		"""getParamAtPoint(point, tolerance=kPointTolerance, space=kObject) -> float

		Returns the parameter value corresponding to the given point on the
		curve.

		* point    (MPoint) - point on curve.
		* tolerance (float) - max distance 'point' can be from the curve and
		                      still be considered to lie on it.
		* space       (int) - an MSpace constant giving the coordinate space
		                      in which the point is given"""
	def getPointAtParam(self,param:float,space:int=MSpace.kObject)->MPoint:
		"""getPointAtParam(param, space=kObject) -> MPoint

		Returns the point on the curve at the given parameter value.

		* param (float) - parameter value at which to find the point
		* space   (int) - an MSpace constant giving the coordinate space in
		                  which the point should be returned"""
	def isParamOnCurve(self,param:float)->bool:
		"""isParamOnCurve(param) -> bool

		Returns True if the given parameter value lies on the curve (i.e. is
		within the curve's knot domain), False otherwise.

		* param (float) - parameter value to test"""
	def isPointOnCurve(self,point:MPoint,tolerance:float=MFnMesh.kPointTolerance,space:int=MSpace.kObject)->bool:
		"""isPointOnCurve(point, tolerance=kPointTolerance, space=kObject) -> bool

		Returns True if the given point lies on the curve, False otherwise.

		* point    (MPoint) - point to test.
		* tolerance (float) - max distance 'point' can be from the curve and
		                      still be considered to lie on it.
		* space       (int) - an MSpace constant giving the coordinate space
		                      in which the point is given"""
	def knot(self,index:int)->float:
		"""knot(index) -> float

		Returns the parameter value of a single knot.

		* index (int) - index of the knot to return. These range from 0 to
		                (numKnots - 1)"""
	def knots(self)->MDoubleArray:
		"""knots() -> MDoubleArray

		Returns the parameter values for all of the curve's knots."""
	def length(self,tolerance:float=MFnMesh.kPointTolerance)->float:
		"""length(tolerance=kPointTolerance) -> float

		Returns the arc length of this curve or 0.0 if it cannot be computed.

		* tolerance (float) - max error allowed in the calculation."""
	def makeMultipleEndKnots(self)->Self:
		"""makeMultipleEndKnots() -> self

		Sets the curve's end knots to have full multiplicity. This ensures
		that the end points interpolate the first and last CVs (i.e. lie
		directly on them). It can also be used to convert a periodic curve
		to a closed curve."""
	def normal(self,param:float,space:int=MSpace.kObject)->MVector:
		"""normal(param, space=kObject) -> MVector

		Returns the normal at the given parameter value on the curve. For
		degree 1 curves the normal is the vector at right angles to the
		curve that lies in the average plane of the curve. For higher degrees
		the normal is defined by the local curvature at the parameter.

		* param (float) - parameter value at which to find the normal
		* space   (int) - an MSpace constant giving the coordinate space in
		                  which the normal should be returned"""
	def removeKnot(self,param:float,removeAll:bool=False)->Self:
		"""removeKnot(param, removeAll=False) -> self

		Removes one or more knots at the given parameter value.

		If there are multiple knots at the parameter value then 'removeAll'
		determines which ones will be removed. If it is True then they will
		all be removed. If it is False then all but one will be removed.

		* param     (float) - parameter of the knot
		* removeAll  (bool) - how to handle multiple knots at the same param"""
	def reverse(self)->Self:
		"""reverse() -> self

		Reverses the direction of the curve."""
	def setCVPosition(self,index:int,point:MPoint,space:int=MSpace.kObject)->Self:
		"""setCVPosition(index, point, space=kObject) -> self

		Sets the position of a single control vertex of the curve.

		* index    (int) - index of the cv
		* point (MPoint) - new position for the cv
		* space    (int) - an MSpace constant giving the coordinate space
		                   in which the point is given"""
	def setCVPositions(self,points:MPointArray|Sequence[MPoint],space:int=MSpace.kObject)->Self:
		"""setCVPositions(points, space=kObject) -> self

		Sets the positions of all of the curve's control vertices.

		* points (MPointArray or seq of MPoint)
		               - the points to be set. The array/sequence must
		                 contain exactly the same number of points as the
		                 curve has control vertices.
		* space  (int) - an MSpace constant giving the coordinate space
		                 in which the points are given"""
	def setKnot(self,index:int,param:float)->Self:
		"""setKnot(index, param) -> self

		Sets the parameter value of a single knot.
		* index   (int) - index of the knot
		* param (float) - new parameter value for the knot"""
	def setKnots(self,params:Any,startIndex:int,endIndex:int)->Self:
		"""setKnots(params, startIndex, endIndex) -> self

		Sets the parameter values of a contiguous group of knots.

		* params (MDoubleArray of seq of float)
		                   - the parameter values to set, one per knot in
		                     the range
		* startIndex (int) - first knot in the range to be set
		* endIndex   (int) - last knot in the range to be set"""
	def tangent(self,param:float,space:int=MSpace.kObject)->MVector:
		"""tangent(param, space=kObject) -> MVector

		Returns the normalized tangent vector at the given parameter value
		on the curve.

		* param (float) - parameter value at which to find the tangent
		* space   (int) - an MSpace constant giving the coordinate space in
		                  which the tangent should be returned"""
	def updateCurve(self)->Self:
		"""updateCurve() -> self

		Tells the shape node which represents the curve in the scene, if
		any, that the curve has changed and needs to be redrawn."""
class MFnNurbsCurveData(MFnGeometryData):
	"""MFnNurbsCurveData allows the creation and manipulation of Nurbs Curve
	data objects for use in the dependency graph.

	__init__()
	Initializes a new, empty MFnNurbsCurveData object

	__init__(MObject)
	Initializes a new MFnNurbsCurveData function set, attached
	to the specified object."""
	@overload
	def __init__(self)->None:
		"""Default constructor. Returns a new, empty MFnNurbsCurveData object."""
	@overload
	def __init__(self,obj:MObject)->None:
		"""Returns a new MFnNurbsCurveData function set, attached to the specified object."""
	def create(self)->MObject:
		"""Creates a new nurbs curve data object, attaches it to this function set and returns an MObject which references it."""
class MFnNurbsSurface(MFnDagNode):
	"""NURBS (Non-Uniform Rational B-Spline) surface function set.

	The shape of a NURBS surface is defined by an array of CVs
	(control vertices), an array of knot values in the U direction
	and an array of knot values in the V direction, a degree in U
	and in V, and a form in U and in V.

	The U and V knot vectors for NURBS surfaces are of size
	(spansInU + 2*degreeInU -1) and (spansInV + 2*degreeInV -1).
	Note: spans = numCVs - degree.

	There are 3 possible forms for the surface in the U and V
	directions: open, closed and periodic. These forms are described
	below. Note that the descriptions below apply to both the U and
	V directions.

	The open and closed forms are quite similar, and in fact a
	closed surface will become an open surface if either the first
	or last CV is moved so that they are no longer coincident. To
	create an open or closed surface, of degree N, with M spans, you
	must provide M+N CVs. This implies that for a degree N surface,
	you must specify at least N+1 CVs to get a surface with a single
	span.

	The number of knots required for the surface is M + 2N - 1.  If
	you want the surface to start exactly at the first CV and end
	exactly at the last CV, then the knot vector must be structured
	to have degree N multiplicity at the beginning and end. This
	means that the first N knots must be identical, and the last N
	knots must be identical.

	A periodic surface is a special case of a closed surface.
	Instead of having just the first and last CVs coincident, the
	last N CVs in the surface, where N is equal to the degree,
	overlap the first N CVs. This results in a surface with no
	tangent break where the ends meet. The last N CVs in a periodic
	surface are permanently bound to the first N CVs, and Maya will
	not allow those last N CVs to be repositioned. If one or more
	of the first N CVs of the surface are repositioned, the
	overlapping CV's will remain bound, and will also be moved.

	In order to create a periodic surface, you must specify at least
	2N+1 CVs, so that that last N can overlap the first N and you
	still have 1 non-overlapping CV left.  The number of CVs
	required to create a periodic surface is still N+M (with a
	lower limit of 2N+1), but you must ensure that the positions
	of the last N CVs are identical to the positions of the
	first N.

	You still need M + 2N - 1 knots for a periodic surface, but
	the knot values required are more restrictive than for open
	or closed surfaces because of the overlap of the last N CVs.
	The first N knots should be specified at the beginning of
	the knot array as values { -(N-1), -(N-2), ... 0 } in order
	to implement the overlap.  Additionally there can be no knot
	multiplicity at the end of the surface, because that would
	compromise the tangent continuity property.

	Note that some third party applications use a different
	format for knots, where the number of knots required for a
	surface is M+2N+1 rather than M+2N-1 as used in Maya. Both
	knot representations are equivalent mathematically. To
	convert from one of these external representations into the
	Maya representation, simply omit the first and last knots
	from the external representation when creating the Maya
	representation. To convert from the Maya representation into
	the external representation, add two new knots at the
	beginning and end of the Maya knot sequence. The value of
	these new knots depends on the existing knot sequence. For a
	knot sequence with multiple end knots, simply duplicate the
	existing first and last knots once more, for example:

	Maya representation: {0,0,0,...,N,N,N}
	External representation: {0,0,0,0,...,N,N,N,N}

	For a knot sequence with uniform end knots, create the new
	knots offset at an interval equal to the existing first and
	last knot intervals, for example:

	Maya representation: {0,1,2,...,N,N+1,N+2}
	External representation: {-1,0,1,2,...,N,N+1,N+2,N+3}"""
	@property
	def dataObject(self)->Any:
		"""If the functionset was created using an MFn.kNurbsSurfaceData object
		then this attribute will contain an MObject which references that
		data object. Otherwise it will contain MObject.kNullObj."""
	@dataObject.setter
	def dataObject(self,value:Any)->None:...
	@property
	def degreeInU(self)->Any:
		"""The degree of the surface in the U direction or 0 if the degree
		cannot be determined."""
	@degreeInU.setter
	def degreeInU(self,value:Any)->None:...
	@property
	def degreeInV(self)->Any:
		"""The degree of the surface in the V direction or 0 if the degree
		cannot be determined."""
	@degreeInV.setter
	def degreeInV(self,value:Any)->None:...
	@property
	def formInU(self)->Any:
		"""Form of the surface in the U direction. Can be one of kOpen,
		kClosed, kPeriodic or kInvalid."""
	@formInU.setter
	def formInU(self,value:Any)->None:...
	@property
	def formInV(self)->Any:
		"""Form of the surface in the V direction. Can be one of kOpen,
		kClosed, kPeriodic or kInvalid."""
	@formInV.setter
	def formInV(self,value:Any)->None:...
	@property
	def hasHistoryOnCreate(self)->Any:
		"""True if the surface was created with history."""
	@hasHistoryOnCreate.setter
	def hasHistoryOnCreate(self,value:Any)->None:...
	@property
	def isBezier(self)->Any:
		"""True if the knot spacing gives a Bezier surface."""
	@isBezier.setter
	def isBezier(self,value:Any)->None:...
	@property
	def isFoldedOnBispan(self)->Any:
		"""True if surface contains are any folds or creases on bispan
		boundaries, including trimmed regions."""
	@isFoldedOnBispan.setter
	def isFoldedOnBispan(self,value:Any)->None:...
	@property
	def isTrimmedSurface(self)->Any:
		"""True if the surface is a trimmed surface."""
	@isTrimmedSurface.setter
	def isTrimmedSurface(self,value:Any)->None:...
	@property
	def isUniform(self)->Any:
		"""True if the knot spacing is uniform."""
	@isUniform.setter
	def isUniform(self,value:Any)->None:...
	@property
	def knotDomainInU(self)->Any:
		"""A tuple containing a pair of floats corresponding to the maximum and
		minimum U parameter values for this surface."""
	@knotDomainInU.setter
	def knotDomainInU(self,value:Any)->None:...
	@property
	def knotDomainInV(self)->Any:
		"""A tuple containing a pair of floats corresponding to the maximum and
		minimum V parameter values for this surface."""
	@knotDomainInV.setter
	def knotDomainInV(self,value:Any)->None:...
	@property
	def numCVsInU(self)->Any:
		"""Number of CVs in the surface in the U direction or 0 if the number
		of CVs cannot be determined."""
	@numCVsInU.setter
	def numCVsInU(self,value:Any)->None:...
	@property
	def numCVsInV(self)->Any:
		"""Number of CVs in the surface in the V direction or 0 if the number
		of CVs cannot be determined."""
	@numCVsInV.setter
	def numCVsInV(self,value:Any)->None:...
	@property
	def numKnotsInU(self)->Any:
		"""Number of knots in the surface in the U direction or 0 if the number
		of knots cannot be determined."""
	@numKnotsInU.setter
	def numKnotsInU(self,value:Any)->None:...
	@property
	def numKnotsInV(self)->Any:
		"""Number of knots in the surface in the V direction or 0 if the number
		of knots cannot be determined."""
	@numKnotsInV.setter
	def numKnotsInV(self,value:Any)->None:...
	@property
	def numNonZeroSpansInU(self)->Any:
		"""Number of spans in the U direction which are non-zero (i.e. their
		max param value is greater than their min param value)."""
	@numNonZeroSpansInU.setter
	def numNonZeroSpansInU(self,value:Any)->None:...
	@property
	def numNonZeroSpansInV(self)->Any:
		"""Number of spans in the V direction which are non-zero (i.e. their
		max param value is greater than their min param value)."""
	@numNonZeroSpansInV.setter
	def numNonZeroSpansInV(self,value:Any)->None:...
	@property
	def numPatches(self)->Any:
		"""Number of non-zero patches on the surface."""
	@numPatches.setter
	def numPatches(self,value:Any)->None:...
	@property
	def numPatchesInU(self)->Any:
		"""Number of non-zero patches in the U direction."""
	@numPatchesInU.setter
	def numPatchesInU(self,value:Any)->None:...
	@property
	def numPatchesInV(self)->Any:
		"""Number of non-zero patches in the V direction."""
	@numPatchesInV.setter
	def numPatchesInV(self,value:Any)->None:...
	@property
	def numRegions(self)->Any:
		"""Number of trimmed regions for this surface or 0 if the surface is
		not a trimmed surface."""
	@numRegions.setter
	def numRegions(self,value:Any)->None:...
	@property
	def numSpansInU(self)->Any:
		"""Number of spans in the U direction, including zero-length spans."""
	@numSpansInU.setter
	def numSpansInU(self,value:Any)->None:...
	@property
	def numSpansInV(self)->Any:
		"""Number of spans in the V direction, including zero-length spans."""
	@numSpansInV.setter
	def numSpansInV(self,value:Any)->None:...
	@property
	def numUVs(self)->Any:
		"""Number of texture (uv) coordinates for this surface. The uvs are
		stored in a list which is referenced by patches requiring textures
		on a per-patch per-patchCorner basis. This attribute contains the
		number of elements in this list."""
	@numUVs.setter
	def numUVs(self,value:Any)->None:...
	kInvalidBoundary:int=0
	kOuter:int=1
	kInner:int=2
	kSegment:int=3
	kClosedSegment:int=4
	kInvalid:int=0
	kOpen:int=1
	kClosed:int=2
	kPeriodic:int=3
	kLast:int=4
	kPointTolerance:float=0.001
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def area(self,space:int=MSpace.kObject,tolerance:float=MFnMesh.kPointTolerance)->float:
		"""area(space=kObject, tolerance=kPointTolerance) -> float

		Returns the surface's area, or 0.0 if the area cannot be determined."""
	def assignUV(self,patchId:int,cornerIndex:int,uvId:int)->Self:
		"""assignUV(patchId, cornerIndex, uvId) -> self

		Maps a texture coordinate (uv) to a the specified corner of a patch.

		Note that API methods that modify uv data will work correctly when
		called through a plug-in node that is in the history of the shape,
		or when used on a surface shape that does not have history.
		Modifying uvs directly on a shape with history will result in the
		modifications getting over-written by the next evaluation of the
		history attached to the shape.

		* patchId     (int) - Patch to map to.
		* cornerIndex (int) - Corner of the patch to map to.
		* uvId        (int) - Index into the uv list of the UV to map."""
	def assignUVs(self,uvCounts:MIntArray|Sequence[int],uvIds:MIntArray|Sequence[int])->Self:
		"""assignUVs(uvCounts, uvIds) -> self

		Maps all texture coordinates for the surface. setUV() and setUVs()
		are used to create the texture coordinate table for the surface.
		After the table is created, this method is used to map those values
		to each patch on a per-corner basis.

		The uvCounts array should contain the number of uvs per patch.
		Since uvs are mapped per-patch per-corner, the entries in this array
		should match the corner counts for each patch in the surface.
		If an entry in this array is '0' then the corresponding patch will
		not be mapped.

		The sum of all the entries in the uvCounts array must be equal to
		the size of the uvIds array or this method will fail.

		The uvIds array should contain the UV indices that will be mapped to
		each patch-corner in the surface. The entries in this array specify
		which uvs in the surface's uv table are mapped to each patch-corner.
		Each entry in the uvIds array must be less than numUVs().
		The size of the uvIds array is equivalent to adding up all of the
		entries in the uvCounts array, so for a cube with all patches mapped
		there would be 24 entries.

		Note that API methods that modify uv data will work correctly when
		called through a plug-in node that is in the history of the shape,
		or when used on a surface shape that does not have history.
		Modifying uvs directly on a shape with history will result in the
		modifications getting over-written by the next evaluation of the
		history attached to the shape.

		* uvCounts (MIntArray or seq of int)
		             - UV counts for each patch in the surface.
		* uvIds    (MIntArray or seq of int)
		             - UV indices to be mapped to each patch-corner."""
	def boundaryType(self,region:int,boundary:int)->int:
		"""boundaryType(region, boundary) -> int

		Returns the type of the specified boundary. The surface must be a
		trimmed surface. Valid boundary types are:

		    kInner           - an inner (clockwise) boundary
		    kOuter           - an outser (counter clockwise) boundary
		    kSegment         - a curve on a patch
		    kClosedSegment   - a closed curve on a patch
		    kInvalidBoundary - an invalid boundary type

		* region (int)   - Region containing the boundary
		* boundary (int) - Index of the boundary within the region."""
	def clearUVs(self)->Self:
		"""clearUVs() -> self

		Clears out all texture coordinates for the nurbsSurface, and leaves
		behind an empty UVset.

		This method should be used if it is needed to shrink the size of the
		UV table. In this case, the user should call clearUVs, setUVs and
		then assignUVs to rebuild the mapping info.

		When called on a dataNurbsSurface the UVs are removed. When called
		on a shape with no history, the UVs are removed and the attributes
		are set on the shape. When called on a shape with history, the
		polyDelMap command is invoked and a polyMapDel node is created."""
	def closestPoint(self,testPoint:MPoint,uStart:float|None=None,vStart:float|None=None,ignoreTrimBoundaries:bool=False,tolerance:float=MFnMesh.kPointTolerance,space:int=MSpace.kObject)->tuple[MPoint,float,float]:
		"""closestPoint(testPoint, uStart=None, vStart=None,
		    ignoreTrimBoundaries=False, tolerance=kPointTolerance,
		    space=kObject) -> (MPoint, float, float)

		Returns the closest point on the surface to the specified test point
		The return value is a tuple containing the position of the point and
		and its U and V texture parameters.

		Performance can be greatly increased by supplying starting U and V
		parameter values which are reasonably close to the final point.
		Specifying these values will invoke a special algorithm which will
		begin to search for the closest point at the given parameter value,
		and will check the local surface to see which direction will bring
		it closer to the given point. It then offsets in this direction and
		repeats the process, iteratively traversing the surface until it
		finds the closest point.
		This algorithm will fail if it encounters a seam before reaching
		the closest point, or if it finds a local closest point, such as a
		bulge on a mesh where an offset in any direction will take it
		further from the given point, even if that is not the true closest
		point on the mesh. For this reason it is advisable to avoid using
		this option unless absolutely sure that the initial point will be
		a good enough approximation to the final point that these
		conditions will not occur.

		* testPoint (MPoint) - Position of the point to be checked
		* uStart     (float) - Initial guess of a U parameter near where the
		                       where the closest point is expected to be.
		* vStart     (float) - Initial guess of a V parameter near where the
		                       where the closest point is expected to be.
		* ignoreTrimBoundaries (bool)
		                     - For trimmed surfaces, if this is true the
		                       trim curves will be ignored and the entire
		                       untrimmed surface searched.
		* tolerance  (float) - How close to the surface must a point be to
		                       be considered 'on' the surface.
		* space        (int) - an MSpace constant giving the coordinate
		                       space which 'testPoint' is in. The returned
		                       point will be in the same space."""
	def copy(self,source:MObject,parent:MObject=MObject.kNullObj)->MObject:
		"""copy(source, parent=kNullObj) -> MObject

		Returns a new NURBS surface, which is a copy of the source surface,
		and sets the functionset to operate on it.

		* source (MObject)- The surface to copy.
		* parent (MObject)- The parent/owner of the new surface. If it's a
		                    NURBS surface data wrapper (MFn.kNurbsSurfaceData)
		                    then the created surface will be returned as a
		                    geometry object (MFn.kNurbsSurfaceGeom) owned by
		                    the wrapper. If 'parent' is a DAG node then the
		                    new surface will be returned as nurbsSurface node
		                    parented under it. If 'parent' is not provided
		                    then a new top-level transform will be created
		                    with the new surface parented beneath it as a
		                    nurbsSurface node. In this last case it will be
		                    the transform node which is returned."""
	def create(self,cvs:MPointArray|Sequence[MPoint],uKnots:MDoubleArray|Sequence[float],vKnots:MDoubleArray|Sequence[float],uDegree:int,vDegree:int,uForm:int,vForm:int,rational:bool,parent:MObject=MObject.kNullObj)->MObject:
		"""create(cvs, uKnots, vKnots, uDegree, vDegree, uForm, vForm,
		    rational, parent=kNullObj) -> MObject

		Returns a new NURBS surface created from the specified data and sets
		the function set to operate on it.

		* cvs (MPointArray or seq of MPoint)
		                  - The control vertices.
		* uKnots (MDoubleArray or seq of float)
		                  - Parameter values for the knots in the U direction.
		* vKnots (MDoubleArray or seq of float)
		                  - Parameter values for the knots in the V direction.
		* uDegree   (int) - Degree of the basis functions in the U direction.
		* vDegree   (int) - Degree of the basis functions in the V direction.
		* uForm     (int) - A Form constant (kOpen, kClosed, kPeriodic) giving
		                    the surface's form in the U direction.
		* vForm     (int) - A Form constant (kOpen, kClosed, kPeriodic) giving
		                    the surface's form in the V direction.
		* rational (bool) - Create as rational (True) or non-rational (False)
		                    surface.
		* parent (MObject)- The parent/owner of the new surface. If it's a
		                    NURBS surface data wrapper (MFn.kNurbsSurfaceData)
		                    then the created surface will be returned as a
		                    geometry object (MFn.kNurbsSurfaceGeom) owned by
		                    the wrapper. If 'parent' is a DAG node then the
		                    new surface will be returned as nurbsSurface node
		                    parented under it. If 'parent' is not provided
		                    then a new top-level transform will be created
		                    with the new surface parented beneath it as a
		                    nurbsSurface node. In this last case it will be
		                    the transform node which is returned."""
	def cv(self,uIndex:int,vIndex:int)->MObject:
		"""cv(uIndex, vIndex) -> MObject

		Returns a component for the specified control vertex.

		* uIndex (int) - U index of the CV.
		* vIndex (int) - V index of the CV."""
	def cvPosition(self,uIndex:int,vIndex:int,space:int=MSpace.kObject)->MPoint:
		"""cvPosition(uIndex, vIndex, space=kObject) -> MPoint

		Returns the position of the specified control vertex.

		* uIndex (int) - U index of the CV.
		* vIndex (int) - V index of the CV.
		* space  (int) - an MSpace constant giving the coordinate
		                 space which the point should be returned."""
	def cvPositions(self,space:int=MSpace.kObject)->MPointArray:
		"""cvPositions(space=kObject) -> MPointArray

		Returns the positions of all the surface's control vertices.

		* space  (int) - an MSpace constant giving the coordinate
		                 space which the points should be returned."""
	def cvsInU(self,startUIndex:int,endUIndex:int,vIndex:int)->MObject:
		"""cvsInU(startUIndex, endUIndex, vIndex) -> MObject

		Returns a component for a set of control vertices in the U direction.

		* startUIndex (int) - U index of the first CV to return.
		* endUIndex   (int) - U index of the last CV to return.
		* vIndex      (int) - V index for all of the returned CVs."""
	def cvsInV(self,startVIndex:int,endVIndex:int,uIndex:int)->MObject:
		"""cvsInV(startVIndex, endVIndex, uIndex) -> MObject

		Returns a component for a set of control vertices in the V direction.

		* startVIndex (int) - V index of the first CV to return.
		* endVIndex   (int) - V index of the last CV to return.
		* uIndex      (int) - U index for all of the returned CVs."""
	def distanceToPoint(self,point:MPoint,space:int=MSpace.kObject)->float:
		"""distanceToPoint(point, space=kObject) -> float

		Returns the distance from the given point to the closest point on
		the surface.

		* point (MPoint) - Point to calculate distance to.
		* space  (int)   - An MSpace constant giving the coordinate space in
		                   which the point has been specified."""
	def edge(self,region:int,boundary:int,edge:int,paramEdge:bool=False)->MObjectArray:
		"""edge(region, boundary, edge, paramEdge=False) -> MObjectArray

		Return the specified edge of a trim boundary.

		For each region of a trimmed surface there may be several boundary
		curves: an outer curve and possibly several inner boundary curves
		(which define holes). These boundary curves are made up of one or
		more curves called edges.

		The edge is returned as an MObjectArray as it may consist of more
		than one curve. The returned edge, or trim curve, can be a 2D parameter
		edge or a 3D edge curve. Note that for closed surfaces some of the
		3d edges may be 0 length in which case an empty MObjectArray is
		returned. An example of this is the poles of a sphere.

		* region     (int) - Index of trimmed region containing the edge.
		* boundary   (int) - Index of boundary within trimmed region.
		* edge       (int) - Index of the edge within the boundary.
		* paramEdge (bool) - If True a 2D parameter edge is returned,
		                     otherwise a 3D edge is returned."""
	def getAssignedUVs(self)->tuple[MIntArray,MIntArray]:
		"""getAssignedUVs() -> (MIntArray, MIntArray)

		Returns the indices of all UVs which have been mapped to the surface.
		The return value is a tuple with an array containing the number
		of UVs for each patch in the surface, and a second array containing
		the indices of the UVs mapped to each corner of those patches. This
		is the same format as the arrays taken by the assignUVs() method."""
	def getConnectedShaders(self,instanceNumber:int)->tuple[MObjectArray,MIntArray]:
		"""getConnectedShaders(instanceNumber) -> (MObjectArray, MIntArray)

		Returns a tuple containing an array of all the shaders (sets)
		connected to the specified instance of this surface, and an array of
		patch/shader assignments. The second array will hold, for each patch
		in the surface, an index into the first array. If a patch does not
		have a shader assigned to it, the value of the index will be -1.
		The shader objects can be derived from the sets returned.

		Note: This method will only work with a MFnNurbsSurface function set
		      which has been initialized with an MFn::kNurbsSurface.

		See also getConnectedSetsAndMembers.

		* instanceNumber (int) - Determines which instance of the surface to
		                         query. This will be zero if there is only
		                         one instance."""
	def getDerivativesAtParam(self,uParam:float,vParam:float,space:int=MSpace.kObject,secondOrder:bool=False)->tuple[MPoint,MVector,Any]:
		"""getDerivativesAtParam(uParam, vParam, space=kObject, secondOrder=False)
		    -> (MPoint, MVector, MVector)
		    -> (MPoint, MVector, MVector, MVector, MVector, MVector)

		Evaluates the surface at the given (u,v) coordinates, returning a
		tuple containing the position at that point, the first derivative
		vector in U, and the first derivative vector in V. If 'secondOrder'
		is True then the tuple will also contain three additional vectors:
		the second order partial derivative with respect to U (dUU), the
		second order partial derivative with respect to V (dVV), and the
		second order partial derivative with respect to U then V (dUV).
		None of the vectors will be normalized.

		* uParam (float) - U parameter value at which to do the evaluation.
		* vParam (float) - V parameter value at which to do the evaluation.
		* space    (int) - An MSpace constant giving the coordinate space in
		                   which to perform the calculation.
		* secondOrder (bool)
		                 - If True, second order derivatives will be included
		                   in the result. Note that this will increase
		                   computation time."""
	def getParamAtPoint(self,point:MPoint,ignoreTrimBoundaries:bool,tolerance:float=MFnMesh.kPointTolerance,space:int=MSpace.kObject)->tuple[float,float]:
		"""getParamAtPoint(point, ignoreTrimBoundaries, tolerance=kPointTolerance,
		    space=kObject) -> (float, float)

		Returns a tuple containing the parameter values corresponding to the
		given point on the surface (or underlying surface).

		* point    (MPoint) - Location of the parameter to obtain.
		* ignoreTrimBoundaries (bool)
		                    - For trimmed surfaces, if this is true the
		                      trim curves will be ignored and the entire
		                      untrimmed surface searched.
		* tolerance (float) - Accuracy to be used in the operation.
		* space       (int) - An MSpace constant giving the coordinate space
		                      in which to perform the operation."""
	def getPatchUV(self,patchId:int,cornerIndex:int)->tuple[float,float]:
		"""getPatchUV(patchId, cornerIndex) -> (float, float)

		Returns a tuple containing the texture texture coordinate for a
		corner of a patch. Since texture coordinates (UVs) are stored
		per-patch per-corner you must specify both the patch and the corner
		that the u and v values are mapped to.
		* patchId (int)     - Patch of interest.
		* cornerIndex (int) - Corner of interest."""
	def getPatchUVid(self,patchId:int,cornerIndex:int)->int:
		"""getPatchUVid(patchId, cornerIndex) -> int

		Returns the id of the texture coordinate for a single corner of a patch.

		* patchId (int)     - Patch of interest.
		* cornerIndex (int) - Corner of interest."""
	def getPatchUVs(self,patchId:int)->tuple[MFloatArray,MFloatArray]:
		"""getPatchUVs(patchId) -> (MFloatArray, MFloatArray)

		Returns a tuple containing the values of the texture coordinates on
		all corners of the specified patch. The tuple contains an array of U
		coordinates and an array of V coordinates, both the same length.

		* patchId (int)     - Patch of interest."""
	def getPointAtParam(self,uParam:Any,vParam:Any,space:int=MSpace.kObject)->MPoint:
		"""getPointAtParam(uParam, vParam, space=kObject) -> MPoint"""
	def getUV(self,uvId:int)->tuple[float,float]:
		"""getUV(uvId) -> (float, float)

		Returns a tuple containing the U and V values for the a texture coordinate

		* uvId (int) - Id of the texture coordinate of intest."""
	def getUVs(self)->tuple[MFloatArray,MFloatArray]:
		"""getUVs() -> (MFloatArray, MFloatArray)

		Returns all of the surface's texture coordinates as a tuple containing
		an array of U values and an array of V values."""
	def intersect(self,rayStart:MPoint,rayDir:MVector,tolerance:float=MFnMesh.kPointTolerance,space:int=MSpace.kObject,distance:bool=False,exactHit:bool=False,all:bool=False)->Any:
		"""intersect(rayStart, rayDir, tolerance=kPointTolerance, space=kObject,
		    distance=False, exactHit=False, all=False)
		    -> (MPoint, float, float[, float][, bool])
		    -> (MPointArray, MDoubleArray, MDoubleArray[, MDoubleArray][, bool])
		    -> None

		Returns the closest point of intersection of a ray with the surface
		as a tuple containing the point of intersection and the U and V
		parameters at that point.
		* rayStart (MPoint) - Starting point for the ray.
		* rayDir  (MVector) - Direction of the ray
		* tolerance (float) - Accuracy to be used in the operation.
		* space       (int) - An MSpace constant giving the coordinate space
		                      in which to perform the operation.* distance   (bool) - If True the distance from 'rayStart' to the
		                      point of intersection will be appended to the
		                      returned tuple.
		* exactHit   (bool) - If True then a boolean value indicating if the
		                      point of intersection was an exact hit will be
		                      appended to the returned tuple.
		* all        (bool) - If True then all points of intersection will
		                      be returned. In this case the point of
		                      intersection, U and V parameters, and distance
		                      (if requested) will all be returned as arrays."""
	def isFlipNorm(self,region:Any)->bool:
		"""isFlipNorm(region) -> bool

		Checks whether the normal for the specified region is flipped
		This method is only valid for trimmed surfaces.

		region (int) - Region to check."""
	def isKnotU(self,param:float)->bool:
		"""isKnotU(param) -> bool

		Checks if the specified parameter value is a knot value in the U
		direction.

		* param (float) - Parameter value to check."""
	def isKnotV(self,param:float)->bool:
		"""isKnotV(param) -> bool

		Checks if the specified parameter value is a knot value in the V
		direction.

		* param (float) - Parameter value to check."""
	def isParamOnSurface(self,uParam:float,vParam:float)->bool:
		"""isParamOnSurface(uParam, vParam) -> bool

		Checks if the specified parameter point is on this surface.

		* uParam (float) - U parameter value.
		* vParam (float) - V parameter value."""
	def isPointInTrimmedRegion(self,uParam:float,vParam:float)->bool:
		"""isPointInTrimmedRegion(uParam, vParam) -> bool

		Checks if the given point is in a trimmed away region of a trimmed
		surface. A trimmed away region is the part of the surface that is
		cut away as a result of a trim operation.

		* uParam (float) - U parameter of the point to check.
		* vParam (float) - V parameter of the point to check."""
	def isPointOnSurface(self,point:MPoint,tolerance:float=MFnMesh.kPointTolerance,space:int=MSpace.kObject)->bool:
		"""isPointOnSurface(point, tolerance=kPointTolerance, space=kObject) -> bool

		Checks if the given point is on this surface.

		* point    (MPoint) - Point to check.
		* tolerance (float) - Accuracy to be used in the operation.
		* space       (int) - An MSpace constant giving the coordinate space
		                      in which to perform the operation"""
	def knotInU(self,index:int)->float:
		"""knotInU(index) -> float

		Returns the knot value at the specified U index. U knots are indexed
		from 0 to numKnotsInU-1.
		* index (int) - Index of the U knot to return."""
	def knotInV(self,index:int)->float:
		"""knotInV(index) -> float

		Returns the knot value at the specified V index. V knots are indexed
		from 0 to numKnotsInV-1.
		* index (int) - Index of the V knot to return."""
	def knotsInU(self)->MDoubleArray:
		"""knotsInU() -> MDoubleArray

		Returns all of the surface's knots in the U direction."""
	def knotsInV(self)->MDoubleArray:
		"""knotsInV() -> MDoubleArray

		Returns all of the surface's knots in the V direction."""
	def normal(self,uParam:float,vParam:float,space:int=MSpace.kObject)->MVector:
		"""normal(uParam, vParam, space=kObject) -> MVector

		Returns the normal at the given parameter value on the surface.

		* uParam (float) - U parameter at which to obtain normal.
		* vParam (float) - V parameter at which to obtain normal.
		* space    (int) - An MSpace constant giving the coordinate space
		                   in which to perform the operation"""
	def numBoundaries(self,region:int)->int:
		"""numBoundaries(region) -> unsigned int

		Returns the number of boundaries for the specified region. The
		surface must be a trimmed surface.

		For each region there may be several boundary curves, an outer curve
		and possibly several inner boundary curves which define holes. These
		boundary curves are made up of one or more curves called edges.

		* region (int) - Region of interest."""
	def numEdges(self,region:int,boundary:int)->int:
		"""numEdges(region, boundary) -> unsigned int

		Returns the number of edges for the specified trim boundary.
		For each region there may be several boundary curves, an outer curve
		and possibly several inner boundary curves which define holes. These
		boundary curves are made up of one or more curves called edges.

		* region   (int) - Region of interest.
		* boundary (int) - Boundary of interest"""
	def projectCurve(self,curve:Any,direction:MVector=...,keepHistory:bool=False)->Self:
		"""projectCurve(curve[, direction], keepHistory=False) -> self

		Projects the given curve onto the surface, creating a curve on surface.

		* direction (MVector) - Direction of projection. If not supplied
		                        then surface normals will be used.
		* keepHistory  (bool) - Determines whether the construction history
		                        of the projection should be retained."""
	def removeKnotInU(self,param:float,removeAll:bool=False)->Self:
		"""removeKnotInU(param, removeAll=False) -> self

		Removes one or more U knots at the specified parameter value from
		from the surface.

		* param    (float) - U parameter value of the knot to remove.
		* removeAll (bool) - If True and there are multiple knots at the
		                     parameter value then they will all be removed.
		                     Otherwise, all but one will be removed."""
	def removeKnotInV(self,param:float,removeAll:bool=False)->Self:
		"""removeKnotInV(param, removeAll=False) -> self

		Removes one or more V knots at the specified parameter value from
		from the surface.

		* param    (float) - V parameter value of the knot to remove.
		* removeAll (bool) - If True and there are multiple knots at the
		                     parameter value then they will all be removed.
		                     Otherwise, all but one will be removed."""
	def removeOneKnotInU(self,param:float)->Self:
		"""removeOneKnotInU(param) -> self

		Removes one U knot at the specified parameter value. If there are
		multiple knots at that the value the others are retained.

		* param (float) - U parameter value of the knot to remove."""
	def removeOneKnotInV(self,param:float)->Self:
		"""removeOneKnotInV(param) -> self

		Removes one V knot at the specified parameter value. If there are
		multiple knots at that the value the others are retained.

		* param (float) - V parameter value of the knot to remove."""
	def setCVPosition(self,uIndex:int,vIndex:int,point:Any,space:int=MSpace.kObject)->Self:
		"""setCVPosition(uIndex, vIndex, point, space=kObject) -> self"""
	def setCVPositions(self,points:MPointArray|Sequence[MPoint],space:int=MSpace.kObject)->Self:
		"""setCVPositions(points, space=kObject) -> self

		Set the positions of all of the surface's CVs.
		(numCVsInU * numCVsInV) points must be provided. Converting from
		U and V indices to array indices is done by:

		        array index = numCVsInV * U index + V index

		To keep this method as fast as possible, no checking of the data is
		performed beyond ensuring that the total number of CVs passed in is
		correct. It is up to the caller to ensure that the CVs provide a
		valid surface, for example by ensuring that overlapping CVs in
		periodic surfaces have the same positions.

		* points (MPointArray or seq of MPoint)
		               - Positions of the CVs.
		* space  (int) - An MSpace constant giving the coordinate space
		                 in which to perform the operation"""
	def setKnotInU(self,index:int,param:float)->Self:
		"""setKnotInU(index, param) -> self

		Sets the value of an existing U knot. U knots are indexed from 0 to
		numKnotsInU-1. Note that this method does not insert a new knot, it
		simply changes the value of an existing knot.

		If a knot value is set that breaks the non-decreasing requirement
		for the knot array, the knot value will be changed and an exception
		raised.

		* index   (int) - U index of the knot to set.
		* param (float) - New parameter value for the knot."""
	def setKnotInV(self,index:int,param:float)->Self:
		"""setKnotInV(index, param) -> self

		Sets the value of an existing V knot. V knots are indexed from 0 to
		numKnotsInV-1. Note that this method does not insert a new knot, it
		simply changes the value of an existing knot.

		If a knot value is set that breaks the non-decreasing requirement
		for the knot array, the knot value will be changed and an exception
		raised.

		* index   (int) - V index of the knot to set.
		* param (float) - New parameter value for the knot."""
	def setKnotsInU(self,params:MDoubleArray|Sequence[float],startIndex:int,endIndex:int)->Self:
		"""setKnotsInU(params, startIndex, endIndex) -> self

		Sets the values of a range of U knots.

		* params     (MDoubleArray or seq of float)
		                   - Parameter values to set at the knots. One value
		                     per knot in the range.
		* startIndex (int) - Index of the first U knot to set.
		* endIndex   (int) - Index of the last U knot to set."""
	def setKnotsInV(self,params:MDoubleArray|Sequence[float],startIndex:int,endIndex:int)->Self:
		"""setKnotsInV(params, startIndex, endIndex) -> self

		Sets the values of a range of V knots.

		* params     (MDoubleArray or seq of float)
		                   - Parameter values to set at the knots. One value
		                     per knot in the range.
		* startIndex (int) - Index of the first V knot to set.
		* endIndex   (int) - Index of the last V knot to set."""
	def setUV(self,uvId:int,u:float,v:float)->Self:
		"""setUV(uvId, u, v) -> self

		Sets a single texture coordinate. If 'uvId' is greater than or equal
		to numUVs then the surface's uv list will be grown to accommodate it.

		Note that API methods that modify uv data work correctly either when
		called through a plug-in node that is in the history of the shape,
		or when used on a surface shape that does not have history.
		Modifying uvs directly on a shape with history will result in the
		modifications getting over-written by the next evaluation of the
		history attached to the shape.

		* uvId (int) - Index of the element in the surface's uv list to set.
		* u  (float) - U value to set the uv to.
		* v  (float) - V value to set the uv to."""
	def setUVs(self,uList:MFloatArray|Sequence[float],vList:MFloatArray|Sequence[float])->Self:
		"""setUVs(uList, vList) -> self

		Sets all of the texture coordinates (uvs) for this surface. The
		arrays must be of equal length and must be at least of length numUVs.
		If the arrays are larger than numUVs then the uv list for this surface
		will be grown to accommodate the new uv values.

		After using this method to set the UV values, you can call
		assignUVs to assign the corresponding UVids to the geometry.

		Note that API methods that modify uv data work correctly either when
		called through a plug-in node that is in the history of the shape,
		or when used on a surface shape that does not have history.
		Modifying uvs directly on a shape with history will result in the
		modifications getting over-written by the next evaluation of the
		history attached to the shape.

		* uList (MFloatArray or seq of float) - U values to set
		* vList (MFloatArray or seq of float) - V values to set"""
	def tangents(self,uParam:float,vParam:float,space:int=MSpace.kObject)->tuple[MVector,MVector]:
		"""tangents(uParam, vParam, space=kObject) -> (MVector, MVector)

		Returns the tangents in the U and V directions at a given parameter
		value on the surface. The returned tangent vectors are normalized.

		This method does not fail if the given parameter lies within a
		trimmed away region of a trimmed surface. Use isPointInTrimmedRegion()
		to determine if the uv point lies within such a region.

		* uParam (float) - U parameter value at which to obtain the tangents.
		* vParam (float) - V parameter value at which to obtain the tangents.
		* space    (int) - An MSpace constant giving the coordinate space
		                   in which to perform the operation"""
	def trim(self,regionsToKeepU:MDoubleArray|Sequence[float],regionsToKeepV:MDoubleArray|Sequence[float],keepHistory:bool=False)->Self:
		"""trim(regionsToKeepU, regionsToKeepV, keepHistory=False) -> self

		Trims the surface to its curves on surface. Regions which are kept
		are specified by passing in arrays of u,v parameters.

		This method will create a new trimmed surface in the DAG. The surface
		attached to this function set will remain unchanged.

		* regionsToKeepU (MDoubleArray or seq of float)
		                        - U parameters of points within the regions
		                          to be kept.
		* regionsToKeepV (MDoubleArray or seq of float)
		                        - V parameters of points within the regions
		                          to be kept.
		* keepHistory    (bool) - Determines whether the construction history
		                          of the operation should be retained."""
	def updateSurface(self)->Self:
		"""updateSurface() -> self

		Signals that this surface has changed and needs to be recalculated.

		This method is useful when a large number of CVs for the surface are
		being modified. Instead of updating the surface every time a CV is
		changed it is more efficient to call this method once after all the
		updates are complete."""
class MFnNurbsSurfaceData(MFnGeometryData):
	"""MFnNurbsSurfaceData allows the creation and manipulation of Nurbs Surface
	data objects for use in the dependency graph.

	__init__()
	Initializes a new, empty MFnNurbsSurfaceData object

	__init__(MObject)
	Initializes a new MFnNurbsSurfaceData function set, attached
	to the specified object."""
	@overload
	def __init__(self)->None:
		"""Default constructor. Returns a new, empty MFnNurbsSurfaceData object."""
	@overload
	def __init__(self,obj:MObject)->None:
		"""Returns a new MFnNurbsSurfaceData function set, attached to the specified object."""
	def create(self)->MObject:
		"""Creates a new nurbs surface data object, attaches it to this function set and returns an MObject which references it."""
class MFnPlugin(MFnBase):
	"""Register and deregister plug-in services with Maya."""
	@property
	def version(self)->str:
		"""Plug-in version string."""
	@version.setter
	def version(self,value:str)->None:...
	@overload
	def __init__(self)->None:
		"""Default constructor. Returns a new MFnPlugin function set with no Maya object attached."""
	@overload
	def __init__(self,plugin:MObject,vendor:str,version:str,apiVersion:str)->None:
		"""Attaches the function set to the specified plugin object, which is provided as a parameter to the plugin's initializePlugin() and uninitializePlugin() functions, and specifies an optional vendor name, plugin version string and minimal required Maya apiVersion (which is currently ignored)."""
	def apiVersion(self)->str:
		"""Return the API version required by the plug-in."""
	def deregisterAttributePatternFactory(self,*args)->Any:
		"""Deregister a user defined attribute pattern factory type from Maya."""
	def deregisterCommand(self,cmdName:str)->Self:
		"""Deregister a user defined command from Maya."""
	def deregisterData(self,*args)->Any:
		"""Deregister a user defined data type from Maya."""
	def deregisterDragAndDropBehavior(self,*args)->Any:
		"""Deregister a user defined drag and drop behavior from Maya."""
	def deregisterNode(self,*args)->Any:
		"""Deregister a user defined dependency node from Maya."""
	def deregisterContextCommand(self,*args)->Any:
		"""Deregister a user defined context command from Maya."""
	@staticmethod
	def findPlugin(*args)->Any:
		"""Returns an MObject corresponding to the named plugin."""
	def loadPath(self)->str:
		"""Return the full path name of the file from which the plug-in was loaded."""
	def name(self)->str:
		"""Return the plug-in's name."""
	def registerAttributePatternFactory(self,*args)->Any:
		"""Register a new attribute pattern factory type with Maya."""
	def registerCommand(self,cmdName:str,createCmdFunc:Callable,createSyntaxFunc:Callable|None=None)->Any:
		"""Register a new command with Maya. createCmdFunc is a Python callable which takes no arguments and returns a new instance of the MPxCommand-derived class. createSyntaxFunc is a Python callable which takes no arguments and returns an MSyntax object initialized with the command's syntax."""
	def registerContextCommand(self,*args)->Any:
		"""Register a new context command with Maya.  Once registered, the context
		can be used to create a new tool that can be used in a manner
		identical to built-in Maya tools."""
	def registerData(self,*args)->Any:
		"""Register a new data type with Maya."""
	def registerDragAndDropBehavior(self,*args)->Any:
		"""Register a new drag and drop behavior with Maya.
		Once registered, the new behavior can be used to finish connections between node drag and drops from the hyperGraph/hyperShade to other nodes or Maya UI."""
	def registerNode(self,*args)->Any:
		"""Register a new dependency node with Maya."""
	def registerShape(self,*args)->Any:
		"""Register a new user defined shape node with Maya.
		To deregister the shape node use the MFnPlugin.deregisterNode()."""
	def setName(self,name:str,makeUnique:bool=True)->Self:
		"""Set the plug-in's name. If another plug-in is already using name and makeUnique is True then Maya will choose a unique name for the plug-in, otherwise a RuntimeError will be raised."""
	def vendor(self)->str:
		"""Return the plug-in's vendor string."""
class MFnPluginData(MFnData):
	"""MFnPluginData allows the creation and manipulation of plugin
	data objects for use in the dependency graph.

	__init__()
	Initializes a new, empty MFnPluginData object

	__init__(MObject)
	Initializes a new MFnPluginData function set, attached
	to the specified object."""
	@overload
	def __init__(self)->None:
		"""Initializes a new, empty MFnPluginData object"""
	@overload
	def __init__(self,MObject:Any)->None:
		"""Initializes a new MFnPluginData function set, attached
		to the specified object."""
	def typeId(self)->MTypeId:
		"""typeId() -> MTypeId

		Return the unique MTypeId of the user defined data that is held by this instance"""
	def data(self)->MPxData:
		"""data() -> MPxData

		Return the user defined data held in this instance"""
	def create(self,id:MTypeId)->MObject:
		"""create(id) -> MObject

		Create an instance of the specified user defined data type and attach it to this functionset.

		* id (MTypeId) - the unique MTypeId of the user defined data class derived from MPxData."""
class MFnPointArrayData(MFnData,collections.abc.Sequence[MPoint]):
	"""Function set for node data consisting of an array of MPoints."""
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def __len__(self)->int:
		"""Return len(self)."""
	def __getitem__(self,index:int)->MPoint:
		"""Return self[key]."""
	def __setitem__(self,index:int,value:MPoint)->None:
		"""Set self[key] to value."""
	def __delitem__(self,index:int)->None:
		"""Delete self[key]."""
	def array(self)->MPointArray:
		"""Returns the encapsulated array as an MPointArray . For performance reasons the returned array is a live reference to the encapsulated array so changes made to one directly affect the other. The returned array is only valid for as long as the function set retains the same data object. If the function set is destroyed or attached to a different object then the returned array should be discarded. Failure to do so could result in Maya becoming unstable."""
	def copyTo(self,array:MPointArray)->Self:
		"""Replaces the elements of array with those in the encapsulated array."""
	@overload
	def create(self)->MObject:
		"""Creates a new empty MPoint array data object, attaches it to the function set and returns an MObject which references it."""
	@overload
	def create(self,array:MPointArray|Sequence[MPoint])->MObject:
		"""Creates a new MPoint array data object, initializes it with the elements from array , attaches it to the function set and returns an MObject which references it."""
	@overload
	def set(self,array:MPointArray|Sequence[MPoint])->Self:
		"""Replaces the elements in the encapsulated array with those from the supplied array ."""
	@overload
	def set(self,value:MPoint,index:int)->Self:
		"""Sets the value of the index 'th array element."""
class MFnReference(MFnDependencyNode):
	"""Function set for reference nodes."""
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def isValidReference(self)->bool:
		"""isValidReference() -> bool

		Returns true if the reference is an valid file reference."""
	def fileName(self,resolvedName:bool,includePath:bool,includeCopyNumber:bool)->str:
		"""fileName(bool resolvedName, bool includePath, bool includeCopyNumber) -> MString

		Returns the name of file associated with this reference."""
	def associatedNamespace(self,shortName:bool)->str:
		"""associatedNamespace(bool shortName) -> MString

		Returns the namespace associated with this reference."""
	def parentFileName(self,resolvedName:bool,includePath:bool,includeCopyNumber:bool)->str:
		"""parentFileName(bool resolvedName, bool includePath, bool includeCopyNumber) -> MString

		Returns the name of parent file associated with this reference."""
	def parentReference(self)->MObject:
		"""parentReference() -> MObject

		Returns the reference node associated with the parent reference."""
	def parentAssembly(self)->MObject:
		"""parentAssembly() -> MObject

		Returns the parent assembly node that contains this reference. See MFnAssembly documentation for more details."""
	def containsNode(self,MObject:Any)->bool:
		"""containsNode(MObject) -> bool

		Returns true if the specified node is from this reference or one of its child references. The containsNodeExactly method can be used to test membership without including the child references."""
	def containsNodeExactly(self,MObject:Any)->bool:
		"""containsNodeExactly(MObject) -> bool

		Returns true if the specified node is from this reference. Membership in child references is not checked. The containsNode method may be used to test membership in a reference and its child references."""
	def nodes(self)->MObjectArray:
		"""nodes() -> MObjectArray

		Returns an array of the nodes associated with this reference."""
	def isLoaded(self)->bool:
		"""isLoaded() -> bool

		Returns true if the reference is loaded."""
	def isLocked(self)->bool:
		"""isLocked() -> bool

		Returns true if the reference is locked or if the referenced file was saved as locked."""
	def isExportEditsFile(self)->bool:
		"""isExportEditsFile() -> bool

		Returns true if the reference is an export edits file. An export edits file is a file of type '.editMA' or '.editMB' which was created using Maya's offline file functionality."""
	@staticmethod
	def ignoreReferenceEdits()->bool:
		"""ignoreReferenceEdits() -> bool

		Indicates whether reference edits will be tracked and logged or not."""
	@staticmethod
	def setIgnoreReferenceEdits(bool:bool)->None:
		"""setIgnoreReferenceEdits(bool) -> None

		Specify whether reference edits should be tracked and logged or not.
		This should be treated as a temporary state and should be enabled
		around a batch of operations where reference edits should be ignored.
		Restore the previous value when the batch of operations is complete."""
class MFnSet(MFnDependencyNode):
	"""Function set for sets."""
	kNone:int=0
	kVerticesOnly:int=1
	kEdgesOnly:int=2
	kFacetsOnly:int=3
	kEditPointsOnly:int=4
	kRenderableOnly:int=5
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def create(self,members:MSelectionList,restriction:int=MFileObject.kNone)->MObject:
		"""create(members, restriction=kNone) -> MObject

		Creates a new set dependency node and puts it in the dependency graph.

		* members (MSelectionList) - list of members for new set
		* restriction (MFnSet.Restriction) - restriction applied to members"""
	def getUnion(self,otherSet:MObject|MObjectArray|list[set])->MSelectionList:
		"""getUnion( otherSet ) -> MSelectionList

		This method calculates the union of two sets.  The result will be the union of this set and the set passed into the method.

		* otherSet (MObject or MObjectArray or list of sets) - set(s) to find union of with this set"""
	def getIntersection(self,otherSet:MObject|MObjectArray|list[set])->MSelectionList:
		"""getIntersection( otherSet ) -> MSelectionList

		This method calculates the intersection of two sets.  The result will be the intersection of this set and the set passed into the method.

		* otherSet (MObject or MObjectArray or list of sets) - set(s) to find union of with this set"""
	def clear(self)->Self:
		"""clear() -> self

		Removes all elements from this set."""
	def getMembers(self,flatten:bool)->MSelectionList:
		"""getMembers( flatten ) -> MSelectionList

		Get the members of this set as a selection list.  This information is providedas a selection list so that all of the path information is retained forDAG nodes.

		It is possible to ask for the returned list to be flattened.  This means thatall sets that exist inside this set will be expanded into a list of theircontents.

		* flatten (bool) - whether to flatten the returned list"""
	def addMember(self,object:Any)->Self:
		"""addMember( object ) -> self

		Add a new object to the set.

		The added object may be an MObject, an (MDagPath, MObject) tuple, or an MPlug."""
	def addMembers(self,MSelectionList:Any)->Self:
		"""addMembers( MSelectionList ) -> self

		Add a list of new objects to the set."""
	def removeMember(self,object:Any)->Self:
		"""removeMember( object ) -> self

		Remove an object from the set.

		The removed object may be an MObject, an (MDagPath, MObject) tuple, or an MPlug."""
	def removeMembers(self,MSelectionList:Any)->Self:
		"""removeMembers( MSelectionList ) -> self

		Remove items of the selection list from the set."""
	def isMember(self,object:Any)->bool:
		"""isMember( object ) -> bool

		Returns true if the given object is a member of this set.

		The object may be an MObject, an (MDagPath, MObject) tuple, or an MPlug."""
	def intersectsWith(self,otherSet:Any)->Self:
		"""intersectsWith( otherSet ) -> self

		Returns true if this set intersects with the given set.  An intersection occurs if there are any common members between the two sets."""
	def hasRestrictions(self)->bool:
		"""hasRestrictions() -> bool

		Returns true if this function set has restrictions on the type of objects that it may contain."""
	def restriction(self)->MFnSet.Restriction:
		"""restriction() -> MFnSet.Restriction

		Returns the type of membership restriction that this set has."""
	def annotation(self)->str:
		"""annotation() -> string

		Returns the annotation string for this set.  This allows a description of the set to be stored with it."""
	def setAnnotation(self,annotation:Any)->Self:
		"""setAnnotation( annotation ) -> self

		Sets the annotation string for this set.  This allows a description of the set to be stored with it."""
	def getMemberPaths(self,shading:bool)->MDagPathArray:
		"""getMemberPaths( shading ) -> MDagPathArray

		Get the members of this set as an array of dagPaths.

		This will usually return the same dagPaths as will be contained in the getMembersmethod. If the shading flag is set to true, the list will consist only of dagPathsthat are affected by this set for the purposes of material assignments.

		* shading (bool) -  whether the list should only contain members of this set used for shading purposes."""
class MFnSingleIndexedComponent(MFnComponent):
	"""This function set allows you to create, edit, and query single indexed components.
	Single indexed components store 1 dimensional index values.

	__init__()
	Initializes a new, empty MFnSingleIndexedComponent object

	__init__(MObject component)
	Initializes a new MFnSingleIndexedComponent function set, attached to the specified component."""
	@property
	def elementMax(self)->Any:
		"""Biggest element plus 1 in the component."""
	@elementMax.setter
	def elementMax(self,value:Any)->None:...
	@overload
	def __init__(self)->None:
		"""Initializes a new, empty MFnSingleIndexedComponent object"""
	@overload
	def __init__(self,component:MObject)->None:
		"""Initializes a new MFnSingleIndexedComponent function set, attached to the specified component."""
	def addElement(self,element:int)->Self:
		"""addElement(int element) -> self

		Adds the specified element to the component."""
	@overload
	def addElements(self,arg:list[int])->Self:
		"""addElements([int]) -> self
		addElements(MIntArray) -> self

		Adds the specified elements to the component."""
	@overload
	def addElements(self,MIntArray:Any)->Self:
		"""addElements([int]) -> self
		addElements(MIntArray) -> self

		Adds the specified elements to the component."""
	def create(self,arg:int)->MObject:
		"""create(MFn Type constant) -> MObject

		Creates a new, empty component, attaches it to the function set and
		returns an MObject which references it."""
	def element(self,index:int)->int:
		"""element(index) -> int

		Returns the index'th element of the component."""
	def getCompleteData(self)->int:
		"""getCompleteData() -> int

		Returns the number of elements in the complete component, or 0 if the component is not complete."""
	def getElements(self)->MIntArray:
		"""getElements() -> MIntArray

		Returns all of the component's elements."""
	def setCompleteData(self,numElements:int)->Self:
		"""setCompleteData(numElements) -> self

		Marks the component as complete (i.e. contains all possible elements).
		numElements indicates the number of elements in the complete component."""
class MFnStringArrayData(MFnData,collections.abc.Sequence[MString]):
	"""Function set for node data consisting of an array of string."""
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def __len__(self)->int:
		"""Return len(self)."""
	def __getitem__(self,index:int)->MString:
		"""Return self[key]."""
	def __setitem__(self,index:int,value:MString)->None:
		"""Set self[key] to value."""
	def __delitem__(self,index:int)->None:
		"""Delete self[key]."""
	def array(self)->list[str]:
		"""Returns the encapsulated array as a list of strings."""
	@overload
	def create(self)->MObject:
		"""Creates a new empty string array data object, attaches it to the function set and returns an MObject which references it."""
	@overload
	def create(self,seq:Sequence[str])->MObject:
		"""Creates a new string array data object, initializes it with the elements from seq , attaches it to the function set and returns an MObject which references it."""
	@overload
	def set(self,seq:Sequence[str])->Self:
		"""Replaces the elements in the encapsulated array with those from the supplied sequence."""
	@overload
	def set(self,value:str,index:int)->Self:
		"""Sets the value of the index 'th array element."""
class MFnStringData(MFnData):
	"""Function set for string node data."""
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	@overload
	def create(self)->MObject:
		"""Creates a new empty string data object, attaches it to the function set and returns an MObject which references it."""
	@overload
	def create(self,str:str)->MObject:
		"""Creates a new string data object, initializes it with str , attaches it to the function set and returns an MObject which references it."""
	def set(self,str:str)->Self:
		"""Replaces the contents of the encapsulated string with that of str ."""
	def string(self)->str:
		"""Returns a copy of the encapsulated string."""
class MFnTransform(MFnDagNode):
	"""Function set for operating on transform nodes."""
	kScaleMinX:int=0
	kScaleMaxX:int=1
	kScaleMinY:int=2
	kScaleMaxY:int=3
	kScaleMinZ:int=4
	kScaleMaxZ:int=5
	kShearMinXY:int=6
	kShearMaxXY:int=7
	kShearMinXZ:int=8
	kShearMaxXZ:int=9
	kShearMinYZ:int=10
	kShearMaxYZ:int=11
	kRotateMinX:int=12
	kRotateMaxX:int=13
	kRotateMinY:int=14
	kRotateMaxY:int=15
	kRotateMinZ:int=16
	kRotateMaxZ:int=17
	kTranslateMinX:int=18
	kTranslateMaxX:int=19
	kTranslateMinY:int=20
	kTranslateMaxY:int=21
	kTranslateMinZ:int=22
	kTranslateMaxZ:int=23
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	@staticmethod
	def balanceTransformation(*args)->Any:
		"""Balance a transformation when applying a world matrix to a joint. Thisaccesses the same underlying functionality as the xform command.
		mtx The world matrix to be applied to the joint node, as an MTransformationMatrixrotateAxis The joint's rotateAxis attribute, as an MQuaternionjointOrient The joint's jointOrient attribute, as an MQuaternionsegmentScaleCompensate The joint's segmentScaleCompensate attribute, as a boolinverseScale The joint's inverseScale attribute, as an MVectorrotateOrder The joint's rotateOrder attribute, as an MEulerRotation::RotationOrder
		Returns:List consisting of:localTranslate The resulting translation, as an MVectorlocalRotate The resulting rotation for the joint, as an MEulerRotationlocalScale The resulting scale for the joint, as an MVector"""
	def clearRestPosition(self)->Self:
		"""Clears the transform's rest position matrix, effectively setting it to the identity matrix."""
	def create(self,parent:MObject=MObject.kNullObj)->MObject:
		"""Creates a new transform node, parents it under parent , attaches it to the function set and returns it in an MObject . If parent is MObject.kNullObj then the new transform will be parented under the world."""
	def enableLimit(self,limitType:int,state:bool)->Self:
		"""Enables or disables the specified limitType ."""
	def isLimited(self,limitType:int)->bool:
		"""Returns True if the specified limitType is enabled."""
	def limitValue(self,limitType:int)->float:
		"""Returns the value of the specified limit."""
	def resetFromRestPosition(self)->Self:
		"""Resets the transform from its rest position matrix."""
	def resetTransformation(self,*args)->Any:
		"""Resets the transform's attribute values to represent the given transformation matrix in world space."""
	def restPosition(self)->MTransformationMatrix:
		"""Returns the transform's rest position matrix, or the identity matrix if no rest position has been set."""
	def rotateBy(self,rot:MQuaternion|MEulerRotation,space:int)->Self:
		"""Adds rot to the transform's rotation component."""
	def rotateByComponents(self,seq:Sequence[float|int],space:int,asQuaternion:bool=False)->Self:
		"""Adds the rotation represented by the four parameter values to the transform's rotate component. If asQuaternion is True then seq must contain four floats representing the x, y, z and w components of a quaternion rotation. If asQuaternion is False then seq must contain three floats representing the x, y and z angles, followed by an MTransformationMatrix Rotation Order constant, which together form an Euler rotation."""
	def rotatePivot(self,space:int)->MPoint:
		"""Returns the transform's rotate pivot component."""
	def rotatePivotTranslation(self,space:int)->MVector:
		"""Returns the transform's rotate pivot translation component."""
	def rotation(self,space:int=MSpace.kTransform,asQuaternion:bool=False)->MEulerRotation|MQuaternion:
		"""Returns the transform's rotation component as either an Euler rotation or a quaternion."""
	def rotationComponents(self,space:int=MSpace.kTransform,asQuaternion:bool=False)->list[float|order]|list[float]:
		"""Returns a list containing the four components of the transform's rotate component. If asQuaternion is True then the first three elements are the quaternion's unreal x, y, and z components, and the fourth is its real w component. If asQuaternion is False then the first three components are the x, y and z Euler rotation angles and the fourth is an MTransformationMatrix Rotation Order constant."""
	def rotationOrder(self)->int:
		"""Returns the order of rotations when the transform's rotate component is expressed as an euler rotation."""
	def rotateOrientation(self,space:int)->MQuaternion:
		"""Returns the rotation which orients the local rotation space."""
	def scale(self)->list[float]:
		"""Returns a list containing the transform's scale components."""
	def scaleBy(self,seq:Sequence[float])->Self:
		"""Multiplies the transform's scale components by the three floats in seq ."""
	def scalePivot(self,space:int)->MPoint:
		"""Returns the transform's scale pivot component."""
	def scalePivotTranslation(self,space:int)->MVector:
		"""Returns the transform's scale pivot translation component."""
	def setLimit(self,limitType:int,value:float)->Self:
		"""Sets the value of the specified limit."""
	def setRestPosition(self,matrix:MTransformationMatrix)->Self:
		"""Sets the transform's rest position matrix."""
	def setRotatePivot(self,pivot:MPoint,space:int,balance:bool)->Self:
		"""Sets the transform's rotate pivot component."""
	def setRotatePivotTranslation(self,trans:MVector,space:int)->Self:
		"""Sets the transform's rotate pivot translation component."""
	def setRotation(self,rot:MQuaternion|MEulerRotation,space:int)->Self:
		"""Sets the transform's rotation component to rot ."""
	def setRotationComponents(self,seq:Sequence[float|int],space:int=MSpace.kTransform,asQuaternion:bool=False)->Self:
		"""Sets the transform's rotate component. If asQuaternion is True then seq must contain four floats representing the x, y, z and w components of a quaternion rotation. If asQuaternion is False then seq must contain three floats representing the x, y and z angles, followed by an MTransformationMatrix Rotation Order constant, which together form an Euler rotation."""
	def setRotationOrder(self,order:int,reorder:bool)->Self:
		"""Sets the transform's rotation order. If reorder is True then the X, Y and Z rotations will be modified so that the resulting rotation under the new order is the same as it was under the old. If reorder is False then the X, Y and Z rotations are unchanged."""
	def setRotateOrientation(self,rot:MQuaternion,space:int,balance:bool)->Any:
		"""Sets the rotation which orients the local rotation space. If balance is True then the transform's other components will be adjusted to give the same overall transformation as before."""
	def setScale(self,seq:Sequence[float])->Self:
		"""Sets the transform's scale components to the three floats in seq ."""
	def setScalePivot(self,pivot:MPoint,space:int,balance:bool)->Self:
		"""Sets the transform's scale pivot component."""
	def setScalePivotTranslation(self,trans:MVector,space:int)->Self:
		"""Sets the transform's scale pivot translation component."""
	def setShear(self,seq:Sequence[float])->Self:
		"""Sets the transform's shear component."""
	def setTransformation(self,transformation:MTransformationMatrix)->Self:
		"""Sets this transform's attribute values to represent the given transformation matrix."""
	def setTranslation(self,trans:MVector,space:int)->Self:
		"""Sets the transform's translation component."""
	def shear(self)->list[float]:
		"""Returns a list containing the transform's shear component."""
	def shearBy(self,seq:Sequence[float])->Self:
		"""Multiplies the transform's shear components by the elements of seq ."""
	def transformation(self)->MTransformationMatrix:
		"""Returns the transformation matrix represented by this transform."""
	def translateBy(self,vec:MVector,space:int)->Self:
		"""Adds vec to the transform's translation component."""
	def translation(self,space:int)->MVector:
		"""Returns the transform's translation component as a vector."""
class MFnTripleIndexedComponent(MFnComponent):
	"""This function set allows you to create, edit, and query triple indexed
	components. Triple indexed components store 3 dimensional index values.

	__init__()
	Initializes a new, empty MFnTripleIndexedComponent object

	__init__(MObject component)
	Initializes a new MFnTripleIndexedComponent function set, attached
	to the specified component."""
	@overload
	def __init__(self)->None:
		"""Initializes a new, empty MFnTripleIndexedComponent object"""
	@overload
	def __init__(self,component:MObject)->None:
		"""Initializes a new MFnTripleIndexedComponent function set, attached
		to the specified component."""
	@overload
	def addElement(self,sIndex:int,tIndex:int,uIndex:int)->Self:
		"""addElement(sIndex, tIndex, uIndex) -> self
		addElement([sIndex, tIndex, uIndex]) -> self

		Adds the element identified by (sIndex, tIndex, uIndex) to the component."""
	@overload
	def addElement(self,arg:list[int])->Self:
		"""addElement(sIndex, tIndex, uIndex) -> self
		addElement([sIndex, tIndex, uIndex]) -> self

		Adds the element identified by (sIndex, tIndex, uIndex) to the component."""
	def addElements(self,arg:Sequence[int])->Self:
		"""addElements(sequence of [sIndex, tIndex, uIndex]) -> self

		Adds the specified elements to the component. Each item in the
		elements sequence is itself a sequence of three ints which are the
		S, T and U indices of an element to be added."""
	def create(self,arg:int)->MObject:
		"""create(MFn Type constant) -> MObject

		Creates a new, empty component, attaches it to the function set and
		returns an MObject which references it."""
	def getCompleteData(self)->tuple[int,int,int]:
		"""getCompleteData() -> (numS, numT, numU)

		Returns a tuple containing the number of S, T and U indices in
		the complete component, or (0,0,0) if the component is not complete."""
	def getElement(self,index:int)->tuple[int,int,int]:
		"""getElement(index) -> (sIndex, tIndex, uIndex)

		Returns the index'th element of the component as a tuple containing the
		element's S, T and U indices."""
	def getElements(self)->list[int]:
		"""getElements() -> list of (sIndex, tIndex, uIndex)

		Returns all of the component's elements as a list of tuples with each
		tuple containing the S, T and U indices of a single element."""
	def setCompleteData(self,numS:int,numT:int,numU:int)->Self:
		"""setCompleteData(numS, numT, numU) -> self

		Marks the component as complete (i.e. contains all possible elements).
		numS, numT and numU indicate the number of S, T and U indices
		in the complete component (i.e. the max S index is numS-1, the max T
		index is numT-1 and the max U index is numU-1)."""
class MFnTypedAttribute(MFnAttribute):
	"""Functionset for creating and working typed attributes."""
	@property
	def default(self)->MObject:
		"""Default value"""
	@default.setter
	def default(self,value:MObject)->None:...
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def attrType(self)->int:
		"""Returns the type of data handled by the attribute."""
	def create(self,longName:str,shortName:str,type:MTypeId|int,defaultValue:MObject=MObject.kNullObj)->MObject:
		"""Creates a new attribute of the given type with the given longName , shortName and defaultValue , attaches it to the function set and returns it in an MObject ."""
class MFnUInt64ArrayData(MFnData,collections.abc.Sequence[int]):
	"""Function set for node data consisting of an array of MUint64."""
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def __len__(self)->int:
		"""Return len(self)."""
	def __getitem__(self,index:int)->int:
		"""Return self[key]."""
	def __setitem__(self,index:int,value:int)->None:
		"""Set self[key] to value."""
	def __delitem__(self,index:int)->None:
		"""Delete self[key]."""
	def array(self)->MUint64Array:
		"""Returns the encapsulated array as an MUint64Array . For performance reasons the returned array is a live reference to the encapsulated array so changes made to one directly affect the other. The returned array is only valid for as long as the function set retains the same data object. If the function set is destroyed or attached to a different object then the returned array should be discarded. Failure to do so could result in Maya becoming unstable."""
	def copyTo(self,array:MUint64Array)->Self:
		"""Replaces the elements of array with those in the encapsulated array."""
	@overload
	def create(self)->MObject:
		"""Creates a new empty unsigned long array data object, attaches it to the function set and returns an MObject which references it."""
	@overload
	def create(self,array:MUint64Array|Sequence[int])->MObject:
		"""Creates a new unsigned long array data object, initializes it with the elements from array , attaches it to the function set and returns an MObject which references it."""
	@overload
	def set(self,array:MUint64Array|Sequence[int])->Self:
		"""Replaces the elements in the encapsulated array with those from the supplied array ."""
	@overload
	def set(self,value:int|int,index:int)->Self:
		"""Sets the value of the index 'th array element."""
class MFnUnitAttribute(MFnAttribute):
	"""Functionset for creating and working with angle, distance and time attributes."""
	@property
	def default(self)->Any:
		"""Default value"""
	@default.setter
	def default(self,value:Any)->None:...
	kInvalid:int=0
	kAngle:int=1
	kDistance:int=2
	kTime:int=3
	kLast:int=4
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	@overload
	def create(self,longName:str,shortName:str,type:int,defaultValue:float=0.0)->MObject:
		"""Creates a new attribute of the given type with the given longName , shortName and defaultValue , attaches it to the function set and returns it in an MObject ."""
	@overload
	def create(self,longName:str,shortName:str,defaultValue:MAngle|MDistance|MTime)->MObject:
		"""Creates a new angle, distance or time attribute, depending upon the type of the defaultValue , with the given longName , shortName , attaches it to the function set and returns it in an MObject ."""
	def getMax(self)->MAngle|MDistance|MTime:
		"""Returns the attribute's hard maximum value. Raises a RuntimeError if the attribute does not have a hard maximum."""
	def getMin(self)->MAngle|MDistance|MTime:
		"""Returns the attribute's hard minimum value. Raises a RuntimeError if the attribute does not have a hard minimum."""
	def getSoftMax(self)->MAngle|MDistance|MTime:
		"""Returns the attribute's soft maximum value. Raises a RuntimeError if the attribute does not have a soft maximum."""
	def getSoftMin(self)->MAngle|MDistance|MTime:
		"""Returns the attribute's soft minimum value. Raises a RuntimeError if the attribute does not have a soft minimum."""
	def hasMax(self)->bool:
		"""Returns True if a hard maximum value has been specified for the attribute."""
	def hasMin(self)->bool:
		"""Returns True if a hard minimum value has been specified for the attribute."""
	def hasSoftMax(self)->bool:
		"""Returns True if a soft maximum value has been specified for the attribute."""
	def hasSoftMin(self)->bool:
		"""Returns True if a soft minimum value has been specified for the attribute."""
	def setMax(self,maxValue:float|MAngle|MDistance|MTime)->Self:
		"""Sets the attribute's hard maximum to maxValue"""
	def setMin(self,minValue:float|MAngle|MDistance|MTime)->Self:
		"""Sets the attribute's hard minimum to minValue ."""
	def setSoftMax(self,maxValue:float|MAngle|MDistance|MTime)->Self:
		"""Sets the attribute's soft maximum to maxValue ."""
	def setSoftMin(self,minValue:float|MAngle|MDistance|MTime)->Self:
		"""Sets the attribute's soft minimum to minValue ."""
	def unitType(self)->int:
		"""Returns the type of data handled by the attribute."""
class MFnVectorArrayData(MFnData,collections.abc.Sequence[MVector]):
	"""Function set for node data consisting of an array of MVectors."""
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def __len__(self)->int:
		"""Return len(self)."""
	def __getitem__(self,index:int)->MVector:
		"""Return self[key]."""
	def __setitem__(self,index:int,value:MVector)->None:
		"""Set self[key] to value."""
	def __delitem__(self,index:int)->None:
		"""Delete self[key]."""
	def array(self)->MVectorArray:
		"""Returns the encapsulated array as an MVectorArray . For performance reasons the returned array is a live reference to the encapsulated array so changes made to one directly affect the other. The returned array is only valid for as long as the function set retains the same data object. If the function set is destroyed or attached to a different object then the returned array should be discarded. Failure to do so could result in Maya becoming unstable."""
	def copyTo(self,array:MVectorArray)->Self:
		"""Replaces the elements of array with those in the encapsulated array."""
	@overload
	def create(self)->MObject:
		"""Creates a new empty MVector array data object, attaches it to the function set and returns an MObject which references it."""
	@overload
	def create(self,array:MVectorArray|Sequence[MVector])->MObject:
		"""Creates a new MVector array data object, initializes it with the elements from array , attaches it to the function set and returns an MObject which references it."""
	@overload
	def set(self,array:MVectorArray|Sequence[MVector])->Self:
		"""Replaces the elements in the encapsulated array with those from the supplied array ."""
	@overload
	def set(self,value:MVector,index:int)->Self:
		"""Sets the value of the index 'th array element."""
class MGlobal:
	"""Static class providing common API global functions.
	"""
	kInteractive:int=0
	kBatch:int=1
	kLibraryApp:int=2
	kBaseUIMode:int=3
	kReplaceList:int=0
	kXORWithList:int=1
	kAddToList:int=2
	kRemoveFromList:int=3
	kAddToHeadOfList:int=4
	kSurfaceSelectMethod:int=0
	kWireframeSelectMethod:int=1
	kSelectObjectMode:int=0
	kSelectComponentMode:int=1
	kSelectRootMode:int=2
	kSelectLeafMode:int=3
	kSelectTemplateMode:int=4
	kHighIdlePriority:int=0
	kLowIdlePriority:int=1
	kVeryLowIdlePriority:int=2
	@staticmethod
	def animSelectionMask()->MSelectionMask:
		"""animSelectionMask() -> MSelectionMask

		Returns the animation selection mask."""
	@staticmethod
	def componentSelectionMask()->MSelectionMask:
		"""componentSelectionMask() -> MSelectionMask

		Returns the component selection mask."""
	@staticmethod
	def displayError(msg:str)->Any:
		"""Display an error in the script editor."""
	@staticmethod
	def displayInfo(msg:str)->Any:
		"""Display an informational message in the script editor."""
	@staticmethod
	def displayWarning(msg:str)->Any:
		"""Display a warning in the script editor."""
	@staticmethod
	def getActiveSelectionList()->MSelectionList:
		"""Returns a copy of the active selection list."""
	@staticmethod
	def getFunctionSetList(object:MObject)->tuple[str,...]:
		"""Returns a tuple of strings that represent the type of each function set that will accept this object."""
	@staticmethod
	def getRichSelection(defaultToActiveSelection:Any=True)->MRichSelection:
		"""getRichSelection(defaultToActiveSelection=True) -> MRichSelection

		Returns the current rich selection (usually the active selection with
		any soft selection and symmetry applied). If no rich selection exists
		and 'defaultToActiveSelection' is True, the current active selection
		will be returned instead."""
	@staticmethod
	def getSelectionListByName(name:str)->MSelectionList:
		"""Returns a selection list with all of the objects that match the specified name . The name may use the same type of regular expressions as can be used in MEL commands. For example, the pattern "pCube*" will match all occurrences of objects whose names begin with "pCube"."""
	@staticmethod
	def miscSelectionMask()->MSelectionMask:
		"""miscSelectionMask() -> MSelectionMask

		Returns the miscellaneous selection mask."""
	@staticmethod
	def objectSelectionMask()->MSelectionMask:
		"""objectSelectionMask() -> MSelectionMask

		Returns the object selection mask."""
	@staticmethod
	def selectionMode()->int:
		"""selectionMode() -> int

		Get current selection mode:
		  kSelectObjectMode     Objects are selected as a whole. Components are not directly accessible.
		  kSelectComponentMode  Components such as vertices are selectable in this mode.
		  kSelectRootMode       Selecting the child in a hierarchy will also select its root DAG node.
		  kSelectLeafMode       Selecting the child in a hierarchy will result only in that child being selected.
		  kSelectTemplateMode   Templated objects are selectable in this mode."""
	@staticmethod
	def setActiveSelectionList(MSelectionList:Any,listAdjustment:int=MGlobal.kReplaceList)->None:
		"""setActiveSelectionList(MSelectionList, listAdjustment=kReplaceList) -> None

		Set the active selection list.
		The selection items on the given list will update the contents of the active selection
		list as indicated by the listAdjustment parameter.
		Valid listAdjustment values are:
		  kReplaceList      #Totally replace the list with the given items.
		  kXORWithList      #Items already in the list will be removed. New items will be appended to the end of the list.
		  kAddToList        #Add the items to the end of the list.
		  kRemoveFromList   #Remove the items from the list.
		  kAddToHeadOfList  #Add the items to the beginning of the list."""
	@staticmethod
	@overload
	def setAnimSelectionMask(mask:MSelectionMask)->MGlobal:
		"""setAnimSelectionMask(mask) -> selfsetAnimSelectionMask(type) -> self

		Set the animation selection mask to the supplied value.

		* mask (MSelectionMask) - The selection mask.
		* type (int) - The selection type (see MSelectionMask.addMask() for a list of values)."""
	@overload
	@staticmethod
	def setAnimSelectionMask(type:int)->MGlobal:
		"""setAnimSelectionMask(mask) -> selfsetAnimSelectionMask(type) -> self

		Set the animation selection mask to the supplied value.

		* mask (MSelectionMask) - The selection mask.
		* type (int) - The selection type (see MSelectionMask.addMask() for a list of values)."""
	@staticmethod
	@overload
	def setComponentSelectionMask(mask:MSelectionMask)->MGlobal:
		"""setComponentSelectionMask(mask) -> selfsetComponentSelectionMask(type) -> self

		Set the component selection mask to the supplied value.

		* mask (MSelectionMask) - The selection mask.
		* type (int) - The selection type (see MSelectionMask.addMask() for a list of values)."""
	@overload
	@staticmethod
	def setComponentSelectionMask(type:int)->MGlobal:
		"""setComponentSelectionMask(mask) -> selfsetComponentSelectionMask(type) -> self

		Set the component selection mask to the supplied value.

		* mask (MSelectionMask) - The selection mask.
		* type (int) - The selection type (see MSelectionMask.addMask() for a list of values)."""
	@staticmethod
	@overload
	def setMiscSelectionMask(mask:MSelectionMask)->MGlobal:
		"""setMiscSelectionMask(mask) -> selfsetMiscSelectionMask(type) -> self

		Set the miscellaneous selection mask to the supplied value.

		* mask (MSelectionMask) - The selection mask.
		* type (int) - The selection type (see MSelectionMask.addMask() for a list of values)."""
	@overload
	@staticmethod
	def setMiscSelectionMask(type:int)->MGlobal:
		"""setMiscSelectionMask(mask) -> selfsetMiscSelectionMask(type) -> self

		Set the miscellaneous selection mask to the supplied value.

		* mask (MSelectionMask) - The selection mask.
		* type (int) - The selection type (see MSelectionMask.addMask() for a list of values)."""
	@staticmethod
	@overload
	def setObjectSelectionMask(mask:MSelectionMask)->MGlobal:
		"""setObjectSelectionMask(mask) -> selfsetObjectSelectionMask(type) -> self

		Set the object selection mask to the supplied value.

		* mask (MSelectionMask) - The selection mask.
		* type (int) - The selection type (see MSelectionMask.addMask() for a list of values)."""
	@overload
	@staticmethod
	def setObjectSelectionMask(type:int)->MGlobal:
		"""setObjectSelectionMask(mask) -> selfsetObjectSelectionMask(type) -> self

		Set the object selection mask to the supplied value.

		* mask (MSelectionMask) - The selection mask.
		* type (int) - The selection type (see MSelectionMask.addMask() for a list of values)."""
	@staticmethod
	def setRichSelection(MRichSelection:Any)->None:
		"""setRichSelection(MRichSelection) -> None

		Set the current rich selection."""
	@staticmethod
	def setSelectionMode(int:int)->None:
		"""setSelectionMode(int) -> None

		Set the current selection mode.
		See selectionMode() for a list of valid modes."""
	@staticmethod
	def isUndoing()->bool:
		"""isUndoing() -> bool

		true if Maya is currently in the middle of an undo."""
	@staticmethod
	def isRedoing()->bool:
		"""isRedoing() -> bool

		true if Maya is currently in the middle of a redo."""
	@staticmethod
	def mayaName()->str:
		"""mayaName() -> string

		Returns a string containing name of running application."""
	@staticmethod
	def mayaVersion()->str:
		"""mayaVersion() -> string

		Returns a string describing this version of Maya."""
	@staticmethod
	def apiVersion()->int:
		"""apiVersion() -> int

		Returns a number describing the version of the Maya API at runtime."""
	@staticmethod
	def mayaFeatureSet()->int:
		"""mayaFeatureSet() -> int

		Returns an enumerated type specifying if Maya API has unlimited set of features.
		  kComplete  Running Maya version with all features available.
		  kRestricted  Running Maya version with some features limited in availability."""
	@staticmethod
	def mayaState()->int:
		"""mayaState() -> int

		Returns an enumerated type specifying the way in which Maya was invoked.
		  kInteractive  Running with a UI
		  kBatch  Running without a UI
		  kLibraryApp  Running as a standalone (MLibrary) application.
		  kBaseUIMode  Running with UI enabled but Maya's std UI scripts not run."""
	@staticmethod
	def getLiveList()->MSelectionList:
		"""getLiveList() -> MSelectionList

		Returns a copy of the live list. When a user performs a
		"Modify->Make Live" in the user interface the currently selected
		objects are added to the live list."""
	@staticmethod
	def getHiliteList()->MSelectionList:
		"""getHiliteList() -> MSelectionList

		Returns a copy of the hilite list.  The hilite list contains all DAG objects
		that are hilited for component selection mode.  (e.g. when the user right clicks
		over a Mesh object and chooses the "vertex" option the Mesh line drawing changes
		color and the mesh is added to the hiliteList.)"""
	@staticmethod
	def setHiliteList(MSelectionList:Any)->None:
		"""setHiliteList(MSelectionList) -> None

		Sets the current hilite list. The current selection list is unchanged."""
	@staticmethod
	def getPreselectionHiliteList()->MSelectionList:
		"""getPreselectionHiliteList() -> MSelectionList

		Gets the objects for which Maya is displaying a preselection
		highlight in the viewports."""
	@staticmethod
	def setPreselectionHiliteList(MSelectionList:Any)->None:
		"""setPreselectionHiliteList(MSelectionList) -> None

		Sets the objects for which Maya will display a preselection
		highlight in the viewports.

		The objects/components in the list will be drawn in Maya's
		preselection highlight style on the next viewport refresh
		(if preselection highlighting is enabled in the preferences).

		If preselection highlighting is not enabled, Maya will still
		store the list."""
	@staticmethod
	def selectCommand(MSelectionList:Any,listAdjustment:int=MGlobal.kReplaceList)->None:
		"""selectCommand(MSelectionList, listAdjustment=kReplaceList) -> None

		Set the active selection list, by calling the built in Maya select
		command.  This differs from setActiveSelectionList in that in this
		version Maya takes over the selection list you give it and will be
		responsible for maintaing the necessary information required for
		undo, redo, and journaling."""
	@staticmethod
	def selectByName(string:str,listAdjustment:int=MGlobal.kReplaceList)->None:
		"""selectByName(string, listAdjustment=kReplaceList) -> None

		Puts objects that match the give name on the active selection list."""
	@staticmethod
	def unselectByName(string:str)->None:
		"""unselectByName(string) -> None

		Removes objects matching the pattern from the active selection list."""
	@staticmethod
	@overload
	def unselect(MObject:Any)->None:
		"""unselect(MObject) -> None
		unselect(MDagPath, MObject) -> None

		Remove the given object/components from the active selection list.
		If components is null then the object will be unselected, otherwise
		the components will be unselected.

		Perform marquee type selection on the dag.  If an object intersects the
		selection rectangle, it is selected according to listAdjustment."""
	@overload
	@staticmethod
	def unselect(MDagPath:Any,MObject:Any)->None:
		"""unselect(MObject) -> None
		unselect(MDagPath, MObject) -> None

		Remove the given object/components from the active selection list.
		If components is null then the object will be unselected, otherwise
		the components will be unselected.

		Perform marquee type selection on the dag.  If an object intersects the
		selection rectangle, it is selected according to listAdjustment."""
	@staticmethod
	@overload
	def selectFromScreen(short:int,short2:int,listAdjustment:int=MGlobal.kAddToList,selectMethod:int=MGlobal.kWireframeSelectMethod)->None:
		"""selectFromScreen(short, short, listAdjustment=kAddToList, selectMethod=kWireframeSelectMethod) -> None
		selectFromScreen(short, short, short, short, listAdjustment=kAddToList, selectMethod=kWireframeSelectMethod) -> None

		Perform click-pick type selection on the dag. If an object intersects
		the click point then it is selected according to listAdjustment."""
	@overload
	@staticmethod
	def selectFromScreen(short:int,short2:int,short3:int,short4:int,listAdjustment:int=MGlobal.kAddToList,selectMethod:int=MGlobal.kWireframeSelectMethod)->None:
		"""selectFromScreen(short, short, listAdjustment=kAddToList, selectMethod=kWireframeSelectMethod) -> None
		selectFromScreen(short, short, short, short, listAdjustment=kAddToList, selectMethod=kWireframeSelectMethod) -> None

		Perform click-pick type selection on the dag. If an object intersects
		the click point then it is selected according to listAdjustment."""
	@staticmethod
	def isSelected(MObject:Any)->bool:
		"""isSelected(MObject) -> bool

		Determines whether the given object is on the active selection list."""
	@staticmethod
	def selectionMethod()->int:
		"""selectionMethod() -> int

		Determines the selection method that should be used in the currently active
		viewport.  This is useful as input to the "selectFromScreen" functions."""
	@staticmethod
	def clearSelectionList()->None:
		"""clearSelectionList() -> None

		Removes all items from the active selection list."""
	@staticmethod
	def trackSelectionOrderEnabled()->bool:
		"""trackSelectionOrderEnabled() -> bool

		Returns whether the selection order is currerntly being tracked."""
	@staticmethod
	def setTrackSelectionOrderEnabled()->None:
		"""setTrackSelectionOrderEnabled() -> None

		Set whether Maya should maintain an active selection list which
		maintains object and component selection order."""
	@staticmethod
	def addToModel(MObject:Any,MObject2:Any)->None:
		"""addToModel(MObject, MObject) -> None

		This method is used to add new dag objects to the model.  If no parent node
		is specified, then the node is added under the world.  When a node is
		added under the world, then a transform node is automatically created as
		a parent.  This assumes that the node being added is not already a
		transform node.
		This method is only valid for dag nodes. If the specified
		object is not of type MFn::kDagNode then MS::kInvalidParameter will be returned."""
	@staticmethod
	def addToModelAt(MObject:Any,MVector:Any,arg:Any,arg2:Any,rotateOrder:Any=MTransformationMatrix.kXYZ)->None:
		"""addToModelAt(MObject, MVector, double[3], double[3], rotateOrder=MTransformationMatrix.kXYZ) -> None

		Adds the specified dag object to the DAG and transform the object
		by the specified arguments.
		This method is only valid for dag nodes. If the specified
		object is not of type MFn::kDagNode then MS::kInvalidParameter
		will be returned."""
	@staticmethod
	def removeFromModel(MObject:Any)->None:
		"""removeFromModel(MObject) -> None

		Removes the specified dag node from the scene.
		This method is only valid for dag nodes. If the specified
		object is not of type MFn::kDagNode then MS::kInvalidParameter
		will be returned.

		Note that this method doesn't delete the dag node which means
		the node must be added back to scene by calling either
		MGlobal::addToModel() or MGlobal::addToModelAt() in later
		calls, otherwise the dag node is leaked. To delete the dag node,
		call MGlobal::deleteNode() instead."""
	@staticmethod
	def deleteNode(MObject:Any)->None:
		"""deleteNode(MObject) -> None

		Delete the given dag node or dependency graph node."""
	@staticmethod
	def executeCommandOnIdle(string:str,displayEnabled:bool=False)->None:
		"""executeCommandOnIdle(string, bool displayEnabled=False) -> None

		Sets a MEL command to execute on the next idle event. Since the command
		will likely not be executed until some time after control is returned to
		caller, there is no access to the command results.

		This method is thread safe and can be called from a thread other than
		Maya's main thread. However, that thread must still be part of the Maya
		process. Calling this method from a completely separate process will
		not work and may lead to unpredictable behaviour."""
	@staticmethod
	def executeCommandOnIdleWithPriority(string:str,priority:int,displayEnabled:bool=False)->None:
		"""executeCommandOnIdleWithPriority(string, int priority, bool displayEnabled=False) -> None

		Sets a MEL command to execute on the next idle event with the given priority.
		Since the command will likely not be executed until some time after control is
		returned to caller, there is no access to the command results.

		This method is thread safe and can be called from a thread other than
		Maya's main thread. However, that thread must still be part of the Maya
		process. Calling this method from a completely separate process will
		not work and may lead to unpredictable behaviour."""
	@staticmethod
	def executeCommandStringResult(string:str,displayEnabled:bool=False,undoEnabled:bool=False)->str|list[str]:
		"""executeCommandStringResult(string, bool displayEnabled=False, bool undoEnabled=False) -> string or [string, string, ...]

		Executes a MEL command that returns a string or an array of strings
		result from the command engine depending on the number of return values.
		Optionally allows display of the command in the Command Window to be
		enabled or disabled.  Defaults to disabled.  Optionally allows undo
		for the command to be enabled or disabled.  Defaults to disabled.

		Note: This is not thread safe; you may use executeCommandOnIdle instead"""
	@staticmethod
	def optionVarIntValue(string:str)->int:
		"""optionVarIntValue(string) -> int

		This method is used to get the option variable value of int type"""
	@staticmethod
	def optionVarDoubleValue(string:str)->float:
		"""optionVarDoubleValue(string) -> double

		This method is used to get the option variable value of type double"""
	@staticmethod
	def optionVarStringValue(string:str)->str:
		"""optionVarStringValue(string) -> MString

		This method is used to get the option variable value of type string"""
	@staticmethod
	@overload
	def setOptionVarValue(string:str,int:int)->bool:
		"""setOptionVarValue(string, int) -> bool
		setOptionVarValue(string name, double) -> bool
		setOptionVarValue(string name, string) -> bool


		This method is used to set the option variable value of int, bool, string type"""
	@overload
	@staticmethod
	def setOptionVarValue(name:str,double:Any)->bool:
		"""setOptionVarValue(string, int) -> bool
		setOptionVarValue(string name, double) -> bool
		setOptionVarValue(string name, string) -> bool


		This method is used to set the option variable value of int, bool, string type"""
	@overload
	@staticmethod
	def setOptionVarValue(name:str,string:str)->bool:
		"""setOptionVarValue(string, int) -> bool
		setOptionVarValue(string name, double) -> bool
		setOptionVarValue(string name, string) -> bool


		This method is used to set the option variable value of int, bool, string type"""
	@staticmethod
	@overload
	def initOptionVar(name:str,int:int,category:str)->bool:
		"""initOptionVar(string name, int, string category) -> bool
		initOptionVar(string name, double, string category) -> bool
		initOptionVar(string name, string, string category) -> bool


		This method is used to initialize an option variable value of int, bool, string type.
		This method will create the option var if it doesn't exist and set the default value
		and category."""
	@overload
	@staticmethod
	def initOptionVar(name:str,double:Any,category:str)->bool:
		"""initOptionVar(string name, int, string category) -> bool
		initOptionVar(string name, double, string category) -> bool
		initOptionVar(string name, string, string category) -> bool


		This method is used to initialize an option variable value of int, bool, string type.
		This method will create the option var if it doesn't exist and set the default value
		and category."""
	@overload
	@staticmethod
	def initOptionVar(name:str,string:str,category:str)->bool:
		"""initOptionVar(string name, int, string category) -> bool
		initOptionVar(string name, double, string category) -> bool
		initOptionVar(string name, string, string category) -> bool


		This method is used to initialize an option variable value of int, bool, string type.
		This method will create the option var if it doesn't exist and set the default value
		and category."""
	@staticmethod
	def removeOptionVar(string:str)->None:
		"""removeOptionVar(string) -> None

		This method is used to remove the option variable"""
	@staticmethod
	def optionVarExists(string:str)->bool:
		"""optionVarExists(string) -> bool

		This method is used to check if the option variable exists"""
	@staticmethod
	def resetToDefaultErrorLogPathName()->None:
		"""resetToDefaultErrorLogPathName() -> None

		Closes the current log file if it is open, and then resets the log path to
		the default path.
		Logging is disabled and the log file speicified by the default path is not opened.
		If logging is disabled, it remains disabled.
		Use startErrorLogging() to enable logging to the default log file.
		If the current path is the default path, no action is taken,
		but an invalid parameter error is returned.

		Note that if the default log is reopened after it is closed, all information
		previously logged to it is lost."""
	@staticmethod
	def defaultErrorLogPathName()->str:
		"""defaultErrorLogPathName() -> string

		Determines the default path name of the error log file.
		Returns an empty string on failure."""
	@staticmethod
	def setErrorLogPathName(string:str)->None:
		"""setErrorLogPathName(string) -> None

		Determines the default path name of the error log file.
		Returns an empty string on failure."""
	@staticmethod
	def errorLogPathName()->str:
		"""errorLogPathName() -> string

		Determines the path name of the current error log file.
		Returns the null stringon failure."""
	@staticmethod
	def errorLoggingIsOn()->bool:
		"""errorLoggingIsOn() -> bool

		This method determines whether or not API errors are being logged."""
	@staticmethod
	@overload
	def startErrorLogging()->None:
		"""startErrorLogging() -> None
		startErrorLogging(string)

		This method enables output to the API error log file specified by the path.
		If another error log file is already open this method time and date stamps
		the log, and closes it.
		The new error log is time and date stamped when it is opened.

		If the new path name is the same as the current path name, this method ensures
		that logging is enabled, but no other action is taken."""
	@overload
	@staticmethod
	def startErrorLogging(string:str)->None:
		"""startErrorLogging() -> None
		startErrorLogging(string)

		This method enables output to the API error log file specified by the path.
		If another error log file is already open this method time and date stamps
		the log, and closes it.
		The new error log is time and date stamped when it is opened.

		If the new path name is the same as the current path name, this method ensures
		that logging is enabled, but no other action is taken."""
	@staticmethod
	def stopErrorLogging()->None:
		"""stopErrorLogging() -> None

		This method disables output to the API error log but does not close the log file."""
	@staticmethod
	def closeErrorLog()->None:
		"""closeErrorLog() -> None

		This method closes the API error log file.  If error logging is currently
		enabled this method disables it.
		The error log is time and date stamped before it is closed.
		After the log is closed the error log path name is reset to the default
		path name.
		If the error log file is already closed, then no action is taken.

		Note that if a log is reopened after it is closed, all information previously
		logged to it is lost."""
	@staticmethod
	def doErrorLogEntry(string:str)->bool:
		"""doErrorLogEntry(string) -> bool

		Logs an entry in the currently open log file.  It is not necessary for error
		logging to be enabled, but a log file must be open.
		A newline is appended to each log entry."""
	@staticmethod
	def getAbsolutePathToResources()->str:
		"""getAbsolutePathToResources() -> string

		Return the absolute path of Maya's "Resources" fold on the system,
		including the "Resources" folder itself."""
	@staticmethod
	def disableStow()->bool:
		"""disableStow() -> bool

		This method is used to query if the disabling of Stowing (hiding)
		and Unstowing (showing) windows is active."""
	@staticmethod
	def setDisableStow(bool:bool)->None:
		"""setDisableStow(bool) -> None

		This method is used to make the visiblity of all Maya windows unchangable.
		If set to true, it disables any attempts to change the visiblity of any window.
		In addition, all popup windows will be supressed."""
	@staticmethod
	def sourceFile(string:str)->None:
		"""sourceFile(string) -> None

		Causes the MEL command engine to open the named file and execute
		the contents of the file as a MEL script.  If the provided fileName
		is a Unix absolute pathname, then that file is opened.  If a relative
		pathname is provided, the directories indicated by the environment
		variable, MAYA_SCRIPT_PATH, will be searched for a matching filename."""
	@staticmethod
	def setDisplayCVs(MSelectionList:Any,bool:bool)->None:
		"""setDisplayCVs(MSelectionList, bool) -> None

		Controls drawing of control points in the specified selection list.

		The selection items on the given list will be marked for drawing. This
		overrides Maya's current draw list and allow, for example, the drawing
		of control points without being in vertex selection mode."""
	@staticmethod
	def getAssociatedSets(MSelectionList:Any)->list:
		"""getAssociatedSets(MSelectionList) -> list

		This utility method finds all the sets that the items in
		the given selection list are members of."""
	@staticmethod
	@overload
	def viewFrame(double:Any)->None:
		"""viewFrame(double) -> None
		viewFrame(MTime) -> None

		Sets the global time to the specified time.  This function is optimized
		for sequential time values that are monotonically increasing.  While
		one can set the time randomly with this function, a significant
		performance hit will be incurred."""
	@overload
	@staticmethod
	def viewFrame(MTime:Any)->None:
		"""viewFrame(double) -> None
		viewFrame(MTime) -> None

		Sets the global time to the specified time.  This function is optimized
		for sequential time values that are monotonically increasing.  While
		one can set the time randomly with this function, a significant
		performance hit will be incurred."""
	@staticmethod
	def currentToolContext()->MObject:
		"""currentToolContext() -> MObject

		Returns the current tool context as an MObject."""
	@staticmethod
	def setYAxisUp()->None:
		"""setYAxisUp() -> None

		This method sets the flag to identify which axis is Up, and
		rotates the ground plane around around the X-axis 90 degrees to get
		the Y-Up from Z-Up."""
	@staticmethod
	def isYAxisUp()->bool:
		"""isYAxisUp() -> bool

		This method returns true if, currently, the Y-axis is UP."""
	@staticmethod
	def setZAxisUp()->None:
		"""setZAxisUp() -> None

		This method sets the flag to identify which axis is Up, and
		rotates the ground plane around around the X-axis 90 degrees to get
		the Y-Up from Y-Up."""
	@staticmethod
	def isZAxisUp()->bool:
		"""isZAxisUp() -> bool

		This method returns true if, currently, the Z-axis is UP."""
	@staticmethod
	def upAxis()->MVector:
		"""upAxis() -> MVector

		This method returns the model's current up axis."""
	@staticmethod
	def className()->str:
		"""className() -> string

		Returns the name of this class."""
class MImage:
	"""Manipulate color data."""
	kNoFormat:int=0
	kHeightFieldBumpFormat:int=1
	kNormalMapBumpFormat:int=2
	kUnknownFormat:int=3
	kUnknown:int=0
	kByte:int=1
	kFloat:int=2
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def pixelType(self)->int:
		"""pixelType() -> int

		Get the current pixel format of the image:  kUnknown    Format not known or invalid.
		  kByte       One byte per channel, ranging from 0 to 255.
		  kFloat      One float per channel, ranging from 0.0 to 1.0."""
	def depth(self)->int:
		"""depth() -> int

		Get the color depth (in bytes) of the currently opened image."""
	def isRGBA(self)->bool:
		"""isRGBA() -> bool

		Query flag which indicates whether the pixel information is in RGBA sequence or BGRA sequence.
		If no pixel data exists, then False will be returned."""
	def setRGBA(self,bool:bool)->Self:
		"""setRGBA(bool) -> self

		Sets a flag to indicate that pixel information is in RGBA sequence or BGRA sequence.
		Pixel data must have been allocated before this call is made."""
	def pixels(self)->int:
		"""pixels() -> long

		Returns a long containing a C++ 'unsigned char' pointer which points to the pixel data.
		This data is uncompressed and tightly packed, of size (width * height * depth) bytes.
		For the moment, pixels are always stored in a RGBA (depth=4 bytes) pixel format."""
	def floatPixels(self)->int:
		"""floatPixels() -> long

		Returns a long containing a C++ 'float' pointer which points to the pixel data.
		This data is uncompressed and tightly packed, of size (width * height * depth * sizeof( float)) bytes."""
	def haveDepth(self)->bool:
		"""haveDepth() -> bool

		Returns True if this instance of MImage contains a depth map."""
	def depthMap(self)->int:
		"""depthMap() -> long

		Returns a long containing a C++ 'float' pointer which points to the depth data."""
	def release(self)->Self:
		"""release() -> self

		Release the current image. If there is no current image, the call is ignored."""
	def verticalFlip(self)->bool:
		"""verticalFlip() -> bool

		Flips the image vertically."""
	def create(self,width:int,height:int,channels:int=4,type:int=MColor.kByte)->Self:
		"""create(width, height, channels=4, type=kByte) -> self

		Create a new MImage object. Allocates memory for an RGBA array of pixels
		of the given size. If an object was already in memory, it is released first.

		* width (unsigned int) - the desired image's width in pixels.
		* height (unsigned int) - the desired image's height in pixels.
		* channels (unsigned int) - the desired number of channels per pixel.
		* type (int) - the desired pixel format (kByte or kFloat, see MImage.pixelType() description for details.)"""
	def getSize(self)->list[width|height]:
		"""getSize() -> [width, height]

		Get the width and height of the currently opened image."""
	def resize(self,width:int,height:int,preserveAspectRatio:bool=True)->Self:
		"""resize(width, height, preserveAspectRatio=True) -> self

		Resize the currently opened image to the specified dimension, or to the closest
		width/height that is preserves the original aspect ratio.* width (unsigned int) - the desired image's width in pixels.
		* height (unsigned int) - the desired image's height in pixels.
		* preserveAspectRatio (bool) - specifies whether the aspect ratio should be preserved or not.
		         If this flag is set, the given width and height are interpreted as the maximum dimensions allowable."""
	def setPixels(self,pixels:char,width:int,height:int)->Self:
		"""setPixels(pixels, width, height) -> self

		Copy the uncompressed pixels array passed in into the MImage.
		This array is tightly packed, of size (width * height * depth) bytes.
		For the moment, pixels are always stored in a RGBA (depth=4 bytes) pixel format.

		* pixels (unsigned char*) - the variable containing a block of pixels.
		* width (unsigned int) - the variable that will be set to the image's width in pixels.
		* height (unsigned int) - the variable that will be set to the image's height in pixels."""
	def setFloatPixels(self,pixels:float,width:int,height:int,channels:int=4)->Self:
		"""setFloatPixels(pixels, width, height, channels=4) -> self

		Copy the uncompressed pixels array passed in into the MImage.
		This array is tightly packed, of size (width * height * depth) bytes.
		For the moment, pixels are always stored in a RGBA (depth=4 bytes) pixel format.

		* pixels (float*) - the variable containing a block of pixels.
		* width (unsigned int) - the variable that will be set to the image's width in pixels.
		* height (unsigned int) - the variable that will be set to the image's height in pixels.
		* channels (unsigned int) - the number of channels per pixel."""
	def getDepthMapSize(self)->list[width|height]:
		"""getDepthMapSize() -> [width, height]

		Returns the size of the depth map buffer."""
	def getDepthMapRange(self)->list[minValue|maxValue]:
		"""getDepthMapRange() -> [minValue, maxValue]

		Compute the minimum and maximum depth values (range) for any stored depth buffer."""
	def setDepthMap(self,depth:float,width:int,heigth:Any)->Self:
		"""setDepthMap(depth, width, heigth) -> self

		Specifies the depth map resolution and data.

		* depth (float*) - float buffer that contains depth values.
		* width (unsigned int) - the width of the depth buffer.
		* height (unsigned int) - the height of the depth buffer.

		* depth (MFloatArray) - float array that contains depth values.
		* width (unsigned int) - the width of the depth buffer.
		* height (unsigned int) - the height of the depth buffer."""
	@staticmethod
	def filterExists(sourceFormat:Any,targetFormat:Any)->bool:
		"""filterExists(sourceFormat, targetFormat) -> bool

		Return whether or not a given source format can be directly converted to a given target format.

		* sourceFormat (MImageFilterFormat) - the format of the source image.
		* targetFormat (MImageFilterFormat) - the format of the resulting image."""
	def filter(self,sourceFormat:Any,targetFormat:Any,scale:float=1.0,offset:float=1.0)->Self:
		"""filter(sourceFormat, targetFormat, scale=1.0, offset=1.0) -> self

		Modify the content of the image by applying a filter.
		The dimension of the image remains the same; only the RGBA components get affected.

		* sourceFormat (MImageFilterFormat) - the format of the source image.
		* targetFormat (MImageFilterFormat) - the format of the resulting image.* scale (float) - vary depending on the source/target format.
		* offset (float) - vary depending on the source/target format.

		The scale argument for this filter can vary from -256.0 to 256.0, although typical values range from 1.0 to 10.0.
		The offset argument is currently ignored and should be left to the default value of 0.0."""
	def readFromFile(self,pathname:str,type:int=MColor.kByte)->Self:
		"""readFromFile(pathname, type=kByte) -> self

		Attempt to identify and open the specified image file.

		* pathname (string) - the full path of the image file that should be opened.
		* type (MPixelType) - the desired pixel format. kUnknown attempts to load the native pixel type."""
	def readFromTextureNode(self,fileTextureObject:MObject,type:int=MColor.kByte)->Self:
		"""readFromTextureNode(fileTextureObject, type=kByte) -> self

		Attempt to read the content of the given file texture node.


		* fileTextureObject (MObject) - an object that refers to the file texture node that should be read.
		* type (MPixelType) - the desired pixel format. kUnknown attempts to load the native pixel type."""
	def readDepthMap(self,pathname:str)->Self:
		"""readDepthMap(pathname) -> self

		Reads the depth map from the specified file and place the result into the depth map array of this MImage instance."""
	def writeToFile(self,pathname:str,outputFormat:Any=iff)->Self:
		"""writeToFile(pathname, outputFormat=iff) -> self

		Save the content of this image in a file. By default, the file is saved in IFF format.
		Optionally, the file can also be converted in a variety of image formats."""
	def writeToFileWithDepth(self,pathname:str,outputFormat:Any=iff,writeDepth:Any=False)->Self:
		"""writeToFileWithDepth(pathname, outputFormat=iff, writeDepth=False) -> self

		Save the content of this image in a file. By default, the file is saved in IFF format.
		Optionally, the file can also be converted in a variety of image formats.
		If the writeDepth parameter is True then any depth information stored in MImage will be written to file."""
class MInt64Array(collections.abc.Sequence[int]):
	"""Array of MInt64 values."""
	@property
	def sizeIncrement(self)->Any:
		"""Number of elements by which to grow the array when necessary."""
	@sizeIncrement.setter
	def sizeIncrement(self,value:Any)->None:...
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def __len__(self)->int:
		"""Return len(self)."""
	def __getitem__(self,index:int)->int:
		"""Return self[key]."""
	def __setitem__(self,index:int,value:int)->None:
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
class MIntArray(collections.abc.Sequence[int]):
	"""Array of int values."""
	@property
	def sizeIncrement(self)->Any:
		"""Number of elements by which to grow the array when necessary."""
	@sizeIncrement.setter
	def sizeIncrement(self,value:Any)->None:...
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def __len__(self)->int:
		"""Return len(self)."""
	def __getitem__(self,index:int)->int:
		"""Return self[key]."""
	def __setitem__(self,index:int,value:int)->None:
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
class MItCurveCV:
	"""An iterator for traversing a curve's CVs."""
	def __iter__(self)->Any:
		"""Implement iter(self)."""
	def __next__(self)->Any:
		"""Implement next(self)."""
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def isDone(self)->bool:
		"""isDone() -> bool

		Indicates if all of the edges have been traversed yet."""
	def next(self)->Self:
		"""next() -> self

		Advances to the next edge in the iteration."""
	@overload
	def reset(self)->Self:
		"""reset() -> self
		reset(curve) -> self
		reset(curve, component=None) -> self

		Reset the iterator to the first CV of the curve.

		Reset the iterator to the first CV of the specified curve

		* curve (MObject) - The curve for the iteration

		Reset the iterator with the given curve and component.
		If component is None then the iteration will be for all CVs in the curve.

		* curve (MDagPath) - The curve to iterate over
		* component (MObject) - The CVs of the curve to iterate over"""
	@overload
	def reset(self,curve:MObject)->Self:
		"""reset() -> self
		reset(curve) -> self
		reset(curve, component=None) -> self

		Reset the iterator to the first CV of the curve.

		Reset the iterator to the first CV of the specified curve

		* curve (MObject) - The curve for the iteration

		Reset the iterator with the given curve and component.
		If component is None then the iteration will be for all CVs in the curve.

		* curve (MDagPath) - The curve to iterate over
		* component (MObject) - The CVs of the curve to iterate over"""
	@overload
	def reset(self,curve:MObject,component:MObject|None=None)->Self:
		"""reset() -> self
		reset(curve) -> self
		reset(curve, component=None) -> self

		Reset the iterator to the first CV of the curve.

		Reset the iterator to the first CV of the specified curve

		* curve (MObject) - The curve for the iteration

		Reset the iterator with the given curve and component.
		If component is None then the iteration will be for all CVs in the curve.

		* curve (MDagPath) - The curve to iterate over
		* component (MObject) - The CVs of the curve to iterate over"""
	def position(self)->MPoint:
		"""position() -> MPoint

		Returns the position of the current CV."""
	def setPosition(self,point:MPoint,space:int=MSpace.kObject)->Self:
		"""setPosition(point, space=kObject) -> self

		Sets the position of the current CV, in the given transformation

		space.

		* point       (MPoint) - The new position for the specified vertex
		* space (MSpace constant) - The transformation space"""
	def translateBy(self,vector:MVector,space:int=MSpace.kObject)->Self:
		"""translateBy(vector, space=kObject) -> self

		Translate the current CV by the amount specified
		by the given vector.

		* vector (MVector) - The amount of translation
		* space (int) - The Transformation space"""
	def index(self)->int:
		"""index() -> int

		Returns the index of the current edge in the iteration."""
	def currentItem(self)->MObject:
		"""currentItem() -> MObject

		Returns the current CV in the iteration as an MObject."""
	def hasHistoryOnCreate(self)->bool:
		"""hasHistoryOnCreate() -> bool

		This method determines if the shape was created with history.

		If the object that this iterator is attached to is not a shape then this method will fail."""
	def updateCurve(self)->Self:
		"""updateCurve() -> self

		This method is used to signal the curve that it has been changed and needs to redraw itself.

		When modifying a large number of CVs, it is most efficient to call this method after all of the CVs have been modified."""
class MItDag:
	"""DAG Iterator.

	Use the DAG iterator to traverse the DAG either depth first or breadth
	first, visiting each node and, if desired, retrieving the node (as an
	MObject).  The DAG iterator provides a basic filtering capability, so
	that DAG node retrieval can be limited to a  specific type (MFn.Type)
	of node.  With filtering enabled the iterator checks to see if the node
	is compatible with the type of Function Set specified by the filter.
	See MFn.Type for a list of all valid Function set types.

	Since each object, if retrieved, is returned as an MObject, the
	MObject.hasFn() method can be used to further check for compatible
	function set types since an MObjects may be compatible with more than
	one function set).

	Any compatible Function Set can be attached to the retrieved object to
	query or or edit it.  Often you will want to use the DAG node Function
	Set (MFnDagNode), which is compatible with all DAG objects, to perform
	basic queries on each node as the iterator traverses the DAG.

	The iterator also provides the capability to reset the root of the
	iteration, the type of traversal, and the filter.

	Additionally, the iterator can be queried for the root, mode and type
	of traversal, and to determine if the the traversal has been completed."""
	@property
	def traverseUnderWorld(self)->Any:
		"""Specifies whether underworld traversal is turned on (Bool)."""
	@traverseUnderWorld.setter
	def traverseUnderWorld(self,value:Any)->None:...
	kInvalidType:int=0
	kDepthFirst:int=1
	kBreadthFirst:int=2
	def __iter__(self)->Any:
		"""Implement iter(self)."""
	def __next__(self)->Any:
		"""Implement next(self)."""
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def iternext(self)->Self:
		"""iternext() -> self

		Used in pythonic iteration to move the iterator"""
	def iter(self)->Self:
		"""iter() -> self

		Initializes the iterator object for pythonic iteration."""
	def currentItem(self)->MObject:
		"""currentItem() -> MObject

		Retrieves DAG node to which the iterator points."""
	def depth(self)->int:
		"""depth() -> integer

		Returns the height or depth of the current node in the DAG relative to the
		root node.  The root node has a depth of zero."""
	def fullPathName(self)->str:
		"""fullPathName() -> MString

		Return a string representing the full path from the root of the dag to this object."""
	def getAllPaths(self)->MDagPathArray:
		"""getAllPaths() -> MDagPathArray

		Determines all DAG Paths to current item in the iteration."""
	def getPath(self)->MDagPath:
		"""getPath() -> MDagPath

		Determines a DAG Path to the current item in the iteration."""
	def instanceCount(self,total:Any)->int:
		"""instanceCount(total) -> Integer

		Determines the number of times the current item (DAG node) in the iteration
		is instanced.

		If total is False the number of direct instances is returned, which
		is the same as the node's parent count.

		If total is True the total number of instances is returned, including
		indirect instances resulting from instancing higher up the DAG hierarchy
		(i.e. one or more of the node's ancestors also has multiple instances)."""
	def isDone(self)->bool:
		"""isDone() -> Bool

		Indicates end of iteration path."""
	def isInstanced(self,indirect:bool=True)->bool:
		"""isInstanced(indirect = True) -> Bool

		Determines whether the current item (DAG node) in the iteration is directly
		or indirectly instanced.

		If indirect instance flag is False, the result is True if and only if the
		Node itself is multiply instanced (node.parentCount > 1).

		If the indirect flag is True, the result is True if and only if the Node
		itself is multiply instanced (node.parentCount > 1) or if the Node is not
		multiply instanced, but it has a directly instanced parent
		(node.parentCount()=1 and parent.parentCount >1).

		* indirect (Bool) -Indirect instance flag, defaults to True."""
	def next(self)->Self:
		"""next() -> self

		Moves to the next node matching the filter in the graph."""
	def partialPathName(self)->str:
		"""partialPathName() -> MString

		Return a string representing the partial path from the root of the
		dag to this object.

		The partial path is the minimum path that is still unique. This string
		may contain wildcards."""
	def prune(self)->Self:
		"""prune() -> self

		Prunes iteration tree at current node."""
	@overload
	def reset(self)->Self:
		"""reset() -> self
		reset(rootObject, traversalType = MItDag.kDepthFirst, filterType = MFn.kInvalid) -> self
		reset(rootPath, traversalType = MItDag.kDepthFirst, filterType = MFn.kInvalid) -> self
		reset(dagInfoObject, rootObject OR rootPath, traversalType = MItDag.kDepthFirst) -> self


		Resets the iterator.
		When used without parameters, the iterator is reset to the previous traversal setting.
		If a dagInfoObject is used, then the type of the provided rootObject or rootPath must
		match dagInfoObject.objectType.

		   rootObject (MObject) - Root node to begin the next traversal.
		   rootPath (MDagPath) - Root path to to begin the next traversal. Useful with instances.
		   dagInfoObject (MIteratorType) - Iterator object having info on filter or filterlist.
		   traversalType (MItDag.TraversalType) - Enumerated type that determines the direction of the traversal, defaults to kDepthFirst.
		   filterType (MFn.Type) - Function set type, defaults to MFn.kInvalid"""
	@overload
	def reset(self,rootObject:Any,traversalType:Any=MItDag.kDepthFirst,filterType:Any=MFn.kInvalid)->Self:
		"""reset() -> self
		reset(rootObject, traversalType = MItDag.kDepthFirst, filterType = MFn.kInvalid) -> self
		reset(rootPath, traversalType = MItDag.kDepthFirst, filterType = MFn.kInvalid) -> self
		reset(dagInfoObject, rootObject OR rootPath, traversalType = MItDag.kDepthFirst) -> self


		Resets the iterator.
		When used without parameters, the iterator is reset to the previous traversal setting.
		If a dagInfoObject is used, then the type of the provided rootObject or rootPath must
		match dagInfoObject.objectType.

		   rootObject (MObject) - Root node to begin the next traversal.
		   rootPath (MDagPath) - Root path to to begin the next traversal. Useful with instances.
		   dagInfoObject (MIteratorType) - Iterator object having info on filter or filterlist.
		   traversalType (MItDag.TraversalType) - Enumerated type that determines the direction of the traversal, defaults to kDepthFirst.
		   filterType (MFn.Type) - Function set type, defaults to MFn.kInvalid"""
	@overload
	def reset(self,rootPath:Any,traversalType:Any=MItDag.kDepthFirst,filterType:Any=MFn.kInvalid)->Self:
		"""reset() -> self
		reset(rootObject, traversalType = MItDag.kDepthFirst, filterType = MFn.kInvalid) -> self
		reset(rootPath, traversalType = MItDag.kDepthFirst, filterType = MFn.kInvalid) -> self
		reset(dagInfoObject, rootObject OR rootPath, traversalType = MItDag.kDepthFirst) -> self


		Resets the iterator.
		When used without parameters, the iterator is reset to the previous traversal setting.
		If a dagInfoObject is used, then the type of the provided rootObject or rootPath must
		match dagInfoObject.objectType.

		   rootObject (MObject) - Root node to begin the next traversal.
		   rootPath (MDagPath) - Root path to to begin the next traversal. Useful with instances.
		   dagInfoObject (MIteratorType) - Iterator object having info on filter or filterlist.
		   traversalType (MItDag.TraversalType) - Enumerated type that determines the direction of the traversal, defaults to kDepthFirst.
		   filterType (MFn.Type) - Function set type, defaults to MFn.kInvalid"""
	@overload
	def reset(self,dagInfoObject:Any,rootObject:Any,traversalType:Any=MItDag.kDepthFirst)->Self:
		"""reset() -> self
		reset(rootObject, traversalType = MItDag.kDepthFirst, filterType = MFn.kInvalid) -> self
		reset(rootPath, traversalType = MItDag.kDepthFirst, filterType = MFn.kInvalid) -> self
		reset(dagInfoObject, rootObject OR rootPath, traversalType = MItDag.kDepthFirst) -> self


		Resets the iterator.
		When used without parameters, the iterator is reset to the previous traversal setting.
		If a dagInfoObject is used, then the type of the provided rootObject or rootPath must
		match dagInfoObject.objectType.

		   rootObject (MObject) - Root node to begin the next traversal.
		   rootPath (MDagPath) - Root path to to begin the next traversal. Useful with instances.
		   dagInfoObject (MIteratorType) - Iterator object having info on filter or filterlist.
		   traversalType (MItDag.TraversalType) - Enumerated type that determines the direction of the traversal, defaults to kDepthFirst.
		   filterType (MFn.Type) - Function set type, defaults to MFn.kInvalid"""
	def root(self)->MObject:
		"""root() -> MObject

		Returns the root (start node) of the current traversal.
		The constructor sets the root of traversal to the world node.
		The root can be changed by the reset() method."""
	def traversalType(self)->int:
		"""traversalType() -> MItDag.TraversalType

		Returns the direction of the traversal."""
class MItDependencyGraph:
	"""Dependency Graph Iterator.

	Iterate over Dependency Graph (DG) Nodes or Plugs starting at a specified
	root Node or Plug.


	Set and query the root of the iteration.


	Set and query the direction (downstream or upstream), traversal priority
	(depth first or breadth first), level of detail (Node level or Plug
	level) and relationship (dependency, DG connection, eval graph) of the iteration.


	Set and disable a filter to iterate over only specific types (MFn.Type) of
	Nodes.


	Reset the root, filter, direction, traversal priority and level of detail
	of the iteration.


	Prune branches of the graph from iteration.


	In Maya, all geometry, animation and rendering information is implemented
	in nodes in the Dependency Graph (DG).  The DG includes the Directed Acyclic
	Graph (DAG).  Therefore, all DAG nodes are also DG nodes.  The data on nodes
	is associated with Attributes.  Attributes on nodes are connected to
	Attributes on other nodes via plugs on the Attributes.  Plugs are, in effect
	the external intefaces of Attributes.


	The DG Iterator Class (MItDependencyGraph) provides methods for iterating
	over either nodes or plugs, as well as methods for setting and querying the
	characteristics and behaviour of the iterator.


	This iterator will traverse all connected attributes upstream or
	downstream from the root node of the traversal. For non root nodes,
	only attributes that are affected by the incoming attribute to that
	node will be traversed.  Hence, only nodes to which data from the root
	node is flowing will be traversed.


	By default, the iterator does not traverse world-space attribute
	dependencies (an example of a world-space dependency is that
	translateX affects worldMatrix). The
	setTraversalOverWorldSpaceDependents method can be used to enable such
	traversal. Note that even when world-space traversal is enabled, the
	iterator will only iterate to connected nodes. It does not iterate up
	and down through the dag hierarchy.


	The DG Iterator is used in conjunction with the Maya Object (MObject), plug
	(MPlug), Maya Object Array (MObjectArray) and plug Array (MPlugArray)
	classes.


	It is also useful to use Function Sets specific to the nodes returned by
	the iterator to query and modify the nodes in the DG.


	The DG itself can be modified using a DG Modifer (MDGModifier).


	Additionally, nodes can be added to and retrieved from selection lists using
	the Selection List (MSelectionList) class and Selection List Iterator
	(MItSelectionList).  This can be useful for obtaining the root node for an
	iteration.


	Attributes on the nodes can be manipulated using the Attribute Function Set
	(MFnAttribute) and its derivations."""
	@property
	def currentFilter(self)->Any:
		"""Current node type filter (MFn.Type) ."""
	@currentFilter.setter
	def currentFilter(self,value:Any)->None:...
	@property
	def pruningOnFilter(self)->Any:
		"""Whether or not the iteration path is pruned automatically at nodes or plugs which do not match the filter (Bool)."""
	@pruningOnFilter.setter
	def pruningOnFilter(self,value:Any)->None:...
	@property
	def currentDirection(self)->Any:
		"""Direction of the iteration through the graph (MItDependencyGraph.Direction)."""
	@currentDirection.setter
	def currentDirection(self,value:Any)->None:...
	@property
	def currentTraversal(self)->Any:
		"""Traversal mode of the iteration through the graph (MItDependencyGraph.Traversal)."""
	@currentTraversal.setter
	def currentTraversal(self,value:Any)->None:...
	@property
	def currentLevel(self)->Any:
		"""Level of the iteration through the graph (MItDependencyGraph.Level)."""
	@currentLevel.setter
	def currentLevel(self,value:Any)->None:...
	@property
	def currentRelationship(self)->Any:
		"""Relationship mode of the iteration through the graph (MItDependencyGraph.Relationship)."""
	@currentRelationship.setter
	def currentRelationship(self,value:Any)->None:...
	@property
	def traversingOverWorldSpaceDependents(self)->Any:
		"""Whether the iterator is set to traverse world-space attribute dependencies (Bool)."""
	@traversingOverWorldSpaceDependents.setter
	def traversingOverWorldSpaceDependents(self,value:Any)->None:...
	@property
	def nodeDepth(self)->Any:
		"""Depth of the iteration through the graph (int)."""
	@nodeDepth.setter
	def nodeDepth(self,value:Any)->None:...
	kDownstream:int=0
	kUpstream:int=1
	kDepthFirst:int=0
	kBreadthFirst:int=1
	kNodeLevel:int=0
	kPlugLevel:int=1
	kDependsOn:int=0
	kConnectedTo:int=1
	kEvaluationGraph:int=2
	def __iter__(self)->Any:
		"""Implement iter(self)."""
	def __next__(self)->Any:
		"""Implement next(self)."""
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def iternext(self)->Self:
		"""iternext() -> self

		Used in pythonic iteration to move the iterator"""
	def iter(self)->Self:
		"""iter() -> self

		Initializes the iterator object for pythonic iteration."""
	def currentNode(self)->MObject:
		"""currentNode() -> MObject

		Retrieves the current node of the iteration.  Results in a null object on
		failure or if the node is of a unrecognized type."""
	def currentNodeHasUnknownType(self)->bool:
		"""currentNodeHasUnknownType() -> Bool

		Indicates whether or not the current node has an unrecognised
		type.  This is useful if an unexpected failure is encountered
		in the next() or currentNode() methods."""
	def currentPlug(self)->MPlug:
		"""currentPlug() -> MPlug

		Retrieves the current plug of the iteration.  Results in a null
		plug on failure."""
	def getNodePath(self)->MObjectArray:
		"""getNodePath() -> MObjectArray

		Retrieves the direct path from the current node to the root
		node.  Path does not include the current node.
		State of the provided array is undefined if this method fails."""
	def getNodesVisited(self)->MObjectArray:
		"""getNodesVisited() -> MObjectArray

		Retrieves all nodes visited during the iteration.
		State of the provided array is undefined if this method fails."""
	def getPlugPath(self)->MPlugArray:
		"""getPlugPath() -> MPlugArray

		Retrieves the direct path from the current plug to the root
		plug, with the current plug in element 0 of the array and the root
		plug in the final element of the array.

		Once the iterator is done (i.e. isDone() returns True) there is no
		longer a current plug and this method will return an empty array.

		If this method fails the state of the returned array is undefined."""
	def getPlugsVisited(self)->MPlugArray:
		"""getPlugsVisited() -> MPlugArray

		Retrieves all plugs visited during the iteration.
		State of the provided array is undefined if this method fails."""
	def isDone(self)->bool:
		"""isDone() -> Bool

		Indicates whether or not all nodes or plugs have been iterated over
		in accordance with the direction, traversal, level, relationship and filter.
		If a valid filter is set, the iterator only visits those nodes that match
		the filter."""
	def next(self)->Self:
		"""next() -> self

		Iterates to the next node or plug in accordance with the
		direction, traversal, level, relationship and filter.  If a valid filter is
		set, the iterator only visits those nodes that match the
		filter.  When filtering is enabled nodes that have unknown type
		are treated as non-matching nodes.  With filtering disabled,
		iteration to a node with an unknown type is treated as a
		failure.  An attempt to iterate when there is nothing left to
		iterate over has no effect."""
	def previousPlug(self)->MPlug:
		"""previousPlug() -> MPlug

		Retrieves the previous plug of the iteration.  Results in a
		null plug on failure.  Null plug may also indicate that the
		current plug is the root plug."""
	def prune(self)->Self:
		"""prune() -> self

		Prunes the search path at the current plug.  Iterator will not
		visit any of the plugs connected to the pruned plug."""
	def reset(self)->Self:
		"""reset() -> self

		Clears iterator data and resets the iterator to the root node
		or plug.  If a valid filter is enabled, the iterator
		automatically advances to the next node after the root node
		that matches the filter.  If no matching node is found an
		exception is thrown."""
	def resetFilter(self)->Self:
		"""resetFilter() -> self

		Resets the node or plug filter to default, MFn.kInvalid
		(filter disabled).  Disables pruning on the filter (default).
		Resets the iterator."""
	@overload
	def resetTo(self,rootObject:Any,filter:Any=MFn.kInvalid,direction:Any=MItDependencyGraph.kDownstream,traversal:Any=MItDependencyGraph.kDepthFirst,level:Any=MItDependencyGraph.kNodeLevel,relationship:Any=MItDependencyGraph.kDependsOn)->Self:
		"""resetTo(rootObject, filter = MFn.kInvalid, direction = MItDependencyGraph.kDownstream, traversal = MItDependencyGraph.kDepthFirst, level = MItDependencyGraph.kNodeLevel, relationship = MItDependencyGraph.kDependsOn) -> self
		resetTo(rootPlug, filter = MFn.kInvalid, direction = MItDependencyGraph.kDownstream, traversal = MItDependencyGraph.kDepthFirst, level = MItDependencyGraph.kNodeLevel, relationship = MItDependencyGraph.kDependsOn) -> self
		resetTo(infoObject, rootObject OR rootPlug, direction = MItDependencyGraph.kDownstream, traversal = MItDependencyGraph.kDepthFirst, level = MItDependencyGraph.kNodeLevel, relationship = MItDependencyGraph.kDependsOn) -> self


		Clears iterator data and re-initializes the iterator.  If a
		valid filter is provided, the iterator automatically advances
		to the next node after the root node that matches the filter.
		If no matching node is found an exception is thrown.


		   rootObject (MObject) - Root node to begin the next traversal.
		   rootPlug (MPlug) - Root plug to to begin the next traversal.
		   infoObject (MIteratorType) - Iterator object having info on filter or filterlist.
		   filter (MFn.Type) - Function set type, defaults to MFn.kInvalid
		   direction (MItDependencyGraph.Direction) - Primary direction of iteration, defaults to MItDependencyGraph.kDownstream
		   traversal (MItDependencyGraph.Traversal) - Order of traversal, defaults to MItDependencyGraph.kDepthFirst
		   level (MItDependencyGraph.Level) - Level of detail of the iteration, defaults to MItDependencyGraph.kNodeLevel
		   relationship (MItDependencyGraph.Relationship) - Relationship mode of the iteration, defaults to MItDependencyGraph.kDependsOn"""
	@overload
	def resetTo(self,rootPlug:Any,filter:Any=MFn.kInvalid,direction:Any=MItDependencyGraph.kDownstream,traversal:Any=MItDependencyGraph.kDepthFirst,level:Any=MItDependencyGraph.kNodeLevel,relationship:Any=MItDependencyGraph.kDependsOn)->Self:
		"""resetTo(rootObject, filter = MFn.kInvalid, direction = MItDependencyGraph.kDownstream, traversal = MItDependencyGraph.kDepthFirst, level = MItDependencyGraph.kNodeLevel, relationship = MItDependencyGraph.kDependsOn) -> self
		resetTo(rootPlug, filter = MFn.kInvalid, direction = MItDependencyGraph.kDownstream, traversal = MItDependencyGraph.kDepthFirst, level = MItDependencyGraph.kNodeLevel, relationship = MItDependencyGraph.kDependsOn) -> self
		resetTo(infoObject, rootObject OR rootPlug, direction = MItDependencyGraph.kDownstream, traversal = MItDependencyGraph.kDepthFirst, level = MItDependencyGraph.kNodeLevel, relationship = MItDependencyGraph.kDependsOn) -> self


		Clears iterator data and re-initializes the iterator.  If a
		valid filter is provided, the iterator automatically advances
		to the next node after the root node that matches the filter.
		If no matching node is found an exception is thrown.


		   rootObject (MObject) - Root node to begin the next traversal.
		   rootPlug (MPlug) - Root plug to to begin the next traversal.
		   infoObject (MIteratorType) - Iterator object having info on filter or filterlist.
		   filter (MFn.Type) - Function set type, defaults to MFn.kInvalid
		   direction (MItDependencyGraph.Direction) - Primary direction of iteration, defaults to MItDependencyGraph.kDownstream
		   traversal (MItDependencyGraph.Traversal) - Order of traversal, defaults to MItDependencyGraph.kDepthFirst
		   level (MItDependencyGraph.Level) - Level of detail of the iteration, defaults to MItDependencyGraph.kNodeLevel
		   relationship (MItDependencyGraph.Relationship) - Relationship mode of the iteration, defaults to MItDependencyGraph.kDependsOn"""
	@overload
	def resetTo(self,infoObject:Any,rootObject:Any,direction:Any=MItDependencyGraph.kDownstream,traversal:Any=MItDependencyGraph.kDepthFirst,level:Any=MItDependencyGraph.kNodeLevel,relationship:Any=MItDependencyGraph.kDependsOn)->Self:
		"""resetTo(rootObject, filter = MFn.kInvalid, direction = MItDependencyGraph.kDownstream, traversal = MItDependencyGraph.kDepthFirst, level = MItDependencyGraph.kNodeLevel, relationship = MItDependencyGraph.kDependsOn) -> self
		resetTo(rootPlug, filter = MFn.kInvalid, direction = MItDependencyGraph.kDownstream, traversal = MItDependencyGraph.kDepthFirst, level = MItDependencyGraph.kNodeLevel, relationship = MItDependencyGraph.kDependsOn) -> self
		resetTo(infoObject, rootObject OR rootPlug, direction = MItDependencyGraph.kDownstream, traversal = MItDependencyGraph.kDepthFirst, level = MItDependencyGraph.kNodeLevel, relationship = MItDependencyGraph.kDependsOn) -> self


		Clears iterator data and re-initializes the iterator.  If a
		valid filter is provided, the iterator automatically advances
		to the next node after the root node that matches the filter.
		If no matching node is found an exception is thrown.


		   rootObject (MObject) - Root node to begin the next traversal.
		   rootPlug (MPlug) - Root plug to to begin the next traversal.
		   infoObject (MIteratorType) - Iterator object having info on filter or filterlist.
		   filter (MFn.Type) - Function set type, defaults to MFn.kInvalid
		   direction (MItDependencyGraph.Direction) - Primary direction of iteration, defaults to MItDependencyGraph.kDownstream
		   traversal (MItDependencyGraph.Traversal) - Order of traversal, defaults to MItDependencyGraph.kDepthFirst
		   level (MItDependencyGraph.Level) - Level of detail of the iteration, defaults to MItDependencyGraph.kNodeLevel
		   relationship (MItDependencyGraph.Relationship) - Relationship mode of the iteration, defaults to MItDependencyGraph.kDependsOn"""
	def rootNode(self)->MObject:
		"""rootNode() -> MObject

		Retrieves the root node of the iteration."""
	def rootPlug(self)->MPlug:
		"""rootPlug() -> MPlug

		Retrieves the root plug of the iteration."""
class MItDependencyNodes:
	"""Dependency Node iterator.

	Use the dependency node iterator to traverse all the nodes in Maya's
	Dependency Graph.

	With filtering enabled, the iterator checks to see if the node is
	compatible with the type specified by the filter.  See MFn.Type for a
	list of all valid types.

	Since MObjects may be compatible with more than one type (nodes are
	organised in a hierarchy) the MObject.hasFn() method can be used to
	further check for compatible types.

	Any compatible Function Set can be attached to the retrieved object to
	query or or edit it.  Often you will want to use the dependency node
	function set (MFnDependencyNode), which is compatible with all
	dependency nodes, to perform queries on each node as the iterator
	traverses the Dependency Graph."""
	def __iter__(self)->Any:
		"""Implement iter(self)."""
	def __next__(self)->Any:
		"""Implement next(self)."""
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def iternext(self)->Self:
		"""iternext() -> self

		Used in pythonic iteration to move the iterator"""
	def iter(self)->Self:
		"""iter() -> self

		Initializes the iterator object for pythonic iteration."""
	def thisNode(self)->MObject:
		"""thisNode() -> MObject

		Retrieves the dependency node to which the iterator points."""
	def isDone(self)->bool:
		"""isDone() -> Bool

		Indicates end of the iteration."""
	def next(self)->Self:
		"""next() -> self

		Moves to the next node matching the filter.  If the filter
		is set to kInvalid, this method advances to the next
		DG node without doing any filtering."""
	@overload
	def reset(self)->Self:
		"""reset() -> self
		reset(filterType = MFn.kInvalid) -> self
		reset(dagInfoObject) -> self


		Resets the iterator.


		   dagInfoObject (MIteratorType) - Iterator object having info on filter or filterlist.
		   filterType (MFn.Type) - Function set type, defaults to MFn.kInvalid."""
	@overload
	def reset(self,filterType:Any=MFn.kInvalid)->Self:
		"""reset() -> self
		reset(filterType = MFn.kInvalid) -> self
		reset(dagInfoObject) -> self


		Resets the iterator.


		   dagInfoObject (MIteratorType) - Iterator object having info on filter or filterlist.
		   filterType (MFn.Type) - Function set type, defaults to MFn.kInvalid."""
	@overload
	def reset(self,dagInfoObject:Any)->Self:
		"""reset() -> self
		reset(filterType = MFn.kInvalid) -> self
		reset(dagInfoObject) -> self


		Resets the iterator.


		   dagInfoObject (MIteratorType) - Iterator object having info on filter or filterlist.
		   filterType (MFn.Type) - Function set type, defaults to MFn.kInvalid."""
class MItGeometry:
	"""Geometry iterator.

	This class is the iterator class for geometry data, and can be used to
	loop over the CVs of NURBS, the points of subds & lattices, and the
	vertices of polygonal meshes."""
	def __iter__(self)->Any:
		"""Implement iter(self)."""
	def __next__(self)->Any:
		"""Implement next(self)."""
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def iternext(self)->Self:
		"""iternext() -> self

		Used in pythonic iteration to move the iterator"""
	def iter(self)->Self:
		"""iter() -> self

		Initializes the iterator object for pythonic iteration."""
	def isDone(self)->bool:
		"""isDone() -> Bool

		Indicates end of the iteration."""
	def next(self)->Self:
		"""next() -> self

		Advance to the next component in the iteration.
		If the iterator is already at the last component then this
		method has no effect. Use isDone to determine if the iterator
		is at the last component."""
	def position(self)->MPoint:
		"""position() -> MPoint

		Return the position of the current point/CV/vertex component."""
	def normal(self)->MVector:
		"""normal() -> MVector

		Return the normal of the current point/CV/vertex component."""
	def setPosition(self)->Any:
		"""setPosition() -> MStatus

		Set the position of the current point/CV/vertex."""
	def weight(self)->MWeight:
		"""weight() -> MWeight

		Return the weight of the current point/CV/vertex component."""
	def index(self)->int:
		"""index() -> int


		This method returns the index of the current point/CV/vertex
		component in the iteration."""
	def component(self)->MObject:
		"""component() -> MObject

		    DEPRECATED in 2019, use currentItem instead.
		This method returns the current component in the iteration."""
	def currentItem(self)->MObject:
		"""currentItem() -> MObject

		This method returns the current component in the iteration."""
	def count(self)->int:
		"""count() -> int


		Return the number of items in this iteration. This number will
		always be at least as large as the number of items, however in
		some cases it may be larger. It is useful if allocating space in
		an array to hold the results, since it will always be of
		sufficient size. If the exact number of items is required, use the
		exactCount method instead. The exactCount method is however
		significantly slower than this method."""
	def exactCount(self)->int:
		"""exactCount() -> int


		Return the exact number of items in this iteration. This method is
		significantly slower than the count() method, so use if only if
		the precise number is required."""
	def reset(self)->Self:
		"""reset() -> self


		Resets the iterator."""
	def allPositions(self)->Any:
		"""allPositions() -> MStatus

		Return the position of all the points/CVs/vertices.  This
		operation is faster than using the iterator to get values one by
		one, but uses more memory as it requires an array to hold all the
		values to be returned."""
	def setAllPositions(self)->Any:
		"""setAllPositions() -> MStatus

		Set the position of all the points/CVs/vertices at once. This
		operation is faster than using the iterator to set values one by
		one, but uses more memory as it requires an array to hold all the
		values to be set."""
class MItMeshEdge:
	"""An iterator for traversing a mesh's edges."""
	@property
	def isSmooth(self)->Any:
		"""True if the edge is smooth, False if it is hard."""
	@isSmooth.setter
	def isSmooth(self,value:Any)->None:...
	def __iter__(self)->Any:
		"""Implement iter(self)."""
	def __next__(self)->Any:
		"""Implement next(self)."""
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def iternext(self)->Self:
		"""iternext() -> self

		Used in pythonic iteration to move the iterator"""
	def iter(self)->Self:
		"""iter() -> self

		Initializes the iterator object for pythonic iteration."""
	def center(self,space:int=MSpace.kObject)->MPoint:
		"""center(space=kObject) -> MPoint

		Returns the center point of the edge, in the given transformation space.

		* space (MSpace constant) - The  transformation space"""
	def connectedToEdge(self,index:int)->bool:
		"""connectedToEdge(index) -> bool

		Determines whether the given edge is connected to the current edge.

		* index (int) - Index of edge to check."""
	def connectedToFace(self,index:int)->bool:
		"""connectedToFace(index) -> bool

		Determines whether the given face contains the current edge.

		* index (int) - Index of face to check."""
	def count(self)->int:
		"""count() -> int

		Return the number of edges in the iteration"""
	def currentItem(self)->MObject:
		"""currentItem() -> MObject

		Returns the current edge in the iteration as a component.

		Components are used to specify one or more edges and are useful in operating on groups of non-contiguous edges for a surface.
		Components do not contain any information about the surface that they refer to so an MDagPath must be specified when dealing with components."""
	def geomChanged(self)->Self:
		"""geomChanged() -> self

		Resets the geom pointer in the MItMeshEdge. If you're using MFnMesh to
		update Normals or Color per vertex while iterating, you must call geomChanged
		on the iterator immediately after the MFnMesh call to make sure that your
		geometry is up to date. A crash may result if this method is not called.
		A similar approach must be taken for updating upstream vertex tweaks
		with an MPlug. After the update, call this method."""
	def getConnectedEdges(self)->MIntArray:
		"""getConnectedEdges() -> MIntArray

		Returns the indices of edges connected to the current edge."""
	def getConnectedFaces(self)->MIntArray:
		"""getConnectedFaces() -> MIntArray

		Returns the indices of the faces connected to the current edge.
		Normally a boundary edge will only have one face connected to it and
		an internal edge will have two, but if the mesh has manifold geometry
		then the edge may have three or more faces connected to it."""
	def index(self)->int:
		"""index() -> int

		Returns the index of the current edge in the iteration."""
	def isDone(self)->bool:
		"""isDone() -> bool

		Indicates if all of the edges have been traversed yet."""
	def length(self,space:int=MSpace.kObject)->float:
		"""length(space=kObject) -> float

		Returns the length of the edge, in the given transformation space.

		* space (MSpace constant) - The  transformation space"""
	def next(self)->Self:
		"""next() -> self

		Advances to the next edge in the iteration."""
	def numConnectedEdges(self)->int:
		"""numConnectedEdges() -> int

		Returns the number of edges connected to the current edge."""
	def numConnectedFaces(self)->int:
		"""numConnectedFaces() -> int

		Returns the number of faces connected to the current edge."""
	def onBoundary(self)->bool:
		"""onBoundary() -> bool

		Determines if the current edge is a border edge."""
	def point(self,whichVertex:Literal[0]|Literal[1],space:int=MSpace.kObject)->MPoint:
		"""point(whichVertex, space=kObject) -> MPoint

		Returns the position of one of the current edge's vertices, int the
		given transformation space.

		* whichVertex    (0 or 1) - Which of the edge's two vertices to return
		* space (MSpace constant) - The transformation space"""
	@overload
	def reset(self)->Self:
		"""reset() -> self
		reset(mesh) -> self
		reset(mesh, component=None) -> self

		Reset the iterator to the first edge of the mesh.

		Reset the iterator to the first edge of the specified mesh

		* mesh (MObject) - The polygon for the iteration

		Reset the iterator with the given mesh and component.
		If component is None then the iteration will be for all edges in the mesh.

		* mesh (MDagPath) - The mesh to iterate over
		* component (MObject) - The edges of the mesh to iterate over"""
	@overload
	def reset(self,mesh:MObject)->Self:
		"""reset() -> self
		reset(mesh) -> self
		reset(mesh, component=None) -> self

		Reset the iterator to the first edge of the mesh.

		Reset the iterator to the first edge of the specified mesh

		* mesh (MObject) - The polygon for the iteration

		Reset the iterator with the given mesh and component.
		If component is None then the iteration will be for all edges in the mesh.

		* mesh (MDagPath) - The mesh to iterate over
		* component (MObject) - The edges of the mesh to iterate over"""
	@overload
	def reset(self,mesh:MObject,component:MObject|None=None)->Self:
		"""reset() -> self
		reset(mesh) -> self
		reset(mesh, component=None) -> self

		Reset the iterator to the first edge of the mesh.

		Reset the iterator to the first edge of the specified mesh

		* mesh (MObject) - The polygon for the iteration

		Reset the iterator with the given mesh and component.
		If component is None then the iteration will be for all edges in the mesh.

		* mesh (MDagPath) - The mesh to iterate over
		* component (MObject) - The edges of the mesh to iterate over"""
	def setIndex(self,index:int)->int:
		"""setIndex(index) -> int

		Sets the index of the current edge to be accessed. The current edge
		will no longer be in sync with any previous iteration.

		Returns the index of the edge which was current before the change.


		* index (int) - The index of desired edge to access. """
	def setPoint(self,point:MPoint,whichVertex:Literal[0]|Literal[1],space:int=MSpace.kObject)->Self:
		"""setPoint(point, whichVertex, space=kObject) -> self

		Sets the position of one of the current edge's vertices, in the given
		transformation space.

		* point       (MPoint) - The new position for the specified vertex
		* whichVertex (0 or 1) - Which of the edge's 2 vertices to set.
		* space (MSpace constant) - The transformation space"""
	def updateSurface(self)->Self:
		"""updateSurface() -> self

		Tells Maya that mesh has been changed and needs to redraw itself."""
	def vertexId(self,whichVertex:Literal[0]|Literal[1])->int:
		"""vertexId(whichVertex) -> int

		Returns the global index (as opposed to face-relative index) of one of
		the edge's vertices.

		* whichVertex (0 or 1) - Which of the edge's 2 vertices to use."""
class MItMeshFaceVertex:
	"""An iterator for traversing a mesh's face vertices."""
	def __iter__(self)->Any:
		"""Implement iter(self)."""
	def __next__(self)->Any:
		"""Implement next(self)."""
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def iternext(self)->Self:
		"""iternext() -> self

		Used in pythonic iteration to move the iterator"""
	def iter(self)->Self:
		"""iter() -> self

		Initializes the iterator object for pythonic iteration."""
	def currentItem(self)->MObject:
		"""currentItem() -> MObject

		Returns the current faceVertex as a double-indexed component."""
	def faceId(self)->int:
		"""faceId() -> int

		Returns the current face index."""
	def faceVertexId(self)->int:
		"""faceVertexId() -> int

		Returns the relative index of the vertex within the current face. This
		index together with the faceId can be used for a fast access to get
		various info stored per vertex (normals, uvs, colors)."""
	def geomChanged(self)->Self:
		"""geomChanged() -> self

		Resets the geom pointer in the MItMeshFaceVertex. If you're using
		MFnMesh to update Normals or Color per vertex while iterating, you
		must call geomChanged on the iterator immediately after the MFnMesh
		call to make sure that your geometry is up to date. A crash may result
		if this method is not called. A similar approach must be taken for
		updating upstream vertex tweaks with an MPlug. After the update, call
		this method."""
	def getBinormal(self,space:Any=MSpace.kObject,uvSet:Any='')->MVector:
		"""getBinormal(space=MSpace.kObject, uvSet='') -> MVector

		Returns the face vertex binormal associated with the UV set."""
	def getColor(self,colorSetName:str='')->MColor:
		"""getColor(colorSetName='') -> MColor

		Returns a color of the current face vertex."""
	def getColorIndex(self,colorSetName:str='')->int:
		"""getColorIndex(colorSetName='') -> int

		Return a color index of the current face vertex."""
	def getNormal(self,space:Any=MSpace.kObject)->MVector:
		"""getNormal(space=MSpace.kObject) -> MVector

		Returns the face vertex normal."""
	def getTangent(self,space:Any=MSpace.kObject,uvSet:Any='')->MVector:
		"""getTangent(space=MSpace.kObject, uvSet='') -> MVector

		Returns the face vertex tangent associated with the given UV set. The
		tangent is defined as the surface tangent of the polygon running in
		the U direction."""
	def getUV(self,uvSet:Any='')->tuple[float,float]:
		"""getUV(uvSet='') -> (float, float)

		Returns the texture coordinate for the current face vertex."""
	def getUVIndex(self,uvSet:Any='')->int:
		"""getUVIndex(uvSet='') -> int

		Returns the index of the texture coordinate for the current face
		vertex. This index refers to an element of the mesh's texture
		coordinate array as returned by MFnMesh::getUVs()."""
	def hasColor(self)->bool:
		"""hasColor() -> bool

		Returns whether the current face vertex has a color-per-vertex set."""
	def hasUVs(self,uvSet:Any='')->bool:
		"""hasUVs(uvSet='') -> bool

		Returns whether the current face vertex has UVs mapped in the given
		set."""
	def isDone(self)->bool:
		"""isDone() -> bool

		Indicates if all of the face vertices have been traversed."""
	def next(self)->Self:
		"""next() -> self

		Advances to the next face vertex in the iteration."""
	def normalId(self)->int:
		"""normalId() -> int

		Returns the normal index for the specified vertex. This index refers
		to an element in the normal array returned by MFnMesh::getNormals().
		These normals are per-face per-vertex normals."""
	def position(self,space:Any=MSpace.kObject)->MPoint:
		"""position(space=MSpace.kObject) -> MPoint

		Returns the position of the current face vertex."""
	@overload
	def reset(self)->Self:
		"""reset() -> self
		reset(mesh) -> self
		reset(mesh, component=None) -> self

		Reset the iterator to the first face vertex of the mesh.

		Reset the iterator to the first face vertex of the specified mesh.

		* mesh (MObject) - The mesh for the iteration

		Reset the iterator with the given mesh and component.
		If component is None then the iteration will be for all face vertices in the mesh.

		* mesh (MDagPath) - The mesh to iterate over
		* component (MObject) - The faces of the mesh to iterate over"""
	@overload
	def reset(self,mesh:MObject)->Self:
		"""reset() -> self
		reset(mesh) -> self
		reset(mesh, component=None) -> self

		Reset the iterator to the first face vertex of the mesh.

		Reset the iterator to the first face vertex of the specified mesh.

		* mesh (MObject) - The mesh for the iteration

		Reset the iterator with the given mesh and component.
		If component is None then the iteration will be for all face vertices in the mesh.

		* mesh (MDagPath) - The mesh to iterate over
		* component (MObject) - The faces of the mesh to iterate over"""
	@overload
	def reset(self,mesh:MObject,component:MObject|None=None)->Self:
		"""reset() -> self
		reset(mesh) -> self
		reset(mesh, component=None) -> self

		Reset the iterator to the first face vertex of the mesh.

		Reset the iterator to the first face vertex of the specified mesh.

		* mesh (MObject) - The mesh for the iteration

		Reset the iterator with the given mesh and component.
		If component is None then the iteration will be for all face vertices in the mesh.

		* mesh (MDagPath) - The mesh to iterate over
		* component (MObject) - The faces of the mesh to iterate over"""
	def setIndex(self,faceId:int,faceVertexId:int)->tuple[oldFaceId,oldFaceVertexId]:
		"""setIndex(faceId, faceVertexId) -> (oldFaceId, oldFaceVertexId)

		Sets the index of the current face vertex to be accessed. The current
		face vertex will no longer be in sync with any previous iteration.

		Returns the indices of the old face and vertex.


		* faceId (int) - Index of desired face to access.
		* faceVertexId (int) - Face-relative index of desired vertex to access.
		* oldFaceId (int) - Index of the face which was current before the change.
		* oldFaceVertexId (int) - Face-relative index of the vertex which was current before the change."""
	def tangentId(self)->int:
		"""tangentId() -> int

		Returns the tangent index for the current face vertex. This index
		refers to an element in the array returned by MFnMesh::getTangents.
		These tangents are per-face per-vertex."""
	def updateSurface(self)->Self:
		"""updateSurface() -> self

		Tells Maya that mesh has been changed and needs to redraw itself."""
	def vertexId(self)->int:
		"""vertexId() -> int

		Returns the global (as opposed to face-relative) index of the
		current vertex."""
class MItMeshPolygon:
	"""This class is the iterator for polygonal surfaces (meshes)."""
	def __iter__(self)->Any:
		"""Implement iter(self)."""
	def __next__(self)->Any:
		"""Implement next(self)."""
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def iternext(self)->Self:
		"""iternext() -> self

		Used in pythonic iteration to move the iterator"""
	def iter(self)->Self:
		"""iter() -> self

		Initializes the iterator object for pythonic iteration."""
	def center(self,space:int=MSpace.kObject)->MPoint:
		"""center(space=kObject) -> MPoint

		Return the position of the center of the current polygon

		* space (int) - The coordinate system for this operation"""
	def count(self)->int:
		"""count() -> int

		Return the number of polygons in the iteration"""
	def currentItem(self)->MObject:
		"""currentItem() -> MObject

		Get the current polygon in the iteration as a component.

		Components are used to specify one or more polygons and are usefull in operating on groups of non-contiguous polygons for a surface.
		Components do not contain any information about the surface that they refer to so an MDagPath must be specified when dealing with components."""
	def geomChanged(self)->Self:
		"""geomChanged() -> self

		Reset the geom pointer in the MItMeshPolygon. This is now being handled automatically inside the iterator, and users should no longer need to call this method directly to sync up the iterator to changes made by MFnMesh"""
	def getArea(self,space:int=MSpace.kObject)->float:
		"""getArea(space=kObject) -> float

		This method gets the area of the face

		* space (int) - World Space or Object Space"""
	@overload
	def getColor(self,colorSetName:str|None=None)->MColor:
		"""getColor(colorSetName=None) -> MColor
		getColor(vertexIndex) -> MColor

		This method gets the color of the specified vertex in this face

		* index (int) - The face-relative vertex index on this face

		Or the average color of the all the vertices in this face

		* colorSetName (string) - Name of the color set."""
	@overload
	def getColor(self,vertexIndex:int)->MColor:
		"""getColor(colorSetName=None) -> MColor
		getColor(vertexIndex) -> MColor

		This method gets the color of the specified vertex in this face

		* index (int) - The face-relative vertex index on this face

		Or the average color of the all the vertices in this face

		* colorSetName (string) - Name of the color set."""
	def getColorIndex(self,vertexIndex:int,colorSetName:str|None=None)->int:
		"""getColorIndex(vertexIndex, colorSetName=None) -> int

		This method returns the colorIndex for a vertex of the current face.

		* vertexIndex (int) - Face-relative index of vertex.
		* colorSetName (string) - Name of the color set."""
	def getColorIndices(self,colorSetName:str|None=None)->MIntArray:
		"""getColorIndices(colorSetName=None) -> MIntArray

		This method returns the colorIndices for each vertex on the face.

		* colorSetName (string) - Name of the color set."""
	def getColors(self,colorSetName:str|None=None)->MColorArray:
		"""getColors(colorSetName=None) -> MColorArray

		This method gets the color of the each vertex in the current face.

		* colorSetName (string) - Name of the color set."""
	def getConnectedEdges(self)->MIntArray:
		"""getConnectedEdges() -> MIntArray

		This method gets the indices of the edges connected to the vertices of the current face, but DOES not include the edges contained in the current face"""
	def getConnectedFaces(self)->MIntArray:
		"""getConnectedFaces() -> MIntArray

		This method gets the indices of the faces connected to the current face."""
	def getConnectedVertices(self)->MIntArray:
		"""getConnectedVertices() -> MIntArray

		This method gets the object-relative indices of the vertices surrounding the vertices of the current face, but does not include the vertices of the current face"""
	def getEdges(self)->MIntArray:
		"""getEdges() -> MIntArray

		This method gets the indices of the edges contained in the current face."""
	@overload
	def getNormal(self,space:int=MSpace.kObject)->MVector:
		"""getNormal(space=kObject) -> MVector
		getNormal(vertexIndex, [space=]kObject) -> MVector

		Return the face normal of the current polygon.

		* space (int) - The transformation space. The keyword 'space' has to be explicitly stated. If not present, the argument will be identified as a 'vertexIndex' argument, and the second form of this function will be used instead.

		Returns the vertex-face normal for the vertex in the current polygon.

		* index (int) - face-relative vertex index of the vertex whose normal to retrieve
		* space (int) - The transformation space. Defaults to kObject, the keyword 'space' is optional as well."""
	@overload
	def getNormal(self,vertexIndex:int,space:int=MSpace.kObject)->MVector:
		"""getNormal(space=kObject) -> MVector
		getNormal(vertexIndex, [space=]kObject) -> MVector

		Return the face normal of the current polygon.

		* space (int) - The transformation space. The keyword 'space' has to be explicitly stated. If not present, the argument will be identified as a 'vertexIndex' argument, and the second form of this function will be used instead.

		Returns the vertex-face normal for the vertex in the current polygon.

		* index (int) - face-relative vertex index of the vertex whose normal to retrieve
		* space (int) - The transformation space. Defaults to kObject, the keyword 'space' is optional as well."""
	def getNormals(self,space:int=MSpace.kObject)->MVectorArray:
		"""getNormals(space=kObject) -> MVectorArray

		Returns the normals for all vertices in the current face

		* space (int) - The transformation space"""
	def getPointAtUV(self,uvPoint:list[float],space:int=MSpace.kObject,uvSet:str|None=None,tolerance:float=0)->MPoint:
		"""getPointAtUV(uvPoint, space=kObject, uvSet=None, tolerance=0) -> MPoint

		Return the position of the point at the given UV value in the current polygon.

		* uvPoint ([float, float]) - The UV value to try to locate
		* space (int) - The coordinate system for this operation
		* uvSet (string) - UV set to work with
		* tolerance (float) - tolerance value to compare float data type"""
	def getPoints(self,space:int=MSpace.kObject)->MPointArray:
		"""getPoints(space=kObject) -> MPointArray

		Retrieves the positions of the vertices on the current face/polygon that the iterator is pointing to. Vertex positions will be inserted into the given array and will be indexed using face-relative vertex IDs (ie. ordered from 0 to (vertexCount of the face) - 1), which should not be confused with the vertexIDs of each vertex in relation to the entire mesh object.

		* space (int) - The coordinate system for this operation"""
	def getTriangle(self,localTriIndex:int,space:int=MSpace.kObject)->list[MPointArray|MIntArray]:
		"""getTriangle(localTriIndex, space=kObject) -> [MPointArray, MIntArray]

		Get the vertices and vertex positions of the given triangle in the current face's triangulation.

		* localTriIndex (int) - Local index of the desired triangle in this face
		* space (int) - World Space or Object Space"""
	def getTriangles(self,space:int=MSpace.kObject)->list[MPointArray|MIntArray]:
		"""getTriangles(space=kObject) -> [MPointArray, MIntArray]

		Get the vertices and vertex positions of all the triangles in the current face's triangulation

		* space (int) - World Space or Object Space"""
	def getUV(self,vertexId:Any,uvSet:str|None=None)->list[float]:
		"""getUV(vertexId, uvSet=None) -> [float, float]

		Return the texture coordinate for the given vertex.

		* vertex (int) - The face-relative vertex index to get UV for
		* uvSet (string) - UV set to work with"""
	def getUVArea(self,uvSet:str|None=None)->float:
		"""getUVArea(uvSet=None) -> float

		This method gets the UV area of the face

		* uvSet (string) - UV set to work with"""
	def getUVAtPoint(self,pt:MPoint,space:int=MSpace.kObject,uvSet:str|None=None)->list[float]:
		"""getUVAtPoint(pt, space=kObject, uvSet=None) -> [float, float]

		Find the point closest to the given point in the current polygon, and return the UV value at that point.

		* pt (MPoint) - The point to try to get UV for
		* space (int) - The coordinate system for this operation
		* uvSet (string) - UV set to work with"""
	def getUVIndex(self,vertex:int,uvSet:str|None=None)->int:
		"""getUVIndex(vertex, uvSet=None) -> int

		Returns the index of the texture coordinate for the given vertex.
		This index refers to an element of the texture coordinate array for the polygonal object returned by MFnMesh.getUVs.

		* vertex (int) - The face-relative vertex index of the current polygon
		* uvSet (string) - UV set to work with"""
	def getUVIndexAndValue(self,vertex:int,uvSet:str|None=None)->list[int|float]:
		"""getUVIndexAndValue(vertex, uvSet=None) -> [int, float, float]

		Return the index and value of the texture coordinate for the given vertex. This index refers to an element of the texture coordinate array for the polygonal object returned by MFnMesh.getUVs.

		* vertex (int) - The face-relative vertex index of the current polygon
		* uvSet (string) - UV set to work with"""
	def getUVSetNames(self)->list[str]:
		"""getUVSetNames() -> list of strings

		This method is used to find the UV set names mapped to the current face"""
	def getUVs(self,uvSet:str|None=None)->list[MFloatArray]:
		"""getUVs(uvSet=None) -> [MFloatArray, MFloatArray]

		Return the all the texture coordinates for the vertices of this face (in local vertex order).

		* uvSet (string) - UV set to work with"""
	def getVertices(self)->MIntArray:
		"""getVertices() -> MIntArray

		This method gets the indices of the vertices of the current face"""
	@overload
	def hasColor(self)->bool:
		"""hasColor() -> bool
		hasColor(localVertexIndex) -> bool

		This method determines whether the current face has color-per-vertex set for any or the given vertex

		* localVertexIndex (int) - face-relative vertex index to check for color on"""
	@overload
	def hasColor(self,localVertexIndex:int)->bool:
		"""hasColor() -> bool
		hasColor(localVertexIndex) -> bool

		This method determines whether the current face has color-per-vertex set for any or the given vertex

		* localVertexIndex (int) - face-relative vertex index to check for color on"""
	def hasUVs(self,uvSet:str|None=None)->bool:
		"""hasUVs(uvSet=None) -> bool

		Tests whether this face has UV's mapped or not (either all the vertices for a face should have UV's, or none of them do, so the UV count for a face is either 0, or equal to the number of vertices).

		* uvSet (string) - UV set to work with"""
	def hasValidTriangulation(self)->bool:
		"""hasValidTriangulation() -> bool

		This method checks if the face has a valid triangulation. If it doesn't, then the face was bad geometry: it may gave degenerate points or cross over itself."""
	def index(self)->int:
		"""index() -> int

		Returns the index of the current polygon"""
	def isConnectedToEdge(self,index:int)->bool:
		"""isConnectedToEdge(index) -> bool

		This method determines whether the given face is adjacent to the current face

		* index (int) - Index of the face to be tested for"""
	def isConnectedToFace(self,index:int)->bool:
		"""isConnectedToFace(index) -> bool

		This method determines whether the given face is adjacent to the current face

		* index (int) - Index of the face to be tested for"""
	def isConnectedToVertex(self,index:int)->bool:
		"""isConnectedToVertex(index) -> bool

		This method determines whether the given vertex shares an edge with a vertex in the current face

		* index (int) - Index of the face to be tested for"""
	def isConvex(self)->bool:
		"""isConvex() -> bool

		This method checks if the face is convex."""
	def isDone(self)->bool:
		"""isDone() -> bool

		Indicates if all of the polygons have been traversed yet."""
	def isHoled(self)->bool:
		"""isHoled() -> bool

		This method checks if the face has any holes."""
	def isLamina(self)->bool:
		"""isLamina() -> bool

		This method checks if the face is a lamina (the face is folded over onto itself)."""
	def isPlanar(self)->bool:
		"""isPlanar() -> bool

		This method checks if the face is planar"""
	def isStarlike(self)->bool:
		"""isStarlike() -> bool

		This method checks if the face is starlike. That is, a line from the centre to any vertex lies entirely within the face."""
	def isUVReversed(self,faceId:Any)->bool:
		"""isUVReversed(faceId) -> bool

		Returns True if the texture coordinates (uv's) for the face are
		reversed (clockwise), False if they are not reversed (counter clockwise)."""
	def next(self)->Self:
		"""next() -> self

		Advance to the next polygon in the iteration."""
	def normalIndex(self,vertex:Any)->int:
		"""normalIndex(vertex) -> int

		Returns the normal index for the specified vertex.
		This index refers to an element in the normal array returned by MFnMesh.getNormals.  These normals are per-polygon per-vertex normals. See the MFnMesh description for more information on normals.

		* localVertexIndex (int) - The face-relative index of the vertex to examine for the current polygon"""
	def numColors(self,colorSetName:str|None=None)->int:
		"""numColors(colorSetName=None) -> int

		This method checks for the number of colors on vertices in this face

		* colorSetName (string) - Name of the color set."""
	def numConnectedEdges(self)->int:
		"""numConnectedEdges() -> int

		This method checks for the number of connected edges on the vertices of this face"""
	def numConnectedFaces(self)->int:
		"""numConnectedFaces() -> int

		This method checks for the number of connected faces"""
	def numTriangles(self)->int:
		"""numTriangles() -> int

		This Method checks for the number of triangles in this face in the current triangulation"""
	def onBoundary(self)->bool:
		"""onBoundary() -> bool

		This method determines whether the current face is on a boundary"""
	def point(self,index:int,space:int=MSpace.kObject)->MPoint:
		"""point(index, space=kObject) -> MPoint

		Return the position of the vertex at index in the current polygon.

		* index (int) - The face-relative index of the vertex in the current polygon
		* space (int) - The coordinate system for this operation"""
	def polygonVertexCount(self)->int:
		"""polygonVertexCount() -> int

		Return the number of vertices for the current polygon"""
	@overload
	def reset(self)->Self:
		"""reset() -> self
		reset(polyObject) -> self
		reset(polyObject, component=None) -> self

		Reset the iterator to the first polygon

		Reset the iterator to the first polygon in the supplied surface

		* polyObject (MObject) - The polygon for the iteration

		Reset the iterator with the given surface and component.
		If component is None then the iteration will be for all polygons in the given surface.

		* polyObject (MDagPath) - The surface (mesh) to iterate over
		* component (MObject) - The polygons (faces) of the polyObject to iterate over"""
	@overload
	def reset(self,polyObject:MObject)->Self:
		"""reset() -> self
		reset(polyObject) -> self
		reset(polyObject, component=None) -> self

		Reset the iterator to the first polygon

		Reset the iterator to the first polygon in the supplied surface

		* polyObject (MObject) - The polygon for the iteration

		Reset the iterator with the given surface and component.
		If component is None then the iteration will be for all polygons in the given surface.

		* polyObject (MDagPath) - The surface (mesh) to iterate over
		* component (MObject) - The polygons (faces) of the polyObject to iterate over"""
	@overload
	def reset(self,polyObject:MObject,component:MObject|None=None)->Self:
		"""reset() -> self
		reset(polyObject) -> self
		reset(polyObject, component=None) -> self

		Reset the iterator to the first polygon

		Reset the iterator to the first polygon in the supplied surface

		* polyObject (MObject) - The polygon for the iteration

		Reset the iterator with the given surface and component.
		If component is None then the iteration will be for all polygons in the given surface.

		* polyObject (MDagPath) - The surface (mesh) to iterate over
		* component (MObject) - The polygons (faces) of the polyObject to iterate over"""
	def setIndex(self,index:int)->int:
		"""setIndex(index) -> int

		This method sets the index of the current face to be accessed.
		The current face will no longer be in sync with any previous iteration.
		Returns the index of the current face in the iteration

		* index (int) - The index of desired face to access."""
	def setPoint(self,point:MPoint,index:int,space:int=MSpace.kObject)->Self:
		"""setPoint(point, index, space=kObject) -> self

		Set the vertex at the given index in the current polygon.

		* point (MPoint) - The new position for the vertex
		* index (int) - The face-relative index of the vertex in the current polygon
		* space (int) - The coordinate system for this operation"""
	def setPoints(self,pointArray:MPointArray,space:int=MSpace.kObject)->Self:
		"""setPoints(pointArray, space=kObject) -> self

		Sets new locations for vertices of the current polygon that the iterator is pointing to.

		* pointArray (MPointArray) - The new positions for the vertices.
		* space (int) - The coordinate system for this operation."""
	def setUV(self,vertexId:int,uvPoint:list[float],uvSet:str|None=None)->Self:
		"""setUV(vertexId, uvPoint, uvSet=None) -> self

		Modify the UV value for the given vertex in the current face.
		If the face is not already mapped, this method will fail.

		* vertexId (int) - face-relative index of the vertex to set UV for.
		* uvPoint ([float, float]) - The UV values to set it to
		* uvSet (string) - UV set to work with"""
	def setUVs(self,uArray:MFloatArray,vArray:MFloatArray,uvSet:str|None=None)->Self:
		"""setUVs(uArray, vArray, uvSet=None) -> self

		Modify the UV value for all vertices in the current face.
		If the face has not already been mapped, this method will fail.

		* uArray (MFloatArray) - All the U values - in local face order
		* vArray (MFloatArray) - The corresponding V values
		* uvSet (string) - UV set to work with"""
	def tangentIndex(self,localVertexIndex:int)->int:
		"""tangentIndex(localVertexIndex) -> int

		Returns the tangent (or binormal) index for the specified vertex.
		This index refers to an element in the normal array returned by MFnMesh.getTangents. These tangent or binormals are per-polygon per-vertex.
		See the MFnMesh description for more information on tangents and binormals.

		* localVertexIndex(int) - The face-relative index of the vertex to examine for the current polygon"""
	def updateSurface(self)->Self:
		"""updateSurface() -> self

		Signal that this polygonal surface has changed and needs to redraw itself."""
	def vertexIndex(self,index:int)->int:
		"""vertexIndex(index) -> int

		Returns the object-relative index of the specified vertex of the current polygon.
		The index returned may be used to refer to an element in the vertex list returned by MFnMesh.getPoints.

		* index (int) - The face-relative index of the vertex in the polygon"""
	def zeroArea(self)->bool:
		"""zeroArea() -> bool

		This method checks if its a zero area face"""
	def zeroUVArea(self,uvSet:str|None=None)->bool:
		"""zeroUVArea(uvSet=None) -> bool

		This method checks if the UV area of the face is zero

		* uvSet (string) - UV set to work with"""
class MItMeshVertex:
	"""This class is the iterator for polygonal surfaces (meshes)."""
	def __iter__(self)->Any:
		"""Implement iter(self)."""
	def __next__(self)->Any:
		"""Implement next(self)."""
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def iternext(self)->Self:
		"""iternext() -> self

		Used in pythonic iteration to move the iterator"""
	def iter(self)->Self:
		"""iter() -> self

		Initializes the iterator object for pythonic iteration."""
	def count(self)->int:
		"""count() -> int

		Return the number of vertices in the iteration"""
	def currentItem(self)->MObject:
		"""currentItem() -> MObject

		Get the current vertex in the iteration as a component.

		Components are used to specify one or more vertices and are usefull in operating on groups of non-contiguous vertices for a surface.
		Components do not contain any information about the surface that they refer to so an MDagPath must be specified when dealing with components."""
	def geomChanged(self)->Self:
		"""geomChanged() -> self

		Reset the geom pointer in the MItMeshVertex. If you're using MFnMesh to
		update Normals or Color per vertex while iterating, you must call geomChanged
		on the iteratior immediately after the MFnMesh call to make sure that your
		geometry is up to date. A crash may result if this method is not called.
		A similar approach must be taken for updating upstream vertex tweaks
		with an MPlug. After the update, call this method."""
	def getConnectedEdges(self)->MIntArray:
		"""getConnectedEdges() -> MIntArray

		This method gets the indices of the edges contained in the current vertex."""
	def getConnectedFaces(self)->MIntArray:
		"""getConnectedFaces() -> MIntArray

		This method gets the indices of the faces connected to the current vertex."""
	def getConnectedVertices(self)->MIntArray:
		"""getConnectedVertices() -> MIntArray

		This method gets the indices of the vertices surrounding the current vertex."""
	@overload
	def getNormal(self,space:int=MSpace.kObject)->MVector:
		"""getNormal(space=kObject) -> MVector
		getNormal(faceIndex, space=kObject) -> MVector

		Return the normal or averaged normal if unshared of the current vertex.

		* space (int) - The transformation space

		Return the normal of the current vertex in the specified face.

		* faceIndex (int) - face index to get normal for
		* space (int) - The transformation space"""
	@overload
	def getNormal(self,faceIndex:int,space:int=MSpace.kObject)->MVector:
		"""getNormal(space=kObject) -> MVector
		getNormal(faceIndex, space=kObject) -> MVector

		Return the normal or averaged normal if unshared of the current vertex.

		* space (int) - The transformation space

		Return the normal of the current vertex in the specified face.

		* faceIndex (int) - face index to get normal for
		* space (int) - The transformation space"""
	def getNormals(self,space:int=MSpace.kObject)->MVectorArray:
		"""getNormals(space=kObject) -> MVectorArray

		Return the normals of the current vertex for all faces

		* space (int) - The transformation space"""
	def getNormalIndices(self)->MIntArray:
		"""getNormalIndices() -> MIntArray

		This method returns the normal indices of the face/vertex associated
		with the current vertex."""
	@overload
	def getUV(self,uvSet:str|None=None)->list[float]:
		"""getUV(uvSet=None) -> [float, float]getUV(faceId, uvSet=None) -> [float, float]

		Get the shared UV value at this vertex.

		* uvSet (string) - Name of the uv set to work with.

		Get the UV value for the give facen at the current vertex.

		* faceId (int) - Index of the required face
		* uvSet (string) - Name of the uv set to work with"""
	@overload
	def getUV(self,faceId:int,uvSet:str|None=None)->list[float]:
		"""getUV(uvSet=None) -> [float, float]getUV(faceId, uvSet=None) -> [float, float]

		Get the shared UV value at this vertex.

		* uvSet (string) - Name of the uv set to work with.

		Get the UV value for the give facen at the current vertex.

		* faceId (int) - Index of the required face
		* uvSet (string) - Name of the uv set to work with"""
	def getUVIndices(self,uvSet:str|None=None)->MIntArray:
		"""getUVIndices(uvSet=None) -> MIntArray

		This method returns the uv indices into the normal array see MFnMesh::getUVs()
		of the current vertex.

		* uvSet (string) - Name of the uv set."""
	def getUVs(self,uvSet:str|None=None)->list[MFloatArray|MIntArray]:
		"""getUVs(uvSet=None) -> [MFloatArray, MFloatArray, MIntArray]

		Get the UV values for all mapped faces at the current vertex.
		If at least one face was mapped the method will succeed.

		* uvSet (string) - Name of the uv set to work with"""
	def index(self)->int:
		"""index() -> int

		Returns the index of the current vertex in the vertex list for this
		polygonal object.
		Polygonal objects contain a list of vertices. Faces and edges are
		specified as indicies from this list, in this way vertices can
		be shared amoung faces and edges."""
	def connectedToEdge(self,index:int)->bool:
		"""connectedToEdge(index) -> bool

		This method determines whether the given edge contains the current vertex

		* index (int) - Index of edge to check."""
	def connectedToFace(self,index:int)->bool:
		"""connectedToFace(index) -> bool

		This method determines whether the given face contains the current vertex

		* index (int) - Index of face to check."""
	@overload
	def getColor(self,colorSetName:str|None=None)->MColor:
		"""getColor(colorSetName=None) -> MColor
		getColor(faceIndex, colorSetName=None) -> MColor

		This method gets the average color of the vertex

		* colorSetName (string) - Name of the color set.

		This method gets the color of the current vertex in the specified face

		* index (int) - The face to get the color for this vertex for* colorSetName (string) - Name of the color set."""
	@overload
	def getColor(self,faceIndex:int,colorSetName:str|None=None)->MColor:
		"""getColor(colorSetName=None) -> MColor
		getColor(faceIndex, colorSetName=None) -> MColor

		This method gets the average color of the vertex

		* colorSetName (string) - Name of the color set.

		This method gets the color of the current vertex in the specified face

		* index (int) - The face to get the color for this vertex for* colorSetName (string) - Name of the color set."""
	def getColorIndices(self,colorSetName:str|None=None)->MIntArray:
		"""getColorIndices(colorSetName=None) -> MIntArray

		This method returns the colorIndices into the color array see MFnMesh::getColors()
		of the current vertex.

		* colorSetName (string) - Name of the color set."""
	def getColors(self,colorSetName:str|None=None)->MColorArray:
		"""getColors(colorSetName=None) -> MColorArray

		This method gets the colors of the current vertex for each face it
		belongs to. If no colors are assigned to the vertex at all, the
		return values will be (-1 -1 -1 1). If some but not all of the
		vertex/face colors have been explicitly set, the ones that have not
		been set will be (0, 0, 0, 1).

		* colorSetName (string) - Name of the color set."""
	def getOppositeVertex(self,edgeId:int)->int:
		"""getOppositeVertex(edgeId) -> int

		This method gets the other vertex of the given edge

		* edgeId (int) - The edge to get the other vertex for"""
	@overload
	def hasColor(self)->bool:
		"""hasColor() -> bool
		hasColor(index) -> bool

		This method determines whether the current Vertex has a color set
		for one or more faces.

		* index (int) - Index of face to check"""
	@overload
	def hasColor(self,index:int)->bool:
		"""hasColor() -> bool
		hasColor(index) -> bool

		This method determines whether the current Vertex has a color set
		for one or more faces.

		* index (int) - Index of face to check"""
	def isDone(self)->bool:
		"""isDone() -> bool

		Indicates if all of the vertices have been traversed yet."""
	def next(self)->Self:
		"""next() -> self

		Advance to the next edge in the iteration."""
	def numConnectedEdges(self)->int:
		"""numConnectedEdges() -> int

		This Method checks for the number of connected Edges on this vertex"""
	def numConnectedFaces(self)->int:
		"""numConnectedFaces() -> int

		This Method checks for the number of Connected Faces"""
	def numUVs(self,uvSet:str|None=None)->int:
		"""numUVs(uvSet=None) -> int

		This method returns the number of unique UVs mapped on this vertex

		* uvSet (string) - Name of the uv set to work with"""
	def onBoundary(self)->bool:
		"""onBoundary() -> bool

		This method determines whether the current vertex is on a Boundary"""
	def position(self,space:int=MSpace.kObject)->MPoint:
		"""position(space=kObject) -> MPoint

		Return the position of the current vertex in the specified space.
		Object space ignores all transformations for the polygon, world space
		includes all such transformations.

		* space (int) - The  transformation space"""
	@overload
	def reset(self)->Self:
		"""reset() -> self
		reset(polyObject) -> self
		reset(polyObject, component=None) -> self

		Reset the iterator to the first polygon

		Reset the iterator to the first polygon in the supplied polygon

		* polyObject (MObject) - The polygon for the iteration

		Reset the iterator with the given surface and component.
		If component is None then the iteration will be for all vertices in the given polygon.

		* polyObject (MDagPath) - The surface (mesh) to iterate over
		* component (MObject) - The vertices of the polyObject to iterate over"""
	@overload
	def reset(self,polyObject:MObject)->Self:
		"""reset() -> self
		reset(polyObject) -> self
		reset(polyObject, component=None) -> self

		Reset the iterator to the first polygon

		Reset the iterator to the first polygon in the supplied polygon

		* polyObject (MObject) - The polygon for the iteration

		Reset the iterator with the given surface and component.
		If component is None then the iteration will be for all vertices in the given polygon.

		* polyObject (MDagPath) - The surface (mesh) to iterate over
		* component (MObject) - The vertices of the polyObject to iterate over"""
	@overload
	def reset(self,polyObject:MObject,component:MObject|None=None)->Self:
		"""reset() -> self
		reset(polyObject) -> self
		reset(polyObject, component=None) -> self

		Reset the iterator to the first polygon

		Reset the iterator to the first polygon in the supplied polygon

		* polyObject (MObject) - The polygon for the iteration

		Reset the iterator with the given surface and component.
		If component is None then the iteration will be for all vertices in the given polygon.

		* polyObject (MDagPath) - The surface (mesh) to iterate over
		* component (MObject) - The vertices of the polyObject to iterate over"""
	def setIndex(self,index:int)->int:
		"""setIndex(index) -> int

		This method sets the index of the current vertex to be accessed.
		The current vertex will no longer be in sync with any previous iteration.

		* index (int) - The index of desired vertex to access."""
	def setPosition(self,point:MPoint,space:int=MSpace.kObject)->Self:
		"""setPosition(point, space=kObject) -> self

		Set the position of the current vertex in the given space.

		* point (MPoint) - The new position for the current vertex
		* space (int) - The Transformation space"""
	@overload
	def setUV(self,uvPoint:list[float],uvSet:str|None=None)->Self:
		"""setUV(uvPoint, uvSet=None) -> selfsetUV(faceId, uvPoint, uvSet=None) -> self

		Set the shared UV value at this vertex

		* uvPoint ([float, float]) - The UV values to set
		* uvSet (string) - Name of the UV set to work with

		Set the UV value for the given face at the current vertex

		* faceId (int) - Index of required face
		* uvPoint ([float, float]) - The UV values to set
		* uvSet (string) - Name of the UV set to work with"""
	@overload
	def setUV(self,faceId:int,uvPoint:list[float],uvSet:str|None=None)->Self:
		"""setUV(uvPoint, uvSet=None) -> selfsetUV(faceId, uvPoint, uvSet=None) -> self

		Set the shared UV value at this vertex

		* uvPoint ([float, float]) - The UV values to set
		* uvSet (string) - Name of the UV set to work with

		Set the UV value for the given face at the current vertex

		* faceId (int) - Index of required face
		* uvPoint ([float, float]) - The UV values to set
		* uvSet (string) - Name of the UV set to work with"""
	def setUVs(self,uArray:MFloatArray,vArray:MFloatArray,faceIds:MIntArray,uvSet:str|None=None)->Self:
		"""setUVs(uArray, vArray, faceIds, uvSet=None) -> self

		Set the UV value for the specified faces at the current vertex.
		If the face is not already mapped, the value will not be set.
		If at least ne face was previously mapped, the method should succeed.
		If no faces were mapped, the method will fail.

		* uArray (MFloatArray) - All the U values - in local face order
		* vArray (MFloatArray) - The corresponding V values
		* faceIds (MIntArray) - The corresponding face Ids
		* uvSet (string) - UV set to work with"""
	def translateBy(self,vector:MVector,space:int=MSpace.kObject)->Self:
		"""translateBy(vector, space=kObject) -> self

		Translate the current vertex by the amount specified
		by the given vector.

		* vector (MVector) - The amount of translation
		* space (int) - The Transformation space"""
	def updateSurface(self)->Self:
		"""updateSurface() -> self

		Signal that this polygonal surface has changed and needs to redraw itself."""
class MItSelectionList:
	"""Class for iterating over the items in an MSelection list."""
	kUnknownItem:int=-1
	kDagSelectionItem:int=0
	kAnimSelectionItem:int=1
	kDNselectionItem:int=2
	kPlugSelectionItem:int=3
	def __iter__(self)->Any:
		"""Implement iter(self)."""
	def __next__(self)->Any:
		"""Implement next(self)."""
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def iternext(self)->Self:
		"""iternext() -> self

		Used in pythonic iteration to move the iterator"""
	def iter(self)->Self:
		"""iter() -> self

		Initializes the iterator object for pythonic iteration."""
	def getDagPath(self)->MDagPath:
		"""getDagPath() -> MDagPath

		This method retrieves the dag path of the current selection item."""
	def getComponent(self)->tuple[MDagPath,MObject]:
		"""getComponent() -> (MDagPath, MObject)

		This method retrieves the dag path and the component of the current selection item."""
	def getDependNode(self)->MObject:
		"""getDependNode() -> MObject

		This method retrieves the dependency node of the current selection itemRaises kFailure if there is no dependency node associated with the current item"""
	def getPlug(self)->MPlug:
		"""getPlug() -> MPlug

		This method retrieves the plug of the current selection item."""
	def getStrings(self)->list[str]:
		"""getStrings() -> list of strings

		Get the string representation of the current item in the selection list.
		It is possible that it will require more than one string to represent the item (the item may contain groups of CVs for example)"""
	def hasComponents(self)->bool:
		"""hasComponents() -> bool

		Returns whether or not the current selection item has components."""
	def isDone(self)->bool:
		"""isDone() -> bool

		Specifies whether or not there is anything more to iterator over."""
	def itemType(self)->int:
		"""itemType() -> int

		Returns the current selection item type.

		  kDagSelectionItem    selection item is in the DAG
		  kAnimSelectionItem   selection item is a keyset
		  kDNselectionItem     selection item is a dependency node"""
	def next(self)->Self:
		"""next() -> self

		Advance to the next item. If components are selected then advance to next component.

		If a filter is specified then the next item will be one that matches the filter."""
	def reset(self)->Self:
		"""reset() -> self

		Reset the iterator.
		If a filter has been specified then the current item will be the first selected item that matches the filter."""
	def setFilter(self,filter:Any)->Self:
		"""setFilter(filter) -> self

		Apply a filter to the iteration.
		Selection items not matching the filter type will be excluded from the iteration."""
class MItSurfaceCV:
	""" NURBS surface CV iterator."""
	def __iter__(self)->Any:
		"""Implement iter(self)."""
	def __next__(self)->Any:
		"""Implement next(self)."""
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def iternext(self)->Self:
		"""iternext() -> self

		Used in pythonic iteration to move the iterator"""
	def iter(self)->Self:
		"""iter() -> self

		Initializes the iterator object for pythonic iteration."""
	def hasHistoryOnCreate(self)->bool:
		"""hasHistoryOnCreate() -> bool

		This method determines if the shape was created with history.

		If the object that this iterator is attached to is not a shape then this method will raise."""
	def currentItem(self)->MObject:
		"""currentItem() -> MObject

		Get the current CV in the iteration as a component.

		Components are used to specify one or more CVs and are useful in operating on groups of non-contiguous CVs for a curve or surface.
		Components do not contain any information about the surface that they refer to so an MDagPath must be specified when dealing with components."""
	def index(self)->int:
		"""index() -> int

		Get the index of the current CV as it appears in CV array for this surface."""
	def uvIndices(self)->tuple[int,int]:
		"""uvIndices() -> (indexU, indexV)

		Get the u and v index of the current CV."""
	def isDone(self)->bool:
		"""isDone() -> bool

		Returns True if the iteration is finished, i.e. there are no more CVs to iterate on."""
	def isRowDone(self)->bool:
		"""isRowDone() -> bool

		Returns True if the current row has no more CVs to iterate over.
		The row can be in the U or V direction depending on what value of useURows has been set in the constructor."""
	def next(self)->Self:
		"""next() -> self

		Advance to the next CV in the iteration.
		If the iterator is already at the last CV then this method has no effect. Use isDone() to determine if the iterator is at the last CV."""
	def nextRow(self)->Self:
		"""nextRow() -> self

		Advance to the next row in the iteration.
		The row can be in the U or V direction depending on what value of useURows has been set in the constructor."""
	def position(self,space:int=MSpace.kObject)->MPoint:
		"""position(space=kObject) -> MPoint

		Returns the position of the current CV in the iteration in the specified space.

		* space (int) - The coordinate space in which the CV is set"""
	@overload
	def reset(self)->Self:
		"""reset() -> self
		reset(surface, useURows=True) -> self
		reset(surface, component, useURows=True) -> self

		Reset the iterator to the first CV.

		Or
		Reset the iterator to iterate over all CVs on the specified surface.

		* surface (MObject) - The surface for the iteration
		* useURows (bool) - If True then the iterator will iterate in the U direction, otherwise it will be in the V direction.

		Or
		Reset the iterator to iterate over the CVs of the given surface that are specified in the given component. If the component is NULL then the iteration will be over all CVs on the surface.

		* surface (MDagPath) - The surface for the iteration
		* component (MObject) - A group of CVs to be iterated on
		* useURows (bool) - If True then the iterator will iterate in the U direction, otherwise it will be in the V direction."""
	@overload
	def reset(self,surface:MObject,useURows:bool=True)->Self:
		"""reset() -> self
		reset(surface, useURows=True) -> self
		reset(surface, component, useURows=True) -> self

		Reset the iterator to the first CV.

		Or
		Reset the iterator to iterate over all CVs on the specified surface.

		* surface (MObject) - The surface for the iteration
		* useURows (bool) - If True then the iterator will iterate in the U direction, otherwise it will be in the V direction.

		Or
		Reset the iterator to iterate over the CVs of the given surface that are specified in the given component. If the component is NULL then the iteration will be over all CVs on the surface.

		* surface (MDagPath) - The surface for the iteration
		* component (MObject) - A group of CVs to be iterated on
		* useURows (bool) - If True then the iterator will iterate in the U direction, otherwise it will be in the V direction."""
	@overload
	def reset(self,surface:MObject,component:MObject,useURows:bool=True)->Self:
		"""reset() -> self
		reset(surface, useURows=True) -> self
		reset(surface, component, useURows=True) -> self

		Reset the iterator to the first CV.

		Or
		Reset the iterator to iterate over all CVs on the specified surface.

		* surface (MObject) - The surface for the iteration
		* useURows (bool) - If True then the iterator will iterate in the U direction, otherwise it will be in the V direction.

		Or
		Reset the iterator to iterate over the CVs of the given surface that are specified in the given component. If the component is NULL then the iteration will be over all CVs on the surface.

		* surface (MDagPath) - The surface for the iteration
		* component (MObject) - A group of CVs to be iterated on
		* useURows (bool) - If True then the iterator will iterate in the U direction, otherwise it will be in the V direction."""
	def setPosition(self,point:MPoint,space:int=MSpace.kObject)->Self:
		"""setPosition(point, space=kObject) -> self

		Set the position of the current CV in the iteration to the specified point.

		* point (MPoint) - The new position for the current CV in the iteration
		* space (int) - The coordinate space in which the CV is set"""
	def translateBy(self,vector:MVector,space:int=MSpace.kObject)->Self:
		"""translateBy(vector, space=kObject) -> self

		Move the current CV in the iteration by the sepcified vector.

		* vector (MVector) - The translation vector
		* space (int) - The coordinate space in which the CV is set"""
	def updateSurface(self)->Self:
		"""updateSurface() -> self

		This method is used to signal the surface that it has been changed and needs to redraw itself.

		When modifying a large number of CVs, it is most efficient to call this method after all of the CVs have been modified."""
class MIteratorType:
	"""The MIteratorType class is used on iterators where more than one type
	of filters can be specified. It also provides functionalities to set and
	get the filter list or individual types of filter. This class should be
	used in conjunction with DAG/DG/DependencyNodes iterators for using filter
	list (list of MFn::Type objects) on them, thus enabling faster traversal
	thro' iterators.

	Also, the class has functionalities for specifying the type of object the
	iterator will be reset to. This could be an MObject, an MPlug or an MDagPath."""
	@property
	def filterType(self)->Any:
		"""Filter type (MFn.Type)."""
	@filterType.setter
	def filterType(self,value:Any)->None:...
	@property
	def filterList(self)->Any:
		"""Filter list (MIntArray containing MFn.Type)."""
	@filterList.setter
	def filterList(self,value:Any)->None:...
	@property
	def objectType(self)->Any:
		"""Object type (MIteratorType.objFilterType)."""
	@objectType.setter
	def objectType(self,value:Any)->None:...
	@property
	def filterListEnabled(self)->Any:
		"""Whether the we are using a single filter on the iterator or a filter list (Boolean)."""
	@filterListEnabled.setter
	def filterListEnabled(self,value:Any)->None:...
	kMObject:int=0
	kMDagPathObject:int=1
	kMPlugObject:int=2
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
class MLockMessage(MMessage):
	"""Class used to register callbacks for model related messages."""
	kInvalidPlug:int=0
	kPlugLockAttr:int=1
	kPlugUnlockAttr:int=2
	kPlugAttrValChange:int=3
	kPlugRemoveAttr:int=4
	kPlugRenameAttr:int=5
	kPlugConnect:int=6
	kPlugDisconnect:int=7
	kLastPlug:int=8
	kInvalidDAG:int=0
	kGroup:int=1
	kUnGroup:int=2
	kReparent:int=3
	kChildReorder:int=4
	kCreateNodeInstance:int=5
	kCreateChildInstance:int=6
	kCreateParentInstance:int=7
	kLastDAG:int=8
	kInvalid:int=0
	kRename:int=1
	kDelete:int=2
	kLockNode:int=3
	kUnlockNode:int=4
	kAddAttr:int=5
	kRemoveAttr:int=6
	kRenameAttr:int=7
	kUnlockAttr:int=8
	kLockAttr:int=9
	kLast:int=10
	@staticmethod
	def setNodeLockDAGQueryCallback(dagPath:MDagPath,function:Callable,clientData:Any|None=None)->int:
		"""setNodeLockDAGQueryCallback(dagPath, function, clientData=None) -> id

		This methods registers a callback that is invoked in any situation
		involving a locking condition on DAG level changes.  When called,
		the API user can make a decision on how to handle the given locking
		situation. The programmer can either accept the default action, or
		they can deny the default action. The decision is returned through a
		decision variable which is passed to the callback function.

		The callback function takes the following parameters:
		 * dagPath - The DAG path that the event occurred on.
		 * otherPath - The other path involved, e.g. the new parent.
		 * clientData - User defined data passed to the callback function.
		 * eventType - Description of the event.
		And return True to accept the default behavior and False to
		reject it.

		 The meanings of the dagPath and otherPath parameters for each
		eventType, and default actions associated with those event types, are
		as follows:

		kGroup
		 * dagPath - Path of the node to be grouped.
		 * otherPath - Path of the group node.
		 * default actions - If dagPath
		   is locked then the default action is to not allow the grouping.
		   If dagPath is unlocked then dagPath
		   can be grouped with otherPath.

		kUnGroup
		 * dagPath - Path of the node attempted to ungroup.
		 * otherPath - Path of the group node.
		 * default actions - If dagPath is locked then
		   the default action is to not allow the ungrouping. If dagPath
		   is unlocked then dagPath can be ungrouped from otherPath.

		kReparent
		 * dagPath - Path of the node which is being reparented.
		 * otherPath - Path of the new parent, if any. When
		   reparenting to the world, otherPath will be invalid.
		 * default actions - If dagPath is locked then
		   the default action is to not allow the reparenting. If dagPath
		   is unlocked then dagPath can be parented to otherPath.

		kChildReorder
		 * dagPath - Path of the child node to be reordered.
		 * otherPath - Path of the parent node.
		 * default actions - If dagPath is locked then
		   the default action is to not allow the reordering. If dagPath
		   is unlocked then dagPath can be reordered on otherPath.

		kCreateNodeInstance
		 * dagPath - Path of the node which is being instanced.
		 * otherPath - Invalid Path.
		 * default actions - If dagPath is locked then
		   the default action is to not allow the instance to be created.
		   If dagPath is unlocked then dagPath can be instanced.

		kCreateChildInstance
		 * dagPath - Path of the node whose child is being
		   instanced.
		 * otherPath - Path of the child node.
		 * default actions - If dagPath is locked then
		   the default action is to not allow the instance to be created.
		   If dagPath is unlocked then dagPath can be instanced.

		 * dagPath (MDagPath) - The path to attach the callback.
		 * function - the callback function (see below for the description)
		 * clientData - User defined data passed to the callback function

		 * return: Identifier used for removing the callback."""
	@staticmethod
	def setNodeLockQueryCallback(node:MObject,function:Callable,clientData:Any|None=None)->int:
		"""setNodeLockQueryCallback(node, function, clientData=None) -> id

		This methods registers a callback that is invoked in any locking
		condition on node properties, e.g. name, lock status, etc. When
		called, the API user can make a decision on how to handle the given
		locking situation. The programmer can either accept the default
		action, or they can deny the default action. The decision is returned
		through a decision variable which is passed to the callback function.

		The callback function takes the following parameters:
		   * node - The node that triggered the callback.
		   * aux - Any auxiliary data that may be needed, e.g.
		     the attribute about to be added.
		   * clientData - User defined data passed to the
		     callback function.
		   * eventType - Description of the event.
		And return True to accept the default behavior and False to
		reject it.

		The meanings of the node and aux parameters for each
		eventType, and default actions associated with those event types, are
		as follows:

		kRename
		   * node - The node that the user is attempting to rename.
		   * aux - MObject.kNullObj
		   * default actions - If node is locked then the
		     default action is to not allow the rename. Otherwise,
		     if node is unlocked then node can be renamed.

		kDelete   * node - The node that the user is attempting to delete.
		   * aux - MObject.kNullObj
		   * default actions - If node is locked then the
		     default action is to not allow the delete. If node is unlocked
		     then the node can be deleted.

		kLockNode   * node - The node that the user is attempting to lock.
		   * aux - MObject.kNullObj
		   * default actions - If node is unlocked then the
		     default action is to ALLOW the node to be locked. The callback
		     is not invoked when the user tries to unlock an already unlocked
		     node.

		kUnlockNode   * node - The node that the user is attempting to unlock.
		   * aux - MObject.kNullObj
		   * default actions - If node is locked then the
		     default action is to ALLOW the unlock. The callback is not invoked
		     when the user tries to unlock an already unlocked node.

		kAddAttr   * node - The node that is having an attribute added.
		   * aux - MObject of the attribute to be added. Note:
		     the attribute does not belong to the node yet. You can only
		     access the attribute information using MFnAttribute.
		   * default actions - If node is locked then the default
		     action is to not allow to the addition of aux. If node
		     is unlocked then aux can be added to the node.

		kRemoveAttr
		   * node - The node that is having an attribute removed.
		   * aux - The attribute to be removed. In certain
		     situations the user is allowed to do a global delete,
		     e.g. "deleteAttr -at AttrName [nodes]". In these cases the plug is not
		     created until checks have been performed; so aux ==
		     MObject.kNullObj
		   * default actions - If node is locked then the default
		     action is to not allow the attribute removal. If node is
		     unlocked then aux can be removed.

		kRenameAttr
		   * node - The node that is having an attribute renamed.
		   * aux - The attribute.
		   * default actions - If node is locked then the default
		     action is to not allow the rename. If node is unlocked then
		     aux can be renamed.

		kUnlockAttr
		   * node - The node that is having an attribute unlocked.
		   * aux - The attribute to be unlocked.
		   * default actions - If node is locked then the default
		     action is to not allow the unlock. If node is unlocked then
		     aux attribute can be unlocked.

		kLockAttr
		   * node - The node that is having an attribute locked.
		   * aux - The attribute to be locked.
		   * default actions - If node is locked then the default
		     action is to not allow the locking of aux. If node is
		     unlocked then aux can be locked.

		 * node (MObject) - The node to register the callback for.
		 * function - the callback function (see below for description)
		 * clientData - User defined data passed to the callback function

		 * return: Identifier used for removing the callback."""
	@staticmethod
	def setPlugLockQueryCallback(plug:MPlug,function:Callable,clientData:Any|None=None)->int:
		"""setPlugLockQueryCallback(plug, function, clientData=None) -> id

		This method registers a callback that is invoked in any locking
		condition on a plug, e.g. plug unlock, plug lock, connections, etc.
		When the callback is invoked, the API programmer can make a decision on
		how to handle the given locking situation. The programmer can either
		accept the default action, or they can deny the default action.
		The decision is made through the decision variable described above.

		The callback function takes the following parameters:
		   * plug - The plug that triggered the callback.
		   * otherPlug - The other plug involved in the callback.
		     This is only valid during connect and disconnect events.
		     clientData - User defined data passed to the
		     callback function.
		   * eventType - Description of the event.
		And return True to accept the default behavior and False to
		reject it.

		The meanings of the plug and otherPlug parameters for each
		eventType, and default actions associated with those event types, are
		as follows:

		kPlugLockAttr
		   * plug - The plug that the user is attempting to lock.
		   * otherPlug - None.
		   * default actions - If plug is unlocked then the
		     default action is to allow the plug to be locked.

		kPlugUnlockAttr
		   * plug - The plug that the user is attempting to unlock.
		   * otherPlug - None.
		   * default actions - If plug is locked then the
		     default action is to allow the plug to be unlocked.

		kPlugAttrValChange
		   * plug - The plug that the user is attempting to change.
		   * otherPlug - None.
		   * default actions - If plug is locked then the
		     default action is to not allow plug to change. If plug is
		     unlocked then plug can change.

		kPlugRemoveAttr
		   * plug - The plug that the user is attempting to remove.
		   * otherPlug - None.
		   * default actions - If plug is locked then the
		     default action is to not allow removal. Otherwise, if plug is
		     unlocked then plug can be removed.

		kPlugRenameAttr
		   * plug - The plug that the user is attempting to rename.
		   * otherPlug - None.
		   * default actions - If plug is locked then the default
		     action is to not allow the rename. Otherwise, if plug is
		     unlocked then plug can be renamed.

		kPlugConnect
		   * plug - The plug that is to be connected (incoming
		     connection).
		   * otherPlug - The source plug of the connection being made.
		   * default actions - If plug is locked then the
		     connection is DENIED. If plug is unlocked then otherPlug can
		     be connected to plug.

		kPlugDisconnect
		   * plug - The plug that it is having an incoming connection broken.
		   * otherPlug - The source plug of the connection being made.
		   * default actions - If plug is locked then the
		     default action is to DENY the connection from being broken. If
		     plug is unlocked then otherPlug can be disconnected from
		     plug.

		 * plug (MPlug) - the plug to attach the callback
		 * function - the callback function (see below for description)
		 * clientData - User defined data passed to the callback function

		 * return: Identifier used for removing the callback."""
class MMatrix(collections.abc.Sequence[float]):
	"""4x4 matrix with double-precision elements."""
	__hash__:None=None
	kIdentity:MMatrix
	kTolerance:float=1e-10
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
	@overload
	def __init__(self)->None:
		"""Default constructor. Returns a new matrix set to the identity matrix."""
	@overload
	def __init__(self,src:MMatrix)->None:
		"""Copy constructor. Returns a new matrix with the same value as src ."""
	@overload
	def __init__(self,values:Sequence[Any|tuple[Any,...]])->None:
		"""Returns a new matrix whose elements are set to those given by values . Values are interpreted in row order, so the first four values make up the first row of the matrix, the second four values the second row of the matrix, and so on."""
	def __add__(self,other:MMatrix)->MMatrix:
		"""Returns a new matrix which is the sum of the two matrices."""
	def __radd__(self,other:MMatrix)->MMatrix:
		"""Returns a new matrix which is the sum of the two matrices."""
	def __sub__(self,other:MMatrix)->MMatrix:
		"""Returns a new matrix which is the result of subtracting the second matrix from the first."""
	def __rsub__(self,other:MMatrix)->MMatrix:
		"""Returns a new matrix which is the result of subtracting the second matrix from the first."""
	@overload
	def __mul__(self,other:MMatrix)->MMatrix:
		"""Returns a new matrix which is the product of the two matrices."""
	@overload
	def __mul__(self,other:float)->MMatrix:
		"""Returns a new matrix in which all of the elements of the given matrix have been multiplied by the given float."""
	@overload
	def __rmul__(self,other:MMatrix)->MMatrix:
		"""Returns a new matrix which is the product of the two matrices."""
	@overload
	def __rmul__(self,other:float)->MMatrix:
		"""Returns a new matrix in which all of the elements of the given matrix have been multiplied by the given float."""
	def __iadd__(self,other:MMatrix)->Self:
		"""Adds the second matrix to the first and returns a new reference to the first."""
	def __isub__(self,other:MMatrix)->Self:
		"""Subtracts the second matrix from the first and returns a new reference to the first."""
	@overload
	def __imul__(self,other:MMatrix)->Self:
		"""Multiplies the first matrix by the second and returns a new reference to the first."""
	@overload
	def __imul__(self,other:float)->Self:
		"""Multiplies all the elements of the matrix by the float and returns a new reference to the matrix."""
	def __len__(self)->int:
		"""Return len(self)."""
	def __getitem__(self,index:int)->float:
		"""Return self[key]."""
	def __setitem__(self,index:int,value:float)->None:
		"""Set self[key] to value."""
	def __delitem__(self,index:int)->None:
		"""Delete self[key]."""
	def getElement(self,row:int,col:int)->float:
		"""Returns the matrix element specified by row and col . For retrieving single elements this is faster than indexing into the matrix as a sequence because it does not require the creation of an entire row tuple simply to retrieve one element from that row."""
	def setElement(self,row:int,col:int,value:float)->Self:
		"""Set the matrix element specified by row and col to the given value ."""
	def setToIdentity(self)->Self:
		"""Sets this matrix to the identity."""
	def setToProduct(self,left:MMatrix,right:MMatrix)->Self:
		"""Sets this matrix to the product of left and right ."""
	def transpose(self)->MMatrix:
		"""Returns a new matrix containing this matrix's transpose."""
	def inverse(self)->MMatrix:
		"""Returns a new matrix containing this matrix's nverse."""
	def adjoint(self)->MMatrix:
		"""Returns a new matrix containing this matrix's adjoint."""
	def homogenize(self)->MMatrix:
		"""Returns a new matrix containing the homogenized version of this matrix."""
	def det4x4(self)->float:
		"""Returns this matrix's determinant."""
	def det3x3(self)->float:
		"""Returns the determinant of the 3x3 matrix formed by the first 3 elements of the first 3 rows of this matrix."""
	def isEquivalent(self,other:MMatrix,tolerance:float=MEulerRotation.kTolerance)->bool:
		"""Inexact equality test. Returns True if each element of this matrix is within tolerance of the corresponding element of other ."""
	def isSingular(self)->bool:
		"""Returns True if this matrix is singular."""
class MMatrixArray(collections.abc.Sequence[MMatrix]):
	"""Array of MMatrix values."""
	@property
	def sizeIncrement(self)->Any:
		"""Number of elements by which to grow the array when necessary."""
	@sizeIncrement.setter
	def sizeIncrement(self,value:Any)->None:...
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def __len__(self)->int:
		"""Return len(self)."""
	def __getitem__(self,index:int)->MMatrix:
		"""Return self[key]."""
	def __setitem__(self,index:int,value:MMatrix)->None:
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
class MMeshIntersector:
	"""Provides methods for efficiently finding the closest point on
	the surface of a mesh. An octree algorithm is used to find the
	closest point.
	"""
	@property
	def isCreated(self)->Any:
		"""True if the intersector has been created, False otherwise."""
	@isCreated.setter
	def isCreated(self,value:Any)->None:...
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def create(self,mesh:Any,matrix:Any)->Self:
		"""create(mesh, matrix) -> self

		Creates the internal data required by the intersector. It is a
		compute-heavy operation and should only be called when necessary.

		mesh (MObject)   - the mesh to be used
		matrix (MMatrix) - transformation to use to bring points into the
		mesh's object space.faceIds (list) - the faces of the mesh to be passed to the intersector"""
	def getClosestPoint(self,referencePoint:Any,maxDistance:Any=sys.float_info.max)->MPointOnMesh:
		"""getClosestPoint(referencePoint, maxDistance=sys.float_info.max) -> MPointOnMesh

		Finds the closest point within 'maxDistance' of the reference point
		(MPoint) which lies on the surface of the mesh. The reference point
		will first be transformed by the matrix passed in the create() call,
		so if, for example, you want to specify reference points in world
		space then the matrix passed to create() should provide the mapping
		from world space to the mesh's object space.

		Returns an MPointOnMesh object if a closest point is found, or None
		if no closest point is found (e.g. referencePoint is not within
		maxDistance of the mesh).

		Raises ValueError if create() has not yet been called for this
		intersector."""
class MMeshIsectAccelParams:
	"""Opaque class used to store parameters used by MFnMesh's
	intersection calculations for later re-use. Use MFnMesh's
	uniformGridParams() or autoUniformGridParams() to create one
	of these to pass into the allIntersections(),
	closestIntersection(), and anyIntersection() methods"""
	def __init__(self)->None:
		"""Default constructor. Returns a new, empty MMeshIsectAccelParams object."""
class MMeshSmoothOptions:
	"""Options for control of smooth mesh generation."""
	@property
	def boundaryRule(self)->Any:
		"""Determines how boundary edges and vertices are creased."""
	@boundaryRule.setter
	def boundaryRule(self,value:Any)->None:...
	@property
	def subdivisionType(self)->Any:
		"""Determines subdivision algorithm used for mesh smoothing."""
	@subdivisionType.setter
	def subdivisionType(self,value:Any)->None:...
	@property
	def divisions(self)->Any:
		"""Number of subdivisions used in smoothing."""
	@divisions.setter
	def divisions(self,value:Any)->None:...
	@property
	def keepBorderEdge(self)->Any:
		"""If True, border edges will not be smoothed."""
	@keepBorderEdge.setter
	def keepBorderEdge(self,value:Any)->None:...
	@property
	def keepHardEdge(self)->Any:
		"""If True, hard edges will not be smoothed."""
	@keepHardEdge.setter
	def keepHardEdge(self,value:Any)->None:...
	@property
	def propEdgeHardness(self)->Any:
		"""If True, the hardness of edges in the base cage will be propagated to the edges of the smoothed mesh which derive from them."""
	@propEdgeHardness.setter
	def propEdgeHardness(self,value:Any)->None:...
	@property
	def smoothness(self)->Any:
		"""The degree of smoothness desired. Ranges from 0.0 (hard) to 1.0 (fully smoothed)."""
	@smoothness.setter
	def smoothness(self,value:Any)->None:...
	@property
	def smoothUVs(self)->Any:
		"""If True, UVs will be smoothed as well as geometry. If False, only geometry will be smoothed."""
	@smoothUVs.setter
	def smoothUVs(self,value:Any)->None:...
	kInvalid:int=-1
	kLegacy:int=0
	kCreaseAll:int=1
	kCreaseEdge:int=2
	kLast:int=3
	kInvalidSubdivision:int=-1
	kCatmullClark:int=0
	kOpenSubdivCatmullClarkUniform:int=2
	kOpenSubdivCatmullClarkAdaptive:int=3
	kLastSubdivision:int=4
	def __init__(self)->None:
		"""Default constructor. Returns a new, empty MMeshSmoothOptions object."""
class MMessage:
	"""Base class for message callbacks."""
	kDefaultAction:int=0
	kDoNotDoAction:int=1
	kDoAction:int=2
	@staticmethod
	def currentCallbackId()->int:
		"""currentCallbackId() -> id

		Returns the callback ID of the currently executing callback. If called
		outside of a callback, an invalid MCallbackId and failed status will
		be returned."""
	@staticmethod
	def nodeCallbacks(node:MObject)->ids:
		"""nodeCallbacks(node) -> ids

		Returns a list of callback IDs registered to a given node.

		 * node (MObject) - Node to query for callbacks.
		 * ids (MCallbackIdArray) - Array to store the list of callback IDs."""
	@staticmethod
	def removeCallback(id:Any)->None:
		"""removeCallback(id) -> None

		Removes the specified callback from Maya.
		This method must be called for all callbacks registered by a
		plug-in before that plug-in is unloaded.

		 * id (MCallbackId) - identifier of callback to be removed"""
	@staticmethod
	def removeCallbacks(ids:Any)->None:
		"""removeCallbacks(ids) -> None

		Removes all of the specified callbacks from Maya.
		This method must be called for all callbacks registered by a
		plug-in before that plug-in is unloaded.

		 * idList (MCallbackIdArray) - list of callbacks to be removed."""
class MModelMessage(MMessage):
	"""Class used to register callbacks for model related messages.The class also provides the following Message constants which
	describe the different types supported by the addCallback method:
	  kActiveListModified		#active selection changes
	"""
	kActiveListModified:int=0
	@staticmethod
	def addPostDuplicateNodeListCallback(function:Callable,clientData:Any|None=None)->int:
		"""addPostDuplicateNodeListCallback(function, clientData=None) -> id

		This method registers a callback that is called after a duplicate
		command is made. The callback will be called after everything is
		duplicated, and provides a list of originals and duplicates.

		 * function - callable which will be passed the clientData object
		 * clientData - User defined data passed to the callback function

		 * return: Identifier used for removing the callback."""
	@staticmethod
	def addAfterDuplicateCallback(function:Callable,clientData:Any|None=None)->int:
		"""addAfterDuplicateCallback(function, clientData=None) -> id

		This method registers a callback that is called after a duplicate
		command is made. The callback will be called after everything is
		duplicated.

		 * function - callable which will be passed the clientData object
		 * clientData - User defined data passed to the callback function

		 * return: Identifier used for removing the callback."""
	@staticmethod
	def addBeforeDuplicateCallback(function:Callable,clientData:Any|None=None)->int:
		"""addBeforeDuplicateCallback(function, clientData=None) -> id

		This method registers a callback that is called whenever a duplicate
		command is made. The callback will be called before anything is
		duplicated.

		 * function - callable which will be passed the clientData object
		 * clientData - User defined data passed to the callback function

		 * return: Identifier used for removing the callback."""
	@staticmethod
	def addCallback(message:int|Any,function:Callable,clientData:Any|None=None)->int:
		"""addCallback(message, function, clientData=None) -> id

		Adds a new callback for the specified model message.


		 * message (Message constant, see class doc for a list) - the model
		   message that will trigger the callback
		 * function - callable which will be passed the clientData object
		 * clientData - User defined data passed to the callback function

		 * return: Identifier used for removing the callback."""
	@staticmethod
	def addNodeAddedToModelCallback(dagNode:MObject,function:Callable,clientData:Any|None=None)->int:
		"""addNodeAddedToModelCallback(dagNode, function, clientData=None) -> id

		This method registers a callback that is called when a dag node is about
		to be added to the Maya model.

		 * dagNode (MObject) - Node that should acquire the callback
		 * function - callable which will be passed a MObject indicating
		   the node being added to the model and the clientData object
		 * clientData - User defined data passed to the callback function

		 * return: Identifier used for removing the callback."""
	@staticmethod
	def addNodeRemovedFromModelCallback(dagNode:MObject,function:Callable,clientData:Any|None=None)->int:
		"""addNodeRemovedFromModelCallback(dagNode, function, clientData=None) -> id

		This method registers a callback that is called when the
		specified dag node is being removed from the Maya model.

		 * dagNode (MObject) - Node that should acquire the callback
		 * function - callable which will be passed a MObject indicating
		   the node being removed to the model and the clientData object
		 * clientData - User defined data passed to the callback function

		 * return: Identifier used for removing the callback."""
class MNamespace:
	"""Access Maya namespace functionality."""
	@staticmethod
	def addNamespace(name:str,parent:str|None=None)->None:
		"""addNamespace(MString name, MString parent=None)

		Create the namespace 'name'. If the `parent' namespace is given
		the new namespace will be a child of `parent', otherwise the new
		namespace will be a child of the current namespace.
		The new namespace is added, but not made current. To make the
		new namespace be current use MNamespace.setCurrentNamespace().
		Note that adding a namespace changes the scene, so any code that calls
		this method needs to handle undo.

		     name    The new namespace to create. A qualified or unqualified
		             name may be used. If a qualified name is used and one or
		             more of the higher level namespaces do not already exist,
		             they will be created automatically. For example, if the new
		             name is 'a:b:c' and 'a' does not yet exist, then it will be
		             created automatically and 'b' automatically created beneath
		             it and finally 'c' will be created beneath 'b'.
		             If the supplied name contains invalid characters it will first
		             be modified as per the validateName() method.
		     parent  The fully qualified name of the namespace under which
		             the new one is to be created. If not provided then the
		             current namespace will be used. If the name of the new
		             namespace is absolute (i.e. begins with a colon, ':a:b:c')
		             then the 'parent' parameter will be ignored and the new namespace
		             will be created under the root namespace."""
	@staticmethod
	def validateName(name:str)->str:
		"""validateName(MString name) -> MString

		Convert the specified name to a validated name which
		contains no illegal characters.
		The leading illegal characters will be removed and
		other illegal characters will be converted to '_'.

		For example, name '@name@space@' will be converted to 'name_space_'.

		If the entire name consists solely of illegal characters,
		e.g. '123' which contains only leading digits, then the
		returned string will be empty."""
	@staticmethod
	def currentNamespace()->str:
		"""currentNamespace() -> MString

		Get the name of the current namespace. This name is returned
		as an absolute namepath (i.e. fully qualfied from the root
		namespace downwards, ':a:b:c')."""
	@staticmethod
	def setCurrentNamespace(name:str)->str:
		"""setCurrentNamespace(MString name) -> MString

		Set the specified namespace to be the current namespace. The 'name'
		parameter you specify is relative to whatever namespace is current,
		but any namespace can be specified by passing an absolute name (e.g. :a:b:c).
		Note that making a namespace current changes the scene, so any code
		that calls this method needs to handle undo.

		To make the root namespace become current, use:
		    MNamespace.setCurrentNamespace(MNamespace.rootNamespace())"""
	@staticmethod
	def getNamespaces(parentNamespace:str|None=None,recurse:bool=False)->list[str]:
		"""getNamespaces(MString parentNamespace=None, bool recurse=False) -> [MString]

		Return a list of all namespaces in the current namespace.
		Notes:
		    1)  Names returned are always absolute (e.g. :a:b:sphere).
		    2)  The list returned is just the child namespaces (and
		        descendents if `recurse' is true). It thus never contains
		        the root namespace in the list returned.

		           parentNamespace  the namespace to query.
		           recurse          optional parameter to control whether all
		                            namespaces or just top-level namespaces
		                            are returned. A value of false (the
		                            default if unspecified) causes only the
		                            top-level namespaces to be returned. If
		                            true, all namespaces will be listed."""
	@staticmethod
	def namespaceExists(name:str)->bool:
		"""namespaceExists(MString name) -> bool

		Check if a given namespace exists."""
	@staticmethod
	def parentNamespace()->str:
		"""parentNamespace() -> MString

		Get the name of the current namespace's parent. This name is returned
		as an absolute namepath (i.e. fully qualfied from the root namespace
		downwards, ':a:b'). If the root namespace is
		current, this method returns an error. """
	@staticmethod
	def removeNamespace(name:str,removeContents:bool=False)->None:
		"""removeNamespace(MString name, bool removeContents=False)

		Remove the specified namespace.
		Note that removing a namespace changes the scene, so any code
		that calls this method needs to handle undo. """
	@staticmethod
	def renameNamespace(oldName:str,newName:str,parent:str|None=None)->None:
		"""renameNamespace(MString oldName, MString newName, MString parent=None)

		Rename the specified namespace to a new name with optional parent name.
		Note that removing a namespace changes the scene, so any code
		that calls this method needs to handle undo. """
	@staticmethod
	def getNamespaceObjects(parentNamespace:str,recurse:bool=False)->MObjectArray:
		"""getNamespaceObjects(MString parentNamespace, bool recurse=False) -> MObjectArray

		Return an array of MObjects representing the object contained within
		the specified namespace. To query the current namespace, call this
		method in this way: """
	@staticmethod
	def moveNamespace(src:str,dst:str,force:bool=False)->None:
		"""moveNamespace(MString src, MString dst, bool force=False)

		Move the contents of the namespace 'src' into the namespace 'dst'.
		Note that moving namespace contents changes the scene, so any code
		that calls this method needs to handle undo.

		          src       source namespace from which objects will be moved.
		          dst       destination namespace to which objects will be moved.
		          force     optional parameter which if true forces the move
		                    even if name clashes occur, in which case nodes are
		                    renamed to ensure uniqueness. If false, the move
		                    will not happen if there are clashes. The default
		                    value is false. """
	@staticmethod
	def rootNamespace()->str:
		"""rootNamespace() -> MString

		Get the name of the root namespace. This name is an absolute
		namepath (i.e. prefixed by a ':'). """
	@staticmethod
	def relativeNames()->bool:
		"""relativeNames() -> bool

		Query Maya's current 'relative name lookup' state. Relative name
		lookup causes lookups to be relative to the current namespace.
		By default, relative name lookup in Maya is off, which causes
		name lookups to be relative to the root namespace. For example,
		if you have the object :a:b:sphere, and the current namespace is
		':a:b', in relative name lookup mode you can issue a command like

		    setAttr sphere.translateX 10;

		If relative name lookup is off, you need to specify the full
		namepath, e.g.

		    setAttr a:b:sphere.translateX 10; """
	@staticmethod
	def setRelativeNames(newState:bool)->None:
		"""setRelativeNames(bool newState)

		Set relative name lookup mode.

		Note that turning on or off relativeNames mode can change the scene,
		so any code that calls this method needs to handle undo.
		See MNamespace.relativeNames() for details on relative name lookup.

		Note: relative name lookup mode is intended for bracketing user
		code which needs to be namespace-independent. Leaving relative
		name lookup enabled outside of your specific code could cause
		functionality such as 3rd-party plugins that assume absolute
		name lookup to fail.

		   newState         true to turn on relative name lookup, false to
		                    turn it off. Maya's default setting is false. """
	@staticmethod
	def getNamespaceFromName(fullName:str)->str:
		"""getNamespaceFromName(MString fullName) -> MString

		Get namespace from a full name.
		For example, given a full name: 'a:b:c:d:ball' this method
		would return: 'a:b:c:d'. """
	@staticmethod
	def stripNamespaceFromName(fullName:str)->str:
		"""stripNamespaceFromName(MString fullName) -> MString

		Strips the namespace from a full name.
		For example, given a full name: 'a:b:c:d:ball' this method
		would return: 'ball'. """
	@staticmethod
	def makeNamepathAbsolute(fullName:str)->str:
		"""makeNamepathAbsolute(MString fullName) -> MString

		Make a namepath which is relative to the root into an absolute
		namepath. For example, given the namepath 'a:sphere' this method
		returns ':a:sphere'. It also culls out duplicate and trailing
		separators, e.g. 'a:b::c:' will return ':a:b:c'. """
class MNodeCacheDisablingInfo:
	"""Defines additional info about why the node disables Cached Playback."""
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def setCacheDisabled(self,bool:bool)->None:
		"""setCacheDisabled(bool)

		Set if the cache should be disabled because of this node."""
	def getCacheDisabled(self)->bool:
		"""getCacheDisabled() -> bool

		Return True if the cache should be disabled because of this node."""
	def setReason(self,reason:Any)->None:
		"""setReason(reason)

		Sets the reason for disabling Cached Playback."""
	def setMitigation(self,mitigation:Any)->None:
		"""setMitigation(mitigation)

		Sets the mitigation to fix the reason for disabling Cached Playback."""
	def reset(self)->None:
		"""reset()

		Resets the disabling info to an enabled state."""
class MNodeCacheSetupInfo:
	"""Defines preferences and requirements the node has for Cached Playback."""
	kWantToCacheByDefault:int=0
	kLastPreference:int=1
	kSimulationSupport:int=0
	kLastRequirement:int=1
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def getPreference(self,PreferenceFlag:Any)->bool:
		"""getPreference(PreferenceFlag) -> bool

		Get a preference flag for this node."""
	def setPreference(self,PreferenceFlag:Any,bool:bool)->None:
		"""setPreference(PreferenceFlag, bool)

		Set a preference flag for this node."""
	def getRequirement(self,RequirementFlag:Any)->bool:
		"""getRequirement(RequirementFlag) -> bool

		Get a requirement flag for this node."""
	def setRequirement(self,RequirementFlag:Any,bool:bool)->None:
		"""setRequirement(RequirementFlag, bool)

		Set a requirement flag for this node."""
class MNodeClass:
	"""A class for performing node class-level operations in the dependency graph."""
	@property
	def attributeCount(self)->int:
		"""Number of attributes the node class has. Includes extension attributes, since those are applied to the entire node class, but not dynamic attributes, since those are only applied to individual nodes."""
	@property
	def classification(self)->str:
		"""This is a string that is used in dependency nodes that are also shaders to provide more detailed type information to the rendering system."""
	@property
	def pluginName(self)->str:
		"""File path of the plug-in in which the node class is defined. The empty string is returned for Maya's built-in node types."""
	@property
	def typeId(self)->MTypeId:
		"""Type ID for the node class."""
	@property
	def typeName(self)->str:
		"""Name of the node class. This is the name that is given to the createNode command to create nodes of this type."""
	@overload
	def __init__(self,arg:Any)->None:
		"""Returns a new MNodeClass object which will operate on the named node class."""
	@overload
	def __init__(self,nodeTypeId:MTypeId)->None:
		"""Returns a new MNodeClass object which will operate on the node class having the given nodeTypeId ."""
	def addExtensionAttribute(self,attr:MObject)->Self:
		"""Adds an extension attribute to the node class. An extension attribute is a class-level attribute which has been added dynamically to a node class. Because it is added at the class level, all nodes of that class will have the given attribute, and will only store the attribute's value if it differs from the default."""
	@overload
	def attribute(self,index:int)->MObject:
		"""Returns the node class's index 'th attribute. Raises IndexError if index is out of bounds."""
	@overload
	def attribute(self,name:str)->MObject:
		"""Returns the node class's attribute having the given name . Returns MObject.kNullObj if the class does not have an attribute with that name."""
	def getAttributes(self)->MObjectArray:
		"""Returns an MObjectArray array containing all of the node class's attributes."""
	def hasAttribute(self,name:str)->bool:
		"""Returns True if the node class has an attribute of the given name , False otherwise."""
	def removeExtensionAttribute(self,attr:MObject)->Self:
		"""Removes an extension attribute from the node class. Raises ValueError if attr is not an extension attribute of this node class."""
	def removeExtensionAttributeIfUnset(self,attr:MObject)->bool:
		"""Removes an extension attribute from the node class, but only if there are no nodes in the graph with non-default values for this attribute. Returns True if the attribute was removed, False otherwise. Raises ValueError if attr is not an extension attribute of this node class."""
class MNodeMessage(MMessage):
	"""Class used to register callbacks for dependency node messages of specific dependency nodes.

	The class also provides the following AttributeMessage constants which describe
	the type of attribute changed/addedOrRemoved messages that has occurred:
	  kConnectionMade		#a connection has been made to an attribute of this node
	  kConnectionBroken	#a connection has been broken for an attribute of this node
	  kAttributeEval		#an attribute of this node has been evaluated
	  kAttributeSet		#an attribute value of this node has been set
	  kAttributeLocked		#an attribute of this node has been locked
	  kAttributeUnlocked	#an attribute of this node has been unlocked
	  kAttributeAdded		#an attribute has been added to this node
	  kAttributeRemoved	#an attribute has been removed from this node
	  kAttributeRenamed	#an attribute of this node has been renamed
	  kAttributeKeyable	#an attribute of this node has been marked keyable
	  kAttributeUnkeyable	#an attribute of this node has been marked unkeyable
	  kIncomingDirection	#the connection was coming into the node
	  kAttributeArrayAdded	#an array attribute has been added to this node
	  kAttributeArrayRemoved	#an array attribute has been removed from this node
	  kOtherPlugSet		#the otherPlug data has been set


	The class also provides the following KeyableChangeMsg constants which
	allows user to prevent attributes from becoming (un)keyable:
	  kKeyChangeInvalid
	  kMakeKeyable
	  kMakeUnkeyable
	  kKeyChangeLast
	"""
	kConnectionMade:int=1
	kConnectionBroken:int=2
	kAttributeEval:int=4
	kAttributeSet:int=8
	kAttributeLocked:int=16
	kAttributeUnlocked:int=32
	kAttributeAdded:int=64
	kAttributeRemoved:int=128
	kAttributeRenamed:int=256
	kAttributeKeyable:int=512
	kAttributeUnkeyable:int=1024
	kIncomingDirection:int=2048
	kAttributeArrayAdded:int=4096
	kAttributeArrayRemoved:int=8192
	kOtherPlugSet:int=16384
	kLast:int=32768
	kKeyChangeInvalid:int=0
	kMakeKeyable:int=1
	kMakeUnkeyable:int=2
	kKeyChangeLast:int=3
	@staticmethod
	def addAttributeAddedOrRemovedCallback(node:MObject,function:Callable,clientData:Any|None=None)->int:
		"""addAttributeAddedOrRemovedCallback(node, function, clientData=None) -> id

		Registers callbacks for attribute add/removed messages.
		This is a more specific version of addAttributeChanged as only attribute
		added and attribute removed messages will trigger the callback.

		 * node (MObject) - the node to register the callback for
		 * function - callable which will be passed an AttributeMessage constant (see
		   class doc for a list) containing the kind of attribute change triggering
		   the callback, a MObject indicating the node's plug where the connection
		   changed and the clientData object
		 * clientData - User defined data passed to the callback function

		 * return: Identifier used for removing the callback."""
	@staticmethod
	def addAttributeChangedCallback(node:MObject,function:Callable,clientData:Any|None=None)->int:
		"""addAttributeChangedCallback(node, function, clientData=None) -> id

		This method registers a callback for attribute changed messages.
		See the AttributeChanged enum for a list of all possible messages
		that will trigger the callback.

		Note: Attribute Changed messages will not be generated
		while Maya is either in playback or scrubbing modes. If you need to
		do something during playback or scrubbing you will have to register
		a callback for the timeChanged message which is the only
		message that is sent during those modes.

		The callback function will be passed the type of attribute message
		that has occurred, the plug(s) for the attributes, and any client
		data that the user wishes to pass in.

		 * node (MObject) - the node to register the callback for
		 * function - callable which will be passed an AttributeMessage constant (see
		   class doc for a list) containing the kind of attribute change triggering
		   the callback, a MObject indicating the node's plug where the connection
		   changed, a MObject indicating the plug opposite the node's plug where the
		   connection changed and the clientData object
		 * clientData - User defined data passed to the callback function

		 * return: Identifier used for removing the callback."""
	@staticmethod
	def addKeyableChangeOverride(plug:MPlug,function:Callable,clientData:Any|None=None)->int:
		"""addKeyableChangeOverride(plug, function, clientData=None) -> id

		This method registers a callback that is invoked by any class that
		changes the keyable state of an attribute.  When the callback is
		invoked, the API programmer can make a decision on how to handle
		the given keyable change event.  The programmer can either accept
		the keyable state change by returning True
		or reject it by returning False.

		Note: you can only attach one callback keyable change override
		callback per attribute.  It is an error to attach more than one
		callback to the same attribute.

		 * plug (MPlug) - The plug to which to attach the callback.
		 * function - callable which will be passed a MPlug indicating the plug that
		   has triggered the callback, the clientData object, and a KeyableChangeMsg
		   constant (see class doc for a list) containing the kind of Keyable change
		   the callback, a MObject indicating the node's plug where the connection.
		   User can return True to accept the keyable state change or False to reject it.
		 * clientData - User defined data passed to the callback function

		 * return: Identifier used for removing the callback."""
	@staticmethod
	def addNameChangedCallback(node:MObject,function:Callable,clientData:Any|None=None)->int:
		"""addNameChangedCallback(node, function, clientData=None) -> id

		Registers a callback for name changed messages.

		 * node (MObject) - the node. If this is a NULL MObject then the callback
		   applies to all node name changes.
		 * function - callable which will be passed a MObject indicating the node whose
		   name's changed, a string containing the previous name of the node and the
		   clientData object
		 * clientData - User defined data passed to the callback function

		 * return: Identifier used for removing the callback."""
	@staticmethod
	def addNodeAboutToDeleteCallback(node:MObject,function:Callable,clientData:Any|None=None)->int:
		"""addNodeAboutToDeleteCallback(node, function, clientData=None) -> id

		Registers a callback which will get called when a node is about to
		be deleted.

		The callback will be passed the MDGModifer that will be used to
		delete the node. This modifier can be used to do any DG modifications,
		such as disconnections, before the node is deleted.  These operations are
		also stored and performed when the deletion operation is undone or redone.

		The callback registered with this method will only get called when the
		deletion operation is first performed. Undos and redos will be handled solely
		through the MDGModifier which was passed to the callback on the original
		deletion. If you also wish to receive notification of deletion events
		when they are redone, you should register an additional callback using
		addNodePreRemovalCallback().

		When a node is deleted Maya automatically breaks all connections to that
		node. This process takes place after the callback has been called. This
		means that if you use the passed-in MDGModifier to break any
		connections to the node you must be sure to call the modifier's doIt() method
		before returning from the callback. Otherwise Maya will see that the connections
		still exist and try to delete them again, which can lead to errors.

		Note that it uses the passed-in MDGModifier to perform all the disconnections and
		connections. This ensures that if the deletion is undone or redone then all of
		the connections will be restored correctly.

		After it is done breaking connections, the callback calls the
		modifier's doIt() method to commit those disconnections. As noted
		above, this is necessary to ensure that Maya doesn't see the
		connections and try to break them again later on.

		 * node (MObject) - the node to register the callback for
		 * function - callable which will be passed a MObject indicating the node that
		   will be deleted, a MDGModifier indicating the DG modifier used to delete the
		   node and the clientData object
		 * clientData - User defined data passed to the callback function

		 * return: Identifier used for removing the callback."""
	@staticmethod
	def addNodeDestroyedCallback(node:MObject,function:Callable,clientData:Any|None=None)->int:
		"""addNodeDestroyedCallback(node, function, clientData=None) -> id

		Registers a callback which will get called when a node's destructor is
		called.

		 * node (MObject) - the node to register the callback for
		 * function - callable which will be passed the clientData object
		 * clientData - User defined data that will be passed to the callback
		   function

		 * return: Identifier used for removing the callback."""
	@staticmethod
	def addNodeDirtyCallback(node:MObject,function:Callable,clientData:Any|None=None)->int:
		"""addNodeDirtyCallback(node, function, clientData=None) -> id

		Registers a callback for node dirty messages.

		 * node (MObject) - the node to register the callback for
		 * function - callable which will be passed a MObject indicating the node
		   that has  become dirty and the clientData object
		 * clientData - User defined data passed to the callback function

		 * return: Identifier used for removing the callback."""
	@staticmethod
	def addNodeDirtyPlugCallback(node:MObject,function:Callable,clientData:Any|None=None)->int:
		"""addNodeDirtyPlugCallback(node, function, clientData=None) -> id

		Registers a callback for node dirty messages.  This callback provides
		the plug on the node that was dirtied.  Only provides dirty information
		on input plugs.

		 * node (MObject) - the node to register the callback for
		 * function - callable which will be passed a MObject indicating the node
		   that has  become dirty, a MPlug indicating the plug on the node that has
		   become dirty and the clientData object * clientData - User defined data passed to the callback function

		 * return: Identifier used for removing the callback."""
	@staticmethod
	def addNodePreRemovalCallback(node:MObject,function:Callable,clientData:Any|None=None)->int:
		"""addNodePreRemovalCallback(node, function, clientData=None) -> id

		Registers a callback which will get called before a node is deleted.
		This callback is called before connections on the node are removed.
		Unlike the aboutToDelete callback, this callback will be invoked whenever
		the node is deleted, even during a redo.

		Pre-removal and aboutToDelete callbacks serve different purposes.  If DG
		changes need to be made when a node is deleted, the aboutToDelete callback
		should be used to add undoable operations to an MDGModifier to perform
		these changes.  When the desired actions cannot be accomplished using the
		MDGModifier passed to the aboutToDelete callback, this callback can be
		used to receive notification of the deletion event, even during redo.

		Note that this callback method should not perform any DG operations.

		 * node (MObject) - the node to register the callback for
		 * function - callable which will be passed a MObject indicating the node
		   that is being deleted and the clientData object
		 * clientData - User defined data that will be passed to the callback
		   function

		 * return: Identifier used for removing the callback."""
	@staticmethod
	def addUuidChangedCallback(node:MObject,function:Callable,clientData:Any|None=None)->int:
		"""addUuidChangedCallback(node, function, clientData=None) -> id

		Registers a callback for UUID changed messages.

		 * node (MObject) - the node to register the callback for
		 * function - callable which will be passed a MObject indicating the node
		   that is being modified, a MUuid containing the previous UUID of the node
		   and the clientData object
		 * clientData - User defined data that will be passed to the callback
		   function

		 * return: Identifier used for removing the callback."""
class MObject:
	"""Opaque wrapper for internal Maya objects."""
	@property
	def apiTypeStr(self)->str:
		"""(readonly) String containing the object's type name."""
	__hash__:None=None
	kNullObj:MObject
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
	@overload
	def __init__(self)->None:
		"""Default constructor. Returns an empty MObject instance (i.e. one which contains kNullObj)."""
	@overload
	def __init__(self,src:MObject)->None:
		"""Copy constructor. Returns a new MObject instance which references the same internal Maya object as src , which must be another MObject instance."""
	def hasFn(self,fn:int)->bool:
		"""Returns True if the internal Maya object supports the specified function set specified by fn ."""
	def isNull(self)->bool:
		"""Returns True if the MObject is not referring to any Maya internal internal object (i.e. it is equivalent to kNullObj)."""
	def apiType(self)->int:
		"""Returns a constant indicating the type of the internal Maya object. If the MObject is null MFn.kInvalid will be returned."""
class MObjectArray(collections.abc.Sequence[MObject]):
	"""Array of MObject values."""
	@property
	def sizeIncrement(self)->Any:
		"""Number of elements by which to grow the array when necessary."""
	@sizeIncrement.setter
	def sizeIncrement(self,value:Any)->None:...
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def __len__(self)->int:
		"""Return len(self)."""
	def __getitem__(self,index:int)->MObject:
		"""Return self[key]."""
	def __setitem__(self,index:int,value:MObject)->None:
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
class MObjectHandle:
	"""Generic Class for validating MObjects."""
	def __hash__(self,*args)->Any:
		"""Return hash(self)."""
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
	def assign(self,source:MObject|MObjectHandle)->Self:
		"""assign(source) -> self

		Assigns this MObjectHandle to an instance of another MObjectHandle, or to a MObject instance.

		* source (MObject/MObjectHandle) - other instance to assign from."""
	def hashCode(self)->int:
		"""hashCode() -> int

		Returns a hash code for the internal Maya object referenced by the MObject within this MObjectHandle. If the MObject is null or no longer alive then 0 will be returned, otherwise the hash code is guaranteed to be non-zero"""
	def isAlive(self)->bool:
		"""isAlive() -> bool

		Returns the live state of the associated MObject. An object can still be 'alive' but not 'valid' (eg. a deleted object that resides in the undo queue)."""
	def isValid(self)->bool:
		"""isValid() -> bool

		Returns the validity of the associated MObject."""
	def object(self)->MObject:
		"""object() -> MObject

		Returns the MObject associated with this handle. The returned MObject will be MObject.kNullObj if the object is invalid."""
class MObjectSetMessage(MMessage):
	"""Class used to register callbacks for set modified related messages."""
	@staticmethod
	def addSetMembersModifiedCallback(node:MObject,function:Callable,clientData:Any|None=None)->int:
		"""addSetMembersModifiedCallback(node, function, clientData=None) -> id

		Registers callbacks for set modified messages.

		 * node (MObject) - the set that has triggered a setModified event
		 * function (MMessage::MNodeFunction) - the callback function
		 * function - callable which will be passed a MObject indicating the
		   set that has triggered a setModified event and the clientData object
		 * clientData - User defined data passed to the callback function

		 * return: Identifier used for removing the callback."""
class MPlane:
	"""This class describes a mathematical plane."""
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def distance(self)->float:
		"""distance() -> float

		Returns the distance of the plane along the normal."""
	def distanceToPoint(self,point:MVector,signed:bool=False)->float:
		"""distanceToPoint(point, signed=False) -> float

		Returns the distance from the plane to the specified point.

		* point (MVector) - The point from which to calculate the distance
		* signed (bool) - Whether to return a signed or unsigned distance"""
	def normal(self)->MVector:
		"""normal() -> MVector

		Returns the normal of the plane."""
	@overload
	def setPlane(self,a:float,b:float,c:float,d:float)->Self:
		"""setPlane(a, b, c, d) -> self
		setPlane(n, d) -> self

		Set the equation of the plane.

		From values : ax + by + cz + d = 0
		* a (float) - The plane equation's x coefficent
		* b (float) - The plane equation's y coefficent
		* c (float) - The plane equation's z coefficent
		* d (float) - The plane equation's constant distance term

		From a normal and offset
		* n (MVector) - The plane's normal
		* d (float) - The offset of the plane along the normal"""
	@overload
	def setPlane(self,n:MVector,d:float)->Self:
		"""setPlane(a, b, c, d) -> self
		setPlane(n, d) -> self

		Set the equation of the plane.

		From values : ax + by + cz + d = 0
		* a (float) - The plane equation's x coefficent
		* b (float) - The plane equation's y coefficent
		* c (float) - The plane equation's z coefficent
		* d (float) - The plane equation's constant distance term

		From a normal and offset
		* n (MVector) - The plane's normal
		* d (float) - The offset of the plane along the normal"""
class MPlug:
	"""Create and access dependency node plugs."""
	@property
	def info(self)->str:
		"""Description of the plug for debugging purposes, in the form node:attr1.attr2[].attr3..."""
	@property
	def isArray(self)->bool:
		"""True if plug is an array of plugs."""
	@property
	def isCaching(self)->bool:
		"""True if plug's value is being cached."""
	@isCaching.setter
	def isCaching(self,value:bool)->None:...
	@property
	def isChannelBox(self)->bool:
		"""True if plug will appear in Maya's Channel Box."""
	@isChannelBox.setter
	def isChannelBox(self,value:bool)->None:...
	@property
	def isChild(self)->bool:
		"""True if plug is a child of a compound parent."""
	@property
	def isCompound(self)->bool:
		"""True if plug is compound parent with children."""
	@property
	def isConnected(self)->bool:
		"""True if plug has any connections."""
	@property
	def isDestination(self)->bool:
		"""True if plug is the destination of a connection."""
	@property
	def isDynamic(self)->bool:
		"""True if plug is for a dynamic attribute."""
	@property
	def isElement(self)->bool:
		"""True if plug is an element of an array of plugs."""
	@property
	def isFromReferencedFile(self)->bool:
		"""True if plug is part of a connection from a referenced file."""
	@property
	def isIgnoredWhenRendering(self)->bool:
		"""True if connetions to plug are ignored during rendering."""
	@property
	def isKeyable(self)->bool:
		"""True if keys can be set on plug from Maya's UI."""
	@isKeyable.setter
	def isKeyable(self,value:bool)->None:...
	@property
	def isLocked(self)->bool:
		"""True if plug is locked against changes."""
	@isLocked.setter
	def isLocked(self,value:bool)->None:...
	@property
	def isNetworked(self)->bool:
		"""True if plug is networked."""
	@property
	def isNull(self)->bool:
		"""True if plug does not reference an attribute."""
	@property
	def isProcedural(self)->bool:
		"""True if plug is procedural."""
	@property
	def isSource(self)->bool:
		"""True if plug is the source of a connection."""
	@property
	def isProxy(self)->Any:
		"""True if plug is a proxy plug."""
	@isProxy.setter
	def isProxy(self,value:Any)->None:...
	__hash__:None=None
	kFreeToChange:int=0
	kNotFreeToChange:int=1
	kChildrenNotFreeToChange:int=2
	kAll:int=0
	kNonDefault:int=1
	kChanged:int=2
	kLastAttrSelector:int=3
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
	@overload
	def __init__(self)->None:
		"""Default constructor. Returns a new, empty MPlug object."""
	@overload
	def __init__(self,src:MPlug)->None:
		"""Copy constructor. Returns a new MPlug object referencing the same plug as src ."""
	@overload
	def __init__(self,node:MObject,attribute:MObject)->None:
		"""Returns a new plug for the given attribute of the given node ."""
	def array(self)->MPlug:
		"""Returns a plug for the array of plugs of which this plug is an element. Raises a TypeError if this plug is not an element of an array of plugs."""
	def asBool(self,context:MDGContext=MDGContext.kNormal)->bool:
		"""Retrieves the plug's value, at the time specified by the context , as a boolean."""
	def asChar(self,context:MDGContext=MDGContext.kNormal)->int:
		"""Retrieves the plug's value, at the time specified by the context , as a single-byte integer."""
	def asDouble(self,context:MDGContext=MDGContext.kNormal)->float:
		"""Retrieves the plug's value, at the time specified by the context , as a double-precision float."""
	def asFloat(self,context:MDGContext=MDGContext.kNormal)->float:
		"""Retrieves the plug's value, at the time specified by the context , as a single-precision float."""
	def asInt(self,context:MDGContext=MDGContext.kNormal)->int:
		"""Retrieves the plug's value, at the time specified by the context , as a regular integer."""
	def asMAngle(self,context:MDGContext=MDGContext.kNormal)->MAngle:
		"""Retrieves the plug's value, at the time specified by the context , as an MAngle ."""
	def asMDistance(self,context:MDGContext=MDGContext.kNormal)->MDistance:
		"""Retrieves the plug's value, at the time specified by the context , as an MDistance ."""
	def asMObject(self,context:MDGContext=MDGContext.kNormal)->MObject:
		"""Retrieves the plug's value, at the time specified by the context , and returns it as an MObject containing a direct reference to the plug's data."""
	def asMDataHandle(self,*args)->Any:
		"""Retrieve the current value of the attribute this plug references."""
	def asMTime(self,context:MDGContext=MDGContext.kNormal)->MTime:
		"""Retrieves the plug's value, at the time specified by the context , as an MTime ."""
	def asShort(self,context:MDGContext=MDGContext.kNormal)->int:
		"""Retrieves the plug's value, at the time specified by the context , as a short integer."""
	def asString(self,context:MDGContext=MDGContext.kNormal)->str:
		"""Retrieves the plug's value, at the time specified by the context , as a string."""
	def attribute(self)->MObject:
		"""Returns the attribute currently referenced by this plug."""
	@overload
	def child(self,attribute:MObject)->MPlug:
		"""Returns a plug for the specified child attribute of this plug. Raises a TypeError if this plug is not compound."""
	@overload
	def child(self,index:int)->MPlug:
		"""Returns a plug for the index 'th child of this plug. Raises a TypeError if this plug is not compound."""
	def connectedTo(self,asDest:bool,asSrc:bool)->MPlugArray:
		"""Returns an array of plugs which are connected to this one. If asDest is True connections in which this plug is the destination will be included in the array. If asSrc is True connections in which this plug is the source will be included in the array."""
	def source(self,*args)->Any:
		"""If this plug is a destination, return the source plug connected to it.
		If this plug is not a destination, a null plug is returned.
		This method will produce the networked version of the connectedplug."""
	def sourceWithConversion(self)->None:
		"""If this plug is a destination, return the source plug connected to it.
		This method is very similar to the source() method.  The only difference is that the source() method skips over any unit conversionnode connected to this destination, and returns the source of the unit conversion node.
		sourceWithConversion() does not skip over unitconversion nodes, and returns the source plug on a unit conversionnode, if present.
		Note that the behavior of connectedTo() is identical to sourceWithConversion(), that is, do not skip over unit conversion nodes."""
	def destinations(self,*args)->Any:
		"""If this plug is a source, return the destination plugs connected to it.
		If this plug is not a source, a null plug is returned.
		This method will produce the networked version of the connected plug."""
	def destinationsWithConversions(self,*args)->Any:
		"""If this plug is a source, return the destination plugs connected to it.
		This method is very similar to the destinations() method.  The only difference is that the destinations() method skips over any unit conversion node connected to this source, and returns the destination of the unit conversion node.
		destinationsWithConversionNode() does not skip over unit conversion nodes, and returns the destination plug on a unit conversion node, if present.
		Note that the behavior of connectedTo() is identical to destinationsWithConversions(), that is, do not skip over unit conversion nodes."""
	def connectionByPhysicalIndex(self,index:int)->MPlug:
		"""Returns a plug for the index 'th connected element of this plug. Raises a TypeError if this plug is not an array of plugs."""
	def constructHandle(self,block:MDataBlock)->MDataHandle:
		"""Constructs a data handle for the plug."""
	def copy(self,*args)->Any:
		"""Copies one plug to another."""
	def destructHandle(self,handle:MDataHandle)->Self:
		"""Destroys a data handle previously constructed using constructHandle() ."""
	def elementByLogicalIndex(self,index:int)->MPlug:
		"""Returns a plug for the element of this plug array having the specified logical index . Raises a TypeError if this plug is not an array of plugs."""
	def elementByPhysicalIndex(self,index:int)->MPlug:
		"""Returns a plug for the element of this plug array having the specified physical index . Raises a TypeError if this plug is not an array of plugs."""
	def evaluateNumElements(self)->int:
		"""Like numElements() but evaluates all connected elements first to ensure that they are included in the count. Raises a TypeError if the plug is not a plug array."""
	def getExistingArrayAttributeIndices(self)->MIntArray:
		"""Returns an array of all the plug's logical indices which are currently in use. Raises a TypeError if the plug is not a plug array."""
	def getSetAttrCmds(self,valueSelector:int=MDagMessage.kAll,useLongNames:bool=False)->list[str]:
		"""Returns a list of strings containing the setAttr commands (in MEL syntax) for this plug and all of its descendents."""
	def isDefaultValue(self,*args)->Any:
		"""Returns a value indicating if the plug's value is equivalent to the plug's default value."""
	def isFreeToChange(self)->int:
		"""Returns a value indicating if the plug's value can be changed, after taking into account the effects of locking and connections."""
	def logicalIndex(self)->int:
		"""Returns this plug's logical index within its parent array. Raises a TypeError if the plug is not an element of an array of plugs."""
	def name(self)->str:
		"""Returns the name of the plug."""
	def node(self)->MObject:
		"""Returns the node that this plug belongs to."""
	def numChildren(self)->int:
		"""Returns the number of children this plug has. Raises a TypeError if the plug is not compound."""
	def numConnectedChildren(self)->int:
		"""Returns the number of this plug's children which have connections. Raises a TypeError if the plug is not compound."""
	def numConnectedElements(self)->int:
		"""Returns the number of this plug's elements which have connections. Raises a TypeError if the plug is not an array of plugs."""
	def numElements(self)->int:
		"""Returns the number of the plug's logical indices which are currently in use. Connected elements which have not yet been evaluated may not yet fully exist and may be excluded from the count. Raises a TypeError if the plug is not a plug array."""
	def parent(self)->MPlug:
		"""Returns a plug for the parent of this plug. Raises a TypeError if this plug is not the child of a compound plug."""
	def partialName(self,includeNodeName:bool=False,includeNonMandatorIndices:bool=False,includeInstancedIndices:bool=False,useAlias:bool=False,useFullAttributePath:bool=False,useLongNames:bool=False)->str:
		"""Returns the name of the plug, formatted according to various criteria."""
	def selectAncestorLogicalIndex(self,index:int,attribute:MObject=MObject.kNullObj)->Self:
		"""Changes the logical index of the specified attribute in the plug's path. Raises a TypeError if the current plug is networked. or if attribute is not an array."""
	def setAttribute(self,attr:MObject)->Self:
		"""Switches the plug to reference the given attribute of the same node as the previously referenced attribute."""
	def setBool(self,value:bool)->Self:
		"""Sets the plug's value as a boolean."""
	def setChar(self,value:int)->Self:
		"""Sets the plug's value as a single-byte integer."""
	def setDouble(self,value:float)->Self:
		"""Sets the plug's value as a double-precision float."""
	def setFloat(self,value:float)->Self:
		"""Sets the plug's value as a single-precision float."""
	def setInt(self,value:int)->Self:
		"""Sets the plug's value as a regular integer."""
	def setMAngle(self,value:MAngle)->Self:
		"""Sets the plug's value as an MAngle ."""
	def setMDataHandle(self,value:MDataHandle)->Self:
		"""Sets the plug's value using a data handle."""
	def setMDistance(self,value:MDistance)->Self:
		"""Sets the plug's value as an MDistance ."""
	def setMObject(self,value:MObject)->Self:
		"""Sets the plug's value as an MObject ."""
	def proxied(self,*args)->Any:
		"""Returns the proxied plug for this plug."""
	def setMPxData(self,value:MPxData)->Self:
		"""Sets the plug's value using custom plug-in data."""
	def setMTime(self,value:MTime)->Self:
		"""Sets the plug's value as an MTime ."""
	def setNumElements(self,count:int)->Self:
		"""Pre-allocates space for count elements in an array of plugs. Raises a TypeError if the plug is not a plug array or if it already has elements."""
	def setShort(self,value:int)->Self:
		"""Sets the plug's value as a short integer."""
	def setString(self,value:str)->Self:
		"""Sets the plug's value as a string."""
	def isExactlyEqual(self,*args)->Any:
		"""Returns true if both plugs refer to the same node, attribute and multi-index. If either or both plugs are null, the plugs are not considered equal."""
class MPlugArray(collections.abc.Sequence[MPlug]):
	"""Array of MPlug values."""
	@property
	def sizeIncrement(self)->Any:
		"""Number of elements by which to grow the array when necessary."""
	@sizeIncrement.setter
	def sizeIncrement(self,value:Any)->None:...
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def __len__(self)->int:
		"""Return len(self)."""
	def __getitem__(self,index:int)->MPlug:
		"""Return self[key]."""
	def __setitem__(self,index:int,value:MPlug)->None:
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
class MPoint(collections.abc.Sequence[float]):
	"""3D point with double-precision coordinates."""
	@property
	def x(self)->float:
		"""X coordinate"""
	@x.setter
	def x(self,value:float)->None:...
	@property
	def y(self)->float:
		"""Y coordinate"""
	@y.setter
	def y(self,value:float)->None:...
	@property
	def z(self)->float:
		"""Z coordinate"""
	@z.setter
	def z(self,value:float)->None:...
	@property
	def w(self)->float:
		"""W coordinate"""
	@w.setter
	def w(self,value:float)->None:...
	__hash__:None=None
	kOrigin:MPoint
	kTolerance:float=1e-10
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
	@overload
	def __init__(self)->None:
		"""Default constructor. Returns a new MPoint object, initialized to the origin."""
	@overload
	def __init__(self,src:MPoint|MFloatPoint|MVector|MFloatVector)->None:
		"""Copy constructor. Returns a new MPoint object with its x, y, z and w coords set to the same values as src . If src is a vector then the new MPoint 's w coordinate is set to 1.0."""
	@overload
	def __init__(self,seq:Sequence[two|three|float])->None:
		"""Returns a new MPoint object whose x, y, z and w coordinates are set to the elements of seq . If the sequence contains fewer than four values w will be set to 1.0. If the sequence contains fewer than three values z will be set to 0.0."""
	@overload
	def __init__(self,x:float,y:float,z:float,w:float)->None:
		"""Returns a new MPoint object with the specified x , y , z and w coordinates."""
	def __add__(self,other:MVector)->MPoint:
		"""Addition of a vector to a point."""
	def __radd__(self,*args)->Any:
		"""Return value+self."""
	@overload
	def __sub__(self,other:MVector)->MPoint:
		"""Subtraction of a vector from a point."""
	@overload
	def __sub__(self,other:MPoint)->MVector:
		"""Vector difference between two points."""
	def __rsub__(self,other:MPoint)->MVector:
		"""Vector difference between two points."""
	@overload
	def __mul__(self,other:MMatrix)->MPoint:
		"""Post-multiplication of a point by a matrix."""
	@overload
	def __mul__(self,other:float)->MPoint:
		"""Multiplication of a point by a scalar. The scalar must be convertable to float."""
	def __rmul__(self,other:MMatrix)->MPoint:
		"""Pre-multiplication of a point by a matrix."""
	def __iadd__(self,other:MVector)->Self:
		"""In-place addition of a vector to the point. Returns a new reference to the point."""
	def __isub__(self,other:MVector)->Self:
		"""In-place subtraction of a vector from a point. Returns a new reference to the point."""
	def __imul__(self,other:MMatrix)->Self:
		"""In-place post-multiplication of a point by a matrix. Returns a new reference to the point."""
	def __truediv__(self,other:float)->MPoint:
		"""Division of a point by a scalar. The scalar must be convertable to float."""
	def __rtruediv__(self,other)->Any:
		"""Return value/self."""
	def __len__(self)->int:
		"""Return len(self)."""
	def __getitem__(self,index:int)->float:
		"""Return self[key]."""
	def __setitem__(self,index:int,value:float)->None:
		"""Set self[key] to value."""
	def __delitem__(self,index:int)->None:
		"""Delete self[key]."""
	def cartesianize(self)->Self:
		"""Converts this point to cartesian form."""
	def rationalize(self)->Self:
		"""Converts this point to rational form."""
	def homogenize(self)->Self:
		"""Converts this point to homogenous form."""
	def distanceTo(self,other:MPoint)->float:
		"""Returns the distance between this point and other ."""
	def isEquivalent(self,other:MPoint,tol:float=MEulerRotation.kTolerance)->bool:
		"""Returns True if the coordinates of this point and other are equal to within a tolerance of tol ."""
class MPointArray(collections.abc.Sequence[MPoint]):
	"""Array of MPoint values."""
	@property
	def sizeIncrement(self)->Any:
		"""Number of elements by which to grow the array when necessary."""
	@sizeIncrement.setter
	def sizeIncrement(self,value:Any)->None:...
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def __len__(self)->int:
		"""Return len(self)."""
	def __getitem__(self,index:int)->MPoint:
		"""Return self[key]."""
	def __setitem__(self,index:int,value:MPoint)->None:
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
class MPointOnMesh:
	"""This class is used to return information about a point on the
	surface of a mesh: 3D position, normal, barycentric coordinates,
	etc. The point can be anywhere on the mesh, not just at its
	vertices."""
	@property
	def barycentricCoords(self)->Any:
		"""(float, float) Tuple containing the barycentric coordinates of the
		point. If the triangle has vertices (A, B, C) then barycentric
		coordinates of (u, v) mean that the 3D position of the point is
		u*A + v*B + (1 - u - v)*C. The barycentric coordinates are
		particularly useful when interpolating attributes from one mesh to
		another."""
	@barycentricCoords.setter
	def barycentricCoords(self,value:Any)->None:...
	@property
	def face(self)->Any:
		"""(int) Mesh-global index of the face containing the point."""
	@face.setter
	def face(self,value:Any)->None:...
	@property
	def normal(self)->Any:
		"""(MFloatVector) Surface normal vector at the point."""
	@normal.setter
	def normal(self,value:Any)->None:...
	@property
	def point(self)->Any:
		"""(MFloatPoint) 3D position of the point."""
	@point.setter
	def point(self,value:Any)->None:...
	@property
	def triangle(self)->Any:
		"""(int) Face-local index of the triangle containing the point."""
	@triangle.setter
	def triangle(self,value:Any)->None:...
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
class MPolyMessage(MMessage):
	"""Class used to register callbacks for poly related messages."""
	@staticmethod
	def addPolyComponentIdChangedCallback(node:MObject,arg:tuple[wantVertIds,wantEdgeIds,wantFaceIds],function:Callable,clientData:Any|None=None)->int:
		"""addPolyComponentIdChangedCallback(node, (wantVertIds, wantEdgeIds, wantFaceIds), function, clientData=None) -> id

		This method registers a callback that should be called whenever a poly
		component id is modified.
		Currently, there are some cases where the component ids for a polygonal
		mesh can be modified without generating a callback or without generating a
		correct mapping.  These cases are outlined below.

		- Polygonal mesh has construction history enabled, and there is more than
		         one topology changing operation in the history.  In this case, the
		         callback is only called when the component ID mapping changes for the
		         most recent operation, and performs the mapping with respect to the
		         input and output meshes for this operation node.
		- Polygonal mesh has construction history enabled, and the most recent
		         topology changing operation is no longer the most recent operation.
		         In this case, no id remapping callbacks will be invoked when the
		         attributes on the operation node are changed in the history.
		- When undo is used to revert a topology changing operation, the callback
		         will not be invoked.  The MEventMessage class can be used to get
		         notification when undo is performed.


		Component id mapping should always work correctly when construction history
		is off.  It should also work correctly when construction history is on and
		only the most recent operation is permitted to be adjusted (eg. changing
		the distance parameter for a merge vertex node, when merge vertices was the
		most recent operation.)  In either case, undo will not produce a poly
		message callback.

		 * node (MObject) - the node the callback function should listen to
		 *(wantVertIds, wantEdgeIds, wantFaceIds) - tuple of 3 booleans specifying
		   what arrays should be provided to the callback function when it is
		   invoked: (vertex indices, edge indices, face indices).
		 * function - callable which will be passed a tuple and the clientData object.
		   The tuple will contain three MUintArrays which are, respectively, the vertex,
		   edge and face ids of the modified components. Only the arrays which were requested
		   when the callback was registered will contain data, the others will be empty.
		 * clientData - User defined data passed to the callback function

		 * return: Identifier used for removing the callback."""
	@staticmethod
	def addPolyTopologyChangedCallback(node:MObject,function:Callable,clientData:Any|None=None)->int:
		"""addPolyTopologyChangedCallback(node, function, clientData=None) -> id

		This method registers a callback that will be called when a node impacting
		the topology of a meshShape is modified. Because the callback is invoked
		before the mesh has evaluated, the new topology data cannot be
		queried at the time the callback is received. If you want to receive a
		callback at a time when the new mesh data can be queried, use the
		following technique:

		- Use this method to register a topology-changed callback.
		- In the topology-changed callback, add an MNodeMessage.addAttributeChangedCallback on the mesh shape.
		- In the attribute-changed callback, check the inputs for an MNodeMessage.kAttributeEval message received by the "outMesh" plug of the mesh.
		- Once you have received the eval message on that plug, the attribute-changed callback can be removed and the mesh topology can be queried.

		 * node (MObject) - the node the callback function should listen to
		 * function - callable which will be passed the clientData object
		 * clientData - User defined data passed to the callback function

		 * return: Identifier used for removing the callback."""
class MPxAttributePatternFactory:
	"""Base class for custom attribute pattern factories."""
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
class MPxCommand:
	"""Base class for custom commands."""
	@property
	def historyOn(self)->bool:
		"""Determines if construction history is on for the command."""
	@historyOn.setter
	def historyOn(self,value:bool)->None:...
	@property
	def commandString(self)->str:
		"""Command string to be echoed to the user."""
	@commandString.setter
	def commandString(self,value:str)->None:...
	kLong:int=0
	kDouble:int=1
	kString:int=2
	kNoArg:int=3
	def __init__(self)->None:
		"""Default constructor. Returns a new, empty MPxCommand object."""
	def doIt(self,args:MArgList)->None:
		"""Called by Maya to execute the command."""
	def undoIt(self)->None:
		"""Called by Maya to undo a previously executed command."""
	def redoIt(self)->None:
		"""Called by Maya to redo a previously undone command."""
	def isUndoable(self)->bool:
		"""Called by Maya to determine if the command supports undo."""
	def hasSyntax(self)->bool:
		"""Called by Maya to determine if the command provides an MSyntax object describing its syntax."""
	def syntax(self)->MSyntax:
		"""Returns the command's MSyntax object, if it has one."""
	@staticmethod
	def displayInfo(msg:str,showLineNumbers:bool=False)->None:
		"""Display an informational message."""
	@staticmethod
	def displayWarning(msg:str,showLineNumbers:bool=False)->None:
		"""Display a warning message."""
	@staticmethod
	def displayError(msg:str,showLineNumbers:bool=False)->None:
		"""Display an error message."""
	@staticmethod
	def clearResult()->None:
		"""Clears the command's result."""
	@staticmethod
	def setResult(value:bool|int|float|str|Sequence[float]|Sequence[str])->None:
		"""Set the value of the result to be returned by the command."""
	@staticmethod
	def appendToResult(value:bool|int|float|str|Sequence[float]|Sequence[str])->None:
		"""Append a value to the result to be returned by the command."""
	@staticmethod
	def currentResultType()->int:
		"""Returns the type of the current result."""
	@staticmethod
	def isCurrentResultArray()->bool:
		"""Returns True if the command's current result is an array of values."""
	@staticmethod
	def currentResult()->bool|int|float|str|list[int]|list[float]|list[str]:
		"""Returns the command's current result."""
class MPxData:
	"""Base Class for User-defined Dependency Graph Data Types."""
	kData:int=0
	kGeometryData:int=1
	kLast:int=2
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def readASCII(self,argList:MArgList,endOfTheLastParsedElement:int)->int:
		"""readASCII(argList, endOfTheLastParsedElement) -> int

		Creates Data in Data Block as specified by input from ASCII file record.
		Returns the new last argument parsed by this method.

		* argList (MArgList) - List of arguments read from ASCII record* endOfTheLastParsedElement (int) - points to last argument already parsed."""
	def readBinary(self,in_:bytearray,length:int)->int:
		"""readBinary(in, length) -> int

		Creates Data in Data Block as specified by binary data from the given stream.
		Returns the numbers of data bytes processed or -1 in case of error.

		* in (bytearray) - Input stream
		* length (int) - Length in bytes of binary data to be read."""
	def writeASCII(self)->str:
		"""writeASCII() -> string

		Encodes Data in accordance with the ASCII file format and returns as string."""
	def writeBinary(self)->bytearray:
		"""writeBinary() -> bytearray

		Encodes Data in accordance with the binary file format and returns as bytearray."""
	def copy(self,src:MPxData)->Self:
		"""copy(src) -> self

		This method initializes an instance of an MPxData derived class from another existing instance.  This method can be thought of as the second half of a copy constructor for the class.  The default constructor has already been called for the instance, and this method is used to set the private data by copying the values from an existing instance.
		This method must be implemented by the derived class.

		* src (MPxData) - The object from which to copy the private data"""
	def typeId(self)->MTypeId:
		"""typeId() -> MTypeId

		Determines the type id of the Data object.
		This method must be implemented by the derived class."""
	def name(self)->str:
		"""name() -> string

		Returns the name of the custom data type.
		This method must be implemented by the derived class."""
class MPxGeometryData(MPxData):
	"""Base Class for User-defined Dependency Graph Geometry Data Types."""
	@property
	def matrix(self)->Any:
		"""The matrix associated to MPxGeometryData."""
	@matrix.setter
	def matrix(self,value:Any)->None:...
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def deleteComponent(self,compList:MObjectArray)->bool:
		"""deleteComponent(compList) -> bool

		This method should be overridden if this data is to support component deletion. For user defined shapes (MPxSurfaceShape) which support components, this method must be overridden if component deletion is to be supported when the shape has history.

		Returns True if the deletion was successfull, False otherwise.

		* compList (MObjectArray) - a list of components that are to be deleted"""
	def deleteComponentsFromGroups(self,compList:MObjectArray,groupIdArray:Any,groupComponentArray:MObjectArray)->bool:
		"""deleteComponentsFromGroups(compList, groupIdArray, groupComponentArray) -> bool

		This method should be overridden to modify the groups that flows along with the geometry, as part of the data, based on the components being deleted. It should intelligently update the groups based on what gets deleted. The class MFnGeometryData can be used to access and modify grouping information for data.

		Returns True if the deletion was successfull, False otherwise.

		The groupIdArray and groupComponentArray should contain the updated grouping information after the deletion has occurred.

		* compList (MObjectArray) - a list of components that are to be deleted
		* groupIdArray [OUT] (MIntArray) - array of group id's
		* groupComponentArray (MObjectArray) - array of updated components, one for each group id"""
	def getMatrix(self,matrix:Any)->bool:
		"""getMatrix(matrix) -> bool

		Gets the matrix associated to MPxGeometryData and retursn True if is identity

		* matrix [OUT] (MMatrix) - the returned matrix that takes a point from local object space to world space."""
	def iterator(self,componentList:MObjectArray,component:MObject,useComponents:bool,world:bool|None=None)->MPxGeometryIterator:
		"""iterator(componentList, component, useComponents, world=None) -> MPxGeometryIterator

		Associates a control point based geometry iterator with this data.
		This method is used in conjunction with MPxSurfaceShape and should be overridden if your shape is to support maya's deformations.

		The useComponents argument specifies whether the iteration is over the given componentList or the component.

		Returns an iterator for your geometry.

		* componentList (MObjectArray) - a list of components that are to be iterated over.
		* component (MObject) - a component to be iterator over.
		* useComponents (bool) - if True then componentList is to be iterated over, otherwise the iteration is on component.
		* world (bool) - specifies whether the iteration is for world space data."""
	def smartCopy(self,srcGeom:MPxGeometryData)->Self:
		"""smartCopy(srcGeom) -> self

		This method is used in conjunction with MPxSurfaceShape classes which support maya's deformations.

		This method is used to prvoide maya with an efficient way to copy the source data into the memory of this data with as little memory allocation as possible.

		This method is not mandatory and only needs to be overridden to improve performance of deformations on shapes.

		* srcGeom (MPxGeometryData) - the data to be copied"""
	def updateCompleteVertexGroup(self,component:MObject)->bool:
		"""updateCompleteVertexGroup(component) -> bool

		This method is used in conjunction with MPxSurfaceShape classes which support maya's deformations.

		This method should make sure that complete vertex group data is up-to-date.
		If the given component is not complete (i.e. it represents all elements of your geometry) then you must mark is as complete using the methods of MFnComponent and return true if the component was updated, false if it was already complete.

		This method is used by deformers when deforming the "whole" object and not just selected components.

		Returns true if the component was updated, false if it was already complete.

		* component (MObject) - the component to test"""
class MPxGeometryIterator:
	"""Base class for user defined geometry iterators."""
	@property
	def currentPoint(self)->Any:
		"""The current index of the iteration.
		This value is used when iterating over all elements of your geometry, i.e. when there are no components specified."""
	@currentPoint.setter
	def currentPoint(self,value:Any)->None:...
	@property
	def maxPoints(self)->Any:
		"""The largest index that will be iterated over.
		This value is used when iterating over all elements of your geometry, i.e. when there are no components specified."""
	@maxPoints.setter
	def maxPoints(self,value:Any)->None:...
	def __iter__(self)->Any:
		"""Implement iter(self)."""
	def __next__(self)->Any:
		"""Implement next(self)."""
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def component(self)->MObject:
		"""component() -> MObject

		Returns a component for the current item in the iteration."""
	def geometry(self)->int|object:
		"""geometry() -> long/object

		Returns the user geometry that this iterator is iterating over."""
	def hasNormals(self)->bool:
		"""hasNormals() -> bool

		Returns whether the underlying geometry has normals."""
	def hasPoints(self)->bool:
		"""hasPoints() -> bool

		Returns whether the underlying geometry has point data."""
	def index(self)->int:
		"""index() -> int

		Returns a unique index for the current item in the iteration.
		If the iteration is over the whole geometry then this index is the same as current point. If the iteration is over some elements of the geometry specified by a component then this index is the index in your geometry."""
	def indexUnsimplified(self)->int:
		"""indexUnsimplified() -> int

		Returns a unique index for the current item in the iteration.
		Rather than being the iterator index this is the index for the actual item when simplification is skipping items. This index will be equal to index() if no simplification, otherwise it will be larger."""
	def isDone(self)->bool:
		"""isDone() -> bool

		Returns whether all the items have been traversed yet."""
	def iteratorCount(self)->int:
		"""iteratorCount() -> int

		Returns an estimate of how many items will be iterated over."""
	def next(self)->Self:
		"""next() -> self

		Advances to the next component."""
	def point(self)->MPoint:
		"""point() -> MPoint

		Returns the current component's positional data."""
	def reset(self)->Self:
		"""reset() -> self

		Resets the iterator to the start of the components so that another pass over them may be made."""
	def setObject(self,shape:MPxSurfaceShape)->Self:
		"""setObject(shape) -> self

		Optional method to set a shape object to iterate over to allow tweaking of the shape's history (input geometry).

		* shape (MPxSurfaceShape) - a user defined shape object."""
	def setPoint(self,point:MPoint)->Self:
		"""setPoint(point) -> self

		Sets the current component's positional data.

		* point (MPoint) - the new positional value to set."""
	def setPointGetNext(self,point:MPoint)->int:
		"""setPointGetNext(point) -> int

		Sets the current component's positional data, and returns the next index value.

		* point (MPoint) - the positional value to set."""
class MPxNode:
	"""Base class for user defined dependency nodes."""
	kDependNode:int=0
	kLocatorNode:int=1
	kDeformerNode:int=2
	kManipContainer:int=3
	kSurfaceShape:int=4
	kFieldNode:int=5
	kEmitterNode:int=6
	kSpringNode:int=7
	kIkSolverNode:int=8
	kHardwareShader:int=9
	kHwShaderNode:int=10
	kTransformNode:int=11
	kObjectSet:int=12
	kFluidEmitterNode:int=13
	kImagePlaneNode:int=14
	kParticleAttributeMapperNode:int=15
	kCameraSetNode:int=16
	kConstraintNode:int=17
	kManipulatorNode:int=18
	kMotionPathNode:int=19
	kClientDeviceNode:int=20
	kThreadedDeviceNode:int=21
	kAssembly:int=22
	kSkinCluster:int=23
	kGeometryFilter:int=24
	kBlendShape:int=25
	kLast:int=26
	kEvaluatedIndirectly:int=0
	kEvaluatedDirectly:int=1
	kLeaveDirty:int=2
	kPostEvaluationTypeLast:int=3
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	@staticmethod
	def addAttribute(attr:MObject)->None:
		"""addAttribute(attr) -> None

		This method adds a new attribute to a user defined node type during the type's initialization.

		This method will only work during the static initialization method of the user defined node class.  The initialization method is the one that is passed into  MFnPlugin.registerNode(). The attributes must first be created using one of the MFnAttribute classes, and can then be added using this method.

		For compound attributes, the proper way to use this method is by calling it with the parent attribute. If a compound attribute is passed, this method will add all of its children.
		NOTE: A failure will occur if you attempt to call addAttribute() on the children of a compound attribute.

		* attr (MObject) - new attribute to add."""
	@staticmethod
	def attributeAffects(whenChanges:MObject,isAffected:MObject)->None:
		"""attributeAffects(whenChanges, isAffected) -> None

		This method specifies that a particular input attribute affects a specific output attribute.  This is required to make evaluation efficient.  When an input changes, only the affected outputs will be computed. Output attributes cannot be keyable - if they are keyable, this method will fail.

		This method must be called for every attribute dependency when initializing the node's attributes.  The attributes must first be added using the MPxNode.addAttribute() method.  Failing to call this method will cause the node not to update when its inputs change. If there are no calls to this method in a node's initialization, then the compute method will never be called.

		This method will only work during the static initialization method of the user defined node class.  The initialization method is the one that is passed into MFnPlugin.registerNode().  As a result, it does not work with dynamic attributes. For an alternate solution which handles dynamic as well as non-dynamic attributes refer to MPxNode.setDependentsDirty.()

		* whenChanges (MObject) - input attribute - MObject that points to an input attribute that has already been added.
		* isAffected (MObject) - affected output attribute - MObject that points to an output attribute that has already been added."""
	def compute(self,plug:MPlug,dataBlock:Any)->Self:
		"""compute(plug, dataBlock) -> self

		This method should be overridden in user defined nodes.

		Recompute the given output based on the nodes inputs.  The plug represents the data value that needs to be recomputed, and the data block holds the storage for all of the node's attributes.

		The MDataBlock will provide smart handles for reading and writing this node's attribute values.  Only these values should be used when performing computations.

		When evaluating the dependency graph, Maya will first call the compute method for this node.  If the plug that is provided to the compute indicates that that the attribute was defined by the Maya parent node, the compute method should return None.  When this occurs, Maya will call the internal Maya node from which the user-defined node is derived to compute the plug's value. Returning any othervalue (including self) will tell Maya that this node successfully computed theplug. Raising an exception will tell Maya that this node failed at computingthe plug. Note that in most cases, Maya ignores node compute failures.

		In other words, the compute method should return None to get the Maya parent class to compute the plug. It should return self (or any other value) to indicate that the plug was computed successfully.

		This means that a user defined node does not need to be concerned with computing inherited output attributes.  However, if desired, these can be safely recomputed by this method to change the behaviour of the node.

		* plug (MPlug) - plug representing the attribute that needs to be recomputed.
		* block (MDataBlock) - data block containing storage for the node's attributes."""
	def preEvaluation(self,context:MDGContext,evalNode:Any)->None:
		"""preEvaluation(context, evalNode) -> None

		Prepare a node's internal state for threaded evaluation.

		During the evaluation graph execution each node gets a chance to reset its internal states just before being evaluated.

		This code has to be thread safe, non - blocking and work only on data owned by the node.

		The timing of this callback is at the discretion of evaluation graph dependencies and individual evaluators.This means, it should be used purely to prepare this node for evaluation and no particular order should be assumed.

		This call will most likely happen from a worker thread.

		* context (MDGContext) - Context in which the evaluation is happening.
		                         This should be respected and only internal state
		                         information pertaining to it should be modified.
		* evaluationNode (MEvaluationNode) - Evaluation node which contains
		                                     information about the dirty plugs that
		                                     are about to be evaluated for the context.
		                                     Should be only used to query information."""
	def postEvaluation(self,context:MDGContext,evalNode:Any,evalType:int)->None:
		"""postEvaluation(context, evalNode, evalType) -> None

		Clean up node's internal state after threaded evaluation.

		After the evaluation graph execution, each node gets a chance to restore / update its internal states.For example, resetting draw state.

		This code has to be thread safe, non - blocking and work only on data owned by the node.

		This call will most likely happen from a worker thread.

		* context (MDGContext) - Context in which the evaluation is happening.
		                         This should be respected and only internal state
		                         information pertaining to it should be modified.
		* evaluationNode (MEvaluationNode) - Evaluation node which contains
		                                     information about the dirty plugs the
		                                     dirty plugs that were evaluated for this
		                                     context.
		* evalType (PostEvaluationType)
		  * kEvaluatedIndirectly : The node's compute function handled evaluation.
		  * kEvaluatedDirectly   : Evaluation was performed externally and the results injected
		                           back into the node.  This would happen in situations such as
		                           extracting values from an external cache.The node needs to
		                           update any additional internal state based on the new values.
		  * kLeaveDirty          : Evaluation was performed without updating this node. Internal
		                           state should be updated to reflect that the node is dirty."""
	def getCacheSetup(self,evalNode:MEvaluationNode,disablingInfo:MNodeCacheDisablingInfo,setupInfo:Any,objectArray:Any)->None:
		"""getCacheSetup(evalNode, disablingInfo, setupInfo, objectArray) -> None

		Provide node-specific setup info for the Cached Playback system.

		This method will be called at EM partitioning time.  It works in one of two ways.
		- It can state that the node supports Cached Playback and background evaluation.  In this case it can use the cacheSetupInfo to configure preferences and requirements
		- It can state that this node cannot work with Cached Playback enabled and will  therefore cause Cached Playback to be disabled.  In this case it can use the disablingInfo to provide additional info about why Cached Playback is disabled.

		In case the answer depends on the value of attributes (for example, a node can have multiple modes, some of them working with caching and some of them not), the node can add the attributes to the monitored attribute list so they can be monitored in case the value changes.

		By default, this method states that Cached Playback is supported, but does not request to be cached by default.

		Note that regardless of the preferences expressed by a node, Caching Rules can always override the preferences from this method.  Caching Rules always have the last world.  This method simply indicates the built-in Evaluation Cache rule used by Maya's default Caching Modes that this node is to be cached.  Other rules can ignore or override this behavior.

		* evalNode (MEvaluationNode)              - This node's evaluation node, contains animated plug information
		* disablingInfo (MNodeCacheDisablingInfo) - Information about why the node disables Cached Playback to be reported to the user
		* cacheSetupInfo (MNodeCacheSetupInfo)    - Preferences and requirements this node has for Cached Playback
		* monitoredAttributes (MObjectArray)      - Attributes impacting the behavior of this method that will be monitored for change"""
	def configCache(self,evalNode:MEvaluationNode,schema:MCacheSchema)->None:
		"""configCache(evalNode, schema) -> None

		Defines the node's behavior when participating in Cached Playback.

		This method will be called at EM partitioning time, after rules evaluation.

		* evalNode (MEvaluationNode)  - This node's evaluation node, contains animated plug information
		* schema (MCacheSchema)       - Specification about what attributes to cache"""
	def transformInvalidationRange(self,plug:Any,timeRange:Any)->MTimeRange:
		"""transformInvalidationRange(plug, timeRange) -> timeRange

		Override this method to register this node as an Invalidation-Range-Transformation kernel (IRT kernel) An IRT kernel node will change the invalidation time range for its downstream nodes For example, Dynamics-solver will transform invalidation time range [a,b] to [a,+inf) And Clip-Time-Editor will send out the invalidation range for each of the clip [a,b] to ( [t0+a,t0+b] U [t1+a,t1+b] U [t2+a,t2+b] U ... )

		* source (MPlug)     - The source plug in this node where the dirty propagation comes from
		* input (MTimeRange) - The incoming invalidation range


		Returns The output invalidation range for all the dependents of plug 'source'

		WARNING: You cannot do any evaluation in this function, because it can be called in dirty-propagation
		WARNING: Do *not* call MPxNode::transformInvalidationRange from your override method
		NOTE: If a plugin node have invalidation-range-transformation *conditionally* Only transform the invalidation range when attribute 'enableIRT' is set The plugin should call MPxNode::transformInvalidationRange to signal it does not perform any IRT."""
	def hasInvalidationRangeTransformation(self)->bool:
		"""hasInvalidationRangeTransformation() -> bool

		Checks if this MPxNode derived node overrides the MPxNode::transformInvalidationRange method"""
	def connectionBroken(self,plug:MPlug,otherPlug:MPlug,asSrc:bool)->Self:
		"""connectionBroken( plug, otherPlug, asSrc) -> self

		This method gets called when connections are broken with attributes of this node.

		* plug (MPlug) - attribute on this node.
		* otherPlug (MPlug) - attribute on other node.
		* asSrc (bool) - is this plug a source of the connection."""
	def connectionMade(self,plug:MPlug,otherPlug:MPlug,asSrc:bool)->Self:
		"""connectionMade(plug, otherPlug, asSrc) -> self

		This method gets called when connections are made to attributes of this node.

		* plug (MPlug) - attribute on this node.
		* otherPlug (MPlug) - attribute on other node.
		* asSrc (bool) - is this plug a source of the connection."""
	def copyInternalData(self,node:MPxNode)->Self:
		"""copyInternalData(node) -> self

		This method is overriden by nodes that store attribute data in some internal format.

		On duplication this method is called on the duplicated node with the node being duplicated passed as the parameter.  Overriding this method gives your node a chance to duplicate any internal data you've been storing and manipulating outside of normal attribute data.

		* node (MPxNode) - the node that is being duplicated."""
	def dependsOn(self,plug:MPlug,otherPlug:MPlug)->bool|None:
		"""dependsOn( plug, otherPlug) -> bool/None

		This method may be overridden by the user defined node. It should only be required to override this on rare occasions.

		This method determines whether a specific attribute depends on another attribute.

		You should return None to specify that Maya should determines the dependency (default).

		This is mainly to define dependency of dynamic attributes, since attributeAffects does not work with dynamic attributes.

		* plug (MPlug) - attribute on this node.
		* otherPlug (MPlug) - attribute on other node."""
	def doNotWrite(self)->bool:
		"""doNotWrite() -> bool

		use this method to query the "do not write" state of this proxy node. True is returned if this node will not be saved when the maya model is written out. """
	def existWithoutInConnections(self)->bool:
		"""existWithoutInConnections() -> bool

		Determines whether or not this node can exist without input connections.

		If a node connected to this node is deleted resulting in no more input
		connections and if this flag is false, then this node will be deleted.

		Do not override this method.

		Returns true if this node can exist without input connections, false otherwise"""
	def existWithoutOutConnections(self)->bool:
		"""existWithoutOutConnections() -> bool

		Determines whether or not this node can exist without output connections.

		If a node connected to this node is deleted resulting in no more output
		connections and if this flag is false, then this node will be deleted.

		Do not override this method.

		Returns true if this node can exist without output connections, false otherwise"""
	def forceCache(self,ctx:MDGContext=...)->MDataBlock:
		"""forceCache(ctx=MDGContext::current()) -> MDataBlock

		Get the datablock for this node. If there is no datablock then one will be created.
		NOTE: This should be used only in places where fast access to the datablock outside of a compute is critical such as the transformUsing method of MPxSurfaceShape.

		* ctx (MDGContext) - The context in which the datablock will be retrieved."""
	def getFilesToArchive(self,shortName:bool=False,unresolvedName:bool=False,markCouldBeImageSequence:bool=False)->list[str]:
		"""getFilesToArchive(shortName=False, unresolvedName=False, markCouldBeImageSequence=False) -> list of strings

		Use this method to return all external files used by this node. This file list will be used by the File > Archive zip feature, maya.exe -archive and the `file -q -list` mel command.

		Only include files that exist.

		If shortName is True, return just the filename portion of the path. Otherwise, return a full path.

		If unresolvedName is True, return the path before any resolution has been done (i.e leave it as a relative path, include unexpanded environment variables,  tildes, ".."s etc). Otherwise, resolve the file     path and return an absolute path (to resolve with standard Maya path resolution, use MFileObject.resolvedFullName()).

		* shortName (bool) - If True, only add the filename of the path.
		* unresolvedName (bool) - If True, add paths before any resolution, rather than absolute paths.
		* markCouldBeImageSequence (bool) - If True, append an asterisk after any file path that could be an image sequence (note: only used by maya.exe -archive)."""
	def getInternalValue(self,plug:MPlug,dataHandle:Any)->bool:
		"""getInternalValue(plug, dataHandle) -> bool

		This method is overridden by nodes that store attribute data in some internal format.

		The internal state of attributes can be set or queried using the setInternal and internal methods of MFnAttribute.

		When internal attribute values are queried via getAttr or MPlug.getValue() this method is called.

		All internal data should respect the current context, which may be obtained from MDGContext::current()

		* plug (MPlug) - the attribute that is being queried.
		* dataHandle [OUT] (MDataHandle) - the dataHandle to store the attribute value."""
	def getInternalValueInContext(self,plug:MPlug,dataHandle:Any,ctx:MDGContext)->bool:
		"""getInternalValueInContext(plug, dataHandle, ctx) -> bool [OBSOLETE]

		This method is obsolete. Override MPxNode.getInternalValue instead.

		* plug (MPlug) - the attribute that is being queried.
		* dataHandle [OUT] (MDataHandle) - the dataHandle to store the attribute value.
		* ctx (MDGContext) - the context the method is being evaluated in."""
	@staticmethod
	def inheritAttributesFrom(parentClassName:str)->None:
		"""inheritAttributesFrom(parentClassName) -> None

		This method allows a class of plugin node to inherit all of the attributes of a second class of plugin node.

		This method will only work during the static initialization method of the user defined node class and must be called before any other attributes have been added.  The initialization method is the one that is passed into  MFnPlugin.registerNode().

		A plugin node may only inherit attributes from one other class of plugin node. Attempting to call this method multiple times within a node's initialization method will result in an error.

		Both node classes must be registered using the same MPxNode type, listed in MPxNode.type().

		* parentClassName (string) - class of node to inherit attributes from."""
	@overload
	def internalArrayCount(self,plug:MPlug)->int:
		"""internalArrayCount(plug) -> int
		internalArrayCount(plug, ctx) -> int  [OBSOLETE]

		This method is overridden by nodes that have internal array attributes which are not stored in Maya's datablock. This method is used by Maya to determine the non-sparse count of array elements during file IO. If the internal array is stored sparsely, you should return the maximum index of the array plus one. If the internal array is non-sparse then return the length of the array.

		This method does not need to be implemented for attributes that are stored in the datablock since Maya will use the datablock size.

		If this method is overridden, it should return -1 for attributes which it does not handle. Maya will use the datablock size to determine the array length when -1 is returned.

		All internal data should respect the current context, which may be obtained from MDGContext.current()

		* plug (MPlug) - the array plug.
		* ctx (MDGContext) - the context, default to MDGContext.current()."""
	@overload
	def internalArrayCount(self,plug:MPlug,ctx:MDGContext)->int:
		"""internalArrayCount(plug) -> int
		internalArrayCount(plug, ctx) -> int  [OBSOLETE]

		This method is overridden by nodes that have internal array attributes which are not stored in Maya's datablock. This method is used by Maya to determine the non-sparse count of array elements during file IO. If the internal array is stored sparsely, you should return the maximum index of the array plus one. If the internal array is non-sparse then return the length of the array.

		This method does not need to be implemented for attributes that are stored in the datablock since Maya will use the datablock size.

		If this method is overridden, it should return -1 for attributes which it does not handle. Maya will use the datablock size to determine the array length when -1 is returned.

		All internal data should respect the current context, which may be obtained from MDGContext.current()

		* plug (MPlug) - the array plug.
		* ctx (MDGContext) - the context, default to MDGContext.current()."""
	def isAbstractClass(self)->bool:
		"""isAbstractClass() -> bool

		Override this class to return True if this node is an abstract node. An abstract node can only be used as a base class.  It cannot be created using the 'createNode' command.

		It is not necessary to override this method."""
	def isPassiveOutput(self,plug:MPlug)->bool:
		"""isPassiveOutput(plug) -> bool

		This method may be overridden by the user defined node if it wants to provide output attributes which do not prevent value modifications to the destination attribute. For example, output plugs on animation curve nodes are passive. This allows the attributes driven by the animation curves to be set to new values by the user.

		* plug (MPlug) - plug representing output in question."""
	def legalConnection(self,plug:MPlug,otherPlug:MPlug,asSrc:bool)->bool|None:
		"""legalConnection(plug, otherPlug, asSrc) -> bool/None

		This method allows you to check for legal connections being made to attributes of this node.

		You should return None to specify that maya should handle this connection if you are unable to determine if it is legal.

		* plug (MPlug) - attribute on this node.
		* otherPlug (MPlug) - attribute on other node.
		* asSrc (bool) - is this plug a source of the connection."""
	def legalDisconnection(self,plug:MPlug,otherPlug:MPlug,arsSrc:Any)->bool|None:
		"""legalDisconnection(plug, otherPlug, arsSrc) -> bool/None

		This method allows you to check for legal disconnections being made to attributes of this node.

		You should return None to specify that maya should handle this disconnection if you are unable to determine if it is legal.

		* plug (MPlug) - attribute on this node.
		* otherPlug (MPlug) - attribute on other node.
		* asSrc (boool) - is this plug a source of the connection."""
	def passThroughToMany(self,plug:MPlug,plugArray:MPlugArray)->bool:
		"""passThroughToMany(plug, plugArray) -> bool

		This method is overriden by nodes that want to control the traversal behavior of some Maya search algorithms which traverse the history/future of shape nodes looking for directly related nodes. In particular, the Artisan paint code uses this method when searching for paintable nodes, and the disk cache code uses this method when searching for upstream cacheFile nodes.

		If this method is not implemented or returns False, the base class Maya implementation of this method calls passThroughToOne and returns the results of that call.

		* plug (MPlug) - the plug.
		* plugArray (MPlugArray) - the corresponding plugs."""
	def passThroughToOne(self,plug:MPlug)->plug:
		"""passThroughToOne(plug) -> plug

		This method may be overriden by nodes that have a one-to-one relationship between an input attribute and a corresponding output attribute. This method is used by Maya to perform the following capabilities:

		- When this node is deleted, the delete command will rewire the source of the input attribute to the destination of the output attribute if the source and destination are connected to nodes that are not deleted.
		- History traversal algorithms such as the bakePartialHistory command use this method to direct its traversal through a shape's construction history.
		- The base class Maya implementation of passThroughToAll will call this method if passThroughToAll returns False.

		* plug (MPlug) - the plug."""
	def postConstructor(self)->Self:
		"""postConstructor() -> self

		Internally maya creates two objects when a user defined node is created, the internal MObject and the user derived object.
		The association between the these two objects is not made until after the MPxNode constructor is called. This implies that no MPxNode member function can be called from the MPxNode constructor.
		The postConstructor will get called immediately after the constructor when it is safe to call any MPxNode member function."""
	def setDependentsDirty(self,plug:MPlug,plugArray:Any)->Self:
		"""setDependentsDirty(plug, plugArray) -> self

		This method can be overridden in user defined nodes to specify which plugs should be set dirty based upon an input plug which Maya is marking dirty. The list of plugs for Maya to mark dirty is returned by the plug array. This method handles both dynamic as well as non-dynamic plugs and is useful in the following ways:



		- Allows attributeAffects-style relationships to be handled for dynamically-added attributes. Since MPxNode.attributeAffects() can only be used with non-dynamic attributes, use of this method allows a way for all attributes of a node to affect one another, both dynamic and non-dynamic.

		- Provides more flexible relationships than what is available with MPxNode.attributeAffects(). For example, you may wish to not dirty plugs when the current frame is one. However, as the routine is called during dirty propagation, there are restrictions on what can be done within the routine, most importantly you must not cause any dependency graph computation. For details, see the IMPORTANT NOTE below.



		This method is designed to work harmoniously with MPxNode.attributeAffects() on the same node. Alternately, you can do all affects relationships within a yourNode.setDependentsDirty() implementation.

		The body of a user-implemented setDependentsDirty() implementation might look like the following example, which causes the plug called "B" to be set dirty whever plug "A" is changed, i.e. A affects B.

		* plug (MPlug) - plug which is being set dirty by Maya.
		* plugArray the programmer should add any plugs which they want to set dirty to this list."""
	def setDoNotWrite(self,bool:bool)->Self:
		"""setDoNotWrite(bool) -> self

		Use this method to mark the "do not write" state of this proxy node.  If set, this node will not be saved when the Maya model is written out.

		NOTES:
		1. Plug-in "requires" information will be written out with the model when saved.  But a subsequent reload and resave of the file will cause these to go away.
		2. If this node is a DAG and has a parent or children, the "do not write" flag of the parent or children will not be set. It is the developer's responsibility to ensure that the resulting scene file is capable of being read in without errors due to unwritten nodes. """
	def setExistWithoutInConnections(self,bool:bool)->bool:
		"""setExistWithoutInConnections(bool) -> bool

		This method specifies whether or not the node can exist without input
		connections.

		If a node connected to this node is deleted resulting in no more input
		connections and if this flag is false, then this node will be deleted.

		Do not override this method.

		* flag (bool) true if this node can exist without input connections, false otherwise"""
	def setExistWithoutOutConnections(self,bool:bool)->bool:
		"""setExistWithoutOutConnections(bool) -> bool

		This method specifies whether or not the node can exist without
		output connections.

		If a node connected to this node is deleted resulting in no more output
		connections and if this flag is false, then this node will be deleted.

		Do not override this method.

		* flag (bool) true if this node can exist without output connections, false otherwise"""
	def setInternalValue(self,plug:MPlug,dataHandle:MDataHandle)->bool:
		"""setInternalValue(plug, dataHandle) -> bool


		This method is overriden by nodes that store attribute data in some internal format.

		The internal state of attributes can be set or queried using the setInternal and internal methods of MFnAttribute.

		When internal attribute values are set via setAttr or MPlug.setValue() this method is called.

		Another use for this method is to impose attribute limits.

		All internal data should respect the current context, which may be obtained from MDGContext::current()

		* plug (MPlug) - the attribute that is being set.
		* dataHandle (MDataHandle) - the dataHandle containing the value to set."""
	def setInternalValueInContext(self,plug:MPlug,dataHandle:MDataHandle,ctx:MDGContext)->bool:
		"""setInternalValueInContext(plug, dataHandle, ctx) -> bool  [OBSOLETE]

		This method is obsolete. Override MPxNode.setInternalValue instead.

		* plug (MPlug) - the attribute that is being set.
		* dataHandle (MDataHandle) - the dataHandle containing the value to set.
		* ctx (MDGContext) - the context the method is being evaluated in."""
	def setMPSafe(self,bool:bool)->Self:
		"""setMPSafe(bool) -> self

		This method is obsolete. Override MPxNode.setSchedulingType instead.

		Set a flag to specify if a user defined shading node is safe for multi-processor rendering. For a shading node to be MP safe, it cannot access any shared global data and should only use attributes in the datablock to get input data and store output data.

		NOTE: This should be called from the postConstructor() method for shading node plug-ins only. If a shading node is non-safe, then it will only be useful during single processor rendering."""
	def shouldSave(self,plug:MPlug)->bool|None:
		"""shouldSave(plug) -> bool/None

		This method may be overridden by the user defined node.  It should only be required to override this on rare occasions.

		This method determines whether a specific attribute of this node should be written out during a file save.  The default behavior is to only write the value if it differs from the default and is not being supplied by a connection.  This behavior should be sufficient in most cases.
		This method is not called for ramp attributes since they should always be written.

		* plug (MPlug) - plug representing the attribute to be saved."""
	def thisMObject(self)->MObject:
		"""thisMObject() -> MObject

		Returns the MObject associated with this user defined node.  This makes it possible to use MFnDependencyNode or to construct plugs to this node's attributes."""
	def type(self)->int:
		"""type() -> int

		Returns the type of node that this is.  This is used to differentiate user defined nodes that are derived off different MPx base classes.

		It is not necessary to override this method.

		  kDependNode                    Custom node derived from MPxNode
		  kLocatorNode                   Custom locator derived from MPxLocatorNode
		  kDeformerNode                  Custom deformer derived from MPxDeformerNode
		  kManipContainer                Custom container derived from MPxManipContainer
		  kSurfaceShape                  Custom shape derived from MPxSurfaceShape
		  kFieldNode                     Custom field derived from MPxFieldNode
		  kEmitterNode                   Custom emitter derived from MPxEmitterNode
		  kSpringNode                    Custom spring derived from MPxSpringNode
		  kIkSolverNode                  Custom IK solver derived from MPxIkSolverNode
		  kHardwareShader                Custom shader derived from MPxHardwareShader
		  kHwShaderNode                  Custom shader derived from MPxHwShaderNode
		  kTransformNode                 Custom transform derived from MPxTransform
		  kObjectSet                     Custom set derived from MPxObjectSet
		  kFluidEmitterNode              Custom fluid emitter derived from MpxFluidEmitterNode
		  kImagePlaneNode                Custom image plane derived from MPxImagePlane
		  kParticleAttributeMapperNode   Custom particle attribute mapper derived from MPxParticleAttributeMapperNode
		  kCameraSetNode                 Custom director derived from MPxCameraSet
		  kConstraintNode                Custom constraint derived from MPxConstraint
		  kManipulatorNode               Custom manipulator derived from MPxManipulatorNode
		  kClientDeviceNode              Custom threaded device derived from MPxThreadedDeviceNode
		  kThreadedDeviceNode            Custom threaded device node
		  kAssembly                      Custom assembly derived from MPxAssembly
		  kSkinCluster                                  Custom deformer derived from MPxSkinCluster
		  kGeometryFilter                               Custom deformer derived from MPxGeometryFilter
		         kBlendShape                                    Custom deformer derived from MPxBlendShape"""
	def typeId(self)->MTypeId:
		"""typeId() -> MTypeId

		Returns the TYPEID of this node."""
	def typeName(self)->str:
		"""typeName() -> string

		Returns the type name of this node.  The type name identifies the node type to the ASCII file format"""
	def name(self)->str:
		"""name() -> string

		Returns the name of this particular instance of this class.  Each objectin the dependency graph has a name.  This name will be used by the UIand by MEL.

		It is not necessary to override this method.

		Returns the name of the node"""
	def addExternalContentForFileAttr(self,table:Any,attr:MObject)->bool:
		"""addExternalContentForFileAttr(table, attr) -> bool

		This method is a helper for derived clases implementing getExternalContent().  It augments the external content info table passed in with an entry describing external content whose location is described by the specified attribute.

		The method will not overwrite existing items, i.e. items with the same key. (attribute name).  In this context, overwriting an item means the caller has called this function twice with the same attribute, or that two separate but identically named attributes were used.  If replacing an entry is the desired effect, it is the caller's responsibility to erase the previous item first.

		* table [OUT] (MExternalContentInfoTable) - table The table in which the new entry will be added.
		* attr (MObject) - The attribute for which the plug value will be queried for a location.

		Returns True if an item was sucessfully added to the table.  False if the attribute does not describe a non-empty location, or an item with the same key was already present in the table."""
	def getExternalContent(self,table:Any)->Self:
		"""getExternalContent(table) -> self

		The table populated by this method must include the location of all the content (files) used by this node, including those that do not exist.  See MExternalContentInfoTable for details.

		Keys used to add items to this table will be the same that get passed to setExternalContent through its MExternalContentLocationTable parameter to perform a batched change of content location.

		When implementing getExternalContent, you are responsible for forwarding the call to the base class when it makes sense to do so, so that base classes  can also add their external content to the table.

		The default implementation does nothing.

		* table [OUT] (MExternalContentInfoTable) - Content information table that this method must populate."""
	def setExternalContent(self,table:Any)->Self:
		"""setExternalContent(table) -> self

		This is useful in the context of content relocation.  This will be called while the scene is being loaded to apply path changes performed externally. Consequently, interaction with the rest of the scene must be kept to a minimum.  It is however valid to call this method outside of scene loading contexts.

		The keys in the map must be the same as the ones provided by the node in getExternalContent.  The values are the new locations.

		When implementing setExternalContent, you are responsible for forwarding the call to the base class when it makes sense to do so, so that base classes  can also set their external content.

		The default implementation does nothing.

		* table Key->location table with new content locations."""
	def setExternalContentForFileAttr(self,attr:MObject,table:MExternalContentLocationTable)->bool:
		"""setExternalContentForFileAttr(attr, table) -> bool

		This method is a helper for derived clases implementing setExternalContent().  It assigns a value to a plug with the one from the table whose key is the same as the passed in attribute name.

		The method will not write to the plug if the attribute is not found in the  table.

		* attr (MObject) - The attribute of the plug we want to write to.
		* table (MExternalContentLocationTable) - A table which may hold or not the value for a given plug.

		Returns True if the plug was successfully written to. False if no entry in the table was named after the attribute or if no plug was found."""
class MPxSurfaceShape(MPxNode):
	"""Parent class of all user defined shapes."""
	@property
	def isRenderable(self)->Any:
		"""Specifies whether the shape is a renderable shape.
		Making a shape renderable allows the shape to have shading group assignments."""
	@isRenderable.setter
	def isRenderable(self,value:Any)->None:...
	kNoPointCaching:int=0
	kSavePoints:int=1
	kRestorePoints:int=2
	kUpdatePoints:int=3
	kTransformOriginalPoints:int=4
	kNormal:int=0
	kUTangent:int=1
	kVTangent:int=2
	kUVNTriad:int=3
	kMatchOk:int=0
	kMatchNone:int=1
	kMatchTooMany:int=2
	kMatchInvalidName:int=3
	kMatchInvalidAttribute:int=4
	kMatchInvalidAttributeIndex:int=5
	kMatchInvalidAttributeRange:int=6
	kMatchInvalidAttributeDim:int=7
	kObjectChanged:int=0
	kBoundingBoxChanged:int=1
	mHasHistoryOnCreate:MObject
	mControlPoints:MObject
	mControlValueX:MObject
	mControlValueY:MObject
	mControlValueZ:MObject
	nodeBoundingBox:MObject
	nodeBoundingBoxMin:MObject
	nodeBoundingBoxMinX:MObject
	nodeBoundingBoxMinY:MObject
	nodeBoundingBoxMinZ:MObject
	nodeBoundingBoxMax:MObject
	nodeBoundingBoxMaxX:MObject
	nodeBoundingBoxMaxZ:MObject
	nodeBoundingBoxSize:MObject
	nodeBoundingBoxSizeX:MObject
	nodeBoundingBoxSizeY:MObject
	nodeBoundingBoxSizeZ:MObject
	center:MObject
	boundingBoxCenterX:MObject
	boundingBoxCenterY:MObject
	boundingBoxCenterZ:MObject
	matrix:MObject
	inverseMatrix:MObject
	worldMatrix:MObject
	worldInverseMatrix:MObject
	parentMatrix:MObject
	parentInverseMatrix:MObject
	visibility:MObject
	intermediateObject:MObject
	isTemplated:MObject
	instObjGroups:MObject
	objectGroups:MObject
	objectGrpCompList:MObject
	objectGroupId:MObject
	objectGroupColor:MObject
	useObjectColor:MObject
	objectColor:MObject
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	@overload
	def acceptsGeometryIterator(self,component:MObject,writeable:bool=True,forReadOnly:bool=False)->bool:
		"""acceptsGeometryIterator(component, writeable=True, forReadOnly=False) -> bool
		acceptsGeometryIterator(writeable=True) -> boolboundingBox() -> MBoundingBox

		Returns True if the shape can supply a component iterator.
		This methods should be overridden to return True. The default is to return False.

		* component (MObject) - the component to test
		* writeable (bool) - is this component type writable by an iterator
		* forReadOnly (bool) - is this component type readable by an iterator"""
	@overload
	def acceptsGeometryIterator(self,writeable:bool=True)->Any:
		"""acceptsGeometryIterator(component, writeable=True, forReadOnly=False) -> bool
		acceptsGeometryIterator(writeable=True) -> boolboundingBox() -> MBoundingBox

		Returns True if the shape can supply a component iterator.
		This methods should be overridden to return True. The default is to return False.

		* component (MObject) - the component to test
		* writeable (bool) - is this component type writable by an iterator
		* forReadOnly (bool) - is this component type readable by an iterator"""
	def activeComponents(self)->MObjectArray:
		"""activeComponents() -> MObjectArray

		Returns a list of active (selected) components for the shape."""
	def boundingBox(self)->MBoundingBox:
		"""boundingBox() -> MBoundingBox

		This method should be overridden to return a bounding box for the shape.
		If this method is overridden, then MPxSurfaceShape.isBounded() should also be overridden to return True."""
	def cachedShapeAttr(self)->MObject:
		"""cachedShapeAttr() -> MObject

		Returns the attribute containing the shape's cached geometry, if it has one."""
	def canMakeLive(self)->bool:
		"""canMakeLive() -> bool

		This method is used by Maya to determine whether a surface can be made live. It can be overridden to return True if you wish to allow your surface to be made live. If you return True, you will also need to implement both closestPoint() overloads. The default is to return False."""
	def childChanged(self,state:int=MPxSurfaceShape.kObjectChanged)->Self:
		"""childChanged(state=kObjectChanged) -> self

		This method can be used to trigger the shape to recalculate its bounding box.

		* state (int) - the type of change that has occurred

		Valid state:
		  kObjectChanged         Object geometry changed. Internal caches need to be updated.
		  kBoundingBoxChanged    Object geometry is unchanged but its bounding box has changed.
		                         This might happen if the object was moved or an offset changed."""
	@overload
	def closestPoint(self,toThisPoint:MPoint,theClosestPoint:Any,tolerance:float=MPoint.kTolerance)->Self:
		"""closestPoint(toThisPoint, theClosestPoint, tolerance=MPoint.kTolerance) -> self
		closestPoint(raySource, rayDirection, theClosestPoint, theClosestNormal, findClosestOnMiss, tolerance=MPoint.kTolerance) -> bool

		This methods are respectively used by Maya in functions (such as select) that require closest point information from your surface and for snapping queries when your surface is live.

		For selection:
		If you've overridden canMakeLive() to return True, this method is also used by Maya for some snapping queries when your surface is live.

		* toThisPoint (MPoint) - the point to test against.
		* theClosestPoint [OUT] (MPoint) - the closest point on your surface.
		* tolerance (float) - tolerance to use in your calculations.


		For snapping:
		If you override this method, you should set theClosestPoint to the closest point on your surface intersected by the ray defined by raySource and rayDirection. You should also populate the theClosestNormal parameter with the surface normal at that intersection point.

		If no intersection is found and findClosestOnMiss is True, you should still provide a point on your surface closest to the ray defined by raySource and rayDirection. When used for live snapping, this allows the user to click and drag outside the bounds    of a live surface and still have it snap to the nearest point on it within the viewport. Note, performing a pure 3D closest point of approach test in this situation may not give the most natural result for live mesh snapping.
		To provide behavior that matches Maya, you can project your surface onto the plane defined by the ray, then perform your calculations. This will account for view perspective and give accurate live snap points along the silhouette of the surface.

		If findClosestOnMiss is False, you should not provide a point and normal when the ray misses.
		Should return True if theClosestPoint and theClosestNormal have been set, False otherwise.
		canMakeLive() must also be overridden to return True.

		* raySource (MPoint) - the origin of the ray to test against
		* rayDirection (MVector) - the direction of the ray to test against
		* theClosestPoint [OUT] (MPoint) - the closest point on your surface
		* theClosestNormal [OUT] (MVector) - the normal at the closest point on your surface
		* findClosestOnMiss (bool) - when True, you should calculate theClosestPoint and theClosestNormal even if the ray misses your surface.
		* tolerance (float) - tolerance to use in your calculations"""
	@overload
	def closestPoint(self,raySource:MPoint,rayDirection:MVector,theClosestPoint:Any,theClosestNormal:Any,findClosestOnMiss:bool,tolerance:float=MPoint.kTolerance)->bool:
		"""closestPoint(toThisPoint, theClosestPoint, tolerance=MPoint.kTolerance) -> self
		closestPoint(raySource, rayDirection, theClosestPoint, theClosestNormal, findClosestOnMiss, tolerance=MPoint.kTolerance) -> bool

		This methods are respectively used by Maya in functions (such as select) that require closest point information from your surface and for snapping queries when your surface is live.

		For selection:
		If you've overridden canMakeLive() to return True, this method is also used by Maya for some snapping queries when your surface is live.

		* toThisPoint (MPoint) - the point to test against.
		* theClosestPoint [OUT] (MPoint) - the closest point on your surface.
		* tolerance (float) - tolerance to use in your calculations.


		For snapping:
		If you override this method, you should set theClosestPoint to the closest point on your surface intersected by the ray defined by raySource and rayDirection. You should also populate the theClosestNormal parameter with the surface normal at that intersection point.

		If no intersection is found and findClosestOnMiss is True, you should still provide a point on your surface closest to the ray defined by raySource and rayDirection. When used for live snapping, this allows the user to click and drag outside the bounds    of a live surface and still have it snap to the nearest point on it within the viewport. Note, performing a pure 3D closest point of approach test in this situation may not give the most natural result for live mesh snapping.
		To provide behavior that matches Maya, you can project your surface onto the plane defined by the ray, then perform your calculations. This will account for view perspective and give accurate live snap points along the silhouette of the surface.

		If findClosestOnMiss is False, you should not provide a point and normal when the ray misses.
		Should return True if theClosestPoint and theClosestNormal have been set, False otherwise.
		canMakeLive() must also be overridden to return True.

		* raySource (MPoint) - the origin of the ray to test against
		* rayDirection (MVector) - the direction of the ray to test against
		* theClosestPoint [OUT] (MPoint) - the closest point on your surface
		* theClosestNormal [OUT] (MVector) - the normal at the closest point on your surface
		* findClosestOnMiss (bool) - when True, you should calculate theClosestPoint and theClosestNormal even if the ray misses your surface.
		* tolerance (float) - tolerance to use in your calculations"""
	def componentToPlugs(self,component:MObject,selectionList:Any)->Self:
		"""componentToPlugs(component, selectionList) -> self

		Converts the given component into a selection list of plugs.
		This method is used to associate a shapes components into the corresponding attributes (plugs) within the shape. For example, it gets called by the translate manipulator to determine which attributes should be driven by the manipulator, and by the setKeyframe command to determine where to connect animCurves for components.

		This method should be overridden if the shape supports components that can be selected and moved in Maya.

		* component (MObject) - the component to be converted
		* list (MSelectionList) - a selection list where the plug should be added"""
	def convertToTweakNodePlug(self,plug:MPlug)->bool:
		"""convertToTweakNodePlug(plug) -> bool

		Check if a tweak node is connected to this node. If it is, then reset the supplied plug to contain the controlPoints attribute on the tweak node.
		Returns True if a tweak node was found, False if the plug was unchanged

		* plug (MPlug) - plug which will be set to point to the associated tweak node plug if a tweak node is connected"""
	def createFullRenderGroup(self)->MObject:
		"""createFullRenderGroup() -> MObject

		Returns a component containing all of renderable elements in the shape.
		This method is used to create a component containing every renderable element in the object.

		This method is supposed to return non-null object only if the dag object contains renderable components. Type of the return component should is the same as the one returned by MPxSurfaceShape::renderGroupComponentType()."""
	def createFullVertexGroup(self)->MObject:
		"""createFullVertexGroup() -> MObject

		Returns a component containing all of the vertices in the shape.
		This method is used to create a component containing every vertex/CV in the object.

		This method is supposed to return non-null object only if the dag object contains vertices/CVs (control points), so derived classes that do should override this method."""
	def deleteComponents(self,componentList:MObjectArray,undoInfo:MDoubleArray)->bool:
		"""deleteComponents(componentList, undoInfo) -> bool

		Returns True if this method was successful, False otherwise.
		This method should be overridden if the shape is to support deletion of components. A list of components to be deleted will be passed in as well as an array of doubles where information about each deleted component can be stored for undo purposes. A typical use for this array is to store knot values or weights for control points that are deleted.

		* componentList (MObjectArray) - List of components to be deleted
		* undoInfo (MDoubleArray) - Values used for undo purposes"""
	def excludeAsPluginShape(self)->bool:
		"""excludeAsPluginShape() -> bool

		A Maya viewport can be set to not display "Plugin Shapes", which means shapes derived from MPxSurfaceShape. By overriding excludeAsPluginShape() to return False, you can change that behaviour so that this shape is still displayed even when the display of "Plugin Shapes" is disabled.
		The default implementation returns True.
		Returns True to have this shape obey the "Plugin Shapes" settings in the viewport's "Show" menu; False to have it ignore that setting."""
	def geometryData(self)->MObject:
		"""geometryData() -> MObject

		Returns the geometry data of the shape. The geometry data must be derived from the MPxGeometryData class.

		The data is used by Maya to add, edit and query component grouping (set) information for the shape. This set information is stored and managed by Maya's shape base class, geometryShape."""
	def geometryIteratorSetup(self,componentList:MObjectArray,components:MObject,forReadOnly:bool=False)->MPxGeometryIterator:
		"""geometryIteratorSetup(componentList, components, forReadOnly=False) -> MPxGeometryIterator

		This method should be overridden by the user to return a geometry iterator compatible with the user's geometry.
		A geometry iterator is used for iterating over the components of a shape, such as the vertices of a mesh, in a generic manner.

		The components to be iterated over are passed to this function in on of two ways, as a list of components, or as a single component.
		Only one of these arguments is used at any particular time.

		* componentList (MObjectArray) - a list of components to be iterated over
		* components (MObject) - the components to be iterated over
		* forReadOnly (bool) - specifies whether the iterator is for read-only"""
	def getComponentSelectionMask(self)->MSelectionMask:
		"""getComponentSelectionMask() -> MSelectionMask

		Returns the selection mask of the shape.
		This routine must be overridden if the shape is to support interactive component selection in Viewport 2.0 and should provide information about the selection mask of the shape component."""
	def getShapeSelectionMask(self)->MSelectionMask:
		"""getShapeSelectionMask() -> MSelectionMask

		Returns the selection mask of the shape.
		This routine must be overridden if the shape is to support interactive object selection in Viewport 2.0 and should provide information about the selection mask of the shape."""
	def getWorldMatrix(self,block:MDataBlock,instanceGeom:int)->MMatrix:
		"""getWorldMatrix(block, instanceGeom) -> MMatrix

		Returns MMatrix which takes a point from local object space to world space.

		* block (MDataBlock) - a MDataBlock
		* instanceGeom (int) - the instance this MPxSurfaceShape corresponds to"""
	def hasActiveComponents(self)->bool:
		"""hasActiveComponents() -> bool

		This method is used to determine whether or not the shape has active (selected) components."""
	def isBounded(self)->bool:
		"""isBounded() -> bool

		This method should be overridden to return True if the user supplies a bounding box routine.  Supplying a bounding box routine makes refresh and selection more efficient.
		Returns a boolean value indicating whether a bounding box routine has been supplied"""
	def localShapeInAttr(self)->MObject:
		"""localShapeInAttr() -> MObject

		Returns the attribute containing the shape's input geometry in local space.

		This method will be called by Maya to determine if the shape has construction history and must be overridden if the shape is to support deformers."""
	def localShapeOutAttr(self)->MObject:
		"""localShapeOutAttr() -> MObject

		Returns the attribute containing the shape's output geometry in local space.

		This method must be overridden if the shape is to support deformers."""
	def match(self,mask:MSelectionMask,componentList:MObjectArray)->bool:
		"""match(mask, componentList) -> bool

		This method is used to check for matches between a selection type (or mask) and a given component. If your shape has components representing attributes then this method is used to match up your components with selection masks.

		This is used by sets and deformers to make sure that the selected components fall into the "vertex only" category. This is useful when you want to make sure that only a particular component can be deformed.

		* mask (MSelectionMask) - the selection mask to test against
		* componentList (MObjectArray) - a list of components to be tested"""
	def matchComponent(self,item:MSelectionList,spec:MAttributeSpecArray,list:MSelectionList)->int:
		"""matchComponent(item, spec, list) -> int

		This method is used to convert the string representation of a component into a component object and to validate that the indices.

		This method should be overridden if the shape has components.

		* item (MSelectionList) - DAG selection item for the object being matched
		* spec (MAttributeSpecArray) - attribute specification object
		* list (MSelectionList) - list to add components to

		List of valid component match result:
		  kMatchOk                       The component was matched without error.
		  kMatchNone                     No component was matched.
		  kMatchTooMany                  Not used.
		  kMatchInvalidName              One of the names in the attribute specification was not valid.
		  kMatchInvalidAttribute         Not used.
		  kMatchInvalidAttributeIndex    The attribute specification contained an index for a non-array attribute.
		  kMatchInvalidAttributeRange    An attribute index was out of range.
		  kMatchInvalidAttributeDim      The attribute specification provided the wrong number of dimensions for an attribute."""
	def newControlPointComponent(self)->MObject:
		"""newControlPointComponent() -> MObject

		The default action of this method is to return an MFnSingleIndexedComponent (of type MFn::kMeshVertComponent) in order to support rigid skinning binds.

		This method can be overridden to support other types of components such as MFnDoubleIndexedComponent and MFnTripleIndexedComponent      and should return a new component of that type.  The types allowed are those listed in the create() method docs for each MFn*IndexedComponent."""
	def pointAtParm(self,atThisParm:MPoint,evaluatedPoint:Any)->bool:
		"""pointAtParm(atThisParm, evaluatedPoint) -> bool

		This method is used by Maya in functions (such as select) that require point at parameter values. This only makes sense for parametric surfaces such as NURBS.
		Returns True if a point was found, False otherwise

		* atThisParm (MPoint) - the parameter to check
		* evaluatedPoint [OUT] (MPoint) - the surface point"""
	def renderGroupComponentType(self)->int:
		"""renderGroupComponentType() -> int

		This method is used to return the type of renderable components for this shape. It should return a type among MFn::kMeshPolygonComponent, MFn::kSubdivFaceComponent and MFn::kSurfaceFaceComponent, which is used in the creation of per-face/patch shader assignment.

		Returns the type of renderable components for this shape.
		See MFnSet.addMember()"""
	def transformUsing(self,matrix:MMatrix,componentList:MObjectArray,cachingMode:int|None=None,pointCache:MPointArray|None=None)->Self:
		"""transformUsing(matrix, componentList, cachingMode=None, pointCache=None) -> self

		Transform the given components using the specified transformation matrix.
		This method should be overridden if the shape supports components that can be transformed using maya's move, scale, and rotate tools.

		* matrix (MMatrix) - the matrix representing the transformation that is to be applied to the components
		* componentList (MObjectArray) - a list of components to be transformed. If the list is empty, it indicates that every point in the geometry should be transformed.
		* cachingMode (int) - whether the points should be cached in the pointCache argument, or restored from the pointCache
		* pointCache (MPointArray) - used to store for undo and restore points during undo

		List of valid caching modes:
		  kNoPointCaching             No point caching.
		  kSavePoints                 Points should be saved for undo in the point cache.
		  kRestorePoints              Points should be restored from the point cache.
		  kUpdatePoints               Transform and update the points in the point cache.
		  kTransformOriginalPoints    Transform using use the original pre-transformation values stored in the pointCache."""
	def tweakUsing(self,matrix:MMatrix,componentList:MObjectArray,cachingMode:int,pointCache:MPointArray,handle:MArrayDataHandle)->Self:
		"""tweakUsing(matrix, componentList, cachingMode, pointCache, handle) -> self

		Transform the given components using the specified transformation matrix.
		This method should be overridden if the shape supports components that can be transformed using maya's move, scale, and rotate tools. This method is called when the shape has history & connected to a tweak node. The most common reason why the shape would be connected to a tweak node is if it is being deformed. When a shape is connected to a tweak node, transformations applied to the points are placed in the tweak node rather than in the shape itself.

		* matrix (MMatrix) - the matrix representing the transformation that is to be applied to the components
		* componentList (MObjectArray) - a list of components to be tranformed. If the list is empty, it indicates that every point in the geometry should be transformed.
		* cachingMode (int) - whether the points should be cached in the pointCache argument, or restored from the pointCache
		* pointCache (MPointArray) - used to store for undo and restore points during undo
		* handle (MArrayDataHandle) - array data handle where the tweaks are stored

		See transformUsing() for a list of valid caching mode"""
	def undeleteComponents(self,componentList:MObjectArray,undoInfo:MDoubleArray)->bool:
		"""undeleteComponents(componentList, undoInfo) -> bool

		This method should be overridden if the shape is to support undeletion of components. A list of components to be deleted will be passed in as well as an array of doubles where information about each deleted component is stored for undo purposes. A typical use for this array is to store knot values or weights for control points that are deleted.
		Returns True if this method was successful, False otherwise

		* componentList (MObjectArray) - List of components that were deleted
		* undoInfo (MDoubleArray) - Values used for undo purposes"""
	def vertexOffsetDirection(self,component:MObject,direction:MVectorArray,mode:int,normalize:bool)->bool:
		"""vertexOffsetDirection(component, direction, mode, normalize) -> bool

		This method should be overridden if the shape supports components that can be moved in the direction of the normal or UV's using the move vertex normal tool.

		This method should calculate the offset direction for a vertex components. The direction vector array is an array of offsets corresponding to the elements in the component. The mode argument specifies the type of movement that is being performed.

		The default for this method is to return False, i.e. no support for move normal tool.
		Returns True if the shape supports the current mode, False if the shape cannot do the requested vertex move

		* component (MObject)
		* direction (MVectorArray)
		* mode (int) - The type of vertex movement
		* normalize (bool) - specifies whether the offset vectors should be normalized

		List of valid types:
		  kNormal       Move in normal direction.
		  kUTangent     Move in u tangent direction.
		  kVTangent     Move in v tangent direction.
		  kUVNTriad     Calculate u, v, and normal offsets."""
	def weightedTransformUsing(self,xform:MTransformationMatrix,space:MMatrix,componentList:MObjectArray,cachingMode:int,pointCache:MPointArray,freezePlane:MPlane)->Self:
		"""weightedTransformUsing(xform, space, componentList, cachingMode, pointCache, freezePlane) -> self

		Transform the given components with interpolation using the specified transformation matrix.

		If not overridden, then a default implementation will be used to perform the transformation and interpolation.
		The default implementation calls setPoint() for each transformed point.

		* xform (MTransformationMatrix) - the matrix representing the transformation that is to be applied to the components.
		* space (MMatrix) - the matrix representing the transformation space to perform the interpolated transformation. A value of None indicates it should be ignored.
		* componentList (MObjectArray) - a list of components to be transformed and their weights. This list will not be empty.* cachingMode (int) - whether the points should be added/updated in the pointCache, restored from the pointCache, or transform using use the original values in the pointCache.
		* pointCache (MPointArray) - used to store for undo and restore points during undo
		* freezePlane (MPlane) - used for symmetric transformation of components. A value of None indicates it is not used and there is no symmetric transformation.

		See transformUsing() for a list of valid caching mode"""
	def weightedTweakUsing(self,xform:MTransformationMatrix,space:MMatrix,componentList:MObjectArray,cachingMode:int,pointCache:MPointArray,freezePlane:MPlane,handle:MArrayDataHandle)->Self:
		"""weightedTweakUsing(xform, space, componentList, cachingMode, pointCache, freezePlane, handle) -> self

		Transform the given components with interpolation using the specified transformation matrix.
		This method is called for transforming components using maya's move, scale, and rotate tools when the shape has history and is connected to a tweak node. The most common reason why the shape would be connected to a tweak node is if it is being deformed. When a shape is connected to a tweak node, transformations applied to the points are placed in the tweak node rather than in the shape itself.

		If not overridden, then a default implementation will be used to perform the transformation and interpolation.
		The default implementation calls setPoint() for each transformed point.

		* xform (MTransformationMatrix) - the matrix representing the transformation that is to be applied to the components
		* space (MMatrix) - the matrix representing the transformation space to perform the interpolated transformation. A value of None indicates it should be ignored.
		* componentList (MObjectArray) - a list of components to be transformed and their weights. This list will not be empty.
		* cachingMode (int) - whether the points should be added/updated in the pointCache, restored from the pointCache, or transform using the original values in the pointCache.
		* pointCache (MPointArray) - used to store for undo and restore points during undo
		* freezePlane (MPlane) - used for symmetric transformation of components. A value of None indicates it is not used and there is no symmetric transformation.
		* handle (MArrayDataHandle) - array data handle where the tweaks are stored

		See transformUsing() for a list of valid caching mode"""
	def worldShapeOutAttr(self)->MObject:
		"""worldShapeOutAttr() -> MObject

		Returns the attribute containing the shape's output geometry in world space.

		This method must be overridden if the shape is to support deformers."""
class MQuaternion(collections.abc.Sequence[float]):
	"""Quaternion math."""
	@property
	def x(self)->float:
		"""Imaginary X component"""
	@x.setter
	def x(self,value:float)->None:...
	@property
	def y(self)->float:
		"""Imaginary Y component"""
	@y.setter
	def y(self,value:float)->None:...
	@property
	def z(self)->float:
		"""Imaginary Z component"""
	@z.setter
	def z(self,value:float)->None:...
	@property
	def w(self)->float:
		"""Real component"""
	@w.setter
	def w(self,value:float)->None:...
	__hash__:None=None
	kIdentity:MQuaternion
	kTolerance:float=1e-10
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
	@overload
	def __init__(self)->None:
		"""Default constructor. Returns a new MQuaternion object, initialized to the multiplicative identity."""
	@overload
	def __init__(self,src:MQuaternion)->None:
		"""Copy constructor. Returns a new MQuaternion object with the same value as src ."""
	@overload
	def __init__(self,x:float,y:float,z:float,w:float)->None:
		"""Returns a new MQuaternion object with its imaginary components set to x , y and z and its real component set to w ."""
	@overload
	def __init__(self,seq:Sequence[float])->None:
		"""Returns a new MQuaternion object with its x, y, z, and w components set to the elements of seq ."""
	@overload
	def __init__(self,a:MVector,b:MVector,factor:float)->None:
		"""Returns a new MQuaternion which will rotate vector a into vector b , about their mutually perpendicular axis. If factor is less than 1 then it will rotate only part of the way into b . If factor is greater than 1 then it will overshoot b ."""
	@overload
	def __init__(self,angle:float,axis:MVector)->None:
		"""Returns a new MQuaternion representing a rotation of angle radians about axis ."""
	def __add__(self,other:MQuaternion)->MQuaternion:
		"""Component-by-component addition."""
	def __radd__(self,other:MQuaternion)->MQuaternion:
		"""Component-by-component addition."""
	def __sub__(self,other:MQuaternion)->MQuaternion:
		"""Component-by-component subtraction."""
	def __rsub__(self,other:MQuaternion)->MQuaternion:
		"""Component-by-component subtraction."""
	def __mul__(self,other:MQuaternion)->MQuaternion:
		"""Multiplication by another quaternion."""
	@overload
	def __rmul__(self,other:MQuaternion)->MQuaternion:
		"""Multiplication by another quaternion."""
	@overload
	def __rmul__(self,other:float)->MQuaternion:
		"""Scaling of each component by the float."""
	def __neg__(self)->Self:
		"""-self"""
	def __imul__(self,other:MQuaternion)->Self:
		"""In-place multiplication by another quaternion. Returns a reference to the left operand."""
	def __len__(self)->int:
		"""Return len(self)."""
	def __getitem__(self,index:int)->float:
		"""Return self[key]."""
	def __setitem__(self,index:int,value:float)->None:
		"""Set self[key] to value."""
	def __delitem__(self,index:int)->None:
		"""Delete self[key]."""
	@staticmethod
	def slerp(p:MQuaternion,q:MQuaternion,t:float,spin:int=0)->MQuaternion:
		"""Spherical interpolation of unit quaternions. Returns a quaternion along the shortest path (in quaternion space) between p and q , at interpolation value t . Thus a value of 0.0 will return p while a value of 1.0 will return q . spins gives the number of complete rotations about the axis which must occur when going from p to q ."""
	@staticmethod
	def squad(p:MQuaternion,a:MQuaternion,b:MQuaternion,q:MQuaternion,t:float,spin:int=0)->MQuaternion:
		"""Interpolation along a cubic curve segment in quaternion space. Returns a quaternion along the cubic curve segment which interpolates p and q , at interpolation value t . Thus a value of 0.0 will return p while a value of 1.0 will return q . The curve is C1 continuous with a and b as intermediate points. spins gives the number of complete rotations about the axis which must occur when going from p to q ."""
	@staticmethod
	def squadPt(q0:MQuaternion,q1:MQuaternion,q2:MQuaternion)->MQuaternion:
		"""Returns a new quaternion representing an intermediate point (in quaternion space) which when used with squad() will produce a C1 continuous spline."""
	def asAxisAngle(self)->tuple[MVector,float]:
		"""Returns a tuple containing an axis and angle in radians which is equivalent to the rotation represented by the quaternion."""
	def asEulerRotation(self)->MEulerRotation:
		"""Returns the quaternion as an equivalent euler rotation."""
	def asMatrix(self)->MMatrix:
		"""Returns the quaternion as an equivalent rotation matrix."""
	def conjugate(self)->MQuaternion:
		"""Returns a new quaternion containing the conjugate of this one (i.e. x, y and z components negated)."""
	def conjugateIt(self)->Self:
		"""In-place conjugation (i.e. negates the x, y and z components)."""
	def exp(self)->MQuaternion:
		"""Returns a new quaternion containing the exponent of this one."""
	def inverse(self)->MQuaternion:
		"""Returns a new quaternion containing the inverse of this one."""
	def invertIt(self)->Self:
		"""In-place inversion."""
	def isEquivalent(self,other:MQuaternion,tolerance:float=MEulerRotation.kTolerance)->bool:
		"""Returns True if the distance between the two quaternions (in quaternion space) is less than or equal to tolerance ."""
	def log(self)->MQuaternion:
		"""Returns a new quaternion containing the natural log of this one."""
	def negateIt(self)->Self:
		"""In-place negation of the x, y, z and w components."""
	def normal(self)->MQuaternion:
		"""Returns a new quaternion containing the normalized version of this one (i.e. scaled to unit length)."""
	def normalizeIt(self)->Self:
		"""In-place normalization (i.e. scales the quaternion to unit length)."""
	def setToXAxis(self,angle:float)->Self:
		"""Set the value of this quaternion to be equivalent to a rotation of angle radians about the X-axis."""
	def setToYAxis(self,angle:float)->Self:
		"""Set the value of this quaternion to be equivalent to a rotation of angle radians about the Y-axis."""
	def setToZAxis(self,angle:float)->Self:
		"""Set the value of this quaternion to be equivalent to a rotation of angle radians about the Z-axis."""
	@overload
	def setValue(self,quat:MQuaternion)->Self:
		"""Set the value of this quaternion to be the same as quat ."""
	@overload
	def setValue(self,rot:MEulerRotation)->Self:
		"""Set the value of this quaternion to be equivalent to the rotation rot ."""
	@overload
	def setValue(self,mat:MMatrix)->Self:
		"""Set the value of this quaternion to be equivalent to the rotation derived from decomposing mat ."""
	@overload
	def setValue(self,axis:MVector,angle:float)->Self:
		"""Set the value of this quaternion to be equivalent to a rotation of angle radians about axis ."""
class MRampAttribute:
	"""Functionset for creating and working with ramp attributes."""
	@property
	def isColorRamp(self)->bool:
		"""True if the attribute is a color ramp."""
	@property
	def isCurveRamp(self)->bool:
		"""True if the attribute is a curve ramp."""
	kNone:int=0
	kLinear:int=1
	kSmooth:int=2
	kSpline:int=3
	@overload
	def __init__(self)->None:
		"""Default constructor. Returns a new, empty MRampAttribute object."""
	@overload
	def __init__(self,src:MRampAttribute)->None:
		"""Copy constructor. Returns a new MRampAttribute referencing the same attribute as src ."""
	@overload
	def __init__(self,plug:MPlug)->None:
		"""Returns a new MRampAttribute referencing the same attribute as plug . Raises a TypeError if plug 's attribute is not a ramp."""
	@overload
	def __init__(self,node:MObject,attribute:MObject)->None:
		"""Returns a new MRampAttribute referencing the specified attribute of the given node . Raises a TypeError if attribute is not a ramp."""
	@staticmethod
	def createColorRamp(longName:str,shortName:str)->MObject:
		"""Creates and returns a new color ramp attribute."""
	@staticmethod
	def createCurveRamp(longName:str,shortName:str)->MObject:
		"""Creates and returns a new curve ramp attribute."""
	@staticmethod
	def createRamp(*args)->Any:
		"""Creates and returns a new color or curve ramp attribute initialized with values."""
	def addEntries(self,positions:Sequence[float],values:Sequence[float|MColor],interps:Sequence[int])->Self:
		"""Adds entries to the ramp. For a curve ramp values must be a sequence of floats, for color ramps it must be a sequence of MColors. A TypeError will be raised if the wrong type of values are supplied."""
	def deleteEntries(self,indices:Sequence[int])->Self:
		"""Removes from the ramp those entries with the specified indices . Raises a ValueError if an attempt is made to remove the last remaining entry from the ramp."""
	def getEntries(self)->tuple[indices,positions,values,interps]:
		"""Returns a tuple containing all of the entries in the ramp. The first element of the tuple is an MIntArray containing the indices . The second element is an MFloatArray containing the positions . The third element is the values , which is an MFloatArray for a curve ramp or an MColorArray for a color ramp. The fourth and final element of the tuple is an MIntArray containing the interps , which are Interpolation Type constants."""
	def getValueAtPosition(self,position:float)->float|MColor:
		"""Returns the value of the entry at the given position . The value will be a float for a curve ramp or an MColor for a color ramp."""
	def numEntries(self)->int:
		"""Returns the number of entries in the ramp."""
	def setInterpolationAtIndex(self,interp:int,index:int)->Self:
		"""Sets the interpolation of the entry at the given index ."""
	def setPositionAtIndex(self,position:float,index:int)->Self:
		"""Sets the position of the entry at the given index ."""
	def setValueAtIndex(self,value:float|MColor,index:int)->Self:
		"""Sets the value of the entry at the given index . The value must be a float for a curve ramp or an MColor for a color ramp. A TypeError will be raised if the wrong type of value is supplied."""
	def setRamp(self,*args)->Any:
		"""Set this ramp with one or multiple entries. Current entries are removed before adding the new one(s)."""
	def pack(self,*args)->Any:
		"""Change the indices numbering by re-ordering them from 0."""
	def hasIndex(self,*args)->Any:
		"""Return true if an entry is defined at this index."""
	def sort(self,*args)->Any:
		"""Sort the ramp by position. Indices are also re-ordered during sort."""
class MRichSelection:
	"""A selection list supporting soft selection and symmetry.

	The rich selection is split into two halves: the 'normal' side,
	and an optional symmetric component. Components on both sides
	can include weight data which is used to specify both the amount
	of influence and the proximity to the centre of symmetry.

	In addition to the selected objects, the rich selection also
	includes information about the axis of symmetry so that
	operations can determine how to process any symmetric selection
	(e.g. reflect transformations).

	__init__()
	Initializes a new, empty MRichSelection object.

	__init__(MRichSelection other)
	Initializes a new MRichSelection object containing the same
	items as another rich selection."""
	@overload
	def __init__(self)->None:
		"""Initializes a new, empty MRichSelection object."""
	@overload
	def __init__(self,other:MRichSelection)->None:
		"""Initializes a new MRichSelection object containing the same
		items as another rich selection."""
	def clear(self)->Self:
		"""clear() -> self


		Empties the rich selection."""
	def getRawSymmetryMatrix(self)->tuple[MMatrix,space]:
		"""getRawSymmetryMatrix() -> (MMatrix, space)

		Returns a tuple containing the raw symmetry matrix to use for the
		symmetric components of the rich selection, and the transformation
		space used by the matrix (see MSpace). The caller is responsible for
		handling any necessary transformation space conversions."""
	def getSelection(self)->MSelectionList:
		"""getSelection() -> MSelectionList

		Returns a copy of the non-symmetry component of the rich selection."""
	def getSymmetry(self)->MSelectionList:
		"""getSymmetry() -> MSelectionList

		Returns a copy of the symmetry component of the rich selection."""
	def getSymmetryMatrix(self,MDagPath:Any,space:Any)->MMatrix:
		"""getSymmetryMatrix(MDagPath, space) -> MMatrix

		Returns the symmetry matrix to use for the symmetric component of
		the specified DAG object. The matrix will already be converted to
		use the specified transformation space (see MSpace)."""
	def getSymmetryPlane(self,MDagPath:Any,space:Any)->MPlane:
		"""getSymmetryPlane(MDagPath, space) -> MPlane

		Returns the plane of symmetry, in the specified transformation space
		(see MSpace). This can be used to enforce seam weights in tools that
		support symmetry. Note that the direction of the plane carries no
		significance. Specifically, having a positive offset from the plane
		does not imply a point is part of the non-symmetric selection."""
	def setSelection(self,MSelectionList:Any)->Self:
		"""setSelection(MSelectionList) -> self

		Sets the non-symmetry component of the rich selection."""
class MSceneMessage(MMessage):
	"""Class used to register callbacks for scene related messages."""
	kSceneUpdate:int=0
	kBeforeNew:int=1
	kAfterNew:int=2
	kBeforeImport:int=3
	kAfterImport:int=4
	kBeforeOpen:int=5
	kAfterOpen:int=6
	kBeforeFileRead:int=7
	kAfterFileRead:int=8
	kAfterSceneReadAndRecordEdits:int=9
	kBeforeExport:int=10
	kAfterExport:int=11
	kBeforeSave:int=12
	kAfterSave:int=13
	kBeforeReference:int=14
	kAfterReference:int=15
	kBeforeRemoveReference:int=16
	kAfterRemoveReference:int=17
	kBeforeImportReference:int=18
	kAfterImportReference:int=19
	kBeforeExportReference:int=20
	kAfterExportReference:int=21
	kBeforeUnloadReference:int=22
	kAfterUnloadReference:int=23
	kBeforeSoftwareRender:int=24
	kAfterSoftwareRender:int=25
	kBeforeSoftwareFrameRender:int=26
	kAfterSoftwareFrameRender:int=27
	kSoftwareRenderInterrupted:int=28
	kMayaInitialized:int=29
	kMayaExiting:int=30
	kBeforeNewCheck:int=31
	kBeforeOpenCheck:int=32
	kBeforeSaveCheck:int=33
	kBeforeImportCheck:int=34
	kBeforeExportCheck:int=35
	kBeforeLoadReference:int=36
	kAfterLoadReference:int=37
	kBeforeLoadReferenceCheck:int=38
	kBeforeReferenceCheck:int=39
	kBeforeCreateReferenceCheck:int=39
	kBeforePluginLoad:int=40
	kAfterPluginLoad:int=41
	kBeforePluginUnload:int=42
	kAfterPluginUnload:int=43
	kBeforeCreateReference:int=44
	kAfterCreateReference:int=45
	kExportStarted:int=46
	kBeforeLoadReferenceAndRecordEdits:int=47
	kAfterLoadReferenceAndRecordEdits:int=48
	kBeforeCreateReferenceAndRecordEdits:int=49
	kAfterCreateReferenceAndRecordEdits:int=50
	kLast:int=51
	@staticmethod
	def addCallback(message:Any,function:Callable,clientData:Any|None=None)->int:
		"""addCallback(message, function, clientData=None) -> id

		Adds a new callback for the specified scene message.
		If a 'before' message is sent, the corresponding 'after' message
		will be as well.
		Callbacks can be added to the following Message constant with this function: kSceneUpdate
		 kBeforeNew
		 kAfterNew
		 kBeforeImport
		 kAfterImport
		 kBeforeOpen
		 kAfterOpen
		 kBeforeFileRead
		 kAfterFileRead
		 kAfterSceneReadAndRecordEdits
		 kBeforeExport
		 kExportStarted
		 kAfterExport
		 kBeforeSave
		 kAfterSave
		 kBeforeCreateReference
		 kBeforeCreateReferenceAndRecordEdits
		 kAfterCreateReference
		 kAfterCreateReferenceAndRecordEdits
		 kBeforeRemoveReference
		 kAfterRemoveReference
		 kBeforeImportReference
		 kAfterImportReference
		 kBeforeExportReference
		 kAfterExportReference
		 kBeforeUnloadReference
		 kAfterUnloadReference
		 kBeforeLoadReference
		 kBeforeLoadReferenceAndRecordEdits
		 kAfterLoadReference
		 kAfterLoadReferenceAndRecordEdits
		 kBeforeSoftwareRender
		 kAfterSoftwareRender
		 kBeforeSoftwareFrameRender
		 kAfterSoftwareFrameRender
		 kSoftwareRenderInterrupted
		 kMayaInitialized
		 kMayaExiting

		Note that for referencing, the creation of the reference (i.e. creation of
		the reference node and associated structures) is separate from the loading
		of the reference itself (i.e. read the nodes from file).

		The kBeforeCreateReference message will be sent when a reference is created.
		So it will happen for both loaded and unloaded references. But the
		kBeforeLoadReference message will only be sent when the file is read from disk.

		When opening a file with a loaded reference, the callback order is as follows:
		 kBeforeCreateReference
		 kBeforeCreateReferenceAndRecordEdits
		 kBeforeCreateReferenceAndRecordEdits
		 kAfterCreateReferenceAndRecordEdits

		 kBeforeLoadReference
		 kBeforeLoadReferenceAndRecordEdits
		 kAfterLoadReference
		 kAfterLoadReferenceAndRecordEdits

		By default, edits to referenced objects will not be recorded during the execution
		of file I/O callbacks. A specific set of callbacks are provided that will enable
		the recording of reference edits during their execution as follows:
		 kAfterSceneReadAndRecordEdits
		 kBeforeCreateReferenceAndRecordEdits
		 kAfterCreateReferenceAndRecordEdits
		 kBeforeLoadReferenceAndRecordEdits
		 kAfterLoadReferenceAndRecordEdits

		The kExportStarted callback is sent after the kBeforeExport callback, once Maya
		has actually started to process the exported data. One important difference between
		the two callbacks is that the fileInfo command affects the exported scene when used
		in the kExportStarted callback, but affects the current scene in memory when used
		in the kBeforeExport callback.

		 * message - the Message constant that will trigger the callback
		 * function - callable which will be passed the clientData object
		 * clientData - user data that will be passed to the callback function"""
	@staticmethod
	def addCheckCallback(message:Any,function:Callable,clientData:Any|None=None)->int:
		"""addCheckCallback(message, function, clientData=None) -> id

		This function adds a new callback for the specified scene message.
		The callback will have the ability to abort the current operation
		by returning False.

		Callbacks can be added to the following messages with this function:
		 kBeforeNewCheck
		 kBeforeImportCheck
		 kBeforeOpenCheck
		 kBeforeExportCheck
		 kBeforeSaveCheck
		 kBeforeCreateReferenceCheck
		 kBeforeLoadReferenceCheck

		 * message - the scene message that will trigger the callback
		 * function - callable which will be passed the clientData object,
		   return False to abort the current operation.
		 * clientData - user data that will be passed to the callback function

		 * return: Identifier used for removing the callback."""
	@staticmethod
	def addCheckFileCallback(message:Any,function:Callable,clientData:Any|None=None)->int:
		"""addCheckFileCallback(message, function, clientData=None) -> id

		This function adds a new callback for the specified scene message. This
		callback has the option to abort the current operation by returning
		False. The file parameter stores the target file for the current
		file IO operation, by modifying this file parameter the target file
		will be changed as well.

		Callbacks can be added to the following messages with this function:
		 kBeforeImportCheck
		 kBeforeOpenCheck
		 kBeforeExportCheck
		 kBeforeCreateReferenceCheck
		 kBeforeLoadReferenceCheck

		 * message - the scene message that will trigger the callback
		 * function - callable which will be passed a MFileObject indicating the
		   file object that will be acted on by the current file IO operation, any
		   modifications to it will be passed back to Maya and change the file being
		   acted on, and the clientData object.
		   return False to abort the current operation.
		 * clientData - User defined data passed to the callback function

		 * return: Identifier used for removing the callback."""
	@staticmethod
	def addCheckReferenceCallback(message:Any,function:Callable,clientData:Any|None=None)->int:
		"""addCheckReferenceCallback(message, function, clientData=None) -> id

		This function adds a new callback for the specified scene message.
		The callback will have the ability to abort the current operation
		by returning False.

		Callbacks can be added to the following Message constant with this function:
		 BeforeLoadReferenceCheck

		 * message - the scene Message constant that will trigger the callback
		 * function - callable which will be passed a MObject indicating the
		   reference node, a MFileObject indicating the resolved file path of the
		   referenced file, and the clientData object
		   return False to abort the current operation
		 * clientData - User defined data passed to the callback function

		 * return: Identifier used for removing the callback."""
	@staticmethod
	def addConnectionFailedCallback(function:Callable,clientData:Any|None=None)->int:
		"""addConnectionFailedCallback(function, clientData=None) -> id

		This method registers a callback that is called when a connection was
		unable to be made.
		Currently, the callback is only triggered during the reading of files (.ma or .mb)
		or of edits files (.editMA or .editMB files created by Maya's offline file support).
		The most common reasons why a connection would fail are:
		- inability to find the specified node or attribute names, or
		- a conflicting existing connection

		 * function - callable which will be passed a MPlug indicating the
		   source plug of the connection (or None if it could not be found),
		   a MPlug indicating destination plug of the connection (or None if
		   it could not be found), a string containing the name used to look up
		   the source plug, a string containing the name used to look up the
		   destination plug and the clientData object.
		 * clientData - User defined data passed to the callback function

		 * return: Identifier used for removing the callback."""
	@staticmethod
	def addNamespaceRenamedCallback(function:Callable,clientData:Any|None=None)->int:
		"""addNamespaceRenamedCallback(function, clientData=None) -> id

		This method registers a callback that is called when a namespace is renamed.


		 * function - callable which will be passed a string containing the new
		   name of namespace that was changed, a string containing the old name of
		   namespace that was changed and the clientData object.
		 * clientData - User defined data passed to the callback function

		 * return: Identifier used for removing the callback."""
	@staticmethod
	def addReferenceCallback(message:Any,function:Callable,clientData:Any|None=None)->int:
		"""addReferenceCallback(message, function, clientData=None) -> id

		This function adds a new callback for the specified scene message.

		Callbacks can be added to the following messages with this function:
		 kBeforeRemoveReference
		 kBeforeImportReference
		 kBeforeUnloadReference
		 kAfterUnloadReference
		 kBeforeLoadReference
		 kAfterLoadReference
		 kAfterCreateReference
		 kAfterCreateReferenceAndRecordEdits
		 kBeforeLoadReferenceAndRecordEdits
		 kAfterLoadReferenceAndRecordEdits

		 * message - the scene Message constant that will trigger the callback
		 * function - callable which will be passed a MObject indicating the
		   reference node, a MFileObject indicating he resolved file path of the
		   referenced file and the clientData object.
		 * clientData - User defined data passed to the callback function

		 * return: Identifier used for removing the callback."""
	@staticmethod
	def addStringArrayCallback(message:Any,function:Callable,clientData:Any|None=None)->int:
		"""addStringArrayCallback(message, function, clientData=None) -> id

		Adds a new callback which takes a string array argument, in addition to
		the usual clientData.

		The Message constants which can be used with this method and the contents
		of the string array passed to their callbacks are as follows:
		 kBeforePluginLoad - path to plug-in file
		 kAfterPluginLoad - path to plug-in file, name of plug-in
		 kBeforePluginUnload - name of plug-in
		 kAfterPluginUnload - name of plug-in, path to plug-in file

		        To allow for future expansion callbacks should not rely on the number
		of array elements being exactly as given above. While there will not
		be fewer elements than given above, there may in future be more.

		 * message - the scene Message constant that will trigger the callback
		 * function - callable which will be passed a list of strings and the
		   clientData object.
		 * clientData - User defined data passed to the callback function

		 * return: Identifier used for removing the callback."""
class MSelectionList:
	"""A heterogenous list of MObjects, MPlugs and MDagPaths.

	__init__()
	Initializes a new, empty MSelectionList object.

	__init__(MSelectionList other)
	Initializes a new MSelectionList object containing the same
	items as another list."""
	kMergeNormal:int=0
	kXORWithList:int=1
	kRemoveFromList:int=2
	@overload
	def __init__(self)->None:
		"""Default constructor. Returns a new, empty MSelectionList object."""
	@overload
	def __init__(self,src:MSelectionList)->None:
		"""Copy constructor. Returns a new MSelectionList with the same contents as src ."""
	@overload
	def add(self,pattern:str,searchChildNamespaces:bool=False)->Self:
		"""Adds to the list any nodes, DAG paths, components or plugs which match the given pattern ."""
	@overload
	def add(self,item:MObject|MDagPath|MPlug|tuple[MDagPath|MObject,...],mergeWithExisting:bool=True)->Self:
		"""Adds a node, DAG path, plug or component to the end of the selection list. A component is passed as a tuple containing the MDagPath of the DAG node and an MObject containing the component. If mergeWithExisting is True and the item is already on the list then those existing instances of the item will be removed, leaving just the newly added instance at the end of the list. For components this applies at the component element level, meaning that any overlapping elements will be removed from the existing components. If mergeWithExisting is False then the new item is added to the end of the list without affecting any existing instances of the item already on the list."""
	def clear(self)->Self:
		"""Empties the selection list."""
	def copy(self,src:MSelectionList)->Self:
		"""Replaces the contents of the selection list with a copy of those from src ."""
	def getComponent(self,index:int)->tuple[MDagPath,MObject]:
		"""Returns the index 'th item of the list as a component, represented by a tuple containing the item's MDagPath and an MObject containing its component. If the item is just a DAG path without a component then MObject.kNullObj will be returned in the second element of the tuple. Raises TypeError if the item is neither a DAG path nor a component. Raises IndexError if index is out of range."""
	def getDagPath(self,index:int)->MDagPath:
		"""Returns the DAG path associated with the index'th item of the list. Raises TypeError if the item is neither a DAG path nor a component. Raises IndexError if index is out of range. Release Note : In Maya 2012 Gold this method returned a tuple containing both the DAG path and the component. In Maya 2012 HotFix 1 that functionality is supplied by the getComponent() method and this method returns only the DAG path. Existing code which uses this method will have to be modified accordingly."""
	def getDependNode(self,index:int)->MObject:
		"""Returns the node associated with the index 'the item, whether it be a dependency node, DAG path, component or plug. Raises IndexError if index is out of range."""
	def getPlug(self,index:int)->MPlug:
		"""Returns the index 'th item of the list as a plug. Raises TypeError if the item is not a plug. Raises IndexError if index is out of range."""
	def getSelectionStrings(self,index:int|None=None)->tuple[str,...]:
		"""Returns a tuple containing the string representation of the specified item. For nodes, DAG paths, plugs and contiguous components the tuple will only contain a single string, but for non-contiguous components there will be a separate string for each distinct block of contiguous elements. If index is not specified then the string representations of all the items in the selection list are returned. Raises IndexError if index is out of bounds."""
	def hasItem(self,item:MObject|MDagPath|MPlug|tuple[MDagPath|MObject,...])->bool:
		"""Returns True if the given item is on the selection list. For a component this means that all of the elements of the component must be on the list. A component is passed as a tuple containing the MDagPath of the DAG node and an MObject containing the component."""
	def hasItemPartly(self,dagPath:MDagPath,component:MObject)->bool:
		"""Returns True if at least one of the component's elements is on the selection list. Raises TypeError if dagPath is invalid or component does not contain a component."""
	def isEmpty(self)->bool:
		"""Returns True if the selection list is empty."""
	def length(self)->int:
		"""Returns the number of items on the selection list."""
	@overload
	def merge(self,other:MSelectionList,strategy:int=MSelectionList.kMergeNormal)->Self:
		"""Merges the items from another selection list in with those already on the list, using the given strategy ."""
	@overload
	def merge(self,dagPath:MDagPath,component:MObject,strategy:int=MSelectionList.kMergeNormal)->Self:
		"""Merges the specified<span> component in with those already on the list, using the given<span> strategy ."""
	def remove(self,index:int)->Self:
		"""Removes the index 'th item from the list. Raises IndexError if the index is out of range."""
	def replace(self,index:int,newItem:MObject|MDagPath|MPlug|tuple[MDagPath|MObject,...])->Self:
		"""Replaces the index 'th item on the list with newItem . A component is passed as a tuple containing the MDagPath of the DAG node and an MObject containing the component. Raises IndexError if the index is out of range."""
	def toggle(self,dagPath:MDagPath,component:MObject)->Self:
		"""Removes from the list those elements of the given component which are already on it and adds those which are not."""
	def intersect(self,other:Any,expandToLeaves:Any=False)->Self:
		"""intersect(other, expandToLeaves=False) -> self

		Modify this list to contain the intersection of itself and the given list."""
class MSelectionMask:
	"""Selection masks provide a way to control what is selectable in Maya."""
	kSelectHandles:int=0
	kSelectLocalAxis:int=1
	kSelectIkHandles:int=2
	kSelectIkEndEffectors:int=3
	kSelectJoints:int=4
	kSelectLights:int=5
	kSelectCameras:int=6
	kSelectLattices:int=7
	kSelectClusters:int=8
	kSelectSculpts:int=9
	kSelectNurbsCurves:int=10
	kSelectNurbsSurfaces:int=11
	kSelectMeshes:int=12
	kSelectSubdiv:int=13
	kSelectSketchPlanes:int=14
	kSelectParticleShapes:int=15
	kSelectEmitters:int=16
	kSelectFields:int=17
	kSelectSprings:int=18
	kSelectRigidBodies:int=19
	kSelectRigidConstraints:int=20
	kSelectCollisionModels:int=21
	kSelectXYZLocators:int=22
	kSelectOrientationLocators:int=23
	kSelectUVLocators:int=24
	kSelectTextures:int=25
	kSelectCurves:int=26
	kSelectSurfaces:int=27
	kSelectLocators:int=28
	kSelectObjectsMask:int=29
	kSelectCVs:int=30
	kSelectHulls:int=31
	kSelectEditPoints:int=32
	kSelectMeshVerts:int=33
	kSelectMeshEdges:int=34
	kSelectMeshFreeEdges:int=35
	kSelectMeshFaces:int=36
	kSelectSubdivMeshPoints:int=37
	kSelectSubdivMeshEdges:int=38
	kSelectSubdivMeshFaces:int=39
	kSelectMeshUVs:int=40
	kSelectVertices:int=41
	kSelectEdges:int=42
	kSelectFacets:int=43
	kSelectMeshLines:int=44
	kSelectMeshComponents:int=45
	kSelectCurveParmPoints:int=46
	kSelectCurveKnots:int=47
	kSelectSurfaceParmPoints:int=48
	kSelectSurfaceKnots:int=49
	kSelectSurfaceRange:int=50
	kSelectSurfaceEdge:int=51
	kSelectIsoparms:int=52
	kSelectCurvesOnSurfaces:int=53
	kSelectPPStrokes:int=54
	kSelectLatticePoints:int=55
	kSelectParticles:int=56
	kSelectJointPivots:int=57
	kSelectScalePivots:int=58
	kSelectRotatePivots:int=59
	kSelectPivots:int=60
	kSelectSelectHandles:int=61
	kSelectComponentsMask:int=62
	kSelectAnimCurves:int=63
	kSelectAnimKeyframes:int=64
	kSelectAnimInTangents:int=65
	kSelectAnimOutTangents:int=66
	kSelectAnimMask:int=67
	kSelectAnimAny:int=68
	kSelectTemplates:int=69
	kSelectManipulators:int=70
	kSelectGuideLines:int=71
	kSelectPointsForGravity:int=72
	kSelectPointsOnCurvesForGravity:int=73
	kSelectPointsOnSurfacesForGravity:int=74
	kSelectObjectGroups:int=75
	kSelectSubdivMeshMaps:int=76
	kSelectFluids:int=77
	kSelectHairSystems:int=78
	kSelectFollicles:int=79
	kSelectNCloths:int=80
	kSelectNRigids:int=81
	kSelectDynamicConstraints:int=82
	kSelectNParticles:int=83
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def addMask(self,selType:int)->Self:
		"""addMask(selType) -> self

		Add the specified selection type to this mask.

		* selType (int) - the selection type to add.

		Valid selection types:
		  kSelectHandles
		  kSelectLocalAxis
		  kSelectIkHandles
		  kSelectIkEndEffectors
		  kSelectJoints
		  kSelectLights
		  kSelectCameras
		  kSelectLattices
		  kSelectClusters
		  kSelectSculpts
		  kSelectNurbsCurves
		  kSelectNurbsSurfaces
		  kSelectMeshes
		  kSelectSubdiv
		  kSelectSketchPlanes
		  kSelectParticleShapes
		  kSelectEmitters
		  kSelectFields
		  kSelectSprings
		  kSelectRigidBodies
		  kSelectRigidConstraints
		  kSelectCollisionModels
		  kSelectXYZLocators
		  kSelectOrientationLocators
		  kSelectUVLocators
		  kSelectTextures
		  kSelectCurves
		  kSelectSurfaces
		  kSelectLocators
		  kSelectObjectsMask
		  kSelectCVs
		  kSelectHulls
		  kSelectEditPoints
		  kSelectMeshVerts
		  kSelectMeshEdges
		  kSelectMeshFreeEdges
		  kSelectMeshFaces
		  kSelectSubdivMeshPoints
		  kSelectSubdivMeshEdges
		  kSelectSubdivMeshFaces
		  kSelectMeshUVs
		  kSelectVertices
		  kSelectEdges
		  kSelectFacets
		  kSelectMeshLines
		  kSelectMeshComponents
		  kSelectCurveParmPoints
		  kSelectCurveKnots
		  kSelectSurfaceParmPoints
		  kSelectSurfaceKnots
		  kSelectSurfaceRange
		  kSelectSurfaceEdge
		  kSelectIsoparms
		  kSelectCurvesOnSurfaces
		  kSelectPPStrokes
		  kSelectLatticePoints
		  kSelectParticles
		  kSelectJointPivots
		  kSelectScalePivots
		  kSelectRotatePivots
		  kSelectPivots
		  kSelectComponentsMask
		  kSelectAnimCurves
		  kSelectAnimKeyframes
		  kSelectAnimInTangents
		  kSelectAnimOutTangents
		  kSelectAnimMask
		  kSelectAnimAny
		  kSelectTemplates
		  kSelectManipulators
		  kSelectGuideLines
		  kSelectPointsForGravity
		  kSelectPointsOnCurvesForGravity
		  kSelectPointsOnSurfacesForGravity
		  kSelectObjectGroups
		  kSelectSubdivMeshMaps
		  kSelectFluids
		  kSelectHairSystems
		  kSelectFollicles
		  kSelectNCloths
		  kSelectNRigids
		  kSelectDynamicConstraints
		  kSelectNParticles"""
	def copy(self,source:MSelectionMask)->Self:
		"""copy(source) -> self

		Copy data from source selection mask.

		* source (MSelectionMask) - The source selection mask to copy from"""
	@staticmethod
	def deregisterSelectionType(selTypeName:str)->bool:
		"""deregisterSelectionType(selTypeName) -> bool

		Unregisters a previously registered selection type.

		* selTypeName (string) - Name of the selection type."""
	@staticmethod
	def getSelectionTypePriority(selTypeName:str)->int:
		"""getSelectionTypePriority(selTypeName) -> int

		Gets the selection priority corresponding to a given selection type.

		* selTypeName (string) - Name of the selection type."""
	@overload
	def intersects(self,mask:MSelectionMask)->bool:
		"""intersects(mask) -> bool
		intersects(selType) -> bool

		Returns True if the specified selection mask or selection type is contained within this selection mask.

		* mask (MSelectionMask) - the selection mask to test.
		* selType (int) - the selection type to test.  See addMask() for a list of valid selection masks."""
	@overload
	def intersects(self,selType:int)->bool:
		"""intersects(mask) -> bool
		intersects(selType) -> bool

		Returns True if the specified selection mask or selection type is contained within this selection mask.

		* mask (MSelectionMask) - the selection mask to test.
		* selType (int) - the selection type to test.  See addMask() for a list of valid selection masks."""
	@staticmethod
	def registerSelectionType(selTypeName:str,priority:int=0)->bool:
		"""registerSelectionType(selTypeName, priority=0) -> bool

		Registers a new selection type. It is perfectly legal for 2 plug-ins to register the same selection type.
		Currently we use the registration count. The selection type is deleted only when deregisterSelectionType() as been called the same number of times as this function - registerSelectionType().

		When registerSelectionType() is invoked and the selection type already exists, we neither enable it nor change its priority, just add its registration count by 1.
		The reason is the user might has modified these values after loading the plug-in that has register the selection type the first time.

		* selTypeName (string) - Name of the selection type.
		* priority (int) - Priority of the selection type."""
	@overload
	def setMask(self,mask:MSelectionMask)->Self:
		"""setMask(mask) -> self
		setMask(selType) -> self

		Sets the selection mask to the specified selection mask or selection type.

		* mask (MSelectionMask) - the selection mask to be set.
		* selType (int) - the selection type to be set.  See addMask() for a list of valid selection masks."""
	@overload
	def setMask(self,selType:int)->Self:
		"""setMask(mask) -> self
		setMask(selType) -> self

		Sets the selection mask to the specified selection mask or selection type.

		* mask (MSelectionMask) - the selection mask to be set.
		* selType (int) - the selection type to be set.  See addMask() for a list of valid selection masks."""
class MSpace:
	"""Static class providing coordinate space constants."""
	kInvalid:int=0
	kTransform:int=1
	kPreTransform:int=2
	kPostTransform:int=3
	kWorld:int=4
	kObject:int=2
	kLast:int=5
class MSyntax:
	"""Syntax for commands."""
	@property
	def enableQuery(self)->bool:
		"""Enable support for the -query flag."""
	@enableQuery.setter
	def enableQuery(self,value:bool)->None:...
	@property
	def enableEdit(self)->bool:
		"""Enable support for the -edit flag."""
	@enableEdit.setter
	def enableEdit(self,value:bool)->None:...
	kInvalidArgType:int=0
	kNoArg:int=1
	kBoolean:int=2
	kLong:int=3
	kDouble:int=4
	kString:int=5
	kUnsigned:int=6
	kDistance:int=7
	kAngle:int=8
	kTime:int=9
	kSelectionItem:int=10
	kLastArgType:int=11
	kInvalidObjectFormat:int=0
	kNone:int=1
	kStringObjects:int=2
	kSelectionList:int=3
	kLastObjectFormat:int=4
	@overload
	def __init__(self)->None:
		"""Default constructor. Returns a new, empty MSyntax object."""
	@overload
	def __init__(self,src:MSyntax)->None:
		"""Copy constructor. Returns a new MSyntax object with the same value as src ."""
	def addArg(self,argType:int)->Self:
		"""Add a command argument."""
	def addFlag(self,shortName:str,longName:str,argTypes:Any)->Self:
		"""Add a flag and its arguments. Raises TypeError if more than 6 argument types are provided."""
	def makeFlagMultiUse(self,flagName:str)->Self:
		"""Set whether a flag may be used multiple times on the command line."""
	def makeFlagQueryWithFullArgs(self,flagName:str,argsOptional:bool)->Self:
		"""Set whether a flag requires its args when queried."""
	def maxObjects(self)->int:
		"""Returns the maximum number of objects which can be passed to the command. If no maximum has been set then the maximum will be unbounded and this method will return 0, which unfortunately is indistinguishable from the situation where the maximum has been set to 0."""
	def minObjects(self)->int:
		"""Returns the minimum number of objects which can be passed to the command. If no minimum has been set then the minimum will default to 0."""
	def setMaxObjects(self,max:int)->Self:
		"""Sets the maximum number of objects which can be passed to the command. If no maximum has been set then the maximum will be unbounded. Raises ValueError if max is negative."""
	def setMinObjects(self,min:int)->Self:
		"""Sets the minimum number of objects which can be passed to the command. If no minimum has been set then the minimum will be 0. Raises ValueError if min is negative."""
	def setObjectType(self,objType:int,min:Any=0,max:Any|None=None)->Self:
		"""Set the type and number of objects to be passed to the command. Raises ValueError if min or max is negative, or if max is less than min ."""
	def useSelectionAsDefault(self,useSelection:bool)->Self:
		"""If set to True then when no objects are provided on the command-line Maya will pass the current selection instead. Defaults to False."""
class MTime:
	"""Manipulate time data."""
	@property
	def unit(self)->int:
		"""Time units currently in use."""
	@unit.setter
	def unit(self,value:int)->None:...
	@property
	def value(self)->float:
		"""Value of the time in the current units."""
	@value.setter
	def value(self,value:float)->None:...
	__hash__:None=None
	kInvalid:int=0
	kHours:int=1
	kMinutes:int=2
	kSeconds:int=3
	kMilliseconds:int=4
	kGames:int=5
	k15FPS:int=5
	kFilm:int=6
	k24FPS:int=6
	kPALFrame:int=7
	k25FPS:int=7
	kNTSCFrame:int=8
	k30FPS:int=8
	kShowScan:int=9
	k48FPS:int=9
	kPALField:int=10
	k50FPS:int=10
	kNTSCField:int=11
	k60FPS:int=11
	k2FPS:int=12
	k3FPS:int=13
	k4FPS:int=14
	k5FPS:int=15
	k6FPS:int=16
	k8FPS:int=17
	k10FPS:int=18
	k12FPS:int=19
	k16FPS:int=20
	k20FPS:int=21
	k40FPS:int=22
	k75FPS:int=23
	k80FPS:int=24
	k100FPS:int=25
	k120FPS:int=26
	k125FPS:int=27
	k150FPS:int=28
	k200FPS:int=29
	k240FPS:int=30
	k250FPS:int=31
	k300FPS:int=32
	k375FPS:int=33
	k400FPS:int=34
	k500FPS:int=35
	k600FPS:int=36
	k750FPS:int=37
	k1200FPS:int=38
	k1500FPS:int=39
	k2000FPS:int=40
	k3000FPS:int=41
	k6000FPS:int=42
	k23_976FPS:int=43
	k29_97FPS:int=44
	k29_97DF:int=45
	k47_952FPS:int=46
	k59_94FPS:int=47
	k44100FPS:int=48
	k48000FPS:int=49
	k90FPS:int=50
	k119_88FPS:int=51
	kUserDef:int=52
	kLast:int=53
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
	@overload
	def __init__(self)->None:
		"""Default constructor. Returns a new MTime object with value 1.0 and unit set to the current UI unit."""
	@overload
	def __init__(self,src:MTime)->None:
		"""Copy constructor. Returns a new MTime object with the same value and unit as src ."""
	@overload
	def __init__(self,value:float,unit:int)->None:
		"""Returns a new MTime object with the given value and unit ."""
	@overload
	def __add__(self,other:MTime)->MTime:
		"""Addition of another time. Uses the units of the left operand."""
	@overload
	def __add__(self,other:float)->MTime:
		"""Addition of a float value. The value is interpreted in the units of the left operand."""
	def __radd__(self,other:MTime)->MTime:
		"""Addition of another time. Uses the units of the left operand."""
	def __sub__(self,other:float)->MTime:
		"""Subtraction of a float value. The value is interpreted in the units of the left operand."""
	def __rsub__(self,*args)->Any:
		"""Return value-self."""
	def __mul__(self,other:float)->MTime:
		"""Multiplication by a float value. The result uses the units of the left operand."""
	def __rmul__(self,other)->Any:
		"""Return value*self."""
	def __iadd__(self,other:MTime)->Self:
		"""In-place addition of another time. Retains the units of the left operand."""
	@overload
	def __isub__(self,other:MTime)->Self:
		"""In-place subtraction of another time. Retains the units of the left operand."""
	@overload
	def __isub__(self,other:float)->Self:
		"""In-place subtraction of a float value. The value is interpreted in the units of the left operand."""
	def __imul__(self,other:float)->Self:
		"""In-place multiplication by a float value. The units of the left operand are retained."""
	def __truediv__(self,other:float)->MTime:
		"""Division by a float value. The result uses the units of the left operand."""
	def __rtruediv__(self,other)->Any:
		"""Return value/self."""
	def __itruediv__(self,other:float)->Self:
		"""In-place division by a float value. The units of the left operand are retained."""
	@staticmethod
	def uiUnit()->int:
		"""Returns the unit type currently used by Maya's UI to display time values."""
	@staticmethod
	def setUIUnit(unit:int)->None:
		"""Sets the unit type to be used by Maya's UI to display time values."""
	@staticmethod
	def ticksPerSecond(*args)->Any:
		"""Returns the number of ticks per second, the smallest unit of time available."""
	def asUnits(self,unit:int)->float:
		"""Returns the time value converted to the specified unit ."""
class MTimeArray(collections.abc.Sequence[MTime]):
	"""Array of MTime values."""
	@property
	def sizeIncrement(self)->Any:
		"""Number of elements by which to grow the array when necessary."""
	@sizeIncrement.setter
	def sizeIncrement(self,value:Any)->None:...
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def __len__(self)->int:
		"""Return len(self)."""
	def __getitem__(self,index:int)->MTime:
		"""Return self[key]."""
	def __setitem__(self,index:int,value:MTime)->None:
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
class MTimeRange:
	"""Mathematic type that represents a set of pseudo-real numbers (in units of time), such as [-1s, +1s] U [+2, +5s]"""
	__hash__:None=None
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
	def __or__(self,*args)->Any:
		"""Return self|value."""
	def __ror__(self,*args)->Any:
		"""Return value|self."""
	def empty(self)->bool:
		"""empty() -> bool

		Checks if this time range is an empty set"""
	@overload
	def contains(self,MTime:Any)->bool:
		"""contains(MTime) -> boolcontains(MTime, MTime) -> bool

		Checks if the given time point or interval is contained in this time range."""
	@overload
	def contains(self,MTime:Any,MTime2:Any)->bool:
		"""contains(MTime) -> boolcontains(MTime, MTime) -> bool

		Checks if the given time point or interval is contained in this time range."""
	def intersects(self,MTime:Any,MTime2:Any)->bool:
		"""intersects(MTime, MTime) -> bool

		Checks if the given interval intersects with this time range."""
class MTimerMessage(MMessage):
	"""Class used to register callbacks for timer related messages."""
	@staticmethod
	def addTimerCallback(period:float,function:Callable,clientData:Any|None=None)->int:
		"""addTimerCallback(period, function, clientData=None) -> id

		This method registers a callback which is called repeatedly with a
		specified period of time between calls. Each time the timer fires the
		callback will be placed on the idle queue for execution in the next
		idle cycle. If the timer fires again, before the previous invocation
		has completed execution, the new firing will be skipped.

		If the execution time of the callback exceeds half of its period then
		the next timeout will be skipped to give Maya time to process other tasks.

		The maximum resolution for this callback is about 1ms.  The response
		is, however, not guaranteed because while multitasking, the OS may
		delay for an unspecified length of time before returning control to
		Maya.

		 * period (float) - the period at which the callback will be
		executed (Measured in seconds)
		 * function - callable which will be passed a float indicating
		   the elapsed time since this function was last called, a float
		   indicating the execution time of this function the last time
		   it was called, and the clientData object
		 * clientData - User defined data passed to the callback function

		 * return: Identifier used for removing the callback."""
class MTransformationMatrix:
	"""Manipulate the individual components of a transformation."""
	__hash__:None=None
	kIdentity:MTransformationMatrix
	kTolerance:float=1e-10
	kInvalid:int=0
	kXYZ:int=1
	kYZX:int=2
	kZXY:int=3
	kXZY:int=4
	kYXZ:int=5
	kZYX:int=6
	kLast:int=7
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
	@overload
	def __init__(self)->None:
		"""Default constructor. Returns a new MTransformationMatrix object, set to the identity transformation."""
	@overload
	def __init__(self,src:MTransformationMatrix|MMatrix)->None:
		"""Returns a new MTransformationMatrix object with the same value as src ."""
	def asMatrix(self,interp:float=1.0)->MMatrix:
		"""Interpolates between the identity transformation and that currently in the object, returning the result as an MMatrix . When interp is 0.0 the result will be the identity matrix. When it is 1.0 the result will be the full transformation. If interp is less than 0.0 or greater than 1.0 the result will properly extrapolated."""
	def asMatrixInverse(self)->MMatrix:
		"""Returns the inverse of the matrix representing the transformation."""
	def asRotateMatrix(self)->MMatrix:
		"""Returns the matrix which takes points from object space to the space immediately following the scale/shear/rotation transformations."""
	def asScaleMatrix(self)->MMatrix:
		"""Returns the matrix which takes points from object space to the space immediately following scale and shear transformations."""
	def isEquivalent(self,other,tolerance:float=MEulerRotation.kTolerance)->bool:
		"""Inexact equality test. Returns true if this transformation's matrix is within tolerance of other 's matrix."""
	def reorderRotation(self,order:int)->Self:
		"""Reorders the transformation's rotate component to give the same overall rotation but using the new order or rotations."""
	def rotateBy(self,rot:MQuaternion|MEulerRotation,space:int)->Self:
		"""Adds rot to the transformation's rotation component."""
	def rotateByComponents(self,seq:Sequence[float|int],space:int,asQuaternion:bool=False)->Self:
		"""Adds the rotation represented by the four parameter values to the transformation's rotate component. If asQuaternion is True then seq must contain four floats representing the x, y, z and w components of a quaternion rotation. If asQuaternion is False then seq must contain three floats representing the x, y and z angles, followed by a Rotation Order constant, which together form an Euler rotation."""
	def rotatePivot(self,space:int)->MPoint:
		"""Returns the transformation's rotate pivot component."""
	def rotatePivotTranslation(self,space:int)->MVector:
		"""Returns the transformation's rotate pivot translation component."""
	def rotation(self,asQuaternion:bool=False)->MEulerRotation|MQuaternion:
		"""Returns the transformation's rotation component as either an Euler rotation or a quaternion."""
	def rotationComponents(self,asQuaternion:bool=False)->list[float|order]|list[float]:
		"""Returns a list containing the four components of the transformation's rotate component. If asQuaternion is True then the first three elements are the quaternion's unreal x, y, and z components, and the fourth is its real w component. If asQuaternion is False then the first three components are the x, y and z Euler rotation angles and the fourth is a Rotation Order constant."""
	def rotationOrder(self)->int:
		"""Returns the order of rotations when the transformation's rotate component is expressed as an euler rotation."""
	def rotationOrientation(self)->MQuaternion:
		"""Returns the rotation which orients the local rotation space."""
	def scale(self,space:int)->list[float]:
		"""Returns a list containing the transformation's scale components."""
	def scaleBy(self,seq:Sequence[float],space:int)->Self:
		"""Multiplies the transformation's scale components by the three floats in seq ."""
	def scalePivot(self,space:int)->MPoint:
		"""Returns the transformation's scale pivot component."""
	def scalePivotTranslation(self,space:int)->MVector:
		"""Returns the transformation's scale pivot translation component."""
	def setRotatePivot(self,pivot:MPoint,space:int,balance:bool)->Self:
		"""Sets the transformation's rotate pivot component."""
	def setRotatePivotTranslation(self,trans:MVector,space:int)->Self:
		"""Sets the transformation's rotate pivot translation component."""
	def setRotation(self,rot:MQuaternion|MEulerRotation)->Self:
		"""Sets the transformation's rotation component to rot ."""
	def setRotationComponents(self,seq:Sequence[float|int],asQuaternion:bool=False)->Self:
		"""Sets the transformation's rotate component. If asQuaternion is True then seq must contain four floats representing the x, y, z and w components of a quaternion rotation. If asQuaternion is False then seq must contain three floats representing the x, y and z angles, followed by a Rotation Order constant, which together form an Euler rotation."""
	def setRotationOrientation(self,rot:MQuaternion)->Self:
		"""Sets the rotation which orients the local rotation space."""
	def setScale(self,seq:Sequence[float],space:int)->Self:
		"""Sets the transformation's scale components to the three floats in seq ."""
	def setScalePivot(self,pivot:MPoint,space:int,balance:bool)->Self:
		"""Sets the transformation's scale pivot component."""
	def setScalePivotTranslation(self,trans:MVector,space:int)->Self:
		"""Sets the transformation's scale pivot translation component."""
	def setShear(self,seq:Sequence[float],space:int)->Self:
		"""Sets the transformation's shear component."""
	def setTranslation(self,trans:MVector,space:int)->Self:
		"""Sets the transformation's translation component."""
	def setToRotationAxis(self,axis:MVector,rot:float)->Self:
		"""Sets the transformation's rotate component to be rot radians around axis ."""
	def shear(self,space:int)->list[float]:
		"""Returns a list containing the transformation's shear component."""
	def shearBy(self,seq:Sequence[float],space:int)->Self:
		"""Multiplies the transformation's shear components by the elements of seq ."""
	def translateBy(self,vec:MVector,space:int)->Self:
		"""Adds vec to the transformation's translation component."""
	def translation(self,space:int)->MVector:
		"""Returns the transformation's translation component as a vector."""
class MTypeId:
	"""Stores a Maya object type identifier."""
	__hash__:None=None
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
	@overload
	def __init__(self)->None:
		"""Default constructor. Returns a new, empty MTypeId object."""
	@overload
	def __init__(self,src:MTypeId)->None:
		"""Copy constructor. Returns a new MTypeId object with the same value as src ."""
	@overload
	def __init__(self,id:int)->None:
		"""Returns a new MTypeId object with the given id ."""
	@overload
	def __init__(self,prefix:int,id:int)->None:
		"""Returns a new MTypeId object whose id uses prefix for its upper 24 bits and id for its lower 8. Note that only the lower 24 bits of prefix and the lower 8 of id are significant. All higher order bits are ignored."""
	def id(self)->int:
		"""Returns the object's id."""
class MURI:
	"""Manipulate URIs."""
	__hash__:None=None
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
	@staticmethod
	def isValidURI(uri:Any)->bool:
		"""isValidURI(uri) -> bool

		Determines if a string value represents a valid URI."""
	def asString(self)->str:
		"""asString() -> string

		Returns the string representation of the URI."""
	def getScheme(self)->str:
		"""getScheme() -> string

		Returns the scheme of the URI."""
	def getPath(self)->str:
		"""getPath() -> string

		Returns the path component of the URI."""
	def getFragment(self)->str:
		"""getFragment() -> string

		Returns the fragment component of the URI."""
	def getFileName(self,includeExtension:bool=True)->str:
		"""getFileName(bool includeExtension=True) -> string

		Returns just the file name portion of the URI, with or without the extension."""
	def getDirectory(self)->str:
		"""getDirectory() -> string

		Returns just the file directory portion of the URI, without the file name."""
	def getAuthority(self)->str:
		"""getAuthority() -> string

		Returns the authority component of the URI."""
	def getUserInfo(self)->str:
		"""getUserInfo() -> string

		Returns the user info component of the URI."""
	def getUserName(self)->str:
		"""getUserName() -> string

		Returns the user name component of the URI."""
	def getPassword(self)->str:
		"""getPassword() -> string

		Returns the password component of the URI."""
	def getHost(self)->str:
		"""getHost() -> string

		Returns the host component of the URI."""
	def getPort(self)->int:
		"""getPort() -> int

		Returns the port component of the URI, or -1 if the port is not defined."""
	def getAllQueryItemKeys(self)->array:
		"""getAllQueryItemKeys() -> array

		Returns an array containing the keys from all query string pairs."""
	def getQueryItemValue(self,key:Any)->str:
		"""getQueryItemValue(key) -> string

		Returns the value from the first query string pair in the URI which has a given key."""
	def getAllQueryItemValues(self,key:Any)->array:
		"""getAllQueryItemValues(key) -> array

		Returns an array containing the values from all query string pairs which have a given key."""
	def getQueryValueDelimiter(self)->str:
		"""getQueryValueDelimiter() -> string

		Returns the character used to delimit keys and values in the query string of the URI."""
	def getQueryPairDelimiter(self)->str:
		"""getQueryPairDelimiter() -> string

		Returns the character used to delimit between key-value pairs in the query string of the URI."""
	def setScheme(self,string:str)->Self:
		"""setScheme(string) -> self

		Sets the scheme component of the URI."""
	def setPath(self,string:str)->Self:
		"""setPath(string) -> self

		Sets the path component of the URI."""
	def setFragment(self,string:str)->Self:
		"""setFragment(string) -> self

		Sets the fragment component of the URI."""
	def setFileName(self,string:str)->Self:
		"""setFileName(string) -> self

		Sets just the filename portion of the URI (i.e. not including the directory)."""
	def setDirectory(self,string:str)->Self:
		"""setDirectory(string) -> self

		Sets just the directory portion of the URI (i.e. not including the filename)."""
	def setAuthority(self,string:str)->Self:
		"""setAuthority(string) -> self

		Set the authority portion of the URI."""
	def setUserInfo(self,string:str)->Self:
		"""setUserInfo(string) -> self

		Decomposes the userInfo string to fill out the userInfo-related component values."""
	def setUserName(self,string:str)->Self:
		"""setUserName(string) -> self

		Sets the user name part of the user info component."""
	def setPassword(self,string:str)->Self:
		"""setPassword(string) -> self

		Sets the password part of the user info component."""
	def setHost(self,string:str)->Self:
		"""setHost(string) -> self

		Set the host component of the URI."""
	def setPort(self,int:int)->Self:
		"""setPort(int) -> self

		Set the port component of the URI."""
	def addQueryItem(self,key:Any,value:Any)->Self:
		"""addQueryItem(key, value) -> self

		Add a key/value pair to the query string of the URI."""
	def setQueryDelimiters(self,valueDelimiter:Any,pairDelimiter:Any)->Self:
		"""setQueryDelimiters(valueDelimiter, pairDelimiter) -> self

		Sets the delimiter characters used in the query string of the URI."""
	def removeQueryItem(self,int:int)->Self:
		"""removeQueryItem(int) -> self

		Removes the first query string pair with a given key from the URI."""
	def removeAllQueryItems(self,int:int)->Self:
		"""removeAllQueryItems(int) -> self

		Removes all query string pairs having a given key from the URI."""
	def copy(self,source:MURI)->Self:
		"""copy(source) -> self

		Copy method. Assigns the value of one MURI to another.

		* source (MURI) - Existing MURI object to copy."""
	def setURI(self,uri:Any)->Self:
		"""setURI(uri) -> self

		Initialize the MURI from a string value."""
	def isEmpty(self)->bool:
		"""isEmpty() -> bool

		Determines if the URI does not contain any data."""
	def isValid(self)->bool:
		"""isValid() -> bool

		Determines if the URI is valid."""
	def clear(self)->Self:
		"""clear() -> self

		Clears the contents of the MURI object."""
class MUint64Array(collections.abc.Sequence[int]):
	"""Array of MUint64 values."""
	@property
	def sizeIncrement(self)->Any:
		"""Number of elements by which to grow the array when necessary."""
	@sizeIncrement.setter
	def sizeIncrement(self,value:Any)->None:...
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def __len__(self)->int:
		"""Return len(self)."""
	def __getitem__(self,index:int)->int:
		"""Return self[key]."""
	def __setitem__(self,index:int,value:int)->None:
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
class MUintArray(collections.abc.Sequence[int]):
	"""Array of unsigned int values."""
	@property
	def sizeIncrement(self)->Any:
		"""Number of elements by which to grow the array when necessary."""
	@sizeIncrement.setter
	def sizeIncrement(self,value:Any)->None:...
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def __len__(self)->int:
		"""Return len(self)."""
	def __getitem__(self,index:int)->int:
		"""Return self[key]."""
	def __setitem__(self,index:int,value:int)->None:
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
class MUserData:
	"""Virtual base class for user data caching.

	MUserData( deleteAfterUse=False, legacy=True )
	* deleteAfterUse (bool) - Enabled if user data should be deleted immediately after use. DEPRECATED in 2022.
	* legacy (bool) - Enabled if legacy constructor arguments are used. DEPRECATED in 2022.
	"""
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def deleteAfterUse(self)->bool:
		"""deleteAfterUse() -> bool

		Returns whether or not this user data should be deleted immediately after use instead of being
		maintained until the internal owning object is deleted.

		    DEPRECATED in 2022, deleteAfterUse is deprecated."""
	def setDeleteAfterUse(self,bool:bool)->Self:
		"""setDeleteAfterUse(bool) -> self

		Sets whether or not this user data should be deleted immediately after use instead of being
		maintained until the internal owning object is deleted.

		Setting this to false may allow the data to be reused in some situations.
		For example, if the MUserData returned by an MPxDrawOverride instance's prepareForDraw() method has
		its delete-after-use set to false, then Maya will retain the data between draws of that object,
		passing it back to the instance for reuse on subsequent draws.

		    DEPRECATED in 2022, deleteAfterUse is deprecated."""
class MUserEventMessage(MMessage):
	"""Class used to register callbacks for user event messages."""
	@staticmethod
	def registerUserEvent(eventName:str)->None:
		"""registerUserEvent(eventName)

		Adds a new event type with the given string identifier.  The string
		identifier can then be used in all other MUserEventMessage methods to operate
		on the new event type.

		 * eventName (string) - the name of the new event to register.  Any
		   non-empty string may be used as an event name."""
	@staticmethod
	def isUserEvent(eventName:str)->bool:
		"""isUserEvent(eventName) -> bool

		Checks if an event type exists with the given event name.

		 * eventName (string) - the name of the new event to check. """
	@staticmethod
	def deregisterUserEvent(eventName:str)->None:
		"""deregisterUserEvent(eventName)

		Removes the event type with the given event name.  If callbacks have been
		registered with this event type, they will become invalid after a
		successful call to this method.

		 * eventName (string) - the name of the new event to deregister."""
	@staticmethod
	def postUserEvent(eventName:str,clientData:Any|None=None)->None:
		"""postUserEvent(eventName, clientData=None)

		Notifies all callbacks attached to the given event type of the occurence
		of the event.

		If clientData is specified, this data will be passed to all callbacks that
		receive the event.  If clientData is None (the default), the clientData
		registered with addUserEventCallback will be passed to the callbacks.


		 * eventName (string) - the name of the new event.
		 * clientData - User defined data."""
	@staticmethod
	def addUserEventCallback(eventName:str,function:Callable,clientData:Any|None=None)->int:
		"""addUserEventCallback(eventName, function, clientData=None) -> id

		This method registers a callback for user-defined messages.

		The parameter clientData will be passed to callbacks registered for this
		event whenever the event is triggered.  To override the data that is passed
		to the callback whenever the event is posted, you can supply a clientData
		pointer to postUserEvent()..

		 * eventName (string) - the event name to register the callback for
		 * function - callable which will be passed the clientData object
		 * clientData - User defined data passed to the callback function

		 * return: Identifier used for removing the callback."""
class MUuid:
	"""Manipulate UUID data."""
	__hash__:None=None
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
	def asString(self)->str:
		"""asString() -> string

		Return the UUID as a string."""
	def copy(self,source:MUuid)->Self:
		"""copy(source) -> self

		Copy method. Assigns the value of one MUuid to another.

		* source (MUuid) - Existing MUuid object to copy."""
	def valid(self)->bool:
		"""valid() -> bool

		Return whether the UUID is valid."""
	def generate(self)->Self:
		"""generate() -> self

		Generate a new UUID."""
class MVector(collections.abc.Sequence[float]):
	"""3D vector with double-precision coordinates."""
	@property
	def x(self)->float:
		"""X coordinate"""
	@x.setter
	def x(self,value:float)->None:...
	@property
	def y(self)->float:
		"""Y coordinate"""
	@y.setter
	def y(self,value:float)->None:...
	@property
	def z(self)->float:
		"""Z coordinate"""
	@z.setter
	def z(self,value:float)->None:...
	__hash__:None=None
	kTolerance:float=1e-10
	kXaxis:int=0
	kYaxis:int=1
	kZaxis:int=2
	kWaxis:int=3
	kZeroVector:MVector
	kOneVector:MVector
	kXaxisVector:MVector
	kYaxisVector:MVector
	kZaxisVector:MVector
	kXnegAxisVector:MVector
	kYnegAxisVector:MVector
	kZnegAxisVector:MVector
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
	@overload
	def __init__(self)->None:
		"""Default constructor. Returns a new MVector object initialized to the zero vector."""
	@overload
	def __init__(self,src:MVector|MFloatVector|MPoint|MFloatPoint)->None:
		"""Copy constructor. Returns a new MVector object whose x, y and z coordinates are set to the x, y and z coordinates of src ."""
	@overload
	def __init__(self,seq:Sequence[two|float])->None:
		"""Returns a new MVector object whose x, y and z coordinates are set to the elements of seq . If the sequence only contains two values z will be set to 0.0."""
	@overload
	def __init__(self,x:float,y:float,z:float)->None:
		"""Returns a new MVector object with the specified x , y and z coordinates."""
	def __add__(self,other:MVector)->MVector:
		"""New vector which is the sum of the two vectors."""
	def __radd__(self,other:MVector)->MVector:
		"""New vector which is the sum of the two vectors."""
	def __sub__(self,other:MVector)->MVector:
		"""New vector which is the difference of the two vectors."""
	def __rsub__(self,other:MVector)->MVector:
		"""New vector which is the difference of the two vectors."""
	@overload
	def __mul__(self,other:MVector)->float:
		"""Dot product of the two vectors."""
	@overload
	def __mul__(self,other:float)->MVector:
		"""New vector whose components are those of the given vector, each multiplied by scalar , which can be of any type which is convertable to float."""
	@overload
	def __mul__(self,other:MMatrix)->MVector:
		"""New vector resulting from postmultiplying the vector by the matrix."""
	@overload
	def __rmul__(self,other:MVector)->float:
		"""Dot product of the two vectors."""
	@overload
	def __rmul__(self,other:float)->MVector:
		"""New vector whose components are those of the given vector, each multiplied by scalar , which can be of any type which is convertable to float."""
	@overload
	def __rmul__(self,other:MMatrix)->MVector:
		"""New vector resulting from premultiplying the vector by the matrix."""
	def __neg__(self)->Self:
		"""-self"""
	def __xor__(self,other:MVector)->MVector:
		"""New vector which is the cross product of the two vectors."""
	def __rxor__(self,other:MVector)->MVector:
		"""New vector which is the cross product of the two vectors."""
	def __iadd__(self,other:MVector)->Self:
		"""Adds the second vector to the first and returns a new reference to the first."""
	def __isub__(self,other:MVector)->Self:
		"""Subtracts the second vector from the first and returns a new reference to the first."""
	@overload
	def __imul__(self,other:float)->Self:
		"""Multiplies each component of the vector by scalar , which can be of any type which is convertable to float, and returns a new reference to the vector."""
	@overload
	def __imul__(self,other:MMatrix)->Self:
		"""Postmultiplies the vector by the matrix and returns a new reference to the vector."""
	def __truediv__(self,other:float)->MVector:
		"""New vector whose components are those of the given vector, each divided by scalar , which can be of any type which is convertable to float."""
	def __rtruediv__(self,other)->Any:
		"""Return value/self."""
	def __itruediv__(self,other:float)->Self:
		"""Divides each component of the vector by scalar , which can be of any type which is convertable to float, and returns a new reference to the vector."""
	def __len__(self)->int:
		"""Return len(self)."""
	def __getitem__(self,index:int)->float:
		"""Return self[key]."""
	def __setitem__(self,index:int,value:float)->None:
		"""Set self[key] to value."""
	def __delitem__(self,index:int)->None:
		"""Delete self[key]."""
	def length(self)->float:
		"""Returns the magnitude of this vector."""
	def normal(self)->MVector:
		"""Returns a new vector containing the normalized version of this vector."""
	def normalize(self)->MVector:
		"""Normalizes this vector in-place and returns a new reference to it."""
	def transformAsNormal(self,matrix:MMatrix)->MVector:
		"""Returns a new vector which is calculated by postmultiplying this vector by the transpose of matrix 's inverse and then normalizing it."""
	def angle(self,other:MVector)->float:
		"""Returns the angle, in radians, between this vector and other ."""
	def isEquivalent(self,other:MVector,tolerance:float=MEulerRotation.kTolerance)->bool:
		"""Returns True if this vector and other are within the given tolerance of being equal."""
	def isParallel(self,other:MVector,tolerance:float=MEulerRotation.kTolerance)->bool:
		"""Returns True if this vector and other are within the given tolerance of being parallel."""
	@overload
	def rotateBy(self,rot:MQuaternion|MEulerRotation)->MVector:
		"""Returns a new vector containing the result of rotating this vector by the rotation given by rot ."""
	@overload
	def rotateBy(self,axis:int,angle:float)->MVector:
		"""Returns a new vector containing the result of rotating this vector by angle radians about the specified axis ."""
	def rotateTo(self,target:MVector)->MQuaternion:
		"""Returns the quaternion which will rotate this vector into the target vector, about their mutually perpendicular axis."""
class MVectorArray(collections.abc.Sequence[MVector]):
	"""Array of MVector values."""
	@property
	def sizeIncrement(self)->Any:
		"""Number of elements by which to grow the array when necessary."""
	@sizeIncrement.setter
	def sizeIncrement(self,value:Any)->None:...
	def __init__(self,*args)->None:
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def __len__(self)->int:
		"""Return len(self)."""
	def __getitem__(self,index:int)->MVector:
		"""Return self[key]."""
	def __setitem__(self,index:int,value:MVector)->None:
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
class MWeight:
	"""Methods for accessing component weight data. This class is currently
	only used to access soft select and symmetry selection weights.
	Other weight data (e.g. deformer weights) does not use this class
	and can be accessed through the corresponding MFn class or directly
	from the node's attributes.

	__init__()
	Initializes a new MWeight object with influence weight of 1 and seam
	weight of 0.
	__init__(MWeight src)
	Initializes a new MWeight object with the same value as src."""
	@property
	def influence(self)->Any:
		"""Controls how much of a given operation is applied to the entity
		associated with this weight structure. A value of 1 means the full
		 effect should be applied. A value of 0 means the operation should
		not affect the entity at all."""
	@influence.setter
	def influence(self,value:Any)->None:...
	@property
	def seam(self)->Any:
		"""Indicates how close the entity associated with this weight is to the
		plane of reflection (the seam), and hence, how strongly it should be
		associated with the seam. A value of 0 means the entity is free to move
		independent of the seam. A value of 1 means the entity is full on the
		seam, and should ideally maintain it's distance relative to the plane of
		symmetry. This value is only relevant when symmetry is enabled."""
	@seam.setter
	def seam(self,value:Any)->None:...
	@overload
	def __init__(self)->None:
		"""Default constructor. Returns a new MWeight object with influence weight of 1 and seam weight of 0."""
	@overload
	def __init__(self,src:MWeight)->None:
		"""Copy constructor. Returns a new MWeight object with the same value as src ."""

def getStringResource(*args)->Any:...
def registerStringResource(*args)->Any:...
def registerStringResources(*args)->Any:...
