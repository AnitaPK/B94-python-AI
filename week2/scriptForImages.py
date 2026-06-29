import os
import shutil


sourceFolder = input("Enter folder name : ")

imagesFolder = sourceFolder + "/Images"

if not os.path.exists(sourceFolder):
    print("Folder not found .... ")
else:
    if not os.path.exists(imagesFolder):
        os.mkdir(imagesFolder)

    files = os.listdir(sourceFolder)

    for file in files:
        if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png"):
            
            sourcePath = sourceFolder +"/"+ file
            destinationPath = imagesFolder +"/"+ file
            shutil.move(sourcePath, destinationPath)
    print("Files succesfully Organized")
