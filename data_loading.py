# Import necessary libraries
import pandas as pd

# Define the path to the dataset (adjust if necessary)
data_path = '../data/raw/owid-covid-data.csv'  # Ensure this points to your raw CSV file

# Load the dataset
def load_data():
    try:
        df = pd.read_csv(data_path)
        print("Data loaded successfully.")
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

# Explore the dataset
def explore_data(df):
    # Show basic information about the data
    print("Data Info:")
    print(df.info())
    
    # Show the first 5 rows of the dataset
    print("\nFirst 5 rows of data:")
    print(df.head())
    
    # Check for missing values
    print("\nMissing values:")
    print(df.isnull().sum())

# Main function to load and explore data
if __name__ == '__main__':
    # Load the dataset
    covid_df = load_data()

    if covid_df is not None:
        # Explore the dataset
        explore_data(covid_df)
