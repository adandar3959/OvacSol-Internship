# Statistical Analysis - A/B Testing

A/B test analysis comparing website conversion rates using statistical methods.

## Setup & Run

```bash
cd Week5-Statistics-Project
python -m venv venv
venv\Scripts\activate
pip install pandas numpy matplotlib seaborn scipy
python statistical_analysis.py
```

## Analysis

**Scenario**: Testing if a new website design increases conversion rate

**Methods Used**:
- Descriptive statistics (mean, variance, std dev)
- Hypothesis testing (t-test)
- P-value calculation
- 95% Confidence intervals
- Probability distributions

## Output

- `ab_test_data.csv` - Generated A/B test dataset
- 4 visualizations in `charts/` folder
- Statistical test results with recommendation
