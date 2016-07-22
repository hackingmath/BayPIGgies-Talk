from math import sqrt
import time

#primes = 2,3,5,7,11,13,17,19

t1 = time.time()

def prime(num):
	'''Returns True if num is prime'''
	for i in range(3,int(sqrt(num))+1,2):
		if num % i == 0:
			return False
	return True
	
def nthPrime(n):
	'''Retuns the nth Prime number'''
	primes = [2,3]
	runningNum = 3
	while len(primes) < n:
		runningNum += 2
		if prime(runningNum):
			primes.append(runningNum)
	return primes[-1]

print("prime = ",nthPrime(10000))
print(time.time() - t1)

