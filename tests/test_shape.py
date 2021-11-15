import pytest
from src.shape import Shape


def test_get_area():
    """Test if Shape.get_area() calculates correct area.
    """
    test_shape = Shape(0, 0, 2, 5)
    assert test_shape.get_area() == 10


def test_invalid_height():
    """Shape() must raise Value Error if input length argument <= 0.
    """
    with pytest.raises(ValueError):
        test_shape = Shape(0, 0, 1, 0)


def test_invalid_width():
    """Shape() must raise Value Error if input width argument <= 0.
    """
    with pytest.raises(ValueError):
        test_shape = Shape(0, 0, 0, 1)


def test_non_integer_width():
    """Shape() must raise Type Error if its input arguments are not integers.
    """
    with pytest.raises(TypeError):
        test_shape = Shape(0, 0, 1, 1.5)


def test_non_integer_height():
    """Shape() must raise Type Error if its input arguments are not integers.
    """
    with pytest.raises(TypeError):
        test_shape = Shape(0, 0, 1.5, 1)


def test_non_integer_x_offset():
    """Shape() must raise Type Error if its input arguments are not integers.
    """
    with pytest.raises(TypeError):
        test_shape = Shape(1.0, 0, 1, 1)


def test_non_integer_y_offset():
    """Shape() must raise Type Error if its input arguments are not integers.
    """
    with pytest.raises(TypeError):
        test_shape = Shape(0, 1.0, 1, 1)
