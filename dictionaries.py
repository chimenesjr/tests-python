all = [
    {'name': 'Mark', 'id': 1},
    {'name': 'Katarina', 'id': 2}
]

print(all[0]['name'])

print(all[0].get('last-name', 'Unknown'))

student = all[1]

print(student.keys())
print(student.values())

del student['name']
print(student.values())