import pandas as pd

# Define the path to the raw data file
data_path = '../data/raw/owid-covid-data.csv'  # Adjust path if necessary

# Load the dataset
def load_data():
    try:
        df = pd.read_csv(data_path)
        print("Data loaded successfully.")
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

# Clean the dataset
def clean_data(df):
    # Convert the 'date' column to datetime
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    
    # Drop rows with missing 'date' or critical columns
    df = df.dropna(subset=['date', 'total_cases', 'total_deaths', 'total_vaccinations'])
    
    # Fill missing values for numeric columns (e.g., 'total_cases', 'total_deaths')
    # You can choose to either fill with zero or use interpolation or forward-fill depending on your needs
    df['total_cases'] = df['total_cases'].fillna(0)
    df['total_deaths'] = df['total_deaths'].fillna(0)
    df['total_vaccinations'] = df['total_vaccinations'].fillna(0)

    # Optionally, filter the dataset for specific countries if needed
    # Example: Filter for USA, India, and Kenya
    countries_of_interest = ['USA', 'India', 'Kenya']
    df = df[df['location'].isin(countries_of_interest)]

    print("Data cleaned successfully.")
    return df

# Save the cleaned dataset to the processed folder
def save_cleaned_data(df):
    # Define the path to save the cleaned data
    processed_data_path = '../data/processed/cleaned_covid_data.csv'
    df.to_csv(processed_data_path, index=False)
    print(f"Cleaned data saved to: {processed_data_path}")

# Main function to clean data
if __name__ == '__main__':
    # Load the dataset
    covid_df = load_data()

    if covid_df is not None:
        # Clean the dataset
        cleaned_df = clean_data(covid_df)

        # Save the cleaned data
        save_cleaned_data(cleaned_df)
