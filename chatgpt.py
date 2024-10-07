import openai

def chat_with_gpt(api_key):
    openai.api_key = api_key
    print("Hello! Welcome to ChatGPT (By OpenAI), type 'gpt.quit' to quit the program.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == "gpt.quit":
            print("Exiting the chat. Goodbye!")
            break
        
        try:
            # Call the OpenAI API
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  # or another model like "gpt-4"
                messages=[
                    {"role": "user", "content": user_input}
                ]
            )

            # Extract the assistant's response
            chatgpt_response = response['choices'][0]['message']['content']
            print(f"ChatGPT: {chatgpt_response}")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    api_key = input("Please enter your OpenAI API key: ")
    chat_with_gpt(api_key)
