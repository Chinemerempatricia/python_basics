import json
json_file = "016_data.json"
try:
    with open(json_file, "r") as file:
        my_list_dict =json.load(file)
        if not isinstance(my_list_dict, list):
            my_list_dict = []
except (FileNotFoundError, json.JSONDecodeError):
    my_list_dict = []
data_dict = {
    "id": input("Enter ID: "),
    "first_name": input("Enter First Name: "),
    "middle_name": input("Enter Middle Name: "),
    "last_name": input("Enter Last Name: "),
    "email": input("Enter Email: "),
    "password": input("Enter Password: ")

}

with open(json_file, "w") as file:
    json.dump(my_list_dict, file, indent =4)
print("Data has been appended to 016_data.json")
