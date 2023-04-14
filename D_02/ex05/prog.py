def	check_string(string: str) -> str:
	if (string[:3] == 'The'):
		return ('Yes!')
	else:
		return ('No!')

# def	check_string(string: str) -> str:
# 	return ("Yes!" if string[:3] == 'The' else "No!")

print(check_string("The"))
print(check_string("Thumbs up"))
print(check_string("Theatre can be boring"))
print(check_string("This is The place"))