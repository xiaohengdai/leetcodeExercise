class Solution:
    def combinationSum(self, candidates, target) :
        res = []

        def backtrack(candidates, path, target, start):
            if sum(path) == target:
                print("path:", path)
                print("path[:]:", path[:])
                res.append(path)
                return
            if sum(path) > target:
                return

            for i in range(start, len(candidates)):
                path.append(candidates[i])

                backtrack(candidates, path, target, i)
                path.pop()

        backtrack(candidates, [], target, 0)
        return res

candidates = [2,3,6,7]
target = 7
res=Solution().combinationSum(candidates=candidates,target=target)
print("res:",res)
