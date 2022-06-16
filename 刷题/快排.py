def quick_sort(lst):  #O(nlogn)，用 Python 实现十大经典排序算法：https://blog.csdn.net/dQCFKyQDXYm3F8rB0/article/details/123390733
    n=len(lst)
    if n<=1:
        return lst

    baseline=lst[0]
    left=[]
    right=[]
    for i in range(1,len(lst)):
        if lst[i]<baseline:
            left.append(lst[i])
    for j in range(1,len(lst)):
        if lst[j]>=baseline:
            right.append(lst[j])
    # print("left0:", left)
    # print("right0:", right)
    # left = [lst[i] for i in range(1, len(lst)) if lst[i] < baseline]
    # print("left1:",left)
    # right = [lst[i] for i in range(1, len(lst)) if lst[i] >= baseline]
    # print("right1:", right)
    return quick_sort(left)+[baseline]+quick_sort(right)

li=[10,11,13,18,15,17,21,16,25]
li=quick_sort(li)
print("li:",li)