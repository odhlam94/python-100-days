
class Question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def ask(self) -> bool:
        """Show question and check answer is correct"""
        answer = input(f"{self.question}(True/False): ")
        result = answer.lower() == self.answer.lower()
        return result


class QuizBrain:
    current_question_index = 0
    score = 0

    def __init__(self, questions: list[Question]):
        self.questions: list[Question] = questions

    def still_has_questions(self) -> bool:
        has_questions = self.current_question_index < len(self.questions)
        return has_questions

    def next_question(self):
        question = self.questions[self.current_question_index]
        self.current_question_index += 1
        if question.ask():
            self.score += 1
            print(f"Correctly! Your score is {self.score}")
        else:
            print(f"Wrong! Your score is {self.score}")


