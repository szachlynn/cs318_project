# possibly can do this better with dynamic programming

mindc = 100
for i in range(fibers) :
	for j in range (fibers) :
		if (i=j) :
			pass
		else :
			# each fiber is a list of voxels (hopefully 'in order') 
			for (voxel in i) :
				calculate mindistance to j
				#so maybe what this does is that it gives you a measure of
				# how close other fibers are to this 1 fiber.
				# lacks global picture i.e., doesn't care the relationship
				# between other fibers and other fibers

				# find min distance to other fibers,
				# store all distances in SUMdistance2fibers (distance to fiber)
				
				# set threshhold for :
				# average mindistance
			# calculate average

	# perform some sort of analysis of bundle ideas and assign each fiber to 
	# at most 1 bundle



	#post analysis to determine actual bundling
	#		# Jicard similarity maybe  intersection/union
	#		# emasure of common neighbors
	#