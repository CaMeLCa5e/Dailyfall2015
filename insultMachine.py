#! /usr/bin/env python

import os 
import random 

def main(): 
	insults = "no"
	print "welcome! please enter a number"
	num = random.randrange(100)
	guess = ''

	while guess != num: 
		guess = int(raw_input("Take a guess: "))
		print "Nope, try again"
	print "You got it!!!"
	raw_input()

main()	