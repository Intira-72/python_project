import threading

def func_one():
    for x in range(10000):
        print("ONE")

def func_two():
    for x in range(10000):
        print("TWO")

if __name__=="__main__":
    f1 = threading.Thread(target=func_one)
    f2 = threading.Thread(target=func_two)

    f1.start()
    f2.start()