import re

def check_password_strength(password):
    # Criteria
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    # Count errors
    errors = [length_error, digit_error, uppercase_error, lowercase_error, symbol_error]
    passed = errors.count(False)

    # Strength assessment
    if passed == 5:
        strength = "Strong"
    elif passed >= 3:
        strength = "Medium"
    else:
        strength = "Weak"

    return strength


# --- Main Program ---
password = input("Enter your password: ")
print("Password Strength:", check_password_strength(password))
