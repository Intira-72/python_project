import threading
import time

x = 8192
lock = threading.Lock()

def double():
    global x, lock
    lock.acquire()
    while x < 16384:
        x *= 2
        print(x)
        time.sleep(1)
    print("Reached the maximum.")
    lock.release()


def halve():
    global x, lock
    lock.acquire()
    while x > 1:
        x /= 2
        print(x)
        time.sleep(1)
    print("Reached the minimum.")
    lock.release()


semaphore = threading.BoundedSemaphore(value=5)
def access(thread_number):
    print(f"{thread_number} is trying to access.")
    semaphore.acquire()
    print(f"{thread_number} was granted access.")
    time.sleep(10)
    print(f"{thread_number} is now releasing.")
    semaphore.release()


if __name__=="__main__":
    for thread_number in range(1, 11):
        t = threading.Thread(target=access, args=(thread_number,))
        t.start()
        time.sleep(1)