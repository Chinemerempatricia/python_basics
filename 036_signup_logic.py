import json
with open("035_signup_data.json", "r")  as file:
    data = json.load(file)
new_user = {
        "id": input("Enter ID: "),
        "first_name": input("Enter First Name: "),
        "last_name": input("Enter Last Name: "),
        "email": input("Enter Email: "),
        "password": input("Enter Password: ")
}

data.append(new_user)

with open("035_signup_data.json", "w") as file:
    json.dump(data, file, indent=4)
print("User added successfully!")



