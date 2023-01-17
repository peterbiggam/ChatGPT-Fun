import openai

openai.api_key = "YOUR_API_KEY"

def communicate_with_openai():
    # Ask the user for their name
    name = input("What is your name? ")
    
    # Greet the user
    print("Hi " + name + ", How can I assist you today?")
    
    while True:
        # Get the user's prompt
        prompt = input(name + ": ")
        
        # Use the OpenAI API to generate a response
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt='Hi ' + name + ', ' + prompt
        )
        
        # Print the response
        print("OpenAI: " + response["choices"][0]["text"])

# Call the function to start communicating with OpenAI
communicate_with_openai()