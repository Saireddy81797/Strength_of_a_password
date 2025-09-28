# Task 3 – Password Strength Checker

**SkillCraft Technology – Cybersecurity Internship**

## 📌 Objective

Build a **Python tool** that evaluates the strength of a password based on length, character variety (uppercase, lowercase, digits, symbols), and overall complexity. The tool helps users create more secure passwords and understand good practices in cybersecurity.

---

## ⚙️ Code (Task3_strengthofapassword.py)

```python
# Password Strength Checker - Task 03
# SkillCraft Technology Internship

import re

def check_password_strength(password):
    strength = 0
    remarks = ""

    # Length check
    if len(password) < 6:
        remarks = "Password too short! Use at least 8 characters."
        return "Weak", remarks
    elif len(password) >= 8:
        strength += 1

    # Check for uppercase letters
    if re.search(r"[A-Z]", password):
        strength += 1

    # Check for lowercase letters
    if re.search(r"[a-z]", password):
        strength += 1

    # Check for digits
    if re.search(r"[0-9]", password):
        strength += 1

    # Check for special characters
    if re.search(r"[@$!%*?&]", password):
        strength += 1

    # Strength classification
    if strength <= 2:
        remarks = "Weak password. Try mixing upper/lowercase, numbers, and symbols."
        return "Weak", remarks
    elif strength == 3:
        remarks = "Moderate password. Add more variety to strengthen it."
        return "Moderate", remarks
    elif strength >= 4:
        remarks = "Strong password. Good job!"
        return "Strong", remarks


if __name__ == "__main__":
    password = input("Enter a password to check: ")
    level, message = check_password_strength(password)
    print("Password Strength:", level)
    print("Remarks:", message)
```

---

## ▶️ How to Run

1. Save the file as **`Task3_strengthofapassword.py`**
2. Run in terminal or IDE:

   ```bash
   python Task3_strengthofapassword.py
   ```
3. Enter any password when prompted → tool will analyze and print strength level.

---

## ✅ Sample Output

```
Enter a password to check: abc123
Password Strength: Weak
Remarks: Weak password. Try mixing upper/lowercase, numbers, and symbols.
```

```
Enter a password to check: SecurePass123!
Password Strength: Strong
Remarks: Strong password. Good job!
```

---

## 📖 Explanation

* **Weak password** → Too short, or only letters/numbers.
* **Moderate password** → Has some variety but still predictable.
* **Strong password** → Long, includes uppercase, lowercase, digits, and symbols.

---

## 🔐 Learning Outcome

* Understood how to evaluate password complexity using **regular expressions**.
* Learned the importance of **password diversity** in cybersecurity.
* Built an interactive Python tool to guide users toward stronger passwords.

---

👨‍💻 *Prepared by: [Your Name]*
SkillCraft Technology – Cybersecurity Internship
