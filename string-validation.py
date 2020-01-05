if __name__ == '__main__':
    s = input()
    print(any(char.isalnum() for char in s),any(char.isalpha() for char in s), any(char.isdigit() for char in s),any(char.islower() for char in s),any(char.isupper() for char in s),sep="\n")
