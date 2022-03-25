import datetime
import os

file_path = input("enter the file path: ")
delete_time = input("Type when file to be deleted(HH:MM:SS) in 24 hrs format: ")
print("Performing the operation....")
while True:
    date_and_time = datetime.datetime.now()
    time = date_and_time.strftime("%H:%M:%S")
    if time == delete_time:
        os.remove(file_path)
        print("Operation Successful!")
        break
    else:
        continue
