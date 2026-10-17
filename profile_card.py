import os

name = input("Enter Your Name : ")
email = input("Enter your Email Id : ")
phone = input("Enter Your Phone No. : ")
city = input("Enter Your City : ")
course = input("Enter Your Course : ")

name_clean = " ".join(name.split()).title()

email_clean = email.strip().lower()
at_index = email_clean.find("@")
valid_extensions = (".com", ".in", ".org", ".net", ".edu", ".co")
is_valid_email = (
    at_index > 0
    and email_clean.count("@") == 1
    and email_clean.endswith(valid_extensions)
    and email_clean.rfind(".") > at_index + 1
)

phone_clean = phone.strip().replace("-", "").replace(" ", "")
if phone_clean.startswith("+91"):
    phone_digits = phone_clean[3:]
else:
    phone_digits = phone_clean

is_valid_phone = phone_digits.isdigit() and len(phone_digits) == 10
if is_valid_phone:
    phone_display = phone_digits
else:
    phone_display = "Invalid Phone Number"

city_clean = city.strip().title()
course_clean = course.strip().upper()

os.system("cls" if os.name == "nt" else "clear")

print(f"Name: {name_clean}")
if is_valid_email:
    print(f"Username: {email_clean[:at_index]}")
    print(f"Email: {email_clean}")
else:
    print("Username: Invalid Email")
    print("Email: Invalid Email")

print(f"Phone No.: {phone_display}")
print(f"City: {city_clean}")
print(f"Course: {course_clean}")
