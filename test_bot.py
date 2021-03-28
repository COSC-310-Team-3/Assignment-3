import unittest
import ChatBotWithPyDictionary

class TestChatBot(unittest.TestCase):
  
    
    #this first function tests the checkPolarity
    def test_checkPolarity(self):
          self.assertEqual(ChatBotWithPyDictionary.checkPolarity("I hate you"), True)
          self.assertEqual(ChatBotWithPyDictionary.checkPolarity("Soccer is terrible"), True)
          self.assertEqual(ChatBotWithPyDictionary.checkPolarity("I love you"), False)
          self.assertEqual(ChatBotWithPyDictionary.checkPolarity("Curling is boring"), True)
          self.assertEqual(ChatBotWithPyDictionary.checkPolarity("You couldn't beat me"), False)
          self.assertEqual(ChatBotWithPyDictionary.checkPolarity("Crosby is bad at hockey"), True)
          self.assertEqual(ChatBotWithPyDictionary.checkPolarity("Messi is a great guy"), False)
          self.assertEqual(ChatBotWithPyDictionary.checkPolarity("Hi how are you?"), False)
          self.assertEqual(ChatBotWithPyDictionary.checkPolarity("No you could not"), False) 
          
          
          
    def test_checkForCurrency(self):
          self.assertEqual(ChatBotWithPyDictionary.checkForCurrency("Can I go to a game for $100?"), True)
          self.assertEqual(ChatBotWithPyDictionary.checkForCurrency("£100"), False) 
          self.assertEqual(ChatBotWithPyDictionary.checkForCurrency("one hundred dollars"), False)
          self.assertEqual(ChatBotWithPyDictionary.checkForCurrency("is messi worth $100 mil?"), True)


    def test_checkForNum(self):
          self.assertEqual(ChatBotWithPyDictionary.checkForNum("Who won in 1900?"), True)
          self.assertEqual(ChatBotWithPyDictionary.checkForNum("Who won in 2000?"), True)
          self.assertEqual(ChatBotWithPyDictionary.checkForNum("Who won in 3000?"), False)
          self.assertEqual(ChatBotWithPyDictionary.checkForNum("Who won in 19000?"), False)
          self.assertEqual(ChatBotWithPyDictionary.checkForNum("Who won in 190?"), False)






    
if __name__ == '__main__':
     unittest.main()
  
    
  
      
