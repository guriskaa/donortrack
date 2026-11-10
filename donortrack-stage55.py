# === Stage 55: Add a setting to disable colorized output ===
# Project: DonorTrack
USE_COLOR = os.environ.get("DONORTRACK_COLOR", "auto").lower() != "0"

def colorize(text, color):
    if not USE_COLOR:
        return text
    codes = {
        "red": "\033[91m", "green": "\033[92m", "yellow": "\033[93m",
        "blue": "\033[94m", "magenta": "\033[95m", "cyan": "\033[96m",
        "gray": "\033[90m", "reset": "\033[0m",
    }
    return codes.get(color, "") + text + codes["reset"]

def print_field(label, value):
    print(colorize(label, "cyan") + ": " + str(value))

def print_header(title):
    print(colorize(title, "magenta"))
    print(colorize("=" * len(title), "magenta"))

def print_success(message):
    print(colorize(message, "green"))

def print_warning(message):
    print(colorize(message, "yellow"))

def print_error(message):
    print(colorize(message, "red"))

def prompt_choice(message, options):
    print(colorize(message, "cyan"))
    for i, opt in enumerate(options, 1):
        print("  " + str(i) + ". " + opt)
    while True:
        choice = input("Select > ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return options[int(choice) - 1]
        print(colorize("Invalid choice, try again.", "yellow"))
