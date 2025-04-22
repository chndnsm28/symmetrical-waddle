from threading import *
from time import sleep

def display(str1):
    l.acquire()
    for x in str1:
        print(x)
        sleep(1)
    l.release()


l = Semaphore(2)
t1 = Thread(target=display, args=("Hello WORLD",))

t2 = Thread(target=display,  args=("you are welcome",))
t3 = Thread(target=display,  args=("0123456789",))

t1.start()
t2.start()

t1.join()
t2.join()