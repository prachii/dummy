while True:
	Firstname=raw_input('Enter your firstname : ')
	Lastname=raw_input('Enter your lastname : ')
	dict={'Fname':Firstname, 'lname':Lastname}
	if Firstname == "" and Lastname == "":
		break
	print dict
