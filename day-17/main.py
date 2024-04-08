from data import question_data
from models import Question, QuizBrain
import random

questions: list[Question] = []

for question in question_data:
    questions.append(Question(question["question"], question["correct_answer"]))
random.shuffle(questions)
quiz = QuizBrain(questions)

while quiz.still_has_questions():
    quiz.next_question()
