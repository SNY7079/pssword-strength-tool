import re

def check_password_strength(password):
    strength = 0
    remarks = []
    if len(password) >= 8:
        strength += 1
    else:
        remarks.append("Password is too short. Minimum 8 characters required.")
    if re.search(r'[a-z]', password):
        strength += 1
    else:
        remarks.append("Add lowercase letters.")
    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        remarks.append("Add uppercase letters.")
    if re.search(r'\d', password):
        strength += 1
    else:
        remarks.append("Add digits.")
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 1
    else:
        remarks.append("Add special characters.")
    if strength == 5:
        rating = "Strong"
    elif 3 <= strength < 5:
        rating = "Moderate"
    else:
        rating = "Weak"

    return rating, remarks
if __name__ == "__main__":
    user_password = input("Enter your password to test its strength: ")
    rating, issues = check_password_strength(user_password)
    
    print(f"\nPassword Strength: {rating}")
    if issues:
        print("Suggestions:")
        for item in issues:
            print(f"- {item}")
