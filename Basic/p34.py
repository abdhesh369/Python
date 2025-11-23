def multiplier(x,y):
    for i in range(1,y+1):
        print(f"{x}*{i}={x*i}")

num=int(input("enter a number: \n"))        
lim=int(input("enter a limit number: \n"))   
multiplier(num,lim)     