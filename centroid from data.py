import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Replace this with the path to your data file
data_path = 'data_log_2023-10-12_19-24.csv'

# Read the data into a pandas DataFrame
df = pd.read_csv(data_path, delimiter=',', skipinitialspace=True)

# Define the column groups
llmlrl_columns = ['LL', 'ML', 'RL']
lumuru_columns = ['LU', 'MU', 'RU']
lbmbrb_columns = ['LB', 'MB', 'RB']

# Calculate the centroid for each row
df['Centroid_LLMLRL'] = df[llmlrl_columns].mean(axis=1)
df['Centroid_LUMURU'] = df[lumuru_columns].mean(axis=1)
df['Centroid_LBMBRB'] = df[lbmbrb_columns].mean(axis=1)

# Function to update the scatter plot for each row
def update_plot(frame):
    plt.clf()  # Clear the previous plot
    plt.scatter(df.iloc[frame][llmlrl_columns], df.iloc[frame][lumuru_columns], label='Data Points')
    plt.scatter(df.iloc[frame]['Centroid_LLMLRL'], df.iloc[frame]['Centroid_LUMURU'], marker='X', color='red', label='Centroid')
    plt.xlabel('LLMLRL')
    plt.ylabel('LUMURU')
    plt.title(f'Frame {frame + 1}')
    plt.legend()

# Create an animation
animation_fig = plt.figure(figsize=(8, 6))
animation_frames = len(df)

ani = animation.FuncAnimation(animation_fig, update_plot, frames=animation_frames, interval=500, repeat=False)

# Show the animation
plt.show()
