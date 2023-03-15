class QuizBrain:
  def __init__(self,questionList):
    self.score=0
    self.questionNumber=0
    self.questionList=questionList
  def nextQuestion(self):
     question=self.questionList[self.questionNumber]
     return question
  def checkAnswer(self,answer):
    question = self.questionList[self.questionNumber]
    self.questionNumber+=1
    if question.answer.lower() == answer:
      self.score+=1
      print(f"You got it right! \nThe correct answer was: {answer}.\nyour current score is: {self.score}/{self.questionNumber}.")
      return 
    print(f"That's wrong.\nThe correct answer was:{question.answer}.\nYour current score is:{self.score}/{self.questionNumber}")  
    return  
  def chekEnd(self):
    return self.questionNumber!=len(self.questionList)   



    