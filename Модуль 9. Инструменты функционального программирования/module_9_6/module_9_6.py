def all_variants(text):
    for letters in text:
        yield letters
    for lines in text:
        if lines != letters:
            yield lines + letters
    yield text
              
        
a = all_variants("abc")
for i in a:
    print(i)