from ai import chat_with_memory

def explain_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        code = f.read()

    messages = [
        {"role": "system", "content": "You are a senior software engineer."},
        {"role": "user", "content": f"Explain this code:\n\n{code}"}
    ]

    return chat_with_memory(messages)


def refactor_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        code = f.read()

    messages = [
        {"role": "system", "content": "You are a senior software engineer."},
        {"role": "user", "content": f"Refactor this code and only return the code do not add the ```python``` tags:\n\n{code}"}
    ]

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(chat_with_memory(messages))

    return chat_with_memory(messages)


def generate_function(description):
    messages = [
        {"role": "system", "content": "You are a senior software engineer."},
        {"role": "user", "content": f"Write a clean Python function for: {description}"}
    ]

    return chat_with_memory(messages)


def debug_error(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        code = f.read()

    messages = [
        {"role": "system", "content": "You are a senior software engineer."},
        {"role": "user", "content": f"Explain and fix this error and only return the code do not add the ```python``` tags:\n\n{code}"}
    ]

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(chat_with_memory(messages))

    return chat_with_memory(messages)