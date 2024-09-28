my_string = input()
print(f'{len(my_string)}')
print(f'{my_string.upper()}')
print(f'{my_string.lower()}')
print(my_string.replace(' ',''))
print(f'{my_string[0]}')
print(f'{my_string[-1]}')

class Example:
    def __init__(self, my_string):
        self.my_string = my_string
        print(f'{len(self.my_string)}')
        print(f'{self.my_string.upper()}')
        print(f'{self.my_string.lower()}')
        print(self.my_string.replace(' ',''))
        print(f'{self.my_string[0]}')
        print(f'{self.my_string[-1]}')    
Example(input())

