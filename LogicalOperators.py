#!/usr/bin/env python

a = 10
b = 5
if a == 10 and b == 5:
	print("The condition has been met")
else:
	print("The condition has not been met")

a = False
b = False
if not(a and b):
	print("The condition has been met")
else:
	print("The condition has not been met")
	
a = True
b = False
if a or b:
	print("The condition has been met")
else:
	print("The condition has not been met")
	
variable = "X-Team"
if "Team" in variable:
	print("The value of Team is in the variable")
else:
	print("The value of Team is not in the variable")