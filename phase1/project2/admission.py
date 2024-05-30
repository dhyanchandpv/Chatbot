import json
from googleapiclient.discovery import build

# Initialize Google Custom Search client
def google_search(query, api_key, cse_id, num=1):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=query, cx=cse_id, num=num).execute()
    return res['items'][0]['snippet'] if 'items' in res else None

GOOGLE_API_KEY = 'AIzaSyD4wcI0gU2Y1kL3Dx-JtQr_Iq14gphsPA8'
GOOGLE_CSE_ID = 'd5099cbcfeb7445d3'
# OPENAI_API_KEY = 'your-openai-api-key'

# Function to load basic responses from JSON file
def load_basic_responses(filepath):
    with open('C:/Users/dhyan/Downloads/chatbot/admission_responses.json', 'r') as f:
        data = json.load(f)
    return {item['question']: item['answer'] for item in data['responses']}

# Load basic responses
basic_responses = load_basic_responses('basic_responses.json')

# Function to get response from GPT-3.5
# def get_gpt3_response(prompt):
#     openai.api_key = OPENAI_API_KEY
#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=[{"role": "user", "content": prompt}]
#     )
#     return response.choices[0].message.content.strip()

# Function to respond to basic questions
def respond_to_basic_question(user_message):
    for question, answer in basic_responses.items():
        if question in user_message:
            return answer

    # If the question doesn't match any basic question, use Google Custom Search
    google_response = google_search(user_message, GOOGLE_API_KEY, GOOGLE_CSE_ID)
    if google_response:
        return google_response

    # Default friendly error response
    return friendly_error_response()

# Function to generate a friendly error response
def friendly_error_response():
    return "I'm not sure how to respond to that. Maybe try asking something else? 😊"

# Function to generate a farewell message
def farewell_message():
    return "Goodbye! Have a great day! 🌟"

# Chatbot main function
def chatbot():
    wakeup_call = "chatbot"
    print(f"Type '{wakeup_call}' to start chatting with me!")

    while True:
        user_input = input("You: ").strip().lower()
        if user_input == wakeup_call:
            print("Hello! What's your name?")
            user_name = input("You: ").strip()
            if user_name.lower() == "quit":
                print(farewell_message())
                break

            print(f"Welcome, {user_name}!")

            print("How can I help you today?")
            while True:
                user_message = input("You: ").strip().lower()
                if user_message == "quit":
                    print(farewell_message())
                    break
                else:
                    response = respond_to_basic_question(user_message)
                    print("Bot:", response)

        elif user_input == "quit":
            print(farewell_message())
            break
        else:
            print("Please type the wakeup call to start chatting.")

chatbot()
