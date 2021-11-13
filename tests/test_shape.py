import pytest
from src.shape import Shape


def test_get_area():
    test_shape = Shape(0, 0, 2, 5)
    assert test_shape.get_area() == 10


def test_invalid_height():
    with pytest.raises(ValueError):
        test_shape = Shape(0, 0, 1, 0)


def test_invalid_width():
    with pytest.raises(ValueError):
        test_shape = Shape(0, 0, 0, 1)


def test_non_integer_width():
    with pytest.raises(TypeError):
        test_shape = Shape(0, 0, 1, 1.5)


def test_non_integer_height():
    with pytest.raises(TypeError):
        test_shape = Shape(0, 0, 1.5, 1)


def test_non_integer_x_offset():
    with pytest.raises(TypeError):
        test_shape = Shape(1.0, 0, 1, 1)


def test_non_integer_y_offset():
    with pytest.raises(TypeError):
        test_shape = Shape(0, 1.0, 1, 1)
