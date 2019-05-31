students = []

def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase.append(student['name'].title())
    return students_titlecase

def print_students_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)

def add_student(name, id=332):
    student = {'name': name, 'student_id': id}
    students.append(student)

def save_file(student):
    try:
        f = open('students.txt', 'a')
        f.write(student + '\n')
        f.close()
    except Exception as ex:
        print(f"Could not save {ex}")

def read_file():
    try:
        f = open("students.txt", "r")
        for student in f.readlines():
            add_student(student)
        f.close()
    except Exception as ex:
        print("Could not read file" + ex)

read_file()
print_students_titlecase()


name = input('Enter student name: ')
student_id = input('Enter student id: ')

student = add_student(name, student_id)
save_file(name)