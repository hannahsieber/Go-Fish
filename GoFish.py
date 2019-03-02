from Classes import Card, Hand
import random
# what happens when the deck runs out???
# FIX SO "COMP REQUESTED ..." HAS ACE INSTEAD OF 1
deck = []
your_hand = Hand()
comp_hand = Hand()
your_score = 0
comp_score = 0
values = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

def main():
    turn = 1
    over = False
    global your_score
    global comp_score
    # CREATE DECK
    for i in range(1, 14):
        deck.append(Card(i,"spades"))
        deck.append(Card(i,"diamonds"))
        deck.append(Card(i,"hearts"))
        deck.append(Card(i,"clubs"))
    # HAND OUT CARDS
    print("\n\nYou will each get 7 cards \n")
    for i in range(0,7):
        your_hand.add_card(hand_out())
        comp_hand.add_card(hand_out())
    print("Here are your cards... but let's check for pairs!\n")
    your_hand.print()
    # CHECK FOR INITIAL PAIRS
    done = False
    y = 7
    while not done and y >= 2:
        y = your_hand.check_pairs()
        if y != 0:
            your_score += 1
        else:
            done = True
    done = False
    y = 7
    while not done and y >= 2:
        y = comp_hand.check_pairs()
        if y != 0:
            comp_score += 1
        else:
            done = True
    print_scores()

    while deck.__len__() > 0 and not over:
        if turn == 1:
            print(" hand size " + str(your_hand.hand_size()))
            your_hand.print()
            # comp_hand.print()  for testing purposes
            val = 0
            request = input("Ask for the value you want: Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, or King \n")
            for i in range(0,13):
                if request == values[i]:
                    val = i+1
                    break
            while not your_hand.has_card(val):
                request = input("Be sure to properly ask for a value that is in your own hand! ")
                for i in range(0, 13):
                    if request == values[i]:
                        val = i+1
                        break
            get = comp_hand.get_card(val)
            if get:
                your_hand.get_card(val)
                your_score += 1
                print("You got your card! Your score is now " + str(your_score) + "\n")
                turn = 1
                if your_hand.hand_size() == 0:
                    print("\nYou're out of cards! \n")
                    over = True
                elif comp_hand.hand_size() == 0:
                    print("\nThe computer ran out of cards!\n")
                    over = True
                else:
                    print("\nYou get to go again!\n")
            else:
                print("\n\nGO FISH!!!\n\n")
                your_hand.add_card(hand_out())
                y = your_hand.check_pairs()
                if y != 0:
                    your_score += 1
                    print("You got a match!\n")
                    if your_hand.hand_size() == 0:
                        print("\nYou're out of cards! \n")
                        over = True
                    elif comp_hand.hand_size() == 0:
                        print("\nThe computer ran out of cards!\n")
                        over = True
                    else:
                        print("\nYou get to go again!\n")
                    turn = 1
                else:
                    your_hand.print()
                    turn = 2
                print_scores()

        if turn == 2:
            r = comp_request()
            inp = input("Enter any value to see the computer's turn\n\n") #so there is a pause in the game
            if your_hand.get_card(r):
                comp_hand.get_card(r)
                print("The computer requested a(n) " + str(r) + " and you had it!\n")
                print_scores()
                comp_score += 1
                if your_hand.hand_size() == 0:
                    print("\nYou're out of cards! \n")
                    over = True
                elif comp_hand.hand_size() == 0:
                    print("\nThe computer ran out of cards!\n")
                    over = True
                else:
                    print("\nThe computer gets to go again!\n")
            else:
                print("The computer requested a(n) " + str(r) + " but you didn't have one.\n")
                print("\n\nGO FISH!!!\n\n")
                comp_hand.add_card(hand_out())
                y = comp_hand.check_pairs()
                if y != 0:
                    comp_score += 1
                    print("It got a match!\n")
                    if your_hand.hand_size() == 0:
                        print("\nYou're out of cards! \n")
                        over = True
                    elif comp_hand.hand_size() == 0:
                        print("\nThe computer ran out of cards!\n")
                        over = True
                    else:
                        print("\nThe computer gets to go again!\n")
                    turn = 2
                else:
                    turn = 1
                print_scores()
    if deck.__len__() == 0:
        print("The deck ran out! Game over!\n")
    else:
        print("Game over!")
    print("Final Scores:\n")
    print("    You: " + str(your_score) + " Computer: " + str(comp_score) + "\n") #didn't use print_scores because I don't want comp hand count


def print_scores():
    print("    You: " + str(your_score) + " Computer: " + str(comp_score))
    print("    The computer has " + str(comp_hand.hand_size()) + " cards.")
    print("    The deck has " + str(deck.__len__()) + " cards left.\n")


def hand_out():
    if deck.__len__() > 0:
        r = random.choice(deck)
        deck.remove(r)
        return r


def comp_request():
    r = random.choice(comp_hand.hand)
    return r.value


if __name__ == '__main__':
    main()

