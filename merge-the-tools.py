def merge_the_tools(string, k):
    seen = ""
    for i in range(len(string)):
        if string[i] not in seen:
            seen+=string[i]
        if (i+1)%k == 0:
            print(seen)
            seen = ""

    # if k == 1:
    #     for i in string:
    #         print(i)
    #     return
    # cuts = []
    # for i in range(0,len(string),k):
    #     cuts.append(string[i:i+k])
    
    # seen = {}
    # the_output = ["" for i in range(k)]
    # for i in range(len(cuts)):
    #     for char in cuts[i]:
    #         if char in seen:
    #             continue
    #         else:
    #             seen[char]=1
    #             #print(char,end="")
    #             the_output[i]+=char
    #     #print("\n")
    #     seen = {}
    # for i in the_output:
    #     print(i)

    
    # your code goes here

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
