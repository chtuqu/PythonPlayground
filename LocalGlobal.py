#!/usr/bin/env python
hacker = "me"

def local_variable_example():
	hacker = "you"
	print("The local variable is {}".format(hacker))
	
local_variable_example()
print("The global variable is {}".format(hacker))