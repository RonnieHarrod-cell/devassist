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
        {"role": "user", "content": f"Refactor this code:\n\n{code}"}
    ]

    return chat_with_memory(messages)


def generate_function(description):
    messages = [
        {"role": "system", "content": "You are a senior software engineer."},
        {"role": "user", "content": f"Write a clean Python function for: {description}"}
    ]

    return chat_with_memory(messages)


def debug_error(error_text):
    messages = [
        {"role": "system", "content": "You are a senior software engineer."},
        {"role": "user", "content": f"Explain and fix this error:\n\n{error_text}"}
    ]

    return chat_with_memory(messages)