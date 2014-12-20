#run as: python 4hello.py name1 name2 name3 ...
import sys
print "greetings,",

if len(sys.argv) ==1:
	print "my nameless friend"
elif len(sys.argv)==2:
	print sys.argv[1]
else:
	i=1
	last_index = len(sys.argv) -1
	while i < last_index:
		print sys.argv[i] + ",",
		i=i+1
	print "and", sys.argv[last_index]
#There is no "switch" statement in Python, instead a long "if: ... elif: ... elif: ... else: ..." statement is used.