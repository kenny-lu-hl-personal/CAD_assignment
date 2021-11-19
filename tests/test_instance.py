import pytest
from src.instance import Instance
from src.design import Design


def test_non_integer_x_offset():
    """Should raise error when x_offset is assigned a non-integer value"""
    with pytest.raises(TypeError):
        Instance(-1.5, 0, Design())


def test_set_integer_y_offset():
    """Should raise error when y_offset is assigned a non-integer value"""
    with pytest.raises(TypeError):
        Instance(0, -1.5, Design())


def test_non_design_design_ref():
    """Should raise error when design ref is assigned a non Design object"""
    with pytest.raises(TypeError):
        Instance(0, 0, "not a design")


def test_get_design_ref():
    """get_design_ref() should return a reference to the same design that was assigned"""
    design_to_add = Design()
    inst = Instance(0, 0, design_to_add)
    assert inst.get_design_ref() is design_to_add


def test_get_offsets():
    """get_offsets() works with positive, negative, and zero x and y offset values
    """
    inst1 = Instance(-1, -2, Design())
    assert inst1.get_offsets() == (-1, -2)

    inst2 = Instance(-1, 2, Design())
    assert inst2.get_offsets() == (-1, 2)

    inst3 = Instance(1, -1, Design())
    assert inst3.get_offsets() == (1, -1)

    inst4 = Instance(0, 0, Design())
    assert inst4.get_offsets() == (0, 0)
