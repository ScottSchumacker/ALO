# Scott Schumacker
# Basic chatbot script

# Importing libraries
import random

# Greetings section
Greetings = ['hello', 'hi', 'hey', "whats up", "what's up", "good morning", "good afternoon",
             "good evening", "good night", "good day"]
greetingResponse = ["Hello!", "How are you?", "Hi!", "Hey!", "Whats up?"]

# Name section
Name = ["whats your name", "what is your name",'your name', 'what are you called by', 'reference number', 'who are you', 'what is your first name']
nameResponse = ['My name is ALO', 'Hello, I am ALO', "I am ALO", "You can call me ALO", "I'm ALO"]

# Feelings section
Feeling = ["how are you feeling?", "how are you?", "how do you feel?", "are you happy?", "are you sad?",
           'are you angry?', "what do you feel?"]
feelingResponse = ["I am doing well", "I have been better", "I am great!", "I am happy", "I am sad"]

# Likes = []

# Creating a variable to leave the chat
leave = "bye"

# Creating a loop to chat with ALO
while True:
    inp = input("You:").lower()
    if inp == leave:
        print("Good bye. I hope to chat soon!")
        break
    elif str(inp) in Greetings:
        print(random.choice(greetingResponse))
    elif str(inp) in Name:
        print(random.choice(nameResponse))
    elif str(inp) in Feeling:
        print(random.choice(feelingResponse))