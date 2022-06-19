from math import inf


class Solution:
    def threeSum(self, nums,target) :
        if len(nums) < 2:
            return []
        nums.sort()
        min_value=float(inf)
        li = [inf,inf,inf]
        for i in range(0, len(nums) - 2):
            if (i>0)and (nums[i] == nums[i - 1]) :
                continue
            two_sum = target-nums[i]
            surplus_li = nums[i + 1:]
            left = 0
            right = len(surplus_li)-1
            while left < right:
                s=nums[i]+surplus_li[left]+surplus_li[right]
                value = abs(two_sum - (surplus_li[left] + surplus_li[right]))
                if value < min_value:
                    li[0] = nums[i]
                    li[1] = surplus_li[left]
                    li[2] = surplus_li[right]
                    min_value = value
                if s==target:
                    break
                elif s>target:
                    right = right - 1
                else:
                    left = left + 1
        return sum(li)


res=Solution().threeSum(nums=[-1,2,1,-4],target=1)
print("res:",res)
