# gui/student_pages.py
import streamlit as st

def show_student_management_page(manager):
    """Renders all components for the student management page."""
    st.header("Student Management")

    # --- Search Section (remains the same) ---
    st.subheader("Find a Student")
    # ...
    with st.form("student_search_form"):
        search_term = st.text_input("Enter Student ID or Name")
        search_submitted = st.form_submit_button("Search")

        if search_submitted:
            search_term = search_term.strip()
            if search_term:
                matching_students = []

                for student in manager.students: # search for id or name match
                    if (str(student.id) == search_term or search_term.lower() in student.name.lower()):
                        matching_students.append(student)

                if matching_students:
                    for student in matching_students:
                        st.write(f"### {student.name}")
                        st.write(f"**Student ID:** {student.id}")

                        st.write("**Enrolled Courses:**")

                        if student.enrolled_course_ids:
                            for course_id in student.enrolled_course_ids:
                                course = manager.find_course_by_id(course_id)

                                if course:
                                    st.write(f"{course.name}")
                                else:
                                    st.write(f"Course ID {course_id} " f"(course not found)")
                        else:
                            st.write("No courses enrolled.")
                else:
                    st.warning("No student found matching search.")
            else:
                st.warning("Please enter a student ID or name.")

    # --- Registration Section (now works correctly) ---
    st.subheader("Register New Student")
    with st.form("registration_form"):
        reg_name = st.text_input("New Student Name")
        reg_course = st.text_input("First Course")
        submitted = st.form_submit_button("Register Student")
        
        if submitted:
            # This call now works because we implemented the method in PST3.
            # Add a check for blank name/instrument.
            if reg_name and reg_course:
                new_student = manager.register_new_student(reg_name, reg_course)
                if new_student:
                    st.success(f"Successfully registered {reg_name}!")
                    # You can use st.balloons() for extra flair.
                else:
                    st.error(f"Could not register student. A teacher for {reg_course} might not be available.")
            else:
                st.warning("Please enter both a name and an instrument.")
