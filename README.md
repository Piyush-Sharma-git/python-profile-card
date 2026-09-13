# Python Profile Card Generator

A beginner-friendly Python mini project that takes user details, cleans the input using string methods, extracts the username from the email, and prints a neatly formatted profile card.

---

## 📌 Features
- Takes user inputs: Name, Email, Phone Number, City, and Course.
- Cleans and formats input data using Python string methods.
- Extracts the username from the provided email address (everything before `@`).
- Basic validation: Displays `Invalid Email ` if the `@` symbol is missing.
- Clears the terminal before displaying the final output (for cleaner display).

---

## 💻 Requirements
- Python 3.x installed on your system.

---

## 🚀 How to Run

1. Clone or download this repository to your local machine.
2. Open your terminal / command prompt in the project directory.
3. Run the script using:

```bash
py profile_card.py
```

---

## 📋 Example Run (Dummy Data)
```text
Enter Your Name :   piyush sharma
Enter your Email Id :  PIYUSH@GMAIL.COM 
Enter Your Phone No. : 98765-43210
Enter Your City : gwalior
Enter Your Course : bca 

Name: Piyush Sharma
Username: piyush
Email: piyush@gmail.com
Phone No.: 9876543210
City: Gwalior
Course: BCA
```

---

## 🧠 Concepts Used
- User Input: `input()`
- String Cleaning Methods: `.strip()`, `.title()`, `.lower()`, `.replace()`, `.upper()`
- Searching & Slicing: `.find()` and `[:at_index]`
- Conditional Statements: `if` / `else`
- Output Formatting: f-strings `(f"...")`

---

## 🔮 Future Improvements
- Handle multiple spaces between first and last name using `.split()` and `.join()`.
- Add stronger email validation (check for domain extensions like .com).
- Add basic length and character validation for phone numbers.

---

## 📝 Notes
-  The program clears the terminal before displaying the final profile for cleaner output.
- The screen-clearing behavior may vary depending on the operating system and terminal.
- This feature currently uses the Windows `cls` command.
- Clearing the screen is only visual and does not securely erase terminal history.

