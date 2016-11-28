import numpy as np
from sklearn.svm import LinearSVC
from sklearn.svm import SVC
from sklearn.preprocessing import scale
import Balance_error
from sklearn import tree

def classify(data, labels, predict, predictlabels):

    X = np.array(scale(data))     #for LinearSVC
    #X = np.array((data))
    y = np.array(labels)

    print(X)
    print(y)

    print("reached to classify")

    ########################################
    ######### classification method ########
    ########################################

    clf = LinearSVC(max_iter=10000, verbose=1,).fit(X,[x[0] for x in y])
    #clf = SVC(kernel='rbf', max_iter=10000, verbose=1,).fit(X,[x[0] for x in y])
    #clf = tree.DecisionTreeClassifier().fit(X,[x[0] for x in y])


    ########################################
    ######## data prediction methods #######
    ########################################

    #predictedl=clf.predict((predict))
    predictedl=clf.predict(scale(predict))     #For LinearSVC


    ##########################################
    ######## writing and printing data #######
    ##########################################
    finalout = []
    print('/n')

    f = open('/Users/vishalkulkarni/Developments/Project_MachineLearning/pred0', 'w')
    for i in range(0, len(predict), 1):

        l =[]
        l.append(predictlabels[i])
        l.append(int(predictedl[i]))

        finalout.append(l)

        print(str(int(predictedl[i]))+" "+str(predictlabels[i]))

        f.write(str(int(predictedl[i]))+" "+str(predictlabels[i])+'\n')

    f.close()


    #####################################################
    ######## method call to find accuracy and BER #######
    #####################################################

    #Balance_error.balance_error("/Users/vishalkulkarni/Developments/Project_MachineLearning/datasets/trueclass.txt", "/Users/vishalkulkarni/Developments/Project_MachineLearning/pred0")
    Balance_error.balance_error("/Users/vishalkulkarni/Developments/Project_MachineLearning/datasets/breast_cancer.labels", "/Users/vishalkulkarni/Developments/Project_MachineLearning/pred0")