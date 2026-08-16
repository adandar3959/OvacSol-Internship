import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
from scipy import stats

os.makedirs('charts', exist_ok=True)

sns.set_style("whitegrid")
sns.set_palette("husl")

print("="*70)
print("TITANIC DATASET - EXPLORATORY DATA ANALYSIS")
print("="*70)

df = pd.read_csv('titanic.csv')

print("\n1. DATASET OVERVIEW")
print("-"*70)
print(f"Shape: {df.shape[0]} rows, {df.shape[1]} columns")
print(f"\nColumns and Data Types:")
print(df.dtypes)

print("\n2. MISSING VALUES")
print("-"*70)
missing = df.isnull().sum()
missing_pct = (df.isnull().sum() / len(df)) * 100
missing_df = pd.DataFrame({'Missing Count': missing, 'Percentage': missing_pct})
print(missing_df[missing_df['Missing Count'] > 0])

print("\n3. BASIC STATISTICS")
print("-"*70)
print(df.describe())

print("\n4. SURVIVAL RATE")
print("-"*70)
survival_rate = df['survived'].mean() * 100
print(f"Overall Survival Rate: {survival_rate:.2f}%")
print(f"Survived: {df['survived'].sum()} passengers")
print(f"Did not survive: {len(df) - df['survived'].sum()} passengers")

numerical_cols = ['age', 'fare', 'sibsp', 'parch']
categorical_cols = ['survived', 'pclass', 'sex', 'embarked', 'who', 'deck', 'embark_town', 'alive', 'alone']

print("\n" + "="*70)
print("GENERATING VISUALIZATIONS")
print("="*70)

print("\n[1/8] Survival Distribution (Univariate)...")
plt.figure(figsize=(8, 6))
survival_counts = df['survived'].value_counts()
colors = ['#e74c3c', '#2ecc71']
plt.bar(['Did Not Survive', 'Survived'], survival_counts.values, color=colors, edgecolor='black')
plt.title('Survival Distribution on Titanic', fontsize=16, fontweight='bold')
plt.xlabel('Survival Status', fontsize=12)
plt.ylabel('Number of Passengers', fontsize=12)
plt.grid(axis='y', alpha=0.3)
for i, v in enumerate(survival_counts.values):
    plt.text(i, v + 10, str(v), ha='center', fontsize=12, fontweight='bold')
plt.tight_layout()
plt.savefig('charts/1_survival_distribution.png', dpi=300)
plt.close()

print("[2/8] Age Distribution (Univariate)...")
plt.figure(figsize=(10, 6))
plt.hist(df['age'].dropna(), bins=30, color='skyblue', edgecolor='black', alpha=0.7)
plt.axvline(df['age'].mean(), color='red', linestyle='--', linewidth=2, label=f'Mean: {df["age"].mean():.1f}')
plt.axvline(df['age'].median(), color='green', linestyle='--', linewidth=2, label=f'Median: {df["age"].median():.1f}')
plt.title('Age Distribution of Titanic Passengers', fontsize=16, fontweight='bold')
plt.xlabel('Age (years)', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.legend()
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('charts/2_age_distribution.png', dpi=300)
plt.close()

print("[3/8] Correlation Heatmap (Multivariate)...")
plt.figure(figsize=(10, 8))
numerical_data = df[['survived', 'pclass', 'age', 'sibsp', 'parch', 'fare']].dropna()
correlation = numerical_data.corr()
sns.heatmap(correlation, annot=True, fmt='.2f', cmap='coolwarm', center=0, 
            square=True, linewidths=1, cbar_kws={"shrink": 0.8})
plt.title('Correlation Heatmap - Titanic Dataset', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.savefig('charts/3_correlation_heatmap.png', dpi=300)
plt.close()

print("[4/8] Boxplot for Outlier Detection (Univariate)...")
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Boxplots for Outlier Detection', fontsize=16, fontweight='bold')

sns.boxplot(data=df, y='age', ax=axes[0, 0], color='lightblue')
axes[0, 0].set_title('Age Distribution', fontweight='bold')
axes[0, 0].set_ylabel('Age (years)')

sns.boxplot(data=df, y='fare', ax=axes[0, 1], color='lightgreen')
axes[0, 1].set_title('Fare Distribution', fontweight='bold')
axes[0, 1].set_ylabel('Fare ($)')

sns.boxplot(data=df, y='sibsp', ax=axes[1, 0], color='lightcoral')
axes[1, 0].set_title('Siblings/Spouses Aboard', fontweight='bold')
axes[1, 0].set_ylabel('Count')

sns.boxplot(data=df, y='parch', ax=axes[1, 1], color='lightyellow')
axes[1, 1].set_title('Parents/Children Aboard', fontweight='bold')
axes[1, 1].set_ylabel('Count')

plt.tight_layout()
plt.savefig('charts/4_boxplot_outliers.png', dpi=300)
plt.close()

print("[5/8] Survival by Gender (Bivariate)...")
plt.figure(figsize=(10, 6))
survival_by_sex = df.groupby('sex')['survived'].mean() * 100
colors = ['#3498db', '#e74c3c']
bars = plt.bar(survival_by_sex.index, survival_by_sex.values, color=colors, edgecolor='black')
plt.title('Survival Rate by Gender', fontsize=16, fontweight='bold')
plt.xlabel('Gender', fontsize=12)
plt.ylabel('Survival Rate (%)', fontsize=12)
plt.ylim(0, 100)
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 2,
             f'{height:.1f}%', ha='center', fontsize=12, fontweight='bold')
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('charts/5_survival_by_gender.png', dpi=300)
plt.close()

print("[6/8] Survival by Class (Bivariate)...")
plt.figure(figsize=(10, 6))
survival_by_class = df.groupby('pclass')['survived'].mean() * 100
colors = ['#f39c12', '#9b59b6', '#1abc9c']
bars = plt.bar(['1st Class', '2nd Class', '3rd Class'], survival_by_class.values, 
               color=colors, edgecolor='black')
plt.title('Survival Rate by Passenger Class', fontsize=16, fontweight='bold')
plt.xlabel('Passenger Class', fontsize=12)
plt.ylabel('Survival Rate (%)', fontsize=12)
plt.ylim(0, 100)
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 2,
             f'{height:.1f}%', ha='center', fontsize=12, fontweight='bold')
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('charts/6_survival_by_class.png', dpi=300)
plt.close()

print("[7/8] Age vs Fare Scatter Plot (Bivariate)...")
plt.figure(figsize=(12, 6))
survived = df[df['survived'] == 1]
died = df[df['survived'] == 0]
plt.scatter(died['age'], died['fare'], c='red', alpha=0.5, s=50, label='Did Not Survive', edgecolors='black')
plt.scatter(survived['age'], survived['fare'], c='green', alpha=0.5, s=50, label='Survived', edgecolors='black')
plt.title('Age vs Fare (Colored by Survival)', fontsize=16, fontweight='bold')
plt.xlabel('Age (years)', fontsize=12)
plt.ylabel('Fare ($)', fontsize=12)
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig('charts/7_age_fare_scatter.png', dpi=300)
plt.close()

print("[8/8] Survival Heatmap by Class and Gender (Multivariate)...")
plt.figure(figsize=(10, 6))
survival_pivot = df.pivot_table(values='survived', index='pclass', columns='sex', aggfunc='mean')
sns.heatmap(survival_pivot, annot=True, fmt='.2%', cmap='RdYlGn', center=0.5,
            linewidths=2, cbar_kws={"shrink": 0.8})
plt.title('Survival Rate Heatmap: Class vs Gender', fontsize=16, fontweight='bold')
plt.xlabel('Gender', fontsize=12)
plt.ylabel('Passenger Class', fontsize=12)
plt.tight_layout()
plt.savefig('charts/8_survival_heatmap_class_gender.png', dpi=300)
plt.close()

print("\n" + "="*70)
print("OUTLIER DETECTION")
print("="*70)

def detect_outliers(data, column):
    Q1 = data[column].quantile(0.25)
    Q3 = data[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = data[(data[column] < lower_bound) | (data[column] > upper_bound)]
    return len(outliers), lower_bound, upper_bound

for col in ['age', 'fare', 'sibsp', 'parch']:
    outlier_count, lower, upper = detect_outliers(df, col)
    print(f"\n{col.upper()}:")
    print(f"  Outliers detected: {outlier_count}")
    print(f"  Valid range: {lower:.2f} to {upper:.2f}")

print("\n" + "="*70)
print("KEY INSIGHTS")
print("="*70)

print("\n1. Overall survival rate was {:.1f}%".format(survival_rate))
print("2. Women had {:.1f}% survival rate vs men at {:.1f}%".format(
    survival_by_sex['female'], survival_by_sex['male']))
print("3. 1st class passengers had {:.1f}% survival vs 3rd class at {:.1f}%".format(
    survival_by_class[1], survival_by_class[3]))
print("4. Average age of passengers was {:.1f} years".format(df['age'].mean()))
print("5. Fare prices ranged from ${:.2f} to ${:.2f}".format(
    df['fare'].min(), df['fare'].max()))

age_survived = df[df['survived'] == 1]['age'].mean()
age_died = df[df['survived'] == 0]['age'].mean()
print("6. Average age of survivors: {:.1f} vs non-survivors: {:.1f}".format(
    age_survived, age_died))

print("\n" + "="*70)
print("ANALYSIS COMPLETE!")
print("="*70)
print("\nAll visualizations saved in 'charts/' folder:")
print("  1. Survival distribution")
print("  2. Age distribution")
print("  3. Correlation heatmap")
print("  4. Boxplot outliers")
print("  5. Survival by gender")
print("  6. Survival by class")
print("  7. Age vs Fare scatter")
print("  8. Survival heatmap (class x gender)")
