import os, sys
import threading
from threading import Thread
import time
import client1
import client2
import client3
import client4
import client5



def method_1():

    def run():
            threading.Thread(target = function_a, args = ()).start()
            threading.Thread(target = function_b, args = ()).start()
            threading.Thread(target = function_c, args = ()).start()
            threading.Thread(target = function_d, args = ()).start()
            threading.Thread(target = function_e, args = ()).start()

    def function_a():
            client1.runClient1()
            time.sleep(0.1) # Add some delay here

    def function_b():

            client2.runClient2()
            time.sleep(0.1) # and here
    def function_c():

            client3.runClient3()
            time.sleep(0.1) # and here
    def function_d():

            client4.runClient4()
            time.sleep(0.1) # and her
    def function_e():

            client5.runClient5()
            time.sleep(0.1) # and here
    run()






