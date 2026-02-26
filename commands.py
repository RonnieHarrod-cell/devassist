from ai import ask_ai

def explain_file(filepath: str):
    with open(filepath, "r", encoding="utf-8") as f:
        code = f.read()

    prompt = f"Explain this code in detail:\n\n{code}"
    return ask_ai(prompt)


def refactor_file(filepath: str):
    with open(filepath, "r", encoding="utf-8") as f:
        code = f.read()

    prompt = f"Refactor this code to improve readability and structure:\n\n{code}"
    return ask_ai(prompt)


def generate_function(description: str):
    prompt = f"Write a clean Python function for this requirement:\n\n{description}"
    return ask_ai(prompt)


def debug_error(error_text: str):
    prompt = f"Explain this Python error and suggest fixes:\n\n{error_text}"
    return ask_ai(prompt)