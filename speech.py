import pyttsx3

speech = pyttsx3.init()

en_voice = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
speech.setProperty('voice', en_voice)

speech.setProperty('rate', 150)    # Speed percent (can go over 100)
speech.setProperty('volume', 0.5)  # Volume 0-1
#speech.say('Hello with my new voice')

speech.runAndWait()
#
# import pyttsx3
# def onStart(name):
#    print('starting', name)
# def onWord(name, location, length):
#    print('word', name, location, length)
# def onEnd(name, completed):
#    print('finishing', name, completed)
# engine = pyttsx3.init()
# engine.connect('started-utterance', onStart)
# engine.connect('started-word', onWord)
# engine.connect('finished-utterance', onEnd)
# engine.say('The quick brown fox jumped over the lazy dog.')
# engine.runAndWait()

#
# # voice = speech.getProperty('voice')
# #
# # rate = speech.getProperty('rate')
# #
# # volume = speech.getProperty('volume')
# #
# #
# # print('voice', voice, 'rate',str(rate), 'volume ', str(volume))
#
# import pyttsx3
# def onWord(name, location, length):
#    print('word', name, location, length)
#    if location > 10:
#       engine.stop()
# engine = pyttsx3.init()
# engine.connect('started-word', onWord)
# engine.say('The quick brown fox jumped over the lazy dog.')
# engine.runAndWait()
