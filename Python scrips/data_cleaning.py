

# Filter countries of interest (e.g., Kenya, USA, India)
countries_of_interest = ['Kenya', 'USA', 'India']
df_filtered = df[df['location'].isin(countries_of_interest)]

# Drop rows with missing critical values (e.g., dates, total_cases)
df_filtered = df_filtered.dropna(subset=['date', 'total_cases', 'total_deaths'])

# Convert 'date' column to datetime
df_filtered['date'] = pd.to_datetime(df_filtered['date'])

# Handle missing numeric values by interpolation
df_filtered['total_cases'] = df_filtered['total_cases'].fillna(method='ffill')
df_filtered['total_deaths'] = df_filtered['total_deaths'].fillna(method='ffill')

