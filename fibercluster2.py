comparisonMatrix[[0 for b in fibers] for a in fibers]

for i in range(fibers) :
	for j in range (fibers) :
		if (i=j) :
			pass
		else :
			# each fiber is a list of voxels (hopefully 'in order') 
			for (vi in i) :
				for (vj in j) :
					if (distance(vi,vj)<minDistance):
						minDistance=distance(vi,vj)
			comparisonMatrix[i][j] = minDistance

#post analysis
total = i^2;
totalSoFar = 0;
for (Iindex in range(i)) :
	for (Jindex in range(j)): 
		totalSoFar += comparisonMatrix[Iindex, Jindex]
average = totalSoFar / total
#calculate the average of all the entries in comparisonMatrix

# calculate threshold somehow, call it fiberThreshold (call it average for now)

clusterArray[b for b in range (fibers)]

for (Iindex in i) :
	for (Jindex in j): 
		#comparisonPoint2 = comparisonMatrix[Iindex, Jindex]
		if (comparisonMatrix[i,j] > average/2) 
			comparisonMatrix[i,j] = 