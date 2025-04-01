age = int(input("Enter your age: " ))

nationality = input("Enter your nationality: ").strip().lower()

if age >= 18 and nationality == "nigerian":
    print("You are eligible to vote in Nigeria.")

elif age  < 18 and nationality == "nigerian":
    print("You are too young to Vote.")
else:
    print("You must be a Nigerian Citizen to vote here.")

