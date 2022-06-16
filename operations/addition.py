from utils.functions import *


#   OBJECTIVE
#   Perform addition arithmetic operations
#   without the aid of language's operators.

def add(num1=0, num2=0, *nums, binary=False):
	def recurse(result):
		if len(nums):
			for num in nums:
				result = add(result, num if not binary else int(num or '0', 2))
		return result

	if (not num1) or type(num1) == list:
		if len(nums):
			num1 = nums[ 0 ]
			nums = nums[ 1: ]
		else:
			num1 = '0' if binary else 0
	if not num2:
		if len(nums):
			num2 = nums[ 0 ]
			nums = nums[ 1: ]
		else:
			num2 = '0' if binary else 0

	signage = list()

	if int(num1) < 0:
		signage.append('num1')
		num1 = int(str(num1)[ 1: ])
	if int(num2) < 0:
		signage.append('num2')
		num2 = int(str(num2)[ 1: ])

	if len(signage) == 1:
		from operations.subtraction import subtract

		if 'num1' in signage:
			return recurse(subtract(num2, num1))
		elif 'num2' in signage:
			return recurse(subtract(num1, num2))

	# binarise digits
	num1_binary, num2_binary = binarise_digits(num1, binary=binary).split(), binarise_digits(num2, binary=binary).split()

	padd_array(num1_binary, num2_binary, '0')

	# find longest place value digit
	max_binary_len = resolve_max_binary_len(num1_binary, num2_binary)
	denary_result = ''

	for i in range(max_binary_len - 1, -1, -1):
		val1, val2 = num1_binary[ i ], num2_binary[ i ]
		carry_over_index = i - 1

		if val1:
			val1 = val1.lstrip('0')
		if val2:
			val2 = val2.lstrip('0')

		val_len = 0
		if val1:
			val_len = len(val1)
		if val2 and len(val2) > val_len:
			val_len = len(val2)

		val1 = str(val1)
		val2 = str(val2)

		while val_len > len(val1) or val_len > len(val2):
			if val_len > len(val1):
				val1 = f'0{val1}'
			if val_len > len(val2):
				val2 = f'0{val2}'

		result, remainder = '', '0'
		for x in range(val_len - 1, -1, -1):
			i, j = val1[ x ], val2[ x ]

			if i == '1' and j == '1':
				res = 0
				if remainder == '0':
					res = '0'
				else:
					res = '1'
				result = f'{res}{result}'
				remainder = '1'
			elif (i == '0' and j == '1') or (i == '1' and j == '0'):
				res = 0
				if remainder == '1':
					res = '0'
				else:
					res = '1'
				result = f'{res}{result}'
			elif i == '0' and j == '0':
				res = 0
				if remainder == '1':
					res = '1'
					remainder = '0'
				else:
					res = '0'
				result = f'{res}{result}'

		if remainder == '1':
			result = f'1{result}'

		dena_result = str(int(result or '0', 2))
		if len(dena_result) == 2:
			if (carry_over_index < 0):
				pass
			else:
				try:
					if num1_binary[ carry_over_index ]:
						num1_binary[ carry_over_index ] = inc_bin(num1_binary[ carry_over_index ])
				except IndexError:
					try:
						if num2_binary[ carry_over_index ]:
							num2_binary[ carry_over_index ] = inc_bin(num2_binary[ carry_over_index ])
					except IndexError:
						pass
				dena_result = dena_result[ -1 ]

		denary_result = f'{dena_result}{denary_result}'

	if len(signage) == 2:
		denary_result = int(str(f'-{denary_result}'))

	denary_result = recurse(denary_result)

	if binary:
		# shallow signage fix
		if int(denary_result) < 0:
			denary_result = int(str(denary_result)[ 1: ])
		return bin(int(denary_result))[ 2: ]
	return denary_result
