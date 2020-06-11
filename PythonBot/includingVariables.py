responses = {
    "What's today's weather?":"it's {} today"
    }


weather_today = "cloudy"

def respond(message):
    if message in responses:
        return responses[message].format(weather_today)



print(respond("What's today's weather?"))
