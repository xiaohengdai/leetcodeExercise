import functools

#动态规划更快
def wordBreak(self, s, wordDict):
    dp = [False] * (len(s) + 1)
    dp[0] = True
    for i in range(0, len(s)):
        for j in range(i + 1, len(s) + 1):
            if dp[i] and s[i:j] in wordDict:
                dp[j] = True
    return dp[-1]

# class Solution:
#     def wordBreak(self, s, wordDict) :
#         res = []
#
#         def dfs(wordDict, path):
#             if len(path) > len(s):
#                 return
#             if path == s:
#                 res.append(path)
#             if path not in s[0:len(path)]:
#                 return
#             # print("path:",path)
#             for i in range(0, len(wordDict)):
#                 if wordDict[i] not in s:
#                     continue
#                 if path not in s[0:len(path)]:
#                     continue
#                 if path + wordDict[i] not in s[0:len(path + wordDict[i])]:
#                     continue
#                 path = path + wordDict[i]
#                 dfs(wordDict, path)
#                 path = path[0:len(path) - len(wordDict[i])]
#
#         dfs(wordDict, '')
#         if len(res) > 0:
#             return True
#         return False
#
# s="bccdbacdbdacddabbaaaadababadad"
# # s="leetcode"
# wordDict=["cbc","bcda","adb","ddca","bad","bbb","dad","dac","ba","aa","bd","abab","bb","dbda","cb","caccc","d","dd","aadb","cc","b","bcc","bcd","cd","cbca","bbd","ddd","dabb","ab","acd","a","bbcc","cdcbd","cada","dbca","ac","abacd","cba","cdb","dbac","aada","cdcda","cdc","dbc","dbcb","bdb","ddbdd","cadaa","ddbc","babb"]
# # wordDict=["a","b","bbb","bbbb"]
# value=Solution().wordBreak(s=s, wordDict=wordDict)
# print(value)


#leetcode执行超时，本地执行没问题