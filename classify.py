import numpy as np
from sklearn.svm import LinearSVC
from sklearn.svm import SVC
from sklearn.preprocessing import scale

def classify(data, labels, predict, predictlabels):
    X = np.array(scale(data))     #for LinearSVC
    #X = np.array((data))
    y = np.array(labels)
    print(X)
    print(y)
    print("reached to classify")
    clf = LinearSVC(max_iter=10000, verbose=1,).fit(X,[x[0] for x in y])




#    SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
#        decision_function_shape=None, degree=3, gamma='auto', kernel='linear',
#        max_iter=-1, probability=False, random_state=None, shrinking=True,
#        tol=0.000000001, verbose=False)
#    LinearSVC(C=1.0, class_weight=None, dual=False, fit_intercept=True,
#              intercept_scaling=1, loss='hinge', max_iter=20000,
#              multi_class='crammer_singer', penalty='l2', random_state=None, tol=0.00000000001,
#              verbose=0)








    #loss ='hinge''squared_hinge'
    predictedl=[]
    finalout = []

#    predictedl=clf.predict((predict))
    predictedl=clf.predict(scale(predict))     #For LinearSVC

    print('/n')
    f = open('/Users/vishalkulkarni/Developments/Project_MachineLearning/pred0', 'w')
    for i in range(0, len(predict), 1):
        #print(int(predictedl[i]), predictlabels[i])
        l =[]
        l.append(predictlabels[i])
        l.append(int(predictedl[i]))

        #finalout.append(str(int(predictedl[i]))+" "+str(predictlabels[i]))
        finalout.append(l)
        print(str(int(predictedl[i]))+" "+str(predictlabels[i]))


        f.write(str(int(predictedl[i]))+" "+str(predictlabels[i]))

    #finalout.sort()
    #for i in range(0, len(predict), 1):
    #    print(finalout[i])

    #print(clf.predict(predict))
    f.close()