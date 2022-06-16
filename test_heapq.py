import heapq

array=[10,17,50,7,30,24,27,45,15,5,36,21]
heap=[]
for num in range(0,len(array)):
    heapq.heappush(heap,array[num])

print("array:",array)
print("heap:",heap)

large_data=heapq.nlargest(2,array)
print("large_data:",large_data)
small_data=heapq.nsmallest(3,array)
print("small_data:",small_data)

