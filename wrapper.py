import sys
import traceback
import mainprogram
import classify
import createtrainlabel
from imp import reload


if __name__=='__main__':

    cache = None
    labels = None
    is_first_iteration = True

    while True:
        if not cache:
            cache = mainprogram.initialize(1)
            labels = mainprogram.initialize(2)
        try:
            if not is_first_iteration:
                reload(mainprogram)
            is_first_iteration = False
            #mainprogram.select_features( cache )
            data1, predict1,labels1, predictlabels = createtrainlabel.createtrainlabel(cache,labels)
            classify.classify(data1, labels1, predict1, predictlabels)
        except Exception as e:
            print ('*' * 64)
            print ('Exception raised in tested module')
            print (traceback.print_exc())
            print ('*' * 64)
        print ("Press enter to re-run script or CTRL-C to exit")
        sys.stdin.readline()