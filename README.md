COVID-19 Global Data Tracker
Project Overview
The COVID-19 Global Data Tracker project aims to track and visualize global COVID-19 trends, including cases, deaths, recoveries, and vaccinations. Using real-world data, this project performs data cleaning, exploratory data analysis (EDA), and generates insights through interactive visualizations. The goal is to provide a comprehensive overview of the pandemic's impact across countries and regions over time.

Project Objectives
Data Collection: Obtain a reliable COVID-19 dataset.

Data Exploration: Load, explore, and clean the dataset.

Trend Analysis: Analyze COVID-19 trends (cases, deaths, and vaccinations) over time.

Visualization: Create visualizations using matplotlib, seaborn, and Plotly.

Insights & Reporting: Summarize key findings and present them in a well-documented report.

Technologies Used
Python: The primary programming language.

pandas: Data manipulation and cleaning.

matplotlib & seaborn: Data visualization.

Plotly: Interactive visualizations (for maps).

Jupyter Notebook: For documenting and running the analysis.

Dataset
The dataset used for this project is the COVID-19 dataset from Our World in Data. It contains global COVID-19 data, including total cases, deaths, recoveries, and vaccinations, by country and date.

You can download the dataset from the following link:

Our World in Data COVID-19 Dataset

Steps to Reproduce
Data Collection: Download the dataset (owid-covid-data.csv) and place it in your working directory.

Data Loading & Exploration: Load the dataset using pandas and check for missing values.

python
Copy code
import pandas as pd
df = pd.read_csv('owid-covid-data.csv')
print(df.head())
print(df.isnull().sum())
Data Cleaning: Filter the countries of interest, drop rows with missing values, and convert the date column to a datetime object.

python
Copy code
df_filtered = df[df['location'].isin(['Kenya', 'USA', 'India'])]
df_filtered['date'] = pd.to_datetime(df_filtered['date'])
df_filtered = df_filtered.dropna(subset=['total_cases', 'total_deaths'])
Exploratory Data Analysis (EDA): Plot total cases, deaths, and daily new cases over time.

python
Copy code
import matplotlib.pyplot as plt
for country in ['Kenya', 'USA', 'India']:
    country_data = df_filtered[df_filtered['location'] == country]
    plt.plot(country_data['date'], country_data['total_cases'], label=country)
plt.title('Total COVID-19 Cases Over Time')
plt.legend()
plt.show()
Vaccination Progress: Visualize the vaccination rollout and compare the vaccination rates.

python
Copy code
for country in ['Kenya', 'USA', 'India']:
    country_data = df_filtered[df_filtered['location'] == country]
    plt.plot(country_data['date'], country_data['total_vaccinations'], label=country)
plt.title('COVID-19 Vaccinations Over Time')
plt.legend()
plt.show()
Optional Choropleth Map: Visualize global COVID-19 cases on an interactive map.

python
Copy code
import plotly.express as px
choropleth_df = df_filtered[df_filtered['date'] == df_filtered['date'].max()]
fig = px.choropleth(choropleth_df, locations='iso_code', color='total_cases', title="COVID-19 Total Cases by Country")
fig.show()
Insights & Reporting: Write a report summarizing the key insights and findings. Use Jupyter Notebook's Markdown cells to add commentary, and export the report as a PDF if needed.

Deliverables
Jupyter Notebook: Contains the Python code, visualizations, and analysis.

Insights: Written narrative summarizing key trends (e.g., country comparisons, vaccination rollouts, etc.).

Optional: Exported PDF or PowerPoint with visualizations.

Insights & Observations
The USA has the highest total COVID-19 cases, followed by India, which also has a significantly higher death rate relative to its cases.

Kenya's vaccination rate has increased steadily, and it is nearing 50% of the population vaccinated.

Global vaccination rollouts have been slower in many developing countries compared to countries with more resources.

Future Improvements
More Countries: Extend the analysis to more countries or regions.

Recovery Data: Include data on recoveries and analyze recovery rates.

Advanced Visualizations: Use GeoPandas for more advanced geographical data analysis.

License
This project is licensed under the MIT License - see the LICENSE file for details.

By following the steps in the README, you should be able to replicate the project and analyze COVID-19 trends globally. The code and insights will help present a comprehensive analysis of the pandemic's impact.




