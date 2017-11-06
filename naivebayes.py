import csv
import numpy as np
import time

start_time = time.time()

def read_lines2(type):
    datnam=type+"data.txt"
    tarnam=type+"tar.txt"
    arr=[]
    arr2=[]
    with open(datnam, 'rU') as data:
        reader = csv.reader(data)
        y=0
        for row in reader:
            #y=y+1
            #print(x)
            new = [float(x) for x in row if x != '']
            arr.append(new)
            #print(new)
            #if x==10:
                #break
    with open(tarnam, 'rU') as data:
        dat=csv.reader(data)
        for line in dat:
            
            arr2.append(float(line[0]))

    return {'dat':arr,'tar':arr2}
rec=read_lines2("train")
rec2=read_lines2("test")
print("fin1")
datset=np.array(rec['dat'])
tarset=np.array(rec['tar'])
testdat=np.array(rec2['dat'])
testtar=np.array(rec2['tar'])

import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB
from sklearn import cross_validation
#from utilities import visualize_classifier

classifier = GaussianNB()

#classifier.fit(datset,tarset)

pred=classifier.fit(datset,tarset).predict(testdat)
#pred=classifier.predict(testdat)

accuracy=100.0 * (testtar==pred).sum() / testdat.shape[0]
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

true_labels=testtar

from sklearn import metrics

print(metrics.accuracy_score(true_labels,pred))
print("fin6")
print(metrics.confusion_matrix(true_labels,pred))

print("accuracy of classifier =",round(accuracy,2),"%")
targets=['class1','class2','class3','class4']
print(classification_report(true_labels,pred,target_names=targets))

#visualize_classifier(classifier,testdat,testtar)
elapsed_time = time.time() - start_time
print(elapsed_time)
