from datetime import datetime
import random

responses = {
    "hello": "Hello! How can I help you?",
    "hi": "Hi! Nice to meet you.",
    "hey": "Hey there!",
    "how are you": "I am doing great. Thanks for asking!",
    "name": "My name is CodSoft AI ChatBot.",
    "python": "Python is a popular programming language used in AI, Machine Learning, and Data Science.",
    "ai": "Artificial Intelligence enables machines to learn, think, and make decisions.",
    "course": "I can help you with Python, AI, Machine Learning, and Programming basics.",
    "thank you": "You're welcome! Happy to help.",
    "thanks": "You're welcome!"
}

jokes = [
    "Why do programmers love Python? Because it is simple and powerful!",
    "Why was the computer cold? It left its Windows open!",
    "Why do Java developers wear glasses? Because they don't C#!",
    "Why did the programmer quit his job? Because he didn't get arrays.",
    "Why do programmers prefer dark mode? Because light attracts bugs.",
    "Why was the computer late? It had a hard drive.",
    "Why don't robots get scared? They have nerves of steel.",
    "Why did the AI go to school? To improve its neural network.",
    "Why was the keyboard always tired? Because it had too many shifts.",
    "Why did the computer go to the doctor? It caught a virus.",
    "What is a programmer's favorite snack? Computer chips.",
    "Why did the laptop break up with the charger? There was no connection.",
    "Why did the student bring a ladder to class? To reach the next level.",
    "Why was the math book sad? Because it had too many problems.",
    "Why did the smartphone need glasses? It lost its contacts.",
    "Why do Python programmers make good friends? They are easy to understand.",
    "Why did the computer sneeze? It had a bad cache.",
    "What do you call an intelligent robot? A smartie-bot.",
    "Why did the coder bring a pencil? To draw conclusions.",
    "Why don't computers ever get hungry? They always have bytes.",
    "Why was the internet slow? It was stuck in traffic.",
    "Why did the robot become a musician? It had perfect timing.",
    "Why did the computer laugh? Someone cracked a good byte.",
    "What do computers eat for lunch? Microchips.",
    "Why was the monitor happy? It finally found its resolution."
]

print("=" * 55)
print("🤖 WELCOME TO CODSOFT AI CHATBOT 🤖")
print("=" * 55)
print("Type 'help' to see available commands.")
print("Type 'bye' to exit.\n")

while True:
    user_input = input("You: ").lower().strip()

    if user_input in ["bye", "exit", "quit"]:
        print("Bot: Goodbye! Have a wonderful day. 👋")
        break

    elif user_input == "help":
        print("\n📋 Available Commands:")
        print("- hello / hi / hey")
        print("- how are you")
        print("- what is your name")
        print("- time")
        print("- date")
        print("- joke")
        print("- tell me 5 jokes")
        print("- python")
        print("- ai")
        print("- course")
        print("- thanks")
        print("- bye\n")

    elif user_input == "time":
        current_time = datetime.now().strftime("%H:%M:%S")
        print(f"Bot: Current Time is {current_time}")

    elif user_input == "date":
        current_date = datetime.now().strftime("%d-%m-%Y")
        print(f"Bot: Today's Date is {current_date}")

    elif user_input == "joke":
        print("Bot:", random.choice(jokes))

    elif "5 jokes" in user_input:
        print("\n😂 Here are 5 random jokes:\n")
        for joke in random.sample(jokes, 5):
            print("•", joke)

    else:
        found = False

        for key in responses:
            if key in user_input:
                print("Bot:", responses[key])
                found = True
                break

        if not found:
            print("Bot: Sorry, I don't understand that.")
            print("Bot: Type 'help' to see available commands.")

print("\n✅ ChatBot Closed Successfully.")