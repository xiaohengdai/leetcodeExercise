class Solution:
    def lengthOfLongestSubstring(self, s) :
        if len(s)<=1:
            return len(s)
        i=0
        j=1
        max_len=1
        while i<len(s):
            while j<len(s):
                if s[j] not in s[i:j]:
                    j=j+1
                    if len(s[i:j])>max_len:
                        max_len=len(s[i:j])
                else:
                    if len(s[i:j])>max_len:
                        max_len=len(s[i:j])
                    break
            i=i+1
        return max_len


res=Solution().lengthOfLongestSubstring(s="au")
print("res:",res)