import random
options = ('r','s','p')
start = input("Press 'k' to start or type 'stop' to exit anytime.")

while(start == 'k'):
    player = input("Type 'r' for 'rock, 's' for scissors, and 'p' for 'paper' or type 'stop' to exit anytime.")
    cpu = random.choice(options)
    if(cpu == player):
        print(cpu)
        print("It's a tie!")
        
    if((cpu == 'r' and player == 'p')or(cpu == 's'and player =='r')or(cpu=='p' and player == 's')):
        print(cpu)
        print("You lose!")
        
    if((player == 'r' and cpu == 'p')or(player == 's'and cpu =='r')or(player=='p' and cpu == 's')):
        print(cpu)
        print("You win!")
    if(player == 'stop'):
        break
      
else:
    print("Please restart")