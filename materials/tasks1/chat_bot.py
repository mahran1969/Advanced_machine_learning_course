from mmmm import responses
import random
def get_response(user_input):
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])  
    return random.choice(responses["default"])
class n:
    def chatbot():
        print("Chatbot: Hi! How can I assist you today?")
        
        while True:
            user_input = input("User: ").lower()
            response = get_response(user_input)
            print("Chatbot:", response)
        
            if user_input == "goodbye":
                break
x=n()
print(x.chatbot())