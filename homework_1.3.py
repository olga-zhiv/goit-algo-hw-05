def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter the argument for the command"
    return inner


def parse_input(user_input):
    # Розбиваємо рядок на команду і аргументи
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args



@input_error
def add_contact(args, contacts):
    # Додає новий контакт
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args, contacts):
    # Змінює телефон у наявного контакту
    name, phone = args
    contacts[name] = phone
    return "Contact updated."


@input_error
def show_phone(args, contacts):
    # Показує номер телефону за іменем
    name = args[0]
    return contacts[name]


@input_error
def show_all(contacts):
    # Показує всі збережені контакти
    if not contacts:
        return "No contacts saved."
    result = ""
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
    return result.strip()



def main():
    contacts = {}  # словник для зберігання контактів
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")

        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, contacts))

        elif command == "change":
            print(change_contact(args, contacts))

        elif command == "phone":
            print(show_phone(args, contacts))

        elif command == "all":
            print(show_all(contacts))

        else:
            print("Invalid command.")



if __name__ == "__main__":
    main()