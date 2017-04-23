# Sieve of Eratosthenes
# Fastest method of finding primes < 10,000,000
import math

n = 100
limit = int(math.sqrt(n))
vals = [t for t in range(2,n)]

def eliminate(s):
	numValues = len(vals)
	for i in range(0,numValues):
		if i >= len(vals):
			break

		elif vals[i] == s:
			pass

		elif vals[i] % s == 0:
			del vals[i]


for i in range(2,limit):
	eliminate(i)

for prime in vals:
	print prime

