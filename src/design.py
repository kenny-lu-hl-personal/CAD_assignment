from copy import copy, deepcopy
from typing import List
import src.shape
import src.instance


class Design:
    """A design represents a collection of shapes in a 2D coordinate system.
       A shape is a rectangle object and includes information about where it lies w.r.t. the parent design's origin (0, 0)
       In addition to shapes, a design can have other designs embedded within it. 
       Embedded designs are modeled through Instance objects. 
       An instance has a reference to another design object and where it is situated with respect to the parent design.

    Attributes:
        self._shapes (List[Shape]): Shapes at the top-level of the design.
        self._instances (List[Instance]): Instances embedded in the design

    Methods:
        def __init__(self):
            Initializes the design instance. A design starts out empty, without any shapes or instances

        def add_shape(self, x_offset: int, y_offset: int, height: int, width: int) -> Shape:
            Creates a shape with the given parameters and adds it to the design.
            Returns the newly created and added shape.

        def add_shape_copy(self, shape: Shape) -> Shape:
            Creates a shallow copy of an existing shape and adds the copy to the design.
            Returns the newly created copy.
            Adding a copy ensures that every shape inside a design refers to an unique shape instance.

        def add_instance(self, x_offset: int, y_offset: int, design_ref) -> Instance:
            Creates an instance with the given parameters and adds it to the design.
            Returns the newly created and added instance.

        def add_instance_copy(self, inst: Instance) -> Instance:
            Creates a shallow copy of an existing instance and adds the copy to the design.
            Returns the newly created copy.

        def get_instances(self) -> List[Instance]:
            Returns a list of instances belonging to the design.
            Does not return instances belonging to other designs embedded within the design.

        def get_shapes(self) -> List[Shape]:
            Returns a list of shapes in the design.

        def get_shapes_inorder_of_descending_area(self) -> List[Shape]:
            Returns a list of shapes in the design sorted by area in descending order.

        def get_shapes_within_one_level(self) -> List[Shape]:
            Returns a list of shapes representing all shapes within 1 level of the design's hierarchy.
            The shapes in the returned list are deep copies of the shapes in the design.
            The copied shapes have their x and y offets updated such that they are now relative to the top-level design.
    """

    def __init__(self):
        """Initializes the design instance. A design starts out empty, without any shapes or instances."""
        self._shapes = []
        self._instances = []

    def add_shape(self, x_offset: int, y_offset: int, height: int, width: int) -> src.shape.Shape:
        """Creates a shape with the given parameters and adds it to the design.
           Returns the newly created and added shape.

        Args:
            x_offset (int): x offset with respect to the origin (0,0) of the parent design
            y_offset (int): y offset with respect to the origin (0,0) of the parent design
            width (int): Width of shape. Must be a positive integer
            height (int): Height of shape. Must be a positive integer

        Returns:
            (Shape): The newly created shape that was added to the design.
        """
        new_shape = src.shape.Shape(x_offset, y_offset, height, width)
        self._shapes.append(new_shape)
        return new_shape

    def add_shape_copy(self, shape: src.shape.Shape) -> src.shape.Shape:
        """Creates a deep copy of an existing shape and adds the copy to the design.
           Returns the newly created copy.
           Adding a copy ensures that every shape inside a design refers to an unique shape instance.

        Args:
            shape (Shape): Shape to be copied. Its copy will be added to the design.

        Returns:
            (Shape): The newly created copy added to design.
        """
        if not isinstance(shape, src.shape.Shape):
            error_message = f'Input argument {shape} is not of type Shape'
            print(error_message)
            raise TypeError(error_message)

        shape_copy = deepcopy(shape)
        self._shapes.append(shape_copy)
        return shape_copy

    def add_instance(self, x_offset: int, y_offset: int, design_ref) -> src.instance.Instance:
        """Creates an instance with the given parameters and adds it to the design.
           Returns the newly created and added instance.

        Args:
            x_offset (int): x offset with respect to the origin (0,0) of the parent design
            y_offset (int): y offset with respect to the origin (0,0) of the parent design
            design_ref (Design): design that the instance will refer to

        Returns:
            (Instance): The newly created instance that was added to the design.
        """
        new_instance = src.instance.Instance(x_offset, y_offset, design_ref)
        self._instances.append(new_instance)
        return new_instance

    def add_instance_copy(self, inst: src.instance.Instance) -> src.instance.Instance:
        """Creates a shallow copy of an existing instance and adds the copy to the design.
           Returns the newly created copy.

           The copy has the same x and y offets as the original instance.  
           It also contains a reference to the same design object referenced by the original instance.
           Several instance objects can use the same design object as a design reference.   
           When a design object is updated, the change is reflected in all instances that use it as a reference design.

        Args:
            inst (Instance): Instance to be copied. Its copy will be added to the design.

        Returns:
            (Instance): The newly created copy added to design.
        """
        if not isinstance(inst, src.instance.Instance):
            error_message = f'Input argument {inst} is not of type Instance'
            print(error_message)
            raise TypeError(error_message)

        instance_copy = copy(inst)
        self._instances.append(instance_copy)
        return instance_copy

    def get_instances(self) -> List[src.instance.Instance]:
        """Returns a list of instances belonging to the design.
           Does not return instances belonging to other designs embedded within the design.

        Returns:
            (List[Instance]): List of instances in the design.
        """
        return self._instances[:]

    def get_shapes(self) -> List[src.shape.Shape]:
        """Returns a list of shapes in the design.

           If the design contains/embeds other designs,
           the shapes of those embedded designs are NOT included in the list.

        Returns:
            (List[Shape]): List of shapes in the design.
        """
        return self._shapes[:]

    def get_shapes_inorder_of_descending_area(self) -> List[src.shape.Shape]:
        """Returns a list of shapes in the design.
           The shapes are sorted by area in descending order.

           If the design contains/embeds other designs,
           the shapes of those embedded designs are NOT included in the list.

        Returns:
            (List[Shape]): List of shapes in the design sorted in order of descending area.
        """
        sorted_shapes = self._shapes[:]
        sorted_shapes.sort(key=lambda x: -x.get_area())
        return sorted_shapes

    def get_shapes_within_one_level(self) -> List[src.shape.Shape]:
        """Returns a list of shapes representing all shapes within 1 level of the design's hierarchy.
           Only includes shapes at the design's own level, and shapes of its immediate instances/designs (one level down).

           The shapes in the returned list are deep copies of the shapes in the design.
           The copied shapes have their x and y offets updated such that they are now relative to the top-level design.
           Copies are used so that shapes in the design do not have their x and y offsets modified by this function.

        Returns:
            List[Shape]: List containing copies of shapes within 1 level, with their locations relative to top-level design.
        """
        # start with copies of shapes at top-level
        shapes_within_one_level = deepcopy(self._shapes)

        # get shapes one-level down
        for inst in self._instances:
            inst_x_offset, inst_y_offset = inst.get_offsets()
            design_ref = inst.get_design_ref()
            for shape in design_ref.get_shapes():
                shape_copy = deepcopy(shape)
                shape_copy.shift_offsets(inst_x_offset, inst_y_offset)
                shapes_within_one_level.append(shape_copy)

        return shapes_within_one_level
