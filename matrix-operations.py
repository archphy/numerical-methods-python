# commonly required basic operations for matrices

from numpy import matrix

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

# matrix equality
def matrix_equality(a,b):
	c = (a==b)
	for k in c:
		for j in k:
			if not j:
				return False
	return True

# print matrix elements without '['
def matrix_print():
	pass

# infinity norm of the matrix
def infinity_norm(a):
	pass

# euclidean norm of the matrix
def euclidean_norm(a):
	pass

# L1 norm of the matrix
def l1_norm(a):
	pass

# check if matrix is upper triangular
def check_upper_triangular(a):
	pass

# augmented matrix
def augmented_matrix(a,b):
	pass


def testing_function(a,b):
	if a==b:
		print 'Passed _/'
	else:
		print 'Failed X'

def test_all():
	# a = array([[1,2],[3,4]])
	# b = array([[1,3],[5,7]])
	# c = array([[11,17],[23,37]])
	# d = array([[11,17],[23,37]])
	# print 'Testing: matrix_equality ->', testing_function(matrix_equality(c,d), True)
	# print 'Testing: matrix_equality ->', testing_function(matrix_equality(c,a), False)
	# print 'Testing: matrix_product ->', testing_function(matrix_equality(matrix_product(a, b), c), True)
	# a = array([[3,4,5,2], [4,2,7,9]])
	# a = a.transpose()
	# b = array([[1,2],[3,4]])
	# print b[0][0]
	# print b[0][1]
	# print b[1][0]
	# print b[1][1]
	A = matrix([[1,2],[3,4]])
	B = matrix([[1,3],[5,7]])
	C = matrix([[11,17],[23,37]])
	print C
	print C.transpose()
	print A*B
	# print 'Testing: matrix_product ->', testing_function(matrix_equality(matrix_product(A, B), C), True)
	# print A*B==C

test_all()