# my_list = [1,2,3,4]
# second_list = [5,6]
# print(*my_list,*second_list)

"insert"

# my_list = [1,2,3,4]
# my_list.insert(len(my_list),5)
# print(my_list)

"for"

# my_list = [1,2,3,4,5]
# for item in [6,7,8]:
#     my_list.append(item)
#     print(my_list)

"chain"

# from itertools import chain
# a = [1,2,3]
# b = [4,5,6]
# c = [7,8,9]
# combain = chain(a,b,c)
# print(list(combain))

"deque"

# from collections import deque
# dq = deque([1,2,3])
# dq_2 = deque([4,5,6])
# dq.extend(dq_2)
# print(dq)

"append"

# my_list = [1,2,3,4]
# my_list.append(5)
# print(my_list)

"extend"

# my_list = [1,2,3,4]
# my_list.extend([5,6,7,8])
# print(my_list)

"+="

# my_list = [1,2,3,4]
# my_list += [5,6]
# print(my_list)

"anpack"

# my_list = [1,2,3,4]
# my_list = [*my_list,5]
# print(my_list)



#                                   "new list"


"copy"
# lst = [1,2,3,4]
# new_list = lst.copy()
# new_list.append(5)
# print("orginal_list:",lst)
# print("New list:",new_list)


"unpak"
# my_list =[1,2,3,4]
# new_list = [*my_list,5,6]
# print(new_list)


"+"
# my_list =[1,2,3,4]
# new_list = my_list + [5,6]
# print(new_list)


"list"
# my_list =[1,2,3,4]
# new_list = list(my_list) + [5,6,7]
# print(new_list)


"itertools"
# import itertools
# lst = [1,2,3,4]
# new_list = list(itertools.chain(lst, [5,6,7]))
# print("orginal list:",lst)
# print("New list:",new_list)




