import sys
print(f"Python version: {sys.version}")
print("initialising CipherMaster...")
print("done")
print("loading ciphers...")

# ------------------------------------------------------------------------[ MODULES ]------------------------------------------------------------------------ #

import pyperclip
import os
import importlib.util

MODULES_DIR = "Modules"
ciphers = []

for filename in os.listdir(MODULES_DIR):
    if filename.endswith(".py") and not filename.startswith("__"):
        path = os.path.join(MODULES_DIR, filename)
        module_name = filename[:-3]

        spec = importlib.util.spec_from_file_location(module_name, path)
        module = importlib.util.module_from_spec(spec)
        try:
            spec.loader.exec_module(module)
 
            if all(hasattr(module, attr) for attr in ("name", "command", "info", "encrypt", "decrypt")):
                ciphers.append(module)
                print(f"Loaded {filename}")
            else:
                print(f"Skipping {filename}: missing required attributes.")
        except Exception as e:
            print(f"Error loading {filename}: {e}")
print("done")

# ------------------------------------------------------------------------[ VARIABLES ]------------------------------------------------------------------------ #

PROMPT = "\033[96m"      # Cyan
SUCCESS = "\033[92m"     # Green
ERROR = "\033[91m"       # Red
INFO = "\033[95m"        # Magenta
SEPARATOR = "\033[90m"   # Dark gray / dim white
RESET = "\033[0m" # Plain White

# ------------------------------------------------------------------------[ FUNCTIONS ]------------------------------------------------------------------------ #

def print_colored_results(results):
    colors = [SUCCESS, ERROR]
    for i in range(0, len(results), 5):
        row = results[i:i+5]
        line_parts = []
        for idx, item in enumerate(row):
            color = colors[idx % 2]
            line_parts.append(f"{color}{item}{RESET}")
        separator = f"{SEPARATOR}|{RESET}"
        print(separator.join(line_parts))

def cmds():
        print(f"{SEPARATOR}-" * 40)
        print(f"""
{INFO}Command Name {SEPARATOR}|{INFO} Command Use
{SEPARATOR}_____________{SEPARATOR}|____________________________________________________
{INFO}cmds         {SEPARATOR}|{INFO} Displays all Commands
{INFO}exit         {SEPARATOR}|{INFO} Exits the Application
{INFO}encrypt      {SEPARATOR}|{INFO} Encrypts a message with the chosen cipher
{INFO}decrypt      {SEPARATOR}|{INFO} Decrypts a message with any supported cipher
{RESET}""")

def greet():
    print(f"""{INFO}
Welcome to CipherMaster V2!
Use the "exit" Command to Quit the application and the "cmds" Command to view all Existing Commands
Your inputs are non Case-Sensitive{RESET}
""")

def encrypt():
    print(f"{PROMPT}Input text to encrypt:{RESET}")
    user_input = input(">>> ")

    print(f"\n{INFO}Available Ciphers:{RESET}")
    for mod in ciphers:
        print(f"{INFO}{mod.name:<15} {SEPARATOR}|{INFO} {mod.command:<6} {SEPARATOR}| {mod.info}{RESET}")

    print(f"\n{PROMPT}Enter the command of the cipher you'd like to use:{RESET}")
    selected_command = input(">>> ").lower()

    for mod in ciphers:
        if mod.command.lower() == selected_command:
            try:
                result = mod.encrypt(user_input)
                print(f"{SUCCESS}Encrypted text: {result}{RESET}")
                pyperclip.copy(result)
                print(f"{INFO}(Copied to clipboard){RESET}")
            except Exception as e:
                print(f"{ERROR}Encryption failed: {e}{RESET}")
            return

    print(f"{ERROR}Unknown cipher command '{selected_command}'.{RESET}")

def decrypt():
    print(f"{PROMPT}Input text to decrypt:{RESET}")
    user_input = input(">>> ")

    print(f"\n{INFO}Available Ciphers:{RESET}")
    for mod in ciphers:
        print(f"{INFO}{mod.name:<15} {SEPARATOR}|{INFO} {mod.command:<6} {SEPARATOR}| {mod.info}{RESET}")

    print(f"\n{PROMPT}Enter the command of the cipher you'd like to use:{RESET}")
    selected_command = input(">>> ").lower()

    for mod in ciphers:
        if mod.command.lower() == selected_command:
            try:
                result = mod.decrypt(user_input)
                print(f"{SUCCESS}Decrypted text: {result}{RESET}")
                pyperclip.copy(result)
                print(f"{INFO}(Copied to clipboard){RESET}")
            except Exception as e:
                print(f"{ERROR}Decryption failed: {e}{RESET}")
            return

    print(f"{ERROR}Unknown cipher command '{selected_command}'.{RESET}")


# ------------------------------------------------------------------------[ CODE ]------------------------------------------------------------------------ #

greet()
while True:
    command = input(">>> ").lower()
    if command == "exit":
        break
    elif command == "cmds":
        cmds()
    elif command == "encrypt":
        encrypt()
    elif command == "decrypt":
        decrypt()
    else:
        print(f'"{command}" {ERROR}is not a known command, use "cmds" to list all commands{RESET}')
input("Press Enter to exit...")

