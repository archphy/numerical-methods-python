# algorithm#3.1

import matrix_operations as mo
import gauss_elimination as ge
from numpy import array
from numpy import zeros

# forward substitution
def forward_substitution(a,b):
	x = zeros(b.shape)
	x[0] = b[0]/a[0][0]
	sum_of_others = 0
	for i in xrange(1,b.shape[0]):
		for j in xrange(0,i):
			sum_of_others += a[i][j]*x[j]
		x[i] = (b[i] - sum_of_others) / a[i][i]
		sum_of_others = 0
	return x

def solve(a,b):
	(l,u) = ge.transform_to_row_echleon(a, True)
	print 'Lower triangular matrix:\n', l
	print 'Upper triangular matrix:\n', u
	y = forward_substitution(l,b)
	print 'On forward substitution:\n', y
	s = ge.backward_substitution(mo.augmented_matrix(u,y))
	print 'On backward substitution:\n', s

# test
# A = array([[4,1],[1,3]], dtype='float')
# B = mo.transpose(array([1,2]))
# solve(A,B)
# A = array([[2,3,-1],[4,4,-3],[-2,1,-1]])
# B = mo.transpose(array([5,3,-3]))
# solve(A,B)