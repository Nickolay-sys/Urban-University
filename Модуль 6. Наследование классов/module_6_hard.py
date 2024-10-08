import math
class Figure:
    sides_count = 0
    def __init__(self, color: list, *sides: int):
        self.__color = [*color] if self.__is_valid_color(*color) else [0,0,0]
        self.__sides = [*sides] if len(sides) == self.sides_count else [1] * self.sides_count
        self.filled = False
        
    def get_color(self):
        return list(self.__color)

    def __is_valid_color(self, r, g, b):
        list_ = [r, g, b]
        list_.sort()
        if isinstance(list_[0], int) and list_[0] < 0 or isinstance(list_[-1], int) and list_[-1] > 255:
            return False
        else:
            return True

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            if r >= 0 and g >= 0 and b >= 0:
                self.__color = (r, g, b)
            
    def __is_valid_sides(self, sides):
        lst = []
        for i in sides:
            if isinstance(i, int) and i > 0 < 255:
                lst.append(i)
        if len(lst) > 0 and len(sides) == len(self.__sides):
            return True
        else:
            return False
        
    def get_sides(self):
        return [*self.__sides]
    
    def __len__(self):
        return sum(self.__sides)
    
    def set_sides(self, *sides):
        if self.__is_valid_sides(sides):
            self.__sides = sides
        
class Circle(Figure):
    sides_count = 1
    def __init__(self, color: str, *sides: int):
        super().__init__(color, *sides)
        self.__radius = self.get_sides()[0]/(2*math.pi)
    def get_square(self):
        return self.__radius ** 2 * math.pi
    
class Triangle(Figure):
    sides_count = 3
    def __init__(self, color: str, *sides:int):
        super().__init__(color, *sides)
        self.semiperim = sum(sides) / 2
    # def get_square(self):
    #     sp = len(self) / 2 
    #     s = math.sqrt(sp*(sp - self.__sides[0]) * (sp - self.__sides[1]) * (sp - self.__sides[2]))
    #     return s
    def get_square(self):
        square = math.sqrt(self.semiperim * 
                           (self.semiperim - self.get_sides()[0]) * 
                           (self.semiperim - self.get_sides()[1]) * 
                           (self.semiperim - self.get_sides()[2]))
        return square
        
class Cube(Figure):
    sides_count = 12
    def __init__(self, color, *sides: int, filled: bool = True):
        super().__init__(color, *sides, filled)
        if len(sides) == 1:
            self.__sides = self.sides_count * [i for i in sides]
        else:
            self.__sides = [1*self.sides_count]
        self.set_sides(*list(sides)*12)
      
    def get_volume(self):
        return self.__sides[1]**3
        
circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

print('Проверка на изменение цветов')
# Проверка на изменение цветов:
print(circle1.get_color())
circle1.set_color(55, 66, 77) # Изменится
cube1.set_color(300, 70, 15) # Не изменится
print(circle1.get_color())
print(cube1.get_color())

print('Проверка на изменение сторон:')
# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
circle1.set_sides(15) # Изменится
print(cube1.get_sides())
print(circle1.get_sides())

print('Проверка периметра (круга), это и есть длина:')
# Проверка периметра (круга), это и есть длина:
print(len(circle1))

print('Проверка объёма (куба):')
# Проверка объёма (куба):
print(cube1.get_volume())    
triangle1 = Triangle((10,10,10), 3)       
print(triangle1.get_square())