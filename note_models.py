from model import User

class Author(User):
    def __init__(self, login, password):
        super().__init__(login, password)
        self.notes = []

    def create_note(self):
        note = Note(input("Заголовок: "), input("Текст: "))
        return note

    def read_notes(self):
        for index, note in enumerate(self.notes, 1):
            print(f"{index}. {note.title}")

    def read_note(self, number):
        note = self.notes[number - 1]
        note.show()

    def update_note(self, number, new_title, new_text):
        note = self.notes[number - 1]
        note.update(new_title, new_text)

    def delete_note(self, number):
        self.notes.pop(number - 1)
        print("Статтю видалено")

    def add_note(self, note):
        self.notes.append(note)


class Note:
    def __init__(self, title, text):
        self.title = title
        self.text = text

    def show(self):
        print(f"{self.title}\n{self.text}")

    def update(self, title, text):
        self.title = title
        self.text = text


def get_note_number(notes):
    choice = input("Введіть номер статті: ")
    if choice.isdigit() and 0 < int(choice) <= len(notes):
        return int(choice) - 1

authors = []
