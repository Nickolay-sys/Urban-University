
class Human:        # class ~ инструкция которую можно вызывать к разным объектам
    def __init__(self, name):       # __init__ запускает код в class
        self.name = name        # self  указывает на самого себя

den = Human('Denis')        # объекты создаваемые классами уникальны
max_ = Human('Max')
print(den == max_)
print(den is max_)
print(id(den), id(max_))
print(den.name, max_.name)