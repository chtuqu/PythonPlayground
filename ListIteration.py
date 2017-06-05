#!/usr/bin/env python

list_example = [100,222,333,444,'string value']
list_example_length = len(list_example)
for iteration in list_example:
	index_value = list_example.index(iteration)
	print('The length of list list_example is {}, the value at position {} is {}'.format(list_example_length, index_value, iteration))
	
print('Script finished')	