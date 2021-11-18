import pytest
from collections import Counter
from src.shape import Shape
from src.design import Design
from src.instance import Instance


def test_add_shape_copy_passed_non_shape_object():
    """Design.add_shape_copy() must raise TypeError if it is passed an object which is not a shape
    """
    design = Design()
    with pytest.raises(TypeError):
        design.add_shape_copy("not a shape")


def test_get_shapes():
    """Design.get_shapes() must return an empty list if no shapes have been added to the design
    """
    design = Design()
    retrieved_shapes = design.get_shapes()
    assert retrieved_shapes == []


def test_add_shape_copy_and_get_shapes():
    """Design.get_shapes() returns copies of shapes added by Design.add_shapes()
    """
    design = Design()
    shape_1 = Shape(0, 0, 1, 1)
    shape_2 = Shape(1, 1, 2, 2)
    design.add_shape_copy(shape_1)
    design.add_shape_copy(shape_2)
    retrieved_shapes = design.get_shapes()
    assert retrieved_shapes == [shape_1, shape_2]


def test_added_shape_copy():
    """Design.add_shapes() returns a copy of the shape it created an added to the design
    """
    design = Design()
    shape_1 = Shape(0, 1, 2, 3)
    shape_1_copy = design.add_shape_copy(shape_1)
    assert shape_1 == shape_1_copy  # added copy has same offset and dimensions
    shape_1.set_offset(5, 5)
    assert shape_1 != shape_1_copy  # changing original shape does not affect copy


def test_get_shapes_inorder_of_descending_area_1():
    """Design.get_shapes_inorder_of_descending_area() returns shapes sorted by area (descending order)
    """
    design = Design()
    shape_1 = Shape(0, 0, 1, 1)
    shape_2 = Shape(0, 0, 1, 1)
    shape_3 = Shape(0, 0, 5, 5)
    shape_4 = Shape(0, 0, 2, 2)
    design.add_shape_copy(shape_1)
    design.add_shape_copy(shape_2)
    design.add_shape_copy(shape_3)
    design.add_shape_copy(shape_4)
    sorted_shapes = design.get_shapes_inorder_of_descending_area()
    assert sorted_shapes[0] == shape_3
    assert sorted_shapes[1] == shape_4
    assert sorted_shapes[2] == shape_1
    assert sorted_shapes[3] == shape_2


def test_get_shapes_inorder_of_descending_area_2():
    """Design.get_shapes_inorder_of_descending_area() returns shapes sorted by area (descending order)
    """
    design = Design()
    shape_1 = Shape(-5, -5, 1, 1)
    shape_2 = Shape(5, 5, 1, 1)
    shape_3 = Shape(1, 2, 5, 5)
    shape_4 = Shape(-3, 10, 2, 2)
    design.add_shape_copy(shape_1)
    design.add_shape_copy(shape_2)
    design.add_shape_copy(shape_3)
    design.add_shape_copy(shape_4)
    sorted_shapes = design.get_shapes_inorder_of_descending_area()
    assert sorted_shapes[0] == shape_3
    assert sorted_shapes[1] == shape_4
    assert sorted_shapes[2] == shape_1
    assert sorted_shapes[3] == shape_2


def test_add_non_instance_type():
    """Design.add_instance_copy() raises an error if input argument is not of type Instance"""
    design = Design()
    with pytest.raises(TypeError):
        design.add_instance_copy("not an instance")


def test_add_and_get_instance():
    top_design, embedded_design = Design(), Design()
    instance = Instance(0, 0, embedded_design)
    top_design.add_instance_copy(instance)
    top_design_instances = top_design.get_instances()
    assert top_design_instances[0].get_design_ref() is instance.get_design_ref()


def test_get_shapes_within_one_level_on_empty_design():
    """When a design does not contain any shape or instance, there are no shapes within 1 level of hierarchy.
       get_shapes_within_one_level() should return empty list.
    """
    empty_design = Design()
    assert empty_design.get_shapes_within_one_level() == []


def test_get_shapes_within_one_level_on_empty_embedded_design():
    """When a design and its embedded designs do not contain any shape, there are no shapes within 1 level of hierarchy.
       get_shapes_within_one_level() should return empty list.
    """
    empty_design = Design()
    design_top = Design()
    design_top.add_instance(0, 0, empty_design)
    assert empty_design.get_shapes_within_one_level() == []  # design_top contains 1 instance of an empty design
    design_top.add_instance(5, 5, empty_design)
    assert empty_design.get_shapes_within_one_level() == []  # design_top contains 2 instances of an empty design


def test_get_shapes_within_one_level_stops_within_one_level():
    """get_shapes_within_one_level() should only look down 1 level of design hierarchy.
       It should not return shapes deeper than 1 level of hierarchy.
    """
    design_3 = Design()
    design_3.add_shape(-10, -100, 20, 30)
    design_3.add_shape(10, -100, 10, 10)  # design at bottom level has 2 shapes

    design_2 = Design()
    design_2.add_instance(50, 50, design_3)  # design at mid level has no shapes

    design_1 = Design()
    design_1.add_instance(12, 1, design_2)  # design at top  has no shapes
    assert design_1.get_shapes_within_one_level() == []


def test_get_shapes_within_one_level_returns_depth_0_shapes():
    """
    top design multiple instances of same design. get shapes from all of these instances
    """
    x_offset_1, y_offset_1, width_1, height_1 = -5, -5, 10, 20
    x_offset_2, y_offset_2, width_2, height_2 = 5, 5, 40, 20

    design = Design()
    design.add_shape(x_offset_1, y_offset_1, width_1, height_1)
    design.add_shape(x_offset_2, y_offset_2, width_2, height_2)

    expected_retrieved_shapes_counter = Counter()
    expected_retrieved_shapes_counter[((x_offset_1, y_offset_1), (width_1, height_1))] += 1
    expected_retrieved_shapes_counter[((x_offset_2, y_offset_2), (width_2, height_2))] += 1

    retrieved_shapes = design.get_shapes_within_one_level()
    retrieved_shapes_counter = Counter()
    for shape in retrieved_shapes:
        retrieved_shapes_counter[(shape.get_offsets(), shape.get_dimensions())] += 1

    assert retrieved_shapes_counter == expected_retrieved_shapes_counter


# design has no shapes, it must return empty

# design's instances has no shapes, must return empty

# design has no shapes, but its instances have, return shapes of instances

# design
