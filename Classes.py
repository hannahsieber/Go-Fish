class Card:
    value = 0
    suit = "spades"

    def __init__(self, v, s):
        self.value = v
        self.suit = s

    def printOLD(self):
        if self.value == 1:
            print("Ace of " + self.suit)
        elif self.value == 11:
            print("Jack of " + self.suit)
        elif self.value == 12:
            print("Queen of " + self.suit)
        elif self.value == 13:
            print("King of " + self.suit)
        else:
            print(str(self.value) + " of " + self.suit)

    def print(self):
        if self.value == 1:
            print("Ace",end="")
        elif self.value == 11:
            print("Jack",end="")
        elif self.value == 12:
            print("Queen",end="")
        elif self.value == 13:
            print("King",end="")
        else:
            print(str(self.value),end="")

class Hand:
    hand = []

    def __init__(self):
        self.hand = []

    def add_card(self,c):
        self.hand.append(c)

    def play_card(self,c):
        self.hand.remove(c)

    def hand_size(self):
        return len(self.hand)

    def printOLD(self):
        for h in self.hand:
            h.print()
        print("\n")

    def print(self):
        print("      | ", end="")
        for h in self.hand:
            h.print()
            print(" | ",end="")
        print("\n")

    def get_card(self, val):
        for c in self.hand:
            if c.value == val:
                self.hand.remove(c)
                return True
        return False



    def has_card(self, val):
        for c in self.hand:
            if c.value == val:
                return True
        return False

    def check_pairs(self):
        for h in range(0,self.hand.__len__()):
            for j in range(0,self.hand.__len__()):
                if (self.hand[h].value == self.hand[j].value) and (self.hand[h].suit != self.hand[j].suit):
                    # have to pop backwards order so index of first doesn't change
                    self.hand.pop(j)
                    self.hand.pop(h)
                    return self.hand_size()
        return -1
