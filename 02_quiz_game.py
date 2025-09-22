import random

score = 0

questions = [
    {
        "q": "What is the capital of India?",
        "options": ["New York", "Delhi", "Moscow", "Los Angeles"],
        "answer": "Delhi"
    },
    {
        "q": "How many oceans are there in the world?",
        "options": ["1", "2", "4", "5"],
        "answer": "5"
    },
    {
        "q": "Which planet is known as the red planet?",
        "options": ["Mercury", "Venus", "Mars", "Jupiter"],
        "answer": "Mars"
    },
    {
        "q": "What art form is described as decorative handwriting or handwritten lettering?",
        "options": ["Calligraphy", "Astrology", "Callilogy", "Extensive Writing"],
        "answer": "Calligraphy"
    },
    {
        "q": "What is acrophobia a fear of?",
        "options": ["Heights", "Spiders", "Closed spaces", "Water"],
        "answer": "Heights"
    }
]

def ask_question(q):
    global score
    print("\n" + q["q"])
    for i, option in enumerate(q["options"], 1):
        print(f"{i}. {option}")
    ans = input("Enter your answer: ").strip().lower()
    if ans == q["answer"].lower():
        print("Excellent work 👍")
        score += 1
    else:
        print(f"Sorry, the correct answer was {q['answer']}")
    print("Current Score:", score)

# Game loop
random.shuffle(questions)  # prevents repeats
for q in questions:
    ask_question(q)
    confirm = input("Do you want to continue? (y/n): ").lower()
    if confirm == "n":
        break

print("\nFinal Score:", score)
