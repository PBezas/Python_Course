# OOP Exercise
# Introduction

# Your goal in this exercise is to implement two classes, Card  and Deck .

# Specifications

### Card

# Each instance of Card  should have a suit ("Hearts", "Diamonds", "Clubs", or "Spades").

# Each instance of Card  should have a value ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K").

# Card 's __repr__  method should return the card's value and suit (e.g. "A of Clubs", "J of Diamonds", etc.)

### Deck

# Each instance of Deck  should have a cards attribute with all 52 possible instances of Card .

# Deck  should have an instance method called count  which returns a count of how many cards remain in the deck.

# Deck 's __repr__  method should return information on how many cards are in the deck (e.g. "Deck of 52 cards", "Deck of 12 cards", etc.)

# Deck  should have an instance method called _deal  which accepts a number and removes at most that many cards from the end of the deck (it may need to remove fewer if you request more cards than are currently in the deck!). If there are no cards left, this method should return a ValueError  with the message "All cards have been dealt".

# Deck  should have an instance method called shuffle  which will shuffle a full deck of cards. If there are cards missing from the deck, this method should raise a ValueError  with the message "Only full decks can be shuffled". shuffle should return the shuffled deck.

# Deck  should have an instance method called deal_card  which uses the _deal  method to deal a single card from the deck and return that single card.

# Deck  should have an instance method called deal_hand  which accepts a number and uses the _deal  method to deal a list of cards from the deck and return that list of cards.

from random import shuffle


class Card:
    def __init__(self, value, suit):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"


class Deck:
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = [
            "A",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "J",
            "Q",
            "K",
        ]
        #  -------------- 1st solution(mine)-----------
        self.cards = [Card(value, suit) for suit in suits for value in values]

        # -------------- 2nd solution ------------------
        # self.cards = []
        # for suit in suits:
        #     for value in values:
        #         self.cards.append(Card(value, suit))

    def __repr__(self):
        return f"Deck of {self.count()} cards"

    def count(self):
        return len(self.cards)

    # ------------------1st way(mine)--------------------

    def _deal(self, amount):
      dealt_cards = []

      if amount <= self.count():
          while amount > 0:
              dealt_cards.append(self.cards.pop())
              amount -= 1
      else:
          while self.count() > 0:
              dealt_cards.append(self.cards.pop())

          raise ValueError("All cards have been dealt")

      return dealt_cards

    # -------------------2nd way------------------------

    # def _deal(self, amount):
    #     deck_length = self.count()
    #     actual_amount = min([deck_length, amount])
    #     if deck_length == 0:
    #         raise ValueError("All cards have been dealt")
    #     dealt_cards = self.cards[-actual_amount:]
    #     self.cards = self.cards[:-actual_amount]
    #     return dealt_cards

    def deal_card(self):
        single_card = self._deal(1)
        return single_card[0]

    def deal_hand(self, amount):
        hand = self._deal(amount)
        return hand

    def shuffle(self):
        if self.count() == 52:
            shuffle(self.cards)
        else:
            raise ValueError("Only full decks can be shuffled")


my_deck = Deck()

# print(my_deck.cards)
# my_deck.shuffle()
# hand1 = my_deck.deal_hand(51)
# print(hand1)
# card = my_deck.deal_card()
# print(card)
# print(my_deck)
# my_deck.deal_hand(25)
# print(f"-25 > {my_deck.count()}")
# my_deck.deal_hand(25)
# print(f"-25 > {my_deck.count()}")
# my_deck.deal_hand(3)
# print(f"-3 > {my_deck.count()}")
# my_deck.deal_hand(3)
# print(f"-3 > {my_deck.count()}")
# print(my_deck.cards)

# # print(my_deck.shuffle())
# print(my_deck.count())

print(my_deck.deal_hand(52))
print(my_deck.count())
print(my_deck.deal_hand(3))
print(my_deck.shuffle())
