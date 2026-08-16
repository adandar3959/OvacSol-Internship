# Titanic Dataset - Exploratory Data Analysis

Complete EDA with 8 visualizations analyzing passenger survival patterns.

## Dataset

**Source**: Titanic passenger data (built-in to Seaborn library)
**Size**: 891 passengers
**No Kaggle download needed** - Dataset loads automatically from seaborn

## Setup & Run

```bash
cd Week4-EDA-Report
python -m venv venv
venv\Scripts\activate
pip install pandas numpy matplotlib seaborn scipy
python download_data.py
python eda_analysis.py
```

## Analysis Performed

**Univariate**: Survival distribution, age distribution, outlier detection
**Bivariate**: Survival by gender/class, age vs fare
**Multivariate**: Correlation heatmap, survival patterns

## Output

8 visualizations saved in `charts/` folder showing survival patterns by gender, class, age, and fare.
