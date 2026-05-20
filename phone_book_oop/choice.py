import choice_handler


def make_choice(phonebook, storages):

    while True:
        choice = choice_handler.show_menu()

        if choice == '1':
            choice_handler.print_book(phonebook)

        elif choice == '2':
            choice_handler.search_contact(phonebook)

        elif choice == '3':
            choice_handler.edit_name(phonebook)

        elif choice == '4':
            choice_handler.edit_numbers(phonebook)

        elif choice == '5':
            choice_handler.edit_email(phonebook)

        elif choice == '6':
            choice_handler.edit_address(phonebook)

        elif choice == '7':
            choice_handler.delete_contact(phonebook)

        elif choice == '8':
            choice_handler.add_contact(phonebook)

        elif choice == '9':
            choice_handler.start_book(phonebook)

        elif choice.strip().upper() == 'QS':
            storages.write(phonebook.list_contacts())
            print('Phonebook updated')
            break

        elif choice == '0':
            choice_handler.quit_book(phonebook)
            break

        print('\n-> Make your choice ...')
        continue
