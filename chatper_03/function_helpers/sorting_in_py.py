# sort() method   = used with lists
# sort() function = used with iterables


# students = ['Squidward', 'Sandy', 'Patrick', 'Spongebob', 'Mr.Krabs']
# tuple_students = tuple(students)
#
# # students.sort(reverse=True)
# sorted_students = sorted(tuple_students, reverse=True)
#
# for i in sorted_students:
#     print(i)


# ===================lvl_2

students = (
    ('Squidward', 'F', 60),
    ('Sandy', 'A', 33),
    ('Patrick', 'D', 36),
    ('Spongebob', 'B', 20),
    ('Mr.Krabs', 'C', 78),
)

grade = lambda grades: grades[1]
age = lambda obj: obj[2]
# students.sort(key=age, reverse=True)
sorted_students = sorted(students, key=age)

for i in sorted_students:
    print(i)
