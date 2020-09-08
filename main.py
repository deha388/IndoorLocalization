# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import client1
import client2
import client3
import client4
import client5

import clientController
import time

global a_dict
a_dict = {}




def print_hi(name):
    i = 0
    for i in range(5):
        print(f'Hi, {name}')

    # Use a breakpoint in the code line below to debug your script.
    # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    clientController.method_1()
    time.sleep(140)

    for key in client1.keyMapDict:
        if key in client2.keyMapDict and key in client3.keyMapDict and key in client4.keyMapDict and key in client5.keyMapDict:
            a_dict[key] = [client1.keyMapDict[key], client2.keyMapDict[key],client3.keyMapDict[key],client4.keyMapDict[key],client5.keyMapDict[key]]
    print("\033[1;34;40m Bright Blue \n")
    print(a_dict)


