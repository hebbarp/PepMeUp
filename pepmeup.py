# This program prints out an inspiring anecdote to pep you up randomly
import random
def pepMeUp(file):
	lines = open(file).read().splitlines()
	myline =random.choice(lines)
	if myline !='':
		print(myline)
	else:
		print("I can't think of anything inspiring right now.")
pepMeUp('trivia.txt')
	
