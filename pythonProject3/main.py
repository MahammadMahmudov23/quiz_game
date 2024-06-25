print("Welcome to my computer quiz!")
score=0;
playing=input("Do you want to play? ")
if playing.lower() !="yes":
    quit()

print("Okay! Let's play :)")

answer=input("What does CPU stand for? ")
if answer=="Central Processing Unit":
    print('Correct!')
    score+=1
else:
    print("Incorrect!");

    print("Your score is",score)