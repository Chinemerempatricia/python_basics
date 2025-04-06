
import pandas as pd

my_file=pd.read_json("029_data.json")

my_file.to_excel("031_data.xlsx",index=False)
print(my_file)

