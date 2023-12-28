class QuizBrain:
    def __init__(self,q_list) -> None:
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
      
    def next_question(self):
        if(self.question_number<len(self.question_list)):
          current_question = self.question_list[self.question_number]
          self.question_number+=1
          choice = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
          if(choice==current_question.answer):
              self.score+=1
              print(f"You got it right! Your current score is {self.score}/{self.question_number}")
          else:
              print(f"Sorry. You got it wrong. Your current score is {self.score}/{self.question_number}")
    
    def quiz_over(self):
        return True if self.question_number==len(self.question_list) else False
