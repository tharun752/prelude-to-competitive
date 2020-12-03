def lowerbound(l,x):
    mins=0
    maxs=len(l)-1
    while(mins<maxs):
        mid=(mins+maxs)//2
        if(x<=l[mid]):
            maxs=mid
        else:
            mins=mid+1
    if(l[mins]!=x):
        return -1
    return mins
def upperbound(l,x):
    mins=0
    maxs=len(l)-1
    while(mins<maxs):
        mid=(mins+maxs)//2
        if(x>=l[mid]):
            mins=mid+1
        else:
            maxs=mid
    if(l[mins]==x):
        return -1
    return mins-1