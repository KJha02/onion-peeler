import random
from time import sleep


def peel_onion():
    time = 0
    jarvis_responses = ["Ahh I see. Why do you feel that way?",
                        "Why might you think that?",
                        "What may be motivating these thoughts?",
                        "Why is that?",
                        "Why?"]
    for i, response in enumerate(jarvis_responses):
        jarvis_responses[i] = '\n' + response + '\n\n'
    while True:
        if time == 0:
            usr_response = input("Hello! Thanks for being here today. What's on your mind? \n"
                                 "What are you feeling? Is there anything bothering you? \n"
                                 "Press a single key followed by enter to end the session.\n\n")
        else:
            jarvis_response = jarvis_responses[random.randint(0, len(jarvis_responses) - 1)]
            usr_response = input(jarvis_response)
        if len(usr_response) <= 1:
            print("Thank you for speaking with me today")
            break
        time += 1
        sleep(5)


peel_onion()
