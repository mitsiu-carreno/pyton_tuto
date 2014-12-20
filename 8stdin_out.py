#!/usr/bin/python
#See https://wiki.debian.org/DebianWomen/PythonTutorial#The_hello_world_program 
#cause i really didn't get this one :(

import sys

line_count = 0
while True:
    line = sys.stdin.readline()
    if not line:
    	print "bye"
        break
    line_count += 1

sys.stdout.write("%d lines\n" % line_count)