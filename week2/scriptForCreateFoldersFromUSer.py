# Student Folder Generator

import os

studName = input("Enter Student name : ")

folders = ["Assigments", "Attendance","Projects","Certificates"]

if not os.path.exists(studName):
    os.mkdir(studName)

    for folder in folders:
        os.mkdir(studName+"/"+folder)

    print("Successfully created folders...")

else:
    print("Student folder already exist")