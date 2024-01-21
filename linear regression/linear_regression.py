import pandas as pd
import requests
import json
import io
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
# GitHub raw content URL
raw_content_url = 'https://raw.githubusercontent.com/JaCARYK/Weather-Application_baht/main/linear%20regression/weather_data.csv'

# Download the raw content
response = requests.get(raw_content_url)


# Read CSV file directly from content
df = pd.read_csv(io.StringIO(response.text))

print(df)  # Print columns to check if 'Date' is present


