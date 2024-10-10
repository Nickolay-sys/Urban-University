import io
def custom_write(file_name, strings):
    file= open(file_name, 'wt', encoding='utf-8')
    file.writelines(strings)
    file.close
    numbers = (file.seek(0), file.seek(16), file.seek(66), file.seek(98))
    strings_positions = dict(zip(enumerate(numbers,+1), strings))
    return strings_positions 
  
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ] 

result = custom_write('test.txt',info)
for elem in result.items():
  print(elem)