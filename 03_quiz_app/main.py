# Simple Quiz Application
# Student Level Pure Python Project

questions = [
    {
        "question": "What is the capital of Pakistan?",
        "options": ["A. Karachi", "B. Lahore", "C. Islamabad", "D. Peshawar"],
        "answer": "C"
    },
    {
        "question": "Which language is used to create this quiz?",
        "options": ["A. Java", "B. Python", "C. C++", "D. HTML"],
        "answer": "B"
    },
    {
        "question": "How many days are there in a leap year?",
        "options": ["A. 365", "B. 366", "C. 364", "D. 360"],
        "answer": "B"
    },
    {
        "question": "What does CPU stand for?",
        "options": ["A. Central Process Unit", "B. Central Processing Unit", "C. Computer Personal Unit", "D. Central Processor Utility"],
        "answer": "B"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"],
        "answer": "B"
    }
]

def run_quiz():
    score = 0
    print("===== WELCOME TO THE QUIZ =====\n")

    for i, q in enumerate(questions, 1):
        print(f"Q{i}. {q['question']}")
        for option in q["options"]:
            print(option)

        user_answer = input("Your answer (A/B/C/D): ").strip().upper()

        if user_answer == q["answer"]:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! Correct answer is {q['answer']}\n")

    print("===== QUIZ FINISHED =====")
    print(f"Your Score: {score}/{len(questions)}")

    percentage = (score / len(questions)) * 100
    print(f"Percentage: {percentage:.1f}%")

    if percentage == 100:
        print("🏆 Excellent! Perfect score!")
    elif percentage >= 60:
        print("👍 Good job!")
    else:
        print("📚 Keep practicing!")

run_quiz()
