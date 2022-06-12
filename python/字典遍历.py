# a={'a': '1'}

# b={'a': '1', 'b': '2', 'c': '3'}
# c=['a','b']
# print(a==b)
# print("c" in c)
# b=list(set(a))
# print("b[0]:",b[0])
# print('a' in a.keys())
# print("b:",b)
# print('d' in b)
# for key in a.keys():
#     print("key:",key)
#     print("a[key]:",a[key])
#
# for value in a.values():
#     print(value)
#
# for key,value in a.items():
#     print("key:",key)
#     print("value:",value)
# if 'a' in a.keys():
#     print(True)
# else:
#     print(False)
#删除其中一个key
# a={'c':2}
# print(len(a))
# print(a)
# a.pop('c')
# print(a)
#
# for key in a:
#     print(key)


#对字典中的key排序
dict_data={6:9,10:5,3:11,8:2,7:6}

# keys0=dict_data.keys()
# print("keys0:",keys0)
# test_data_0=sorted(keys0)
# print("test_data_0:",test_data_0)


#对字典中的value排序
value0=dict_data.values()
print("value0:",value0)
test_data_0=sorted(value0)
print("test_data_0:",test_data_0)

