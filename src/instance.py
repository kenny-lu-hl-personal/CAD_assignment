import src.design as design


class Instance:
    """
    An instance represents a design that is embedded in another design.

    Attributes:
        _x_offset (int): x offset with respect to origin (0,0) of the enclosing design
        _y_offset (int): y offset with respect to origin (0,0) of the enclosing design
        _design_ref (Design): Reference to the embedded design

    Methods:
        def set_offset(self, x_offset: int, y_offset: int) -> None:
            Sets the offset with respect to origin of the enclosing design.
        def set_design_ref(self, design_ref) -> None:
            Sets the the reference for the embedded design
        def get_offset(self) -> int:
            Returns offset with respect to enclosing design
        def get_design_ref(self) -> Design:
            Gets the reference design
    """

    def __init__(self, x_offset, y_offset, design_ref):
        """Initializes offset and reference design

        Args:
            x_offset (int): x offset with respect to origin (0,0) of the enclosing design
            y_offset (int): y offset with respect to origin (0,0) of the enclosing design
            design_ref (Design): design that the instance will refer to
        Raises:
            TypeError: Raised if input parameters are not of expected type.
        """
        self.set_offset(x_offset, y_offset)
        self.set_design_ref(design_ref)

    def set_offset(self, x_offset: int, y_offset: int) -> None:
        """Sets the offset with respect to the origin (0, 0) of the enclosing design

        Args:
            x_offset (int): x offset with respect to origin (0,0) of the enclosing design
            y_offset (int): y offset with respect to origin (0,0) of the enclosing design

        Raises:
            TypeError: Raised if input parameters are not integers
        """
        if not isinstance(x_offset, int) or not isinstance(y_offset, int):
            error_message = 'Input paremeters are no of type int'
            print(error_message)
            raise TypeError(error_message)

        self._x_offset = x_offset
        self._y_offset = y_offset

    def set_design_ref(self, design_ref) -> None:
        """Sets the the reference for the embedded design

        Args:
            design_ref (Design): design that the embedded design will refer to

        Raises:
            TypeError: Raised if input parameter is not of type Design
        """
        if not isinstance(design_ref, design.Design):
            error_message = f'Input parameter {design_ref} is not of type Design'
            print(error_message)
            raise TypeError(error_message)

        self._design_ref = design_ref

    def get_offsets(self) -> int:
        """Returns offset with respect to enclosing design

        Returns:
           (Tuple[int]): Tuple of length two. 
                         First element is the x offset and second element is the y offset.
        """
        return (self._x_offset, self._y_offset)

    def get_design_ref(self):
        """Gets the reference design

        Returns:
           (Design): The referenced design
        """
        return self._design_ref
