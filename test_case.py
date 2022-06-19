class Solution:
    def letterCombinations(self, digits) :
        di = {"2": 'abc', "3": 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        if len(digits) == 0:
            return []
        combination = []
        combinations = []

        def backtrack(index):
            if index == len(digits):
                # print("combination:",combination)
                new_s=''
                for i in range (0,len(combination)):
                    new_s=new_s+combination[i]
                combinations.append(new_s)
                # combinations.append("".join(combination))
            else:
                digit = digits[index]
                for i in range(0, len(di[digit])):
                    combination.append(di[digit][i])
                    backtrack(index + 1)
                    combination.pop()

        backtrack(0)
        return combinations

res=Solution().letterCombinations(digits = "23")
print("res:",res)