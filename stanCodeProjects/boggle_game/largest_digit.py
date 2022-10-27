"""
File: largest_digit.py
Name: Tracy Lee
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	"""
	:return: int; The biggest digit in the integer.

	The program will print the biggest digit in the integer.
	"""
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: int; The target integer.
	:return: int; The biggest digit in the integer.

	The program will find the biggest digit in the integer.
	"""
	if n < 0:
		n = -n
	return find_largest_digit_helper(n, -float("inf"))  # 初始值負無限小


def find_largest_digit_helper(n, ans):
	"""
	:param n: int; The target integer.
	:param ans: int; The biggest number in the integer.
	:return: int; The biggest in the integer.

	This program will keep dividing the integer by 10 to find the largest digit and return it.
	"""
	if n == 0:
		return ans
	else:
		if n % 10 > ans:
			ans = n % 10
		return find_largest_digit_helper(n // 10, ans)


if __name__ == '__main__':
	main()
