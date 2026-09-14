import time

def slow_print(text, delay=0.08):
    for char in text:
        print(char, end="", flush=True)
        # flush=True needed to prevent buffering which would ruin the effect
        time.sleep(delay)
    print()

def loading(dots=3, delay=0.4):
    for _ in range(dots):
        print(".", end="", flush=True)
        time.sleep(delay)
    print()

def red_text(text):
    return f"\033[1;91m{text}\033[0m"

def green_text(text):
    return f"\033[1;92m{text}\033[0m"

def yellow_text(text):
    return f"\033[1;93m{text}\033[0m"
