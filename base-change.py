numerals = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, \
			'A', 'B', 'C', 'D', 'E', 'F', 'G',\
			'H', 'I', 'J', 'K', 'L', 'M', 'N',\
			'O', 'P', 'Q', 'R', 'S', 'T', 'U',\
			'V', 'W', 'X', 'Y' ,'Z']

def map_digits(dig):
	return numerals[dig]

def unmap_digits(dig):
	if ord(dig) >= 48 and ord(dig) <= 57: # numeral
		dig = int(dig)
	elif ord(dig) >= 97 and ord(dig) <= 122: # lowercase alphabet
		# convert to uppercase
	
	if ord(dig) >= 65 and ord(dig) <= 90 # uppercase alphabet
		return numerals.index(dig)

def min_base(inputNum):
	base = 2
	inputNumLength = len(inputNum)
	for i in xrange(inputNumLength-1, -1, -1):
		minDigBase = unmap_digits(inputNum[i])
		if  (minDigBase+1) > base:
			base = minDigBase+1
	return base

def convert_to_decimal(inputNum, inputBase):
	inputNumLength = len(inputNum)
	outputNum = 0
	index = 0
	for i in xrange(inputNumLength-1, -1, -1):
		dig = unmap_digits( inputNum[i] )
		outputNum += dig * ( inputBase ** (inputNumLength - i - 1) )
	return outputNum

def convert_from_decimal(inputNum, outputBase):
	num = inputNum
	outputNum = ''
	while num > 0:
		dig = num % outputBase
		dig = map_digits(dig)
		num /= outputBase
		outputNum = str(dig) + outputNum
	return outputNum
		
def base_change(inputNum, inputBase, outputBase):
	ans = convert_from_decimal( convert_to_decimal(inputNum, inputBase), outputBase)
	return ans

def test_all():
	print '=====Testing map_digits====='
	print 'map the digit:0 ->', map_digits(0)
	print 'map the digit:9 ->', map_digits(9)
	print 'map the digit:10 ->', map_digits(10)
	print 'map the digit:15 ->', map_digits(15)
	print 'map the digit:35 ->', map_digits(35)
	print '=========='
	print '=====Testing unmap_digits====='
	print 'unmap the digit 0 <-', unmap_digits('0')
	print 'unmap the digit 7 <-', unmap_digits('7')
	print 'unmap the digit 9 <-', unmap_digits('9')
	print 'unmap the digit A <-', unmap_digits('A')
	print 'unmap the digit B <-', unmap_digits('B')
	print 'unmap the digit F <-', unmap_digits('F')
	print 'unmap the digit Z <-', unmap_digits('Z')
	print '=========='
	print '=====Testing convert_to_decimal====='
	print '7B in base-16:', convert_to_decimal('7B', 16)
	print '12 in base-3:', convert_to_decimal('12', 3)
	print '11 in base-2:', convert_to_decimal('11', 2)
	print '=========='
	print '=====Testing convert_from_decimal====='
	print '123 to base-16:', convert_from_decimal(123, 16)
	print '5 to base-3:', convert_from_decimal(5, 3)
	print '3 to base-2:', convert_from_decimal(3, 4)
	print '=========='
	print '=====Testing base_change====='
	print '10 from base-2 to base-10:', base_change('10', 2, 10)
	print '7B from base-16 to base-10:', base_change('7B', 16, 10)
	print '=========='
	print '=====Testing min_base====='
	print 'min_base of 1010:', min_base('1010')
	print 'min_base of 13SFR:', min_base('13SFR')
	print 'min_base of 13SFZ:', min_base('13SFZ')
	print '=========='
	
# test_all()

#check if integer
def isInt(num):
	try:
		int(num)
		return True
	except ValueError:
		return False

def accept_inputNum():
	global inputNum
	inputNum = raw_input('Enter the number to be converted: ')
	while not isInt(inputNum):
		print 'The number should be an integer'
		inputNum = raw_input('Enter the number to be converted: ')

def accept_inputBase():
	global inputBase
	inputBase = int(raw_input('Enter the base of the input: '))
	minInputBase = min_base(inputNum)
	while (inputBase < minInputBase or inputBase > 36) \
		or not isInt(inputBase):
		print 'The base should range from', minInputBase, 'to 36 and should be an integer'
		inputBase = int(raw_input('Enter the base of the input: '))

def accept_outputBase():
	global outputBase, inputBase
	outputBase = int(raw_input('Enter the desired base of the output: '))
	while (outputBase < 2 or outputBase > 36) \
		or not isInt(outputBase) \
		or inputBase == outputBase:
		print 'The base should range from 2 to 36, should be an integer and should be different from input-base'
		outputBase = int(raw_input('Enter the base of the input: '))

def accept_inputs():
	accept_inputNum()
	accept_inputBase()
	accept_outputBase()

def execute_base_change():
	print '----------'
	print 'You wanted', inputNum, 'of base:', inputBase, 'to be converted to base:', outputBase
	print 'Answer: ', base_change(inputNum, inputBase, outputBase)

accept_inputs()
execute_base_change()