#To solve for row r and n entry in Pascal's Triangle

def factorial(x):
	'''Returns x!'''
	if x == 0: return 1
	return x*factorial(x-1)

def combin(r,k):
	'''Returns rCk'''
	return factorial(r)/(factorial(k)*factorial(r-k))

def pascal(row,entry):
	'''calculates the entry in Pascal's Triangle
	corresponding to a given row and entry'''
	return combin(row,entry-1)

def triangle(rows):
	'''Prints out Pascal's Triangle'''
	for i in range(rows+1):
		for j in range(1,i+2):
			print (int(pascal(i,j)),end= ' ')
		print()

triangle(10)
