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

print(len(datset))


from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
print("fin2")
sc.fit(datset)
print("fin3")
train_std=sc.transform(datset)
test_std=sc.transform(testdat)
print("fin4")
ml= RandomForestClassifier(criterion='entropy',n_estimators=10,n_jobs=2,random_state=1)
print("fin5")
ml.fit(train_std,tarset)
print("fin6")
pred=ml.predict(test_std)

from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

true_labels=testtar

from sklearn import metrics

print(metrics.accuracy_score(true_labels,pred))
print("fin6")
print(metrics.confusion_matrix(true_labels,pred))

print('총테스트개수 :%d 오류개수:%d' %(len(testtar),(testtar!=pred).sum()))
#print('정확도:%.2f' %accuracy_score(testtar,pred))
from sklearn.metrics import classification_report

targets=['class1','class2','class3','class4']
print('\n',classification_report(true_labels,pred,target_names=targets))

elapsed_time = time.time() - start_time
print(elapsed_time)
