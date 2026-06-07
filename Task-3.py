# ============================================
# RULE-BASED CHATBOT USING PYTHON
# Beginner-Friendly AI Internship Project
# ============================================

# Function to respond to user messages
def chatbot_response(user_input):

    # Convert input to lowercase for easy matching
    user_input = user_input.lower()

    # Greeting responses
    if user_input in ["hello", "hi", "hey"]:
        return "👋 Hello! Nice to meet you."

    # Asking chatbot name
    elif "your name" in user_input:
        return "🤖 My name is CodSoft Chatbot."

    # Asking chatbot condition
    elif "how are you" in user_input:
        return "😊 I'm doing great! Thanks for asking."

    # Asking about creator
    elif "who created you" in user_input:
        return "💻 I was created using Python programming."

    # Asking time greeting
    elif "good morning" in user_input:
        return "☀️ Good Morning! Have a wonderful day."

    elif "good night" in user_input:
        return "🌙 Good Night! Sleep well."

    # Asking help
    elif "help" in user_input:
        return "📌 I can chat with you and answer simple questions."

    # Asking about Python
    elif "python" in user_input:
        return "🐍 Python is a popular programming language used in AI and software development."

    # Goodbye condition
    elif user_input in ["bye", "exit", "quit"]:
        return "👋 Goodbye! Have a great day."

    # Default response
    else:
        return "❓ Sorry, I don't understand that."


# Main chatbot program
print("===================================")
print("🤖 WELCOME TO RULE-BASED CHATBOT")
print("===================================")
print("Type 'bye' to exit the chatbot.\n")

# Loop to keep chatbot running
while True:

    # Take user input
    user_message = input("You: ")

    # Get chatbot response
    bot_reply = chatbot_response(user_message)

    # Display response
    print("Bot:", bot_reply)

    # Exit condition
    if user_message.lower() in ["bye", "exit", "quit"]:
        print("🔴 Chatbot session ended.")
        break