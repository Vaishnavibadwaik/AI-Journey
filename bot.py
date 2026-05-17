import random

print("🤖 Chatbot: Hello! Type 'help' to see options.")
print("Type 'bye' to exit.\n")

while True:

    user_input = input("You: ").lower()

    # Exit
    if user_input == "bye":
        print("🤖 Chatbot: Goodbye 😊")
        break

    # Help Menu
    elif user_input == "help":
        print("""
Available Commands:
- hello / hi
- how are you
- joke
- fact
- your name
- bye
""")

    # Greeting
    elif user_input in ["hello", "hi", "hey"]:
        responses = ["Hello!", "Hi there!", "Hey!"]
        print("🤖 Chatbot:", random.choice(responses))

    # How are you
    elif "how are you" in user_input:
        print("🤖 Chatbot: I am fine. Thanks for asking!")

    # Joke
    elif "joke" in user_input:
        print("🤖 Chatbot: Why do programmers prefer dark mode? Because light attracts bugs!")

    # Fact
    elif "fact" in user_input:
        print("🤖 Chatbot: Python is one of the most popular programming languages.")


    # Name
    elif "your name" in user_input:
        print("🤖 Chatbot: I am RuleBot.")

    # Default response
    else:
        print("🤖 Chatbot: Sorry, I don't understand that.")