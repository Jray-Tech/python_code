student = {
    'name': 'Adejoke',
    'age': 23,
    'courses': ['math', 'yoruba', 'geophysics', 'french', 'chemistry']
}

print(student['age']
      )
print(student)
age = student.pop('age')
print(student)
print(age)
# so we can create pairs of key and values
# simply do this
# use the items
print(student.items())
# to loop throught them
for key, values in student.items():
    print(key, values)
# the major difference between lists and dics is that they are indexed differently
# lists are indexed by arranged orders like... 0-5
# Dictionaries are arranged by using something else by
# python is a great programming language
# it enables us to do so many things
# pycharm is a fucking good text editor

