import collections

class Solution:
    def topKFrequent(self, nums, k) :
        c=collections.Counter(nums)
        s=c.most_common(k)  ##里面调了sorted方法，是O(nlogn)
        li=[]
        for i in range (0,len(s)):
            li.append(s[i][0])
        return li

nums=[1,1,1,2,2,3]
k=2
res=Solution().topKFrequent(nums,k)
print("res:",res)