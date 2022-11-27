import time
import random
import datetime


def myrandint(start, end, seed):
    a = datetime.datetime.now().microsecond
    b = 1729
    rOld = seed
    m = end - start
    while True: 
        rNew = (a * rOld + b) % m
        yield rNew
        rOld = rNew


def gen(size, start, end):
    gen_sys = []
    gen_casual = []

    for i in range(size):
        time.sleep(0.01)
        random.seed()
        gen_sys.append(round(random.random() * end))

        r = myrandint(start, end, i + 5)
        gen_casual.append(next(r))

    print("Написанный: \t", gen_casual)
    print("Из библиотеки Питона: \t", gen_sys)
    

for i in range(5):
    gen(10, 0, 10)
    print()