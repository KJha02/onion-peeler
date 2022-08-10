# Onion Peeler
Onions are stinky and can cause problems. Peeling them is a way to get rid of them. Warning, the process may cause a few tears.

## Day 1: Making a basic responder
This is a *very* simple version, but it gets the job done for today. You are prompted to share your thoughts and feelings as explicitly as you want. The program won't judge. It then randomly chooses from the list of premade responses, all of which are different ways of asking the question "why." Here is an image of the program in action:

<img width="1037" alt="onion_basic" src="https://user-images.githubusercontent.com/78826759/183795809-28538d81-9dc9-4bde-a2e3-41ca1b8eeb46.png">

Some ways I want to take this further: 

- Integrate speech recognition so that you don't have to type things out. Also have text to speech for the program's asking of "why."
- Adapt GPT-3 or GPT-Neo to the program so that the specific formulations of "why" are a little more context dependent.
- Build a GUI for all of this so that you don't have to simply type into a terminal and can maybe look at a calming image or looped video while expressing your thoughts.

## Day 2: Adding in speech recognition
Took the basics from the previous day and built in speech recognition features. The user can now speak their responses, and the computer will reply with verbal responses as well. Relying on APIs from Google for text-to-speech and also speech recognition. Here is a gif of the current setup:

![speech_recog](https://user-images.githubusercontent.com/78826759/183814696-873df9e8-5b7a-4cf1-a5bf-e90ea8eea173.gif)

The next steps will be adapting a language model to give more dynamic responses to the user's inputs. I'll start on the simple text paradigm created on day 1, and then see if any major adaptations need to be made for using the transformers with speech recognition.
