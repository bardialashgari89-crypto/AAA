# project 1


import datetime


def make_backup(data):
     backup_data=data.copy()
     backup_time=datetime.datetime.now().strftime("%Y_%m_%d %H:%M:%S")
     return backup_data,backup_time




grades=[12,13,3,17,13.25,14,20,20,19]
print("20 repeted many times? :",grades.count(20))
print("20 repeted many times? :",grades.count(13))
print("20 repeted many times? :",grades.count(0))



grades.sort()
print("Ascending list grades : ",grades)



grades.sort(reverse=True)
print("descending list grades :",grades)



grades.append(13.13)
backup = make_backup(grades)
grades.append(17.17)
backup =make_backup(grades)
print("main list : ",grades)        
print("back up list :",backup)
