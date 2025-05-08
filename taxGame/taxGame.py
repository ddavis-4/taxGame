import random

# NPCs and their quiz questions
npcs = [
    {
        "name": "Sam the Server",
        "question": "What form do employees receive to report wages?",
        "options": ["A) 1040", "B) W-2", "C) 1099", "D) 401(k)"],
        "answer": "B"
    },
    {
        "name": "Freelancer Fran",
        "question": "Which form reports income for freelance or gig work?",
        "options": ["A) W-2", "B) 1099", "C) 1040", "D) 941"],
        "answer": "B"
    },
    {
        "name": "Middle-Income Max",
        "question": "What form does everyone file to report their taxes?",
        "options": ["A) 1040", "B) W-4", "C) 1099", "D) 1098"],
        "answer": "A"
    },
    {
        "name": "High-Income Holly",
        "question": "What does withholding mean?",
        "options": [
            "A) A bonus for good work",
            "B) Tax paid at the end of the year",
            "C) Money taken out of your paycheck for taxes",
            "D) A refund you receive"
        ],
        "answer": "C"
    },
    {
        "name": "Student Steve",
        "question": "What is the standard deduction?",
        "options": [
            "A) A tax credit for students",
            "B) A fixed amount subtracted from your income",
            "C) A tax you pay on textbooks",
            "D) A refund for filing early"
        ],
        "answer": "B"
    }
]

def tax_game():
    print("\n🎩 Welcome to TAX QUEST: The Top Hat Collector 🎩")
    print("Your mission: Answer tax questions to collect taxes from townspeople!\n")

    random.shuffle(npcs)
    score = 0

    for npc in npcs:
        print(f"You approach {npc['name']}...")
        print(npc['question'])
        for option in npc['options']:
            print(option)

        while True:
            response = input("\nYour answer (A/B/C/D): ").strip().upper()
            if response in ["A", "B", "C", "D"]:
                break
            else:
                print("Please enter a valid choice: A, B, C, or D.")

        if response == npc['answer']:
            print("✅ Correct! You collect their taxes.\n")
            score += 1
        else:
            print(f"❌ Incorrect. The correct answer was {npc['answer']}.")
            print("💡 Hint: Review the basics of tax forms and deductions.\n")

    print(f"🎉 Game Over! You collected taxes from {score} out of {len(npcs)} townspeople.")
    if score == len(npcs):
        print("🏆 You earned the Golden Calculator of Tax Wisdom!")
    else:
        print("📚 Study a little more and try again!")

if __name__ == "__main__":
    tax_game()


