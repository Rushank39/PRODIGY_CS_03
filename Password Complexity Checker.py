import re

def check_password_strength(password):
    criteria = {
        'length': len(password) >= 8,
        'uppercase': bool(re.search(r'[A-Z]', password)),
        'lowercase': bool(re.search(r'[a-z]', password)),
        'digit': bool(re.search(r'\d', password)),
        'special': bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password)),
    }

    score = sum(criteria.values())
    feedback = {
        0: "Very Weak",
        1: "Weak",
        2: "Weak",
        3: "Moderate",
        4: "Strong",
        5: "Very Strong"
    }

    return feedback[score], criteria

# Example usage
password = input("Enter a password: ")
strength, details = check_password_strength(password)
print(f"Password Strength: {strength}")
print("Criteria met:")
for k, v in details.items():
    print(f" - {k.capitalize()}: {'✅' if v else '❌'}")
