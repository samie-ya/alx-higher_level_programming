#!/usr/bin/python3
"""Defining the class square"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """This class is square which inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """This function will initialize the class square.

           Args:
               size (int): the size of the square
               x (int):
               y (int):
               id (int): id of the Base
        """
        super().__init__(width=size, height=size, x=x, y=y, id=id)

    def __str__(self):
        """This function displays [square] (id) x/y - width/height
           if print or str is called"""

        return "[Square] " + "(" + str(self.id) + ") " + str(self.x)\
               + "/" + str(self.y) + " - " + str(self.width)

    @property
    def size(self):
        """This function is used to the set the value of private
           attribute size the value of value

           Args:
               value (int): the new value

           Returns:
               the new width
        """
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """This function changes the order of the attributes

           Args:
               *args(var): allows for variable number of arguments
                           to be passes
               **kwargs (var): allows for many number of key value
                           arguments to pass
        """
        if len(args) != 0:
            if len(args) == 1:
                self.id = args[0]
            elif len(args) == 2:
                self.id = args[0]
                self.width = args[1]
            elif len(args) == 3:
                self.id = args[0]
                self.width = args[1]
                self.x = args[2]
            elif len(args) == 4:
                self.id = args[0]
                self.width = args[1]
                self.x = args[2]
                self.y = args[3]
        elif len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    self.id = v
                elif k == "size":
                    self.width = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """This function returns the dictionary representation of class"""

        return {"id": self.id, "size": self.width, "x": self.x, "y": self.y}
