# new_dict = {new_key:new_value for item in list}
import random
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
student_scores = {
    "Alex":89,  # random generated
    "Beth":98,
# continue like this
}
student_score = {student:random.randint(1, 20) for student in names}
print(student_score)
