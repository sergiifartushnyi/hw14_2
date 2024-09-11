class Student:
    def __init__(self, gender, age, first_name, last_name, student_id):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = student_id

    def __repr__(self):
        return f"Student({self.first_name} {self.last_name}, ID: {self.student_id}, Age: {self.age}, Gender: {self.gender})"

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.first_name == other.first_name and self.last_name == other.last_name
        return False
