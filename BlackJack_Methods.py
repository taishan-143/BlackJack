from BlackJack_Classes import *
from card_data import values

def take_bet(chips):
    while True:
        try:
            chips.bet = int(input(f'How many chips would you like to bet? (up to {chips.total}):  '))
        except ValueError:
            print('Sorry, a bet must be an integer!')
        else:
            if chips.bet > chips.total:
                print("Sorry, your bet can't exceed",chips.total)
            else:
                break

def hit(deck,hand):
    hand.add_card(deck.deal(), values)
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    # global playing  # Sort out to accomodate for new file structure!
    while True:
        choice = input("\nWould you like to Hit or Stand? Enter 'h' or 's': ")
        if choice == 'h':
            hit(deck,hand)  # hit() function defined above
            playing = True
        elif choice == 's':
            print("\nPlayer stands. Dealer is playing.")
            playing = False
        elif choice == '' or choice == ' ':
            print("Sorry, please try again.")
            continue
        else:
            print("Sorry, I don't understand.")
            continue
        break
            
            
def show_some(player,dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('',dealer.cards[1])  
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    
def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)

def player_busts(player,dealer,chips):
    print("Player busts!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("Player wins!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("Dealer busts!")
    chips.win_bet()
    
def dealer_wins(player,dealer,chips):
    print("Dealer wins!")
    chips.lose_bet()
    
def push(player,dealer):
    print("Dealer and Player tie! It's a push.")

