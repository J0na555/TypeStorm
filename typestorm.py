import time
import random
import json
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.syntax import Syntax
from pyfiglet import Figlet

console = Console()
f = Figlet(font='slant')

code_snippets_by_level = {
    "beginner": [
        # Basic variable assignments and prints
        "print('Hello World')",
        "x = 10",
        "name = input('Enter your name: ')",
        "const isRaining = true;",
        "let counter = 0;",
        "System.out.println(\"Java\");",
        "# This is a comment",
        
        # Simple math operations
        "sum = 5 + 3",
        "product = 4 * 7",
        "result = 10 % 3",
        
        # Basic conditionals
        "if True:\n    print('Yes')",
        "if age >= 18:\n    print('Adult')",
    ],
    
    "intermediate": [
        # Loops and collections
        "for i in range(1, 6):\n    print(i*i)",
        "names = ['Alice', 'Bob']\nfor name in names:\n    print(name)",
        "let nums = [1,2,3];\nnums.forEach(n => console.log(n));",
        
        # Functions
        "def double(x):\n    return x * 2",
        "const multiply = (a, b) => a * b;",
        "function greet() {\n    return 'Hello';\n}",
        
        # Data structures
        "student = {'name': 'John', 'age': 20}",
        "numbers = {1, 2, 3}",
        "tuple_colors = ('red', 'green', 'blue')",
        
        # String manipulation
        "'hello'.upper()",
        "name = 'Alice'\nmsg = f\"Hi {name}\"",
        "const str = 'Hello';\nconsole.log(str.substring(1, 3));",
    ],
    
    "advanced": [
        # Classes and OOP
        "class Circle:\n    def __init__(self, radius):\n        self.radius = radius\n    def area(self):\n        return 3.14 * self.radius**2",
        "class Person {\n    constructor(name) {\n        this.name = name;\n    }\n    greet() {\n        console.log(`Hello ${this.name}`);\n    }\n}",
        
        # File I/O
        "with open('data.txt') as f:\n    content = f.read()",
        "import json\nwith open('data.json') as f:\n    data = json.load(f)",
        
        # Error handling
        "try:\n    x = 1/0\nexcept ZeroDivisionError:\n    print('Cannot divide by zero')",
        "try {\n    riskyOperation();\n} catch (e) {\n    console.error(e);\n}",
        
        # Decorators
        "def my_decorator(func):\n    def wrapper():\n        print('Before')\n        func()\n        print('After')\n    return wrapper",
    ],
    
    "expert": [
        # Generators and coroutines
        "def count_up_to(n):\n    i = 1\n    while i <= n:\n        yield i\n        i += 1",
        "async function fetchData() {\n    const response = await fetch('api/data');\n    return await response.json();\n}",
        
        # Metaprogramming
        "class Meta(type):\n    def __new__(cls, name, bases, dct):\n        dct['version'] = 1.0\n        return super().__new__(cls, name, bases, dct)",
        "const handler = {\n    get(target, prop) {\n        return `Property ${prop} doesn't exist`;\n    }\n};\nconst proxy = new Proxy({}, handler);",
        
        # Concurrency
        "import threading\ndef worker():\n    print('Thread working')\nthread = threading.Thread(target=worker)\nthread.start()",
        "const worker = new Worker('worker.js');\nworker.postMessage('start');",
        
        # Advanced algorithms
        "def quicksort(arr):\n    if len(arr) <= 1:\n        return arr\n    pivot = arr[len(arr)//2]\n    left = [x for x in arr if x < pivot]\n    middle = [x for x in arr if x == pivot]\n    right = [x for x in arr if x > pivot]\n    return quicksort(left) + middle + quicksort(right)",
        
        # Database operationsA
        "import sqlite3\nconn = sqlite3.connect('example.db')\nc = conn.cursor()\nc.execute('SELECT * FROM users')\nrows = c.fetchall()",
        "const { Pool } = require('pg');\nconst pool = new Pool();\nconst res = await pool.query('SELECT NOW()');",
    ],
    
    "master": [
        # Machine learning
        "from sklearn.ensemble import RandomForestClassifier\nclf = RandomForestClassifier()\nclf.fit(X_train, y_train)\npredictions = clf.predict(X_test)",
        
        # Web frameworks
        "@app.route('/user/<username>')\ndef show_user(username):\n    return f'User {username}'",
        "const express = require('express');\nconst app = express();\napp.get('/', (req, res) => res.send('Hello'));",
        
        # System programming
        "import os\npid = os.fork()\nif pid == 0:\n    print('Child process')\nelse:\n    print('Parent process')",
        
        # Cryptography
        "from cryptography.fernet import Fernet\nkey = Fernet.generate_key()\ncipher = Fernet(key)\ntoken = cipher.encrypt(b'secret')",
        
        # Game development
        "def update(self):\n    self.velocity += self.acceleration\n    self.position += self.velocity\n    if self.position.y > SCREEN_HEIGHT:\n        self.position.y = 0",
        
        # Compiler/parser
        "import ast\ntree = ast.parse('x = 1 + 2')\nfor node in ast.walk(tree):\n    print(type(node).__name__)",
        
        # Blockchain
        "class Block:\n    def __init__(self, index, timestamp, data, previous_hash):\n        self.index = index\n        self.timestamp = timestamp\n        self.data = data\n        self.previous_hash = previous_hash\n        self.hash = self.calculate_hash()",
    ]
}

def show_banner():
    console.print(f.renderText('TypeStorm'), style= 'bold cyan')

def get_random_code_snippet(level):
    if level  not in code_snippets_by_level:
        raise ValueError("Invalid Level!")
    return random.choice(code_snippets_by_level[level])

def choose_level():
    console.print("\n[bold]Choose Difficulty Level: [bold cyan]")
    console.print("1.Beginner")
    console.print("2.Intermediate")
    console.print("3.Advanced")
    console.print("4.Expert")
    console.print("5.Master")

    while True:
        choice = input("Enter 1,2,3,4,5: ").strip()
        if choice in ("1", "2", "3", "4", "5"):
            return {
                "1":("Beginner", "beginner"),
                "2":("Intermediate", "intermediate"),
                "3":("Advanced", "advanced"),
                "4":("Expert", "expert"),
                "5":("Master", "master")
            }[choice]
        console.print("Invalid Choice! Please Try Again", style="bold red")
        
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

def load_scores():
    try:
        with open('scores.json', 'r') as f:
            return json.load(f)
    except(FileNotFoundError, json.JSONDecodeError):
        return []

def save_scores(scores):
    try:
        with open('scores.json', 'w') as f:
            json.dump(scores, f, indent=4)
    except Exception as e:
        console.print(f"[bold red]Error saving scores: {e}[/bold red]")



def play_round(round_num, scores):
    display_name, key = choose_level()
    snippet = get_random_code_snippet(key)

    syntax_snippet = Syntax(snippet, "python", theme="moonkai", line_numbers=True)
    console.print(Panel(syntax_snippet, title=f"Type this code  ({display_name.capitalize()}) ", style='bold cyan'))

    console.print("\nStart typing and press Enter on empty line when done...", style= 'yellow')
    start_time= time.time()
    typed= multi_line_input()
    end_time= time.time()

    wpm, accuracy, time_taken = calculate_result(snippet, typed, start_time, end_time)

    console.print(f"\n[bold cyan]Results:[/bold cyan] wpm: {wpm}, Accuracy: {accuracy}% Time: {time_taken}s")
 
    scores.append({
        'round':round_num,
        'level':display_name,
        'wpm':wpm,
        'accuracy':accuracy,
        'time':time_taken
    })
    save_scores(scores)

    if scores:
        avg_wpm = sum(s['wpm'] for s in scores) / len(scores)
        console.print(f"Average WPM so far: {round(avg_wpm, 2)}")

if __name__ == "__main__":
    show_banner()
    scores = load_scores()
    round_num = max(s['round'] for s in scores)+1 if scores else 1

    while True:
        play_round(round_num, scores)
        round_num += 1
        again = input('\nPlay again? (y/n) ').lower()
        if again != "y":
            if scores:
                table = Table(title="Game Summary")
                table.add_column("Round")
                table.add_column("Level")
                table.add_column("WPM")
                table.add_column("Accuracy")
                table.add_column("Time(s)")
                for s in scores:
                    table.add_row(str(s['round']), 
                                  s['level'], 
                                  str(s['wpm']), 
                                  f"{s['accuracy']}%", 
                                  str(s['time']))
                console.print(table)

                high_wpm = max(scores, key=lambda x:x['wpm']) ['wpm'] if scores else 0
                console.print(f"Highest wpm: {high_wpm}")
            console.print("Thanks for playing TyperStorm!", style= "bold magenta")
            break

