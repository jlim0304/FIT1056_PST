# pst2_main.py - The Persistent Application - fragment 1

import json
import datetime

DATA_FILE = "msms.json"
app_data = {} # This global dictionary will hold ALL our data.

# --- Core Persistence Engine ---
def load_data(path=DATA_FILE):
    """Loads all application data from a JSON file."""
    global app_data
    try:
        with open(path, 'r') as f:
            # Use json.load(f) to load the file's content into the global 'app_data' variable.
            app_data = json.load(f)
            print("Data loaded successfully.")
    except FileNotFoundError:
        print("Data file not found. Initializing with default structure.")
        # If the file doesn't exist, initialize 'app_data' with a default dictionary.
        # It should have keys like: "students", "teachers", "attendance", "next_student_id", "next_teacher_id".
        # The lists should be empty and the IDs should start at 1.
        app_data = {
            "students": [],
            "teachers": [],
            "attendance": [],
            "next_student_id": 1,
            "next_teacher_id": 1
        }

def save_data(path=DATA_FILE):
    """Saves all application data to a JSON file."""
    # Open the file at 'path' in write mode ('w').
    # Use json.dump() to write the global 'app_data' dictionary to the file.
    # Use the 'indent=4' argument in json.dump() to make the file readable.
    with open(path, 'w') as f:
        json.dump(app_data, f, indent=4)
    print("Data saved successfully.")

# --- Full CRUD for Core Data --- fragment 2
# Note: We are now working with lists of dictionaries, not lists of objects.

def add_teacher(name, speciality):
    """Adds a teacher dictionary to the data store."""
    teacher_id = app_data['next_teacher_id'] # Get the next teacher ID from app_data['next_teacher_id'].
    new_teacher = {"id": teacher_id, "name": name, "speciality": speciality} # Create a new teacher dictionary with 'id', 'name', and 'speciality' keys.
    app_data['teachers'].append(new_teacher) # Append the new dictionary to the app_data['teachers'] list.
    app_data['next_teacher_id'] += 1 # Increment the 'next_teacher_id' in app_data.
    print(f"Core: Teacher '{name}' added.")

def update_teacher(teacher_id, **fields):
    """Finds a teacher by ID and updates their data with provided fields."""
    for teacher in app_data['teachers']: # Loop through the app_data['teachers'] list.
        if teacher['id'] == teacher_id: # If a teacher's 'id' matches teacher_id:
            teacher.update(fields) # Use the .update() method on the teacher dictionary to apply the 'fields'.
            print(f"Teacher {teacher_id} updated.")
            return
    print(f"Error: Teacher with ID {teacher_id} not found.")

def remove_teacher(teacher_id):
    """Removes a teacher from the data store."""
    for teacher in app_data['teachers']: # Loop through the app_data['teachers'] list.
        if teacher['id'] == teacher_id: # If a teacher's 'id' matches teacher_id:
            app_data['teachers'].remove(teacher) # Use the .remove() method on the list to remove the teacher dictionary.
            print(f"Teacher {teacher_id} removed.")
            return
    print(f"Error: Teacher with ID {teacher_id} not found.")

def add_student(name, instrument):
    """Adds a student dictionary to the data store."""
    student_id = app_data['next_student_id'] # Get the next student ID from app_data['next_student_id'].
    new_student = {"id": student_id, "name": name, "enrolled_in": instrument} # Create a new student dictionary with 'id', 'name', and 'instrument' keys.
    app_data['students'].append(new_student) # Append the new dictionary to the app_data['students'] list.
    app_data['next_student_id'] += 1 # Increment the 'next_student_id' in app_data.
    print(f"Core: Student '{name}' added.")

def update_student(student_id, **fields):
    """Finds a student by ID and updates their data with provided fields."""
    for student in app_data['students']: # Loop through the app_data['student'] list.
        if student['id'] == student_id: # If a student's 'id' matches student_id:
            student.update(fields) # Use the .update() method on the student dictionary to apply the 'fields'.
            print(f"Student {student_id} updated.")
            return
    print(f"Error: Student with ID {student_id} not found.")

def remove_student(student_id):
    """Removes a student from the data store."""
    # Find the student dictionary in app_data['students'] with the matching ID.
    # If found, use the .remove() method on the list to delete it.
    # A list comprehension is a clean way to do this:
    # app_data['students'] = [s for s in app_data['students'] if s['id'] != student_id]
    for student in app_data['students']: # Loop through the app_data['students'] list.
        if student['id'] == student_id: # If a student's 'id' matches student_id:
            app_data['students'].remove(student) # Use the .remove() method on the list to remove the student dictionary.
            print(f"Student {student_id} removed.")
            return
    print(f"Error: Student with ID {student_id} not found.")

# --- New Receptionist Features --- fragment 3
def check_in(student_id, course_id, timestamp=None):
    """Records a student's attendance for a course."""
    if timestamp is None:
        # Get the current time as a string using datetime.datetime.now().isoformat()
        timestamp = datetime.datetime.now().isoformat()
    
    # Create a check-in record dictionary.
    # It should contain 'student_id', 'course_id', and 'timestamp'.
    check_in_record = {
        "student_id": student_id,
        "course_id": course_id,
        "timestamp": timestamp
    }
    # Append this new record to the app_data['attendance'] list.
    app_data['attendance'].append(check_in_record)
    print(f"Receptionist: Student {student_id} checked into {course_id}.")

def print_student_card(student_id):
    """Creates a text file badge for a student."""
    # Find the student dictionary in app_data['students'].
    student_to_print = None
    for s in app_data['students']:
        if s['id'] == student_id:
            student_to_print = s
            break
    
    if student_to_print:
        # Create a filename, e.g., f"{student_id}_card.txt".
        filename = f"{student_id}_card.txt"
        # Open the file in write mode ('w').
        with open(filename, 'w') as f:
            # Write the student's details to the file in a nice format.
            f.write("========================\n")
            f.write(f"  MUSIC SCHOOL ID BADGE\n")
            f.write("========================\n")
            f.write(f"ID: {student_to_print['id']}\n")
            f.write(f"Name: {student_to_print['name']}\n")
            f.write(f"Enrolled In: {', '.join(student_to_print.get('enrolled_in', []))}\n")
        print(f"Printed student card to {filename}.")
    else:
        print(f"Error: Could not print card, student {student_id} not found.")

# --- Main Application Loop --- fragment 4
def main():
    """Main function to run the MSMS application."""
    load_data() # Load all data from file at startup.

    while True:
        print("\n===== MSMS v2 (Persistent) =====")
        print("1. Check-in Student")
        print("2. Print Student Card")
        print("3. Add Teacher")
        print("4. Add Student")
        print("5. Update Teacher Info")
        print("6. Update Student Info")
        print("7. Remove Teacher")
        print("8. Remove Student")
        print("q. Quit and Save")
        
        choice = input("Enter your choice: ")
        
        made_change = False # A flag to track if we need to save
        try: 
            if choice == '1':
                # Get student_id and course_id from user, then call check_in().
                student_id = int(input("Enter student id: "))
                course_id = int(input("Enter course id: "))
                check_in(student_id,course_id)
                made_change = True
            elif choice == '2':
                # Get student_id, then call print_student_card().
                student_id = int(input("Enter student id: "))
                print_student_card(student_id)
                # No change made, so no save needed
            elif choice == '3':
                teacher_name = input("Enter teacher name: ")
                teacher_speciality = input("Enter teacher speciality: ")
                add_teacher(teacher_name, teacher_speciality)
                made_change = True
            elif choice == '4':
                student_name = input("Enter student name: ")
                student_instrument = input("Enter student instruments (seperated by commas): ")
                student_instrument = [instr.strip() for instr in student_instrument.split(",")]
                add_student(student_name, student_instrument)
                made_change = True
            elif choice == '5':
                # Get teacher_id and new details, then call update_teacher().
                # Example: update_teacher(1, speciality="Advanced Piano")
                teacher_id = int(input("Enter teacher id: "))
                fields = input("Enter teacher fields: ")
                update_teacher(teacher_id, speciality=fields)
                made_change = True
            elif choice == '6':
                # Get student_id and new details, then call update_student().
                student_id = int(input("Enter student id: "))
                fields = input("Enter student fields: ")
                update_student(student_id, enrolled_in=fields)
                made_change = True
            elif choice == '7':
                # Get teacher_id, then call remove_teacher().
                teacher_id = int(input("Enter teacher id: "))
                remove_teacher(teacher_id)
                made_change = True
            elif choice == '8':
                # Get student_id, then call remove_student().
                student_id = int(input("Enter student id: "))
                remove_student(student_id)
                made_change = True
            elif choice.lower() == 'q':
                print("Saving final changes and exiting.")
                break
            else:
                print("Invalid choice.")
        except ValueError:
            print("Invalid ID, must be an integer")
        if made_change:
            save_data() # Save the data immediately after any change.

    save_data() # One final save on exit.

# --- Program Start ---
if __name__ == "__main__":
    main()
