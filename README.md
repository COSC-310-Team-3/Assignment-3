# Assignment-3

## To use ChatBotWithWordnet.py you need to pip install vaderSentiment, NLTK, and tkinter
## To user ChatBotWitPyDictionary.py you need to pip install PyDictionary, vaderSentiment, NLTK, and tkinter

This is a project to create a functional chatbot for COSC 310. The user should be able to hold basic conversation with the bot about sports. The role the agent will take is that of a friend, and the user can ask the agent questions about sports. This bot was built off of the previous bot created in assignment 2.
ChatBot.ipynb was migrated to ChatBot.py, see commits to Chatbot.ipynb to see original structure of code before it was migrated and the contributors
This program uses modified code from https://github.com/nltk/nltk/blob/develop/nltk/chat/util.py which is open source

New features have been implemented in this bot, including POS tagging and sentiment analysis.

Sentiment analysis adds to the bot by analyzing the user input, judging the overall sentiment, and providing an appropriate response if necessary. This was done by using the 'SentimentIntensityAnalyzer' function from the 'vaderSentiment' tool. When the user inputs a question/phrase, it is assigned a numerical value based on the overall sentiment (positive is a generally nice input, negative is a generally mean input). If the phrase is negative, the bot will get angry and tell the user it wasn't nice.

Example convo:

when is the next world cup?

                                                      Next year in Qatar
                                                      
who will win the next world cup?

                                                      Canada, no doubt. They are a soccer powerhouse
                                                      
what are you talking about?? Canada sucks at soccer!

                                                      Well that does not seem very nice!
                

POS tagging adds to the bot by splitting up every individual word in the user input, and then assigning each word a grammatical category. This was implemented by using the 'words_tokenize' and 'pos_tag' functions from the nltk tool. The bot is programmed to identify currencies and numerical values (to detect years), and will then give a specific response. The bot will also print out a list of each word and its associated part of speech tag.

Example convo:

what is the premier league?

                                                       The Premier League is the top division of soccer in England.
                                                       
do you think i could go to a premier league game for $100?

                                                       Sorry. I don't understand currency well. Can you try again?
                                             
i was born in 1999, who won the premier league that year?

                                                       Sorry, I am unfamiliar with that year. Can you try again?

