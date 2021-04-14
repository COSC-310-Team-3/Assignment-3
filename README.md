# Assignment-3

## To use ChatBotWithWordnet.py you need to pip install vaderSentiment, NLTK, and tkinter
## To user ChatBotWitPyDictionary.py you need to pip install PyDictionary, vaderSentiment, NLTK, and tkinter

This is a project to create a functional chatbot for COSC 310. The user should be able to hold basic conversation with the bot about sports. The role the agent will take is that of a friend, and the user can ask the agent questions about sports. This bot was built off of the previous bot created in Assignment 3.
ChatBot.ipynb was migrated to ChatBot.py, see commits to Chatbot.ipynb to see original structure of code before it was migrated and the contributors
This program uses modified code from https://github.com/nltk/nltk/blob/develop/nltk/chat/util.py which is open source.

New features have been implemented in this bot, including searching for Wikipedia articles and translating sentences.

Searching for Wikipedia articles was implemented using the Wikipedia library. It functions by checking the user input for "Search for" and "Tell me about" followed by what ever the user wants the bot to look up. If it finds a match for what ever the user wants it to look up it returns a small summary of the article and a non clickable link to the wiki article.                                                       

Example:

Search for Obama

                                                          Barack Hussein Obama II ( (listen) bə-RAHK hoo-SAYN oh-BAH-mə; born August 4, 1961) is an American politician and attorney who served as the 44th president of the United States from 2009 to 2017. A member of the Democratic Party, Obama was the first African-American  president of the United States.
Read more at https://en.wikipedia.org/wiki/Barack_Obama
                                            
Tell me about Barack Obama                            

                                                          Barack Hussein Obama II ( (listen) bə-RAHK hoo-SAYN oh-BAH-mə; born August 4, 1961) is an American politician and attorney who served as the 44th president of the United States from 2009 to 2017. A member of the Democratic Party, Obama was the first African-American  president of the United States.
Read more at https://en.wikipedia.org/wiki/Barack_Obama

