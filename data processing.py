import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.animation import FuncAnimation

# Replace 'your_data.csv' with the actual CSV file containing your data
csv_file_path = 'data_log_2023-10-12_19-24.csv'

# Read the data from the CSV file
df = pd.read_csv(csv_file_path)

# Extract relevant columns for each row
columns = ['Date/Time', 'LL', 'ML', 'RL', 'LU', 'MU', 'RU', 'LB', 'MB', 'RB']

# Convert the 'Date/Time' column to datetime format with the correct format
df['Date/Time'] = pd.to_datetime(df['Date/Time'], format='%H:%M:%S')

# Reshape the data into a 3x3 matrix for each row
data_matrix = np.array([df.loc[:, columns[1:]].iloc[i].astype(float).values.reshape(3, 3) for i in range(len(df))])

# Create a function to update the plot in each animation frame
def update(frame):
    plt.clf()  # Clear the previous plot
    plt.contourf(data_matrix[frame], cmap='viridis')
    # Display date and time in the title
    plt.title(f'Contour Plot at {df["Date/Time"].iloc[frame].strftime("%H:%M:%S")}')
    plt.xlabel('Column')
    plt.ylabel('Row')
    plt.colorbar()

# Create an animation
animation = FuncAnimation(plt.figure(), update, frames=len(data_matrix), interval=500)

# Show the animation
plt.show()
