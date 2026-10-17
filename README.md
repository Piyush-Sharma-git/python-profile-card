# Python Profile Card Generator

A beginner-friendly Python mini project that takes user details, cleans and validates the input using string methods, extracts the username from the email, and prints a neatly formatted profile card.

---

## 📌 Features
- Takes user inputs: Name, Email, Phone Number, City, and Course.
- Cleans and formats input data using Python string methods.
- Handles multiple spaces between names using `.split()` and `.join()`.
- Extracts username from email (everything before `@`).
- Email validation: Checks for `@`, verifies username, and validates domain extensions (`.com`, `.in`, `.org`, `.net`, `.edu`, `.co`).
- Phone number validation: Validates 10-digit numeric format (supports hyphens and `+91` prefix).
- Automatically clears the terminal before displaying the final profile card (cross-platform support for Windows and Linux/macOS).

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
Enter Your Name :    piyush    sharma   
Enter your Email Id :   PIYUSH@GMAIL.COM   
Enter Your Phone No. :  +91 98765-43210
Enter Your City :  gwalior  
Enter Your Course :  bca  

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
- String Cleaning & Formatting: `.strip()`, `.title()`, `.lower()`, `.replace()`, `.upper()`, `.split()`, `.join()`
- Searching & Slicing: `.find()`, `.rfind()`, `.count()`, and `[:at_index]`
- String Validation Methods: `.endswith()`, `.isdigit()`, `len()`
- Conditional Statements: `if` / `else`
- Output Formatting: f-strings `f"..."`

---

## 📝 Notes
- Clears the terminal screen before displaying the profile card for a cleaner presentation (`cls` on Windows, `clear` on Linux/macOS).
