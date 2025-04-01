import json
with open("009_data.json", "r") as file: 
    car = json.load(file)
print("Brand:", car["brand"])
print("Year:", car.get("year"))
print("Features:", car["features"])
print("Horsepower:", car["engine"]["horsepower"])
car["year"] = 2025
car["speed"] = "180 km/h"
print("Updated Car Data:", car)

