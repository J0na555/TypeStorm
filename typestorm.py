import argparse
import json
import random
import time
from pathlib import Path

from pyfiglet import Figlet
from rich.console import Console
from rich.panel import Panel
from rich.syntax import Syntax
from rich.table import Table

console = Console()
f = Figlet(font="slant")
SCORE_FILE = Path(__file__).with_name("scores.json")

LEVEL_CHOICES = {
    "1": ("Beginner", "beginner"),
    "2": ("Intermediate", "intermediate"),
    "3": ("Advanced", "advanced"),
    "4": ("Expert", "expert"),
    "5": ("Master", "master"),
}

code_snippets_by_level = {
    "beginner": [
        {"language": "python", "text": "print('Hello World')"},
        {"language": "python", "text": "x = 10"},
        {"language": "python", "text": "name = input('Enter your name: ')"},
        {"language": "javascript", "text": "const isRaining = true;"},
        {"language": "javascript", "text": "let counter = 0;"},
        {"language": "java", "text": "System.out.println(\"Java\");"},
        {"language": "python", "text": "# This is a comment"},
        {"language": "python", "text": "sum = 5 + 3"},
        {"language": "python", "text": "product = 4 * 7"},
        {"language": "python", "text": "result = 10 % 3"},
        {"language": "python", "text": "if True:\n    print('Yes')"},
        {"language": "python", "text": "if age >= 18:\n    print('Adult')"},
    ],
    "intermediate": [
        {"language": "python", "text": "for i in range(1, 6):\n    print(i*i)"},
        {
            "language": "python",
            "text": "names = ['Alice', 'Bob']\nfor name in names:\n    print(name)",
        },
        {
            "language": "javascript",
            "text": "let nums = [1,2,3];\nnums.forEach(n => console.log(n));",
        },
        {"language": "python", "text": "def double(x):\n    return x * 2"},
        {"language": "javascript", "text": "const multiply = (a, b) => a * b;"},
        {"language": "javascript", "text": "function greet() {\n    return 'Hello';\n}"},
        {"language": "python", "text": "student = {'name': 'John', 'age': 20}"},
        {"language": "python", "text": "numbers = {1, 2, 3}"},
        {"language": "python", "text": "tuple_colors = ('red', 'green', 'blue')"},
        {"language": "python", "text": "'hello'.upper()"},
        {"language": "python", "text": "name = 'Alice'\nmsg = f\"Hi {name}\""},
        {
            "language": "javascript",
            "text": "const str = 'Hello';\nconsole.log(str.substring(1, 3));",
        },
    ],
    "advanced": [
        {
            "language": "python",
            "text": (
                "class Circle:\n"
                "    def __init__(self, radius):\n"
                "        self.radius = radius\n"
                "    def area(self):\n"
                "        return 3.14 * self.radius**2"
            ),
        },
        {
            "language": "javascript",
            "text": (
                "class Person {\n"
                "    constructor(name) {\n"
                "        this.name = name;\n"
                "    }\n"
                "    greet() {\n"
                "        console.log(`Hello ${this.name}`);\n"
                "    }\n"
                "}"
            ),
        },
        {"language": "python", "text": "with open('data.txt') as f:\n    content = f.read()"},
        {
            "language": "python",
            "text": "import json\nwith open('data.json') as f:\n    data = json.load(f)",
        },
        {
            "language": "python",
            "text": "try:\n    x = 1/0\nexcept ZeroDivisionError:\n    print('Cannot divide by zero')",
        },
        {
            "language": "javascript",
            "text": "try {\n    riskyOperation();\n} catch (e) {\n    console.error(e);\n}",
        },
        {
            "language": "python",
            "text": (
                "def my_decorator(func):\n"
                "    def wrapper():\n"
                "        print('Before')\n"
                "        func()\n"
                "        print('After')\n"
                "    return wrapper"
            ),
        },
    ],
    "expert": [
        {
            "language": "python",
            "text": "def count_up_to(n):\n    i = 1\n    while i <= n:\n        yield i\n        i += 1",
        },
        {
            "language": "javascript",
            "text": (
                "async function fetchData() {\n"
                "    const response = await fetch('api/data');\n"
                "    return await response.json();\n"
                "}"
            ),
        },
        {
            "language": "python",
            "text": (
                "class Meta(type):\n"
                "    def __new__(cls, name, bases, dct):\n"
                "        dct['version'] = 1.0\n"
                "        return super().__new__(cls, name, bases, dct)"
            ),
        },
        {
            "language": "javascript",
            "text": (
                "const handler = {\n"
                "    get(target, prop) {\n"
                "        return `Property ${prop} doesn't exist`;\n"
                "    }\n"
                "};\n"
                "const proxy = new Proxy({}, handler);"
            ),
        },
        {
            "language": "python",
            "text": (
                "import threading\n"
                "def worker():\n"
                "    print('Thread working')\n"
                "thread = threading.Thread(target=worker)\n"
                "thread.start()"
            ),
        },
        {"language": "javascript", "text": "const worker = new Worker('worker.js');\nworker.postMessage('start');"},
        {
            "language": "python",
            "text": (
                "def quicksort(arr):\n"
                "    if len(arr) <= 1:\n"
                "        return arr\n"
                "    pivot = arr[len(arr)//2]\n"
                "    left = [x for x in arr if x < pivot]\n"
                "    middle = [x for x in arr if x == pivot]\n"
                "    right = [x for x in arr if x > pivot]\n"
                "    return quicksort(left) + middle + quicksort(right)"
            ),
        },
        {
            "language": "python",
            "text": (
                "import sqlite3\n"
                "conn = sqlite3.connect('example.db')\n"
                "c = conn.cursor()\n"
                "c.execute('SELECT * FROM users')\n"
                "rows = c.fetchall()"
            ),
        },
        {
            "language": "javascript",
            "text": "const { Pool } = require('pg');\nconst pool = new Pool();\nconst res = await pool.query('SELECT NOW()');",
        },
    ],
    "master": [
        {
            "language": "python",
            "text": (
                "from sklearn.ensemble import RandomForestClassifier\n"
                "clf = RandomForestClassifier()\n"
                "clf.fit(X_train, y_train)\n"
                "predictions = clf.predict(X_test)"
            ),
        },
        {
            "language": "python",
            "text": "@app.route('/user/<username>')\ndef show_user(username):\n    return f'User {username}'",
        },
        {
            "language": "javascript",
            "text": "const express = require('express');\nconst app = express();\napp.get('/', (req, res) => res.send('Hello'));",
        },
        {
            "language": "python",
            "text": (
                "import os\n"
                "pid = os.fork()\n"
                "if pid == 0:\n"
                "    print('Child process')\n"
                "else:\n"
                "    print('Parent process')"
            ),
        },
        {
            "language": "python",
            "text": (
                "from cryptography.fernet import Fernet\n"
                "key = Fernet.generate_key()\n"
                "cipher = Fernet(key)\n"
                "token = cipher.encrypt(b'secret')"
            ),
        },
        {
            "language": "python",
            "text": (
                "def update(self):\n"
                "    self.velocity += self.acceleration\n"
                "    self.position += self.velocity\n"
                "    if self.position.y > SCREEN_HEIGHT:\n"
                "        self.position.y = 0"
            ),
        },
        {
            "language": "python",
            "text": "import ast\ntree = ast.parse('x = 1 + 2')\nfor node in ast.walk(tree):\n    print(type(node).__name__)",
        },
        {
            "language": "python",
            "text": (
                "class Block:\n"
                "    def __init__(self, index, timestamp, data, previous_hash):\n"
                "        self.index = index\n"
                "        self.timestamp = timestamp\n"
                "        self.data = data\n"
                "        self.previous_hash = previous_hash\n"
                "        self.hash = self.calculate_hash()"
            ),
        },
    ],
}


def show_banner():
    console.print(f.renderText("TypeStorm"), style="bold cyan")


def get_random_code_snippet(level):
    if level not in code_snippets_by_level:
        raise ValueError("Invalid level!")
    return random.choice(code_snippets_by_level[level])


def choose_level(forced_level_key=None):
    if forced_level_key:
        for _, value in LEVEL_CHOICES.items():
            if value[1] == forced_level_key:
                return value
        raise ValueError("Invalid forced level.")

    console.print("\n[bold]Choose Difficulty Level: [bold cyan]")
    console.print("1. Beginner")
    console.print("2. Intermediate")
    console.print("3. Advanced")
    console.print("4. Expert")
    console.print("5. Master")

    while True:
        choice = input("Enter 1,2,3,4,5: ").strip()
        if choice in LEVEL_CHOICES:
            return LEVEL_CHOICES[choice]
        console.print("Invalid choice! Please try again.", style="bold red")


def calculate_result(snippet, typed, start_time, end_time):
    time_taken = end_time - start_time
    matched = sum(1 for idx, char in enumerate(typed) if idx < len(snippet) and snippet[idx] == char)
    total_chars = max(len(snippet), len(typed), 1)
    accuracy = (matched / total_chars) * 100
    wpm = (len(typed) / 5) / (time_taken / 60) if time_taken > 0 else 0
    return round(wpm, 2), round(accuracy, 2), round(time_taken, 2)


def multi_line_input(prompt=""):
    console.print(prompt, style="yellow")
    lines = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        if line == "":
            break
        lines.append(line)
    return "\n".join(lines)


def load_scores(path=SCORE_FILE):
    try:
        with path.open("r", encoding="utf-8") as file:
            data = json.load(file)
            return data if isinstance(data, list) else []
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_scores(scores, path=SCORE_FILE):
    try:
        with path.open("w", encoding="utf-8") as file:
            json.dump(scores, file, indent=4)
    except OSError as error:
        console.print(f"[bold red]Error saving scores: {error}[/bold red]")


def mismatch_feedback(snippet, typed):
    for idx, expected in enumerate(snippet):
        if idx >= len(typed):
            return f"Mismatch at index {idx}: missing {expected!r}."
        actual = typed[idx]
        if actual != expected:
            return f"Mismatch at index {idx}: expected {expected!r}, got {actual!r}."
    if len(typed) > len(snippet):
        extra = typed[len(snippet)]
        return f"Extra input at index {len(snippet)}: got {extra!r}."
    return "Perfect match."


def print_best_scores(scores):
    if not scores:
        return
    grouped = {}
    for score in scores:
        grouped.setdefault(score["level"], []).append(score)

    table = Table(title="Best Scores by Level")
    table.add_column("Level")
    table.add_column("Best WPM")
    table.add_column("Best Accuracy")

    for level in sorted(grouped):
        level_scores = grouped[level]
        best_wpm = max(level_scores, key=lambda item: item["wpm"])["wpm"]
        best_accuracy = max(level_scores, key=lambda item: item["accuracy"])["accuracy"]
        table.add_row(level, str(best_wpm), f"{best_accuracy}%")
    console.print(table)


def play_round(round_num, scores, forced_level_key=None):
    display_name, key = choose_level(forced_level_key)
    snippet_data = get_random_code_snippet(key)
    snippet = snippet_data["text"]
    language = snippet_data["language"]

    syntax_snippet = Syntax(snippet, language, theme="monokai", line_numbers=True)
    console.print(Panel(syntax_snippet, title=f"Type this code ({display_name})", style="bold cyan"))

    console.print("\nStart typing and press Enter on empty line when done...", style="yellow")
    start_time = time.time()
    typed = multi_line_input()
    end_time = time.time()

    wpm, accuracy, time_taken = calculate_result(snippet, typed, start_time, end_time)
    console.print(f"\n[bold cyan]Results:[/bold cyan] WPM: {wpm}, Accuracy: {accuracy}% Time: {time_taken}s")
    console.print(f"[bold yellow]Feedback:[/bold yellow] {mismatch_feedback(snippet, typed)}")

    scores.append(
        {
            "round": round_num,
            "level": display_name,
            "wpm": wpm,
            "accuracy": accuracy,
            "time": time_taken,
        }
    )
    save_scores(scores)

    avg_wpm = sum(score["wpm"] for score in scores) / len(scores)
    console.print(f"Average WPM so far: {round(avg_wpm, 2)}")


def print_summary(scores):
    if not scores:
        console.print("No scores recorded yet.")
        return

    table = Table(title="Game Summary")
    table.add_column("Round")
    table.add_column("Level")
    table.add_column("WPM")
    table.add_column("Accuracy")
    table.add_column("Time(s)")
    for score in scores:
        table.add_row(
            str(score["round"]),
            score["level"],
            str(score["wpm"]),
            f"{score['accuracy']}%",
            str(score["time"]),
        )
    console.print(table)

    high_wpm = max(scores, key=lambda item: item["wpm"])["wpm"]
    console.print(f"Highest WPM: {high_wpm}")
    print_best_scores(scores)


def parse_args():
    parser = argparse.ArgumentParser(description="Play TypeStorm in your terminal.")
    parser.add_argument(
        "--level",
        choices=[value[1] for value in LEVEL_CHOICES.values()],
        help="Play with a fixed level each round.",
    )
    parser.add_argument(
        "--rounds",
        type=int,
        default=None,
        help="Number of rounds to play before exiting automatically.",
    )
    parser.add_argument(
        "--reset-scores",
        action="store_true",
        help="Clear existing scores before starting.",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    if args.rounds is not None and args.rounds < 1:
        raise ValueError("--rounds must be at least 1.")

    if args.reset_scores and SCORE_FILE.exists():
        SCORE_FILE.unlink()

    show_banner()
    scores = load_scores()
    round_num = max(score["round"] for score in scores) + 1 if scores else 1

    played = 0
    while True:
        play_round(round_num, scores, forced_level_key=args.level)
        round_num += 1
        played += 1

        if args.rounds is not None:
            if played >= args.rounds:
                break
            continue

        again = input("\nPlay again? (y/n) ").strip().lower()
        if again != "y":
            break

    print_summary(scores)
    console.print("Thanks for playing TypeStorm!", style="bold magenta")


if __name__ == "__main__":
    main()

