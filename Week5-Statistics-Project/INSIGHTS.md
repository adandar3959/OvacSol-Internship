# Statistical Analysis - Key Insights

## Scenario

Website A/B test comparing conversion rates between control (old design) and treatment (new design) groups.

---

## Results

### Descriptive Statistics

**Control Group** (n=1000):
- Conversion rate: ~10%
- Mean: 0.10
- Std Dev: 0.30

**Treatment Group** (n=1000):
- Conversion rate: ~13%
- Mean: 0.13
- Std Dev: 0.34

**Difference**: +3 percentage points

---

### Hypothesis Testing

**H0**: Treatment has no effect (μ_control = μ_treatment)
**H1**: Treatment has an effect (μ_control ≠ μ_treatment)
**α**: 0.05 (significance level)

**Results**:
- T-statistic: ~-2.5
- P-value: ~0.01

**Conclusion**: P-value < 0.05 → Reject null hypothesis
Treatment has a **statistically significant** effect.

---

### Confidence Intervals (95%)

- Control: [0.08, 0.12]
- Treatment: [0.11, 0.15]

Intervals do NOT overlap → Supports significant difference.

---

### Correlation vs Causation

**Correlation found**: Group assignment correlates with conversion (+0.06)

**Causation established**: Because this is a controlled experiment (randomized A/B test), we CAN claim causation. The treatment caused the increase in conversion rate.

**Note**: In observational studies, correlation ≠ causation.

---

## Business Recommendation

✓ **Implement the new design**

**Reasoning**:
1. Statistically significant improvement (p < 0.05)
2. 30% relative increase in conversion rate (10% → 13%)
3. Large sample size (n=2000) provides confidence
4. Business impact: 3 more conversions per 100 visitors

**Expected Impact**: If site has 10,000 visitors/month, expect 300 additional conversions.

---

## Statistical Concepts Applied

1. **Descriptive Statistics**: Summarized data with mean, variance, std dev
2. **Probability Distributions**: Binomial distribution (conversion = success/failure)
3. **Hypothesis Testing**: T-test to compare two groups
4. **P-value**: Measured probability of observing results by chance
5. **Confidence Intervals**: Estimated range of true conversion rate
6. **Correlation vs Causation**: Established causal relationship through experiment design
