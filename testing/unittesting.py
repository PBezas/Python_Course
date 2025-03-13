# Testing Card/Deck Exercise
# Your goal in this assignment will be to add tests to the classes you created in the last section: Card  and Deck . Try to test that instances have the right structure, and write some tests for the methods. Use some before hooks, and try to test for expected errors as well!

# Note that the shuffle  method will be difficult to test, since it produces a random output. Rather than trying to test randomness, you may just want to write some smaller, more straightforward tests. For instance, you could test that shuffle  doesn't change the size of the deck, or that the list of cards before the shuffle is in a different order than after the shuffle.

from OOP.deck_of_cards.card import Card
from OOP.deck_of_cards.deck import Deck
import unittest


class CardTests(unittest.TestCase):
  def setUp(self):
    self.card = Card('Hearts', 'A')

  def test_init(self):
    """Cards should have a suit and a value"""
    self.assertEqual(self.card.suit, 'Hearts')
    self.assertEqual(self.card.value, 'A')

  def test_repr(self):
    """Card should be represented by the string 'A of Hearts'"""
    self.assertEqual(repr(self.card), 'A of Hearts')

class DeckTests(unittest.TestCase):
  def setUp(self):
    self.deck = Deck()

  def test_init(self):
    """Deck should be a list and the lenght should be 52"""
    self.assertTrue(isinstance(self.deck.cards), list)
    self.assertEqual(len(self.deck.cards), 52)

  def test_repr(self):
    """Deck should be represented by the string 'Deck of 52 cards'"""
    self.assertEqual(repr(self.deck), 'Deck of 52 cards')

  def test_iter(self):
    """Deck should be an iterator"""
    self.assertTrue(isinstance(self.deck), iter)

  def test_count(self):
    """The count should return the number of cards in the deck"""
    self.assertEqual(len(self.deck.cards), 52)
    self.deck.cards.pop()
    self.assertEqual(len(self.deck.cards), 51)
  