def calculate_grade():   
    try:
        score = int(input("Enter Your Marks (1-100): "))
        if score < 1 or score > 100:
            raise ValueError("Marks should be between 1 and 100.")
        elif score >= 90:
            grade = 'A'
        elif score >= 80:
            grade = 'B'
        elif score >= 70:
            grade = 'C'
        elif score >= 60:
            grade = 'D'
        else:
            grade = 'E'
        print("Your Grade is:", grade,  "\nYour Mark is:", score)
    except Exception as e:
        print("An error occurred:" + str(e))
    
calculate_grade()
