import unittest
import ChatBot


class TestChatBot(unittest.TestCase):

    # this first function tests the checkPolarity
    def test_checkPolarity(self):
        self.assertEqual(ChatBot.checkPolarity("I hate you"), True)
        self.assertEqual(ChatBot.checkPolarity("Soccer is terrible"), True)
        self.assertEqual(ChatBot.checkPolarity("I love you"), False)
        self.assertEqual(ChatBot.checkPolarity("Curling is boring"), True)
        self.assertEqual(ChatBot.checkPolarity("You couldn't beat me"), False)
        self.assertEqual(ChatBot.checkPolarity("Crosby is bad at hockey"), True)
        self.assertEqual(ChatBot.checkPolarity("Messi is a great guy"), False)
        self.assertEqual(ChatBot.checkPolarity("Hi how are you?"), False)
        self.assertEqual(ChatBot.checkPolarity("No you could not"), False)

    def test_checkForCurrency(self):
        self.assertEqual(ChatBot.checkForCurrency("Can I go to a game for $100?"), True)
        self.assertEqual(ChatBot.checkForCurrency("£100"), False)
        self.assertEqual(ChatBot.checkForCurrency("one hundred dollars"), False)
        self.assertEqual(ChatBot.checkForCurrency("is messi worth $100 mil?"), True)

    def test_checkForNum(self):
        self.assertEqual(ChatBot.checkForNum("Who won in 1900?"), True)
        self.assertEqual(ChatBot.checkForNum("Who won in 2000?"), True)
        self.assertEqual(ChatBot.checkForNum("Who won in 3000?"), False)
        self.assertEqual(ChatBot.checkForNum("Who won in 19000?"), False)
        self.assertEqual(ChatBot.checkForNum("Who won in 190?"), False)


if __name__ == '__main__':
    unittest.main()
