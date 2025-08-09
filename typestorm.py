import time
import random
from rich.console import Console
from rich.panel import Panel
from pyfiglet import Figlet

console = Console()
f = Figlet(font='slant')

code_snippets = [
    "for i in range(5):\n    print(i)",
    "if x > 10:\n    return True\nelse:\n    return False",
    "public static void main(String[] args) {\n    System.out.println(\"Hello World\");\n}",
    "const add = (a, b) => a + b;",
    "def greet(name):\n    return f\"Hello, {name}!\"", 
]

def show_banner():
    console.print(f.renderText('TypeStorm'), style= 'bold cyan')

def get_random_code_snippet():
    return random.choice(code_snippets)

def calculate_result(snippet, typed, start_time, end_time):
    time_taken = end_time - start_time
    correct_chars = sum(1 for i,c in enumerate(typed) if i < len(snippet) and snippet[i] == c)
    accuracy = (correct_chars / len(snippet)) * 100
    wpm = (len(typed) / 5) / (time_taken/ 60) if time_taken > 0 else 0
    return round(wpm, 2), round (accuracy, 2), round(time_taken, 2)

def multi_line_input(prompt=""):
    console.print(prompt, style='yellow')
    lines = []
    while True:
        try:
            line=input()
        except EOFError:
            break
        if line == "":
            break
        lines.append(line)
    return "\n".join(lines)

def play_round():
    snippet = get_random_code_snippet()
    console.print(Panel(snippet, title="Type this code", style='bold cyan'))

    console.print("\nStart typing and press Enter on empty line when done...", style= 'yellow')
    start_time= time.time()
    typed= multi_line_input()
    end_time= time.time()

    wpm, accuracy, time_taken = calculate_result(snippet, typed, start_time, end_time)

    console.print(f"\n[bold cyan]Results:[/bold cyan] wpm: {wpm}, Accuracy: {accuracy}% Time: {time_taken}s")


if __name__ == "__main__":
    show_banner()

    while True:
        play_round()
        again = input('\nPlay again? (y/n) ').lower()
        if again != "y":
            console.print("Thanks for playing TyperStorm!", style= "bold magenta")
            break

