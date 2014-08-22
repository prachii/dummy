mystr=raw_input('Enter the string: ')
#r_str=reversed(mystr)
r_str=mystr[::-1]

print r_str

if mystr==r_str:
	print "y"
else:
	print "n"
"""
if list(mystr) == list(r_str):
	print "This is a palindrome"
else:
	print "Not a palindrome"
"""
