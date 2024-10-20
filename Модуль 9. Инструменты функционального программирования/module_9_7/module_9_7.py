def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        summ = sum(args)
        if summ % 2 != 0:
            print('Простое')
        else:
            print('Составное')
        return result
    return wrapper

@is_prime    
def sum_three(*args):
    return sum(args)

result = sum_three(2, 3, 6)
print(result)