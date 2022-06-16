def binarise_digits(digit, simple=None, binary=False):
	if binary:
		if type(digit) == str:
			digit = int(digit or '0', 2)
		else:
			digit = int(str(digit), 2)

	if simple:
		return bin(int(digit or 0))[ 2: ]

	digit = str(digit)
	binary = ''
	for d in digit:
		byte = bin(int(d))[ 2: ]
		while len(byte) < 8:
			byte = f'0{byte}'
		binary += f'{byte} '
	return binary.strip()


def resolve_max_binary_len(binary_array1, binary_array2):
	max_binary_len = len(binary_array1)
	if max_binary_len < len(binary_array2):
		max_binary_len = len(binary_array2)
	return max_binary_len


def inc_bin(binary, inc=1):
	d = int(binary, 2) + inc
	return bin(d)[ 2: ]


def string_to_list(string):
	if not string:
		return [ ]
	return [ s for s in string ]


def padd_string(str1, str2, padd=' ', ret=False):
	str_len = len(str1)
	if str_len < len(str2):
		str_len = len(str2)

	while len(str1) < str_len:
		str1 = f'{padd}{str1}'
	if ret:
		return str1


def padd_array(arr1, arr2, padd=None):
	max_len = resolve_max_binary_len(arr1, arr2)
	if len(arr1) < max_len:
		while len(arr1) < max_len:
			arr1.insert(0, padd)
	elif len(arr2) < max_len:
		while len(arr2) < max_len:
			arr2.insert(0, padd)
