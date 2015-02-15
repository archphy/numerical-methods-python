# Algorithm # 10

from numpy import array
from numpy import zeros
import matrix_operations as mo
import gauss_elimination as ge
import dolittle_decomposition as dd

def check_tridiagonal(a):
	n = a.shape[0]
	for i in xrange(n):
		for j in xrange(n):
			if (j == i or j == (i+1) or j == (i-1)):
				pass
			elif a[i][j] != 0:
				return False
	return True


def thomas_decomposition(a):
	n = a.shape[0]
	l = zeros(a.shape)
	u = zeros(a.shape)
	for k in xrange(1,n):
		a[k][k-1] = a[k][k-1]/a[k-1][k-1]
		a[k][k] = a[k][k] - a[k][k-1]*a[k-1][k]
	
	for i in xrange(n):
		l[i][i] = 1
		if i > 0:
			l[i][i-1] = a[i][i-1]
		u[i][i] = a[i][i]
		if i<n-1:
			u[i][i+1] = a[i][i+1]
	
	return (l,u)

def solve(a,b):
	if check_tridiagonal(a):
		(l,u) = thomas_decomposition(a)
	print 'Lower triangular matrix:\n', l
	print 'Upper triangular matrix:\n', u
	y = dd.forward_substitution(l,b)
	print 'On forward substitution:\n', y
	s = ge.backward_substitution(mo.augmented_matrix(u,y))
	print 'On backward substitution:\n', s

# test
# A = array([[3,-1,0,0],[2,-3,2,0],[0,1,2,5],[0,0,1,-1]], dtype='float')
# B = mo.transpose(array([1,2,3,4]))
# solve(A,B)