"""
File: boggle.py
Name: Tracy Lee
----------------------------------------
TODO:
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""
	This program asks user to input 4 rows of letters separated by spaces.

	If the format is inconsistent,
	such as inputting numbers, letters without spaces, etc.,
	it will be regarded as Illegal Input,
	and the program will be terminated directly.

	Results will be rendered in lowercase letters regardless of input case.

	If the user's input is correct,
	the program will start to look for the words
	that can be formed within the 16 letters,
	and finally get the total number of words.
	"""
	rows = lineup()
	start = time.time()
	if rows:
		find_word(rows)
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list.

	:return: list; a list stores the words
	"""
	word_list = []
	with open(FILE, "r") as f:
		for line in f:
			word = line.strip()
			if len(word) >= 4:
				word_list.append(word)
	return word_list


def has_prefix(sub_s, dic_lst):
	"""
	To check if there is any word starts with sub_s.

	:param sub_s: str; a substring that is constructed by neighboring letters on a 4x4 square grid
	:param dic_lst: list; a list stores the words
	:return: bool; if there is any words with prefix stored in sub_s
	"""
	for word in dic_lst:
		if word.startswith(sub_s):
			return True
	return False


def lineup():
	"""
	To store the input strings into a list.

	:return: list; a list that stores the list of the input string
	"""
	rows = []  # store 4 rows
	for i in range(4):
		letters = input(f"{i+1} row of letters: ").lower().split()
		if is_illegal(letters):
			print("Illegal input")
			break
		else:
			rows.append(letters)
	return rows


def is_illegal(letters):
	"""
	If there is any illegal input,
	such as inputting numbers, letters without spaces, etc.,
	return True to terminate the program.

	:param letters: list; a list that stores the input string
	:return: bool; if there is any illegal input or not
	"""
	if len(letters) != 4:
		return True
	for ch in letters:
		if len(ch) != 1:
			return True
		if not ch.isalpha():
			return True


def find_word(rows):
	"""
	Find the words that are constructed by neighboring letters on a 4x4 square grid,
	and record how many words had been found.

	:param rows: list; a list that stores the list of the input string
	"""
	dic_lst = read_dictionary()
	word_lst = []
	for x in range(4):
		for y in range(4):
			s = rows[x][y]
			coordinate = (x, y)
			chosen_lst = [coordinate]
			find_word_helper(s, coordinate, rows, dic_lst, word_lst, chosen_lst)
	print(f"There are {len(word_lst)} words in total.")


def find_word_helper(s, coordinate, rows, dic_lst, word_lst, chosen_lst):
	"""
	The helper function to construct neighboring letters on a 4x4 square grid.

	:param s: str; the string of the letters in the rows
	:param coordinate: tuple; the coordinate of the rows,
								x is the index of the rows,
								y is the index of the input string
	:param rows: list; a list that stores the list of the input string
	:param dic_lst: list; a list stores the words
	:param word_lst: list; a list stores the found words
	:param chosen_lst:list; a list stores the coordinates that have been chosen
	"""
	if len(s) >= 4:
		if s in dic_lst and s not in word_lst:
			print(f"Found: \"{s}\"")
			word_lst.append(s)

	if len(s) == 16:
		return

	for i in range(-1, 2, 1):
		for j in range(-1, 2, 1):
			new_x = coordinate[0] + i
			new_y = coordinate[1] + j
			if 0 <= new_x < 4 and 0 <= new_y < 4 and (new_x, new_y) not in chosen_lst:
				# choose
				s += rows[new_x][new_y]
				chosen_lst.append((new_x, new_y))
				# explore
				if has_prefix(s, dic_lst):
					find_word_helper(s, (new_x, new_y), rows, dic_lst, word_lst, chosen_lst)
				# un-choose
				s = s[:-1]
				chosen_lst.pop()


if __name__ == '__main__':
	main()
