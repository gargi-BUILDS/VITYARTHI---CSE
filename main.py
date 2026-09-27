def quiz_game():

    # Quiz questions
    questions = [
        {
            "question": "Which statement is used to make a decision in Python?",
            "options": [
                "A) for",
                "B) if",
                "C) def",
                "D) return"
            ],
            "answer": "B"
        },

        {
            "question": """What will be the output?

x = 10

if x > 5:
    print("Yes")
else:
    print("No")""",
            "options": [
                "A) No",
                "B) Error",
                "C) Yes",
                "D) 10"
            ],
            "answer": "C"
        },

        {
            "question": "Which loop is commonly used when we know how many times we want to repeat something?",
            "options": [
                "A) if",
                "B) while",
                "C) for",
                "D) def"
            ],
            "answer": "C"
        },

        {
            "question": "What does the break statement do?",
            "options": [
                "A) Skips the current iteration",
                "B) Stops the loop",
                "C) Starts the loop again",
                "D) Defines a function"
            ],
            "answer": "B"
        },

        {
            "question": "What does the continue statement do?",
            "options": [
                "A) Stops the program",
                "B) Stops the loop completely",
                "C) Skips the current iteration and continues with the next one",
                "D) Defines a new function"
            ],
            "answer": "C"
        },

        {
            "question": "Which keyword is used to define a function in Python?",
            "options": [
                "A) function",
                "B) func",
                "C) define",
                "D) def"
            ],
            "answer": "D"
        },

        {
            "question": """What will be the output?

def add(a, b):
    return a + b

print(add(3, 4))""",
            "options": [
                "A) 3",
                "B) 4",
                "C) 7",
                "D) 12"
            ],
            "answer": "C"
        },

        {
            "question": """In the following function, what are a and b called?

def multiply(a, b):
    return a * b""",
            "options": [
                "A) Arguments",
                "B) Parameters",
                "C) Operators",
                "D) Variables only"
            ],
            "answer": "B"
        },

        {
            "question": "What is the purpose of the return statement in a function?",
            "options": [
                "A) To stop every loop in the program",
                "B) To send a value back from the function",
                "C) To define a function",
                "D) To print a value automatically"
            ],
            "answer": "B"
        },

        {
            "question": """What will be the output?

for i in range(3):
    print(i)""",
            "options": [
                "A) 1 2 3",
                "B) 0 1 2",
                "C) 0 1 2 3",
                "D) 3 2 1"
            ],
            "answer": "B"
        }
    ]

    # Initial score
    score = 0

    # Project heading
    print("=" * 60)
    print("             PYTHON MCQ QUIZ GAME")
    print("          Control Flow and Functions")
    print("=" * 60)
    print("Name: Gargi Sharma")
    print("=" * 60)

    print("\nWelcome to the Python Quiz!")
    print("There are 10 questions.")
    print("Each correct answer gives 1 mark.")
    print("There is no negative marking.")

    # Loop through all questions
    for number, q in enumerate(questions, 1):

        print("\n" + "-" * 60)
        print("Question", number)
        print("-" * 60)

        print(q["question"])

        # Display options
        for option in q["options"]:
            print(option)

        # Take answer from user
        user_answer = input("\nEnter your answer (A/B/C/D): ").upper()

        # Check the answer
        if user_answer == q["answer"]:
            print("Correct answer!")
            score += 1
        else:
            print("Incorrect answer!")
            print("Correct answer is:", q["answer"])

    # Calculate result
    total_questions = len(questions)
    incorrect_answers = total_questions - score
    percentage = (score / total_questions) * 100

    # Display final result
    print("\n" + "=" * 60)
    print("                    QUIZ RESULT")
    print("=" * 60)

    print("Name:", "Gargi Sharma")
    print("Total Questions:", total_questions)
    print("Correct Answers:", score)
    print("Incorrect Answers:", incorrect_answers)
    print("Final Score:", score, "/", total_questions)
    print("Percentage:", percentage, "%")

    # Performance message
    if percentage >= 80:
        print("Performance: Excellent!")
    elif percentage >= 60:
        print("Performance: Good!")
    elif percentage >= 40:
        print("Performance: Keep Practicing!")
    else:
        print("Performance: Need More Practice!")

    print("=" * 60)
    print("          Thank you for playing!")
    print("=" * 60)


# Start the quiz
quiz_game()


