import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

os.makedirs('charts', exist_ok=True)

print("Loading COVID-19 dataset...")
df = pd.read_csv('covid_data.csv')

print(f"Original Data Shape: {df.shape}")
print(f"Columns: {df.shape[1]}")

relevant_cols = ['location', 'date', 'total_cases', 'total_deaths', 'new_cases', 'new_deaths', 'population']
df_clean = df[relevant_cols].copy()

df_clean = df_clean[df_clean['location'] != 'World']
df_clean = df_clean[~df_clean['location'].str.contains('income|International|Europe|Asia|Africa|America|Oceania', case=False, na=False)]

df_clean['date'] = pd.to_datetime(df_clean['date'], errors='coerce')

df_clean['total_cases'].fillna(0, inplace=True)
df_clean['total_deaths'].fillna(0, inplace=True)
df_clean['new_cases'].fillna(0, inplace=True)
df_clean['new_deaths'].fillna(0, inplace=True)

df_clean = df_clean.dropna(subset=['date'])

print(f"Cleaned Data Shape: {df_clean.shape}")

country_summary = df_clean.groupby('location').agg({
    'total_cases': 'max',
    'total_deaths': 'max',
    'population': 'first'
}).reset_index()

country_summary = country_summary[country_summary['total_cases'] > 0]
country_summary['death_rate'] = (country_summary['total_deaths'] / country_summary['total_cases'] * 100)

top_10_countries = country_summary.nlargest(10, 'total_cases')

print("\nTop 10 Most Affected Countries:")
print(top_10_countries[['location', 'total_cases', 'total_deaths', 'death_rate']].to_string(index=False))

selected_country = top_10_countries.iloc[0]['location']
print(f"\nAnalyzing trends for: {selected_country}")

country_data = df_clean[df_clean['location'] == selected_country].copy()
country_data = country_data.sort_values('date')

country_data['cases_7day_avg'] = country_data['new_cases'].rolling(window=7, min_periods=1).mean()

country_data['month'] = country_data['date'].dt.to_period('M')
monthly_data = country_data.groupby('month').agg({
    'new_cases': 'sum',
    'new_deaths': 'sum'
}).reset_index()

monthly_data['month'] = monthly_data['month'].astype(str)

print("\nMonthly Trends (Last 12 months):")
print(monthly_data.tail(12).to_string(index=False))

plt.figure(figsize=(14, 6))
plt.plot(country_data['date'], country_data['total_cases'], linewidth=2, color='#e74c3c')
plt.title(f'COVID-19 Total Cases Over Time - {selected_country}', fontsize=16, fontweight='bold')
plt.xlabel('Date', fontsize=12)
plt.ylabel('Total Cases', fontsize=12)
plt.grid(True, alpha=0.3)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('charts/cases_over_time.png', dpi=300)
plt.close()

plt.figure(figsize=(12, 8))
countries = top_10_countries['location'].tolist()
cases = top_10_countries['total_cases'].tolist()

colors = plt.cm.Spectral(np.linspace(0, 1, 10))
plt.barh(countries, cases, color=colors, edgecolor='black')
plt.title('Top 10 Countries by Total COVID-19 Cases', fontsize=16, fontweight='bold')
plt.xlabel('Total Cases', fontsize=12)
plt.ylabel('Country', fontsize=12)
plt.gca().invert_yaxis()
plt.grid(axis='x', alpha=0.3)
plt.tight_layout()
plt.savefig('charts/top10_countries.png', dpi=300)
plt.close()

plt.figure(figsize=(10, 8))
x = top_10_countries['total_cases']
y = top_10_countries['total_deaths']
countries_list = top_10_countries['location']

plt.scatter(x, y, s=200, alpha=0.6, c=range(10), cmap='viridis', edgecolors='black')

for i, country in enumerate(countries_list):
    plt.annotate(country, (x.iloc[i], y.iloc[i]), fontsize=9, ha='right')

plt.title('COVID-19 Cases vs Deaths (Top 10 Countries)', fontsize=16, fontweight='bold')
plt.xlabel('Total Cases', fontsize=12)
plt.ylabel('Total Deaths', fontsize=12)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('charts/cases_vs_deaths.png', dpi=300)
plt.close()

print("\nAnalysis Complete!")
print("Charts saved in 'charts/' folder:")
print("  - cases_over_time.png")
print("  - top10_countries.png")
print("  - cases_vs_deaths.png")
