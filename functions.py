def alert():
    print("txt 2")

def test():
teste = 0
print(int(teste) == 0)
print(bool(teste) == False)
print(str(teste) == None)
print(str(teste) is None and teste)

a = 3
b = 2
if a > b:
    print('bigger')
else:
    print('smaller')
print('bigger' if a > b else 'smaller')

students = ["carlos", 'roberto', 'chimenes']
print(students[1])
students.append('JUNIOR')
print(students[-2])
students[-4] = 'xuxu'
print(students[-4])
print('JUNIOR' in students)

students = ["carlos", 'roberto', 'chimenes']
print(len(students))
del students[2]
print(students.__len__())


students = ["carlos", 'roberto', 'chimenes', 'junior']
print(students[1:-1])
print(students[2:])
print(students.pop())
print(students.pop())

students = ["carlos", 'roberto', 'chimenes', 'junior']
for item in students:
    print('My name is {0}'.format(item))
    print(f"bla bla {item}")

item = 'test'
print(f"bla bla {item}")



