def ending():
    input("Press enter to exit the program.")
    exit()


try:
    import datetime
    import os
    import shutil
    import time

    print("Select what you want to do:")
    time.sleep(0.25)
    print("1. Delete a file")
    print("2. Delete a folder")
    time.sleep(0.5)
    selection = input("Enter your choice: ")

    """try:
        int(selection)
    except ValueError:
        print("you have to enter either 1 or 2 only.")
        ending()"""

    if selection == "1":
        file_path = input("enter the file path: ")
        delete_time = input("Type when file to be deleted(HH:MM:SS) in 24 hrs format: ")
        print("Performing the operation....")
        while True:
            date_and_time = datetime.datetime.now()
            time = date_and_time.strftime("%H:%M:%S")
            if time == delete_time:
                try:
                    os.unlink(file_path)
                    print("Operation Successful!")
                except FileNotFoundError:
                    print("The file path that has been entered is invalid. Please enter a valid file path and try "
                          "again.")
                except PermissionError:
                    print("You don't have sufficient rights to perform this operation.")
                finally:
                    break
            else:
                continue

    elif selection == "2":
        folder_path = input("enter the folder path: ")
        delete_time = input("Type when file to be deleted(HH:MM:SS) in 24 hrs format: ")
        print("Performing the operation....")
        while True:
            date_and_time = datetime.datetime.now()
            time = date_and_time.strftime("%H:%M:%S")
            if time == delete_time:
                try:
                    shutil.rmtree(folder_path)
                    print("Operation Successful.")
                except FileNotFoundError:
                    print("The folder doesn't exist in the path provided. Please check the path once again")
                except PermissionError:
                    print("You don't have sufficient rights to perform this action.")
                finally:
                    break
    else:
        print("you have to enter either 1 or 2 only.")
    ending()
except KeyboardInterrupt:
    print("Action was interrupted.")
    ending()
