#暴力解法：三重for循环对四段值分别判断是否在0到255范围内
# class Solution:
#     def restoreIpAddresses(self, s: str):
#         l=len(s)
#         if l>12 or l<4: return []
#         arr=[]
#         for i in range(1,min(4,l-2)):
#             for j in range(i+1,min(i+4,l-1)):
#                 for k in range(j+1,min(j+4,l)):
#                     if l-k>3: continue
#                     n=[s[:i],s[i:j],s[j:k],s[k:]]
#                     flag=False
#                     for c in n:
#                         if c[0]=='0' and c!='0':
#                             flag=True
#                             break
#                     if flag: continue
#                     # print(n)
#                     a,b,c,d=map(int,n)
#                     if 0<=a<=255 and 0<=b<=255 and 0<=c<=255 and 0<=d<=255:
#                         arr.append(str(a)+'.'+str(b)+'.'+str(c)+'.'+str(d))
#         return arr

#dfs
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        # 特殊情况处理
        if not s or len(s) < 4:
            return []
        # 初始化结果列表
        res = list()
        # DFS递归，需要传入字符串s，对s的分割次数（初始为0），划分的中间（最终）结果，最终结果列表res
        self.dfs(s, 0, '', res)
        # 返回结果列表
        return res

    # DFS递归，s为目标字符串，idx为对s的分割次数（也是递归深度），path为划分的中间（最终）结果字符串，res为结果列表
    def dfs(self, s: str, idx: int, path: str, res: List[str]):
        # 如果idx大于4，那么说明字符串s已经被分割的次数大于4，此时直接返回
        if idx > 4:
            return
            # 如果idx等于4，那么还要继续判断递归传入的s是否已经为空，如果s为空则说明字符串已经被完全分割为IP地址的形式，此时将该分割方法（路径）存储到结果列表res中，然后返回
        if idx == 4 and not s:
            # 这里符合条件的path的形式应该是"xxx.xxx.xxx.xxx."，因此path[:-1]是为了舍弃最后的'.'字符
            res.append(path[:-1])
            return
        # 对s的下标进行遍历
        for i in range(len(s)):
            # 后面的if语句用于处理以下两种情况：
            # （1）当s的首字符为'0'时，可以直接将'0'作为IP地址中四个整数之一
            # （2）当s的首字符不为'0'时，需要保证s[:i+1]处于IP地址整数的范围之内
            if s[:i + 1] == '0' or (s[0] != '0' and 0 < int(s[:i + 1]) < 256):
                # DFS递归调用的参数需要进行以下操作：
                # （1）将下标i之后的s[i+1:]字符串作为新的s进行递归参数传入
                # （2）分割次数idx+1
                # （3）将中间字符串结果path后连接下标i之前的s[:i+1]字符串，并在最后加入'.'
                # （4）结果列表res依然原封不动的传入下次递归
                self.dfs(s[i + 1:], idx + 1, path + s[:i + 1] + '.', res)


# 作者：hughtang
# 链接：https: // leetcode.cn / problems / restore - ip - addresses / solution / python - 24
# ms - zui - jian - jie - yi - dong - de - hui - esrwe /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。