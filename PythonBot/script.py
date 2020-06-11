#Create templates 
bot_template = "BOT : {0}"
user_template = "USER : {0}"

# Define a function that responds to a user's message: respond
def respond(message):
    bot_message = "I can hear you! You said: " + message
    return bot_message

    
#print(respond("Hello"))

# Define a function that sends a message to the bot: send_message
def send_message(message):
    print(user_template.format(message))
    # Get the bot's response to the message
    # Call respond() with the message passed in and save result as response
    response = respond(message) 
    print(bot_template.format(response))


print(send_message("Hello"))
   
 



