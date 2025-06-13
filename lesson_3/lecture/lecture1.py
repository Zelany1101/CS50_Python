# common convention is to use a while loop to validate the input of the user

#dictionaries
students = {
    'Hermoine':'Gryffindor',
    'Harry' : 'Gryffindor',
    'Ron' : 'Gryffindor',
    'Draco' : 'Slytherin',
}

for student in students:
    print(student, students[student], sep=", ")
