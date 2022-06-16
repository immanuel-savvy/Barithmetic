import tkinter, sys, re
from operations import addition, multiplication, subtraction, division

_mul, _add, _sub, _div = 'MUL', 'ADD', 'SUB', 'DIV'


def ALU(string=''):
	"""
	12+2-3*9/3+(4+2)
	:param string:
	:return int:
	"""

	"""
		precedence
		()
		/ * + - 
	"""

	print(sys.argv);

	string = string.replace(' ', '')
	offset = False

	while True:
		try:
			index = string.index(')')
			if index or index == 0:
				if not '(' in string:
					string = string[ :-1 ]
					break

				sub_str_span = re.search('\(.*\)', string[ 0: index + 1 ]).span()

				sub_str = string[ sub_str_span[ 0 ] + 1: sub_str_span[ 1 ] - 1 ]
				if '(' in sub_str:
					sub_counts = sub_str.count('(')
					for i in range(sub_counts):
						if string[ sub_str_span[ 1 ] ] != ')':
							sub_str += ')'
							offset = True
						sub_str += string[
						           sub_str_span[ 1 ]:sub_str_span[ 1 ] + string[ sub_str_span[ 1 ] + 1: ].index(')') + 1 ]
						sub_str_span = (sub_str_span[ 0 ], sub_str_span[ 1 ] + string[ sub_str_span[ 1 ] + 1: ].index(')') + 1)
				if string[ sub_str_span[ 0 ] - 1 ] not in '*-+/':
					string = f'{string[ :sub_str_span[ 0 ] ]}*{string[ sub_str_span[ 0 ]: ]}'
					sub_str_span = (sub_str_span[ 0 ] + 1, sub_str_span[ 1 ] + 1)

				alu = ALU(sub_str)
				if int(alu) < 0:
					if string[ sub_str_span[ 0 ] - 1 ] == '-':
						alu = int(str(alu)[ 1: ])
						string = f'{string[ :sub_str_span[ 0 ] - 1 ]}+{string[ sub_str_span[ 0 ]: ]}'
					elif string[ sub_str_span[ 0 ] - 1 ] == '+':
						string = f'{string[ :sub_str_span[ 0 ] - 1 ]} {string[ sub_str_span[ 0 ]: ]}'

				string = f'{string[ :sub_str_span[ 0 ] ]}{alu}' \
				         f'{string[ sub_str_span[ 1 ] if not offset else sub_str_span[ 1 ] + 1: ]}'
		except ValueError:
			break
		string = string.replace(' ', '')

	precedence = [ '/', '*', '+', '-' ]
	operator_repl = { '/': _div, '*': _mul, '+': _add, '-': _sub }

	def resolve_operation(string):
		operators, result = operator_repl.values(), 0
		for operator in operators:
			if operator not in string:
				continue
			ints = string.split(operator)
			if operator == _div:
				result = division.divide(int(ints[ 0 ]), int(ints[ 1 ]))
			elif operator == _mul:
				result = multiplication.multiply(int(ints[ 0 ]), int(ints[ 1 ]))
			elif operator == _sub:
				result = subtraction.subtract(int(ints[ 0 ]), int(ints[ 1 ]))
			elif operator == _add:
				result = addition.add(int(ints[ 0 ]), int(ints[ 1 ]))
		return result

	for operator in precedence:
		temp_string = string.replace(operator, operator_repl[ operator ])
		while operator in string and not (string.count(operator) == 1 and string[ 0 ] ==
		                                  operator):
			for x in range(temp_string.count(operator_repl[ operator ])):
				arith = re.search('\d+' + operator_repl[ operator ] + '[\-\+]?\d+', temp_string)
				if not arith:
					break
				else:
					arith = arith.span()
					if arith[ 0 ] == 1:
						arith = (0, arith[ 1 ])
					elif arith[ 0 ] > 0 and temp_string[ arith[ 0 ] - 1 ] == '-':
						arith = (arith[ 0 ] - 1, arith[ 1 ])
				try:
					resolve = resolve_operation(temp_string[ arith[ 0 ]: arith[ 1 ] ])
					if int(resolve) < 0:
						if arith[ 0 ] > 0:
							if temp_string[ arith[ 0 ] - 1 ] == '-':
								temp_string = f'{temp_string[ :arith[ 0 ] - 1 ]}+{temp_string[ arith[ 0 ]: ]}'
								resolve = int(str(resolve)[ 1: ])
							elif temp_string[ arith[ 0 ] - 1 ] == '+':
								temp_string = f'{temp_string[ :arith[ 0 ] - 1 ]}-{temp_string[ arith[ 0 ]: ]}'
								resolve = int(str(resolve)[ 1: ])

					string = f'{temp_string[ :arith[ 0 ] ]}{resolve}{temp_string[ arith[ 1 ]: ]}'
					temp_string = string
				except IndexError:
					print('')
					break

	return int(string)


if __name__ == "__main__":
	string = sys.argv;
	if len(string) == 1:
		print("Done.")
	else:
		string = sys.argv[1];
		result = ALU(string)

		print(result)
