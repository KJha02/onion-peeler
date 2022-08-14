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
    'max_new_tokens': 10,  # number of generated tokens
    'temperature': 0.1,   # controlling the randomness of generations
    'end_sequence': "###"  # stopping sequence for generation
}

prompt = "M: I'm feeling very angry today" \
         "J: Why?" \
         "###" \
         "M: Because everyone I care about is gone and I'm left unsure of what to do" \
         "J: Why does this seem true?" \
         "###" \
         "M: Because no one texts me anymore and people in my previous relationships said I was manipulative and now I feel like a failure" \
         "J: Why do your previous relationships make you feel like a failure?" \
         "###" \
         "M: Because I am always blamed as the one responsible even though it isn't always me" \
         "J: Why are you taking ownership if the problem isn't all you?" \
         "###" \
         "M: "             # few-shot prompt

# data = query(prompt,parameters)
for i in range(5):
    usr_response = input(prompt)
    prompt = prompt + usr_response + "J: "
    prompt = query(prompt, parameters)
    prompt = prompt + "M: "
