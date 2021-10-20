"""
File: coin_flip_runs.py
Name:黃稚程 mike
-----------------------
This program should simulate coin flip(s)
with the number of runs input by users.
A 'run' is defined as consecutive results
on either 'H' or 'T'. For example, 'HHHHHTHTT'
is regarded as a 2-run result.
Your program should stop immediately after your
coin flip results reach the runs!
"""

import random as r


def main():
	"""
	This function will ask the user input the number of the runs, and it will spontaneously flip the coin until the
	number of runs reaches the user input.
	"""
	num_run = 0
	print("Let\'s flip a coin !")
	a = int(input("Number of runs: "))
	b = ""
	c = r.randint(0, 1)
	if c == 0:
		c = 'H'
		b += c
	else:
		c = 'T'
		b += c
	d = 0
	while num_run != a:
		c = r.randint(0, 1)
		if c == 0:
			c = 'H'
		else:
			c = 'T'
		if d == 0:
			if c == b[len(b)-1]:
				num_run += 1
				b += c
				d += 1
			else:
				b += c
				d += 1
		else:
			if c == b[len(b)-1]:
				num_run += 1
				if c == b[len(b)-2]:
					num_run -= 1
					b += c
				else:
					b += c
			else:
				b += c
	print(b)


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
