def main():
    print("Avap Bot: Hi! I'm Avap Bot. Type 'help' to see what I can do.")

    while True:
        message = input("You: ").strip().lower()

        if message in ("bye", "exit", "quit"):
            print("Avap Bot: Bye!")
            break
        elif message in ("hi", "hello", "hey"):
            print("Avap Bot: Hi Nice to meet you..")
        elif message == "how are you":
            print("Avap Bot: I'm doing well, thanks for asking.")
        elif message == "help":
            print("Avap Bot: Available commands are: 'hi', 'hello', 'hey', 'how are you', 'help', 'info', 'creator', 'stardance', 'laptop', 'creator-info', 'shut up', 'bye', 'exit', and 'quit'.")
        elif message == "info":
            print("Avap Bot : i am Avap bot, I am created by Aadi Vinayak A Pillai For the stardance hackclub programme, I am a simple script bot that is pre programmed to respond to different messages :)")
        elif message == "creator":
            print("Avap Bot: I was created by Aadi Vinayak A Pillai (AVAP). HE is a 10th grader struggling for bord exams and interested in computers and linux. I am one such of his project for the stardance programme. Also He is from Kerala,India and yo may have understood from the term board exam:D")
        elif message == "stardance":
            print("Avap Bot: Stardance is a hackclub programme for students to learn and explore computers.")
        elif message == "laptop":
            print("Avap Bot: My creator Aadi Vinayak A Pillai (AVAP) uses a 3 year old HP 245g8 laptop with 8gb ram and 128gb ssd and he uses Manjaro Linux as his main os")
        elif message == "creator-info":
            print("Avap Bot: I wont tell you about hi personal info ! I am Not a snitch :P")
        elif message == "shut up":
            print("Oh My God! How rude! Bot has feelings too :(")

        else:
            print("Avap Bot: I don't understand. Type 'help' :(")
        


if __name__ == "__main__":
    main()