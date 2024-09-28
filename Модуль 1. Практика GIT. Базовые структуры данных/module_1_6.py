my_dict = {'Nikolay': 1998,
           'Alexander': 1996,
           'Ivan': 2000,
           'Artem': 2001}
print('Dict:', my_dict)
print('Existing Value:', my_dict.get('Nikolay'))
print('Non existing value:', my_dict.get(2003))
my_dict.update({'Ilya': 1995,
                'Sveta': 1997})
a = my_dict.pop('Ivan')
print('Deleted value:',a)
print('Modified dictionary:', my_dict)

my_set = {898,
          123,
          1002,
          898,
          1002,
          'Owl',
          'Cat'}
print('Set:', my_set)
my_set.update(['Dog'],
              [(123,456,789)])
my_set.discard('Cat')
print('Modified set:', my_set)

class Example:
    def __init__(self,my_dict):
        self.my_dict = my_dict
    def get_dict(self):
        print(f'Dict: {self.my_dict}')
        print(f'Existing value: {self.my_dict}')
        print(f'Non existing value: None')
    def modify(self,new_values):
        self.my_dict.update(new_values)
        self.get_dict()
    def pop(self,a):
        self.a = a
        a = self.my_dict.pop(a)
        print(f'Deleted Value: {a}')
        print(f'Modified dictionary: {self.my_dict}')
        
example = Example({'Nikolay': 1998,'Alexander': 1996,'Ivan': 2000,'Artem': 2001})
example.get_dict()
example.modify({'Ilya': 1995,'Sveta': 1997})
example.pop('Ivan')

class Example_Set:
    def __init__(self,my_set):
        self.my_set = my_set
    def get_set(self):
        print(f'Set: {self.my_set}')
    def modify(self,*new_values):
        for values in new_values:
            if isinstance(values, (list,set)):
                self.my_set.update(values)
        self.get_set()
    def discard(self, delition):
        self.my_set.discard(delition)
        self.get_set()
example_set = Example_Set({898,123,1002,898,1002,'Owl','Cat'})
example_set.get_set()
example_set.modify(['Dog'],[(123,456,789)])
example_set.discard('Cat')

