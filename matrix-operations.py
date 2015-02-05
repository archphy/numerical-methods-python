from numpy import *
# matrix multiplication
def matrix_product(a, b):
	return a*b

# matrix addition
def matrix_sum(a,b):
	return a+b

# matrix subtraction
def matrix_diff(a,b):
	return a-b

# matrix transpose
def matrix_transpose(a):
	return a.T

# matrix check symmetry
def matrix_check_symmetry(a):
	return a == a.T

# matrix check positive_definite
def matrix_check_positive_definite(a):
	pass

# matrix check diagonally_dominant
def matrix_check_diagonally_dominant(a):
	pass

# matrix check orthogonal
def matrix_check_orthogonal(a):
	pass

# matrix check singular
def matrix_check_singular(a):
	pass

def test_all():
	# a = array([[3,4,5,2], [4,2,7,9]])
	# a = a.transpose()
	# print a
	A = matrix('1 2;3 4')
	B = matrix('1 3;2 4')
	print A.T == B
	pass

test_all()