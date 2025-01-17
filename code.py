# PASSWORD-STRENGTH-CHECKER
Develop a tool to assess the strength of passwords entered by users. Implement algorithms to analyze factors such as length, complexity, and uniqueness to provide feedback on password strength.



import re

def password_strength(password):
    strength = 0
    feedback = []

    # Length check
    length = len(password)
    if length < 8:
        feedback.append("Password is too short. Minimum length is 8 characters.")
    elif length > 12:
        strength += 2
        feedback.append("Password length is good.")
    else:
        strength += 1
        feedback.append("Password length is acceptable.")

    # Complexity checks
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("Password should include at least one lowercase letter.")

    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("Password should include at least one uppercase letter.")

    if re.search(r"[0-9]", password):
        strength += 1
    else:
        feedback.append("Password should include at least one digit.")

    if re.search(r"[@$!%*?&]", password):
        strength += 1
    else:
        feedback.append("Password should include at least one special character (@$!%*?&).")

    # Uniqueness check
    if len(set(password)) / length > 0.7:
        strength += 1
        feedback.append("Password has a good level of uniqueness.")
    else:
        feedback.append("Password could be more unique. Avoid using repetitive characters.")

    # Strength rating
    if strength <= 2:
        feedback.append("Overall password strength: Weak")
    elif strength == 3 or strength == 4:
        feedback.append("Overall password strength: Medium")
    else:
        feedback.append("Overall password strength: Strong")

    return strength, feedback

# Example usage
password = input("Enter a password to check its strength: ")
strength, feedback = password_strength(password)

print("\nPassword Strength Feedback:")
for comment in feedback:
    print(f"- {comment}")
