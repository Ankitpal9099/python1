# quiz_master.py
class QuizMaster:
    def __init__(self):
        self.questions = {}

    def add_question(self, question_id, question, options, answer):
        self.questions[question_id] = {
            'question': question,
            'options': options,
            'answer': answer
        }
        print("Question added successfully.")

    def view_questions(self):
        if not self.questions:
            print("No questions available.")
            return
        for qid, details in self.questions.items():
            print(f"ID: {qid}, Question: {details['question']}, Options: {details['options']}, Answer: {details['answer']}")

    def delete_question(self, question_id):
        if question_id in self.questions:
            confirmation = input("Are you sure you want to delete this question? (Y/N): ").strip().upper()
            if confirmation == 'Y':
                del self.questions[question_id]
                print("Question deleted successfully.")
            else:
                print("Deletion cancelled.")
        else:
            print("Question ID not found.")