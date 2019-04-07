list_ = ['a','b','c',1,2,3,4,5,'John']
numbers = []
letters = []

letters = [e for e in list_ if str(e).isalpha() == True]
numbers = [e for e in list_ if str(e).isdigit() == True]

print(letters)
print(numbers)