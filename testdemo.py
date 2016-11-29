import Fscore
import sys
import time
import fetureSelection
import mainprogram
from imp import reload
import traceback
start=time.time()

if __name__=='__main__':

    cache = None
    labels = None
    is_first_iteration = True

    while True:
        if not cache:
            data = mainprogram.initialize(1)
            labels = mainprogram.initialize(2)
        try:
            if not is_first_iteration:
                reload(mainprogram)
            is_first_iteration = False

            secdata = fetureSelection.calFetures(data,labels)

            #data, features, labels  = Fscore.creatingDataset()

            #fscore = Fscore.calculateFscore(data, features, labels)

            #secdata = Fscore.selectFeature(features,fscore)



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
        except Exception as e:
            print ('*' * 64)
            print ('Exception raised in tested module')
            print (traceback.print_exc())
            print ('*' * 64)
        print ("Press enter to re-run script or CTRL-C to exit")
        sys.stdin.readline()