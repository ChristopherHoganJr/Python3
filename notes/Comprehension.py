### List Comprehension
## Version 1
## new_list = [new_item for item in list]
## Version 2
## new_list = [new_item for item in list if test]
#Example #1
#numbers = [1,2,3]
#new_list = [n+1 for n in numbers]
#Example #2
# double_range = [i*2 for i in range(1,5) if i%2 == 0]

names = ['chris','sonja','nick','wendy','andy']
short_names = [i.upper() for i in names if len(i) == 5]
print(short_names)


### Dictionary Comprehension
## Version 1 from list
## new_dict = {new_key:new_value for item in list}
## Version 2 from list
## new_dict = {new_key:new_value for item in list if test}
## Version 1 from dictionary
## new_dict = {new_key:new_value for (key,value) in dict.items()}
## Version 2 from dictionary
## new_dict = {new_key:new_value for (key,value) in dict.items() if test}

import random

students_scores = {name:random.randint(0,100) for name in names}
print(students_scores)

passed_students = {student:score for (student, score) in students_scores.items() if score > 70}

print(passed_students)