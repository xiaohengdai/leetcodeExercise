#暴力解法
# class Solution:
#     def restoreIpAddresses(self, s) :
#         if (len(s) < 4) or (len(s) > 12):
#             return []
#         res = []
#         for first in range(0, 3):
#             for second in range(first + 1, 6):
#                 for third in range(second + 1, 9):
#                     s1 = s[0:first+1]
#                     s2 = s[first + 1:second+1]
#                     s3 = s[second + 1:third+1]
#                     s4 = s[third + 1:]
#                     if (len(s1)>0)and(len(s2)>0)and(len(s3)>0)and(len(s4)>0)and(s1 != '00') and (s1 != '000') and (s2 != '00') and (s2 != '000') and (s3 != '00') and (
#                             s3 != '000')and (s4 != '00') and (s4 != '000') and (int(s1) <= 255) and (int(s2) <= 255) and (int(s3) <= 255) and (int(s4) <= 255) \
#                             and (int(s1) >= 0) and (int(s2) >= 0) and (int(s3) >= 0) and (int(s4) >= 0):
#                         find_s = s1 + '.' + s2 + '.' + s3 + '.' + s4
#                         if ((len(s1)>1)and( s1.startswith('0')))or ((len(s2)>1)and( s2.startswith('0')))or((len(s3)>1)and( s3.startswith('0')))or((len(s4)>1)and( s4.startswith('0'))):
#                             continue
#                         if len(find_s) == len(s) + 3:
#                             res.append(s1 + '.' + s2 + '.' + s3 + '.' + s4)
#         return res



value=Solution().restoreIpAddresses(s='101023')
print("value:",value)