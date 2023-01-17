import openai

# initialize the API with your API key
openai.api_key = "YOUR API KEY"

def play_game():
    location = "Vogon spaceship"
    inventory = []
    print("Welcome to the Hitchhiker's Guide to the Galaxy game!")
    print(f"You are currently in {location}")
    print("You must find a way to escape the ship before the Vogons destroy it.")
    while True:
        user_input = input("What do you want to do? or type 'exit' to quit the game: ")
        if user_input.lower() == "exit":
            break
        prompt = f"Arthur Dent is currently in {location} and has {inventory} in his possession. He wants to {user_input} options:"
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=150,
            temperature=0.5,
            n=4, 
        )
        for i in range(4):
            print(f"{i+1}. {response['choices'][i]['text']}")
        choice = int(input("Please select an option number: "))
        choice_text = response["choices"][choice-1]["text"]
        print(choice_text)
    print("Thanks for playing!")

play_game()
