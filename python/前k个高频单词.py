class Solution:
    def topKFrequent(self, words, k):
        import heapq
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


words = ["i", "love", "leetcode", "i", "love", "coding"]
k = 1
res=Solution().topKFrequent(words=words,k=k)
print("res:",res)