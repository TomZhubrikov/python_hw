from features import PhoneBook

file_name = input("Enter a file name -> ")

pb = PhoneBook(file_name)

flag = True
while flag:
    pb.view_menu()
    feature_number = int(input("Enter feature number -> "))
    match feature_number:
        case 1:
            pb.save_file()
        case 2:
            pb.show_contacts()
        case 3:
            pb.add_contact()
        case 4:
            pb.find_contact()
        case 5:
            pb.change_contact()
        case 6:
            pb.delete_contact()
        case 7:
            flag = False
        case _:
            print("<<<Error404!>>>")
