students = []

def read_file():
    try:
        f = open("students.txt", "r")
        for student in read_students(f):
            students.append(student)
        f.close()
    except Exception as ex:
        print("Could not read file" + ex)

def read_students(f):
    for line in f:
        yield line


read_file()
print(students)