import re


def swap_pronouns(phrase):
    if "I" in phrase:
        return re.sub("I", "you", phrase)
    if "my" in phrase:
        return re.sub("my", "your", phrase)
    else:
        return phrase






print(swap_pronouns("I walk my dog"))

pattern = "do you remember (.*)"

message = "do you remember when you ate strawberries in the garden?"

match = re.search(pattern,message).group(1)




phrase = swap_pronouns(match)

print(phrase)
