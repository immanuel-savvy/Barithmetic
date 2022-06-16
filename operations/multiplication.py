from utils.functions import *
from operations.addition import add


#   OBJECTIVE
#   Perform multiplication arithmetic operations
#   without the aid of language's operators.

def multiply(num1=0, num2=0, *nums):
	if not num1:
		num1 = 0
	if not num2:
		num2 = 0

	signage = list()
	if num1 < 0:
		signage.append('num1')
		num1 = int(str(num1)[ 1: ])
	if num2 < 0:
		signage.append('num2')
		num2 = int(str(num2)[ 1: ])

	if num1 == 0 or num2 == 0:
		return 0

	# binarise digits
	num1_binary, num2_binary = binarise_digits(num1, True), binarise_digits(num2, True)

	addition_list = list()
	for n in num1_binary:
		if n == '0':
			addition_list.insert(0, '0' * len(num2_binary))
		else:
			push = ''
			for m in num2_binary:
				if m == '0':
					push = f'{push}0'
				elif m == '1':
					push = f'{push}1'
			addition_list.insert(0, push)

	for a in range(len(addition_list)):
		addition_list[ a ] = f'{addition_list[ a ]}{"0" * a}'

	result = add(*addition_list, binary=True)

	denary_result = int(result, 2)
	if len(signage) == 1:
		denary_result = int(f'-{denary_result}')

	if len(nums):
		for num in nums:
			denary_result = multiply(denary_result, num)

	return denary_result
