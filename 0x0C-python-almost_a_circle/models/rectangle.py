#!/usr/bin/python3
"""Defining the subclass Rectangle"""

from models.base import Base


class Rectangle(Base):
    """This is the class Rectangle that in herits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """This function initilizes the class Rectangle.

           Args:
               width (int): Width of the rectangle
               height (int): height of the rectangle
               x (int):
               y (int):
               id (int): the attribute inherited from Base
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        if (type(width) is not int):
            raise TypeError("width must be an integer")
        if (width < 0) or (width == 0):
            raise ValueError("width must be > 0")
        if (type(height) is not int):
            raise TypeError("height must be an integer")
        if (height < 0) or (height == 0):
            raise ValueError("height must be > 0")
        if (type(x) is not int):
            raise TypeError("x must be an integer")
        if (x < 0):
            raise ValueError("x must be >= 0")
        if (type(y) is not int):
            raise TypeError("y must be an integer")
        if (y < 0):
            raise ValueError("y must be >= 0")

    @property
    def width(self):
        """This function is used to the set the value of private
           attribute width the value of value

           Args:
               value (int): the new value

           Returns:
               the new width
        """
        return self.__width

    @width.setter
    def width(self, value):
        if (type(value) is not int):
            raise TypeError("width must be an integer")
        if (value < 0) or (value == 0):
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """This function is used to the set the value of private
           attribute height the value of value

           Args:
               value (int): the new value

           Returns:
               the new height
        """
        return self.__height

    @height.setter
    def height(self, value):
        if (type(value) is not int):
            raise TypeError("height must be an integer")
        if (value < 0) or value == 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """This function is used to the set the value of private
           attribute x the value of value

           Args:
               value (int): the new value

           Returns:
               the new x
        """
        return self.__x

    @x.setter
    def x(self, value):
        if (type(value) is not int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """This function is used to the set the value of private
           attribute y the value of value

           Args:
               value (int): the new value

           Returns:
               the new y
        """
        return self.__y

    @y.setter
    def y(self, value):
        if (type(value) is not int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """This function returns the area of rectangle"""

        return self.__width * self.__height

    def display(self):
        """This function displays a rectangle using # and uses
           x and y to create spaces"""

        if self.__y == 0 and self.__x == 0:
            for i in range(self.__height):
                for j in range(self.__width):
                    print("#", end="")
                print()
        else:
            for l in range(self.__y):
                print()
            for i in range(self.__height):
                for k in range(self.__x):
                    print(" ", end="")
                for j in range(self.__width):
                    print("#", end="")
                print()

    def __str__(self):
        """This function displays [rectangle] (id) x/y - width/height
           if print or str is called"""

        return "[Rectangle] " + "(" + str(self.id) + ") " + str(self.__x)\
               + "/" + str(self.__y) + " - " + str(self.__width)\
               + "/" + str(self.__height)

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
                self.__width = args[1]
            elif len(args) == 3:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
            elif len(args) == 4:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
            elif len(args) == 5:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
                self.__y = args[4]
        elif len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    self.id = v
                elif k == "width":
                    self.__width = v
                elif k == "height":
                    self.__height = v
                elif k == "x":
                    self.__x = v
                elif k == "y":
                    self.__y = v

    def to_dictionary(self):
        """This function returns the dictionary representation of class"""

        return {"id": self.id, "width": self.__width, "height": self.__height,
                "x": self.__x, "y": self.__y}
