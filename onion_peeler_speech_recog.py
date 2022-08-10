import speech_recognition as sr
from gtts import gTTS
import random
from playsound import playsound
from time import sleep

r = sr.Recognizer()


def peel_onion_audio():
    time = 0
    jarvis_responses = ["Ahh I see. Why do you feel that way?",
                        "Why might you think that?",
                        "What may be motivating these thoughts?",
                        "Why is that?",
                        "Why?"]
    while True:
        # what will the output be
        if time == 0:
            jarvis_prompt = "Hello! Thanks for being here today. \n" \
                            "For all of your responses, press enter when you're done speaking, or say 'end.' To exit the program, say 'quit.' \n" \
                            "What's on your mind?"
        else:
            jarvis_prompt = jarvis_responses[random.randint(0, len(jarvis_responses) - 1)]
        print("J.A.R.V.I.S.: " + jarvis_prompt)  # print output of program
        jarvis_prompt = gTTS(text=jarvis_prompt, lang='en')  # convert output from text to speech
        jarvis_prompt.save('audio/jarvis_response.mp3')
        playsound("audio/jarvis_response.mp3")

        with sr.Microphone() as source:  # listen to user response
            usr_audio = r.listen(source)

        usr_response = r.recognize_google(usr_audio)
        if "quit" in usr_response:  # condition for breaking
            break
        usr_response = "Me: " + usr_response + "\n"
        print(usr_response)  # display user response so that they can reflect on what they said
        time += 1
        sleep(3)  # add sleep so that it gives perception of program thinking about response


peel_onion_audio()
