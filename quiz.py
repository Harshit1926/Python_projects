import random

questions = [
    ("Which of the following is the correct extension of a Python file?",
     ["a) .py", "b) .p", "c) .python", "d) none of the above"], "a",
     "Python files use the .py extension."),

    ("Which keyword is used for defining a function in Python?",
     ["a) function", "b) func", "c) def", "d) define"], "c",
     "'def' is used for defining a function in Python."),

    ("What will be the output of the following code:\n\nx = 'abcd'\nfor i in x:\n    print(i.upper())",
     ["a) abcd", "b) error", "c) a\n   b\n   c\n   d", "d) A\n   B\n   C\n   D"], "d",
     "The loop iterates over each character, converting each one to uppercase."),

    ("Which arithmetic operator cannot be used with strings in Python?",
     ["a) +", "b) -", "c) *", "d) all of the above"], "b",
     "The + operator concatenates strings, and * repeats them, but - is not valid for string operations."),

    ("What will be the output of the following code:\n\nx = 'abcDEF'\nprint(x.capitalize())",
     ["a) Abcdef", "b) ABCDEF", "c) abc.Def", "d) none of the above"], "a",
     "The .capitalize() method makes the first letter uppercase while making the rest lowercase."),

    ("Which statement is used to create an empty set in Python?",
     ["a) {}", "b) ()", "c) set()", "d) []"], "c",
     "{} creates an empty dictionary, whereas set() correctly initializes an empty set."),

    ("Which of the following is a Python tuple?",
     ["a) (1,2,3,4)", "b) [1,2,3,4]", "c) {1,2,3,4}", "d) [1,2,3,4]"], "a",
     "Tuples are defined using parentheses (). Lists [] and sets {} are different data types."),

    ("What will be the output of the following Python code:\n\nx = 'abcd'\nfor i in range(len(x)):\n    print(x)",
     ["a) 0 1 2 3", "b) 1 2 3 4", "c) None of the Above", "d) a b c d"], "c",
     "The code prints 'abcd' four times because the loop runs for the string's length."),

    ("Which of the following Python statements will result in the output 6?\n\nA = [[1,2,3]\n[4,5,6]\n[7,8,9]]",
     ["a) A[2][1]", "b) A[1][2]", "c) A[3][2]", "d) A[2][3]"], "b",
     "In Python, lists are zero-indexed. A[1] refers to [4,5,6], and A[1][2] gives 6."),

    ("Which of the following is not a core data type in Python?",
     ["a) Tuple", "b) List", "c) Dictionary", "d) Class"], "d",
     "Python has core data types like tuples, lists, and dictionaries. Classes exist but are not core data types."),
]

print("PYTHON QUIZ BY HARSHIT MALHOTRA:")
print("ALL THE BEST!\n")

random.shuffle(questions)
score = 0
incorrect_answers = []

for index, (question, options, correct_answer, explanation) in enumerate(questions, start=1):
    print(f"{index}. {question}")
    for option in options:
        print(option)

    answer = input("Enter your answer (a/b/c/d): ").strip().lower()

    if answer == correct_answer:
        print("Correct answer!\n")
        score += 1
    else:
        print(f"Wrong answer. The correct answer is {correct_answer}.\nExplanation: {explanation}\n")
        incorrect_answers.append((question, explanation))

print(f"Game Over! Your final score is: {score}/{len(questions)}")

if incorrect_answers:
    print("\nReview Your Mistakes:")
    for q, exp in incorrect_answers:
        print(f"{q}\nExplanation: {exp}\n")

print("Thank you for playing!")
