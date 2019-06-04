import chatterbot
from chatterbot import ChatBot
import pyttsx3
import os
import speech as sp
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

# speech = pyttsx3.init()
#
# en_voice = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
# speech.setProperty('voice', en_voice)
#
# speech.setProperty('rate', 150)    # Speed percent (can go over 100)
# speech.setProperty('volume', 0.75)  # Volume 0-1

bot = ChatBot('Eva')

# Create a new instance of a ChatBot
# bot = ChatBot(
#     'Example Bot',
#     #storage_adapter='chatterbot.storage.SQLStorageAdapter',
#     logic_adapters=[
#         # {
#         #     'import_path': 'chatterbot.logic.BestMatch',
#         #     'default_response': 'I am sorry, but I do not understand. type something readable you idiot',
#         #     'maximum_similarity_threshold': 0.90
#         # },
#         # {
#         #     'import_path': 'chatterbot.logic.SpecificResponseAdapter',
#         #     'input_text': 'Who Created you?',
#         #     'output_text': 'God is my creator'
#         # }
#     ]
# )

# for _file in os.listdir('files'):
#     convs = open('files/'+ _file, "r").readlines()


#*******List trainer************
#bot_trainer = ListTrainer(bot)
#bot_trainer.train(convs)

#********Corpus TRainer******************
bot_trainer_con = ChatterBotCorpusTrainer(bot)
bot_trainer_con.train(
    'chatterbot.corpus.english'
    #"chatterbot.corpus.english.greetings",
    #"chatterbot.corpus.english.conversations"exit
)

name = (input('Eva : Tell me your name?\n'))
print("Hi", name, "This is EVA, your personal digital assistant for anything and everything related to Prodapt. Ask me anything")

#sp.speech.say('Hi. This is trisha, your personal digital assistant for anything and everything related to Prodapt. Ask me anything')
#sp.speech.runAndWait()

while True:
    try:
        request = input(name + '-')
        response = bot.get_response(request)
        sp.speech.say(response)
        print("Eva:", response, '\n')
        sp.speech.runAndWait()
    except (KeyboardInterrupt, EOFError, SystemExit):
        break