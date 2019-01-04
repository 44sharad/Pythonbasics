##################
Shape Manipulation
##################

**********************
1.Changing Array Shape
**********************


=========
Reshape
=========

*Gives a new shape to an array
without changing its data.*

**Syntax** : np.reshape(a,newshape,order='C')

**Arguments** :

1. *a =  Array to be reshaped.*

2. *Newshape = The new shape should be compatible with the original shape.*

3. *Order =  {‘C’, ‘F’, ‘A’}, optional.*

**Returns** :*This will be a new view object if possible; otherwise, it will be a copy.*



======
Flat
======

*A 1-D iterator over the array.*

**Syntax** : np.flat(x)

**Arguments** : 

1. *X = Index of elemet*

**Returns** : *Returns the element found at the given index fter flattening the array*



=========
Flatten
=========

*Return a copy of the array collapsed into one dimension.*

**Syntax** : np.flatten()

**Arguments** : 

1. *Order =  {‘C’, ‘F’, ‘A’}, optional*

**Returns** : *A copy of the input array, flattened to one dimension.*




=======
Ravel
=======

*Return a contiguous flattened array. A 1-D array, containing the elements of the input, is returned. A copy is made only if needed.*

**Syntax** : np.ravel(a,order='C')

**Argumnets** :

1. *a = Input array.*

2. *order:{‘C’,’F’, ‘A’, ‘K’}, optional.*

**Returns** : *Returns y,y is an array of the same subtype as a, with shape (a.size,).Note that matrices are special cased for backward compatibility, if a is a matrix, then y is a 1-D ndarray.*



.. Note:: 'C' means to flatten in row-major (C-style) order. ‘F’ means to flatten in column-major (Fortran- style) order. ‘A’ means to flatten in column-major order if a is Fortran contiguous in memory, row-major order otherwise. ‘K’ means to flatten a in the order the elements occur in memory. The default is ‘C’.




***************************
2. Adding/Removing Elements
***************************

========
Resize
========

*Return a new array with the specified shape.*

**Syntax** : np.resize(a,new_shape)

**Arguments** : 
1. *a = Array to be resized.*

2. *new_shape = Shape of resized array.*

**Returns** : *A copy of arr with values inserted. Note that insert does not occur in-place: a new array is returned. If axis is None, out is a flattened array.*



========
Append
========

*Append values to the end of an array.*

**Syntax** : np.append(arr,values,axis=None)

**Arguments** :

1. *arr =Values are appended to a copy of this array.*

2. *values = These values are appended.*

3. *axis = The axis along which values are appended.*

**Returns** : *A copy of arr with values appended to axis. Note that append does not occur in-place: a new array is allocated and filled. If axis is None, out is a flattened array.*



========
Insert
========

*Insert values along the given axis before the given indices.*

**Syntax** :np.insert(arr,obj,values,axis=None)

**Arguments** :

1. *arr =Input array.*
 
2. *obj = Object that defines the index*

3. *values = Values to insert into arr.*

4. *axis = Axis along which to insertvalues.*

**Returns** :*A copy of arr with values inserted. Note that insert does not occur in-place: a new array is returned. If axis is None, out is a flattened array.*


========
Delete
========

*Removes a particular object.*

**Syntax** : np.delete(arr,obj,axis=None)

**Arguments** :

1. *arr =Input array.* 

2. *obj = Indicate which sub-arrays to remove.*

3. *axis = along which axis to delete.*

**Returns** : *A copy of arr with the elements specified by obj removed. Note that delete does not occur in-place. If axis is None, out is a flattened array.*



*******************
3. Combining Arrays
*******************


===============
Concatenation
===============

*Join a sequence of arrays along an existing axis.*

**Syntax** : np.concatenate((a1,a2,...),axis=0,out=None)

**Arguments** : 

1. *a1, a2, …: a sequence of array*

**Dimension & Shape** : *The arrays must have the same shape,except in the dimension correspondingto axis*

**Returns** : *The concatenated array.*

 
========
Vstack
========

*Stack arrays in sequence vertically (row wise).*

**Syntax** : numpy.vstack(tup)

**Arguments** : 

1. *Tup: sequence of arrays*

**Dimenssion & Shape** : *The arrays must have the same shape along all but the first axis.1-D arrays must have the same length.*

**Returns** : *The array formed by stacking the given arrays, will be at least 2-D.*


========
Hstack
========

*Stack arrays in sequence horizontally (column-wise).*

**Syntax** : numpy.hstack(tup)

**Arguments** :

1. *Tup : sequence of arrays*

**Dimenssion & Shape** : *The arrays must have the same shapealong all but the second axis, except 1-D arrays which can be any length.*

**Returns** : *The array formed by stacking the given arrays.*


==============
Column Stack
==============

*Stack 1-D arrays as columns into a 2-D array.*

**Syntax** : numpy.column_stack(tup)

**Arguments** : 

1. *Tup: Arrays to stack*

**Dimenssion & Shape** : *All of them must have the same first dimension*
 
**Returns** : *The array formed by stacking the given arrays.*



******************
4.Splitting Arrays
******************


=======
Split
=======

*Split an array into multiple sub-arrays.*

**Syntax** : numpy.split(ary,indices_or_sections,axis=0)

**Arguments** :

1. *ary: Array to be divided into sub-arrays.*

2. *indices_or_sections :* 
             a. *If(N) - divided into N equal arrays*
             b. *if(1-D array) -  indicate where along axis the array is split*

3. *Axis: The axis along which to split, default is 0.*

**Returns** : *A list of sub-arrays.*

**Error** : *If indices_or_sections is given as an integer, but a split does not result in equal division.*



========
Hsplit
========

*Split an array into multiple sub-arrays horizontally (column-wise).*

**Syntax** : numpy.hsplit(ary,indices_or_sections)

**Arguments** :

1. *ary: Array to be divided into sub-arrays.*


========
Vsplit
========

*Split an array into multiple sub-arrays vertically (row-wise).*

**Syntax** : numpy.vsplit(ary,indices_or_sections)

**Arguments** :

1. *ary: Array to be divided into sub-arrays.*
