#run as: python 6functions.py name1 name2 name3

import sys

def greet(greeting, names):
	print greeting + ",",

	if not names:
		print "my nameless frined"
	elif len(names)==1:
		print names[0]
	else:
		for name in names[:-1]:
			print name+ ",",
		print "and", names[-1]

greet("hi there", sys.argv[1:])