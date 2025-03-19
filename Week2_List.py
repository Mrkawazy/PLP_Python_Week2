#1. Creating empty list
my_list=[]
#2. append values into my_list List
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(f'My List after appending values: {my_list}')
#3. insert 15 at the second position
my_list.insert(2,15)
print(f'List inserted 15 on the second position: {my_list}')
another_list=[50,60,70]
#4. extend the list "my_list" with "another_list"
my_list.extend(another_list)
print(f'Extended list {my_list}')
#5. remove last element from the list "my_list"
my_list.remove(my_list[-1])
print(f'List with removed last value: {my_list}')
#6. Sorting my_list in ascending order
my_list.sort(reverse=False)
print(f'List sorted in ascending order: {my_list}')
#7. Printing the index of the value 30 in my_list
print(f'The index value of 30 is: {my_list.index(30)}')