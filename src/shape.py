
class Shape:
    """
    A Shape instance represents a rectangle lying within a parent Design instance.

    Attributes:
        _x_offset (int): x offset with respect to origin (0,0) of its parent Design instance
        _y_offset (int): x offset with respect to origin (0,0) of its parent Design instance
        _height (int): height of rectangle
        _width (int): Width of rectangle

    Methods:
        def set_offset(self, x_offset: int, y_offset: int) -> None:
            Sets the offset with respect to origin of the parent Design.
        def set_dimensions(self, height: int, width: int) -> None:
            Sets the width  of the rectangle.
        def get_area(self) -> int:
            Returns area of the rectangle.
    """

    def __init__(self, x_offset: int, y_offset: int, height: int, width: int):
        """Initializes a Shape instance. Shape represents a rectangle contained in a Design instance.

        Args:
            x_offset (int): x offset with respect to origin (0,0) of its parent Design
            y_offset (int): x offset with respect to origin (0,0) of its parent Design
            height (int): height of rectangle. Must be a positive integer
            width (int): Width of rectangle. Must be a positive integer
        """
        self.set_offset(x_offset, y_offset)
        self.set_dimensions(height, width)

    def set_offset(self, x_offset: int, y_offset: int) -> None:
        """Sets the offset with respect to the origin (0, 0) of the parent Design

        Args:
            x_offset (int): x offset with respect to origin (0,0) of its parent Design
            y_offset (int): x offset with respect to origin (0,0) of its parent Design

        Raises:
            TypeError: Inputs must be of integer type.
        """
        if not isinstance(x_offset, int) or not isinstance(y_offset, int):
            error_message = 'x and y offsets from the parent design must be integers'
            print(error_message)
            raise TypeError(error_message)

        self._x_offset = x_offset
        self._y_offset = y_offset

    def set_dimensions(self, height: int, width: int) -> None:
        """Sets the height and width of the rectangle.

        Args:
            height (int): height of rectangle. Must be a positive integer
            width (int): width of rectangle. Must be a positive integer

        Raises:
            TypeError: Raised if height and width are not integers
            ValueError: Raised if height and width are not positive integers
        """
        error_message = 'Height and width must be positive integers'

        if not isinstance(height, int) or not isinstance(width, int):
            print(error_message)
            raise TypeError(error_message)
        if height < 1 or width < 1:
            print(error_message)
            raise ValueError(error_message)

        self._height = height
        self._width = width

    def get_area(self) -> int:
        """Returns area of a shape

        Returns:
            (int): Area of the shape represented by Shape instance
        """
        return self._height * self._width

    def __str__(self) -> str:
        return f'x_offset:{self._x_offset}, y_offset:{self._y_offset}, w:{self._width}, l:{self._height}'
