import logging
import threading
import time


def contador(name):
    for i in range(100):
        print(str(i)+ " ->Hilo ->"+name)


for i in range(2):
    hilo = threading.Thread(target=contador, args=(str(i),))
    hilo.start()
for i in range(100):
        print(str(i)+ " ->MAIN ->")