# Enter your code here. Read input from STDIN. Print output to STDOUT
n_lines,width = list(map(int,input().split()))

# the top design
string = ".|."
for i in range(n_lines//2):
    print((string*(2*i+1)).center(width,"-"))

# the middle welcome
print("WELCOME".center(width,"-"))


#the bottom design 
for i in range(n_lines//2):
    print((string*(2*(n_lines//2-i)-1)).center(width,"-"))

