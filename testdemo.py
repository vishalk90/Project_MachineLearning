import Fscore
import time
import fetureSelection
import mainprogram
import threading
import sys
start=time.time()

print("Reading data", end='')

########################################
########### Reading Data ###############
########################################
data = mainprogram.initialize(1)
labels = mainprogram.initialize(2)



######################################################
######## calling method for Feature Select ###########
######################################################

secdata = fetureSelection.calFetures(data,labels)

#data, features, labels  = Fscore.creatingDataset()
#fscore = Fscore.calculateFscore(data, features, labels)
#secdata = Fscore.selectFeature(features,fscore)



##########################################################
######## writing selected feature data to file ###########
##########################################################

f = open('/Users/vishalkulkarni/Developments/Project_MachineLearning/secdata', 'w')

print("Number of Features selected:",len(secdata[0]))

for i in range(0, len(secdata),1):
    for j in range(0, len(secdata[i]),1):
        f.write(str(int(secdata[i][j]))+" ")
    f.write('\n')

f.close()

print("Total time:",(time.time()-start))
