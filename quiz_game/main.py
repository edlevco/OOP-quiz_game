from data import question_data
from question_model import Question
from quiz_brain import Brain


score = 0
for i in range(len(question_data)):
    new_question = Question(question_data[i]["text"], (question_data[i]["answer"]).lower())
    user_answer = input(f"Q.{i+1}: {new_question.question} (True/False)?: ").lower()
    if (user_answer == "quit"):
        break
    checker = Brain(user_answer, new_question.answer)
    if checker.checkAnswer():
        score +=1
        print("You are correct!")   
    else:
        print("You are wrong!")
    checker.printScore(score, i, new_question.answer)

print("You completed the quiz!!")
print("")


