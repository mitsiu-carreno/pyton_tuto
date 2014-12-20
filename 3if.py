#run as: python 3hello.py mitsiu
import sys
#la coma despues de el ultimo argumento de print hace que siga en la misma linea
print "greetings, ",
#len = length
if len(sys.argv)==2:
	print sys.argv[1]
else:
	print "my nameless friend"