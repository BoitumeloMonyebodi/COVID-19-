# COVID-19 Global Data Tracker

# 1. Setup & Imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Optional: Settings
pd.set_option('display.max_columns', None)
sns.set(style='whitegrid')

# 2. Load the Dataset
df = pd.read_csv('owid-covid-data.csv')

# Preview the data
print(df.head())

# 3. Initial Exploration
print(df.columns)
print(df.info())
print(df.isnull().sum().sort_values(ascending=False))

# 4. Data Cleaning
countries = ['Kenya', 'India', 'United States']
df = df[df['location'].isin(countries)]

df['date'] = pd.to_datetime(df['date'])

df = df.sort_values(by=['location', 'date'])
df[['total_cases', 'total_deaths', 'total_vaccinations']] = df[['total_cases', 'total_deaths', 'total_vaccinations']].interpolate()

# 5. Exploratory Data Analysis (EDA)
plt.figure(figsize=(12,6))
for country in countries:
    sns.lineplot(data=df[df['location'] == country], x='date', y='total_cases', label=country)
plt.title('Total COVID-19 Cases Over Time')
plt.ylabel('Total Cases')
plt.xlabel('Date')
plt.legend()
plt.tight_layout()
plt.show()

# 6. Vaccination Analysis
plt.figure(figsize=(12,6))
for country in countries:
    sns.lineplot(data=df[df['location'] == country], x='date', y='total_vaccinations', label=country)
plt.title('Total Vaccinations Over Time')
plt.ylabel('Total Vaccinations')
plt.xlabel('Date')
plt.legend()
plt.tight_layout()
plt.show()

# 7. Optional: Choropleth Map
latest = df[df['date'] == df['date'].max()]
fig = px.choropleth(latest, locations='iso_code', color='total_cases',
                    hover_name='location', color_continuous_scale='Reds',
                    title='Global COVID-19 Cases (Latest)')
fig.show()
