class Group:
    def __init__(self, group_name):
        self.group_name = group_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def find_student(self, last_name):
        for student in self.students:
            if student.last_name == last_name:
                return student
        return None

    def delete_student(self, last_name):
        self.students = [student for student in self.students if student.last_name != last_name]

    def __repr__(self):
        return f"Group({self.group_name}): {self.students}"
