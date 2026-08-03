# COVID-19 Dataset Analysis

Real-world data analysis of COVID-19 cases, deaths, and recoveries using publicly available datasets.

## Setup

### 1. Create Virtual Environment

```bash
cd Week2-Covid-Analysis
python -m venv venv
source venv/Scripts/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Download Dataset

```bash
python download_data.py
```

This downloads the latest COVID-19 data from Our World in Data.

### 4. Run Analysis

```bash
python covid_analysis.py
```

## Output

- **Charts**: Saved in `charts/` folder
  - `cases_over_time.png`
  - `top10_countries.png`
  - `cases_vs_deaths.png`
- **Insights**: See `INSIGHTS.md`

## Dataset Source

- **Our World in Data**: COVID-19 dataset (owid-covid-data.csv)
- Updated regularly with global COVID-19 statistics
- Includes: cases, deaths, vaccinations, population data

## Analysis Includes

1. Data cleaning and preprocessing
2. Country-wise aggregation
3. Time-series trend analysis
4. Top 10 most affected countries
5. Cases vs deaths correlation
6. Visual insights
