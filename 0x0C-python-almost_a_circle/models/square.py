#!/usr/bin/python3
"""square is a class that inherits from Rectangle
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Square is a class that print a square"""
    def __init__(self, size, x=0, y=0, id=None):
        """__init__ is a class that print a square"""
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """__init__ is a class that print a square"""
        line1 = str(" - " + str(self.size))
        line2 = str(str(self.x) + "/" + str(self.y))
        return str("[Square] " + "(" + str(self.id) + ") " + line2 + line1)

    @property
    def size(self):
        """size is a getter/setter methods"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update is a getter/setter methods"""
        if (args and args is not None):
            i = 0
            for arg in args:
                if (i == 0):
                    self.id = arg
                elif(i == 1):
                    self.__size = arg
                elif(i == 2):
                    self.__x = arg
                elif(i == 3):
                    self.__y = arg
                i += 1
        else:
            for key in kwargs:
                if(key == "id"):
                    self.id = kwargs[key]
                if(key == "size"):
                    self.__size = kwargs[key]
                if(key == "x"):
                    self.__x = kwargs[key]
                if(key == "y"):
                    self.__y = kwargs[key]

    def to_dictionary(self):
        """to_dictionary is a getter/setter methods"""
        d = {'id': self.id, 'size': self.__size, 'x': self.x, 'y': self.y}
        return d
