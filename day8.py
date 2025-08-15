print("chatbot: Hello! I'm your chatbot.")

while True:
    i = input("you:").lower()

    if i == 'hello' or i == 'hi':
        print('chatbot: Hi there! How can i help you?')

    elif 'manhuas' in i:
        print("Chatbot: Sure, here are some reccomendations:")
        print("1. Asurascans")
        print("2. Flamecomics")
        print("3. Drakescans")
        print("4. MangaDex")

    elif "anime" in i:
        print("Chatbot: Sure, here a some reccomendations:")
        print("1. Crunchyroll")
        print("2. Gogoanime.in")
        print("3. Neko")
        print("4. Netflix")

    elif "games" in i:
        print("Sure: here are some recommendations:")
        print("1. Wuthering Waves")
        print("2. Call of Duty")
        print("3. Moco")
        print("4. Snowbreak: Containment Zone")

    elif "songs" in i:
        print("1. Sweet Dreams")
        print("2. Who I Am")
        print("3. Senorita")

    elif 'help' in i:
        print("Chatbot: Sure! You can ask me about topics like anime, manhuas, games and songs.")

    elif 'bye'in i:
        print("Chatbot: Goodbye! Have a Nice day")
        break

    else:
        print("Chatbot: I'm sorry, I didn't understand that. Try something again")