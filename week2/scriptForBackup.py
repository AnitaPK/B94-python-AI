# os.path.exists()
# os.mkdir()
# os.listdir()
# shutil.copy()
import os
import shutil
from datetime import datetime

getFolderNameForBackup = input("Enter folder name to get backup : ")

backupFolder = "backup_" + datetime.now().date().strftime("%d-%m-%Y")

if not os.path.exists(getFolderNameForBackup):
    print("Folder does not exists...")
else:
    if not os.path.exists(backupFolder):
        os.mkdir(backupFolder)

    files = os.listdir(getFolderNameForBackup)

    for file in files:

        sourcePath=getFolderNameForBackup + "/" + file
        destinationPath=backupFolder + "/" + file

        shutil.copy(sourcePath, destinationPath)
    print("Backup Completed successfully")