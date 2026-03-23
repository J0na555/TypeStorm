# TypeStorm

TypeStorm is a terminal-based Python typing game where you practice typing code snippets of varying difficulty levels while tracking your typing speed (WPM), accuracy, and completion time.

## Features

- **5 Difficulty Levels**: Beginner → Master.
- **Random Multi-Language Snippets**: Practice Python, JavaScript, and Java snippets.
- **Performance Tracking**: Displays WPM, accuracy, and time taken for each round.
- **Immediate Feedback**: Shows the first mismatch to help improve accuracy.
- **Game Summary + Best by Level**: View all rounds plus best WPM/accuracy per level.
- **Syntax Highlighting**: Language-aware rendering using [Rich](https://pypi.org/project/rich/).
- **CLI Options**: Fixed level, fixed round count, and score reset flags.

---

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/J0na555/typestorm.git
   cd typestorm
   ```

2. **Install Dependencies**  
   Make sure you have Python 3.8+ installed.

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Game**

   ```bash
   python typestorm.py
   ```

## CLI Examples

```bash
# Play exactly 3 rounds
python typestorm.py --rounds 3

# Play only advanced snippets
python typestorm.py --level advanced

# Reset saved scores before starting
python typestorm.py --reset-scores
```
