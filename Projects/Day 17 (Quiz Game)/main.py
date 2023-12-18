from question_model import Question
from data import questions_api
from quiz_brain import QuizBrain

# getting data from data
questions_data = questions_api()

# creating question_bank
question_bank = []
if questions_data: # check if not None type
    for question in questions_data:
        question_bank.append(Question(question["question"], question["correct_answer"]))

    # create quiz
    quiz = QuizBrain(question_bank)

    # loop quiz questions
    while quiz.still_has_questions():
        quiz.next_question()

    # final print message
    print(f"You completed the quiz!\nYour final score was {quiz.score}/{quiz.question_number}")
