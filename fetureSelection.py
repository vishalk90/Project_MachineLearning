from sklearn.svm import LinearSVC

########################################
######### Feature selection ############
########################################

def calFetures(data, labels):

    print("Now selecting the bestfeatures...",sep='', end='',flush=True)
    linearSVC = LinearSVC(C=0.002, penalty='l1', dual=False).fit(data,[x[0] for x in labels])
    score = linearSVC.coef_

    feature = []
    for k in range(len(score[0])):
        if(score[0][k] != 0.0):
            rows =[]
            for i in range(len(data)):
                rows.append(data[i][k])
            feature.append(rows)
    secdata = [list(map(float, x)) for x in zip(*feature)]
    return secdata