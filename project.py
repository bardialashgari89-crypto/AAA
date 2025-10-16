# chain
my_list = [1,2,3,4,5]
from itertools import chain
my_list = list(chain(my_list,[6,7,8,9]))
print(my_list)