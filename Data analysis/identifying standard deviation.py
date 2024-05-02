import pandas as pd
import numpy as np

# Load the data from the Excel file
file_path = "Miguel cleaned data.xlsx"
df = pd.read_excel(file_path)

# Extract the first 600 x and y coordinates
x_values = df['Centroid_Row'].iloc[:600].values
y_values = df['Centroid_Col'].iloc[:600].values

# Compute pairwise distances
distances = []
for x1, y1 in zip(x_values, y_values):
    row_distances = []
    for x2, y2 in zip(x_values, y_values):
        distance = np.sqrt((x1 - x2)**2 + (y1 - y2)**2)
        row_distances.append(distance)
    distances.append(row_distances)

distances = np.array(distances)

# Compute the standard deviation for each row of distances
std_devs = np.std(distances, axis=1)

# Add the standard deviations back to the original dataframe (or create a new dataframe)
df_std = df.iloc[:600].copy()
df_std['std_dev'] = std_devs

# Save the updated dataframe back to an Excel file (or a new file)
output_path = "Miguel cleaned data with std_dev.xlsx"
df_std.to_excel(output_path, index=False)

print("Done! Standard deviations added and saved to", output_path)
