from data import question_data
from question_model import Question
from quiz_brain import Quiz

bank = []
for question in question_data:
    text = question["text"]
    answer = question["answer"]
    new_question = Question(text,answer)
    bank.append(new_question)


quiz = Quiz(bank)

while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.number}")
