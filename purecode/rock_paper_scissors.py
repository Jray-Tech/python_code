import random
# now let us make a simple roc paper scissors game
print('''
Hello welcome to rock paper scissors 
if you haven't played this before then  listen up!
Here are the rules of this simple game 
you can use;
 "r" for rock ,
"p" for paper and
 "s" for scissors 
rules 
1, rock beats scissors 
2, paper beats rock
3, scissors beats paper
 ''')

# to store points and print out who wins at the end of the day
p_player1 = 0
p_player2 = 0
number_of_plays = 0
while number_of_plays < 3:
    options = ['rock', 'paper', 'scissors']
    player_raw = input(' What would u like to play?>').lower()
    # using a dic to convert r s and p to rock paper and scissors in the code
    dic = {
        'r': 'rock',
        'p': 'paper',
        's': 'scissors'
    }
    player1 = dic.get(player_raw, 'DOESNT EXIST')
    player2 = random.choice(options)
    print(player2)
    number_of_plays += 1
    if player1 == player2:
        print('this is a tie')
        p_player1 += 1
        p_player2 += 1
    elif player1 == 'rock' and player2 == 'scissors':
        p_player1 += 1
        print('You have won this round')
    elif player1 == 'paper' and player2 == 'rock':
        p_player1 += 1
        print('You have won this round')
    elif player1 == 'scissors' and player2 == 'paper':
        print('You have won this round')
        p_player1 += 1
    else:
        p_player2 += 1
        print('I have won this round')
    print(f'You have  {p_player1} points,  I have {p_player2} points')
    if number_of_plays == 3:
        if p_player2 == p_player1:
            print("Urgh it's a tie")
            start = input('type "yes" to start again').lower()
            if start == 'yes':
                number_of_plays = 0
                p_player1 = 0
                p_player2 = 0
        elif p_player1 > p_player2:
            print('You beat me congratulations!!!!')
            start = input('type "yes" to start again').lower()
            if start == 'yes':
                number_of_plays = 0
                p_player1 = 0
                p_player2 = 0
        elif p_player2 > p_player1:
            print('i won and i am so happy i beat you u donkey!!!!!')
            start = input('type "yes" to start again').lower()
            if start == 'yes':
                number_of_plays = 0
                p_player1 = 0
                p_player2 = 0
print(p_player1, p_player2)
print('did you enjoy this game?')
# this is the end of the game all that remains now is for me to add some sweet code snippets to catch exceptions
# this is actually simpler than it looks so dont be a donkey and think t is hard
# this is the world of us
# we are kings and we have won this indeed
6