import math

class Point:
    def __init__(self, x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise ValueError("Las coordenadas deben ser números.")
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

class Line:
    def __init__(self, x1, y1, x2, y2):
        if not all(isinstance(coord, (int, float)) for coord in [x1, y1, x2, y2]):
            raise ValueError("Las coordenadas deben ser números.")
        self.__start = Point(x1, y1)
        self.__end = Point(x2, y2)
        self.length = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

class Shape:
    def __init__(self, *args):
        if len(args) != 31:
            raise ValueError("Se deben proporcionar exactamente 31 argumentos.")
        self.is_regular = args[0]
        self.vertice1 = Point(args[1], args[2])
        self.vertice2 = Point(args[3], args[4])
        self.vertice3 = Point(args[5], args[6])
        self.vertice4 = Point(args[7], args[8])
        self.edge1 = Line(args[9], args[10], args[11], args[12])
        self.edge2 = Line(args[13], args[14], args[15], args[16])
        self.edge3 = Line(args[17], args[18], args[19], args[20])
        self.edge4 = Line(args[21], args[22], args[23], args[24])
        self.angle1 = args[25]
        self.angle2 = args[26]
        self.angle3 = args[27]
        self.angle4 = args[28]
        self.width = args[29]
        self.height = args[30]

    def compute_area(self):
        pass

    def compute_perimeter(self):
        pass

    def compute_inner_angles(self):
        pass

    def compute_vertices(self):
        pass

class Rectangle(Shape):
    def __init__(self, *args):
        super().__init__(*args)

    def compute_area(self):
        return self.width * self.height

    def compute_perimeter(self):
        return 2 * (self.width + self.height)

    def compute_inner_angles(self):
        return [90, 90, 90, 90]
   
    def compute_vertices(self):
        return [self.vertice1.get_x(), self.vertice1.get_y()], [self.vertice2.get_x(), self.vertice2.get_y()], [self.vertice3.get_x(), self.vertice3.get_y()], [self.vertice4.get_x(), self.vertice4.get_y()]

    @staticmethod
    def initialization_rectangle():
        try:
            x = float(input("Enter the x coordinate for the rectangle's bottom-left corner: "))
            y = float(input("Enter the y coordinate for the rectangle's bottom-left corner: "))
            width = float(input("Enter the rectangle's width: "))
            height = float(input("Enter the rectangle's height: "))

            rectangle = Rectangle(True, x, y, x + width, y, x + width, y + height, x, y + height,  # vertices
                                  x, y, x + width, y, x + width, y, x + width, y + height, x + width, y + height, x, y + height, x, y + height, x, y,  # edges
                                  90, 90, 90, 90,  # angles
                                  width, height)  # width, height

            print("Area:", rectangle.compute_area())
            print("Perimeter:", rectangle.compute_perimeter())
            print("Inner Angles:", rectangle.compute_inner_angles())
            print("Vertices:", rectangle.compute_vertices())
        except ValueError as e:
            print(f"Error: {e}")

class Square(Rectangle):
    def __init__(self, *args):
        super().__init__(*args)

    @staticmethod
    def initialization_square():
        try:
            x = float(input("Enter the x coordinate for the square's bottom-left corner: "))
            y = float(input("Enter the y coordinate for the square's bottom-left corner: "))
            width = float(input("Enter the square's width: "))
            height = width
            square = Square(True, x, y, x + width, y, x + width, y + height, x, y + height,  # vertices
                            x, y, x + width, y, x + width, y, x + width, y + height, x + width, y + height, x, y + height, x, y + height, x, y,  # edges
                            90, 90, 90, 90,  # angles
                            width, height)  # width, height
            print("Area:", square.compute_area())
            print("Perimeter:", square.compute_perimeter())
            print("Inner Angles:", square.compute_inner_angles())
            print("Vertices:", square.compute_vertices())
        except ValueError as e:
            print(f"Error: {e}")

class Triangle(Shape):
    def __init__(self, *args):
        super().__init__(*args)

    def compute_perimeter(self):
        return self.edge1.length + self.edge2.length + self.edge3.length

    def compute_area(self):
        s = self.compute_perimeter() / 2
        return math.sqrt(s * (s - self.edge1.length) * (s - self.edge2.length) * (s - self.edge3.length))

    def compute_inner_angles(self):
        a = self.edge1.length
        b = self.edge2.length
        c = self.edge3.length
        self.angle1 = math.acos((a**2 - b**2 - c**2) / (-2 * b * c))
        self.angle2 = math.acos((b**2 - a**2 - c**2) / (-2 * a * c))
        self.angle3 = math.acos((c**2 - a**2 - b**2) / (-2 * a * b))
        return math.degrees(self.angle1), math.degrees(self.angle2), math.degrees(self.angle3)

    def compute_vertices(self):
        return [(self.vertice1.get_x(), self.vertice1.get_y()),
                (self.vertice2.get_x(), self.vertice2.get_y()),
                (self.vertice3.get_x(), self.vertice3.get_y())]

class Isosceles(Triangle):
    def __init__(self, *args):
        super().__init__(*args)

    @staticmethod
    def initialization_isosceles_triangle():
        try:
            x = float(input("Enter the x coordinate for the isosceles triangle's bottom-left corner: "))
            y = float(input("Enter the y coordinate for the isosceles triangle's bottom-left corner: "))
            base_length = float(input("Enter the isosceles triangle's base length: "))
            equal_side_length = float(input("Enter the isosceles triangle's equal side length: "))
            height = math.sqrt(equal_side_length**2 - (base_length / 2)**2)
            isosceles_triangle = Isosceles(False, x, y, x + base_length, y, (x + base_length) - (base_length / 2), y + height, 0, 0,
                                           x, y, x + base_length, y, x + base_length, y, (x + base_length) - (base_length / 2), y + height,
                                           (x + base_length) - (base_length / 2), y + height, x, y, 0, 0, 0, 0,
                                           0, 0, 0, 0,
                                           base_length, height)
            print("Area:", isosceles_triangle.compute_area())
            print("Perimeter:", isosceles_triangle.compute_perimeter())
            print("Inner Angles:", isosceles_triangle.compute_inner_angles())
            print("Vertices:", isosceles_triangle.compute_vertices())
        except ValueError as e:
            print(f"Error: {e}")

class Equilateral(Triangle):
    def __init__(self, *args):
        super().__init__(*args)

    @staticmethod
    def initialization_equilateral_triangle():
        try:
            x = float(input("Enter the x coordinate for the equilateral triangle's bottom-left corner: "))
            y = float(input("Enter the y coordinate for the equilateral triangle's bottom-left corner: "))
            side_length = float(input("Enter the equilateral triangle's side length: "))
            height = (side_length**2 - (side_length / 2)**2)**(1/2)
            equilateral_triangle = Equilateral(True, x, y, x + side_length, y, (x + side_length) - (side_length / 2), y + height, 0, 0,
                                               x, y, x + side_length, y, x + side_length, y, (x + side_length) - (side_length / 2), y + height,
                                               (x + side_length) - (side_length / 2), y + height, x, y, 0, 0, 0, 0,
                                               60, 60, 60, 0,
                                               side_length, height)
            print("Perimeter:", equilateral_triangle.compute_perimeter())
            print("Area:", equilateral_triangle.compute_area())
            print("Inner Angles:", equilateral_triangle.compute_inner_angles())
            print("Vertices:", equilateral_triangle.compute_vertices())
        except ValueError as e:
            print(f"Error: {e}")

class Scalene(Triangle):
    def __init__(self, *args):
        super().__init__(*args)

    @staticmethod
    def initialization_scalene_triangle():
        try:
            x1 = float(input("Enter the x coordinate for the scalene triangle's first vertice: "))
            y1 = float(input("Enter the y coordinate for the scalene triangle's first vertice: "))
            x2 = float(input("Enter the x coordinate for the scalene triangle's second vertice: "))
            y2 = float(input("Enter the y coordinate for the scalene triangle's second vertice: "))
            x3 = float(input("Enter the x coordinate for the scalene triangle's third vertice: "))
            y3 = float(input("Enter the y coordinate for the scalene triangle's third vertice: "))
            edge1_length = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
            edge2_length = math.sqrt((x3 - x2)**2 + (y3 - y2)**2)
            edge3_length = math.sqrt((x1 - x3)**2 + (y1 - y3)**2)
            scalene_triangle = Scalene(False, x1, y1, x2, y2, x3, y3, 0, 0,
                                       x1, y1, x2, y2, x2, y2, x3, y3, x3, y3, x1, y1, 0, 0, 0, 0,
                                       0, 0, 0, 0,
                                       edge1_length, edge2_length, edge3_length)
            print("Area:", scalene_triangle.compute_area())
            print("Perimeter:", scalene_triangle.compute_perimeter())
            print("Inner Angles:", scalene_triangle.compute_inner_angles())
            print("Vertices:", scalene_triangle.compute_vertices())
        except ValueError as e:
            print(f"Error: {e}")

class TriRectangle(Triangle):
    def __init__(self, *args):
        super().__init__(*args)

    @staticmethod
    def initialization_tri_rectangle():
        try:
            x = float(input("Enter the x coordinate for the triangle rectangle's bottom-left corner: "))
            y = float(input("Enter the y coordinate for the triangle rectangle's bottom-left corner: "))
            width = float(input("Enter the triangle rectangle's width: "))
            height = float(input("Enter the triangle rectangle's height: "))
            tri_rectangle = TriRectangle(False, x, y, x + width, y, x, y + height, 0, 0,
                                         x, y, x + width, y, x + width, y, x, y + height, x, y + height, x, y, 0, 0, 0, 0,
                                         0, 0, 0, 0,
                                         width, height)
            print("Area:", tri_rectangle.compute_area())
            print("Perimeter:", tri_rectangle.compute_perimeter())
            print("Inner Angles:", tri_rectangle.compute_inner_angles())
            print("Vertices:", tri_rectangle.compute_vertices())
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    try:
        method = int(input("Enter the shape you want to create (1 for equilateral, 2 for isosceles, 3 for triangle rectangle, 4 for scalene, 5 for rectangle, 6 for square): "))
        if method == 1:
            Equilateral.initialization_equilateral_triangle()
        elif method == 2:
            Isosceles.initialization_isosceles_triangle()
        elif method == 3:
            TriRectangle.initialization_tri_rectangle()
        elif method == 4:
            Scalene.initialization_scalene_triangle()
        elif method == 5:
            Rectangle.initialization_rectangle()
        elif method == 6:
            Square.initialization_square()
        else:
            print("Invalid option.")
    except ValueError as e:
        print(f"Error: {e}")
