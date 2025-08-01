#!/usr/bin/python3
"""
Password Strength Assessment Tool
"""

def evaluate_password(password):
    """Analyzes password strength returning score and feedback."""
    
    score = 0
    feedback = []
    
    # Check minimum length
    if len(password) < 8:
        feedback.append("Password too short (minimum 8 chars)")
    else:
        score += 2
    
    # Check uppercase letters
    has_uppercase = False
    for ch in password:
        if ch.isupper():
            has_uppercase = True
            break
    
    if has_uppercase:
        score += 1
    else:
        feedback.append("Missing uppercase letters")
    
    # Check lowercase letters
    has_lowercase = False
    for ch in password:
        if ch.islower():
            has_lowercase = True
            break
    
    if has_lowercase:
        score += 1
    else:
        feedback.append("Missing lowercase letters")
    
    # Check numbers
    has_number = False
    for ch in password:
        if ch.isdigit():
            has_number = True
            break
    
    if has_number:
        score += 1
    else:
        feedback.append("No numbers included")
    
    # Check special characters
    has_special = False
    special_chars = "!@#$%^&*()-_=+[]{}|;:,.<>?"
    for ch in password:
        if ch in special_chars:
            has_special = True
            break
    
    if has_special:
        score += 1
    else:
        feedback.append("Lacks special characters")
    
    # Generate final assessment
    assessments = {
        0: "Very Weak",
        1: "Weak",
        2: "Fair",
        3: "Good",
        4: "Strong",
        5: "Excellent"
    }
    
    return {
        "score": score,
        "assessment": assessments[min(score, 5)],
        "feedback": feedback
    }


def main():
    password = input("Enter password: ")
    
    results = evaluate_password(password)
    
    print(f"\nPassword Score: {results['score']}/5 ({results['assessment']})")
    if results['feedback']:
        print("Suggestions:")
        for suggestion in results['feedback']:
            print(f"- {suggestion}")


if __name__ == "__main__":
    main()