from copy import copy, deepcopy
from typing import List
from src.shape import Shape
from src.instance import Instance


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
            error_message = f'Input argument {shape} is not of type Shape'
            print(error_message)
            raise TypeError(error_message)

        shape_copy = deepcopy(shape)
        self._shapes.append(deepcopy(shape))
        return shape_copy

    def add_instance(self, instance: Instance) -> None:
        if not isinstance(instance, Instance):
            error_message = f'Input argument {instance} is not of type Instance'
            print(error_message)
            raise TypeError(error_message)

        instance_copy = copy(instance)
        self._instances.append(instance_copy)
        return instance_copy

    def get_instances(self) -> List[Shape]:
        """Returns a list of instances in the design.

           Only returns instances at the current design level.
           Does not return instances in embedded designs.

        Returns:
            (List[Shape])
        """
        return self._instances[:]

    def get_shapes(self) -> List[Shape]:
        """Returns a list of shapes in the design.

           If the design contains/embeds other designs,
           the shapes of those embedded designs are NOT included in the list.

        Returns:
            (List[Shape])
        """
        return self._shapes[:]

    def get_shapes_inorder_of_descending_area(self) -> List[Shape]:
        """Returns a list of shapes in the design.
           The shapes are sorted by area in descending order.

           If the design contains/embeds other designs,
           the shapes of those embedded designs are NOT included in the list.

        Returns:
            (List[Shape])
        """
        self._shapes.sort(key=lambda x: -x.get_area())
        return self.get_shapes()

    def get_shapes_within_one_level(self) -> List[Shape]:
        # start with list containing copies of shapes in curr level
        shapes = deepcopy(self._shapes)

        for inst in self._instances:
            inst_x_offset, inst_y_offset = inst.get_offsets()
            design_ref = inst.get_design_ref()
            for shape in design_ref.get_shapes():
                shape_copy = deepcopy(shape)
                shape_copy.shift_offsets(inst_x_offset, inst_y_offset)
                shapes.append(shape_copy)

        return shapes
