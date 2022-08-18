class QuizBrain:

    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        # getting current question
        current_question = self.question_list[self.question_number]
        # add question number by 1
        self.question_number += 1
        # input user answer to question
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ").lower().strip()
        user_answer = self.process_user_answer(user_answer)
        # checking answer
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print(f"Wrong answer.\nThe correct answer was {correct_answer}")
        # print score
        print(f"Score: {self.score}/{self.question_number}\n")

    def process_user_answer(self, user_answer):
        if user_answer == 't':
            return 'true'
        elif user_answer == 'f':
            return 'false'
        else:
            return user_answer

