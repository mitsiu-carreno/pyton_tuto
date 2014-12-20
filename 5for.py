#run as: python 5hello.py name1 name2 name3 ..
import sys
print "greetings, ",

if len(sys.argv)==1:
	print "my nameless friend"
elif len(sys.argv)==2:
	print sys.argv[1]
else:
	#wow this shit is amazing!!!
	#"foo[a:b]" is a new list with all elements from index a up to, but not including index b.
	#Thus, "sys.argv[1:-1]" is all the command line arguments from the first one after the program name up until, but not including the last one
	#"foo[a:]" is everything from index a to the end of the list. "foo[:b]" is everything from the beginning of the list up to, but not including index b. "foo[:]" is a copy of the entire list.
	for name in sys.argv[1:-1]:
		print name + ",",
	print "and", sys.argv[-1]
