import pytest
from src.instance import Instance
from src.design import Design


def test_non_design_ref():
    with pytest.raises(TypeError):
        test_instance = Instance(0, 0, "not a design")


def test_non_integer_x_offset():
    with pytest.raises(TypeError):
        test_instance = Instance(-1.5, 0, Design())


def test_non_integer_y_offset():
    with pytest.raises(TypeError):
        test_instance = Instance(0, -1.5, Design())


def test_get_design_ref():
    design_to_add = Design()
    test_instance = Instance(0, 0, design_to_add)
    assert test_instance.get_design_ref() is design_to_add


def test_get_offset():
    test_instance = Instance(1, -1, Design())
    assert test_instance.get_offset() == (1, -1)
