import pandas as pd

df = pd.read_excel("032_books.xlsx")

df . to_json("034_data.json",
orient="records", indent=4)
print("Conversion successful.")
