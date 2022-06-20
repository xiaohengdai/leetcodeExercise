# https://leetcode.cn/problems/top-k-frequent-elements/solution/python3-zi-dian-cun-chu-you-xiu-dui-lie-r6yvo/
'''
先用字典格式(hash算法进行数据存储)后维护一个k的优先队列最终取出队列里面的所有元素
优先队列直接调用包就行，大佬可以自己写。。。
'''
import queue
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        #创建hash结构dict存储次数并遍历获取个数
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] +=1
        #创建优先队列并更新
        q = queue.PriorityQueue()
        for i,j in dic.items():
            q.put((j,i))
            if q.qsize() > k:
                q.get()
        #获取优先队列中的k个元素
        res = []
        while  not q.empty():
            res.append(q.get()[1])
        return res

# 作者：806748118
# 链接：https://leetcode.cn/problems/top-k-frequent-elements/solution/python3-zi-dian-cun-chu-you-xiu-dui-lie-r6yvo/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。