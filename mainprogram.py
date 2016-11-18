import sys
import time
def initialize():
    # Create initialization data and take a lot of time

    data = []
    datafile = sys.argv[1]
    starttimeinmillis = int(round(time.time()))

    f = open(datafile, 'r')
    l = f.readline()
    while (l != ''):
        a = l.split()
        l2 = []
        for j in range(0, len(a), 1):
            l2.append(float(a[j]))
        #l2.append(float(1))
        data.append(l2)
        l = f.readline()

    rows = len(data)
    cols = len(data[0])
    # print(data)
    f.close()
    #print("rows=", rows, " cols=", cols)
    #print("total time taken:",int(round(time.time()))-starttimeinmillis)
    return data

#def select_features( data ):
    #print()
    # Code to test