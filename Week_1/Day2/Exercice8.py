# Liste des questions et réponses
data = [
    {"question": "What is Baby Yoda's real name?", "answer": "Grogu"},
    {"question": "Where did Obi-Wan take Luke after his birth?", "answer": "Tatooine"},
    {"question": "What year did the first Star Wars movie come out?", "answer": "1977"},
    {"question": "Who built C-3PO?", "answer": "Anakin Skywalker"},
    {"question": "Anakin Skywalker grew up to be who?", "answer": "Darth Vader"},
    {"question": "What species is Chewbacca?", "answer": "Wookiee"}
]

def quiz():
    correct_answers = 0
    incorrect_answers = []
    
    print("\n🚀 Welcome to the Star Wars Quiz! 🚀\n")
    
    for item in data:
        user_answer = input(f"{item['question']} ").strip()
        if user_answer.lower() == item['answer'].lower():
            print("✅ Correct!\n")
            correct_answers += 1
        else:
            print(f"❌ Incorrect! The correct answer was: {item['answer']}\n")
            incorrect_answers.append({"question": item["question"], "your_answer": user_answer, "correct_answer": item["answer"]})

    # Résumé des résultats
    print("\n🌟 Quiz Completed! 🌟")
    print(f"You got {correct_answers}/{len(data)} correct answers.\n")

    if incorrect_answers:
        print("🛑 Here are the questions you got wrong:")
        for mistake in incorrect_answers:
            print(f"❌ {mistake['question']}\n   Your answer: {mistake['your_answer']}\n   Correct answer: {mistake['correct_answer']}\n")

    # Relancer le quiz si plus de 3 erreurs
    if len(incorrect_answers) > 3:
        retry = input("You had more than 3 incorrect answers. Do you want to try again? (yes/no): ").strip().lower()
        if retry == "yes":
            quiz()
        else:
            print("Thanks for playing! May the Force be with you. ✨")

# Lancer le quiz
quiz()
