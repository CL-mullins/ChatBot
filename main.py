#TODO: Create a Chatbot to have 'complex' user interactions via Chat format and pop-out window.
from random import choice

def get_chatbot_response(user_response):
    #What do i want Chatbot to say?
    bot_response_sunny = ["It's bright out today! You should wear shorts!", "It's pretty hot out there today, I recommend wearing light clothing!",
                        "The sun is out! Dress in light colors today"]
    bot_response_cloudy = ["Its cloudy today, who knows what will happen! Wear layers.", "Possibility of rain today, make sure to wear a jacket!",
                        "Seems like a good day for some coffee!"]
    bot_response_rainy = ["It's raining today? Remember to bring an umbrella!", "Rainy weather calls for some jazz music and coffee, but most importantly, an umbrella",
                        "Remember to bring an umbrella and some boots!"]
    bot_response_snowy = ["It's snowy today? Better bring your boots!","Snowy day today huh? Better schedule some time to shovel the driveway",
                        "Snowy weather means that it's time to dress in layers"]

    if user_response == "sunny":
            return choice(bot_response_sunny)
    if user_response == "cloudy":
            return choice(bot_response_cloudy)
    if user_response == "rainy":
            return choice(bot_response_rainy)
    if user_response == "snowy":
            return choice(bot_response_snowy)
    else:
            return "No matter what, you can have a good day today!"



print("Welcome to Chatbot!")
print("I will tell you what you should wear based on the weahter!")




#user_response = ""

while True:
    user_response = input("How is the weather today? \n")

          #Quits when user responds with 'goodbye'
    if user_response == 'goodbye' or user_response == 'bye':
            print("Have a good day!")
            break


    bot_response = get_chatbot_response(user_response)
    print(bot_response)


