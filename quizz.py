print("Welcome to quizz game")
player=input("Do you want to play? ")

if player.lower()!= "yes":
    quit()

print("Okay Lets play:")
score=0

answer=input("what is stand for cpu: ")
if answer.lower()=="central processing unit":
    print("Correct")
    score+=1
else:
    print("Wrong")

answer=input("Captial of india is: ")
if answer.lower()=="delhi":
    print("correct!")
    score+=1
else:
    print("wrong")

answer=input("Captial of Tamil Nadu: ")
if answer.lower()=="Chennai":
    print("correct!")
    score+=1
else:
    print("wrong")


print("Your score: " +str(score))