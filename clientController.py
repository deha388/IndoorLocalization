import os, sys
import threading
from threading import Thread
import time

class Example():
    def __init__(self):
        self.method_1()

    def method_1(self):

        def run(self):
            threading.Thread(target = function_a, args = (self,)).start()
            threading.Thread(target = function_b, args = (self,)).start()

        def function_a(self):
            for i in range(10):
                print (1)
                time.sleep(0.01) # Add some delay here

        def function_b(self):
            for i in range(10):
                print (2)
                time.sleep(0.01) # and here


        run(self)


Example()
