# Usage

### Import the Shape, Design, and Instance classes

```python
from src.shape import Shape
from src.design import Design
from src.instance import Instance
```

## Shape

\_\_init\_\_(x_offset, y_offset, width, height)

> Initializes offset and dimensions.
>
> Args:  
> x_offset (int): x offset with respect to the origin (0,0) of the enclosing design  
> y_offset (int): y offset with respect to the origin (0,0) of the enclosing design  
> width (int): width of rectangle. Must be a positive integer  
> height (int): height of rectangle. Must be a positive integer
>
> Raises:  
> TypeError: Inputs must be of integer type, else type error is raised.  
> ValueError: Width and height must be positive integers, else ValueError is raised.

```python
>>> s = Shape(-1, -1, 5, 10)
>>> s.get_offsets()
(-1, -1)
>>> s.get_dimensions()
(5, 10)
```

set_offsets(x_offset: int, y_offset: int)

> Sets the offset with respect to the origin (0, 0) of the enclosing(parent) design
>
> Args:  
> x_offset (int): x offset with respect to the origin (0,0) of the enclosing design  
> y_offset (int): y offset with respect to the origin (0,0) of the enclosing design
>
> Raises:  
> TypeError: Inputs must be of integer type.

```python
>>> s = Shape(0, 0, 2, 5)
>>> s.get_offsets()
(0, 0)
>>> s.set_offsets(-1, 1)
>>> s.get_offsets()
(-1, 1)
```

shift_offsets(x_offset_delta: int, y_offset_delta: int)

> Shifts the shape's current x and y offsets by the specified distances.
>
> Args:  
> x_offset_delta (int): added to current x offset  
> y_offset_delta (int): added to current y offset
>
> Raises:  
> TypeError: Inputs must be of integer type.

```python
>>> s = Shape(0, 0, 2, 5)
>>> s.get_offsets()
(0, 0)
>>> s.shift_offsets(10, -10)
>>> s.get_offsets()
(10, -10)
```

set_dimensions(width: int, height: int)

> Sets the height and width of the rectangle.
>
> Args:  
> width (int): width of rectangle. Must be a positive integer  
> height (int): height of rectangle. Must be a positive integer
>
> Raises:  
> TypeError: Raised if width and height are not integers  
> ValueError: Raised if width and height are not positive integers

```python
>>> s = Shape(0, 0, 5, 10)
>>> s.get_dimensions()
(5, 10)
>>> s.set_dimensions(10, 20)
>>> s.get_dimensions()
(10, 20)
```

get_offsets()

> Returns offset with respect to parent Design
>
> Returns:  
> (Tuple[int]): x and y offsets of the shape (x_offset, y_offset)

```python
>>> s = Shape(0, 0, 2, 5)
>>> s.get_offsets()
(0, 0)
>>> s.shift_offsets(10, -10)
>>> s.get_offsets()
(10, -10)
```

get_dimensions()

> Returns dimensions of a shape.
>
> Returns:  
> (Tuple[int]): Width and height of the shape. (width, height)

```python
>>> s = Shape(0, 0, 5, 10)
>>> s.get_dimensions()
(5, 10)
```

get_area()

> Returns area of a shape
>
> Returns:  
> (int): Area of the shape represented by Shape instance

```python
>>> s = Shape(0, 0, 5, 10)
>>> s.get_dimensions()
(5, 10)
>>> s.get_area()
50
```

\_\_eq\_\_(other)

> Checks if two shapes are equal.
>
> Returns:
> (bool): True if the two shapes have same dimensions and offsets from parent.

```
>>> s1 = Shape(0, 0, 5, 10)
>>> s2 = Shape(0, 0, 5, 10)
>>> s1 == s2
True
>>> s3 = Shape(1, 0, 5, 10)
>>> s1 == s3
False
```

\_\_str\_\_()

> Returns:  
> (str): String containing the x offset, y offset, width, and height of the rectangle

```python
>>> s1 = Shape(-10, 10, 78, 32)
>>> print(s1)
x_offset:-10, y_offset:10, w:78, h:32
>>> s1.str()
>>> str(s1)
'x_offset:-10, y_offset:10, w:78, h:32'
```

## Design

\_\_init\_\_()

> Initializes the design instance. A design starts out empty, without any shapes or instances.
>
> self.\_shapes = []  
> self.\_instances = []

```python
>>> d = Design()
>>> d.get_shapes()
[]
>>> d.get_instances()
[]
```

add_shape(x_offset: int, y_offset: int, height: int, width: int)

> Creates a shape with the given parameters and adds it to the design.  
> Returns the newly created and added shape.
>
> Args:  
> x_offset (int): x offset with respect to the origin (0,0) of the parent design  
> y_offset (int): y offset with respect to the origin (0,0) of the parent design  
> width (int): Width of shape. Must be a positive integer  
> height (int): Height of shape. Must be a positive integer
>
> Returns:  
> (Shape): The newly created shape that was added to the design.

```python
>>> d = Design()
>>> s = d.add_shape(-1, 1, 5, 10)
>>> s
<src.shape.Shape object at 0x00CAE760>
>>> d.get_shapes()
[<src.shape.Shape object at 0x00CAE760>]
>>> s.get_offsets()
(-1, 1)
>>> s.get_dimensions()
(5, 10)
```

add_shape_copy(shape: Shape)

> Creates a deep copy of an existing shape and adds the copy to the design.  
> Returns the newly created copy.  
> Adding a copy ensures that every shape inside a design refers to an unique shape object. No two shapes in any design(s) should refer to the same shape object.
>
> Args:  
> shape (Shape): Shape to be copied. Its copy will be added to the design.
>
> Returns:  
> (Shape): The newly created copy added to design.

```python
>>> d = Design()
>>> s = Shape(-1, 1, 5, 10)
>>> s
<src.shape.Shape object at 0x00CAE880>

>>> s_copy = d.add_shape_copy(s)
>>> s_copy
<src.shape.Shape object at 0x00CAE8B0>  #Note the different memory addr. This is a new (copied) shape object.
>>> d.get_shapes()
[<src.shape.Shape object at 0x00CAE8B0>]  #The copied shape object is added to design

>>> s_copy.get_offsets()  #Copy has same offsets as the original shape
(-1, 1)
>>> s_copy.get_dimensions()  #Copy has same dimensions as original shape
(5, 10)
```

add_instance(x_offset: int, y_offset: int, design_ref: Design)

> Creates an instance with the given parameters and adds it to the design.  
> Returns the newly created and added instance.
>
> Args:  
> x_offset (int): x offset with respect to the origin (0,0) of the parent design  
> y_offset (int): y offset with respect to the origin (0,0) of the parent design  
> design_ref (Design): design that the instance will refer to
>
> Returns:  
> (Instance): The newly created instance that was added to the design.

```python
>>> d_embedded = Design()
>>> d_top = Design()
>>> i = d_top.add_instance(-1, 1, d_embedded)
>>> i
<src.instance.Instance object at 0x00CAE9E8>
>>> d_top.get_instances()
[<src.instance.Instance object at 0x00CAE9E8>]

>>> i.get_offsets()
(-1, 1)
>>> i.get_design_ref() is d_embedded
True
```

add_instance_copy(inst: Instance)

> Creates a shallow copy of an existing instance and adds the copy to the design.  
> Returns the newly created copy.
>
> The copy has the same x and y offets as the original instance.  
> It also contains a reference to the same design object referenced by the original instance.  
> Several instance objects can use the same design object as a design reference.  
> When a design object is updated, the change is reflected in all instances that use it as a reference design.
>
> Args:  
> inst (Instance): Instance to be copied. Its copy will be added to the design.
>
> Returns:  
> (Instance): The newly created copy added to design.

```python
>>> d_embedded = Design()
>>> d_top = Design()
>>> i = Instance(-1, 1, d_embedded)
>>> i_copy = d_top.add_instance_copy(i) #add an instance of d_embedded to d_top

>>> i
<src.instance.Instance object at 0x00CAEA48>
>>> i_copy
<src.instance.Instance object at 0x00CAE9B8> #Note the different memory addr. Returned instance is a new instance object.
>>> d_top.get_instances()
[<src.instance.Instance object at 0x00CAE9B8>] #The new instance(copy) is added the d_top

>>> i.get_offsets()
(-1, 1)
>>> i_copy.get_offsets() #The copy has same offets as the original instance
(-1, 1)
>>> i.get_design_ref() == i_copy.get_design_ref() #The copy refers to the same design object as the original instance.
True
```

get_instances()

> Returns a list of instances belonging to the design.  
> Does not return instances belonging to other designs embedded within the design.
>
> Returns:  
> (List[Instance]): List of instances in the design.

```python
>>> d_bottom = Design()
>>> d_mid = Design()
>>> d_mid.add_instance(0, 0, d_bottom) #add an instance of d_bottom to d_mid
<src.instance.Instance object at 0x00CAEAA8>

#add 3 instances of d_mid to a top level design d_top
>>> d_top = Design()
>>> d_top.add_instance(1, 1, d_mid)
<src.instance.Instance object at 0x00CAEA78>
>>> d_top.add_instance(2, 2, d_mid)
<src.instance.Instance object at 0x00CAEAF0>
>>> d_top.add_instance(3, 3, d_mid)
<src.instance.Instance object at 0x00CAEB38>

#When get_instances() is called on d_top, it returns the 3 instances of d_mid.
#The instance of d_bottom is not returned, because it is another level down (in d_mid and not d_top)
>>> d_top.get_instances()
[<src.instance.Instance object at 0x00CAEA78>, <src.instance.Instance object at 0x00CAEAF0>, <src.instance.Instance object at 0x00CAEB38>]
>>> len(d_top.get_instances())
3
```

get_shapes()

> Returns a list of shapes in the design.  
> If the design contains/embeds other designs,  
> the shapes of those embedded designs are NOT included in the list.
>
> Returns:  
> (List[Shape]): List of shapes in the design.

```python
>>> d_embedded = Design()
>>> s1 = d_embedded.add_shape(10,10,25,25)

>>> d_top = Design()
>>> i1 = d_top.add_instance(1, 1, d_embedded)
>>> s2 = d_top.add_shape(0,0,5,5)
>>> s3 = d_top.add_shape(0,0,2,2)

>>> d_top.get_shapes()  #Only returns s2 and s3. s1 is another level down hence its not returned.
[<src.shape.Shape object at 0x016FF550>, <src.shape.Shape object at 0x016FF580>]

>>> for shape in d_top.get_shapes():
...     print(shape)
...
x_offset:0, y_offset:0, w:5, h:5   #s2
x_offset:0, y_offset:0, w:2, h:2   #s3
```

get_shapes_inorder_of_descending_area()

> Returns a list of shapes in the design.  
> The shapes are sorted by area in descending order.  
> If the design contains/embeds other designs,  
> the shapes of those embedded designs are NOT included in the list.
>
> Returns:  
> (List[Shape]): List of shapes in the design sorted in order of descending area.

```python
>>> d_embedded = Design()
>>> s1 = d_embedded.add_shape(10,10,25,25)

>>> d_top = Design()
>>> i1 = d_top.add_instance(1, 1, d_embedded)
>>> s2 = d_top.add_shape(0, 0, 5, 5)
>>> s3 = d_top.add_shape(10, 10, 2, 2)
>>> s4 = d_top.add_shape(-10, -10, 20, 20)


>>> d_top.get_shapes_inorder_of_descending_area() #Does not return s1, since s1 is one level below.
[<src.shape.Shape object at 0x016FF628>, <src.shape.Shape object at 0x016FF478>, <src.shape.Shape object at 0x016FF5C8>]

>>> for shape in d_top.get_shapes_inorder_of_descending_area():
...     print(f'area: {shape.get_area()}, {shape}')
...
area: 400, x_offset:-10, y_offset:-10, w:20, h:20  #s4
area: 25, x_offset:0, y_offset:0, w:5, h:5         #s2
area: 4, x_offset:10, y_offset:10, w:2, h:2        #s3
```

get_shapes_within_one_level()

> Returns a list of shapes representing all shapes within 1 level of the design's hierarchy.  
> Only includes shapes at the design's own level, and shapes of its immediate instances/designs (one level down).  
> The shapes in the returned list are deep copies of the shapes in the design.  
> The copied shapes have their x and y offets updated such that they are now relative to the top-level design.  
> Copies are used so that shapes in the design do not have their x and y offsets modified by this function.
>
> Returns:  
> List[Shape]: List containing copies of shapes within 1 level, with their locations relative to top-level design.

```python
>>> design_embedded_1 = Design()
>>> s1 = design_embedded_1.add_shape(-5, -5, 10, 20)

>>> design_embedded_2 = Design()
>>> s2 = design_embedded_2.add_shape(19, 29, 90, 100)

>>> design_top = Design()
>>> i1 = design_top.add_instance(10, 10, design_embedded_1)
>>> i2 = design_top.add_instance(50, 50, design_embedded_2)
>>> s3 = design_top.add_shape(1, 1, 7, 9)

>>> design_top.get_shapes_within_one_level() #3 new shapes representing s1, s2, s3 and their locations
[<src.shape.Shape object at 0x016FF868>, <src.shape.Shape object at 0x016FF8C8>, <src.shape.Shape object at 0x016FF910>]

>>> for shape in design_top.get_shapes_within_one_level():
...     print(shape)
...
x_offset:1, y_offset:1, w:7, h:9      #s3 not shifted since it is at top-level
x_offset:5, y_offset:5, w:10, h:20    #s1 shifted by i1's offset (10, 10)
x_offset:69, y_offset:79, w:90, h:100 #s2 shifted by i2's offset (50, 50)

```

## Instance

\_\_init\_\_(x_offset, y_offset, design_ref)

> Initializes x and y offsets and reference design
>
> Args:  
>  x_offset (int): x offset with respect to origin (0,0) of the parent design  
>  y_offset (int): y offset with respect to origin (0,0) of the parent design  
>  design_ref (Design): design that the instance will refer to
>
> Raises:  
>  TypeError: Raised if input parameters are not of expected type.

```python
>>> d = Design()
>>> i = Instance(-1, 1, d)
>>> i.get_offsets()
(-1, 1)
>>> i.get_design_ref() is d
True
```

set_offsets(x_offset: int, y_offset: int)

> Sets the offsets with respect to the origin (0, 0) of the parent design
>
> Args:  
>  x_offset (int): x offset with respect to origin (0,0) of the parent design  
>  y_offset (int): y offset with respect to origin (0,0) of the parent design
>
> Raises:  
>  TypeError: Raised if input parameters are not integers

```python
>>> i = Instance(0, 0, Design())
>>> i.get_offsets()
(0, 0)

>>> i.set_offsets(5, 10) #update the x and y offsets
>>> i.get_offsets()
(5, 10)
```

set_design_ref(design_ref)

> Sets the design object that represents the embedded design
>
> Args:  
>  design_ref (Design): design object that the embedded design will refer to
>
> Raises:  
>  TypeError: Raised if input parameter is not of type Design

```python
>>> d1 = Design()  #Create design objects to use as embedded designs
>>> d2 = Design()
>>> d1 == d2
False

>>> i = Instance(0, 0, d1)  #Initialize an instance with d1 as an embedded design
>>> i.get_design_ref() is d1
True

>>> i.set_design_ref(d2)    #Change the embedded design reference to d2
>>> i.get_design_ref() is d2
True
```

get_offsets()

> Returns offset with respect to parent design
>
> Returns:  
>  (Tuple[int]): (x_offset, y_offset)

```python
>>> i = Instance(5, 10, Design())
>>> i.get_offsets()
(5, 10)
```

get_design_ref()

> Gets the reference design
>
> Returns:  
> (Design): The referenced design

```python
>>> d1 = Design()           #Create a design object to use as an embedded design
>>> i = Instance(0, 0, d1)  #Initialize an instance with d1 as an embedded design

>>> i.get_design_ref()
<src.design.Design object at 0x00F5F5B0>
>>> i.get_design_ref() is d1
True

```
