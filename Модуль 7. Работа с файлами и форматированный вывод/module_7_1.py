# class Product:
#     def __init__(self, name: str, weight: float, category: str):
#         self.name = name
#         self.weight = weight
#         self.category = category
#     def __str__(self):
#         return f'{self.name}, {self.weight}, {self.category}'
    
# class Shop(Product):
#     def __init__(self, name: str, weight: float, category: str, __file_name = 'products.txt'):
#         super().__init__(name, weight, category)
#         self.__file_name = __file_name
#     def get_products(self):
#         file = open(self.__file_name, 'r')    
#         lst = file.read()
#         file.close()
#         print(f'{lst}')
#     def add(self, *products):
#         for i in products:
#             prod = str(i)
#             file = open(self.__file_name, 'r')    
#             lst = file.read()
#             file.close()
#             if prod in lst:
#                 print(f'Продукт {prod} уже есть в магазине')
#             else:
#                 file = open(self.__file_name,'a')
#                 lst = file.write(f'\n{prod}')
#                 file.close()
class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category
        
    def __str__(self) -> str:
        return f'{self.name}, {self.weight}, {self.category}'
    
class Shop(Product):
    def __init__(self, name, weight, category):
        super().__init__(name, weight, category)
        self.__file_name = 'products.txt'    
    
    def get_products(self):
        file = open(self.__file_name, 'r')
        print(file.read())
        file.close()
        
    def add(self, *products):
        file = open(self.__file_name, 'r')
        list_1 = file.read()
        file.close()
        for i in products:
            prod = str(i)
            if prod in list_1:
                print(f'Продукт {self.name} уже есть в магазине')
            else:
                file = open(self.__file_name, 'a')
                file.write(f'\n{prod}')
                file.close()

        
                
s1 = Shop('', '', '')
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())