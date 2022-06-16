from utils.functions import *
from operations.subtraction import subtract


#   OBJECTIVE
#   Perform division arithmetic operations
#   without the aid of language's operators.

def divide(dividend, divisor, *nums):
	signage = list()

	if dividend < 0:
		signage.append('dividend')
		dividend = int(str(dividend)[ 1: ])
	if divisor < 0:
		signage.append('divisor')
		divisor = int(str(divisor)[ 1: ])

	if dividend == 0 or divisor == 0:
		return 0
	if divisor == 1:
		return dividend if not len(signage) else int(f'-{str(dividend)}')

	# binarise digits
	dividend_binary, divisor_binary = binarise_digits(dividend, True), binarise_digits(divisor, True)

	quotient = ''

	# print(dividend_binary, divisor_binary)
	while True:
		if not dividend_binary:
			break
		if int(dividend_binary[ :len(divisor_binary) ] or '0') >= int(divisor_binary or '0'):
			remainder = subtract(dividend_binary[ :len(divisor_binary) ], divisor_binary, binary=True)
			quotient += '1'
			dividend_binary = f'{remainder if int(remainder) else ""}{dividend_binary[ len(divisor_binary): ]}'
			# print(dividend_binary, 'hh', remainder, quotient)
			if '1' in dividend_binary:
				dividend_binary = dividend_binary.lstrip('0')
			if dividend_binary and not int(dividend_binary):
				quotient += dividend_binary
				break
			elif not int(remainder) and '1' in dividend_binary:
				quotient += '0'
			elif dividend_binary[ :2 ] and int(remainder) and int(f'{remainder}{dividend_binary[ :1 ]}' or '0') < int(
					divisor_binary or
			                                                                                          '0'):
				quotient += '0'

		else:
			print('else here')
			break

	return int(quotient or '0', 2)
