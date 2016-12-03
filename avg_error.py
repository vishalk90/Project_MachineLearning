import sys

import subprocess
import Balance_error

def avg_error():
    #data = sys.argv[1]
    predictions = []
    #predict="/Users/vishalkulkarni/Developments/Project_MachineLearning/prediction.txt"
    cnt =0
    for i in range(50):

        cnt = cnt +1
        print("loop",cnt)
        #print("python3 '/home/kalyani/PycharmProjects/machine learning/SNP/SVC.py' "+
              #" '"+data+"'"+" '/home/kalyani/Desktop/MS-Fall-2016/dataset/test/SNP/labels"+str(i)+"' > '/home/kalyani/PycharmProjects/machine learning/prediction.txt'")
        subprocess.call("python3 '/Users/vishalkulkarni/Developments/Project_MachineLearning/wrapper.py' "+" "
                        +"/Users/vishalkulkarni/Developments/Project_MachineLearning/secdata" + " "
                        +"/Users/vishalkulkarni/Developments/Project_MachineLearning/datasets/trueclass.txt",shell = True)

        predictions.append(Balance_error.balance_error("/Users/vishalkulkarni/Developments/Project_MachineLearning/datasets/trueclass.txt", "/Users/vishalkulkarni/Developments/Project_MachineLearning/pred0"))

    mean = sum(predictions)/cnt
    accu = (1-mean)*100
    print("mean error is :",mean)
    print("accuracy error is :",accu )

avg_error()