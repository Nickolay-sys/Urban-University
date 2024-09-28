name = "Nikolay"
print(name[0])      # первый символ строки   
print(name[-1])     # последний символ строки
print(name[3:])     # второая половина строки (4 символа)
print(name[::-1])       # строка наоборот
print(name[1::2])       # каждый второй символ строки
        
class Example:
    def __init__(self, name):
        self.name = name 
        print(self.name[0])      # первый символ строки
        print(self.name[-1])     # последний символ строки
        print(self.name[8:])     # второая порловина строки (7 символов)
        print(self.name[::-1])       # строка наоборот
        print(self.name[1::2])       # каждый второй символ строки
Example('UrbanUniversity')
