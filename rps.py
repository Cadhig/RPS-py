import random
def rps():
    arr = ['Rock', 'Paper', 'Scissors']
    userChoice = input('Rock, Paper, or Scissors?')
    computer = random.choice(arr)
    if userChoice == computer:
        return 'Tie!'
    if userChoice == 'Rock':
        if computer == 'Paper':
            outcome = 'LOSE'
        if computer == 'Scissors':
            outcome = 'WIN'
    if userChoice == 'Paper':
        if computer == 'Rock':
            outcome = 'WIN'
        if computer == 'Scissors':
           outcome = 'LOSE'
    if userChoice == 'Scissors':
        if computer == 'Rock':
            outcome = 'LOSE'
        if computer == 'Paper':
            outcome = 'WIN'
    return f"You chose {userChoice} and computer chose {computer}, YOU {outcome}"
print(rps())