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


def test_add_shape_copy():
    """Design.add_shape_copy() returns a copy of the shape it created an added to the design
    """
    design = Design()
    shape_1 = Shape(0, 1, 2, 3)
    shape_1_copy = design.add_shape_copy(shape_1)
    assert shape_1 == shape_1_copy  # added copy has same offset and dimensions
    shape_1.set_offsets(5, 5)
    assert shape_1 != shape_1_copy  # changing original shape does not affect copy. They now have different offets.


def test_add_shape_copy_and_get_shapes():
    """Design.get_shapes() returns copies of shapes added by Design.add_shape_copy()
    """
    design = Design()
    shape_1 = Shape(0, 0, 1, 1)
    shape_2 = Shape(1, 1, 2, 2)
    design.add_shape_copy(shape_1)
    design.add_shape_copy(shape_2)
    retrieved_shapes = design.get_shapes()
    assert retrieved_shapes == [shape_1, shape_2]


def test_add_shape_and_get_shapes():
    """Design.get_shapes() returns the shapes created and added by Design.add_shapes()
    """
    design = Design()
    shape_1 = design.add_shape(0, 0, 5, 10)
    shape_2 = design.add_shape(-1, -1, 5, 15)
    retrieved_shapes = design.get_shapes()
    assert retrieved_shapes == [shape_1, shape_2]


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
    assert design.get_shapes_inorder_of_descending_area() == [shape_3, shape_4, shape_1, shape_2]


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
    assert design.get_shapes_inorder_of_descending_area() == [shape_3, shape_4, shape_1, shape_2]


def test_add_non_instance_type():
    """Design.add_instance_copy() raises an error if input argument is not of type Instance"""
    design = Design()
    with pytest.raises(TypeError):
        design.add_instance_copy("not an instance")


def test_add_instance_copy_and_get_instance():
    top_design, embedded_design = Design(), Design()
    instance = Instance(0, 0, embedded_design)
    top_design.add_instance_copy(instance)
    top_design_instances = top_design.get_instances()
    assert top_design_instances[0].get_offsets() == (0, 0)
    assert top_design_instances[0].get_design_ref() is instance.get_design_ref()


def test_add_instance_and_get_instance():
    top_design, embedded_design = Design(), Design()
    instance = top_design.add_instance(0, 0, embedded_design)
    top_design_instances = top_design.get_instances()
    assert top_design_instances[0] is instance


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
    design_bottom = Design()
    design_bottom.add_shape(-10, -100, 20, 30)
    design_bottom.add_shape(10, -100, 10, 10)  # design at bottom level has 2 shapes

    design_mid = Design()
    design_mid.add_instance(50, 50, design_bottom)  # design at mid level has no shapes

    design_top = Design()
    design_top.add_instance(12, 1, design_mid)  # design at top has no shapes
    assert design_top.get_shapes_within_one_level() == []


def test_get_shapes_within_one_level_returns_depth_0_shapes():
    """
    When get_shapes_within_one_level() is called on a design, it returns shapes representing shapes in that design.
    Shapes at depth 0 (contained by the design and not the embedded designs) do not need their x and y offsets adjusted.
    """
    x_offset_s1, y_offset_s1, width_s1, height_s1 = -5, -5, 10, 20
    x_offset_s2, y_offset_s2, width_s2, height_s2 = 5, 5, 40, 20

    design = Design()
    design.add_shape(x_offset_s1, y_offset_s1, width_s1, height_s1)
    design.add_shape(x_offset_s2, y_offset_s2, width_s2, height_s2)
    design.add_shape(x_offset_s2, y_offset_s2, width_s2, height_s2)

    expected_shifted_shapes_cnt = Counter()
    expected_shifted_shapes_cnt[((x_offset_s1, y_offset_s1), (width_s1, height_s1))] += 1
    expected_shifted_shapes_cnt[((x_offset_s2, y_offset_s2), (width_s2, height_s2))] += 2

    shifted_shapes = design.get_shapes_within_one_level()
    shifted_shapes_cnt = Counter()
    for shape in shifted_shapes:
        shifted_shapes_cnt[(shape.get_offsets(), shape.get_dimensions())] += 1

    assert shifted_shapes_cnt == expected_shifted_shapes_cnt


def test_get_shapes_within_one_level_returns_depth_1_shapes():
    """Design has no shapes, but its embedded designs have shapes. Return shapes of embedded designs.
    """
    x_offset_s1, y_offset_s1, width_s1, height_s1 = -5, -5, 10, 20
    x_offset_s2, y_offset_s2, width_s2, height_s2 = 5, 5, 40, 20

    design_embedded = Design()
    design_embedded.add_shape(x_offset_s1, y_offset_s1, width_s1, height_s1)
    design_embedded.add_shape(x_offset_s2, y_offset_s2, width_s2, height_s2)

    design_top = Design()
    x_offset_inst, y_offset_inst = -10, 10
    design_top.add_instance(x_offset_inst, y_offset_inst, design_embedded)

    expected_shifted_shapes_cnt = Counter()
    expected_shifted_shapes_cnt[((x_offset_s1 + x_offset_inst, y_offset_s1 + y_offset_inst), (width_s1, height_s1))] += 1
    expected_shifted_shapes_cnt[((x_offset_s2 + x_offset_inst, y_offset_s2 + y_offset_inst), (width_s2, height_s2))] += 1

    shifted_shapes = design_top.get_shapes_within_one_level()
    shifted_shapes_cnt = Counter()
    for shape in shifted_shapes:
        shifted_shapes_cnt[(shape.get_offsets(), shape.get_dimensions())] += 1

    assert shifted_shapes_cnt == expected_shifted_shapes_cnt


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


def test_get_shapes_within_one_level_with_shapes_and_embedded_shapes():
    """
    When getting shapes within 1 level of an enclosing design, 
    shapes belonging to the enclosing design and all embedded designs should be returned.
    """
    x_offset_s1, y_offset_s1, width_s1, height_s1 = -5, -5, 10, 20
    x_offset_s2, y_offset_s2, width_s2, height_s2 = 5, 5, 40, 20
    x_offset_s3, y_offset_s3, width_s3, height_s3 = 2, 10, 7, 22
    x_offset_s4, y_offset_s4, width_s4, height_s4 = 0, 0, 9, 100
    x_offset_inst1, y_offset_inst1 = -10, 10
    x_offset_inst2, y_offset_inst2 = 10, -10

    design_embedded_1 = Design()
    design_embedded_1.add_shape(x_offset_s1, y_offset_s1, width_s1, height_s1)
    design_embedded_1.add_shape(x_offset_s2, y_offset_s2, width_s2, height_s2)

    design_embedded_2 = Design()
    design_embedded_2.add_shape(x_offset_s3, y_offset_s3, width_s3, height_s3)

    design_top = Design()
    design_top.add_shape(x_offset_s4, y_offset_s4, width_s4, height_s4)
    design_top.add_instance(x_offset_inst1, y_offset_inst1, design_embedded_1)
    design_top.add_instance(x_offset_inst2, y_offset_inst2, design_embedded_2)

    expected_shifted_shapes_cnt = Counter()
    expected_shifted_shapes_cnt[((x_offset_s1 + x_offset_inst1, y_offset_s1 + y_offset_inst1), (width_s1, height_s1))] += 1
    expected_shifted_shapes_cnt[((x_offset_s2 + x_offset_inst1, y_offset_s2 + y_offset_inst1), (width_s2, height_s2))] += 1
    expected_shifted_shapes_cnt[((x_offset_s3 + x_offset_inst2, y_offset_s3 + y_offset_inst2), (width_s3, height_s3))] += 1
    expected_shifted_shapes_cnt[((x_offset_s4, y_offset_s4), (width_s4, height_s4))] += 1

    shifted_shapes = design_top.get_shapes_within_one_level()
    shifted_shapes_cnt = Counter()
    for shape in shifted_shapes:
        shifted_shapes_cnt[(shape.get_offsets(), shape.get_dimensions())] += 1

    assert shifted_shapes_cnt == expected_shifted_shapes_cnt


def test_get_shapes_within_one_level_no_side_effects():
    """
    get_shapes_within_one_level() should return copies of shapes in the design and its embedded design's.
    If a copied shape is in an instance/embedded  design, its x and y offsets are shifted by the instance's offsets.
    This prevents the shapes in the design from being modified.
    """
    x_offset_s1, y_offset_s1, width_s1, height_s1 = -5, -5, 9, 7
    x_offset_s2, y_offset_s2, width_s2, height_s2 = 43, -12, 40, 20
    x_offset_inst, y_offset_inst = -10, 10

    design_embedded = Design()
    design_embedded.add_shape(x_offset_s1, y_offset_s1, width_s1, height_s1)

    design_top = Design()
    design_top.add_shape(x_offset_s2, y_offset_s2, width_s2, height_s2)
    design_top.add_instance(x_offset_inst, y_offset_inst, design_embedded)

    shifted_shapes = design_top.get_shapes_within_one_level()
    for shifted_shape in shifted_shapes:
        shifted_shape.shift_offsets(-5, 1000)

    s1 = design_embedded.get_shapes()[0]
    s2 = design_top.get_shapes()[0]

    assert len(shifted_shapes) == 2
    assert s1.get_offsets() == (x_offset_s1, y_offset_s1)
    assert s2.get_offsets() == (x_offset_s2, y_offset_s2)
