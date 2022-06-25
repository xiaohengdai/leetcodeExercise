class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        const_value0="Neither"
        const_value1="IPv4"
        const_value2="IPv6"
        if len(queryIP)==0:
            return const_value0
        if '.' in queryIP:#进行ipv4的验证逻辑判断
            str_li=queryIP.split(".")
            # print("str_li:",str_li)
            if len(str_li)!=4:
                return const_value0
            for i in range (0,len(str_li)):
                if not str_li[i].isdigit():
                    return const_value0
                if len(str_li[i])==0:
                    return const_value0
                if (len(str_li[i])>1) and (str_li[i][0])=='0':
                    return const_value0
                if (int(str_li[i])>255):
                    return const_value0

            return const_value1
        else:
            if ':' in queryIP: #进行ipv6的验证逻辑判断
                str_li = queryIP.split(":")
                if len(str_li) != 8:
                    return const_value0
                else:
                    for i in range(0, len(str_li)):

                        if (len(str_li[i]) == 0) or (len(str_li[i]) > 4):
                            return const_value0
                        if not str_li[i].isalnum():
                            return const_value0
                        for j in range (0,len(str_li[i])):
                            # print("str_li[i]:",str_li[i])
                            # print("str_li[i][j]:", str_li[i][j])
                            if (str_li[i][j].isalpha()) and (str_li[i][j].lower()>'f'):
                                return const_value0
                    return const_value2


            else:
                return const_value0


res=Solution().validIPAddress(queryIP="2001:0db8:85a3:00000:0:8A2E:0370:7334")
print("res:",res)