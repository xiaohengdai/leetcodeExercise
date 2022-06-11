A=[1,3,5,6,7,4,3,2,1]



# print(max(A))

def get_res(li):
    li_max_value = max(li)
    li_max_index = li.index(li_max_value)
    print("li_max_index:", li_max_index)
    li1=li[0:li_max_index+1]
    print("li1:",li1)
    li2=li[li_max_index+1:]
    li2.reverse()
    print("li2:",li2)
    point1=0
    point2=0
    new_li=[]
    while (point1<len(li1)) and (point2<len(li2)):
        if li1[point1]<li2[point2]:
            new_li.append(li1[point1])
            point1=point1+1
        elif li1[point1]>li2[point2]:
            new_li.append(li2[point2])
            point2=point2+1

        else:
            new_li.append(li1[point1])
            point1=point1+1
            point2=point2+1

    print("new_li:",new_li)
    print("point1:",point1)
    print("point2:", point2)
    if point1==len(li1):
        for k in range (point2,len(li2)):
            new_li.append(li2[k])
    elif point2==len(li2):
        for k in range (point1,len(li1)):
            new_li.append(li[k])
    return new_li



res=get_res(A)
print("res:",res)