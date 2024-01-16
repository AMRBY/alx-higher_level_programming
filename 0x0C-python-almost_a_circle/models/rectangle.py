#!/usr/bin/python3
"""this is the base class
"""


from models.base import Base


class Rectangle(Base):
    """ base is a class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """ i__init__ is a function for initialization
        args:
            width: int
            height: int
            x: int
            y: int
            id : it's an int"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """width is a getter/setter methods"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height is a getter/setter methods"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x is a getter/setter methods"""
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """height is a getter/setter methods"""
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """area is a getter/setter methods"""
        return self.__width * self.__height

    def display(self):
        """display is a getter/setter methods"""
        [print("") for i in range(0, self.__y)]
        for i in range(0, self.__height):
            [print(" ", end="") for j in range(0, self.__x)]
            [print("#", end="") for k in range(0, self.__width)]
            print("")

    def __str__(self):
        """__str__ is a getter/setter methods"""
        line1 = str(" - " + str(self.__width) + "/" + str(self.__height))
        line2 = str(str(self.__x) + "/" + str(self.__y))
        return str("[Rectangle] " + "(" + str(self.id) + ") " + line2 + line1)

    def update(self, *args, **kwargs):
        """update is a getter/setter methods"""
        if (args and args is not None):
            i = 0
            for arg in args:
                if (i == 0):
                    self.id = arg
                elif(i == 1):
                    self.__width = arg
                elif(i == 2):
                    self.__height = arg
                elif(i == 3):
                    self.__x = arg
                elif(i == 4):
                    self.__y = arg
                i += 1
        else:
            for key in kwargs:
                if(key == "id"):
                    self.id = kwargs[key]
                if(key == "width"):
                    self.__width = kwargs[key]
                if(key == "height"):
                    self.__height = kwargs[key]
                if(key == "x"):
                    self.__x = kwargs[key]
                if(key == "y"):
                    self.__y = kwargs[key]

    def to_dictionary(self):
        """to_dictionary is a getter/setter methods"""
        d = {'x': self.__x, 'y': self.__y, 'id': self.id,
             'height': self.__height, 'width': self.__width}
        return d
