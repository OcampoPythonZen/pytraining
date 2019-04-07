from collections import namedtuple,OrderedDict

Person = namedtuple('Person','id Name LastName age')
a_person = Person(id=14253083,Name='Edgar',LastName='Ocampo',age=32)
print(a_person) # I can acces them by index []  


# Next example with OrderedDict :: Order the dict in falling way

d = {'banana' : 3, 'apple' : 4, 'pear' : 1, 'orange' : 2}
new_d = OrderedDict(sorted(d.items()))
print(new_d)

for key in new_d:
    print(key,new_d[key])

# If I Wanna iter in reverse in upward way i have to do this.

for key in reversed(new_d):
    print(key,new_d[key])