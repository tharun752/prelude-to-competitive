def reverse(sb,start,stop):
    start=start
    stop=stop
    while(start<=stop):
        sb[start],sb[stop]=sb[stop],sb[start]
        start+=1
        stop-=1
    # print(sb)
sb=input()
sb=list(sb)
start=0
end=0
for i in range(len(sb)):
    if(sb[i]==" " ):
        
        end=i-1
        reverse(sb,start,end)
        start=i+1
reverse(sb,start,len(sb)-1)
print(sb)
reverse(sb,0,len(sb)-1)
print("".join(str(i) for i in sb))