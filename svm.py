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
print("fin2")
from sklearn.svm import SVC
import sklearn as sk
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cross_validation import train_test_split
from sklearn.cross_validation import cross_val_score, KFold
from sklearn.svm import LinearSVC
from sklearn import preprocessing
from sklearn.multiclass import OneVsOneClassifier
from scipy.stats import sem
#from sklearn import svm

svc_1=LinearSVC(random_state=0)

#rbf_svc = svm.SVC(kernel='rbf')

classifier=OneVsOneClassifier(svc_1)
print("fin3")
classifier.fit(datset,tarset)
#cv=KFold(len(y),k,shuffle=True,random_state=0)
#scores =cross_val_score(clf,x,y,cv=cv)
print("fin4")
pred_labels=classifier.predict(testdat)
print("fin5")
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

true_labels=testtar

from sklearn import metrics

print(metrics.accuracy_score(true_labels,pred_labels))
print("fin6")
print(metrics.confusion_matrix(true_labels,pred_labels))

from sklearn.metrics import classification_report

targets=['class1','class2','class3','class4']
print('\n',classification_report(true_labels,pred_labels,target_names=targets))

print("fin!")

elapsed_time = time.time() - start_time
print(elapsed_time)

