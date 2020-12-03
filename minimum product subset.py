
class Solution:
    def miniminproductsuvset(self,l):
        cntzeroes=0
        cntnegatives=0
        mxnegative=float('-inf')
        mxpositive=float('inf')
        product=1
        for i in range(len(l)):
            if(l[i]==0):
                cntzeroes+=1
                continue
            elif(l[i]<0):
                cntnegatives+=1
                mxnegative=max(mxnegative,l[i])
            else:
                mxpositive=min(mxpositive,l[i])
            product=product*l[i]
        print(cntnegatives,cntzeroes,product,mxnegative,mxpositive)
        if(cntzeroes==len(l) or(cntnegatives==0 and cntzeroes>0)):
            return (0)
        if(cntnegatives%2==0 and cntnegatives!=0):
            return product//mxnegative
        if(cntnegatives==0 and cntzeroes==0):
            return mxpositive
        
        return product
    def maximumproductsuvset(self,l):
        cntzeroes=0
        cntnegatives=0
        mnnegative=float('-inf')
        mxpositive=float('inf')
        product=1
        for i in range(len(l)):
            if(l[i]==0):
                cntzeroes+=1
                continue
            elif(l[i]<0):
                cntnegatives+=1
                mnnegative=max(mnnegative,l[i])
            
            product=product*l[i]
        print(cntnegatives,cntzeroes,product,mnnegative,mxpositive)
        if(cntzeroes==len(l) ):
            return (0)
        if(cntnegatives%2!=0 and cntnegatives!=0):
            if(cntnegatives==1 and (cntnegatives+cntzeroes)==len(l)):
                return 0
            return product//mnnegative
    
        # if(cntnegatives%2==0 and cntnegatives!=0 and cntzeroes==0):
        #     return product
        print("heee")
        return product
    
    def getMaxandMinProduct( self,arr, n):
        

        return(self.maximumproductsuvset(arr),self.miniminproductsuvset(arr))
a=Solution()
e=a.getMaxandMinProduct(list(map(int,input().split())),int(input()))
print(e)