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
	return combin(row,entry)

def triangle(rows):
	'''Prints out Pascal's Triangle'''
	for i in range(rows+1):
		for j in range(i+1):
			print (int(pascal(i,j)),end= ' ')
		print()

##triangle(10)

'''Added Sept 4, 2018: Finding out the probability of
19 or more successful coin flips out of 25, to test if the
Patriots were cheating in their streak'''

def row_greater_than(row,num):
        output = 0
        for i in range(num,row+1):
                output += pascal(row,i)
        return output

