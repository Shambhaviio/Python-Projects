class Quiz: 
    def __init__(self,q_list):
        self.number = 0 
        self.score = 0 
        self.question_list = q_list

    def still_has_question(self):
        return self.number<len(self.question_list)
    
    def next_question(self): 
        current = self.question_list[self.number]
        self.number +=1
        user_answer = input(f"Ques: {self.number}: {current.text} (True/False): ")

    def correct_answer(self, guess, answer):
        if guess.lower() == answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {answer}.")
        print(f"Your current score is: {self.score}/{self.number}")
        print("\n")