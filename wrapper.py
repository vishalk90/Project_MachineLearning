import sys
import traceback
import mainprogram
import classify
import createtrainlabel
from imp import reload
import standerdation
import hingeloss


if __name__=='__main__':

    cache = None
    labels = None
    is_first_iteration = True

    while True:
    #for k in range(0,1,1): #if wants to run for once
        if not cache:
            cache = mainprogram.initialize(1)
            labels = mainprogram.initialize(2)
        try:
            if not is_first_iteration:
                reload(mainprogram)
            is_first_iteration = False

            #stdata = standerdation.calculatinglength(cache)

            org_data, org_labels, data1, predictdata,labels1, predictlabels = createtrainlabel.createtrainlabel(cache,labels)
            classify.classify(data1, labels1, predictdata, predictlabels)
            #hingeloss.findHingeLoss(org_data,labels1)
            cache = org_data
            labels = org_labels
            print(len(org_data), len(org_labels))
        except Exception as e:
            print ('*' * 64)
            print ('Exception raised in tested module')
            print (traceback.print_exc())
            print ('*' * 64)
        print ("Press enter to re-run script or CTRL-C to exit")
        sys.stdin.readline()