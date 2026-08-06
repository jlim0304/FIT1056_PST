# --- Data Models --- fragment 1
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

# --- Core Helper Functions --- fragment 2
def add_teacher(name, speciality):
    """Creates a Teacher object and adds it to the database."""
    global next_teacher_id
    new_teacher = Teacher(next_teacher_id, name, speciality) # creating a new Teacher object using the next available ID.
    teacher_db.append(new_teacher) # appending the new_teacher to the teacher_db list.
    next_teacher_id += 1 # incrementing the next_teacher_id counter.
    print(f"Core: Teacher '{name}' added successfully.")

def list_students():
    """Prints all students in the database."""
    print("\n--- Student List ---")
    if not student_db:
        print("No students in the system.")
        return
    for student in student_db: # looping through student_db and printing each student's ID, name, and enrolled_in list.
        print(f"  ID: {student.id}, Name: {student.name}, Enrolled in: {student.enrolled_in}")

def list_teachers():
    """Prints all teachers in the database."""
    print("\n--- Teacher List ---")
    if not teacher_db:
        print("No teachers in the system.")
        return
    for teacher in teacher_db:
        print(f"  ID: {teacher.id}, Name: {teacher.name}, Speciality: {teacher.speciality}")

def find_students(term):
    """Finds students by name."""
    print(f"\n--- Finding Students matching '{term}' ---")
    matching_students = []
    for student in student_db:
        if term.lower() in student.name.lower(): # checking for case insensitive matches in name
            matching_students.append(student)
    if len(matching_students) == 0: # checking if any students are in the results list
        print("No match found.")
    else:
        for mstudent in matching_students: # printing details for each student in results list
            print(f"  ID: {mstudent.id}, Name: {mstudent.name}, Enrolled in: {mstudent.enrolled_in}")

def find_teachers(term):
    """Finds teachers by name or speciality."""
    print(f"\n--- Finding Teachers matching '{term}' ---")
    matching_teachers = []
    for teacher in teacher_db:
        if term.lower() in teacher.name.lower() or term.lower() in teacher.speciality.lower(): # checking for case insensitive matches in name and speciality
            matching_teachers.append(teacher)
    if len(matching_teachers) == 0:
        print("No match found.")
    else:
        for mteacher in matching_teachers:
            print(f"  ID: {mteacher.id}, Name: {mteacher.name}, Speciality: {mteacher.speciality}")

# --- Front Desk Functions --- fragment 3
def find_student_by_id(student_id):
    """A new helper to find one student by their exact ID."""
    for student in student_db: # loops through student_db. If a student's ID matches student_id, returns the student object.
        if student.id == student_id:
            return student
    return None # if the loop finishes without finding a match, return None.

def front_desk_register(name, instrument):
    """High-level function to register a new student and enrol them."""
    global next_student_id
    new_student = Student(next_student_id, name) # creates a new Student object, adds it to student_db, and increments the ID.
    student_db.append(new_student)
    next_student_id += 1
    
    # Immediately call front_desk_enrol() using the new student's ID and the provided instrument.
    front_desk_enrol(new_student.id, instrument)
    print(f"Front Desk: Successfully registered '{name}' and enrolled them in '{instrument}'.")

def front_desk_enrol(student_id, instrument):
    """High-level function to enrol an existing student in a course."""
    student = find_student_by_id(student_id)
    if student: # if the student is found, append the instrument to their 'enrolled_in' list.
        student.enrolled_in.append(instrument)
        print(f"Front Desk: Enrolled student {student_id} in '{instrument}'.")
    else:
        print(f"Error: Student ID {student_id} not found.") # if the student is not found, print an error message

def front_desk_lookup(term):
    """High-level function to search everything."""
    print(f"\n--- Performing lookup for '{term}' ---")
    find_students(term) # calling both previous helper functions
    find_teachers(term)