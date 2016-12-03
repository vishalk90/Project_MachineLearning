
import sys

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

    ###############################
    # CALCULATING BALANCE_ERROR #
    ##############################
    balance_error1 = float(class0_fasle)/(int(class0_fasle) + int(class0_true))
    balance_error2 = float(class1_false)/(int(class1_false) + int(class1_true))
    balance_error = (balance_error1 + balance_error2)/2

    accuracy = ((class0_true + class1_true)/len(outtraininglabels)) * 100
    #print("class0_false",class0_fasle)
    #print("class0_true:",class0_true)
    #print("class1_false:",class1_false)
    #print("class1_true:",class1_true)
    #print("balance_error:",balance_error)
    #print("accuracy : ", accuracy)
    return balance_error

#balance_error("/Users/vishalkulkarni/Developments/Project_MachineLearning/datasets/trueclass.txt", "/Users/vishalkulkarni/Developments/Project_MachineLearning/pred0")
#balance_error("/Users/vishalkulkarni/Developments/Project_MachineLearning/datasets/breast_cancer.labels", "/Users/vishalkulkarni/Developments/Project_MachineLearning/pred1")