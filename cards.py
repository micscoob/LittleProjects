# Will be a bunch of card games to play. Right now only black jack is playable.

#Things to work on are making it diplay nicer and right now the Ace is always 11.
import random

def menu():  
    while True:
        global deck
        deck = [1,2,3,4,5,6,7,8,9,10,11,12,13]*4
        
        print('########################')
        print('## Welcome to cards   ##')
        print('## 1  Play Black Jack ##')
        print('## 2      Quit        ##')
        print('########################')
        choice =int( input('Enter Choice: '))
        if choice == 1:
              blackjack()
        elif choice == 2:
              exit()
def deal():
     global deck
     facecard = {11:'J',12:'Q',13:'K',1:'A'}
     card = int(random.choice(deck))
     deck.remove(card)
     if card in facecard:
        card = facecard[card]
     return(card)  
def val(hand):
    points = {'K':10,'Q':10,'J':10,'A':11}
    tmp = 0
    for i in hand:
        if i in points:
            tmp += points[i]
        else:
            tmp += i
    return(tmp)   
def blackjack():
    hand_size = 0
    bust = 0
    dealers_hand =[]
    dealertotal = 0
    players_hand = []
    playertotal = 0
    points = {'K':10,'Q':10,'J':10,'A':11}  
#deal 2 cards 
    while hand_size <2:
        dealers_hand.append(deal())
        players_hand.append(deal())
        hand_size += 1
#find value of cards in hands
    dealertotal = val(dealers_hand)
    playertotal = val(players_hand) 
#playing black jack
    while True:
        if playertotal < 21:
            print(players_hand)
            print('Your at %d ' %(playertotal))
            choice = int(input('Would you like to hit[1] or pass[2]? '))
                          
            if choice == 1:
                print('\nHIT\n')
                players_hand.append(deal())
                playertotal = val(players_hand)
            elif choice == 2:
                print('\nPASS\n')
                break
            else:
              print('please enter only 1 or 2')
                          
        elif playertotal == 21:
            print(players_hand)
            print('  /$$$$$$    /$$  ')
            print(' /$$__  $$ /$$$$  ')
            print('|__/  \ $$|_  $$  ')
            print('  /$$$$$$/  | $$  ')
            print(' /$$____/   | $$  ')
            print('| $$        | $$  ')
            print('| $$$$$$$$ /$$$$$$')
            print('|________/|______/')
            break
        else:
            print('BUST!')
            bust = 1
            break
    
    if bust != 1:
        while dealertotal < playertotal:
            print('DEARLS HAND:\n %s'%(dealers_hand))
            print('DEALER WILL HIT!\n')
            dealers_hand.append(deal())
            dealertotal = val(dealers_hand)
            
            
         
        if dealertotal == playertotal:
            print('DEALERS TOTAL IS: %d\nYOUR TOTAL IS: %d\nTIE!\n'%(dealertotal,playertotal))
        elif dealertotal == 21 and playertotal < 21:
            print('DEALERS TOTAL IS: %d\nYOUR TOTAL IS: %d\nDELAER WINS!\n'%(dealertotal,playertotal))
        elif dealertotal > 21:
            print('DEALERS TOTAL IS: %d\nYOUR TOTAL IS: %d\nDELAER BUST!\nYOU WIN!\n'%(dealertotal,playertotal))
        elif dealertotal > playertotal:
            print('DEALERS TOTAL IS: %d\nYOUR TOTAL IS: %d\nYOU LOSE!\n'%(dealertotal,playertotal))
    else:
        print('DEALERS TOTAL IS: %d\nYOUR TOTAL IS: %d\nYOU BUST!\n'%(dealertotal,playertotal))
  
menu()
