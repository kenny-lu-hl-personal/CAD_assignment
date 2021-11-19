# How to use

The [user guide](https://github.com/kenny-lu-hl/CAD_assignment/blob/master/docs/user_guide.md) explains the classes and methods, and gives examples of how to use them.

# Requirements

A design object is an object used to represent a collection of shapes in a 2D coordinate system. A shape is a rectangle object and includes information about where they lie within the parent design object with respect to the 0,0 (origin). In addition to shapes, a design can have other designs embedded within it. These are modeled through Instance objects. For example, a design object d1 can contain an instance i1 which has two pieces of information – a reference to another design object d2 and where d2’s origin is situated within the 2D coordinates of d1.

The objective of the programming assignment is to implement the following:

a. The first task is to model the above (design, shape, instance) using appropriate classes/functions

b. Given a design object, write a function that returns a list of shapes in that design object such that they are sorted descending by their area. You can ignore instances within the given design as we are concerned only with the shapes in top level of the hierarchy in this function.

c. Given a design object, write a function to return all the shapes within 1 level of hierarchy such that the locations of the shapes are described with respect to the 0,0 of the top-level design. Consider the following example. Design d1 contains shape r1 and instance i1. i1 refers to design d2. d2 contains shape r2 and instance i2. Your function should return the location of shapes r1 and r2 with respect to 0,0 of the design d1. You do not need to consider any shapes or instances within design referenced by i2 as it is at level 2 in the hierarchy. We are concerned only till level 1 of hierarchy in this function.

# Assumptions

1. A shape cannot have negative width and/or height.

2. A user should be able to get shapes in a design and updates those shapes. If there is a shape `s1` contained in a parent design `d1`. Given `d1`, user should be able to retrieve `s1` and change `s1`'s location(offset) relative to `d1`.

3. A user should be able to get instances in a parent design and updates those instances. User can change an instance's location and design reference.

4. All shapes within designs are unique. No two shapes in any design(s) should refer to the same shape object. Otherwise, when a user updates a shape object (such as changing it's location), the user may inadvertently update all shapes referring to that same object.

   Assume there is a shape `s1`, a design `d1`, and another design `d2`. `s1` cannot be in both `d1` and `d2`. If `s1` is allowed to be in both `d1` and `d2`, the following may happen: A user wants to move `s1` relative to `d1`, so the user update's `s1`'s offset to its parent design. The user is unaware that `s1` also has `d2` as a parent. Now the user has inadvertently moved `s1`'s location relative to `d2`.

5. Design references of instances do not need to be unique. Several instance objects can use the same design object as a design reference. When a design object is updated, the change is reflected in all instances that use it as a reference design.

# Edge Cases

### 1. Cyclic Design References

<ul>

_This edge case is unresolved_. The implementation does not prevent creation of cyclic design references.

A user can create a design `d1` containing instance `i1`, which contains `d1`  
This causes a never ending cycle d1 -> i1 -> d1 -> i1 -> ...

Assuming a `d1` represents actual physical shapes (such as masks in the fabrication process), an infinite design depth (cycle) most likely does not make sense.

</ul>

### 2) Width and height for a shape must both be >= 0.

<ul>

An exception is raised when attempting to set them to a negative value.

</ul>

### 3) Width, height, x offset, y offset for shapes are limited to integer values.

<ul>

An exception is raised when attempting to set them to non-integer values.

</ul>

### 4) x offset and y offset for instances are limited to integer values.

<ul>

An exception is raised when attempting to set them to non-integer values.

</ul>

### 5) Design contains several instances of the same design.

<ul>

A design can contain several instances referring to the same design object. For example, design `d_top` can contain instances `i1`, `i2`, and `i3`. The three instances have the same design object `d_embedded` as the referenced for the embedded design. When getting all shapes within one level of `d1`, each shape in `d_embedded` must accounted for 3 times (once for `i1`, once for `i2`, and once for `i3`).

</ul>

### 6) Designs with no instances.

<ul>

When getting shapes within 1 level of a design that contains no instances, just return the shapes at the design's own-level (if any exists).

</ul>

### 7) Designs with several levels of hierarchy.

<ul>

When getting shapes within 1 level of a design, ensure that the function does not return shapes more than 1 level deep.
Suppose a design `d1` has an instance of `d2`, which has an instance of `d3`. (`d1` -> `d2` -> `d3`)
Suppose the design `d3` has several shapes. Getting shapes within 1 level of `d1` should only return shapes in `d1` and `d2`.

</ul>

### 8) Adding a non-shape or non-instance type object to a design.

<ul>

An exception is raised when attempting to add a non-shape or non-instance type object to a design object.

</ul>

### 9) Side effects when getting shapes 1 level deep and their locations w.r.t. parent design.

<ul>

Suppose design `d1` has an instance of `d2` which is offset by (5,5). There is a shape `s` in `d2`. When getting all shapes within 1 level of `d1`, we cannot simply get the shape object `s` and shift its offsets by (5,5). That would move the `s` relative to both `d1` and `d2`. Instead, a new shape object is created with the same dimensions and offsets as `s`. Its offet is adjusted by (5, 5), and the new shape object is returned to represent `s`.

</ul>

# Further Improvements

### 1) Add methods to delete Shapes and Instances from a Design.

### 2) Use case dependent: Use a balanced binary search tree to store shapes in Design.

<ul>

Design.get_shapes_inorder_of_descending_area() uses the sort() method to sort the shapes by area.
The runtime for sort() is O(nlogn). By keeping the shapes in a balanced BST, the shapes are always maintained in sorted order.
Getting them in sorted order will be faster and take just O(n) runtime.
However, inserting or deleting a shape will become slower and take O(logn).

</ul>
### 3) Resolve the cyclic design references (mentioned in Edge Cases).

<ul>

To prevent cyclic designs when adding an instance `i` to a design `d`, we must check all embedded designs within `i` and all ancestor designs (parent design of `d` and its parent recursively) of `d`. If a design exists in `i`'s embedded designs and also in `d`'s ancestors, it will cause a cyclic design reference.

</ul>

### 4) Write generator functions to generate test data in unit tests.

Their is a lot of boilerplate/repeated code when when generating test designs, test shapes, and expected results in some unit test functions.
For example, populating the Counter `expected_shifted_shapes_cnt` takes several lines of similar code.
A better approach leading to cleaner code would be to write a function `generate_expected_results()` that generates and returns the Counter `expected_shifted_shapes_cnt`.
Another function `generate_test_designs()` can be written to generate and return all test designs.

````python
# In test_design.py
def test_get_shapes_within_one_level_with_multiple_instances_of_same_design():
    """
    An enclosing design can contain several instances that refer to the same embedded design.
    When getting shapes within 1 level of the enclosing design,
    shapes are returned for each instance of the embedded design adjusted by the offset of each individual instance.
    """
    x_offset_s1, y_offset_s1, width_s1, height_s1 = -5, -5, 10, 20
    x_offset_s2, y_offset_s2, width_s2, height_s2 = 5, 5, 40, 20

    design_embedded = Design()
    design_embedded.add_shape(x_offset_s1, y_offset_s1, width_s1, height_s1)
    design_embedded.add_shape(x_offset_s2, y_offset_s2, width_s2, height_s2)

    design_top = Design()
    x_offset_inst1, y_offset_inst1 = -10, 10
    x_offset_inst2, y_offset_inst2 = 0, 0
    design_top.add_instance(x_offset_inst1, y_offset_inst1, design_embedded)
    design_top.add_instance(x_offset_inst2, y_offset_inst2, design_embedded)  # embedded design is instantiated twice

    expected_shifted_shapes_cnt = Counter()
    expected_shifted_shapes_cnt[((x_offset_s1 + x_offset_inst1, y_offset_s1 + y_offset_inst1), (width_s1, height_s1))] += 1
    expected_shifted_shapes_cnt[((x_offset_s2 + x_offset_inst1, y_offset_s2 + y_offset_inst1), (width_s2, height_s2))] += 1
    expected_shifted_shapes_cnt[((x_offset_s1 + x_offset_inst2, y_offset_s1 + y_offset_inst2), (width_s1, height_s1))] += 1
    expected_shifted_shapes_cnt[((x_offset_s2 + x_offset_inst2, y_offset_s2 + y_offset_inst2), (width_s2, height_s2))] += 1

    shifted_shapes = design_top.get_shapes_within_one_level()
    shifted_shapes_cnt = Counter()
    for shape in shifted_shapes:
        shifted_shapes_cnt[(shape.get_offsets(), shape.get_dimensions())] += 1

    assert shifted_shapes_cnt == expected_shifted_shapes_cnt
    ```
````
