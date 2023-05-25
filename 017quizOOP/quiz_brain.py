class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.q_list = q_list
        self.score = 0
        

    #ask questions
    #checking if the answer was correct
    #checking if at end of the quiz

    def next_question(self):
        question = self.q_list[self.question_number]
        choice = input(f"Q.{self.question_number + 1}. {question.text} (True/False)? ")
        self.question_number += 1
        self.check_answer(choice, question.answer)
        return choice
    
    def still_has_questions(self):
        return self.question_number < len(self.q_list)
    
    def check_answer(self, choice, correct_ans):
        if choice.lower() == correct_ans.lower():
            self.score += 1
            print(f"You got it right!")
            print(f"Score: {self.score}/{self.question_number}")
            
        else:
            print(f"That's incorrect. The correct answer is {correct_ans}.\n")

    

