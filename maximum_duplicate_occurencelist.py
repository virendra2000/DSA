list = [1,2,3,1,2,4,1,5,3,1,5]
set = set(list)
print(set)
max_value=0
min_value=0
times=0
count=len(list)
for i in set:
    temp = list.count(i)
    if temp>times:
        times=temp
        max_value=i
    if temp<count:
        count=temp
        min_value=i
print(f"Maximum no of occurence is {max_value} which occur {times} time")
print(f"Minimum no of occurence is {min_value} which occur {count} time")
