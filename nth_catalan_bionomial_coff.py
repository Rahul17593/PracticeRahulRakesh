#Calculate the Bionomial Coefficient C(c,k)
def binomicial_cofficient(n,k):

    #since c(n,k) = c(n, n-k)
	if(k > n-k):
		k = n-k

	result = 1
	for i in range(k):
		result =result * (n-i)
		result = result / (i+1)

	return result

# findout the catalan number
def catalan(n):
	#call binomicial_cofficient function.
	c = binomicial_cofficient(2*n, n)
	return c/(n+1)
	
for i in range(11):
	print(catalan(i))