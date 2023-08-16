import sys,time,os

# Typewriter function is heavily derived from Learn Learn Scratch Tutorials YouTube Channel
# https://www.youtube.com/watch?v=2h8e0tXHfk0&t=135s

def typewriter(text):
    """
    Creates a retro typewriter effect for text being loaded on the screen.
    """
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()

        if char != "\n":
            time.sleep(0.04)
        else:
            time.sleep(1)

def load_game():
    typewriter("Ah, there you are. Greetings admiral, we were expecting you.\n")
    typewriter("The battle room is being prepared as we speak and our fleet is ready for deployment.\n")
    typewriter("Bring us victory...\n")

def main():
    """
    Run all program functions
    """
    load_game()

main()

