# NYC Yellow Taxi Trips Data Analysis

## Requirements
- Python 3.x
- pandas
- pyarrow

##installation

Clone the repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/nyc-yellow-taxi-trips.git
   cd nyc-yellow-taxi-trips



##file-structure
   
   nyc-yellow-taxi-trips/
├── yellow_tripdata_2024-01.parquet
├── analyze_taxi_data.py
└── filtered_yellow_taxi_trips.csv


#running-the-code

Navigate to the directory: cd /path/to/nyc-yellow-taxi-trips

python analyze_taxi_data.py

The script analyze_taxi_data.py performs several key operations:

Import Libraries:

Uses the pandas library for data manipulation.
Set File Path:

Specifies the path to the input file, which should be updated based on the user's local environment.
Load Data:

Reads the Parquet file into a DataFrame. If the file is not found, it handles the error gracefully.
Calculate the 90th Percentile:

Computes the 90th percentile of trip distances to identify outlier trips.
Filter Data:

Filters the DataFrame to retain only trips longer than the calculated 90th percentile.
Display Data:

Prints the filtered data for user inspection.
Save Filtered Data:

Exports the filtered data to a CSV file for further analysis.
Output
The output will be a CSV file named filtered_yellow_taxi_trips.csv, containing only the trips exceeding the 90th percentile distance.

Assumptions
The input Parquet file is properly formatted and accessible.
The relevant column for trip distances is named trip_distance.
Questions & Clarifications
If you have any questions or need further clarifications about the analysis or data, please feel free to reach out via email at [your-email@example.com].


#author

Akhila Ponugoti
