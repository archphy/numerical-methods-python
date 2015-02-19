from numpy import array # array objects
from numpy import zeros # null arrays
from numpy import arange # arrays with serialized elements
from numpy import dot # dot product of arrays
from math import sqrt # square root function

def transpose(a):
	if not check_1D(a):
		return a.T # use inbuilt function for 1D arrays
	else:
		pShape = [a.shape[0],1]
		p = zeros(pShape)
		for i in xrange(pShape[0]):
			p[i][0] = a[i]
		return p

def check_1D(a):
	try:
		a.shape[1] # throws IndexError if the array is 1D
		return False
	except IndexError:
		return True

def matrix_equality(a,b): # compares to arrays element-wise
	c = (a==b)
	for k in c:
		for j in k:
			if not j:
				return False
	return True

def check_positive_definite(a):
	global n
	X = arange(n) # 1D array with elements as 0,1,2....(n-1)
	Y = dot(dot(X,a),transpose(X)) > 0
	return Y[0]

def forward_substitution(a,b):
	global n
	x = zeros((n,1))
	x[0][0] = b[0][0]/a[0][0]
	sum_of_others = 0
	for i in xrange(1,b.shape[0]):
		for j in xrange(i):
			sum_of_others += a[i][j]*x[j]
		x[i][0] = (b[i][0] - sum_of_others) / a[i][i]
		sum_of_others = 0
	return x

def backward_substitution(a,b):
	global n
	p = zeros(n)
	sum_of_others = 0
	p[-1] = b[-1][-1] / a[-1][-1];
	for i in xrange(n-2,-1,-1):
		for j in xrange(n-1,i,-1):
			sum_of_others += a[i][j]*p[j]
		
		p[i] = (b[i][0] - sum_of_others) / a[i][i]
		sum_of_others = 0	
	return transpose(p)

def choleski_decomposition():
	global A,B,n
	sum_1 = 0
	sum_2 = 0
	for i in xrange(n):
		for j in xrange(i):
			for k in xrange(j):
				sum_1 += A[j][k]*A[i][k]
			A[i][j] = (A[i][j] - sum_1) / A[j][j]
			A[j][i] = A[i][j]
		
		for j in xrange(i):
			sum_2 += A[i][j]*A[i][j]
		
		A[i][i] = sqrt(A[i][i] - sum_2)
		sum_1 = sum_2 = 0

def solve():
	global A,B
	if not check_positive_definite(A):
		print 'A matrix must be positive definite'
		accept_inputs()
	else:
		choleski_decomposition()
		y = forward_substitution(A,B)
		s = backward_substitution(A,y)
		print 'Solution matrix:\n', s

def accept_coefficients():
	global A
	global n
	n = input('Enter the number of variables(n): ')
	A = zeros((n,n))
	print 'Enter the value for:'
	# ensures that A matrix is symmetric and reduces number of inputs required
	for x in xrange(n):
		for y in xrange(x,n):
			A[x][y] = input('A[%d][%d]: ' % (x+1,y+1))
		
		for y in xrange(x):
			A[x][y] = A[y][x]

def accept_values():
	global B
	B = zeros((n,1))
	print 'Enter the value for:'
	for x in xrange(n):
		B[x][0] = input('B[%d][%d]: ' % (x+1,1))

def accept_inputs():
	accept_coefficients()
	accept_values()
	print 'Number of variables:', n
	print 'A matrix\n', A
	print 'B matrix\n', B
	solve()

accept_inputs()