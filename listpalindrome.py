list = [1,3,2,3,1,2]
rev_list = []
for i in range(len(list)-1,-1,-1):
    rev_list.append(list[i])
    print(i)
if rev_list == list:
    print("Palindrome")
