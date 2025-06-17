"""
Simple Rule-Based Chatbot

Example Interactions:

You: hello
SimpleChatbot: Hi there! How can I help you today?

You: how are you
SimpleChatbot: I'm doing well, thank you for asking!

You: what is your name
SimpleChatbot: I am a simple chatbot.

You: tell me a joke
SimpleChatbot: Sorry, I don't understand. Could you please rephrase?

You: bye
SimpleChatbot: Goodbye! Have a great day!
"""

# This is an empty Python file.

def get_chatbot_response(user_input):
  """
  Returns a response to the user's input based on predefined rules.
  """
  rules_and_responses = {
      "hello": "Hi there! How can I help you today?",
      "how are you": "I'm doing well, thank you for asking!",
      "bye": "Goodbye! Have a great day!",
      "name": "I am a simple chatbot."
  }

  lower_user_input = user_input.lower()

  for keyword, response in rules_and_responses.items():
    if keyword in lower_user_input:
      return response

  return "Sorry, I don't understand. Could you please rephrase?"

if __name__ == "__main__":
  print("SimpleChatbot: Hello! Type 'quit' or 'exit' to end the chat.")
  while True:
    user_input = input("You: ")
    if user_input.lower() in ["quit", "exit"]:
      print("SimpleChatbot: Goodbye!")
      break
    response = get_chatbot_response(user_input)
    print(f"SimpleChatbot: {response}")
