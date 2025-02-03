import pandas as pd
import numpy as np
df = pd.read_csv("bike_dataset.csv")
df_filtered = df[df["type_of_bike"] != "Electric Bike"]
df_filtered.to_csv("Filtered_Bike_Dataset.csv", index=False)
print(df_filtered.head())