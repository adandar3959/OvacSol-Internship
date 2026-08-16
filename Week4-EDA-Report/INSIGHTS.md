# Titanic EDA - Key Insights

## Summary

Analysis of 891 Titanic passengers reveals gender and class were the strongest predictors of survival, demonstrating the "women and children first" protocol and socioeconomic advantages.

---

## Key Findings

### 1. Overall Survival
- **38.4% survived** (342 passengers)
- 61.6% perished (549 passengers)

### 2. Gender Impact - "Women and Children First"
- **Women**: 74.2% survival rate
- **Men**: 18.9% survival rate
- Women were 3.9x more likely to survive

### 3. Class Matters
- **1st Class**: 63.0% survival
- **2nd Class**: 47.3% survival
- **3rd Class**: 24.2% survival
- First-class passengers had 2.6x better survival than third-class

### 4. Combined Effect
**Survival Rate by Class and Gender:**
- 1st class women: 96.8% survival
- 1st class men: 36.9% survival
- 3rd class women: 50.0% survival
- 3rd class men: 13.5% survival

### 5. Age Distribution
- Mean age: 29.7 years
- Median age: 28.0 years
- Survivors slightly younger (28.3) than non-survivors (30.6)

### 6. Fare Analysis
- Median fare: $14.45
- Maximum fare: $512.33 (luxury suites)
- 116 fare outliers representing first-class accommodations

### 7. Correlations
- **Strongest with survival**: Class (-0.34), Fare (+0.26)
- **Pclass and Fare**: -0.55 (higher class = higher fare)
- Gender showed strongest predictive power (from visualization)

### 8. Outliers Detected
- **Age**: 10 extreme values (elderly passengers)
- **Fare**: 116 outliers (luxury accommodations)
- **Family size**: Large families (8+ relatives) present challenges

### 9. Missing Data
- Age: 177 missing (19.9%)
- Cabin: 687 missing (77.1%)
- Cabin data mostly missing for lower classes

---

## Visual Story

The Titanic disaster reveals stark inequalities:
- **Protocol**: "Women and children first" clearly followed
- **Privilege**: Class-based access to lifeboats created survival gaps
- **Result**: 1st class women had near-certain survival (97%), while 3rd class men faced 14% survival

---

## Recommendations

1. Impute missing age values for complete analysis
2. Analyze embarkation port impact
3. Create family size feature (sibsp + parch + 1)
4. Build predictive model using discovered patterns