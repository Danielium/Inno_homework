# Напишите программу, которая превратит список списков в одноуровневый список,
# где все элементы предыдущего списка идут в том же порядке.


list_of_lists = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]

single_level_list = []
for i in range(len(list_of_lists)):
    single_level_list.extend(list_of_lists[i])

print(single_level_list)