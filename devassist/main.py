import argparse
from rich.console import Console
from commands import explain_file, refactor_file, generate_function, debug_error
from ai import chat_with_memory

class DevAssist:
    def __init__(self):
        self.console = Console()
        self.messages = [
            {"role": "system", "content": "You are a senior software engineer."}
        ]

        # Central command registry
        self.commands = {
            "explain": explain_file,
            "refactor": refactor_file,
            "generate": generate_function,
            "debug": debug_error,
        }

    # ---------------------------
    # Command Handler
    # ---------------------------
    def handle_command(self, user_input):
        parts = user_input.split(maxsplit=1)

        if not parts:
            return None

        cmd = parts[0]
        arg = parts[1] if len(parts) > 1 else None

        if cmd in self.commands:
            if not arg:
                return f"'{cmd}' requires an argument."

            return self.commands[cmd](arg)

        return None  # Not a command

    # ---------------------------
    # Interactive Chat
    # ---------------------------
    def interactive_chat(self):
        self.console.print("[bold cyan]DevAssist Interactive Mode[/bold cyan]")
        self.console.print("Type 'exit' to quit.\n")

        while True:
            user_input = input("You: ")

            if user_input.lower() == "exit":
                self.console.print("[bold magenta]Goodbye![/bold magenta]")
                break

            if user_input.lower() == "commands":
                self.show_commands()
                continue

            # 🔥 Check if it's a command first
            command_result = self.handle_command(user_input)

            if command_result:
                self.console.print("[bold yellow]Command Output:[/bold yellow]")
                self.console.print(command_result)
                continue

            # Otherwise → AI chat
            self.messages.append({"role": "user", "content": user_input})
            response = chat_with_memory(self.messages)
            self.messages.append({"role": "assistant", "content": response})

            self.console.print("[bold green]AI:[/bold green]", response)

    # ---------------------------
    # CLI Mode
    # ---------------------------
    def run_cli(self):
        parser = argparse.ArgumentParser(
            description="DevAssist CLI - AI Developer Assistant"
        )

        parser.add_argument("--explain", type=str)
        parser.add_argument("--refactor", type=str)
        parser.add_argument("--generate", type=str)
        parser.add_argument("--debug", type=str)
        parser.add_argument("--chat", action="store_true")

        args = parser.parse_args()

        # Map CLI args → command names
        cli_map = {
            "explain": args.explain,
            "refactor": args.refactor,
            "generate": args.generate,
            "debug": args.debug,
        }

        for cmd, value in cli_map.items():
            if value:
                result = self.commands[cmd](value)
                self.console.print(f"[bold green]{cmd.capitalize()} Result:[/bold green]")
                self.console.print(result)
                return

        if args.chat:
            self.interactive_chat()
        else:
            parser.print_help()

    # ---------------------------
    # Utility
    # ---------------------------
    def show_commands(self):
        self.console.print("[bold yellow]Available Commands:[/bold yellow]")
        for cmd in self.commands:
            self.console.print(f"- {cmd} [argument]")


# Entry point
if __name__ == "__main__":
    app = DevAssist()
    app.run_cli()