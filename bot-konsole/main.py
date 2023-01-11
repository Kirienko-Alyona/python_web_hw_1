from user_funcs import handler, EXIT_COMMANDS, exit_func
from address_book import address_book
from termcolor import colored


def main():
    """
   The user enters through a space:
        - a command for the bot;
        - command, contact name, phone number or date of birth, email address, notes, tags,
    The function returns the bot's response and prints them.
    The bot terminates after the words "good bye", "exit", "close", "quit", "bye"
    """
    try:

        print(
            colored(f"\nHello, I am {address_book.bot_name} :)\n", "blue", attrs=["bold"]))

        help_str = colored("help", "blue")
        print(f"Type {help_str} to see all commands")

        while True:

            input_string = input("\nInput command, please: ")

            if input_string.lower() in EXIT_COMMANDS:
                exit_func()
            print(handler(input_string))

    finally:
        address_book.save_address_book()


if __name__ == "__main__":
    main()
