import sys
import traceback
import mainprogram
import createtrainlabel

if __name__=='__main__':

    cache = None
    is_first_iteration = True

    while True:
        if not cache:
            cache = mainprogram.initialize()
        try:
            if not is_first_iteration:
                reload( mainprogram )
            is_first_iteration = False
            #mainprogram.select_features( cache )
            createtrainlabel.createtrainlabel(cache)
        except Exception, e:
            print '*' * 64
            print 'Exception raised in tested module'
            print traceback.print_exc()
            print '*' * 64

        print "Press enter to re-run script or CTRL-C to exit"
        sys.stdin.readline()