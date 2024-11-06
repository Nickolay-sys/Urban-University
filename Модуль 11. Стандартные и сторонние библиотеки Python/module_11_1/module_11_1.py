import requests
from time import sleep
from random import randint
import numpy as np
import pandas as pd

def request_examples():
    response = requests.get("https://ya.ru/")
    print(f"{response.status_code}")
    sleep(1)
    print(f"\n{response.apparent_encoding}")
    sleep(1)
    print(f"\n{response.url}")
    sleep(1)

def numpy_examples():
    a = np.arange(randint(1,5))
    print(f"\n{a}")
    sleep(1)
    b = np.arange(randint(5,10))
    print(f"\n{b}")
    sleep(1)
    print(f"\n{np.concatenate((a,b))}")
    sleep(1)
    c = [4, 16, 14, 15, 3, 4, 12, 17, 19, 14, 5, 13, 12, 8, 11, 15, 20, 19, 1, 13]
    print(f"\n{c}")
    sleep(1)
    print(f"\n{np.sort(c)}")
    sleep(1)
    d = np.reshape(c,shape=(5,4),order="C")
    print(f"\n{d}")
    sleep(1)

def pandas_examples():
    s = pd.Series([i for i in range(randint(6,10))])
    print(f"\n{s}")
    sleep(1)
    print(f"\n{s.head()}")
    sleep(1)
    print(f"\n{s.tail()}")
    sleep(1)
    print(f"\n{s.describe()}")
    

if __name__ == "__main__":
    request_examples()
    numpy_examples()
    pandas_examples()