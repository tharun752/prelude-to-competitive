
class Solution:
    def merge(self, arr: List[List[int]]) -> List[List[int]]:
        arr.sort(key=lambda arr:arr[0])
        res=0
        for j in range(1,len(arr)):
            if(arr[res][1]>=arr[j][0]):
                arr[res][0]=min(arr[res][0],arr[j][0])
                arr[res][1]=max(arr[res][1],arr[j][1])
            else:
                res+=1
                arr[res]=arr[j]
        
        return arr[:res+1]