import random
from time import sleep


def peel_onion():
    time = 0
    jarvis_responses = ["Ahh I see. Why do you feel that way?",
                        "Why might you think that?",
                        "What may be motivating these thoughts?",
                        "Why is that?",
                        "Why?"]
    for i, response in enumerate(jarvis_responses):  # formatting stuff
        jarvis_responses[i] = '\n' + response + '\n\n'
    while True:
        # generate responses for program
        if time == 0:
            jarvis_prompt = "Hello! Thanks for being here today. What's on your mind? \n" \
                            "What are you feeling? Is there anything bothering you? \n"
        else:
            jarvis_prompt = jarvis_responses[random.randint(0, len(jarvis_responses) - 1)]
        usr_response = input(jarvis_prompt)  # get user's input as text
        if len(usr_response) <= 1:  # condition for breaking
            print("Thank you for speaking with me today")
            break
        time += 1
        sleep(3)  # gives the impression of thinking


peel_onion()
