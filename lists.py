if __name__ == '__main__':
    N = int(input())
    finalist = [] 
    while N > 0 :
        data = input().split()
        # if data[0] == "insert":
        #     finalist.insert(int(data[1]),int(data[2]))
        # elif data[0] == "append":
        #     finalist.append(int(data[1]))
        # elif data[0] == "remove":
        #     finalist.remove(int(data[1]))
        # elif data [0] == "sort":
        #     finalist.sort()
        # elif data[0] == "reverse":
        #     finalist.reverse() 
        # elif data[0] == "print":
        #     print(finalist)     
        # elif data[0] == "pop":
        #     finalist.pop()     
        
        cmd = data[0]
        args = data[1:]
        if cmd != "print":
            eval("finalist."+cmd+"("+",".join(args)+")")
        else:
            print(finalist)
        
        N-=1

        


