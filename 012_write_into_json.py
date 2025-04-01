import json
student = {
    "id": 101,
    "name": "Ebere John",
    "gender": "Male",
    "department": "Accountancy",
    "school": "University of Nigeria Nsukka"
}
with open("013_data.json", "w") as json_file:
    json.dump(student, json_file, indent=4)
print("Data successfully written to 013_data.json")
