import random

def shuffle_questions(questions):
    random.shuffle(questions)

def ask_question(question):
    print(question["question"])
    for i, option in enumerate(question["options"], 1):
        print(f"{i}. {option}")
    
    while True:
        try:
            user_answer = int(input("Your answer (enter the number): "))
            if 1 <= user_answer <= len(question["options"]):
                return question["options"][user_answer - 1]
            else:
                print("Invalid input. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def check_answer(user_answer, correct_answer):
    return user_answer == correct_answer

def run_quiz(questions):
    shuffle_questions(questions)
    score = 0

    for question in questions:
        user_answer = ask_question(question)
        if check_answer(user_answer, question["answer"]):
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {question['answer']}\n")

    print(f"Quiz completed! Your score: {score}/{len(questions)}")

if __name__ == "__main__":
    questions = [
        {"question": "Who is known as the national hero of the Philippines?", "options": ["Jose Rizal", "Emilio Aguinaldo", "Andres Bonifacio", "Juan Luna"], "answer": "Jose Rizal"},
        {"question": "In what year did the Philippines gain independence from Spanish rule?", "options": ["1898", "1901", "1946", "1965"], "answer": "1898"},
        {"question": "What is the name of the first President of the Philippines?", "options": ["Manuel Quezon", "Emilio Aguinaldo", "Corazon Aquino", "Ferdinand Marcos"], "answer": "Emilio Aguinaldo"},
        {"question": "Where did the Battle of Mactan, where Ferdinand Magellan was killed, take place?", "options": ["Luzon", "Visayas", "Mindanao", "Palawan"], "answer": "Visayas"},
        {"question": "What is the official language of the Philippines?", "options": ["Filipino", "English", "Tagalog", "Bisaya"], "answer": "Filipino"}
    ]

    print("Welcome to the Philippine National History Quiz!\n")
    run_quiz(questions)
