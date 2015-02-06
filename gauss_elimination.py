# algorithm#1

from numpy import array
from numpy import zeros
import matrix_operations as mo
# row scaling of the matrix
def row_scaling(a,take_abs=True):
	n = a.shape[0]
	max_row = 0
	for i in xrange(0,a.shape[0]):
		for j in xrange(0,n):
			if take_abs and max_row < abs(a[i][j]):
				max_row = abs(a[i][j])
			elif not take_abs and abs(max_row) < abs(a[i][j]):
				max_row = a[i][j]
		if max_row != 0:
			for j in xrange(0,a.shape[1]):
				a[i][j] /= max_row
			max_row = 0
	return a

# partial pivoting, only row
def partial_pivoting(a):
	pass

# transformation to row-echleon form
def transform_to_row_echleon(a):
	n = a.shape[0]
	for i in xrange(0,n-1):
		for j in xrange(i+1,n):
			factor = a[j][i]/a[i][i]
			for k in xrange(0,n+1):
				a[j][k] -= factor*a[i][k]
	return a

# backward substitution
def backward_substitution(a):
	# currently supports only (n x n+1) matrix
	n = a.shape[0]
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
	
	return mo.transpose(p)

# inverse
def inverse(a):
	pass

# solve a set of equation
def solve(a,b):
	print "Coefficients:\n", a
	print "Values:\n", b
	p = mo.augmented_matrix(a,b)
	print 'Augmented:\n', p
	p = row_scaling(p)
	print 'Row scaled:\n', p
	# p = partial_pivoting(p)
	# print "Partially pivoted:\n", p
	p = transform_to_row_echleon(p)
	print 'Transformed to Row-echleon form:\n', p
	q = backward_substitution(p)
	print "On backward substitution:\n", q

# test
# A = array([[2,3,-1],[4,4,-3],[-2,1,-1]])
# B = mo.transpose(array([5,3,-3]))
# A = array([[4,1],[1,3]])
# B = mo.transpose(array([1,2]))
# solve(A,B)