###############################################################################################
##################################### VISHAL KULKARNI | VVK27 #################################
###############################################################################################

import sys
import random
import math
import time
import Balance_error
start=time.time()

def findHingeLoss(data, predictLabels):
    rows = len(data)
    cols = len(data[0])
    print("rows & cols",rows, cols)
    print(len(predictLabels))
    ###############################
    ##### read training labels ####
    ###############################

    labelfile = predictLabels
    trainlabels = {}
    n = [0, 0]

    for i in range(0,len(predictLabels),1):
        a = predictLabels[i]

        trainlabels[int(a[1])] = int(a[0])
        #    trainlabels_size[a[0]] = trainlabels_size[a[0]]+1
        if (trainlabels[a[1]] == 0):
            trainlabels[a[1]] = -1;

        n[int(a[0])] += 1

    print(trainlabels)
    ##################################
    ########## initialize w ##########
    ##################################
    # print("this is new code")
    w = []
    for j in range(0, cols, 1):
        # print(random.random())
        w.append(0.02 * random.random() - 0.01)


    # print(w)

    #####################################
    #### calculation of doc product #####
    #####################################

    def dot_product(a, b):
        dp = 0
        for i in range(0, cols, 1):
            dp += a[i] * b[i]
        # dp = sum(p*q for p,q in zip(a, b))
        return dp


    #######################################
    ##### gradient descent iteration ######
    #######################################

    # eta = 0.0001           #### eta for ionosphere #####
    #eta = 0.000000001      #### eta for breast cancer #####
    eta = 0.00001
    hingloss = rows*10
    diff = 1
    count = 0
    # for i in range(0, 500, 1):

    while ((diff) > 0.01):
        dellf = [0]*cols
        for j in range(0, rows, 1):
            if (trainlabels.get((j)) != None):
                dp = dot_product(w, data[j])
                condition = (trainlabels.get((j)) * (dot_product(w, data[j])))
                for k in range(0, cols, 1):
                    if (condition < 1):
                        dellf[k] += -1 * ((trainlabels.get((j))) * data[j][k])
                    else:
                        dellf[k] += 0
                        #                print ("dellf",dellf)
                        #    print("delf",dellf)
        ##########################
        ####### update w #########
        ##########################

        for j in range(0, cols, 1):
            w[j] = w[j] - eta * dellf[j]
        prev = hingloss
        hingloss = 0

        #################################
        #### compute hinge loss #########
        #################################
        for j in range(0, rows, 1):
            if (trainlabels.get((j)) != None):
                # print(dot_product(w,data[j]))
                hingloss += max(0, 1 - (trainlabels.get((j)) * dot_product(w, data[j])))
                #            print ("errror",hingloss)
            #    if(prev>hingloss):
            diff = abs(prev - hingloss)
            # else:
            #        eta = 0.00001
        #    print("diff", diff)
        #    count = count + 1
        #    print("count", count)
        #    if(hingloss<0):
        #        break


        print ("hingloss = " + str(hingloss))

    # print("w= ")
    normw = 0
    for i in range(0, (cols - 1), 1):
        normw += w[i] ** 2
    print ("w ",w)

    # print("")

    # normw = (normw)**0.5
    normw = math.sqrt(normw)
    # print("sqrt")
    print("||w||="+str(normw))
    # print("")

    d_orgin = abs(w[len(w) - 1] / normw)

    print ("Distance to origin = " + str(d_orgin))

    #################################
    ###### calc of prediction #######
    #################################
    f = open('/Users/vishalkulkarni/Developments/Project_MachineLearning/pred1', 'w')
    for i in range(0, rows, 1):
        if (trainlabels.get((i)) == None):
            dp = dot_product(w, data[i])
            if (dp > 0):
                print("1 " + str(i))
                f.write("1 " + str(i)+'\n')
            else:
                print("0 " + str(i))
                f.write("0 " + str(i)+'\n')
    f.close()
    Balance_error.balance_error("/Users/vishalkulkarni/Developments/Project_MachineLearning/datasets/breast_cancer.labels", "/Users/vishalkulkarni/Developments/Project_MachineLearning/pred1")
    print("total execution time:",(time.time()-start)/60)



