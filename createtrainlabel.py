import random


def createtrainlabel(data):
    rand = []
    tl = len(data)
    #print(tl)
    #rand = [random.randrange(0, (tl-1)) for x in range(0,(tl),1)]
    #print(rand)
    #print(x for x in range(1,10,1))
    #print("starting...")
    for x in range(0, int(tl*0.1) ,1):
        del data[random.randrange(0, (len(data)-1))]
    for x in data:
        print(str(int(x[0]))+" "+str(int(x[1])))
