
import sys
from sklearn.svm import LinearSVC



def creatingDataset():
    rawdata = []
    labels = []
    testdata = []
    file1 = sys.argv[1]
    with open(file1) as datafile:
        for line in datafile:
            rawdata.append([int(l) for l in line.split()])

    print("i am here")
    file2 = sys.argv[2]
    with open(file2) as labelfile:
        for line in labelfile:
            labels.append(int(line.split()[0]))

    file3 = sys.argv[3]
    with open(file3) as testfile:
        for line in testfile:
            testdata.append([int(l) for l in line.split()])

    return rawdata, labels,testdata


def calculateF(rawdata, labels,testdata):
    print("I am there")

    lsvc = LinearSVC(C=0.0021, penalty='l1', dual=False).fit(rawdata, labels)
    score = lsvc.coef_

    testfeature = []
    feature = []
    print("hiiii")

    for k in range(len(score[0])):
        #print(score[0][k])
        if(score[0][k] != 0.0):
            rows = []
            testrows = []
            for i in range(len(rawdata)):
                rows.append(rawdata[i][k])
            feature.append(rows)

            for i in range(len(testdata)):
                testrows.append(testdata[i][k])
            testfeature.append(testrows)

    data = [list(map(float,x)) for x in zip(*feature)]
    test = [list(map(float, x)) for x in zip(*testfeature)]
    #print(rawdata)
    #print(data)

    print(len(data),len(data[0]))
    print(len(test), len(test[0]))

    datafile = open("/home/kalyani/PycharmProjects/machine learning/data/svctrain0021.txt", 'w')
    for item in data:
        datafile.write("%s\n" % item)

    testfile = open("/home/kalyani/PycharmProjects/machine learning/data/svctest0021.txt", 'w')
    for item in test:
        testfile.write("%s\n" % item)