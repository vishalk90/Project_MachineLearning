import sys
import time
def initialize(x: object) -> object:
    # Create initialization data and take a lot of time

    data = []
    starttimeinmillis = int(round(time.time()))

    c =0
    file1 = sys.argv[x]
    with open(file1) as datafile:
        for line in datafile:
            c+=1
            if(c%100==0):
                print(".",sep='', end='',flush=True)
            data.append([int(l) for l in line.split()])

    rows = len(data)
    cols = len(data[0])
    # print(data)

    #print("rows=", rows, " cols=", cols)
    print("time took:",int(round(time.time()))-starttimeinmillis,"seconds")
    return data
