import sys
#from Naive_bays_classifier import calculateMean
#from  hinge_loss_cp1 import wInitialization
######################
#CREATING DATA MATRIX#
######################

def creatingDataset():
    # opening files
    file1 = sys.argv[1]
    with open(file1) as datafile:
        data = [line.split() for line in datafile]
    features = [list(map(float,x)) for x in zip(*data)]
    file2 = sys.argv[2]
    with open(file2) as datafile:
        data_labels = [line.split() for line in datafile]
    labels = {int(x[1]):int(x[0]) for x in data_labels}
    for i in range(len(labels)):
        if(labels.get(i) == 0):
            labels[i]= -1
    print("creating dataset")
    return data, features, labels

def calculateFscore(data, features, labels):
    positive = 0
    negative = 0
    num_feat = len(features)
    num = len(features[0])
    F_score =[]
    for i in range(num_feat):
        pos_list = []
        neg_list = []
        for j in range(len(labels)):
            if(labels.get(j) == 1):
                positive +=1
                pos_list.append(features[i][j])
            else:
                negative +=1
                neg_list.append(features[i][j])
        mean = sum(features[i])/num
        mean_pos = sum(pos_list)/positive
        mean_neg = sum(neg_list)/negative
        vpos=0
        for x in pos_list:
            vpos +=(x - mean_pos) ** 2
        var_pos = vpos/positive
        vneg = 0
        for x in neg_list:
            vneg += (x - mean_neg) ** 2
        var_neg = vneg / negative
        fscore = ((mean_pos - mean)**2+(mean_neg - mean)**2)/(var_pos + var_neg)
        F_score.append(fscore)
    print("calculate score")
    return F_score

def selectFeature(features, F_score):
    num_feat = len(features)
    print("I am here")
    seldata = [features[i] for i in range(num_feat) if F_score[i] > 28800]
    print("I am there")
    print(len(seldata))
    secdata = [list(x) for x in zip(*seldata)]
    print("datarow", len(secdata))
    print("datacol", len(secdata[0]))
    return secdata
    #callClasifier(labels,secdata)


#def callClasifier(labels,data):
#    wInitialization(data,labels)
