import string
class WordsFinder:
    def __init__(self,file_name):
        self.file_name = file_name
       
    def get_all_words(self):
        all_words = {}
        with open(self.file_name, 'r', encoding='utf-8') as file:
            lines = file.read()
            for p in string.punctuation:
                if p in lines:
                    lines = lines.replace(p,'')  
            for self.words in lines:
                lines = lines.lower()
                key = (self.file_name)
                all_words[key] = lines.split()
                return all_words
            
    def find(self, word):
        find_word = {}
        lines = self.get_all_words()[self.file_name]
        for i in range(len(lines)):
            if word.lower() == lines[i]:
                find_word.update({self.file_name: i+1})
                return find_word
                           
    def count(self, word):
        count_word = {}
        lines = self.get_all_words()[self.file_name]
        count_word.update({self.file_name: lines.count(word.lower())})
        return count_word

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего