# --- Data Models ---
class Student:
    """A blueprint for student objects. Holds their info."""
    def __init__(self, student_id, name):
        self.id = student_id # assign parameters to instance variables
        self.name = name
        self.enrolled_in = [] # creating empty list to store enrolment

class Teacher:
    """A blueprint for teacher objects. Holds their info"""
    def __init__(self, teacher_id, name, speciality):
        self.id = teacher_id # assign parameters to instance variables
        self.name = name
        self.speciality = speciality

# --- In-Memory Databases ---
student_db = [] # create global data stores
teacher_db = []
next_student_id = 1
next_teacher_id = 1