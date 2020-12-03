class Solution:
    def kadane(self,l):
        mxsub=[0]*len(l)
        mxsub[0]=l[0]
        for i in range(1,len(l)):
            mxsub[i]=max(mxsub[i-1]+l[i],l[i])
        return max(mxsub)
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        normal=self.kadane(A)
        if(normal<0):
            return normal
        sums=0
        for i in range(len(A)):
            sums+=A[i]
            A[i]=-A[i]
        circular=self.kadane(A)+sums
        return max(normal,circular)