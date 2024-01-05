
class Brain:
    def __init__(self, user_answer, answer):
        self.user_answer = user_answer
        self.answer = answer
    
    def checkAnswer(self):
        if self.answer == self.user_answer:
            return True
        else:
            return False
    
    def printScore(self, score, i, answer):
        print(f"The answer is: {answer}")
        print(f"Current Score: {score}/{i+1}")

