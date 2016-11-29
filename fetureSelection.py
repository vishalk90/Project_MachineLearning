import sys
from sklearn.svm import LinearSVC
import numpy as np

def calFetures(data, labels):
    #X = np.array((data))     #for LinearSVC
    #X = np.array((data))
    #y = np.array([x[0] for x in labels])
    print("inside feature calc")
    linearSVC = LinearSVC(C=0.0025, penalty='l1', dual=False).fit(data,[x[0] for x in labels])
    score = linearSVC.__dict__.get('coef_')

    feature = []
    for k in range(len(score[0])):
        if(score[0][k] != 0.0):
            rows =[]
            for i in range(len(data)):
                rows.append(data[i][k])
            feature.append(rows)
    secdata = [list(map(float, x)) for x in zip(*feature)]
    return secdata