from time import sleep
from threading import *

class Hello(Thread):

    def run(self):
        for i in range(100):
            print("Hello")
            sleep(1)
        
class World(Thread):
    
    def run(self):
        for i in range(100):
            print("World")
            sleep(1)
    
x1 = Hello()
x2 = World()

x1.start()
x2.start()
