#!/usr/bin/python
#./7hashbanging.py mitsiu

import sys

def greet(greeting, names):
	print greeting + ",",

	if not names:
		print "my nameless friend"
	elif len(names)==1:
		print names[0]
	else:
		for name in names[:-1]:
			print name + ",",
		print "and", names[-1]

def main():
	greet("hi there", sys.argv[1:])

main()
