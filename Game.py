import random
from BlackJack_Classes import *
from BlackJack_Methods import *
from card_data import *

def start():

   
    playing = True
    while True:
        # Print an opening statement
        print('Welcome to BlackJack! Get as close to 21 as you can without going over!\nDealer hits until they reach 17. Aces count as 1 or 11.')
        
        # Create & shuffle the deck, deal two cards to each player
        deck = Deck(suits, ranks)
        deck.shuffle()
        
        player_hand = Hand()
        player_hand.add_card(deck.deal(), values)
        player_hand.add_card(deck.deal(), values)
        
        dealer_hand = Hand()
        dealer_hand.add_card(deck.deal(), values)
        dealer_hand.add_card(deck.deal(), values)
                
        # Set up the Player's chips
        player_chips = Chips()  # remember the default value is 100    
        
        # Prompt the Player for their bet
        take_bet(player_chips)
        
        # Show cards (but keep one dealer card hidden)
        show_some(player_hand,dealer_hand)
        
        
        while playing:  # recall this variable from our hit_or_stand function
            
            # Prompt for Player to Hit or Stand
            hit_or_stand(deck,player_hand) 
            
            # Show cards (but keep one dealer card hidden)
            show_some(player_hand,dealer_hand)

            # If player's hand exceeds 21, run player_busts() and break out of loop
            if player_hand.value > 21:
                player_busts(player_hand,dealer_hand,player_chips)
                break



        # If Player hasn't busted, play Dealer's hand until Dealer reaches 17 
        if player_hand.value <= 21:
            
            while dealer_hand.value < 17:
                hit(deck,dealer_hand)    
        
            # Show all cards
            show_all(player_hand,dealer_hand)
            
            # Run different winning scenarios
            if dealer_hand.value > 21:
                dealer_busts(player_hand,dealer_hand,player_chips)

            elif dealer_hand.value > player_hand.value:
                dealer_wins(player_hand,dealer_hand,player_chips)

            elif dealer_hand.value < player_hand.value:
                player_wins(player_hand,dealer_hand,player_chips)

            else:
                push(player_hand,dealer_hand)        
        
        # Inform Player of their chips total 
        print("\nPlayer's winnings stand at",player_chips.total)
        
        # Ask to play again
        new_game = input("\nWould you like to play another hand? Enter 'y' or 'n': ")
        
        if new_game[0].lower()=='y':
            playing=True
            continue
        else:
            print("\nThanks for playing, see you soon!")
            break

start()