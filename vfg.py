import os
from pynput.keyboard import Key, Listener
import time
def k():
    d = [[0 for x in range(10)] for k in range(10)]
    x = 0
    while True:
        
        print(d)
        time.sleep(1)
        print()
        print()
        d[x] = 1
        try:
            d[x-1] = 0
        except:
            pass
        x+=1
        if x == 10:
            x = 0
        os.system("clear")
k()

def on_press(key):
    print("{0} pressed".format(key))
    k()

def on_release(key):
    print("{0} released".format(key))

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
    




    


