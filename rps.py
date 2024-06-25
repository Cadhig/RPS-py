import random
def rps():
    arr = ['rock', 'paper', 'scissors']
    userChoice = input('Rock, Paper, or Scissors?').lower()
    computer = random.choice(arr)
    if userChoice == computer:
        return f"You chose {userChoice} and computer chose {computer}, its a TIE!"
    if userChoice == 'rock':
        if computer == 'paper':
            outcome = 'LOSE'
        if computer == 'scissors':
            outcome = 'WIN'
    if userChoice == 'paper':
        if computer == 'rock':
            outcome = 'WIN'
        if computer == 'scissors':
           outcome = 'LOSE'
    if userChoice == 'scissors':
        if computer == 'rock':
            outcome = 'LOSE'
        if computer == 'paper':
            outcome = 'WIN'
    return f"You chose {userChoice} and computer chose {computer}, YOU {outcome}"
print(rps())