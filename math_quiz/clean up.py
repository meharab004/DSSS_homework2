import random

def function_A(min_val, max_val):
    """
    Generate a random integer between min_val and max_val (inclusive).
    """
    return random.randint(min_val, max_val)

def function_B():
    """
    Return a random arithmetic operator (+, -, *).
    """
    return random.choice(['+', '-', '*'])

def function_C(n1, n2, o):
    """
    Perform the given arithmetic operation on n1 and n2.
    Return the problem statement and the correct answer.
    """
    problem = f"{n1} {o} {n2}"
    if o == '+':
        answer = n1 + n2
    elif o == '-':
        answer = n1 - n2
    else:
        answer = n1 * n2
    return problem, answer

def math_quiz():
    """
    Run a math quiz game with a fixed number of questions.
    """
    score = 0
    total_questions = 10

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        # Generate random numbers and an arithmetic operator
        n1 = function_A(1, 10)
        n2 = function_A(1, 10)
        o = function_B()

        # Get the problem statement and the correct answer
        problem, answer = function_C(n1, n2, o)
        print(f"\nQuestion: {problem}")
        user_answer = int(input("Your answer: "))

        # Check if the user's answer is correct
        if user_answer == answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()