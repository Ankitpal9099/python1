# quiz_game.py
from quiz_master import QuizMaster
from quiz_cracker import QuizCracker

def main():
    quiz_master = QuizMaster()
    while True:
        print("\nMenu:")
        print("1. Quiz Master")
        print("2. Take Quiz")
        print("3. Exit")
        choice = input("Select an option: ").strip()

        if choice == '1':
            while True:
                print("\nQuiz Master Menu:")
                print("1. Add Question")
                print("2. View Questions")
                print("3. Delete Question")
                print("4. Back to Main Menu")
                master_choice = input("Select an option: ").strip()

                if master_choice == '1':
                    question_id = input("Enter question ID: ")
                    question = input("Enter question: ")
                    options = input("Enter options (comma separated): ").split(',')
                    answer = input("Enter correct answer: ")
                    quiz_master.add_question(question_id, question, [opt.strip() for opt in options], answer)
                elif master_choice == '2':
                    quiz_master.view_questions()
                elif master_choice == '3':
                    question_id = input("Enter question ID to delete: ")
                    quiz_master.delete_question(question_id)
                elif master_choice == '4':
                    break
                else:
                    print("Invalid option. Please try again.")

        elif choice == '2':
            quiz_cracker = QuizCracker(quiz_master.questions)
            quiz_cracker.start_quiz()

        elif choice == '3':
            print("Exiting the game.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()