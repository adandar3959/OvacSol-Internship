import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

os.makedirs('charts', exist_ok=True)

df = pd.read_csv('student_marks.csv')

print("Original Data Shape:", df.shape)
print("\nMissing Values:\n", df.isnull().sum())

df_cleaned = df.drop_duplicates(subset=['Roll_Number'], keep='first')
print(f"\nDuplicates removed: {len(df) - len(df_cleaned)} records")

subject_cols = ['Math', 'Science', 'English', 'History', 'Geography']

for col in subject_cols:
    df_cleaned[col] = pd.to_numeric(df_cleaned[col], errors='coerce')
    df_cleaned[col] = df_cleaned[col].clip(lower=0, upper=100)
    df_cleaned[col].fillna(df_cleaned[col].median(), inplace=True)

df_cleaned['Total'] = df_cleaned[subject_cols].sum(axis=1)
df_cleaned['Average'] = df_cleaned[subject_cols].mean(axis=1)

def calculate_grade(avg):
    if avg >= 90:
        return 'A'
    elif avg >= 75:
        return 'B'
    elif avg >= 50:
        return 'C'
    else:
        return 'F'

df_cleaned['Grade'] = df_cleaned['Average'].apply(calculate_grade)

print("\nCleaned Data Shape:", df_cleaned.shape)
print("\nFirst 5 Records:\n", df_cleaned.head())

top_3 = df_cleaned.nlargest(3, 'Average')[['Roll_Number', 'Name', 'Average', 'Grade']]
bottom_3 = df_cleaned.nsmallest(3, 'Average')[['Roll_Number', 'Name', 'Average', 'Grade']]

print("\nTop 3 Students:")
print(top_3.to_string(index=False))

print("\nBottom 3 Students:")
print(bottom_3.to_string(index=False))

subject_avg = df_cleaned[subject_cols].mean()
highest_subject = subject_avg.idxmax()
lowest_subject = subject_avg.idxmin()

print(f"\nHighest Average Subject: {highest_subject} ({subject_avg[highest_subject]:.2f})")
print(f"Lowest Average Subject: {lowest_subject} ({subject_avg[lowest_subject]:.2f})")

plt.figure(figsize=(10, 6))
subject_avg.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Average Marks Per Subject', fontsize=16, fontweight='bold')
plt.xlabel('Subject', fontsize=12)
plt.ylabel('Average Marks', fontsize=12)
plt.xticks(rotation=45)
plt.ylim(0, 100)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('charts/average_marks_per_subject.png', dpi=300)
plt.close()

plt.figure(figsize=(10, 6))
plt.hist(df_cleaned['Average'], bins=15, color='lightgreen', edgecolor='black')
plt.title('Distribution of Student Average Scores', fontsize=16, fontweight='bold')
plt.xlabel('Average Score', fontsize=12)
plt.ylabel('Number of Students', fontsize=12)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('charts/score_distribution.png', dpi=300)
plt.close()

grade_counts = df_cleaned['Grade'].value_counts()
colors = ['#66c2a5', '#fc8d62', '#8da0cb', '#e78ac3']

plt.figure(figsize=(8, 8))
plt.pie(grade_counts, labels=grade_counts.index, autopct='%1.1f%%', 
        startangle=90, colors=colors, textprops={'fontsize': 12})
plt.title('Grade Distribution', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.savefig('charts/grade_distribution.png', dpi=300)
plt.close()

df_cleaned.to_csv('result_analysis_output.csv', index=False)

print("\nAnalysis Complete!")
print("Charts saved in 'charts/' folder")
print("Cleaned data saved to 'result_analysis_output.csv'")
