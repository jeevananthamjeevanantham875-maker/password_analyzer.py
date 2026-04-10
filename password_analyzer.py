import re

def check_password_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if re.search("[a-z]", password):
        score += 1
    if re.search("[A-Z]", password):
        score += 1
    if re.search("[0-9]", password):
        score += 1
    if re.search("[@#$%^&+=!]", password):
        score += 1

    return score

def classify_strength(score):
    if score <= 2:
        return "Weak ❌"
    elif score == 3:
        return "Medium ⚠️"
    else:
        return "Strong ✅"

def suggestions(password):
    tips = []

    if len(password) < 8:
        tips.append("Use at least 8 characters")
    if not re.search("[A-Z]", password):
        tips.append("Add uppercase letters")
    if not re.search("[a-z]", password):
        tips.append("Add lowercase letters")
    if not re.search("[0-9]", password):
        tips.append("Include numbers")
    if not re.search("[@#$%^&+=!]", password):
        tips.append("Use special characters")

    return tips

def main():
    password = input("Enter your password: ")

    score = check_password_strength(password)
    strength = classify_strength(score)
    tips = suggestions(password)

    print("\nPassword Strength:", strength)

    if tips:
        print("\nSuggestions to improve:")
        for tip in tips:
            print("-", tip)
    else:
        print("Great! Your password is strong.")

if __name__ == "__main__":
    main()