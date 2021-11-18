import pytest
#from src.instance import Instance
#from src.design import Design
import src.design as d
import src.instance as i


def test_non_design_ref():
    with pytest.raises(TypeError):
        i.Instance(0, 0, "not a design")


def test_non_integer_x_offset():
    with pytest.raises(TypeError):
        i.Instance(-1.5, 0, d.Design())


def test_non_integer_y_offset():
    with pytest.raises(TypeError):
        i.Instance(0, -1.5, d.Design())


def test_get_design_ref():
    design_to_add = d.Design()
    inst = i.Instance(0, 0, design_to_add)
    assert inst.get_design_ref() is design_to_add


def test_get_offsets():
    inst = i.Instance(1, -1, d.Design())
    assert inst.get_offsets() == (1, -1)
