class Solution:
    def longestPalindrome(self, s):
        s_len = len(s)
        if len(s) < 2:
            return s
        dp = [[False] * s_len for i in range(0, s_len)]
        for i in range(0, s_len):
            dp[i][i] = True
        max_len = 1
        begin = 0
        for L in range(2, s_len + 1):
            for i in range(0, s_len):
                j = L +i -1
                if j>= s_len:
                    continue
                # print("i:",i)
                # print("j:",j)
                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    if j - i <= 2:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                if dp[i][j] and (j - i + 1) > max_len:
                    max_len = j - i + 1
                    begin = i
        return s[begin:max_len + begin]






