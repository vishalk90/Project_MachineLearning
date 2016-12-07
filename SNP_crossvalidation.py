#################################################################
#################################################################
####                                                         ####
####   PROJECT AUTHORS : VISHAL KULKARNI   &  KALYANI TARU   ####
####                                                         ####
####               UCID:      VVK27                KVT3      ####
####                                                         ####
#################################################################
#################################################################

import random
import time
import sys
from sklearn.svm import LinearSVC
import classify

#######################################
####### reading data from args ########
#######################################

def readfile(x):
    data = []
    c =0
    starttimeinmillis = int(round(time.time()))
    print("Reading data from file[",x,"]",sep='',end='',flush=True)
    try:
        file = sys.argv[x]
    except IndexError:
        print()
        print ("#"*104)
        print("###### Improper Syntax: try - python3 SNP_FinalProject.py traindata trainlabels testdata {i.e. 3 dataset files} #####")
        print ("#"*104)
        sys.exit()

    with open(file) as datafile:
        for line in datafile:
            c+=1
            if(c%100==0):
                print(".",sep='', end='',flush=True)
            data.append([int(l) for l in line.split()])

    #rows = len(data)
    #cols = len(data[0])
    # print(data)

    #print("rows=", rows, " cols=", cols)
    print("time took:",int(round(time.time()))-starttimeinmillis,"seconds")
    return data

###########################################################
####### creating train dataset for cross validation #######
###########################################################

def createTrainlabel(data, labels):
    org_data = [x for x in data]
    org_labels = [x for x in labels]
    print("Original data:",len(org_data))
    rows = len(data)
    print(int(rows*0.1))

    print("starting...")
    predictdata = []
    rangef=int(rows*0.1)
    predictlabels =[]
    if rangef<1:
        rangef = 1
    for x in range(0, rangef ,1):
        randomnum = random.randrange(0, (len(data)-1))
        predictlabels.append(randomnum)
        predictdata.append(data[randomnum])
        del data[randomnum]
        del labels[randomnum]
    return org_data, org_labels, data, labels, predictdata, predictlabels

##########################################
############ Feature selection ###########
##########################################

def calFetures(data, labels):

    print("Now selecting the bestfeatures....................",sep='', end='',flush=True)
    linearSVC = LinearSVC(C=0.0024, penalty='l1', dual=False).fit(data,[x[0] for x in labels]) # HERE CHANGE THE VALUE OF C FROM 0.002 TO 0.0021 OR 0.0024 OR 0.003 OR MORE TO GET MORE FEATURES {MORE ACCURACY}...(:D)
    score = linearSVC.coef_
    #print(score)
    feature = []
    feature_cols = []
    for k in range(len(score[0])):
        if(score[0][k] != 0.0):
            feature_cols.append(int(k))
            rowdata = []
            for i in range(len(data)):
                rowdata.append(data[i][k])
            feature.append(rowdata)
    bestfeatures_data = [list(map(float, x)) for x in zip(*feature)]
    #return bestfeatures_data
    #print(feature_cols)
    #---------------------------------------------------
    #------ writing selected feature data to file ------
    #---------------------------------------------------

    bestfeaturesdata_file = open('/Users/vishalkulkarni/Developments/Project_MachineLearning/bestfeaturedata', 'w')

    print("Number of Features selected in traindata:",len(bestfeatures_data[0]))

    for i in range(0, len(bestfeatures_data),1):
        for j in range(0, len(bestfeatures_data[i]),1):
            bestfeaturesdata_file.write(str(int(bestfeatures_data[i][j]))+" ")
        bestfeaturesdata_file.write('\n')

    bestfeaturesdata_file.close()

    return bestfeatures_data, feature_cols

###################################################
##### selecting the best feature of testdata ######
###################################################

def getFetures(testdata,feature_cols):
    print("Now getting the bestfeatures for testdata.........",sep='', end='',flush=True)

    bestfeature_testdata = []
    totalFeatures=len(feature_cols)


    for rows in range(len(testdata)):
        col = []
        k=0
        for cols in range(len(testdata[0])):
            if(k<totalFeatures and feature_cols[k] == cols):
                col.append(testdata[rows][cols])
                k+=1
        bestfeature_testdata.append(col)
    #print(bestfeature_testdata)

    bestfeaturestestdata_file = open('/Users/vishalkulkarni/Developments/Project_MachineLearning/bestfeaturestestdata', 'w')

    print("Number of Features selected in testdata:",len(bestfeature_testdata[0]))

    for i in range(0, len(bestfeature_testdata),1):
        for j in range(0, len(bestfeature_testdata[i]),1):
            bestfeaturestestdata_file.write(str(bestfeature_testdata[i][j])+" ")
        bestfeaturestestdata_file.write('\n')

    bestfeaturestestdata_file.close()

    return bestfeature_testdata


#######################################
########### classify data #############
#######################################

def predictLabels(traindata, trainlabels, testdata, predictlabels):
    print("Classifying data",sep='',end='',flush=True)

    #--------------------------------------
    #-------- classification method -------
    #--------------------------------------

    clf = LinearSVC(max_iter=15000000, tol=0.00000001).fit(traindata,[x[0] for x in trainlabels])
    #clf = SVC(C=10, kernel='linear', verbose=1, tol=0.00000001).fit(data,[x[0] for x in labels])
    #clf = tree.DecisionTreeClassifier().fit(X,[x[0] for x in y])

    #--------------------------------------
    #------- data prediction methods ------
    #--------------------------------------

    predictedlabels=clf.predict((testdata))
    #predictedl=clf.predict(scale(predict))     #For LinearSVC

    #---------------------------------------
    #----- writing and printing data -------
    #---------------------------------------
    print('/n')

    predictedlabels_file = open('/Users/vishalkulkarni/Developments/Project_MachineLearning/predictedlabels', 'w')

    for i in range(0, len(testdata), 1):
        #print(str(predictedlabels[i])+" "+str(i))
        predictedlabels_file.write(str(predictedlabels[i])+" "+str(predictlabels[i])+'\n')

    predictedlabels_file.close()
    return True



def balance_error(path1,path2):
    #####################################
    # CREATING DICTIONARY FOR LABELFILE #
    #####################################
    #file1 = sys.argv[1]
    file1 = path1
    lablefile = open(file1)
    traininglabels = {}
    lable_line = lablefile.readline()
    while (lable_line != ''):
        lable_values = lable_line.split()
        traininglabels[int(lable_values[1])] = int(lable_values[0])
        lable_line = lablefile.readline()
    lablefile.close()

    ######################################
    # CREATING DICTIONARY FOR OUTPUTFILE #
    ######################################
    #file2 = sys.argv[2]
    file2 = path2
    outlablefile = open(file2)
    outtraininglabels = {}
    lable_line_out = outlablefile.readline()
    while (lable_line_out != ''):
        #lable_line_out = lable_line_out.replace("[",'')
        #lable_line_out = lable_line_out.replace("]",'')
        out_lable_values = lable_line_out.split()
        outtraininglabels[int(out_lable_values[1])] = int(out_lable_values[0])
        lable_line_out = outlablefile.readline()
    outlablefile.close()
    ###############################################
    # CALCULATING TRUE AND FALSE RESULT OF OUTPUT #
    ###############################################
    class0_true=0
    class0_fasle=0
    class1_true=0
    class1_false=0
    for key in outtraininglabels:
        if(traininglabels.get(key) == 0):
            if(outtraininglabels.get(key) == 0):
                class0_true += 1
            else:
                class0_fasle +=1

        else:
            if(outtraininglabels.get(key)==1 and traininglabels.get(key) == 1):
                class1_true += 1
            else:
                class1_false += 1

    #-----------------------------------------------
    # CALCULATING BALANCE_ERROR and ACCURACRY ------
    #-----------------------------------------------
    balance_error1 = float(class0_fasle)/(int(class0_fasle) + int(class0_true))
    balance_error2 = float(class1_false)/(int(class1_false) + int(class1_true))
    balance_error = (balance_error1 + balance_error2)/2

    accuracy = ((class0_true + class1_true)/len(outtraininglabels)) * 100
    return accuracy

def main():
    startTime = time.time()

    #traindata = threading.Thread(target=readfile(1)).start()
    #trainlabels = threading.Thread(target=readfile(2)).start()
    #testdata = threading.Thread(target=readfile(3)).start()

    traindata = readfile(1)
    trainlabels = readfile(2)
    testdata = readfile(3)

    #bestfeatures_data, feature_cols = calFetures(traindata,trainlabels)
    #bestfeature_testdata = getFetures(testdata,feature_cols)
    #isPredicted = predictLabels(bestfeatures_data,trainlabels,bestfeature_testdata)

    bestfeatures_data, feature_cols = calFetures(traindata,trainlabels)
    cnt =0
    predictions = []
    for x in range(20):
        cnt +=1
        if(x==0):
            org_data, org_labels, data, labels, predictdata, predictlabels = createTrainlabel(bestfeatures_data,trainlabels)
        else:
            org_data, org_labels, data, labels, predictdata, predictlabels = createTrainlabel(org_data,org_labels)
        isPredicted = predictLabels(data,labels,predictdata, predictlabels)
        predictions.append(balance_error("/Users/vishalkulkarni/Developments/Project_MachineLearning/datasets/trueclass.txt", "/Users/vishalkulkarni/Developments/Project_MachineLearning/predictedlabels"))
        print("Accuracy: ",predictions[x])
    print("Avg. accuracy is :",sum(predictions)/cnt)

    if(isPredicted):
        print ("#"*80)
        print("##      Data classified successfully and stored in 'predictedlabels' file     ##")
        print ("#"*80)

    totalTime = (time.time()-startTime)

    print("Total Execution Time: ",int(totalTime/60), "minutes",int(totalTime%60),"seconds")

main()
