import json
import pdb
import config
import requests

API_TOKEN = config.LM_API_KEY

def query(payload='',parameters=None,options={'use_cache': False}):
    API_URL = "https://api-inference.huggingface.co/models/EleutherAI/gpt-neo-2.7B"
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    body = {"inputs":payload,'parameters':parameters,'options':options}
    response = requests.request("POST", API_URL, headers=headers, data= json.dumps(body))
    try:
      response.raise_for_status()
    except requests.exceptions.HTTPError:
        return "Error:"+" ".join(response.json()['error'])
    else:
      return response.json()[0]['generated_text']

parameters = {
    'max_new_tokens': 15,  # number of generated tokens
    'temperature': 0.1,   # controlling the randomness of generations
    'end_sequence': "###"  # stopping sequence for generation
}

prompt = "Ask creative variations of the question 'Why?': \n" \
         "M: I'm feeling very angry today \n" \
         "J: Why?\n" \
         "###\n" \
         "M: Because everyone I care about is gone and I'm left unsure of what to do\n" \
         "J: Why does this seem true?\n" \
         "###\n" \
         "M: Because no one texts me anymore and people in my previous relationships said I was manipulative and now I feel like a failure\n" \
         "J: Why do your previous relationships make you feel like a failure?\n" \
         "###" \
         "M: Because I am always blamed as the one responsible even though it isn't always me\n" \
         "J: Why are you taking ownership if the problem isn't all you?\n" \
         "###\n" \
         "M: I'm not too sure. I always try to fix the problems of the people I care about because it hurts seeing them in pain, and it never works out\n" \
         "J: Why do you believe you are able to fix the problems of other people?\n" \
         "###\n" \
         "M: "             # few-shot prompt

usr_prompt = ""
t = 0
while True:
    if t == 0:
        x = input("J: Hello, what's on your mind?\nM: ")
    else:
        x = input(usr_prompt)
    if x == 'q': break
    temp = prompt + x + '\n'
    n = len(temp)
    temp += 'J:'
    jarvis = query(temp, parameters)
    jarvis = jarvis[n:]
    if jarvis[-3:] == '###':
        jarvis = jarvis[:-3]
    usr_prompt = jarvis + "\nM: "
    t += 1
