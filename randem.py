import random 

def play() :
    user= input ("What's you choice? 'r' for rock , 's' for scissors and 'p' for paper\n")
    compteur = random.choice(['r','s','p'])

    if user == compteur: 
      return 'It\' s a tie'
    
    if is_win(user,compteur) :
       return 'you won'
    return 'you lost!'
    


def is_win(player,opponent):
   if (player=='r'and opponent=='s')or (player== 's'and opponent =='p')or (player=='p'and opponent=='r'):
      return True     
print (play())