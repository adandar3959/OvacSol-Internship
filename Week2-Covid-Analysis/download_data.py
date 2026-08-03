import requests
import os

url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"

print("Downloading COVID-19 dataset from Our World in Data...")

try:
    response = requests.get(url, timeout=30)
    response.raise_for_status()
    
    with open('covid_data.csv', 'wb') as file:
        file.write(response.content)
    
    file_size = os.path.getsize('covid_data.csv') / (1024 * 1024)
    print(f"Download successful! File size: {file_size:.2f} MB")
    print("Dataset saved as: covid_data.csv")
    
except requests.exceptions.RequestException as e:
    print(f"Error downloading dataset: {e}")
    print("\nAlternative: Download manually from:")
    print("https://covid.ourworldindata.org/data/owid-covid-data.csv")
