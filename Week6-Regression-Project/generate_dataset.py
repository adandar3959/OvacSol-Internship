import numpy as np
import pandas as pd
import os

def generate_housing_dataset(num_samples=1200, random_seed=42):
    """
    Generates a realistic California-style Housing Dataset for regression tasks.
    Features:
      - MedInc: Median Income in block group ($10,000s)
      - HouseAge: Median age of houses (years)
      - AveRooms: Average number of rooms per household
      - AveBedrms: Average number of bedrooms per household
      - Population: Block group population count
      - AveOccup: Average number of household members
      - Latitude: Block group latitude
      - Longitude: Block group longitude
      - Target: HousePrice (Median house value in $100,000s)
    """
    np.random.seed(random_seed)

    # Feature generation with realistic ranges and distributions
    med_inc = np.random.gamma(shape=3.0, scale=1.2, size=num_samples) + 0.5
    house_age = np.random.uniform(5, 52, size=num_samples)
    ave_rooms = 3.0 + 0.6 * med_inc + np.random.normal(0, 0.8, size=num_samples)
    ave_rooms = np.clip(ave_rooms, 1.5, 12.0)
    
    ave_bedrms = 0.2 * ave_rooms + np.random.normal(0.5, 0.15, size=num_samples)
    ave_bedrms = np.clip(ave_bedrms, 0.8, 4.0)

    population = np.random.exponential(scale=1200, size=num_samples) + 200
    population = np.clip(population, 200, 8000)

    ave_occup = np.random.normal(3.0, 0.6, size=num_samples)
    ave_occup = np.clip(ave_occup, 1.2, 6.5)

    latitude = np.random.uniform(32.5, 42.0, size=num_samples)
    longitude = np.random.uniform(-124.3, -114.1, size=num_samples)

    # Underlying physical relationship for target variable: HousePrice ($100,000s)
    # Price is strongly positively correlated with Median Income, moderately with AveRooms & HouseAge,
    # negatively affected by high occupancy/extreme distance, plus stochastic Gaussian noise.
    price = (
        0.42 * med_inc
        + 0.015 * house_age
        + 0.08 * ave_rooms
        - 0.05 * ave_bedrms
        - 0.00002 * population
        - 0.04 * ave_occup
        + 0.02 * (latitude - 34.0)
        + 0.03 * (-118.0 - longitude)
        + 0.85
        + np.random.normal(0, 0.35, size=num_samples)
    )

    price = np.clip(price, 0.5, 5.0)

    df = pd.DataFrame({
        'MedInc': np.round(med_inc, 4),
        'HouseAge': np.round(house_age, 1),
        'AveRooms': np.round(ave_rooms, 2),
        'AveBedrms': np.round(ave_bedrms, 2),
        'Population': np.round(population, 0).astype(int),
        'AveOccup': np.round(ave_occup, 2),
        'Latitude': np.round(latitude, 4),
        'Longitude': np.round(longitude, 4),
        'HousePrice': np.round(price, 4)
    })

    return df

if __name__ == '__main__':
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(script_dir, 'housing_data.csv')
    df = generate_housing_dataset()
    df.to_csv(output_path, index=False)
    print(f"Dataset successfully created at '{output_path}'")
    print(f"Shape: {df.shape}")
    print("\nFirst 5 rows:")
    print(df.head())
