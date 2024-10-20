import random

def get_valid_guess():
    while True:
        try:
            guess = int(input("There are 10 Students, how many do you guess passed? "))
            if 1 <= guess <= 10:
                return guess
            else:
                print("Please enter a number between 1 and 10.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def guesses():
    global userGuess, computerGuess
    userGuess = get_valid_guess()
    computerGuess = random.randint(1, 10)
    
    print(f"Your Guess is {userGuess}")
    print(f"The Computer Guess is {computerGuess}")

def evaluate_students(student_list):
    pass_students = []
    failed_students = []
    
    for student in student_list.values():
        if student['studentGrade'] >= 75:
            pass_students.append(student)
        else:
            failed_students.append(student)
    
    return pass_students, failed_students

def display_results(pass_students, failed_students):
    print("\n----------- List of Students who have a Passing Mark --------------------")
    for student in pass_students:
        print(f"{student['studentName']} - Grade: {student['studentGrade']}, Subject: {student['classSubject']}")
    print(f"Total no. of Passed Students: {len(pass_students)}\n")
    
    print("------------ List of Students who have a Failing Mark ---------------------")
    for student in failed_students:
        print(f"{student['studentName']} - Grade: {student['studentGrade']}, Subject: {student['classSubject']}")
    print(f"Total no. of Failed Students: {len(failed_students)}")

def guessed_near(pass_students):
    global userGuess, computerGuess
    p_student_counter = len(pass_students)
    
    near_u_guess = abs(p_student_counter - userGuess)
    near_c_guess = abs(p_student_counter - computerGuess)

    if near_u_guess < near_c_guess:
        print("\nUser Guess is nearer!")
    elif near_u_guess == near_c_guess:
        print("\nUser and Computer Guesses are the same.")
    else:
        print("\nComputer Guess is nearer.")

def quiz_two(user_name, class_numbers):
    print(f"\nWelcome, {user_name}!")
    
    if userGuess == len(class_numbers):
        print("You guessed exactly right!")
    elif userGuess > len(class_numbers):
        print("Your guess is too high.")
    else:
        print("Your guess is too low.")

def main():
    user_name = input("Enter your name: ")

    student_list = {
        "studentOne": {"studentName": "Ricardo P", "studentGrade": 85, "classSubject": "DSA"},
        "studentTwo": {"studentName": "Anagracia A", "studentGrade": 82, "classSubject": "DSA"},
        "studentThree": {"studentName": "Anastacia D", "studentGrade": 75, "classSubject": "DSA"},
        "studentFour": {"studentName": "Gregorio D", "studentGrade": 74, "classSubject": "DSA"},
        "studentFive": {"studentName": "Alegro", "studentGrade": 95, "classSubject": "DSA"},
        "studentSix": {"studentName": "Maria Juana", "studentGrade": 90, "classSubject": "DSA"},
        "studentSeven": {"studentName": "Shantal T", "studentGrade": 83, "classSubject": "OS"},
        "studentEight": {"studentName": "Mariano J", "studentGrade": 91, "classSubject": "OS"},
        "studentNine": {"studentName": "Josefa G", "studentGrade": 73, "classSubject": "OS"},
        "studentTen": {"studentName": "Eliseo S", "studentGrade": 75, "classSubject": "OS"},
    }

    class_numbers = list(range(1, 11))  # List of class numbers
    class_numbers.sort(reverse=True)  # Reverse sorting of class numbers

    print(f"The following are the List of Students. Total of {len(student_list)}")
    print("----------------------------------------------------")
    for student in student_list.values():
        print(f"{student['studentName']} is enrolled in {student['classSubject']}")

    guesses()
    pass_students, failed_students = evaluate_students(student_list)
    display_results(pass_students, failed_students)
    guessed_near(pass_students)
    
    quiz_two(user_name, class_numbers)

if __name__ == "__main__":
    main()
