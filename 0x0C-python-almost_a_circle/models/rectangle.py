#!/usr/bin/python3
"""
Class Rectangle that inherits from
Base
"""

from models.base import Base


class Rectangle(Base):
    """
    Inherits from Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor"""
        items = {1: "width", 2: "height", 3: "x", 4: "y"}
        i = 1
        for item in [width, height, x, y]:
            if type(item) is not int:
                raise TypeError("{} must be an integer".format(items[i]))
            i += 1
        i = 1
        for item in [width, height]:
            if item <= 0:
                raise ValueError("{} must be > 0".format(items[i]))
            i += 1
        i = 3
        for item in [x, y]:
            if item < 0:
                raise ValueError("{} must be >= 0".format(items[i]))
            i += 1

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """Getter"""
        return(self.__width)

    @width.setter
    def width(self, width):
        """Setter"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

    @property
    def height(self):
        """Getter"""
        return(self.__height)

    @height.setter
    def height(self, height):
        """Setter"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

    @property
    def x(self):
        """Getter"""
        return(self.__x)

    @x.setter
    def x(self, x):
        """Setter"""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

    @property
    def y(self):
        """Getter"""
        return(self.__y)

    @y.setter
    def y(self, y):
        """Setter"""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

    def area(self):
        """Returns area of rectangle"""
        return(self.__width * self.__height)

    def display(self):
        """Displays the rectangle"""
        for i in range(self.__y):
            print("")
        for i in range(self.__height):
            for k in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print("")

    def __str__(self):
        """Overrides __str__"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.__x,
                                                       self.__y,
                                                       self.__width,
                                                       self.__height)

    def update(self, *args, **kwargs):
        """Updated Rectangle"""
        try:
            self.id = args[0]
        except Exception:
            pass
        try:
            self.__width = args[1]
        except Exception:
            pass
        try:
            self.__height = args[2]
        except Exception:
            pass
        try:
            self.__x = args[3]
        except Exception:
            pass
        try:
            self.__y = args[4]
        except Exception:
            pass

        if not args or len(args) == 0:
            if kwargs and len(kwargs) != 0:
                for key, value in kwargs.items():
                    if key == "id":
                        if value is None:
                            self.__init__(self.__width,
                                          self.__height,
                                          self.__x,
                                          self.__y)
                        else:
                            self.id = value
                    elif key == "width":
                        self.__width = value
                    elif key == "height":
                        self.__height = value
                    elif key == "x":
                        self.__x = value
                    elif key == "y":
                        self.__y = value

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
