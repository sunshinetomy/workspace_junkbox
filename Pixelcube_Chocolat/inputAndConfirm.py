def inputTexts():	
	inputText = ""
	while True:
		input_str = input(">")
		if input_str == "a":	# auto
			return "a"
			
		if input_str == "":
			break
		else:
			if inputText == "":
				inputText += input_str
			else:
				inputText += ( "\n" + input_str )
	
	print( inputText )
	return inputText


def inputAndConfirm():
	result = ""

	isOk = False
	while False == isOk:
		result = inputTexts()
		
		if result == "a":		# auto
			return "auto"
			
		if result == "":
			print( "Comment is Empty!!!, Need Comment!" )
			continue
		
		answer = input( "isOk? (y/n) : " )
		if answer == "y": # or answer == "ㅛ":
			break
		else:
			continue
			
	print( result )
	return result
	

	

	
