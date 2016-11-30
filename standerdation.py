import sys

######################
#CREATING DATA MATRIX#
######################

def calculatinglength(data):
    rows = len(data)
    cols = len(data[0])
    distance = []
    for i in range(cols):
        sum = 0
        for j in range(rows):
            sum += (float(data[j][i])) ** 2
        sum = sum ** 0.5
        distance.append(sum)
    data=standerdition(data,distance)
    return data

def standerdition(data,distance):
    #print(data)
    rows = len(data)
    cols = len(data[0])
    for i in range(cols):
        for j in range(rows):
            if(distance[i] != 0):
                data[j][i]= (float(data[j][i])/distance[i])
            else:
                distance[i] = 1
                data[j][i] = (float(data[j][i]) / distance[i])
    return data;