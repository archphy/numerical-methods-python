from numpy import matrix

# row scaling of the matrix
def row_scaling(a):
	pass

# partial pivoting, only row
def partial_pivoting(a):
	pass

# transformation to row-echleon form
def transform_to_row_echleon():
	pass

# backward substitution
def backward_substitution():
	pass

# inverse
def inverse(a):
	pass

# solve a set of equation
def solve(a,b):
	pass

# test
A = matrix([[2,3,-1],[4,4,-3],[-2,1,-1]])
B = matrix([5,3,-3]).transpose()
solve(A,B)