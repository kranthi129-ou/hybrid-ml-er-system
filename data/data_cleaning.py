import pandas as pd
import re
import numpy as np

from sqlalchemy import create_engine

engine = create_engine("postgresql+psycopg2://postgres:Jelly22fi$h@localhost:5432/er_db")
abt_raw = pd.read_sql("SELECT * FROM abt_products", con=engine)
buy_raw = pd.read_sql("SELECT * FROM buy_products", con=engine)

# === Utility Cleaning Functions ===
def clean_text(text):
    if pd.isnull(text):
        return ''
    text = text.lower().strip()
    text = re.sub(r'[^a-z0-9\s]', '', text)  # remove symbols
    return text

def clean_price(price):
    if pd.isnull(price):
        return np.nan
    price = re.sub(r'[^0-9.]', '', str(price))
    try:
        return float(price)
    except:
        return np.nan

# === Clean Abt Dataset ===
abt = abt_raw.copy()
abt['name_clean'] = abt['name'].apply(clean_text)
abt['description_clean'] = abt['description'].apply(clean_text)
abt['price_clean'] = abt['price'].apply(clean_price)
abt['brand_clean'] = abt['name_clean'].apply(lambda x: x.split()[0] if len(x.split()) > 0 else '')

# Flag and log rows with missing or bad price
abt['price_flag'] = abt['price_clean'].isnull()

# === Clean Buy Dataset ===
buy = buy_raw.copy()
buy['name_clean'] = buy['name'].apply(clean_text)
buy['description_clean'] = buy['description'].apply(clean_text)
buy['manufacturer_clean'] = buy['manufacturer'].apply(clean_text)
buy['price_clean'] = buy['price'].apply(clean_price)
buy['brand_clean'] = buy['manufacturer_clean'].fillna('').apply(lambda x: x.split()[0] if len(x.split()) > 0 else '')

# Flag and log rows with missing or bad price
buy['price_flag'] = buy['price_clean'].isnull()

# === Save Cleaned Outputs ===
abt.to_sql("abt_cleaned", con=engine, if_exists='replace', index=False)
buy.to_sql("buy_cleaned", con=engine, if_exists='replace', index=False)
