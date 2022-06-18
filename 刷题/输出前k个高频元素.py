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
        import heapq
        words = nums
        if len(words) == 0:
            return []
        di = {}
        heap = []
        for i in range(0, len(words)):
            if di.get(words[i]):
                di[words[i]] = di[words[i]] + 1
            else:
                di[words[i]] = 1

        for key, count in di.items():
            heapq.heappush(heap, (-count, key))
        li = []
        for i in range(0, k):
            li.append(heapq.heappop(heap)[1])
        return li

nums=[1,1,1,2,2,3]
k=2

s=Solution().topKFrequent(nums=nums,k=k)
print("s:",s)


