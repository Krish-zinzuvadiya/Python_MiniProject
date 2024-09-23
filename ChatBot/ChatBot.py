print("Welcome To Our ChatBot Using Python Programming !")
file_name = input("Enter Your File Name: ")
file_name += ".txt"
file = open(file_name, "a")

first_name = input("Enter Your First Name : ")
last_name = input("Enter Your Last Name : ")

name = first_name + " " + last_name
file.write("Name : " + name + "\n")

while True:
    age = input("Enter Your Age : ")
    if age.isdigit():
        file.write("Age : " + age + "\n")
        break
    else:
        print("Invalid input. Please enter a valid age (only numbers).")

while True:

    email = str(input("Enter Your Email : "))
    if (email.__contains__("@gmail.com")):
        file.write("Email : " + email + "\n")
        break
    else:
        print("Please Enter Valid Email (Example : xyz@gmail.com)")


occupation = input("Enter Your Occupation : ")
file.write("Occupation : " + occupation + "\n")


address = input("Enter Your Permanent-Address :")
file.write("Address : " + address + "\n")

location = input("Enter Your City : ")
file.write("City : " + location + "\n")

state = input("Enter Your State : ")
file.write("State : " + state + "\n")

country = input("Enter Your Country : ")
file.write("Country : " + country + "\n")

print("Thank You For Using Our ChatBot !!!")

file.close()
