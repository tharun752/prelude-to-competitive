def findX(A,B): 
    j = 0
    x = 0
  
    while (A or B): 
        if ((A & 1) and (B & 1)): 
            x += (1 << j) 

        A >>= 1
        B >>= 1
        j += 1
    return x 
for i in range(int(input())):
    m,n=map(int,input().split())
    mn=999
    x=findX(m,n)
    print((m^x)+(n^x))
