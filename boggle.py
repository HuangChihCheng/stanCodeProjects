"""
File: boggle.py
Name: 黃稚程 mike
----------------------------------------
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""
	TODO:
	"""
	start = time.time()

	dictionary = read_dictionary()
	row1 = input("1 row of letters: ")
	row1 = row1.split()
	continue_or_not = check(row1)
	if continue_or_not:
		row2 = input("2 row of letters: ")
		row2 = row2.split()
		continue_or_not = check(row2)
		if continue_or_not:
			row3 = input("3 row of letters: ")
			row3 = row3.split()
			continue_or_not = check(row3)
			if continue_or_not:
				row4 = input("4 row of letters: ")
				row4 = row4.split()
				continue_or_not = check(row4)
				if continue_or_not:
					dic = {}
					for i in range(4):
						dic[(i, 0)] = row1[i]
					for i in range(4):
						dic[(i, 1)] = row2[i]
					for i in range(4):
						dic[(i, 2)] = row3[i]
					for i in range(4):
						dic[(i, 3)] = row4[i]
					key = []
					ans = []
					total_ans = []
					for x in range(4):
						for y in range(4):
							ans += dic[(x, y)]
							key.append((x, y))
							find_words(x, y, dictionary, dic, ans, key, total_ans)
							ans.clear()
							key.clear()
					print(f"There are {len(total_ans)} words in total")

					end = time.time()
					print('----------------------------------')
					print(f'The speed of your boggle algorithm: {end - start} seconds.')
				else:
					print("Illegal input")
			else:
				print("Illegal input")
		else:
			print("Illegal input")
	else:
		print("Illegal input")


def find_words(x, y, dictionary, dic, ans_lst, used_key, total_ans):
	for i in range(-1, 2):
		for j in range(-1, 2):
			if ((x + i) >= 0) and ((x + i) < 4):
				if ((y + j) >= 0) and ((y + j) < 4):
					new_letter = dic[(x+i, y+j)]
					if new_letter not in ans_lst:
						ans_lst.append(new_letter)
						used_key.append((x+i, y+j))
						on_off = has_prefix(ans_lst, dictionary)
						if on_off:
							if len(ans_lst) >= 4:
								s = ''
								for letter in ans_lst:
									s += letter
								if s in dictionary:
									if s not in total_ans:
										print(f"Found \"{s}\"")
										total_ans.append(s)
										find_words(x + i, y + j, dictionary, dic, ans_lst, used_key, total_ans)
										ans_lst.pop()
										used_key.pop()
									else:
										find_words(x + i, y + j, dictionary, dic, ans_lst, used_key, total_ans)
										ans_lst.pop()
										used_key.pop()
								else:
									find_words(x + i, y + j, dictionary, dic, ans_lst, used_key, total_ans)
									ans_lst.pop()
									used_key.pop()
							else:
								find_words(x + i, y + j, dictionary, dic, ans_lst, used_key, total_ans)
								ans_lst.pop()
								used_key.pop()
						else:
							ans_lst.pop()
							used_key.pop()
					else:
						if (x+i, y+j) not in used_key:
							ans_lst.append(new_letter)
							used_key.append((x+i, y+j))
							on_off = has_prefix(ans_lst, dictionary)
							if on_off:
								if len(ans_lst) >= 4:
									s = ''
									for letter in ans_lst:
										s += letter
									if s in dictionary:
										if s not in total_ans:
											print(f"Found \"{s}\"")
											total_ans.append(s)
											find_words(x + i, y + j, dictionary, dic, ans_lst, used_key, total_ans)
											ans_lst.pop()
											used_key.pop()
										else:
											find_words(x + i, y + j, dictionary, dic, ans_lst, used_key, total_ans)
											ans_lst.pop()
											used_key.pop()
									else:
										find_words(x + i, y + j, dictionary, dic, ans_lst, used_key, total_ans)
										ans_lst.pop()
										used_key.pop()
								else:
									find_words(x + i, y + j, dictionary, dic, ans_lst, used_key, total_ans)
									ans_lst.pop()
									used_key.pop()
							else:
								ans_lst.pop()
								used_key.pop()


def check(row):
	if len(row) == 4:
		for ele in row:
			if len(ele) != 1:
				return False
		return True
	else:
		return False


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	dictionary = []
	with open(FILE, 'r') as f:
		for line in f:
			backlash_position = line.find('\\')
			word = line[:backlash_position]
			dictionary.append(word)
		return dictionary


def has_prefix(sub_s, dictionary):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	s = ''
	for letter in sub_s:
		s += letter
	for words in dictionary:
		if words.startswith(s):
			return True
	return False


if __name__ == '__main__':
	main()
