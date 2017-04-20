#! /usr/bin/python

import argparse
import os
import random
import string

# Pasring the Arguments
parser = argparse.ArgumentParser(description='LAN-SCAN')
parser.add_argument('-l','--length', help='Password length', default=15)
parser.add_argument('-q','--quantity', help='The number of passwords you want to be generated', default=1)
parser.add_argument('-c','--complexity', help='Defines if you want special characters in your password', default=1)

args = vars(parser.parse_args())
length = str(args['length'])
quantity = int(args['quantity'])
complexity = int(args['complexity'])

for x in range (0, quantity):

	# Generating the password
	
	sc = '!@#$%&*()'
	if complexity == 1:
	    chars = string.ascii_letters + string.digits + sc 
	else: 
	    chars = string.ascii_letters + string.digits
	
	random.seed = (os.urandom(1024))
	print ''.join(random.choice(chars) for i in range(int(length)))
