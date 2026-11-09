# === Stage 54: Add colorized output through optional ANSI codes ===
# Project: DonorTrack
def colorize(text, color=None):
    if not color:
        return text
    codes = {
        'bold': 1, 'red': 31, 'green': 32, 'yellow': 33,
        'blue': 34, 'magenta': 35, 'cyan': 36, 'gray': 90,
    }
    codes = {k: v for k, v in codes.items() if k in color.split(',')}
    if not codes:
        return text
    reset = '\033[0m'
    return ''.join('\033[%sm%s' % (codes[k], text) for k in codes) + reset

def print_header(title):
    print()
    print(colorize(title, 'bold,cyan'))
    print(colorize('-' * len(title), 'gray'))

def print_success(message):
    print(colorize('  OK: ' + message, 'green'))

def print_error(message):
    print(colorize('  ERROR: ' + message, 'red'))

def print_info(message):
    print(colorize(message, 'blue'))

USE_COLOR = True if os.environ.get('NO_COLOR') else sys.stdout.isatty()

def c(text, color=None):
    return colorize(text, color) if USE_COLOR else text
