def generate_design(chars):
	if len(chars) < 2:
		return chars
	return chars[:len(chars)]+chars[-2::-1]

def print_rangoli(n):
	from string import ascii_lowercase as alpha 
	chars = alpha[:n][::-1]
	pattern=[]
	for i in range(1,n+1):
		pattern.append(generate_design(chars[:i]))
		# i know u can do a one liner in a for loop to generate stuff like this its not at all readable :(  
		#pattern.append(chars[:len(chars[:i])]+chars[:i][-2::-1])
	pattern = pattern+pattern[-2::-1]
	for  i in pattern:
		print(str("-".join(i)).center(4*n-3,"-"))


if __name__ == "__main__":
	n = int(input())
	print_rangoli(n)
