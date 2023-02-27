# Создать телефонный справочник с возможностью импорта и экспорта данных в формате txt.
# Name - Phone - Comment -- формат файла.
# Функционал:
# 1. Open a file
# 2. Save file
# 3. Show contacts
# 4. Add contact
# 5. Find contact
# 6. Change contact
# 7. Delete contact
# 8. Exit

import features


file_name = input("Enter a file name -> ")

flag = True
while flag:
    features.view_menu()
    feature_number = int(input("Enter feature number -> "))
    match feature_number:
        case 1:
            features.save_file()
        case 2:
            features.show_contacts(file_name)
        case 3:
            features.add_contact(file_name)
        case 4:
            features.find_contact(file_name)
        case 5:
            features.change_contact(file_name)
        case 6:
            features.delete_contact(file_name)
        case 7:
            flag = False
        case _:
            print("<<<Error404!>>>")