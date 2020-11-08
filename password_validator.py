import re


x = ''

while x != 'quit' :
	password = input('Enter Password: ')
	if len(password)< 8:
		print('length of the password must be greater than equals to 8')
	elif not re.search('[a-z]', password):
		print('Password must contain letters')
	elif not re.search('[A-Z]', password):
		print('Password must contain atleast a Capital letter')
	elif not re.search('[0-9]', password):
		print('Input atleast a number')
	elif not re.search('[$#@]', password):
		print('input a special character')
	elif re.search('\s', password):
		break
	else:
		print(f'Password valid, Your password is {password}')
		x = False
		break


if x:
	print('The password not valid')


