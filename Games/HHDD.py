import openai

# initialize the API with your API key
openai.api_key = "YOUR API KEY"

def play_game():
    location = "Vogon spaceship"
    inventory = []
    print("Welcome to the Hitchhiker's Guide to the Galaxy and Dungeon's and Dragons game!")
    print("Please choose your character from the following options:")
    characters = ["Human", "Vogon", "Betelgeusian", "Ford Prefect", "Zaphod Beeblebrox", "Marvin the Paranoid Android", "Trillian"]
    for i, character in enumerate(characters):
        print(f"{i+1}. {character}")
    character_choice = int(input("Please select a character number: "))
    character = characters[character_choice - 1]
    print(f"You have chosen to play as a {character}")
    while True:
        user_input = input("What do you want to do? or type 'exit' to quit the game: ")
        if user_input.lower() == "exit":
            break
        prompt = f"{character} is currently in {location} and has {inventory} in his possession. He wants to {user_input} options:"
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
        if "You used the towel" in choice_text:
            inventory.remove("towel")
        elif "You picked up a" in choice_text:
            item = choice_text.split("You picked up a ")[1]
            inventory.append(item)
    print("Thanks for playing!")

play_game()

