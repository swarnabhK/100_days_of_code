from question_model import Question
from quiz_data import question_data
from quiz_brain import QuizBrain

question_bank = []

for q in question_data:
    question_bank.append(Question(q['text'],q['answer']))


quizz = QuizBrain(question_bank)

while(not quizz.quiz_over()):
  quizz.next_question()