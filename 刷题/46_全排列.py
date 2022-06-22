#参考文章：https://leetcode.cn/problems/permutations/solution/by-huan-huan-20-hblf/
class Solution:
    def permute(self, nums) :
        res=[]
        used=[False]*len(nums)
        def backtrack(nums,path,used):
            print("path:",path)

            if len(path)==len(nums):
                res.append(path[:])
                return

            for i in range (0,len(nums)):
                if used[i]:
                    continue
                path.append(nums[i])
                used[i]=True

                backtrack(nums,path,used)
                # print("path:",path)
                path.pop()
                used[i]=False
        backtrack(nums,[],used)
        return res

r=Solution().permute(nums=[1,2,3])
print("r:",r)