import collections

# class Solution: #nlog(n)
#     def topKFrequent(self, nums, k) :
#         c=collections.Counter(nums)
#         s=c.most_common(k)  ##里面调了sorted方法，是O(nlogn)
#         li=[]
#         for i in range (0,len(s)):
#             li.append(s[i][0])
#         return li
#
# nums=[1,1,1,2,2,3]
# k=2
# res=Solution().topKFrequent(nums,k)
# print("res:",res)

#堆排序
# 那么具体的做法如下：
#
# 先用哈希表统计元素出现的次数；
# 建立一个最小堆，维护最小堆：
# 当堆中元素数目小于 k，这里直接将元素插入；
# 若堆中元素数目等于 k 时，这个时候要将新元素出现频率与堆顶元素出现频率进行比较。若新元素出现频率大于堆顶元素，那么弹出，插入新元素。
# 最终，堆中的 k 个即是要求的答案。
import heapq
class Solution:
    def topKFrequent(self,nums,k):
        if len(nums)==0:
            return []
        dic=dict()
        for num in nums:
            dic[num]=dic.get(num,0)+1
        li =list()

        for item in dic.items():
            if len(li)==k:
                if item[1]>li[0][0]:

                    heapq.heappop(li)
                    heapq.heappush(li,(item[1],item[0]))
            else:
                heapq.heappush(li,(item[1],item[0]))

        return [li[len(li)-i-1][1] for i in range (0,len(li)) ]

nums=[1,1,1,2,2,3]
k=2

s=Solution().topKFrequent(nums=nums,k=k)
print("s:",s)


