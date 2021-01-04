import os
import random

deckOfCards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4


def runGame():
    choice = 0
    clear()
    # Begins the game
    print("Lets Play BlackJack. Please read the ReadME file for support.  \n")

    dealer = deal(deckOfCards)  # deals card for dealer
    player = deal(deckOfCards)  # deals cards for player
    print("Dealer has ? ", (dealer[0]), "= ?")  # gives the current result for dealer
    print("Player has", player[0], player[1], " = ", (totalfor(player)))  # gives current result for player

    # Check if it hits black jack prematurely before hiting or standing
    blackjack(dealer, player)
    quit = False
    # while the player is not quiting the game
    while not quit:
        # asks the user if its Hiting Standing or Quiting
        choice = input("Do you want to [H]it, [S]tand, or [Q]uit: ").lower()
        # if the chooses to hit   it class the hit function ans returns the current hands for each (player and dealer)
        if choice == 'h':

            print('Player Hits')
            hitFor(player)

            print('Player has', player)
            # print(totalfor(player)) (debugger)
            print('Dealer has', dealer)
            score(dealer, player)

        # if the player chooses to stand the dealer hits
        elif choice == 's':
            # while the dealer is less than 17 that means they havn't busted and can continue to bust
            while totalfor(dealer) < 17:
                print('Dealer Hits')

                hitFor(dealer)

                print(dealer)
            # if the dealer gets over 21 or 17 then they have busted
            if totalfor(dealer) > 21 or totalfor(dealer) >= 17:
                print('Dealer busts, you win!')
                play_again()
            # else goes to score function and checks if it hits any contion if not it continues through until asking the player to play again
            score(dealer, player)
            play_again()
        # this condtion is ran if the user decides to quit the game and it exist the program.

        elif choice == "q":
            print("Thank you for playing !")
            quit = True
            exit()






# Deals out all the cards
def deal(deckOfCards):
    hands = []
    # starts players with 2 cars and returns the hands
    for i in range(2):
        random.shuffle(deckOfCards)
        card = deckOfCards.pop()
        hands.append(card)
    return hands

# total get the total number for users.  
def totalfor(hands):
    total = 0
    for c in hands:
        # If the nuember choosen from the Deck of Cards is 11 , 12 or 13 then the total is added by 10 due to those number repsenting face cards
        if c == 11 or c == 12 or c == 13:
            total += 10
        # if thenmber is 14 then it marked as an Ace making the total either be added by 11 or 1
        elif c == 14:
            # this section check if the current total is more ll or equal to 11 if it adds by 1
            #given the player or Dealer a better chance of wining. Else it just adds by 11
            if total >= 11:
                total += 1
            else:
                total += 11
        else:
            total += c
    return total


# Function that ask the player if they want to play again. If Yes then cards are dealt and the run game function is called else the exist program
def play_again():
    replay = input("Do you want to replay ? (Y/N) : ").lower()
    if replay == "y":
        dealer = []
        player = []
        deckOfCards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] * 4
        runGame()

    else:
        print("Thank you for playing!")
        exit()


# This fucntion hits for eihter dealer or player
def hitFor(hands):
    # pops out the card choosen and then appends to the deck of cards for player or dealer
    card = deckOfCards.pop()

    hands.append(card)

    return hands

# Clears thes creen to go into game mode 
def clear():
    if os.name == 'nt':
        os.system('CLS')
    if os.name == 'posix':
        os.system('clear')

#check if their is a blackjack
def blackjack(dealer, player):
    if totalfor(player) == 21:
        print_results(dealer, player)
        print(" You got a Blackjack! You Won! \n")
        play_again()
    elif totalfor(dealer) == 21:
        print_results(dealer, player)
        print(" The dealer got a blackjack. You lost. \n")
        play_again()

# Prints the results of the game 
def print_results(dealer, player):
    clear()
    print("The dealer has ", (dealer), " for a total of ", str(totalfor(dealer)))
    print("Player has  ", (player), " for a total of ", (totalfor(player)))


# checks the current score.  
def score(dealer, player):
    #if the player  hits the number 21 then they win and the it prints the result for that outcome
    if totalfor(player) == 21:
        print_results(dealer, player)

        print("Player Wins! \n")
        play_again()

#if the dealer hits the number 21 then the Dealer wins, the Player loses and the it prints the result for that outcome
    elif totalfor(dealer) == 21:
        print_results(dealer, player)
        print("Sorry, you lose. The dealer got a blackjack.\n")
        play_again()
# If the player hits above 21 the player busts and the it prints the result for that outcome
    elif totalfor(player) > 21:
        print_results(dealer, player)
        print("Sorry. You bust. You lost.\n")
        play_again()
# If the player hits above 21 the dealer busts and the it prints the result for that outcome

    elif totalfor(dealer) > 21:
        print_results(dealer, player)
        print("Dealer busts. You win!\n")
        play_again()


    # else:
#		print_results(dealer, player)
#		print ("Congratulations. Your score is larger than the dealer. You won! \n")
#





if __name__ == "__main__":
    runGame()
