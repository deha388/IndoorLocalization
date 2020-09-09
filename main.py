import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics

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
    time.sleep(127)

    for key in client1.keyMapDict:
        if key in client2.keyMapDict and key in client3.keyMapDict and key in client4.keyMapDict and key in client5.keyMapDict:
            a_dict[key] = [client1.keyMapDict[key], client2.keyMapDict[key],client3.keyMapDict[key],client4.keyMapDict[key],client5.keyMapDict[key]]
    print("\033[1;34;40m Bright Blue \n")
    print(a_dict)

    PavoDataset = pd.read_csv('dataset.csv')
    print(PavoDataset.head(6))
    print(PavoDataset.describe())
    location = PavoDataset['location2'][:]
    print(location.head(6))

    X = PavoDataset.drop(['location3', 'location1', 'location2'], axis=1)

    X_train, X_test, y_train, y_test = train_test_split(X, location, test_size=0.10)

    knn = KNeighborsClassifier(n_neighbors=7,metric='minkowski')

    X_train, X_test, y_train, y_test = train_test_split(X, location, test_size=0.10)
    knn.fit(X_train, y_train)

    def predictData():

        values = []
        for key in a_dict:
            asd = a_dict[key]
            va = knn.predict(list([asd]))
            print("2) Using K Neighbors Classifier Prediction is " + str(key) + str(va))

    predictData()




