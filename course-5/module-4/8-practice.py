from typing import List

# Implement the functions below.
# Do not change their names or parameter lists.


def is_pep8_compliant(line: str) -> bool:
    """Return True if the line satisfies basic PEP 8 style rules.

    Rules to enforce:
        - Maximum length of 79 characters.
        - No tab characters ("\t").
        - No trailing whitespace (spaces at the end of the line).
    """
    # TODO: Implement this function
    return len(line) <= 79 and "\t" not in line and not line.rstrip() != line


def summarize_docstring(docstring: str) -> str:
    """Return the first non-empty line of the docstring.

    The input is a raw multi-line string. You should:
        - Split the string into lines.
        - Strip leading and trailing whitespace from each line.
        - Return the first line that is not empty after stripping.
        - If no such line exists, return an empty string.
    """
    # TODO: Implement this function
    for line in docstring.splitlines():
        stripped_line = line.strip()
        if stripped_line:
            return stripped_line
    return ""

from typing import Dict

# Implement the function below.
# Do not change its name or parameter list.


def format_api_doc(name: str, description: str, params: Dict[str, str]) -> str:
    """Return a Sphinx-friendly API documentation string.

    The format must be:
        - First line: "<name>: <description>" (short summary), stripped.
        - Subsequent lines: one or more ":param <param_name>: <description>" lines.
        - Any parameter description that would exceed 79 characters on a single line
          must be wrapped at word boundaries into multiple lines, each beginning
          with the same ":param <param_name>: " prefix.
        - The final returned string must end with a newline character ("\n").
    """
    # TODO: Implement this function
    lines = [f"{name}: {description}"]
    for param_name, param_desc in params.items():
        prefix = f":param {param_name}: "
        words = param_desc.split()
        current_line = prefix
        for word in words:
            if len(current_line) + len(word) + 1 > 79:
                lines.append(current_line.rstrip())
                current_line = prefix + word + " "
            else:
                current_line += word + " "
        lines.append(current_line.rstrip())
    return "\n".join(lines) + "\n"

def filter_active_users_with_email(users):
    """Return a new list of cleaned, active users that have an email.

    Each returned dict must have at least 'name' and 'email' keys.
    Do not mutate the input list.
    """
    # TODO: implement this function
    return [
        {"name": user["name"], "email": user["email"]}
        for user in users
        if user.get("active") and user.get("email")
    ]


def format_active_users(users):
    """Return a summary string of active users with email.

    Use filter_active_users_with_email to select and clean users, then
    format each as "name <email>" and join with ", ". If no users
    qualify, return the empty string.
    """
    # TODO: implement this function
    active_users = filter_active_users_with_email(users)
    return ", ".join(f"{user['name']} <{user['email']}>" for user in active_users) if active_users else ""


# Add comments to the code below
# 1. "Ensure Question class still exists after documenting"
# 2. "Ensure __init__ method still exists
class Question:
    def __init__(self, text, options, answer):
        self.text = text
        self.options = options
        self.answer = answer
# This class represents a multiple-choice question with a text, a list of options, and the correct answer.
# Example usage:
# question = Question("What is 2+2?", ["3", "4", "5"], "4")



# I have a Python codebase for a quiz program. Provide a high-level overview of the program's functionality. 
# Specifically, I'd like to know: What is the purpose of each method? What are the main classes and functions? What are the key data structures used? 
# How does the code execute at a high level? Summarize your findings in a concise paragraph of approximately 150 words.

# This program defines a quiz game with multiple-choice questions. 
# The main classes are Question, which represents a single question, and TriviaGameDriver, which manages the game flow. 
# The TriviaGameDriver class loads questions from a CSV file, initializes a TriviaGame instance, and handles the game loop. 
# The key data structures include lists for storing questions and options, and dictionaries for user data in other parts of the code. 
# The program executes by first loading questions, then repeatedly playing rounds of the game until the user chooses to stop, 
# finally displaying the user's score.

class TriviaGameDriver:

    def __init__(self, filename):
        self.questions = self.load_questions_from_file(filename)
        self.game = TriviaGame(self.questions)

    def load_questions_from_file(self, filename):
        x = []
        with open(filename, 'r') as y:
            z = csv.reader(y)
            next(z)
            for a in z:
                b = a[0]
                c = a[1].split('|')
                d = a[2]
                x.append(Question(b, c, d))
        return x

    def start_game(self):
        while True:
            self.game.play_round()
            play_again = input("Play another round? (y/n): ")
            if play_again.lower() != 'y':
                break
        print(f"\nFinal score: {self.game.score}")


# In the attached code, refactor the variable names to make them more descriptive. In addition, please add PEP8-compliant comments and docstrings. Provide a list of changes after updating the code.

class TriviaGameDriver:

    def __init__(self, filename):
        """Initialize the TriviaGameDriver with questions loaded from a CSV file."""
        self.questions = self.load_questions_from_file(filename)
        self.game = TriviaGame(self.questions)

    def load_questions_from_file(self, filename):
        """Load questions from a CSV file and return a list of Question objects."""
        questions = []
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                question_text = row[0]
                options = row[1].split('|')
                answer = row[2]
                questions.append(Question(question_text, options, answer))
        return questions

    def start_game(self):
        """Start the trivia game and handle the game loop."""
        while True:
            self.game.play_round()
            play_again = input("Play another round? (y/n): ")
            if play_again.lower() != 'y':
                break
        print(f"\nFinal score: {self.game.score}") 