import argparse
from rich.console import Console
from commands import explain_file, refactor_file, generate_function, debug_error
from ai import chat_with_memory

console = Console()

def interactive_chat():
    console.print("[bold cyan]DevAssist Interactive Mode[/bold cyan]")
    console.print("Type'exit' to quit.\n")

    messages = [
        {"role": "system", "content": "You are a senior software engineer."}
    ]

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            break

        messages.append({"role": "user", "content": user_input})

        response = chat_with_memory(messages)

        messages.append({"role": "assistant", "content": response})

        console.print("[bold green]AI:[/bold green]", response)

def main():
    parser = argparse.ArgumentParser(
        description="DevAssist CLI - AI Developer Assistant"
    )

    parser.add_argument("--explain", type=str, help="Explain a file")
    parser.add_argument("--refactor", type=str, help="Refactor a file")
    parser.add_argument("--generate", type=str, help="Generate a function")
    parser.add_argument("--debug", type=str, help="Explain an error")
    parser.add_argument("--chat", action="store_true", help="Interactive chat mode.")

    args = parser.parse_args()

    if args.explain:
        result = explain_file(args.explain)
        console.print("[bold green]Explanation:[/bold green]")
        console.print(result)

    elif args.refactor:
        result = refactor_file(args.refactor)
        console.print("[bold blue]Refactored Code:[/bold blue]")
        console.print(result)

    elif args.generate:
        result = generate_function(args.generate)
        console.print("[bold yellow]Generated Function:[/bold yellow]")
        console.print(result)

    elif args.debug:
        result = debug_error(args.debug)
        console.print("[bold red]Debug Analysis:[/bold red]")
        console.print(result)

    elif args.chat:
        interactive_chat()

    else:
        parser.print_help()

if __name__ == "__main__":
    main()