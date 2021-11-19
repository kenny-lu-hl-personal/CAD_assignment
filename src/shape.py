
class Shape:
    """
    A Shape instance represents a rectangle lying within a parent(enclosing) design.

    Attributes:
        _x_offset (int): x offset with respect to the origin (0,0) of the enclosing design
        _y_offset (int): y offset with respect to the origin (0,0) of the enclosing design
        _width (int): width of rectangle
        _height (int): height of rectangle

    Methods:
        def set_offset(self, x_offset: int, y_offset: int) -> None:
            Sets the offset with respect to origin of the parent Design.

        def set_dimensions(self, width: int, height: int) -> None:
            Sets the width  of the rectangle.

        def get_area(self) -> int:
            Returns area of the rectangle.

        def get_offset(self) -> int:
            Returns offset with respect to parent Design.
    """

    def __init__(self, x_offset: int, y_offset: int, width: int, height: int):
        """Initializes offset and dimensions.

        Args:
            x_offset (int): x offset with respect to the origin (0,0) of the enclosing design
            y_offset (int): y offset with respect to the origin (0,0) of the enclosing design
            width (int): Width of rectangle. Must be a positive integer
            height (int): height of rectangle. Must be a positive integer

        Raises:
            TypeError: Inputs must be of integer type, else type error is raised.
            ValueError: Width and height must be positive integers, else ValueError is raised.
        """
        self.set_offsets(x_offset, y_offset)
        self.set_dimensions(width, height)

    def set_offsets(self, x_offset: int, y_offset: int) -> None:
        """Sets the offset with respect to the origin (0, 0) of the enclosing(parent) design

        Args:
            x_offset (int): x offset with respect to the origin (0,0) of the enclosing design
            y_offset (int): y offset with respect to the origin (0,0) of the enclosing design

        Raises:
            TypeError: Inputs must be of integer type.
        """
        if not isinstance(x_offset, int) or not isinstance(y_offset, int):
            error_message = 'x and y offsets from the parent design must be integers'
            print(error_message)
            raise TypeError(error_message)

        self._x_offset = x_offset
        self._y_offset = y_offset

    def shift_offsets(self, x_offset_delta: int, y_offset_delta: int) -> None:
        """Shifts the shape's current x and y offsets by the specified distances.

        Args:
            x_offset_delta (int): added to current x offset
            y_offset_delta (int): added to current y offset

        Raises:
            TypeError: Inputs must be of integer type.
        """
        if not isinstance(x_offset_delta, int) or not isinstance(y_offset_delta, int):
            error_message = 'x and y offset deltas must be integers'
            print(error_message)
            raise TypeError(error_message)

        self._x_offset += x_offset_delta
        self._y_offset += y_offset_delta

    def set_dimensions(self, width: int, height: int) -> None:
        """Sets the height and width of the rectangle.

        Args:
            width (int): width of rectangle. Must be a positive integer
            height (int): height of rectangle. Must be a positive integer

        Raises:
            TypeError: Raised if width and height are not integers
            ValueError: Raised if width and height are not positive integers
        """
        error_message = 'width and height must be positive integers'

        if not isinstance(width, int) or not isinstance(height, int):
            print(error_message)
            raise TypeError(error_message)
        if width < 1 or height < 1:
            print(error_message)
            raise ValueError(error_message)

        self._width = width
        self._height = height

    def get_offsets(self) -> int:
        """Returns offset with respect to parent Design

        Returns:
           (Tuple[int]): x and y offsets of the shape (x_offset, y_offset)
        """
        return (self._x_offset, self._y_offset)

    def get_dimensions(self) -> int:
        """Returns dimensions of a shape.

        Returns:
            (Tuple[int]): Width and height of the shape. (width, height)
        """
        return (self._width, self._height)

    def get_area(self) -> int:
        """Returns area of a shape

        Returns:
            (int): Area of the shape represented by Shape instance
        """
        return self._width * self._height

    def __eq__(self, other) -> bool:
        """Checks if two shapes are equal.

        Args:
            other (Shape): shape to compare against

        Returns:
            (bool): True if the two shapes have same dimensions and offset from parent.
        """
        return self._x_offset == other._x_offset and \
            self._y_offset == other._y_offset and \
            self._width == other._width and \
            self._height == other._height

    def __str__(self) -> str:
        """Returns string value """
        return f'x_offset:{self._x_offset}, y_offset:{self._y_offset}, w:{self._width}, h:{self._height}'
