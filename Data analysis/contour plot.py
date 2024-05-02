import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Set the working directory to the script directory
script_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_directory)

# Load your Excel file containing multiple frames of 32x32 data
excel_file = '32x32 3 frames.xlsx'  # Adjust the filename with the correct extension
df = pd.read_excel(excel_file, header=None)

# Define the size of each frame
frame_height = 32
frame_width = 32
rows_between_frames = 3

# Initialize frame number
frame_num = 1

# Iterate over each frame and create a 3D contour plot
while True:
    # Extract data for the current frame
    start_row = (frame_num - 1) * (frame_height + rows_between_frames) + 2
    end_row = start_row + frame_height
    start_col = 0  # Assuming the first column is A
    end_col = frame_width  # Assuming the last column is AF

    # Check if there is data for the current frame
    if start_row >= df.shape[0]:
        break  # Exit the loop if there is no more data

    # Extract data for the current frame, excluding non-numeric values
    current_frame = df.iloc[start_row:end_row, start_col:end_col].apply(pd.to_numeric, errors='coerce').fillna(0)

    # Create meshgrid for X and Y values
    X, Y = np.meshgrid(np.arange(current_frame.shape[1]), np.arange(current_frame.shape[0]))

    # Flatten the data values for Z-axis
    Z = current_frame.values.flatten()

    # Create a 3D plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z.reshape(current_frame.shape), cmap='viridis')

    # Customize the plot as needed
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    ax.set_title(f'Frame {frame_num}')

    # Save or display the plot
    plt.savefig(f'3D_contour_plot_frame_{frame_num}.png')  # Save the plot
    plt.show()  # Display the plot

    # Move to the next frame
    frame_num += 1
