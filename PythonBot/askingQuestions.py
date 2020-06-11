import random

#responses = ["Tell me more!","Why do you think that?", "I'm good, how r u?"]
responses = ("Gist me more!","How do you think that?", "I'm better, how r u?")


def respond(message):
    return random.choice(responses)


#print(respond("I think you're really great"))

print(respond(responses))
