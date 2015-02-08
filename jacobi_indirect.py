from numpy import array
import matrix_operations as mo

def diagonally_dominant(a):
	n = a.shape[0]
	row_max = 0
	row_max_index = 0
	for i in xrange(n):
		for j in xrange(i,n):
			if row_max < abs(a[j][i]):
				row_max = abs(a[j][i])
				row_max_index = j
		a = mo.swap_rows(a, i, row_max_index)
	return a

def solve(a,b):
	p = diagonally_dominant(a)
	print 'Diagonally Dominant:\n', p

# test
A = array([[2,1,9],[8,1,-1],[1,-7,2]])
B = mo.transpose(array([5,3,-3]))
solve(A,B)
# A = array([[4,1],[1,3]])
# B = mo.transpose(array([1,2]))