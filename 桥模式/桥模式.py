from abc import ABCMeta, abstractmethod


class Shape(metaclass=ABCMeta):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def draw(self):
        pass


class Color(metaclass=ABCMeta):

    @abstractmethod
    def paint(self, shape):
        pass


class Rectangle(Shape):

    name = "长方形"

    def draw(self):
        self.color.paint(self)


class Circle(Shape):

    name = "圆形"

    def draw(self):
        self.color.paint(self)


class Line(Shape):

    name = "直线"

    def draw(self):
        self.color.paint(self)


class Red(Color):
    def paint(self, shape):
        print("红色的%s" % shape.name)


class Green(Color):
    def paint(self, shape):
        print("绿色的%s" % shape.name)


class Black(Color):
    def paint(self, shape):
        print("黑色的%s" % shape.name)


if __name__ == '__main__':
    shape = Rectangle(Red())
    shape.draw()

    shape2 = Circle(Green())
    shape2.draw()

    shape3 = Line(Black())
    shape3.draw()

