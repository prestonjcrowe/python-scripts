# Provides functions to calculate Riemann's sums using either the 
# midpoint, trapezoidal, or Simpson's rule. Each function accepts
# a lower bound [a], upper bound [b], number of intervals [n], as
# well as a constant to be multiplied with the final value [const]
# Define the function you'd like to find a Riemann's sum for in
# myFunc(x) and then call the respective sum function
# (if no constant multiple, pass 1)

import math

def myFunc(x):	
	return (math.sqrt(1+(9*x)**4))

# midpoint
def midpt(a, b, n, const):
	dx = (b-a)/float(n)
	sumterms = 0
	for i in range(n):
		print(a+(1+i)*dx-(dx/2))
		sumterms += myFunc(a+(1+i)*dx-(dx/2)) #midpt
	
	print("sumterms " + str(sumterms))
	sumterms *= dx
	sumterms *= const
	print("final answer " + str(sumterms))

# simpon's
# ONLY WORKS IF N IS EVEN!
def simpson(a, b, n, const):
	dx = (b-a)/float(n)  
	sumterms = 0
	print('const: ' + str(const))
	for i in range(n+1):
		inp = a+i*dx
		print(str(inp) + ' ' + str(myFunc(inp)))
		if(inp == a or inp == b): 			    #if term is first
			print("endpt: " + str(a+i*dx))
			print("*1")	
			sumterms += myFunc(inp)
		elif i % 2 != 0:
			print("*4")				
			sumterms += 4*myFunc(inp)	   #if term has odd index
		else:
			print("*2")
			sumterms += 2*myFunc(inp)     #if term has even index 

	sumterms *= dx
	sumterms *= (1/float(3)) 
	sumterms *= const
	print("final answer " + str(sumterms))

# trapezoidal
def trap(a, b, n, const):
	dx = (b-a)/float(n)
	sumterms = 0
	for i in range(n+1):
		inp = a+i*dx
		print(inp)
		if(inp == a or inp == b):
			print("endpt: " + str(a+i*dx))
			sumterms += myFunc(inp)
		else:
			sumterms += 2*myFunc(inp)

	sumterms *= dx
	sumterms *= .5
	sumterms *= const
	print("final answer " + str(sumterms))

simpson(0, 1, 6, 1)

