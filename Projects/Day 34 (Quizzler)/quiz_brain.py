from api_manager import ApiManager


class QuizBrain:
    def __init__(self):
        self.questions = ApiManager().questions
        self.question_number = 0
        self.score = 0
        self.current_question = "initial"
        self.current_answer = "initial"

    def next_question(self):
        # checks if there is a next question
        if self.question_number >= len(self.questions):
            self.current_answer = "final"
            return f"You have answered all questions!\nYour final score is {self.score}"

        # saving next question and answer
        self.current_question = self.questions[self.question_number]['question']
        self.current_answer = self.questions[self.question_number]['correct_answer']

        # format question
        self.format_question()

        # add question number by 1
        self.question_number += 1

        return self.current_question

    def update_score(self, user_answer):
        if user_answer == self.current_answer:
            self.score += 1
        return self.score

    def format_question(self):
        current_question_list = self.current_question.split()
        range_value = len(current_question_list) + len(current_question_list) // 4

        for index in range(0, range_value, 4):
            current_question_list.insert(index, "\n")

        self.current_question = ' '.join(current_question_list)
