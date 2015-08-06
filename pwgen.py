#! /usr/bin/python

import argparse
import os
import random
import string

# Pasring the Arguments
parser = argparse.ArgumentParser(description='LAN-SCAN')
parser.add_argument('-l','--length', help='Password length', default=12)
parser.add_argument('-q','--quantity', help='The number of passwords you want to be generated', default=1)

args = vars(parser.parse_args())
length = str(args['length'])
quantity = int(args['quantity'])

for x in range (0, quantity):

	# Generating the password
	chars = string.ascii_letters + string.digits + '!@#$%^&*()'
	random.seed = (os.urandom(1024))

	print ''.join(random.choice(chars) for i in range(int(length)))
