import math
class Figure:
    sides_count = 0
    # def __init__(self, color: list, *sides: int, filled: bool = True):
    #     if len(sides) != self.sides_count:
    #         self.__sides = [1*self.sides_count]
    #     else:
    #         self.__sides = [i for i in sides]
        # self.__color = list(color)
        # self.filled = filled
    def __init__(self, color: list, *sides: int):
        self.__color = [*color] if self.__is_valid_color(*color) else [0,0,0]
        self.__sides = [*sides] if len(sides) == self.sides_count else [1] * self.sides_count
        self.filled = False
        
    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        list_ = [r, g, b]
        list_.sort()
        if list_[0] < 0 or list_[-1] > 255:
            return False
        else:
            return True
    
    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)
            
    def __is_valid_sides(self, sides):
        lst = []
        for i in sides:
            if i > 0 < 255:
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
    def __radius(self):
        return self.__len__ * (2 / 3.14)
    def get_square(self):
        return (self.__len__**2) / (4 * 3.14)
    
class Triangle(Figure):
    sides_count = 3
    def get_square(self):
        sp = self.__len__ / 2 
        s = math.sqrt((sp(sp - self.__sides[0]) * (sp - self.__sides[1]) * (sp - self.__sides[0])))
        return s
        
class Cube(Figure):
    sides_count = 12
    def __init__(self, color, *sides: int, filled: bool = True):
        super().__init__(color, *sides, filled)
        if len(sides) == 1:
            self.__sides = self.sides_count * [i for i in sides]
        else:
            self.__sides = [1*self.sides_count]
    
    def get_sides(self):
        return [*self.__sides]
            
    def get_volume(self):
        return self.__sides[1]**3
        
circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

print('Проверка на изменение цветов')
# Проверка на изменение цветов:
print(circle1.get_color())
circle1.set_color(255, 255, 255) # Изменится
# cube1.set_color(300, 70, 15) # Не изменится
print(circle1.get_color())
# print(cube1.get_color())

# print('Проверка на изменение сторон:')
# # Проверка на изменение сторон:
# cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
# circle1.set_sides(15) # Изменится
# print(cube1.get_sides())
# print(circle1.get_sides())

# print('Проверка периметра (круга), это и есть длина:')
# # Проверка периметра (круга), это и есть длина:
# print(len(circle1))

# print('Проверка объёма (куба):')
# # Проверка объёма (куба):
# print(cube1.get_volume())    
        
        