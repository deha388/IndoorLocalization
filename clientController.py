import os, sys
import threading
from threading import Thread
import time
import client1
import client2



def method_1():

    def run():
            threading.Thread(target = function_a, args = ()).start()
            threading.Thread(target = function_b, args = ()).start()

    def function_a():
            client1.runClient1()
            time.sleep(0.1) # Add some delay here

    def function_b():

            client2.runClient2()
            time.sleep(0.1) # and here
    run()






