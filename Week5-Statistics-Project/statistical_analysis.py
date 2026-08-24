import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from statistics import mode as stat_mode
import os

os.makedirs('charts', exist_ok=True)

np.random.seed(42)

print("="*70)
print("WEEK 5: STATISTICAL ANALYSIS PROJECT")
print("A/B Test Analysis - Website Conversion Rate")
print("="*70)

control_group = np.random.binomial(1, 0.10, 1000)
treatment_group = np.random.binomial(1, 0.13, 1000)

df = pd.DataFrame({
    'group': ['Control']*1000 + ['Treatment']*1000,
    'converted': np.concatenate([control_group, treatment_group])
})

df.to_csv('ab_test_data.csv', index=False)
print("\n✓ Dataset created: ab_test_data.csv")

print("\n" + "="*70)
print("1. DESCRIPTIVE STATISTICS")
print("="*70)

control = df[df['group'] == 'Control']['converted']
treatment = df[df['group'] == 'Treatment']['converted']

from statistics import mode as stat_mode

print("\nControl Group:")
print(f"  Sample size: {len(control)}")
print(f"  Conversions: {control.sum()}")
print(f"  Conversion rate: {control.mean():.4f} ({control.mean()*100:.2f}%)")
print(f"  Mean: {control.mean():.4f}")
print(f"  Median: {control.median():.4f}")
print(f"  Mode: {stat_mode(control)}")
print(f"  Variance: {control.var():.4f}")
print(f"  Std Dev: {control.std():.4f}")

print("\nTreatment Group:")
print(f"  Sample size: {len(treatment)}")
print(f"  Conversions: {treatment.sum()}")
print(f"  Conversion rate: {treatment.mean():.4f} ({treatment.mean()*100:.2f}%)")
print(f"  Mean: {treatment.mean():.4f}")
print(f"  Median: {treatment.median():.4f}")
print(f"  Mode: {stat_mode(treatment)}")
print(f"  Variance: {treatment.var():.4f}")
print(f"  Std Dev: {treatment.std():.4f}")

print("\n" + "="*70)
print("2. HYPOTHESIS TESTING")
print("="*70)

print("\nNull Hypothesis (H0): Treatment has NO effect (p_control = p_treatment)")
print("Alternative Hypothesis (H1): Treatment HAS effect (p_control ≠ p_treatment)")
print("Significance level (α): 0.05")

t_stat, p_value = stats.ttest_ind(control, treatment)

print(f"\nT-statistic: {t_stat:.4f}")
print(f"P-value: {p_value:.4f}")

if p_value < 0.05:
    print(f"\n✓ REJECT null hypothesis (p < 0.05)")
    print("  Conclusion: Treatment has a SIGNIFICANT effect")
else:
    print(f"\n✗ FAIL TO REJECT null hypothesis (p >= 0.05)")
    print("  Conclusion: Treatment has NO significant effect")

print("\n" + "="*70)
print("3. CONFIDENCE INTERVAL (95%)")
print("="*70)

control_ci = stats.t.interval(0.95, len(control)-1, 
                               loc=control.mean(), 
                               scale=stats.sem(control))
treatment_ci = stats.t.interval(0.95, len(treatment)-1, 
                                 loc=treatment.mean(), 
                                 scale=stats.sem(treatment))

print(f"\nControl 95% CI: [{control_ci[0]:.4f}, {control_ci[1]:.4f}]")
print(f"Treatment 95% CI: [{treatment_ci[0]:.4f}, {treatment_ci[1]:.4f}]")

print("\n" + "="*70)
print("4. PROBABILITY DISTRIBUTIONS")
print("="*70)

print("\nNormal Distribution Check (Shapiro-Wilk Test):")
_, p_control_normal = stats.shapiro(control[:50])
_, p_treatment_normal = stats.shapiro(treatment[:50])

print(f"  Control p-value: {p_control_normal:.4f}")
print(f"  Treatment p-value: {p_treatment_normal:.4f}")

print("\nBinomial Distribution (Expected):")
print(f"  Control: n=1000, p={control.mean():.4f}")
print(f"  Treatment: n=1000, p={treatment.mean():.4f}")

print("\n" + "="*70)
print("5. CORRELATION ANALYSIS")
print("="*70)

df['user_id'] = range(len(df))
df['group_numeric'] = df['group'].map({'Control': 0, 'Treatment': 1})

correlation = df[['group_numeric', 'converted']].corr()
print(f"\nCorrelation between Group and Conversion: {correlation.iloc[0,1]:.4f}")

print("\nNote: Correlation does NOT imply causation!")
print("We need hypothesis testing to establish causal relationship.")

print("\n" + "="*70)
print("GENERATING VISUALIZATIONS")
print("="*70)

print("\n[1/4] Conversion rate comparison...")
plt.figure(figsize=(10, 6))
conv_rates = df.groupby('group')['converted'].mean()
colors = ['#3498db', '#2ecc71']
bars = plt.bar(conv_rates.index, conv_rates.values, color=colors, edgecolor='black')
plt.title('A/B Test: Conversion Rate by Group', fontsize=16, fontweight='bold')
plt.xlabel('Group', fontsize=12)
plt.ylabel('Conversion Rate', fontsize=12)
plt.ylim(0, 0.20)
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 0.005,
             f'{height:.2%}', ha='center', fontsize=12, fontweight='bold')
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('charts/1_conversion_rates.png', dpi=300)
plt.close()

print("[2/4] Distribution comparison...")
plt.figure(figsize=(10, 6))
conv_counts = df.groupby(['group', 'converted']).size().unstack()
conv_counts.plot(kind='bar', color=['#e74c3c', '#2ecc71'], edgecolor='black')
plt.title('A/B Test: Conversions vs Non-Conversions', fontsize=16, fontweight='bold')
plt.xlabel('Group', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.legend(['Not Converted', 'Converted'], title='Status')
plt.xticks(rotation=0)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('charts/2_conversion_distribution.png', dpi=300)
plt.close()

print("[3/4] Normal distribution overlay...")
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
fig.suptitle('Distribution Analysis', fontsize=16, fontweight='bold')

axes[0].hist(control, bins=2, color='#3498db', alpha=0.7, edgecolor='black', density=True)
axes[0].set_title('Control Group', fontweight='bold')
axes[0].set_xlabel('Converted (0=No, 1=Yes)')
axes[0].set_ylabel('Density')
axes[0].grid(axis='y', alpha=0.3)

axes[1].hist(treatment, bins=2, color='#2ecc71', alpha=0.7, edgecolor='black', density=True)
axes[1].set_title('Treatment Group', fontweight='bold')
axes[1].set_xlabel('Converted (0=No, 1=Yes)')
axes[1].set_ylabel('Density')
axes[1].grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig('charts/3_distribution_comparison.png', dpi=300)
plt.close()

print("[4/4] Statistical test visualization...")
plt.figure(figsize=(10, 6))
groups = ['Control', 'Treatment']
means = [control.mean(), treatment.mean()]
stds = [control.std(), treatment.std()]

x_pos = np.arange(len(groups))
plt.bar(x_pos, means, yerr=stds, color=colors, alpha=0.7, 
        edgecolor='black', capsize=10, error_kw={'linewidth': 2})
plt.xticks(x_pos, groups)
plt.title(f'A/B Test Results (p-value: {p_value:.4f})', fontsize=16, fontweight='bold')
plt.xlabel('Group', fontsize=12)
plt.ylabel('Mean Conversion Rate', fontsize=12)
plt.ylim(0, 0.20)

if p_value < 0.05:
    plt.text(0.5, max(means) + 0.02, '* Significant difference', 
             ha='center', fontsize=12, color='red', fontweight='bold')

plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('charts/4_hypothesis_test_result.png', dpi=300)
plt.close()

print("\n" + "="*70)
print("SUMMARY & CONCLUSION")
print("="*70)

print(f"\nSample Sizes: Control={len(control)}, Treatment={len(treatment)}")
print(f"Conversion Rates: Control={control.mean():.2%}, Treatment={treatment.mean():.2%}")
print(f"Difference: {(treatment.mean() - control.mean()):.2%}")
print(f"P-value: {p_value:.4f}")

if p_value < 0.05:
    print("\n✓ CONCLUSION: Treatment significantly improves conversion rate")
    print(f"  Recommendation: Implement the treatment (new design/feature)")
else:
    print("\n✗ CONCLUSION: No significant difference detected")
    print(f"  Recommendation: Keep current design or run longer test")

print("\n" + "="*70)
print("ANALYSIS COMPLETE!")
print("="*70)
print("\nOutputs:")
print("  - Dataset: ab_test_data.csv")
print("  - Charts: charts/ folder (4 visualizations)")
print("\nAll statistical tests completed successfully!")
