student_info = {"name": "Bola Tinubu",
                "age": 20, "grade": "C",
                "subjects": ["maths", "physics", "chemistry"],
                "address": {"city": "Lagos",
                            "country": "Nigeria"}
                }


print("Name:", student_info["name"])


print("Age:", student_info.get("age"))

print("Subjects:", student_info["subjects"])

print("City:", student_info["address"]["city"])

student_info["grade"] = "A"
student_info["GPA"] = 4.5
student_info.update({"age": 21, "school": "OAU"})

print("Updated Dictionary:", student_info)

del student_info["GPA"]
print("After removing GPA:", student_info)

student_info.pop("age")
print("After removing age:", student_info)
print("Length of student_info:", len(student_info))

print("Keys:", student_info.keys())

print("Values:", student_info.values())

print("Keys and Values:", student_info.items())

print("Keys:")
for key in student_info:
    print(key)

print("Keys and Values:")
for key, value in student_info.items():
    print(f"{key}: {value}")






