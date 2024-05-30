import pickle

# Initialize a dictionary to store user details
user_details = {}

# Load existing user details if available
try:
    with open('user_details.pkl', 'rb') as f:
        user_details = pickle.load(f)
except FileNotFoundError:
    pass

# Function to save user details
def save_user_details():
    with open('user_details.pkl', 'wb') as f:
        pickle.dump(user_details, f)

# Function to greet the user
def greet():
    print("Hello! What's your name?")

# Function to ask basic details
def ask_basic_details(user_name):
    details = {}
    details['age'] = ask_detail("How old are you? ")
    details['hobbies'] = ask_detail("What are your hobbies? ")
    details['idol'] = ask_detail("Who is your idol? ")
    user_details[user_name] = details
    save_user_details()

def ask_detail(question):
    response = input(question).strip()
    return response

# Function to generate a friendly error response
def friendly_error_response():
    return "I'm not sure how to respond to that. Maybe try asking something else? 😊"

# Function to generate a farewell message
def farewell_message():
    return "Goodbye! Have a great day! 🌟"

# Function to respond with user details
def respond_with_details(user_name):
    details = user_details.get(user_name, {})
    if details:
        detail_str = ", ".join([f"{key.capitalize()}: {value}" for key, value in details.items()])
        return f"Here's what I know about you, {user_name}: {detail_str}."
    else:
        return "I don't have any details saved for you."

# Function to respond to basic questions
def respond_to_basic_question(user_message):
    basic_responses = {
        "how are you": "I'm just a bot, but I'm doing great! How can I assist you today?",
        "what is your name": "I'm Chatbot, your friendly assistant!",
        "what can you do": "I can chat with you, remember details about our conversations, and try to help with your questions.",
        "how is the weather": "I'm not connected to the internet right now, so I can't check the weather. But I hope it's nice where you are!",
        "tell me a joke": "Why don't scientists trust atoms? Because they make up everything! 😄"
    }
    
    # Check for keywords in the user message
    for keyword, response in basic_responses.items():
        if keyword in user_message:
            return response
    
    return friendly_error_response()

# Chatbot main function
def chatbot():
    wakeup_call = "chatbot"
    print(f"Type '{wakeup_call}' to start chatting with me!")

    while True:
        user_input = input("You: ").strip().lower()
        if user_input == wakeup_call:
            greet()
            user_name = input("You: ").strip()
            if user_name.lower() == "quit":
                print(farewell_message())
                break

            if user_name not in user_details:
                print(f"Nice to meet you, {user_name}! Let me get to know you better.")
                ask_basic_details(user_name)
            else:
                print(f"Welcome back, {user_name}!")

            print("How was your day?")
            input("You: ").strip()  # Ignore this input for now

            print("How can I help you today?")
            while True:
                user_message = input("You: ").strip().lower()
                if user_message == "quit":
                    print(farewell_message())
                    break
                elif "tell me what you know about me" in user_message:
                    print("Bot:", respond_with_details(user_name))
                else:
                    response = respond_to_basic_question(user_message)
                    print("Bot:", response)

        elif user_input == "quit":
            print(farewell_message())
            break
        else:
            print("Please type the wakeup call to start chatting.")

chatbot()
