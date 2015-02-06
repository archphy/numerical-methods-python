import gauss_elimination as ge
import matrix_operations as mo
from numpy import array
from numpy import zeros

# transform to identity matrix
def transform_to_identity(a):
	a = ge.transform_to_row_echleon(a)
	n = a.shape[0]
	for i in xrange(1,n):
		print i
		for j in xrange(0,i):
			factor = a[j][i]/a[i][i]
			for k in xrange(0,n+1):
				a[j][k] -= factor*a[i][k]
	a = ge.row_scaling(a, False)
	return a

# abstracting solution
def abstract_solution(a):
	n = a.shape[0]
	p = zeros(n)
	for i in xrange(0,n):
		p[i] = a[i,-1]
	return p

# solve a set of equation
def solve(a,b):
	print "Coefficients:\n", a
	print "Values:\n", b
	p = mo.augmented_matrix(a,b)
	print 'Augmented:\n', p
	p = ge.row_scaling(p)
	print 'Row scaled:\n', p
	# p = partial_pivoting(p)
	# print "Partially pivoted:\n", p
	p = transform_to_identity(p)
	print 'Transformed to identity form:\n', p
	q = ge.backward_substitution(p)
	print "On backward substitution:\n", q
	# q = abstract_solution(p)
	# print "On abstracting solution:\n", q

# test
A = array([[2,3,-1],[4,4,-3],[-2,1,-1]])
B = mo.transpose(array([5,3,-3]))
# A = array([[4,1],[1,3]])
# B = mo.transpose(array([1,2]))
solve(A,B)