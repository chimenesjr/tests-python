students = []

class Student:

    school_name = 'Leoncio Correia'

    def __init__(self, name, id=332):
        self.name = name
        self.id = id
        students.append(self)

    def __str__(self):
        return 'Student ' + self.name

    def get_name_capitalize(self):
        return self.name.capitalize()

    def get_school_name(self):
        return self.school_name




# mark = Student('John', 11)
# # student.add_student('Mark')

# print(mark.school_name)
# print(mark.get_school_name())
# print(Student.school_name)

