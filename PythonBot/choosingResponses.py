import random

responses = {
    "What's your name?":["My name is EchoBot",
                         "They call me EchoBot",
                         "The name's Bot, EchoBot"]
    }


def respond(message):
    if message in responses:
        return random.choice(responses[message])



print(respond("What's your name?"))
