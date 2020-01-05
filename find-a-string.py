def count_substring(string, sub_string):
    # count= 0
    # for i in range(len(string)-len(sub_string)+1):
    #     if(string[i:i+len(sub_string)] == sub_string):
    #         count+=1
    # return count 

    #can be converted to single line using list comprehension
    
    return len([1 for i in range(len(string)-len(sub_string)+1) if string[i:i+len(sub_string)] == sub_string])
    

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
