#!/usr/bin/env python
import argparse
import os

def main():
	parser = argparse.ArgumentParser()
	group = parser.add_mutually_exclusive_group()
	group.add_argument('-v','--verbose',help='turn verbosity on',
							action='store_true')
	group.add_argument('-q','--quit',help='turn verbosity off',
							action='store_true')
	parser.add_argument('-d','--debug',help='turn debug on',
							action='store_true')
	parser.add_argument('-m',help='display mode',
								type=int)
	parser.add_argument('dir',help='directory you want to list')
				
	args = parser.parse_args()
	if args.verbose :
		print 'verbose display is turned on'
	if args.debug:
		print 'debug mode is turned on'

	directory = args.dir
	result = os.listdir(directory)
	for i in result:
		print i


if __name__ == '__main__':
	main()
