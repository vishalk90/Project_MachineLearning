import sys
import numpy as np
import numpy
from sklearn.svm import LinearSVC
from sklearn.svm import SVC
from sklearn.preprocessing import scale
from sklearn import svm




def creatingDataset():
    '''''data= [[-1, -1], [-2, -1], [1, 1], [2, 1]]
    labels = [1, 1, 2, 2]
    testdata = [[2,2]]
    testlabels = [1]
    '''
    file1 = sys.argv[1]
    rawdata =[]
    with open(file1) as datafile:
        for line in datafile:
            line =line.split()
            data_value =[]
            for i in range(len(line)):
                data_value.append(float(line[i]))
            rawdata.append(data_value)
    #print(rawdata)
    file2 = sys.argv[2]
    with open(file2) as datafile:
        data_labels = [line.split() for line in datafile]
    rawlabels = {int(x[1]): int(x[0]) for x in data_labels}
    labels = [int(x[0]) for x in data_labels]
    #print(labels)
    testdata =[]
    data = []
    testlabels =[]
    for i in range (len(rawdata)):
        if(rawlabels.get(i) == None):
            testdata.append(rawdata[i])
            testlabels.append(i)
        else:
            data.append(rawdata[i])
    #print(data)
    #print(labels)
    #print(testdata)
    #print(testlabels)
    #print(labels)'''
    X = np.array(data)
    y = np.array(labels)
    CallSVC(X,labels,testdata,testlabels)

def CallSVC(data,labels,testdata,testlabels):
    print("I am here")
    data = scale(data)
    testdata = scale(testdata)
    #svc = svm.LinearSVC(C=1,verbose=1,max_iter=100000).fit(data, labels)
    svc = svm.SVC(kernel='rbf', C=1,verbose=0).fit(data, labels)


    '''LinearSVC(penalty='l1', loss='squared_hinge', dual=False, tol=0.0001, C=1.0, multi_class='ovr', fit_intercept=True,
              intercept_scaling=1, class_weight=None, verbose=1, random_state=None, max_iter=-1)'''

    print("\n")
    for i in range(len(testdata)):
        print(svc.predict([testdata[i]]),testlabels[i])
