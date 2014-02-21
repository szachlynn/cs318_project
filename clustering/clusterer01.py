import math
#Calculates distance between two points. Takes x,y,z coordinates of each point as arguments
def d(x1,y1,z1,x2,y2,z2):

    #return ((x1-x2)**2+(y1-y2)**2+(z1-z2)**2)**.5
    intermediate = math.pow((x1-x2),2) + math.pow((y1-y2),2) + math.pow((z1-z2),2)
    return math.sqrt(intermediate)
#Calculates the mean minimum distance between 2 fibers. f1 and f2 are arrays
def meanD(f1,f2):
    #sum1 and counter are used to calculate the average
    sum1=0
    counter=0
    #for each point in f1
    for x in range(len(f1)/3):
        #set the minimum distance high
        minD=999
        #Loop through each point in f2
        for y in range(len(f2)/3):
            #if the distance between x in f1 and y in f2 is less than minD
            if(d(f1[3*x],f1[3*x+1],f1[3*x+2],f2[3*y],f2[3*y+1],f2[3*y+2]) < minD):
                #change the value of minD to that distance
                minD=d(f1[3*x],f1[3*x+1],f1[3*x+2],f2[3*y],f2[3*y+1],f2[3*y+2])
        #Add the minD for each point x to sum1
        sum1+=minD
        counter+=1
        print minD, "x, y = ", x, y
        #counter+=1
    #after finding the minD for each point in f1, the average is calculated and returned
    if(counter!=0):
        #print counter
        #print sum1
        return sum1/counter
    else:    
        return 1000

#This method takes an array of fibers as input. It returns a matrix with entries
#corresponding to the mean distance between pairs of fibers
def makeClusterMatrix(fibers):
    #empty square matrix with numRows equal to the number of fibers
    clusterMatrix=[[0 for x in range(len(fibers))] for y in range(len(fibers)) ]
    #for each pair of fibers, fill the corresponding entry in the matrix with something
    for i in range(len(fibers)):
        for j in range(len(fibers)):
            #if the fibers are the same, the distance between them is 0
            if(i==j):
                clusterMatrix[i][j]=0
            #if the fibers are different, fill the entry with the mean minimum distance
            else:
                clusterMatrix[i][j]=meanD(fibers[i],fibers[j])
    #print the similarity matrix
    print clusterMatrix
    return clusterMatrix
    
def agglomCluster(fibers, numClus=2, threshold=null):
    '''
    returns cluster assignments for input fibers
    and maybe cluster centroids
    '''
    assert(fibers!=null)
    clusterAssignments = [i for i in len(fibers)]
    if(len(fibers)>numCLus):
        stoppingCondition = -numClus + len(fibers)
        clusterMatrix=makeClusterMatrix(fibers)
        while (stoppingCondition>=0) :
            #find min value in ClusterMatrix
            currentMin, xCord, yCord = float("inf"), float("inf"), float("inf")
                for (y in len(clusterMatrix)):
                    for (x in len(clusterMatrix)):
                        if (currentMin>clusterMatrix[x][y] and clusterMatrix[x][y]!=0):
                            currentMin=clusterMatrix[x][y]
                            xCord, yCord = x, y
            #reduce ClusterMatrix   --    uses/involves calculation of mean matrix entries
            #update clusterAssignments
            newClusterMatrix = [[0 for i in range(len(clusterMatrix)-1)] for j in range(len(clusterMatrix)-1)]
            newRowColumn = [0 for i in range(len(clusterMatrix)-1)]
            
            if (xCord>yCord):
                z=xCord
                xCord=yCord
                yCord=z     #now we know that x is less than y
            decrementor=0
            
            for (i in range(len(newRowColumn))):
                if (i==xCord):
                    newRowColumn[i]=0
                elif (i==yCord):
                    dec-- #stands for decrementor
                else:
                    newRowColumn[i+dec] = (clusterMatrix[xCord][i]+clusterMatrix[yCord][i] ) / 2 #aka the average
            
            for (i in range(len(newRowColumn))):
                newClusterMatrix[xCord][i] = newRowColumn[i]
                newClusterMatrix[i][xCord] = newRowColumn[i]
            
            #fill in the rest
            for (y in range(len(newClusterMatrix))):
                for (x in range(len(newClusterMatrix))):
                    if ((x == xCord or yCord) or (y == xCord or yCord)):
                        pass
                    if (x < yCord and y < yCord):
                        newClusterMatrix[x][y]=clusterMatrix[x][y]
                    elif (x < yCord and y > yCord):
                        newClusterMatrix[x][y]=clusterMatrix[x][y+1]
                    elif (x > yCord and y < yCord):
                        newClusterMatrix[x][y]=clusterMatrix[x+1][y]
                    else:
                        newClusterMatrix[x][y]=clusterMatrix[x+1][y+1]                  
            clusterMatrix=newClusterMatrix
            stopingCondition--
    
    return clusterAssignments
    

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
    fibers = readInOurFileProperly()
    makeClusterMatrix(fibers)

if __name__ == "__main__":

    main()