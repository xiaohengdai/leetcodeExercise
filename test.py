from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        size = len(candidates)
        if size == 0:
            return []
        print("candidates:", candidates)
        print('size:', size)
        def dfs( begin,  path, res, target):

            print("begin:",begin)

            print("path:",path)
            print("res:",res)
            print("target:",target)
            if target < 0:
                return
            if target == 0:
                res.append(path)
                return

            for index in range(begin, size):
                dfs( index, path + [candidates[index]], res, target - candidates[index])


        path = []
        res = []
        dfs( 0,  path, res, target)
        return res

candidates = [2, 3, 6, 7]
target = 7

res=Solution().combinationSum(candidates=candidates,target=target)
print("res:",res)