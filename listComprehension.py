# numbers = [1,2,3,4,5,6,7,8,9,10]

# my_list = [n for n in numbers if n%2 == 0]
# print(my_list)

# filter_lambda = list(filter(lambda n : n%2 == 0, numbers))
# print(filter_lambda)

# power = [n**2 for n in numbers if n%2 == 0]
# print(power)

x = int(input())
y = int(input()) 
z = int(input())
n = int(input())

print([[a,b,c] for a in range(x+1)
               for b in range(y+1)
               for c in range(z+1) if(a+b+c != n)])

