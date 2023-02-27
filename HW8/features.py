def view_menu():
    print("1. Save file\n"
          "2. Show contacts\n"
          "3. Add contact\n"
          "4. Find contact\n"
          "5. Change contact\n"
          "6. Delete contact\n"
          "7. Exit")


def save_file():
    print("File is saved!")


def show_contacts(f_name):
    with open(f_name, 'r', encoding='utf-8') as data:
        for line in data:
            print(line)


def add_contact(f_name):
    with open(f_name, 'a', encoding='utf-8') as data:
        data.write(f'\n{input("Enter a new contact of the form (<Full name>, <phone number>, <comment>) -> ")}')
        print(">>> Contact is added!")


def find_contact(f_name):
    with open(f_name, 'r', encoding='utf-8') as data:
        search_line = input("Enter to find -> ")
        found_line = 0
        for line in data:
            if search_line in line:
                found_line = 1
                print(line)
        if found_line == 0:
            print("<<<String not found!>>>")


def change_contact(f_name):
    with open(f_name, 'r', encoding='utf-8') as data:
        lines = data.readlines()

    search_line = input("Enter to change -> ")
    found_line = 0
    with open(f_name, 'w', encoding='utf-8') as data:
        for line in lines:
            if search_line in line:
                found_line = 1
                print(f"String found -> {line}")
                data.write(f"{input('Replaced by -> ')}\n")
                print(">>> Contact is changed!")
            else:
                data.write(line)
        if found_line == 0:
            print("<<<String not found!>>>")


def delete_contact(f_name):
    with open(f_name, 'r', encoding='utf-8') as data:
        lines = data.readlines()

    search_line = input("Enter to delete -> ")
    found_line = 0
    with open(f_name, 'w', encoding='utf-8') as data:
        for line in lines:
            if search_line in line:
                found_line = 1
                print(f"String -> {line} - is deleted")
            else:
                data.write(line)
        if found_line == 0:
            print("<<<String not found!>>>")