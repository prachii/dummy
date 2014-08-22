while True:
	Firstname=raw_input('Enter your name : ')
	Lastname=raw_input('Enter your lastname : ')
	dict={'First name':Firstname, ' Last name':Lastname}
	if Firstname == "" and Lastname == "":
		break
	print dict
