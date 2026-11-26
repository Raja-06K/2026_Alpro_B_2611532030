students = input("students: ").split()
submit = input("submit: ").split()

set_students = set(students)
set_submit = set(submit)

not_submitted = set_students - set_submit

print("Submitted: " + str(len(set_submit)) + " students")
print("Not submitted: " + str(len(not_submitted)) + " students")

for not_submitted in set_students:
    print(not_submitted)