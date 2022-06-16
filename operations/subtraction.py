from utils.functions import *
from operations.addition import add


#   OBJECTIVE
#   Perform subtraction arithmetic operations
#   without the aid of language's operators.

def subtract(num1=0, num2=0, *nums, binary=False):
	if not num1:
		num1 = 0
	if not num2:
		num2 = 0

	if binary:
		num1 = int(str(num1), 2)
		num2 = int(str(num2), 2)
		if len(nums):
			new_nums = list()
			for num in nums:
				new_nums.append(int(num, 2))
			nums = tuple(new_nums)

	def recurse(result):
		if len(nums):
			for num in nums:
				result = subtract(result, num)
		if binary and '1' in str(result):
			result = str(result.lstrip('0'))
		return result

	signage = list()

	if num1 < 0:
		signage.append('num1')
		num1 = int(str(num1)[ 1: ])
	if num2 < 0:
		signage.append('num2')
		num2 = int(str(num2)[ 1: ])

	if num1 == 0 and num2 != 0:
		return recurse(num2)
	if num2 == 0 and num1 != 0:
		if 'num1' in signage:
			num1 = int(str(f'-{num1}'))
		return recurse(num1)

	if 'num1' in signage and 'num2' not in signage:
		return recurse(int(f'-{add(num1, num2)}'))
	if 'num2' in signage and 'num1' not in signage:
		return recurse(add(num1, num2))
	if len(signage) == 2:
		return subtract(num2, num1, *nums)

	flip = False
	if num1 < num2:
		num1, num2 = num2, num1
		flip = True
	elif num1 == num2:
		return recurse(0)

	# binarise digits
	num1_binary, num2_binary = binarise_digits(num1, True), binarise_digits(num2, True)

	# find longest place value digit
	max_binary_len = resolve_max_binary_len(num1_binary, num2_binary)
	result = ''

	if len(num1_binary) != len(num2_binary):
		temp1 = num1_binary
		temp2 = num2_binary
		num1_binary = padd_string(num1_binary, temp2, '0', True)
		num2_binary = padd_string(num2_binary, temp1, '0', True)

	num1_binary, num2_binary = string_to_list(num1_binary), string_to_list(num2_binary)

	for x in range(max_binary_len - 1, -1, -1):
		i, j = num1_binary[ x ], num2_binary[ x ]

		if (i == '1' and j == '1') or (i == '0' and j == '0'):
			res = '0'
			result = f'{res}{result}'
		elif (i == '0' and j == '1'):
			for k in range(x - 1, -1, -1):
				if num1_binary[ k ] == '1':
					num1_binary[ k ] = '0'
					for l in range(k + 1, x):
						num1_binary[ l ] = '1'
					break
			res = '1'
			result = f'{res}{result}'
		elif i == '1' and j == '0':
			res = '1'
			result = f'{res}{result}'

	if binary:
		return recurse(result)

	denary_result = int(result or '0', 2)
	if denary_result and flip:
		denary_result = int(f'-{denary_result}')

	return recurse(denary_result)
