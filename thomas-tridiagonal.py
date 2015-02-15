# Algorithm # 10

from numpy import array
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
	pass

def solve(a,b):
	(l,u) = thomas_decomposition(a)
	print 'Lower triangular matrix:\n', l
	print 'Upper triangular matrix:\n', u
	# y = dd.forward_substitution(l,b)
	# print 'On forward substitution:\n', y
	# s = ge.backward_substitution(mo.augmented_matrix(u,y))
	# print 'On backward substitution:\n', s

# test
A = array([[3,-1,0,0],[2,-3,2,0],[0,1,2,5],[0,0,1,-1]])
B = mo.transpose(array([1,2,3,4]))
# solve(A,B)
print check_tridiagonal(A)