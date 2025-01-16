import random

# Predefined virtual assistant names and responses
assistant_names = ["AI Arman", "AI Steve", "AI Harry"]

predefined_responses = {
    "how are you": "I'm doing well, thank you!",
    "library": "The library is open 24/7 during exam periods and you can join anytime soon.",
    "admission": "Admissions can be applied for through our online portal or can be done through physical presence.",
    "scholarship": "Scholarship applications are accepted until the end of Jan."
    
}

# Generic fallback responses for unrecognized input
fallback_responses = [
    "Wow you said something that is out of my aresnal! Anything else I can help with?",
    "I'm not sure about that. You might find more information from Mr. Arman himself!"
]

# Function to select a random assistant name
def get_random_assistant_name():
    """Selects and returns a random assistant name."""
    return random.choice(assistant_names)

# Function to detect keywords in the user's input and provide an appropriate response
def get_response(user_message):
    """Checks for predefined keywords in the user's message and returns the appropriate response. 
    If no keyword is found, returns a fallback response.

    Args:
        user_message (str): The user's input message.

    Returns:
        str: The response message.
    """
    for keyword, reply in predefined_responses.items():
        if keyword in user_message.lower():
            return reply
    return random.choice(fallback_responses)

# Main chat function
def chat_system():
    """Handles the interactive chat session with the user."""
    # Greet the user and introduce the chat system
    user_name = input("Welcome! Please enter your name: ")
    print(f"Hello, {user_name}! Welcome to the Assistant Chat of Arman through AI.")

    # Introduce the virtual assistant
    assistant_name = get_random_assistant_name()
    print(f"My name is {assistant_name}, and I'm here to assist you today.")

    # Interactive chat loop
    while True:
        user_message = input(f"{user_name}: ")

        # Exit the chat if the user types a termination keyword
        if user_message.lower() in ["bye", "quit", "exit"]:
            print(f"{assistant_name}: Goodbye, {user_name}! Have a wonderful day!")
            break

        # Generate and display a response based on the user's input
        response = get_response(user_message)
        print(f"{assistant_name}: {response}")

# Run the chat system if the script is executed
if __name__ == "__main__":
    chat_system()