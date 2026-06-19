# student Record Manager 

# menu 
#  1. Add Student 
#  2. View Students
#  3. Exit 

def addNewStud():
    name = input("Enter student name : ")
    with open("studentInfo.txt", "a") as file:
        file.write(name+ "\n")
    print("student added successfully...")


def viewStudents():
    try:
        with open("studentInfo.txt", "r") as file: 
            students = file.readlines()
        if(len(students) == 0):
            print("No student")
        else:
            print("-------- Student Info --------")
            for i ,students in enumerate(students, start=1):
                print(f"{i}.  {students.strip()}")
    except FileNotFoundError: 
        print("No such file")

while True:
    print("===== student Record Manager =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter choice : ")

    if( choice == "1"):
        addNewStud()
    elif(choice == "2"):
        viewStudents()
    elif(choice == "3"):
        print("Thank you")
        break
    else:
        print("Invalid choice")