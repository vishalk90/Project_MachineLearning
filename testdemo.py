import Fscore
import time
start=time.time()
data, features, labels  = Fscore.creatingDataset()

fscore = Fscore.calculateFscore(data, features, labels)

secdata = Fscore.selectFeature(features,fscore)
f = open('/Users/vishalkulkarni/Developments/Project_MachineLearning/secdata', 'w')
print("cols",len(secdata[0]))
for i in range(0, len(secdata),1):
    for j in range(0, len(secdata[i]),1):
        #print(int(secdata[i][j]))

    #print([x+" " for x in secdata[i]])
    #print('\n')
        f.write(str(int(secdata[i][j]))+" ")
    f.write('\n')
f.close()
print("Total time:",(time.time()-start))
#f.write(str(secdata))
