def binary_search(alist,item):  #O(logn)，Python二分搜索算法：https://blog.csdn.net/qq_39276337/article/details/121868627
    start=0
    end=len(alist)-1

    while start<=end:
        mid=(start+end)//2  #向下取整,(应该是对除以b的结果向负无穷方向取整后的数）
        if item==alist[mid]:
            return mid
        elif item<alist[mid]:
            end=mid-1
        elif item>alist[mid]:
            start=mid+1
res=binary_search(alist=[0,1,2],item=0)
print(res)