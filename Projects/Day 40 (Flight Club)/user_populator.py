from SheetAPI import SheetAPI

sheet = SheetAPI()

print("Welcome to the Flight Club!\nPlease follow the instructions to register.\n")
first_name = input("What's your first name? ").capitalize().strip()
last_name = input("What's your last name? ").capitalize().strip()
email_1 = input("Type your email: ").strip()
email_2 = input("Retype your email: ").strip()

if email_1 == email_2:
    params = {
        "user": {
            "name": first_name,
            "surname": last_name,
            "email": email_1
        }
    }
    sheet.write_to_sheet(
        page="users",
        params=params
    )
    print("Welcome!")
else:
    print("Please, type the same email on both prompts.")