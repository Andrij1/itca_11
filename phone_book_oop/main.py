import app_setup
import choice


def main():

    phonebook, storages = app_setup.setup_app()
    choice.make_choice(phonebook, storages )


if __name__ == '__main__':
    main()
