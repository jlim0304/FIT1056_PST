# main.py - The View Layer
from app.schedule import ScheduleManager

def front_desk_daily_roster(manager, day):
    """Displays a pretty table of all lessons on a given day."""
    print(f"\n--- Daily Roster for {day} ---")
    # Notice: This code does not need to change. It doesn't care where the Course class lives.
    # It only talks to the manager.
    # Call a method on the manager to get the day's lessons and print them.
    roster = manager.get_daily_roster(day)
    if not roster:
        print("No lessons scheduled for this day.")
        return
    print(f"{'Time'} - " f"{'Course'} - " f"{'Instrument'} - " f"{'Room'}") 
    for lesson in roster: 
        print(f"{lesson['start_time']} - " f"{lesson['course_name']} - " f"{lesson['instrument']} - " f"{lesson['room']}")

def switch_course(manager, student_id, from_course_id, to_course_id):
    # Implement the logic to switch a student by calling methods on the manager.
    removed = manager.unenroll_student(student_id, from_course_id)
    if not removed:
        print("Error: Could not remove student from course.")
        return
    enrolled = manager.enroll_student(student_id, to_course_id)
    if not enrolled:
        print("Error: Could not enrol student to course.")
        return

    print(f"Success: Student {student_id} switched from course {from_course_id} to course {to_course_id}.")

def main():
    """Main function to run the MSMS application."""
    manager = ScheduleManager() # Create ONE instance of the application brain.
    
    while True:
        print("\n===== MSMS v3 (Object-Oriented) =====")
        # Create a menu for the new PST3 functions.
        print("1. View daily roster")
        print("2. Switch student course")
        print("3. Check in student")
        print("q. Quit")
        # Get user input and call the appropriate view function, passing 'manager' to it.
        choice = input("Enter choice: ")
        if choice == '1':
            day = input("Enter day (e.g., Monday): ")
            front_desk_daily_roster(manager, day)
        elif choice == "2":
            try: # Ensuring that program does not crash if there is an invalid input
                student_id = int(input("Enter student ID: "))
                from_course_id = int(input("Enter current course ID: "))
                to_course_id = int(input("Enter new course ID: "))
                switch_course(manager, student_id, from_course_id, to_course_id)
            except ValueError:
                print("Error: ID must be an integer")
        elif choice == "3":
            try:
                student_id = int(input("Enter student ID: "))
                course_id = int(input("Enter course ID: "))
                manager.check_in(student_id, course_id)
            except ValueError:
                print("Error: ID must be an integer")
        elif choice.lower() == 'q':
            print("Quitting...")
            break
        else:
            print("Invalid choice. Please try again.")
        
if __name__ == "__main__":
    main()
