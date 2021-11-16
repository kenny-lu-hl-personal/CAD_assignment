import pytest
from src.shape import Shape
from src.design import Design
from src.instance import Instance


def test_add_non_shape_type():
    """Design.add_shape() must raise TypeError if it is passed an object which is not a shape
    """
    design = Design()
    with pytest.raises(TypeError):
        design.add_shape("not a shape")


def test_get_shapes():
    """Design.get_shapes() must return an empty list if no shapes have been added to the design
    """
    design = Design()
    retrieved_shapes = design.get_shapes()
    assert retrieved_shapes == []


def test_add_and_get_shapes():
    """Design.get_shapes() can returns copies of shapes added by Design.add_shapes()
    """
    design = Design()
    shape_1 = Shape(0, 0, 1, 1)
    shape_2 = Shape(1, 1, 2, 2)
    design.add_shape(shape_1)
    design.add_shape(shape_2)
    retrieved_shapes = design.get_shapes()
    assert retrieved_shapes == [shape_1, shape_2]


def test_added_shape_copy():
    """Design.add_shapes() returns a copy of the shape it created an added to the design
    """
    design = Design()
    shape_1 = Shape(0, 1, 2, 3)
    shape_1_copy = design.add_shape(shape_1)
    assert shape_1 == shape_1_copy  # added copy has same offset and dimensions
    shape_1.set_offset(5, 5)
    assert shape_1 != shape_1_copy  # changing original shape does not affect copy


def test_get_shapes_inorder_of_descending_area():
    """Design.get_shapes_inorder_of_descending_area() returns shapes sorted by area (descending order)
    """
    design = Design()
    shape_1 = Shape(0, 0, 1, 1)
    shape_2 = Shape(0, 0, 1, 1)
    shape_3 = Shape(0, 0, 5, 5)
    shape_4 = Shape(0, 0, 2, 2)
    design.add_shape(shape_1)
    design.add_shape(shape_2)
    design.add_shape(shape_3)
    design.add_shape(shape_4)
    sorted_shapes = design.get_shapes_inorder_of_descending_area()
    assert sorted_shapes == [shape_3, shape_4, shape_1, shape_2]


def test_add_non_instance_type():
    """Design.add_instance() raises an error if input argument is not of type Instance"""
    design = Design()
    with pytest.raises(TypeError):
        design.add_instance("not an instance")


def test_add_and_get_instance():
    top_design, embedded_design = Design(), Design()
    instance = Instance(0, 0, embedded_design)
    top_design.add_instance(instance)
    top_design_instances = top_design.get_instances()
    assert top_design_instances[0].get_design_ref(
    ) is instance.get_design_ref()


def test_get_shapes_within_one_level_on_empty_designs():

    top_design, embedded_design_1, embedded_design_2 = Design(), Design(), Design()
    inst_1, inst_2 = Instance(0, 0, embedded_design_1), Instance(
        0, 0, embedded_design_2)
