def get_note_number(notes):
    choice = input("Введіть номер статті:")
    if choice.isdigit() and 0 < int(choice) <= len(notes):
        return int(choice) - 1
    

def note_menu(author):
    while True:
        choice = input("""1) Створити статтю
2) Читати всі статті
3) Читати одну статтю
4) Змінити статтю
5) Видалити статтю
6) Вийти: """)

        if choice == "1":
            note = author.create_note()
            author.add_note(note)

        if choice == "2":
            author.read_notes()

        if choice == "3":
            author.read_notes()
            if author.notes:
                number = get_note_number(author.notes)
                if number is not None:
                    author.read_note(number)
            else:
                print("Статей немає")

        if choice == "4":
            author.read_notes()
            if author.notes:
                number = get_note_number(author.notes)
                if number is not None:
                    new_title = input("Новий заголовок: ")
                    new_text = input("Новий текст: ")
                    author.update_note(number, new_title, new_text)
            else:
                print("Статей немає")


        if choice == "5":
            author.read_notes()
            if author.notes:
                number = get_note_number(author.notes)
                if number is not None:
                    author.delete_note(number)
            else:
                print("Статей немає")


        if choice == "6":
            break