#Trapping Rain Water problem

def findwater(arr, n):

	result = 0
	left_max = 0
	right_max = 0

	lowest = 0
	height = n-1

	while (lowest <= height):
		if(arr[lowest] < arr[height]):
			if (arr[lowest] > left_max):
				left_max = arr[lowest]

			else:
				result += left_max - arr[lowest]
				lowest += 1
		else:

			if(arr[height] > right_max):
				right_max = arr[height]

			else:
				result += right_max - arr[height]
				height -= 1

	return result

   


arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

n = len(arr)
print "maximum water that can be accumulated id", findwater(arr, n)
				
		
