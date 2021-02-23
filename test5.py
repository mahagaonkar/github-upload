from threading import Thread

def func1():
    x = 100
    while x != 0:
        print("Supp")
        x -= x

def func2():
    x = 100
    while x != 0:
        print("bitch")
        x -= x

x = Thread(target=func1)
y = Thread(target=func2)

x, y.start()