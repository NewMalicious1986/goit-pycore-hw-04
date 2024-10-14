from colorama import Fore, Style

COMMANDS = """
    Available commands:
    - hello: Greet the assistant.
    - add <name> <phone>: Add a new contact.
    - change <name> <phone>: Change the phone number of a contact.
    - phone <name>: Get the phone number of a contact.
    - all: List all contacts.
    - help: List available commands.
    - close/exit: Close the assistant.
    """


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    return f"Contact {name} not found."



def get_phone(args, contacts):
    name, *args = args
    phone = contacts.get(name)
    if phone:
        return phone
    return f"Contact {name} not found."


def get_all_contacts(contacts):
    if len(contacts) == 0:
        return "No contacts found."
    for k, v in contacts.items():
        print(f"{k}: {v}")


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        try:
            user_input = input(f"{Style.RESET_ALL}Enter a command: ")
            command, *args = parse_input(user_input)
            match command:
                case "close" | "exit":
                    print("Good bye!")
                    break
                case "hello":
                    print("How can I help you?")
                case "add":
                    print(add_contact(args, contacts))
                case "change":
                    print(change_contact(args, contacts))
                case "phone":
                    print(get_phone(args, contacts))
                case "all":
                    get_all_contacts(contacts)
                case "help":
                    print(COMMANDS)
                case _:
                    print(f"{Fore.RED}Invalid command.\n{Style.RESET_ALL}To see all commands available type 'help'")
        except Exception as e:
            print(f"\n{Fore.RED}Oops, Something went wrong!.\n{Fore.GREEN}See list of available commands below:")
            print(f"{Style.RESET_ALL}" + COMMANDS)


if __name__ == "__main__":
    main()
