# commonly required basic operations for matrices

from numpy import array
from numpy import zeros

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
def transpose(a):
	if not check_1D(a):
		return a.T
	else:
		pShape = [a.shape[0],1]
		p = zeros(pShape)
		for i in xrange(0,pShape[0]):
			p[i][0] = a[i]
		return p

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
def matrix_print(a):
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

# check if 1D array
def check_1D(a):
	try:
		a.shape[1]
		return False
	except IndexError:
		return True
# augmented matrix
def augmented_matrix(a,b):
	pShape = [0,0]
	if a.shape[0] == b.shape[0]:
		pShape[0] = a.shape[0]
		pShape[1] = a.shape[1] + b.shape[1]
		p = zeros(pShape)
		for i in xrange(0,a.shape[0]):
			for j in xrange(0,a.shape[1]):
				p[i][j] = a[i][j]

		for i in xrange(0,a.shape[0]):
			for j in xrange(0,b.shape[1]):
				p[i][j+a.shape[1]] = b[i][j]
		return p
	else:
		print 'check dimensions of the input arrays'

# swapping rows
def swap_rows(a,i,j):
	n = a.shape[1]
	for k in xrange(n):
		temp = a[i][k]
		a[i][k] = a[j][k]
		a[j][k] = temp
	return a

def testing_function(a,b):
	if a==b:
		print 'Passed _/'
	else:
		print 'Failed X'

def test_all():
	A = array([[1,2],[3,4]])
	B = array([[1,3],[5,7]])
	C = array([[11,17],[23,37]])
	D = array([[1,2],[3,4],[5,6]])
	E = array([1,2,3,4])

test_all()