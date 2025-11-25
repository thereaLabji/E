# File was auto-generated. DO NOT EDIT
# Copyright (C) 2012-2025 thereaLabji, Karu Kartulid Oy Inc.
# License: Apache-2.0

# main.py
# An custom Command Prompt with customizeable commands and features. (For new users to Coding)

import sys
import os
from typing import Dict, Callable, List

class CustomCommandPrompt:
    """A beginner-friendly command prompt system with customizable commands."""
    
    def __init__(self, prompt_text: str = ">>> "):
        self.prompt_text = prompt_text
        self.commands: Dict[str, Callable] = {}
        self.running = False
        self._register_default_commands()
    
    def _register_default_commands(self):
       """Register built-in commands for new users."""
       self.register_command("help", self.cmd_help, "Show all available commands")
       self.register_command("exit", self.cmd_exit, "Exit the command prompt")
       self.register_command("clear", self.cmd_clear, "Clear the screen")
       self.register_command("echo", self.cmd_echo, "Print text: echo <text>")
   
    def register_command(self, name: str, func: Callable, description: str = ""):
       """Register a new command."""
       self.commands[name.lower()] = {"func": func, "desc": description}
   
    def cmd_help(self, args: List[str] = None):
       """Display help information."""
       print("\n" + "="*50)
       print("AVAILABLE COMMANDS")
       print("="*50)
       for cmd_name, cmd_info in sorted(self.commands.items()):
            desc = cmd_info["desc"]
            print(f"  {cmd_name:<15} - {desc}")
            print("="*50 + "\n")
    
    def cmd_exit(self, args: List[str] = None):
        """Exit the command prompt."""
        print("Goodbye!")
        self.running = False
    
    def cmd_clear(self, args: List[str] = None):
        """Clear the terminal screen."""
        os.system("clear" if os.name == "posix" else "cls")
    
    def cmd_echo(self, args: List[str] = None):
        """Echo text to the console."""
        if args:
            print(" ".join(args))
        else:
            print("")
    
    def parse_input(self, user_input: str) -> tuple:
        """Parse user input into command and arguments."""
        parts = user_input.strip().split(maxsplit=1)
        if not parts:
            return None, []
        
        command = parts[0].lower()
        args = parts[1].split() if len(parts) > 1 else []
        return command, args
    
    def execute_command(self, command: str, args: List[str]):
        """Execute a registered command."""
        if command not in self.commands:
            print(f"Command '{command}' not found. Type 'help' for available commands.")
            return
        
        try:
            self.commands[command]["func"](args)
        except Exception as e:
            print(f"Error executing command: {e}")
    
    def run(self):
        """Start the interactive command prompt."""
        print("\n" + "="*50)
        print("Welcome to Custom Command Prompt!")
        print("Type 'help' for available commands.")
        print("="*50 + "\n")
        
        self.running = True
        while self.running:
            try:
                user_input = input(self.prompt_text)
                if user_input.strip():
                    command, args = self.parse_input(user_input)
                    if command:
                        self.execute_command(command, args)
            except KeyboardInterrupt:
                print("\n\nUse 'exit' command to quit.")
            except EOFError:
                self.running = False


def main():
    """Main entry point."""
    prompt = CustomCommandPrompt()
    prompt.run()


if __name__ == "__main__":
    main()


