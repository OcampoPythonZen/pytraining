a_list = [1,2,3,4,5]

res = 0

for i in a_list:
    res += i

print(res-a_list[-1])
print(res-a_list[0])

print(res-max(a_list),res-min(a_list))