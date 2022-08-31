# Code related to Question 2

dogs={'name': 'Tony', 'color': 'black', 'breed': 'Boxer', 'legs': '4', 'age':'4'}
student={'first_name':'Deviprasad', 'last_name':'Kajekar Pade',  'gender':'Male', 'age':'28', 'marital_status':'Single',
'skills':['Communication','Programming','Time management'], 'country':'United States', 'city':'Kansas' , 'address':'127th Steet Grandview'}

print("Length of student dictionary is: ", len(student))
print("Students skills are - ",student.get('skills'),". Data Type is", type(student.get('skills')))
student.get('skills').append('Acting')
student.get('skills').append('Collaboration')
print("Skills after modification- ", student.get('skills'))
print("\n**************** Displaying keys ****************")
print(" Dog's - ",dogs.keys())
print(" Students - ",student.keys())

print("\n**************** Displaying Values ****************")
print(" Dog's - ",dogs.values())
print(" Students - ",student.values())

