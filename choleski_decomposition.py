# algorithm#3.3

import gauss_elimination as ge
import matrix_operations as mo
import dolittle_decomposition as dd
from numpy import array
from numpy import identity
from math import sqrt

def choleski_deccomposition(a):
	n = a.shape[0]
	l = identity(n)
	sum_of_others_1 = 0
	sum_of_others_2 = 0
	for i in xrange(0,n):
		for j in xrange(0,i):
			for k in xrange(0,j):
				sum_of_others_1 += l[j][k]*l[i][k]
			l[i][j] = (a[i][j] - sum_of_others_1) / l[j][j]
		for k in xrange(0,i):
			sum_of_others_2 += l[i][k]
		l[i][i] = sqrt(abs(a[i][i] - sum_of_others_2))
		sum_of_others_1 = 0
		sum_of_others_2 = 0
	return l

def solve(a,b):
	l = choleski_deccomposition(a)
	u = mo.transpose(l)
	print 'Lower triangular matrix:\n', l
	print 'Upper triangular matrix:\n', u
	y = dd.forward_substitution(l,b)
	print 'On forward substitution:\n', y
	s = ge.backward_substitution(mo.augmented_matrix(u,y))
	print 'On backward substitution:\n', s

# test
# A = array([[4,1],[1,3]], dtype='float')
# B = mo.transpose(array([1,2]))
# solve(A,B)
# A = array([[2,3,-1],[4,4,-3],[-2,1,-1]])
A = array([[24,20,-12],[20,25,-16],[-12,-16,5]])
B = mo.transpose(array([5,3,-3]))
solve(A,B)