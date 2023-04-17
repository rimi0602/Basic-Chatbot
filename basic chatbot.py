import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    ["my name is (.*)", ["Hello %1, how can I help you?"]],
    ["hi|hello|hey", ["Hi there, how can I assist you?"]],
    ["what is your name?", ["My name is ChatBot."]],
    ["how are you?", ["I'm doing well, thank you! How can I assist you?"]],
    ["bye|goodbye", ["Goodbye, have a nice day!"]],
    ["(.*) help (.*)", ["Sure, I'd be happy to help. How can I assist you?"]],
    ["wish me luck", ["all the best for your NLP presetation"]],
    ["What day is today??", ["Your goodluck day"]],
]

chatbot = Chat(pairs, reflections)

def chat():
    print("Welcome to ChatBot! Please enter your message to begin.")
    chatbot.converse()

if __name__ == "__main__":
    chat()
