#!/usr/bin/env python

# requires Python 2.7+ or the argparse module to be installed

import argparse
import string
import random

cmd_parser = argparse.ArgumentParser(description="Generates random passwords for you")

cmd_parser.add_argument('-l', 
			'--length', 
			type=int, 
			metavar='num', 
			default=8, 
			dest='cmd_len', 
			help='Number of characters the password must be.')
			
cmd_parser.add_argument('-s', 
			'--special', 
			action='store_true', 
			dest='cmd_special', 
			help='Use special characters such as punctuation.')
			
cmd_parser.add_argument('-n', 
			'--num', 
			type=int, 
			default=1, 
			metavar='num', 
			dest='cmd_num', 
			help='Number of passwords to generate')

cmd_args = cmd_parser.parse_args()


if cmd_args.cmd_num < 1:
    cmd_args.cmd_num = 1
    
if cmd_args.cmd_len < 8:
    cmd_args.cmd_len = 8

def pass_gen (size, use_special):
    if use_special == False:
        chars = string.letters + string.digits
    else:
        chars = string.letters + string.digits + string.punctuation

    return ''.join((random.choice(chars)) for x in range(size))

for x in range(cmd_args.cmd_num):
    print pass_gen(cmd_args.cmd_len, cmd_args.cmd_special)

