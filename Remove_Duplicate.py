
class Solution:
    def removeDuplicates(self, nums=[]) :
        if not nums:
            return 0
        arr=[]
        for i in nums:
            if i in arr:
                pass
            else:
                arr.append(i)
        print(arr)

df=Solution()
List=[1,2,3,5,2,1,2,1]
df.removeDuplicates(List)
