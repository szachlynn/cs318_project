import math
from numpy import array, matrix, random

def d(x1,y1,z1,x2,y2,z2):

    return ((x1-x2)**2+(y1-y2)**2+(z1-z2)**2)**.5
    
def meanD(f1,f2):
    sum1=0
    counter=1
    for x in range(len(f1)/3):
        minD=999
        for y in range(len(f2)/3):
            #print 'hello'
            if(d(f1[3*x],f1[3*x+1],f1[3*x+2],f2[3*y],f2[3*y+1],f2[3*y+2])<minD):
                minD=d(f1[3*x],f1[3*x+1],f1[3*x+2],f2[3*y],f2[3*y+1],f2[3*y+2])
            sum1+=minD
            #print minD
        counter+=1
    if(counter!=0):
        return sum1/counter
    else:
        
        return 1000

def clusterFibers(similarityMatrix, threshold = 0.1, k=2):
    '''
    points is an array of points
    indexI=0
    indexJ=0
    for value in similarityMatrix:
        print value
        if (value <= currentMin):
            currentMin = value

    if (min(similarityMatrix) < threshold):
        for 
'''
    
def genSimilarityMatrix(fibers):
    clusterMatrix=[[0 for x in range(len(fibers))] for y in range(len(fibers)) ]
    for i in range(len(fibers)):
        for j in range(len(fibers)):
            if(i==j):
                clusterMatrix[i][j]=0
            else:
                clusterMatrix[i][j]=meanD(fibers[i],fibers[j])
    print clusterMatrix
    return clusterMatrix

def readInOurFileProperly():
    f1=open('data05.txt','r')
    f2=open('data04.txt','r')
    f3=open('data03.txt','r')
    fiber1=f1.read()
    fiber2=f2.read()
    fiber3=f3.read()
    aDirty = fiber1.split(',')
    bDirty = fiber2.split(',')
    cDirty = fiber3.split(',')
    
    a = [0 for x in range(3*len(aDirty))]  
    b = [0 for x in range(3*len(bDirty))]  
    c = [0 for x in range(3*len(cDirty))]   
    for j in range(len(aDirty)):
        i = 0
        for element in aDirty[j].split():
            a[3*j+i] = int(element)
            i+=1

    for j in range(len(bDirty)):
        i = 0
        for element in bDirty[j].split():
            b[3*j+i] = int(element)
            i+=1

    for j in range(len(cDirty)):
        i = 0
        for element in cDirty[j].split():
            c[3*j+i] = int(element)
            i+=1

    #a = [int(y) for y in aDirty]
    #b = [int(z) for z in bDirty]
    #a = aDirty.replace("\'", "")
    #b = bDirty.replace("\'", "")
    print a
    print b
    print c
    #[x.strip() for x in fiber1.split(',')]
    #[y.strip() for y in fiber2.split(',')]
    
    fibers = (a, b, c)

    return fibers

def main():
    #fibers = readInOurFileProperly()
    #genSimilarityMatrix(fibers)
    testMatrix = [[1, 2],[3, 4]]
    rowNum = 0
    for value in testMatrix:
        #rowNum++
        for element in value:
            print element


if __name__ == "__main__":

    main()