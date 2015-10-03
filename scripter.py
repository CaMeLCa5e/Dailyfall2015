#! usr/bin/env python 
from time import *
import os, sys

char_start = 0
char_end = 1
string = sys.stdin.read()

if len(sys.argv) > 1: 
	delay = float(sys.argv[1])

else: 
	delay = 0.09

strlength = len(string) +1

while char_end <= strlength: 
	printchar = string[char_start:char_end]
	sys.stdout.write(printchar)
	sys.stdout.flush()
	sleep(delay)
	char_end += 1
	char_start += 1

exit