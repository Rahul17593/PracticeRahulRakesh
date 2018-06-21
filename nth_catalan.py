# A dynamic programm based function to find nth 
#Catalan number

def catalan(n):
	if(n == 0 or n == 1):
		return 1
     
    # table to store result of subproblem
	catalan =[0 for i in range(n+1)]

    #initialize first two value.
	catalan[0] = 1 
	catalan[1] = 1

	# call the recursive rules
	for i in range(2, n+1):
		catalan[i] = 0
		for j in range(i):
			catalan[i] = catalan[i] + catalan[j] * catalan[i-j-1]
    
    #return the result
	return catalan[n]


for i in range(11):
	print(catalan(i))
			