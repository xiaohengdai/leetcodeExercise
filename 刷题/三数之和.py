class Solution:
    def threeSum(self, nums) :
        if len(nums) < 2:
            return []
        res_li = []
        nums.sort()
        for i in range(0, len(nums) - 2):
            if (i>0)and (nums[i] == nums[i - 1]) :
                continue
            two_sum = -nums[i]
            surplus_li = nums[i + 1:]
            left = 0
            right = len(surplus_li)-1
            while left < right:
                li = []
                if surplus_li[left] + surplus_li[right] == two_sum:
                    li.append(nums[i])
                    li.append(surplus_li[ left])
                    li.append(surplus_li[right])
                    res_li.append(li)
                    while (left < right)  and (surplus_li[left] == surplus_li[left + 1]) :
                        left = left + 1
                    while (right+1<len(surplus_li))and (surplus_li[right] == surplus_li[right + 1]) and (left < right):
                        right = right - 1
                    left = left + 1
                    right = right - 1
                elif surplus_li[left] + surplus_li[right] < two_sum:
                    left = left + 1
                elif surplus_li[left] + surplus_li[right] > two_sum:
                    right = right - 1
        return res_li


res=Solution().threeSum(nums=[0,0,0])
print("res:",res)
