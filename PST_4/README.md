Run the command "streamlit run main.py" in the terminal to start.  
When running the program, it will first check for a database "msms.json" file in the data folder to read from. If not found, it will create an empty default file to write to.  
  
A navigation bar is available on the left side of the screen which will change the page.  

The program will open to the Student Management page on launch.  
At the top of the page is the "Find a Student" input box. Entering a student ID or any part of a student name, and then pressing search, will display the names, IDs and courses of all applicable students. If no matching students are found, the message "No student found matching search." will be provided.  
The "Register New Student" input box is below. Entering both a student's name and an available course will enter their details into the database file.  
  
On the Daily Roster page, a dropdown menu of every day of the week is provided. The roster of courses and their details will be provided based on the day selected.  
The "Student Check-in" input box is provided below. There is one dropdown menu for selecting the student and one for selecting the course. After selecting both, pressing the "Check-in Student" button will add the record to the database file with the current time.  
