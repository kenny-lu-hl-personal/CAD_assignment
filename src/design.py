from src.shape import Shape
from copy import deepcopy
from typing import List


class Design:
    def __init__(self):
        self._shapes = []
        self._instances = []

    def add_shape(self, shape: Shape) -> Shape:
        """Creates a copy (new shape instance) based on the given shape, and adds the copy to the design.
           Returns the newly created copy.
           Adding a copy ensures that every shape inside a design is an unique instance.

        Args:
            shape (Shape): Shape to add to the design.

        Returns:
            (Shape): The newly created copy added to Design.
        """
        if not isinstance(shape, Shape):
            error_message = f'Input argument {shape} is not an instance of Shape'
            print(error_message)
            raise TypeError(error_message)

        shape_copy = deepcopy(shape)
        self._shapes.append(shape_copy)
        return shape_copy

    def get_shapes(self) -> List[Shape]:
        """Returns a list of shapes in the design.

           If the design contains/embeds other designs,
           the shapes of those embedded designs are NOT included in the list.

        Returns:
            (List[Shape])
        """
        return self._shapes[:]

    def get_shapes_descending_area(self) -> List[Shape]:
        """Returns a list of shapes in the design.
           The shapes are sorted by area in descending order.

           If the design contains/embeds other designs,
           the shapes of those embedded designs are NOT included in the list.

        Returns:
            (List[Shape])
        """
        self._shapes.sort(key=lambda x: -x.get_area())
        return self.get_shapes()
