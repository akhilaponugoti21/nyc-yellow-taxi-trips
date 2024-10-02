import pandas as pd

# Set the file path (update this path according to your file location)
file_path = '/Users/akhilaponugoti/Desktop/Math-in-ML/yellow_tripdata_2024-01.parquet'

# Load the Parquet file into a DataFrame
df = pd.read_parquet(file_path)

# Calculate the 90th percentile for trip distance
percentile_90 = df['trip_distance'].quantile(0.9)

# Filter the rows where trip distance is greater than the 90th percentile
filtered_df = df[df['trip_distance'] > percentile_90]

# Display the top rows of the filtered DataFrame
print("Top rows of filtered DataFrame:")
print(filtered_df.head())

# Display the entire filtered DataFrame (consider limiting the output for large DataFrames)
print("\nEntire filtered DataFrame:")
print(filtered_df)

# Optional: Save the filtered DataFrame to a CSV file for easy access
filtered_df.to_csv('filtered_yellow_taxi_trips.csv', index=False)
print("Filtered data saved to 'filtered_yellow_taxi_trips.csv'.")



