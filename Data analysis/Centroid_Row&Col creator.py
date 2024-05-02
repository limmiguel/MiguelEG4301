import pandas as pd
import numpy as np

# Read CSV file, skipping the first row (header)
csv_file_path = 'Li cher 3x3 25 March 2024.csv'
df = pd.read_csv(csv_file_path, skiprows=1, delimiter=',')

# Define pressure matrix size
rows = 3
cols = 3

# Initialize lists to store centroid coordinates
centroid_rows = []
centroid_cols = []

# Iterate over each row
for index, row in df.iterrows():
    matpressureData = row.iloc[1:10].dropna().tolist()

    if len(matpressureData) == rows * cols:
        pressure = np.array(matpressureData, dtype=float).reshape(rows, cols)

        total_pressure = np.sum(pressure)
        weighted_row = np.sum(np.sum(pressure, axis=1) * np.arange(rows))
        weighted_col = np.sum(np.sum(pressure, axis=0) * np.arange(cols))

        centroid_row = weighted_row / total_pressure
        centroid_col = weighted_col / total_pressure

        # Append centroid coordinates to lists
        centroid_rows.append(centroid_row)
        centroid_cols.append(centroid_col)
    else:
        # If there's an error, append NaN to lists
        centroid_rows.append(np.nan)
        centroid_cols.append(np.nan)

# Add new columns for centroid coordinates to the DataFrame
df['Centroid_Row'] = centroid_rows
df['Centroid_Col'] = centroid_cols

# Save the modified DataFrame to a new CSV file
output_csv_path = 'Li cher 3x3 25 March 2024.csv'
df.to_csv(output_csv_path, index=False)

print(f"Centroid coordinates added to the CSV file: {output_csv_path}")
