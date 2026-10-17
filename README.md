# Python Profile Card Generator

A beginner-friendly Python mini project that takes user details, cleans the input using string methods, extracts the username from the email, and prints a neatly formatted profile card.

---

## 📌 Features
- Takes user inputs: Name, Email, Phone Number, City, and Course.
- Cleans and formats input data using Python string methods.
- Handles multiple spaces between names using `.split()` and `.join()`.
- Extracts the username from the provided email address (everything before `@`).
- Stronger email validation: Checks for `@`, ensures username presence, and validates domain extensions like `.com`, `.in`, `.org`, `.net`, `.edu`, etc.
- Phone number validation: Validates 10-digit length and numeric digits (supports hyphens and `+91` country prefix).
- Clears the terminal before displaying the final output (supports both Windows and Linux/macOS).

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
Enter Your Name :   piyush   sharma  
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
- String Cleaning Methods: `.strip()`, `.title()`, `.lower()`, `.replace()`, `.upper()`, `.split()`, `.join()`
- Searching & Slicing: `.find()`, `.rfind()`, `.count()`, and `[:at_index]`
- String Validation Methods: `.endswith()`, `.isdigit()`, `len()`
- Conditional Statements: `if` / `else`
- Output Formatting: f-strings `(f"...")`

---

## 🔮 Future Improvements
- [x] Handle multiple spaces between first and last name using `.split()` and `.join()`.
- [x] Add stronger email validation (check for domain extensions like .com).
- [x] Add basic length and character validation for phone numbers.
- [ ] Export the generated profile card to a text file (`.txt`) or JSON (`.json`).
- [ ] Add a menu loop allowing the user to create multiple profile cards in one session.

---

## 📝 Notes
- The program clears the terminal before displaying the final profile for cleaner output.
- Cross-platform screen clearing is supported (`cls` on Windows, `clear` on Linux/macOS).
- Clearing the screen is only visual and does not securely erase terminal history.

