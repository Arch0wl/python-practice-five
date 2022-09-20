# task 3.1
my_list = ['a', 'b', [1, 2, 3], 'd']
# print only 1, 2, 3,
print(my_list[-2])
# we need to print with star to get just numbers
print(*my_list[-2])

# task 3.2

list_1 = ['Hi', 'ananas', 2, None, 77, 'pizza', 36, 100, 400, True, 12.9]
sum = 0
for i in list_1:
    if type(i) == int:
        print(type(i))
        sum += i
print("The sum of numbers in the list is ", sum)

# finding "a" in words:

for string in list_1:
    if type(string) == str:
        if string.find('a') !=-1:
            print(string)

# finding "z" in words:

for string in list_1:
    if type(string) == str:
        if string.find('z') !=-1:
            print(string)

# task 3.3

list_2 = ['cat', 'dog', 'horse', 'cow']
print(type(list_2))
print(list_2)
tpl = tuple(list_2)
print(type(tpl))
print(tpl)

#reverse

tpl = ('cat', 'dog', 'horse', 'cow')
print(type(tpl))
print(tpl)
lst = list(tpl)
print(type(lst))
print(lst)

# task 3.4

family_1 = input("Please provide the family names: \n").split(',')
family_2 = input("Please provide the family names: \n").split(',')
family_1_members = len(family_1)
family_2_members = len(family_2)

print(f"First famile has {family_1_members}  people.")
print(f"Second famile has {family_2_members}  people.")
if family_1_members > family_2_members:
    print("The first family is bigger")
elif family_2_members > family_1_members:
    print("The second family is bigger")
else:
    print("the families equal.")

# task 3.4-2

fam1 = input("family_1 : ")
fam2 = input("family_2 : ")
tuple1 = tuple(fam1.split(","))
tuple2 = tuple(fam2.split(","))

print(tuple1)
print(tuple2)

if len(tuple1) > len(tuple2):
    print(tuple1)
elif len(tuple2) > len(tuple1):
    print(tuple2)
else:
    print("Equal")

# task 3.5

film = {
    'title': 'The Godfather',
    'director': 'Francis Ford Coppola',
    'year': '1972',
    'budget': '$ 6,000, 000',
    'main actor': 'Richard Castellano',
}
for x in film:
    print(x)
    print(film[x])
    print(*film.values())
    print(*film.keys())

# task 3.6

my_dictionary = {'num1': 375, 'num2': 567, 'num3': -576 }
sum_dic = sum(my_dictionary)
print(sum_dic)

sum_dic = (sum(my_dictionary[item] for item in my_dictionary))
print(sum_dic)

# task 3.7
# delete similar numbers
list_3 = [1, 2, 4, 6, 7, 3, 5, 3, 1, 3, 4]
ints_list_4 = list(set(list_3))
print(*ints_list_4)

# task 3.8
set1 = {'a', 'b', 1, 2, 5, 14, 'v'}
set2 = {'x', 'b', 1, 552, 5, 's', 'd'}
print(set1 & set2)
print(set1 - set2)

dif_set = set1.difference(set2)
print(dif_set)

dif_set = set1.symmetric_difference(set2)
print(dif_set)

print(set1 <= set2)
print(set2.issubset(set1))