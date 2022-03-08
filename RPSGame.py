import random

player_pick = input('rock, paper or scissors? ').lower()

# Choice Generation
computer_picks = ('rock', 'paper', 'scissors')
generated_pick = random.choice(computer_picks)

# Game Logic
if generated_pick == player_pick:
    print(
        f"It's a draw, Player choose {player_pick} and Python choose {generated_pick}")
elif 'rock' in generated_pick and player_pick == 'paper':
    print(f'Player Wins! Python choose {generated_pick}')
elif 'paper' in generated_pick and player_pick == 'scissors':
    print(f'Player Wins! Python choose {generated_pick}')
elif 'scissors' in generated_pick and player_pick == 'rock':
    print(f'Player Wins! Python choose {generated_pick}')
else:
    print(f'Python Wins, Python choose {generated_pick}')
