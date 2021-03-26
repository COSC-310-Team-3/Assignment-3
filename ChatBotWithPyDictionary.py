import nltk
import tkinter
import string
from tkinter import *
from nltk.chat.util import Chat, reflections
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from nltk.corpus import wordnet
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
from nltk import word_tokenize
from PyDictionary import PyDictionary



# This is a modified converse function from nltk.chat.util
class modifiedChat(Chat):
    def converse(self, user_input):
        
        while user_input[-1] in "!.":
            user_input = user_input[:-1]
        return self.respond(user_input)


####################################################################
# The following is our chatbot implementation                      #
####################################################################


# this section is functions

# this function ends the window
def kill():
    root.destroy()


# this function creates the menu
def makeMenu():
    mainMenu = Menu(root)
    mainMenu.add_command(label="Quit", command=kill)
    root.config(menu=mainMenu)


# method to check for currency inputs

def checkForCurrency(userInput):
    userInput = nltk.word_tokenize(userInput)
    userInput = nltk.pos_tag(userInput)
    truth = False
    for i in range(len(userInput)):
        a = userInput[i]
        if (a[1] == '$'):
            truth = True
    return truth


# method to check for year inputs

def checkForNum(userInput):
    userInput = nltk.word_tokenize(userInput)
    userInput = nltk.pos_tag(userInput)
    truth = False
    for i in range(len(userInput)):
        a = userInput[i]
        if (a[1] == 'CD' and len(a[0]) == 4 and (a[0][0] == '2' or a[0][0] == '1')):
            truth = True
    return truth


# method to check polarity of the user input

def checkPolarity(userInput):
    analyzer1 = SentimentIntensityAnalyzer()
    text = analyzer1.polarity_scores(userInput)
    truth = False
    if text['compound'] < -0.299:
        truth = True
    return truth

# this just adds commas based on simple rules
def addComma(text):
    parsed_text = text.split(' ')
    i = 0
    for word in parsed_text:
        if word == 'yes':
            parsed_text[i] = 'yes,'
        if word == 'no':
            parsed_text[i] = 'no,'
        i+=1
    return ' '.join(parsed_text)



# this function replaces words with synonyms and tries to converse with them
# if no synonym is found, it will output the default reply
def tryConverseWithSynonyms(userIn):
    dictionary = PyDictionary()
    tokens = word_tokenize(userIn)
    words = nltk.pos_tag(tokens)
    queue = []
    # add original input to queue
    queue.append(userIn)
    i = 0
    for word in words:
        toMutate = tokens
        # to prevent long 'thinking' times we will only try changing adjectives, and verbs
        
        if 'JJ' in word[1] or 'VB' in word[1]: 
            # get all the synsets of the adjectives and verbs
            synset = dictionary.synonym(word[0])
            # mutate the original sentence with the synonyms
            for synonym in synset:
                toMutate[i] = synonym
                # This monster just detokenizes a string
                mutated = "".join([" "+i if not i.startswith("'") and i not in string.punctuation else i for i in tokens]).strip().lower()
                # add the mutated sentence to the queue
                if mutated not in queue:
                   queue.append(mutated)
        i+=1
    # iterate through the queue
    while len(queue) != 0:
        test = queue.pop()
        # try to converse with the mutated sentence
        reply = chatbot.converse(test)
        # if it is not understood the next mutated sentence
        sorry = word_tokenize(reply)
        if sorry[0] != "Sorry":
            return reply
    return 'Sorry can you try again, I do not understand'
       

# This function retrieves the userInput and then passes it to the console
def sendClick():
    userInput = mesWin.get("1.0", END)
    userInput = userInput
    text = word_tokenize(userInput)
    print(nltk.pos_tag(text))
    words = nltk.pos_tag(text)    
    userInput = addComma(userInput)
    mesWin.delete("1.0", END)
    truth = checkForCurrency(userInput)
    truth1 = checkForNum(userInput)
    truth2 = checkPolarity(userInput)
    if (truth == True):
        reply = "Sorry. I don't understand currency well. Can you try again?"
    else:
        if (truth1 == True):
            reply = "Sorry, I am unfamiliar with that year. Can you try again?"
        else:
            if (truth2 == True):
                reply = "Well that does not seem very nice!"
            else:
                reply = tryConverseWithSynonyms(userInput)
    output = ""
    chatWin.configure(state="normal")
    if "To begin" in chatWin.get("1.0", END):
        chatWin.delete("1.0", END)
        output = userInput + "\n                        " + reply + "\n"
    else:
        output = "\n" + userInput + "\n        " + reply + "\n"
    chatWin.insert(END, output)
    chatWin.see(END)
    chatWin.configure(state="disabled")




# generate the  and run the chat interface
def beginClick():
    begin.destroy()
    # place the Chat window
    chatWin.place(x=6, y=6, height=385, width=562.5)
    # place the message window
    mesWin.place(x=128, y=400, height=88, width=440)
    mesWin.place(x=6, y=400, height=88, width=440)
    # Button to send your message
    sendIn = Button(root, text="Send", width=12, height=5, bd=0, bg="#0080FF", activebackground="#00BFFF",
                    foreground="#FFFFFF", font=("Arial", 12), command=sendClick)
    sendIn.place(x=455, y=400, height=88)


# this section is where the GUI will be built
root = Tk()
root.title("Chatbot")
root.geometry("575x500")
root.resizable(width=FALSE, height=FALSE)

# this section is textboxes that will be placed by the beginClick function
# chat window
chatWin = Text(root, bd=1, bg="black", width=50, height=8, font=("Arial", 25), foreground="#00FFFF", wrap=WORD)
chatWin.insert(END, "To begin chatting type your message into the textbox on the bottom\n")
chatWin.configure(state="disabled")
# Message window
mesWin = Text(root, bd=0, bg="black", width="30", height="4", font=("Arial", 23), foreground="#00ffff")

# generate the menu at the top
makeMenu()

# these are conversation pairs
pairs = [
    ['Hello|Hi', ['Hi, what is your name?']],
    ['my name is (.*)', ['Hello %1, my name is sports bot. Do you play any sports']],
    ['(.*) play (.*)', ['Thats so cool! I used to play %2 as well. Do you watch %2?']],
    ['yes, i watch (.*)', ['Who is your favourite player?']],
    ['No, i do not watch (.*)', ['Really? What sport do you watch']],
    ['i do not watch (.*)', ['Really? What sport do you watch']],
    ['i watch (.*)', ['Who is your favourite player?']],
    ['my favourite player is (.*)', ['%1? I have never heard of him, how many points a game do they score?']],
    ['(.*) scores (.*)', ['Thats not too bad but I bet I could beat him 1 on 1']],
    ['No, you could not', ['Yes I could, how many points can you score in your sport?']],
    ['Yes, you could', ['I know, how many points can you score in your sport?']],
    ['I can score (.*)', ['You can score %1? How old are you?']],
    ['i am (.*) years old',
     ['I guess thats not bad for a %1 year old. Is there anything you want to ask me regarding sports?']],
    ['(.*) favourite sport?', ['Hockey, anything else?']],
    ['(.*) old are you?', ['I am a bot I do not age']],
    ['(.*) favourite player?',
     ['Loui Erikkson of the Vancouver Canucks, he definitely deserves his $36 million contract']],
    ['(.*) to a game?', ['No, I am a bot. I am unable to be physically anywhere.']],
    ['(.*) Stanley Cup this year?', ['Any team but Vancouver']],
    ['(.*) watch the game last night?',
     ['I did not watch it, but all the stats automatically uploaded to my personal hard drive']],
    ['(.*) next summer olympics?', ['This summer in Tokyo']],
    ['(.*) next winter olympics?', ['2022 in Beijing']],
    ['(.*) most gold medals?', ['Michael Phelps with 23.']],
    ['how are you?', ['I am well. And you?']],
    ['i am (.*)', ['Alright']],
    ['when is the next world cup?', ['Next year in Qatar']],
    ['who will win the next world cup?', ['Canada, no doubt. They are a soccer powerhouse']],
    ['who are you', ['I am sports bot. It is my duty to assist you in anything related to sports.']],
    ['(.*) favourite team?', ['I have no allegiance to any sports organization']],
    ['(.*) favourite basketball player?', ['The legend Alex Caruso']],
    ['(.*) favourite goal of all time?', ['Any of Loui Erikksons empty nets']],
    ['who is the most well known canadian hockey player', ['That is Wayne Gretzky easily']],
    ['how many hockey players can you name', ['I can name about 10 or so do you want me to name them all?']],
    ['yes, name them all', [
        'Okay then we have Wayne Gretzky, Sidney Crosby, Alexander Ovechkin, Patrick Kane, Jonathan Toews, Steven Stamkos, Robert Orr, Gordie Howe, P. K. Subban, and finally Tim Hortons']],
    ['who made you (.*)', ['I was made by Keegan Wright, Jivraj Grewal, Owen Spicker, Brenden Trieu, and Hassan Brar']],
    ['what year is it', ['The current year is 2021 as of my last update']],
    ['what stopped sports last year',
     ['The COVID-19 pandemic halted everything for a while but we are slowly recovering']],
    ['(.*) do you think i will get better if i practice sports',
     ['As they say practice makes perfect but remember Rome was not built in a day so it may take some time']],
    ['(.*) win the premier league this year?',
     ['It is looking increasingly likely that Manchester City will win the title.']],
    ['what is the premier league?', ['The Premier League is the top division of soccer in England.']],
    ['(.*) best premier league team?',
     ['All time, Manchester United have won the most titles. But more recently, Manchester City']],
    ['(.*) most premier league goals?', ['Alan Shearer, with 260 goals']],
    ['what is the champions league?',
     ['The UEFA Champions League is an annual soccer competition consisting of the best teams in Europe.']],
    ['(.*) win the champions league this year?', ['At this point, it is too close to determine.']],
    ['(.*) best champions league team?', ['All time, Real Madrid have been the most successful team with 13 titles.']],
    ['(.*) most champions league goals?', ['Cristiano Ronaldo, with 134 goals and counting']],
    ['(.*) favourite soccer player?', ['Adebayo Akinfenwa']],
    ['(.*) best soccer player ever?', ['Many have said Pele, however no one has ever been as good as Messi']],
    ['(.*) best soccer team in Canada?', ['Vancouver Whitecaps']],
    ['(.*) best canadian soccer player?', ['Alphonso Davies']],
    ['(.*) the weather outside?', ['I do not know, ask me about sports']],
    ['(.*) cars (.*)', ['Why are you asking me about cars. I am a sports bot']],
    ['(.*) favourite food (.*)', ['I do not eat food. I am a bot. Ask me something else']],
    ['(.*) computers (.*)?', ['Ask me about sports. I can not understand anything else but sports']],
    ['(.*) clothes (.*)?', ['I am not a fashion bot. I am sports bot, ask about topics related to sports']],
    ['', ['Sorry can you try again, I do not understand']],
    ['(.*)', ['Sorry can you try again I do not understand']],
]

# Entry Screen
# When this button is clicked it will call the beginClick function to generate the chat interface
chatbot = modifiedChat(pairs, reflections)

begin = Button(text="Click me to begin chatting with SportBot!", width=400, height=500, bg="white", fg="black",
               command=beginClick, font=("Arial", 20))
begin.pack()

# when the code reaches this point it begins to loop a chat


root.mainloop()
