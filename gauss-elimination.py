# algorithm#1

from numpy import array
import matrix_operations as mo
# row scaling of the matrix
def row_scaling(a):
	pass

# partial pivoting, only row
def partial_pivoting(a):
	pass

# transformation to row-echleon form
def transform_to_row_echleon(a):
	pass

# backward substitution
def backward_substitution():
	pass

# inverse
def inverse(a):
	pass

# solve a set of equation
def solve(a,b):
	p = mo.augmented_matrix(a,b)
	print 'Augmented:\n', p
	# p = transform_to_row_echleon(p)
	# print p

# test
A = array([[2,3,-1],[4,4,-3],[-2,1,-1]])
B = mo.transpose(array([5,3,-3]))
solve(A,B)
# print B