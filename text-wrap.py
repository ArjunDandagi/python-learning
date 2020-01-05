import textwrap 

def wrap(string,max_width):
	return textwrap.fil(string,max_width)

if __name__ = "__main__":
	paragraph,max_width = input(),int(input())
	print(wrap(paragraph,max_width)
