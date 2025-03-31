# quiz_cracker.py
class QuizCracker:
    def __init__(self, questions):
        self.questions = questions

    def start_quiz(self):
        score = 0
        for qid, details in self.questions.items():
            print(f"Question: {details['question']}")
            for option in details['options']:
                print(option)
            answer = input("Your answer: ").strip()
            if answer == details['answer']:
                score += 1
                print("Correct!")
            else:
                print("Wrong answer.")
        print(f"Your score: {score}/{len(self.questions)}")