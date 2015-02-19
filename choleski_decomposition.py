# algorithm#3.3
# Assignment #3
# tasks left:
# 1. check for symmetry 				done
# 2. check for NxN						done
# 3. minimize storage
# 4. bring all functions in one program	done
# 5. check for positive definite 		done
# 6. solve a test case 					done
# 7. document and submit
# 8. input array from terminal			done
# 9. minimize the number of inputs 		done
# 10. validation for gibberish input

import time
from numpy import array
from numpy import zeros
from numpy import identity
from numpy import arange
from numpy import dot
from math import sqrt

start_time = time.time()

def transpose(a):
	if not check_1D(a):
		return a.T
	else:
		pShape = [a.shape[0],1]
		p = zeros(pShape)
		for i in xrange(pShape[0]):
			p[i][0] = a[i]
		return p

def augmented_matrix(a,b):
	pShape = [0,0]
	if a.shape[0] == b.shape[0]:
		pShape[0] = a.shape[0]
		pShape[1] = a.shape[1] + b.shape[1]
		p = zeros(pShape)
		for i in xrange(a.shape[0]):
			for j in xrange(a.shape[1]):
				p[i][j] = a[i][j]

		for i in xrange(a.shape[0]):
			for j in xrange(b.shape[1]):
				p[i][j+a.shape[1]] = b[i][j]
		return p
	else:
		print 'check dimensions of the input arrays'

def check_1D(a):
	try:
		a.shape[1]
		return False
	except IndexError:
		return True

def matrix_equality(a,b):
	c = (a==b)
	for k in c:
		for j in k:
			if not j:
				return False
	return True

def check_positive_definite(a):
	global n
	X = arange(n)
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

def backward_substitution(a):
	# currently supports only (n x n+1) matrix
	global n
	p = zeros(n)
	sum_of_others = 0

	# last variable
	p[-1] = a[-1][-1] / a[-1][-2];
	
	# other variables
	for i in xrange(n-2,-1,-1):
		for j in xrange(n-1,i,-1):
			sum_of_others += a[i][j]*p[j]
		
		p[i] = (a[i][n] - sum_of_others) / a[i][i]
		sum_of_others = 0
	
	return transpose(p)

def choleski_decomposition():
	global A,B,n
	l = identity(n)
	sum_1 = 0
	sum_2 = 0
	for i in xrange(n):
		for j in xrange(i):
			for k in xrange(j):
				sum_1 += l[j][k]*l[i][k]
			l[i][j] = (A[i][j] - sum_1) / l[j][j]
		
		for k in xrange(i):
			sum_2 += l[i][k]*l[i][k]
		
		l[i][i] = sqrt(A[i][i] - sum_2)
		sum_1 = 0
		sum_2 = 0
	
	return l

def solve():
	global A,B
	if not check_positive_definite(A):
		print 'A matrix must be positive definite'
	else:
		l = choleski_decomposition()
		u = transpose(l)
		y = forward_substitution(l,B)
		s = backward_substitution(augmented_matrix(u,y))
		print s
		# print 'Lower triangular matrix:\n', l
		# print 'Upper triangular matrix:\n', u
		# print 'On forward substitution:\n', y
		# print u.shape, y.shape, b.shape
		# print 'On backward substitution:\n', s

def accept_coefficients():
	global A
	global n
	n = input('Enter the number of variables(n): ')
	A = zeros((n,n))
	for x in xrange(n):
		for y in xrange(x,n):
			A[x][y] = input('Enter the value for A[%d][%d]: ' % (x+1,y+1))
		
		for y in xrange(x):
			A[x][y] = A[y][x]

def accept_values():
	global B
	B = zeros((n,1))
	for x in xrange(n):
		B[x][0] = input('Enter the value for B[%d][%d]: ' % (x+1,1))


def accept_inputs():
	# accept_coefficients()
	# accept_values()
	# print 'Number of variables:', n
	# print 'A matrix\n', A
	# print 'B matrix\n', B
	global A,B,n
	A = array([[1.44,-0.36,5.52,0],[-0.36,10.33,-7.78,0],[5.52,-7.78,28.4,9],[0,0,9,61]], dtype="float")
	B = transpose(array([0.04,-2.15,0,0.88]))
	n = 4
	# print check_positive_definite(A)

accept_inputs()
solve()

# test
# solution: [3.0921,-0.7387,-0.8476,0.1395]
# solve(A,B)
# print 'Time taken: %.4f seconds' % (time.time() - start_time)
# from guppy import hpy
# h = hpy()
# print h.heap()