# Scott Schumacker
# Basic chatbot script

# Importing libraries
import random
import reference

# Creating a variable to leave the chat
leave = "bye"

# Creating a loop to chat with ALO
while True:
    inp = input("You:").lower()
    if inp == leave:
        print("Good bye. I hope to chat soon!")
        break
    elif str(inp) in reference.Greetings:
        print(random.choice(reference.greetingResponse))
    elif str(inp) in reference.Name:
        print(random.choice(reference.nameResponse))
    elif str(inp) in reference.Feeling:
        print(random.choice(reference.feelingResponse))