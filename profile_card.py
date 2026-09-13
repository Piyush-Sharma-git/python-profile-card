import os
name = input("Enter Your Name :")
email =input("Enter your Email Id :")
phone =input("Enter Your Phone No. :")
city =input("Enter Your City :")
course =input("Enter Your Course :")

name_clean = name.strip().title()
email_clean = email.strip().lower()
phone_clean = phone.strip().replace("-","")
city_clean = city.strip().title()
course_clean = course.strip().upper()
at_index = email_clean.find("@")
os.system("cls")
print(f"Name: {name_clean}")
if at_index == -1:
    print("Username: Invalid Email")
else:
    print(f"Username: {email_clean[:at_index]}")   
print(f"Email: {email_clean}")
print(f"Phone No.: {phone_clean}")
print(f"City: {city_clean}")
print(f"Course: {course_clean}")        
