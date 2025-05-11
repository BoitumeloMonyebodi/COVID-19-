import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned data
data_path = '../data/processed/cleaned_covid_data.csv'
df = pd.read_csv(data_path)

# Convert the 'date' column to datetime
df['date'] = pd.to_datetime(df['date'])

# Filter data for a specific country (e.g., USA, India, Kenya)
countries_of_interest = ['USA', 'India', 'Kenya']
df_filtered = df[df['location'].isin(countries_of_interest)]

# Plot total cases over time for the selected countries
plt.figure(figsize=(12, 6))
sns.lineplot(data=df_filtered, x='date', y='total_cases', hue='location')
plt.title('Total COVID-19 Cases Over Time (Selected Countries)', fontsize=16)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Total Cases', fontsize=14)
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig('../images/total_cases_over_time.png')
plt.show()

# Plot total deaths over time for the selected countries
plt.figure(figsize=(12, 6))
sns.lineplot(data=df_filtered, x='date', y='total_deaths', hue='location')
plt.title('Total COVID-19 Deaths Over Time (Selected Countries)', fontsize=16)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Total Deaths', fontsize=14)
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig('../images/total_deaths_over_time.png')
plt.show()

# Plot total vaccinations over time for the selected countries
plt.figure(figsize=(12, 6))
sns.lineplot(data=df_filtered, x='date', y='total_vaccinations', hue='location')
plt.title('Total COVID-19 Vaccinations Over Time (Selected Countries)', fontsize=16)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Total Vaccinations', fontsize=14)
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig('../images/total_vaccinations_over_time.png')
plt.show()

# Calculate and plot vaccination rate over time
df_filtered['vaccination_rate'] = df_filtered['total_vaccinations'] / df_filtered['population'] * 100
plt.figure(figsize=(12, 6))
sns.lineplot(data=df_filtered, x='date', y='vaccination_rate', hue='location')
plt.title('COVID-19 Vaccination Rate Over Time (Selected Countries)', fontsize=16)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Vaccination Rate (%)', fontsize=14)
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig('../images/vaccination_rate_over_time.png')
plt.show()

# Calculate and plot death rate over time
df_filtered['death_rate'] = df_filtered['total_deaths'] / df_filtered['total_cases'] * 100
plt.figure(figsize=(12, 6))
sns.lineplot(data=df_filtered, x='date', y='death_rate', hue='location')
plt.title('COVID-19 Death Rate Over Time (Selected Countries)', fontsize=16)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Death Rate (%)', fontsize=14)
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig('../images/death_rate_over_time.png')
plt.show()
