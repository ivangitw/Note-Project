from presenter import login, registration
from note_presenter import note_menu

while True:
    choice = input("1 registration 2 login 3 exit:")
    if choice == "1":
        registration()
    if choice == "2":
        user = login()
        if user:
            note_menu(user)
    if choice == "3":
        break
