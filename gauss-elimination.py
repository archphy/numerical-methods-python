# algorithm#1

from numpy import array
import matrix_operations as mo
# row scaling of the matrix
def row_scaling(a):
	n = a.shape[0]
	max_row = 0
	for i in xrange(0,a.shape[0]):
		for j in xrange(0,n):
			if max_row < abs(a[i][j]):
				max_row = abs(a[i][j])
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
		# print i, ':'
		for j in xrange(i+1,n):
			factor = a[j][i]/a[i][i]
			# print factor
			for k in xrange(0,n+1):
				a[j][k] -= factor*a[i][k]
	return a

# backward substitution
def backward_substitution(a):
	pass

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
A = array([[2,3,-1],[4,4,-3],[-2,1,-1]])
B = mo.transpose(array([5,3,-3]))
solve(A,B)
# print B