import json
import pandas as pd

with open("035_signup_data.json", "r") as file:
    data = json.load(file)
df = pd.DataFrame(data)
df.to_excel("038_first_exam_result.xlsx", index=False)
print("Excel file created successfully!")

