def get_res(s):
    index_list=[]
    char_list=[]
    sum=0
    for i in range (0,len(s)):
        index_list.append(len(s)-1-i)
        char_list.append(ord(s[i])-ord('0'))
        sum=sum+char_list[i]*(10**index_list[i])
    return sum



print(get_res(s="23456"))