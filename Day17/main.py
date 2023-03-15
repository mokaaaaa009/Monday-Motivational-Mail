from questionmodel import Question
from data import question_data
from quizBrain import QuizBrain
import colorgram

questions=[]
for question in question_data:
  newQ=Question(question['question'],question['correct_answer'])
  questions.append(newQ)
brain=QuizBrain(questions)
on=True
while on:
  question=brain.nextQuestion()
  ans=input(f"Q.{brain.questionNumber+1}:{question.text}.(True/False): ")
  brain.checkAnswer(ans)
  on =brain.chekEnd()

colors = colorgram.extract('.jpg', 6)