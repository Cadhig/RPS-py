import random
def rps():
    arr = ['Rock', 'Paper', 'Scissors']
    userChoice = input('Rock, Paper, or Scissors?')
    computer = random.choice(arr)
    if userChoice == computer:
        return 'Tie!'
    if userChoice == 'Rock':
        if computer == 'Paper':
            return 'You chose ROCK and computer chose PAPER, YOU LOSE!'
        if computer == 'Scissors':
            return 'You chose ROCK and computer chose SCISSORS, YOU WIN!'
    if userChoice == 'Paper':
        if computer == 'Rock':
            return 'You chose PAPER and computer chose ROCK, YOU WIN!'
        if computer == 'Scissors':
            return 'You chose PAPER and computer chose SCISSORS, YOU LOSE!'
    if userChoice == 'Scissors':
        if computer == 'Rock':
            return 'You chose SCISSORS and computer chose ROCK, YOU LOSE!'
        if computer == 'Paper':
            return 'You chose SCISSORS and computer chose PAPER, YOU WIN!'
    return 'go again'
print(rps())