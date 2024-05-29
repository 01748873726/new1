numbers = float(input("Please enter the marks (0-100): "))
    # Validate the marks are within a plausible range (0-100)
if 0 <= numbers <= 100:
        if numbers >= 90:
            grade = 'A'
        elif numbers >= 80:
            grade = 'B'
        elif numbers >= 70:
            grade = 'C'
        elif numbers >= 60:
            grade = 'D'
        else:
            grade = 'F'
        print("Grade:", grade)
else:
        print("Invalid numbers. Please enter a value between 0 and 100.")
