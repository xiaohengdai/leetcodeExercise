import collections

c=collections.Counter('helloworld')

print("c:",c)

#默认获取前n个最高的元素
print("c.most_common(3):",c.most_common(3))
print(type(c.most_common(3)))
#获取前k个最低的元素
print("前k个最低的元素:",c.most_common()[:-4:-1])
