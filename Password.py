import string
import re
# import time

def main():
	welcome()
	password = input("Enter a password: ")
	print("\nyour password length is", length(password))
#	start = time.time()
	print("your password commonality is", common_pass(password))
#	print(time.time() - start) 
	print("your password complexity is", complexity(password))

def welcome():
	"""Prints a welcome message."""
	print("=================================")
	print("Welcome to the Password Analyzer!")
	print("=================================\n")

def complexity(password):
	"""The scores of has_num, same_type, special_char, is_upper, and is_lower
	will be combined and averaged to determine the overall complexity of the 
	password, along with suggested improvements for the user to raise 
	password complexity."""
	hasnum = has_num(password)
	sametype = same_type(password)
	specialchar = special_char(password)
	isupper = is_upper(password)
	islower = is_lower(password)
	score = (hasnum + sametype + specialchar) // 3
	stuff = ""
	if hasnum != 5:
		stuff += "   3 or more numbers\n"
	if sametype != 5:
		stuff += "   more than 2 different characters\n"
	if specialchar != 5:
		stuff += "   1 or more special characters\n"
	if isupper != 5:
		stuff += "   1 or more uppercase letters\n"
	if islower != 5:
		stuff += "   1 or more lowercase letters\n"
	if score < 3:
		return "poor- next time, include:\n" + stuff
	elif score < 5:
		return "average - next time, include:\n" + stuff
	return "great- nice one dude"

def special_char(password):
	"""If a password contains one special character, it will receive a score of
	2; if a password contains more than one special character, it will receive 
	score of 5; if it has no special characters, it will receive a score of 0.
	"""
	specials = string.punctuation
	count = 0
	for char in password:
		if char in specials:
			count += 1
	if count >= 1:
		return 5
	return 0 	

def same_type(password):
	"""If a password consists of the same character repeated multiple times, it
 	will receive a score of 0; if it consists of two characters, it will receive
    a score of 2; otherwise, it will receive a score of 5"""
	try:
		p = password.lower()
	except AttributeError:
		pass
	if len(set(p)) == 1:
		return 0
	if len(set(p)) == 2:
		return 2
	return 5

def length(password):
	"""A password must be of length greater than 12 to receive the 'great' rating,
	of length less than 12 to receive the 'average' rating, and of length less than
	8 to receive the 'poor' rating."""
	l = len(password)
	if l < 8:
		return "poor- your password will be stronger if it is 12 or more characters" 
	elif l < 12:
		return "average- your password will be stronger if it is 12 or more characters"
	return "great"

def has_num(password):
	"""Counts how many numbers are in the password."""
	nums = 0
	for char in password:
		if char.isdigit():
			nums += 1 
	if nums <= 2:
		return 2
	if nums >= 3:
		return 5 
	return 0

def is_upper(password):
	"""Counts how many uppercase letters are in the password."""
	count = 0
	for char in password:
		if char.isupper():
			count += 1
	if count >= 1:
		return 5
	return 0

def is_lower(password):
	"""Counts how many lowercase letters are in the password."""
	count = 0
	for char in password:
		if char.islower():
			count += 1
	if count >= 1:
		return 5
	return 0

def common_pass(password):
	"""Checks seclists 10,000+ common passwords."""
	f = open("commonpasslist.txt", "r")
	lines = f.readlines()
	if re.search(r"password*", password):
		return "very common"
	for word in lines:
		if word == password + "\n":
			return "very common"
	f.close()
	return "uncommon"

if __name__ == "__main__":
	main()