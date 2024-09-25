print("Welcome To Employee Management System...")


def fetch_employee(name):
    file_name = name + ".txt"
    try:
        file = open(file_name, "r")
        data = file.readlines()
        file.close()
        return data
    except FileNotFoundError:
        print("Employee not found.")
        return None


def update_employee(name):
    file_name = name + ".txt"
    try:
        file = open(file_name, "r+")
        data = file.readlines()
        file.seek(0)
        for line in data:
            if "Age :" in line:
                while True:
                    try:
                        age = int(input("Enter new Age : "))
                        file.write("Age : " + str(age) + "\n")
                        break
                    except ValueError:
                        print("Invalid Age Input. Please enter a number.")
            elif "Post :" in line:
                while True:
                    post = str(input("Enter new Post :"))
                    if post.casefold() == "Manager".casefold() or post.casefold() == "Employee".casefold():
                        file.write("Post : " + post + "\n")
                        break
                    else:
                        print("Invalid post. Please enter 'Manager' or 'Employee'.")
            elif "Mobile Number :" in line:
                while True:
                    mobile_no = input("Enter new Mobile Number : ")
                    if mobile_no.isdigit() and len(mobile_no) == 10:
                        file.write("Mobile Number : " + mobile_no + "\n")
                        break
                    else:
                        print("Enter a valid mobile number. It should be 10 digits.")
            elif "Email :" in line:
                while True:
                    email = str(input("Enter new Email : "))
                    if (email.__contains__("@gmail.com")):
                        file.write("Email : " + email + "\n")
                        break
                    else:
                        print("Please Enter Valid Email (Example : xyz@gmail.com)")
            else:
                file.write(line)
        file.truncate()
        file.close()
    except FileNotFoundError:
        print("Employee not found.")
    except IOError:
        print("Error reading or writing to file.")
    except Exception as e:
        print("An error occurred: ", str(e))


def delete_employee(name):
    file_name = name + ".txt"
    try:
        import os
        os.remove(file_name)
    except FileNotFoundError:
        print("Employee not found.")
    except IOError:
        print("Error deleting file.")
    except Exception as e:
        print("An error occurred: ", str(e))


while True:
    try:
        print("1.Add Employee\n2.Update Employee\n3.Delete Employee\n4.View All Employee")
        choice = int(input("Enter Your Choice : "))
        match choice:
            case 1:
                name = str(input("Enter Your Name : "))
                file_name = name + ".txt"
                file = open(file_name, "a")
                file.write("--------------------------\n")
                file.write("Name : " + name + "\n")
                while True:
                    try:
                        age = int(input("Enter Age : "))
                        file.write("Age : " + str(age) + "\n")
                        break
                    except ValueError:
                        print("Invalid Age Input. Please enter a number.")
                print("Manager//Employee (Please Write)")
                while True:
                    post = str(input("Enter Your Post :"))
                    if post.casefold() == "Manager".casefold() or post.casefold() == "Employee".casefold():
                        file.write("Post : " + post + "\n")
                        break
                    else:
                        print("Invalid post. Please enter 'Manager' or 'Employee'.")
                while True:
                    try:
                        mobile_no = input("Enter Mobile Number : ")
                        if mobile_no.isdigit() and len(mobile_no) == 10:
                            file.write("Mobile Number : " + mobile_no + "\n")
                            break
                        else:
                            print(
                                "Enter a valid mobile number. It should be 10 digits.")
                    except ValueError:
                        print("An error occurred")
                while True:
                    email = str(input("Enter Your Email : "))
                    if (email.__contains__("@gmail.com")):
                        file.write("Email : " + email + "\n")
                        file.write("--------------------------")
                        break
                    else:
                        print("Please Enter Valid Email (Example : xyz@gmail.com)")
                file.close()
            case 2:
                name = str(input("Enter Employee Name to Update : "))
                update_employee(name)
                print(f"Data Of {name} Is Update Succesfully")
            case 3:
                name = str(input("Enter Employee Name to Delete : "))
                delete_employee(name)
                print(f"Data Of {name} Is Delete Succesfully")
            case 4:
                name = str(input("Enter Employee Name to View : "))
                data = fetch_employee(name)
                if data:
                    for line in data:
                        print(line.strip())
            case _:
                print("Invalid choice. Please enter a number between 1 and 4.")
    except ValueError:
        print("Invalid input. Please enter a number.")
