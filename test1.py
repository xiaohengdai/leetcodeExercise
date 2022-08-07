class Solution:
    def findMaxLength(self, nums) :
        max_len=0
        di={}
        prefix_num=0
        for i in range (0,len(nums)):
            if nums[i]==0:
                nums[i]=-1
            prefix_num=prefix_num+nums[i]
            if prefix_num == 0:
                length = i + 1
                if length > max_len:
                    max_len = length
            elif di.get(prefix_num) is not None:

                length=i-di.get(prefix_num)
                if length>max_len:
                    max_len=length
            else:
                di[prefix_num]=i
        return max_len


res=Solution().findMaxLength(nums=[0,0,1])
print(res)