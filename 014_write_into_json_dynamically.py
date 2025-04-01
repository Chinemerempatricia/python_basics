import json
user = {
    "id": input("Enter ID:"),
    "first_name": input("Enter First Name:"),
    "last_name": input("Enter Last Name:"),
    "email": input("Enter Email:"),
    "password": input("Enter Password: ")

}
with open("015_register.json", "w") as json_file:
    json.dump(user, json_file, index=4)
print("User informatiom has been saved to 015_register.json")
