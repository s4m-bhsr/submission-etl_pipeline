import pandas as pd
import numpy as np
from datetime import datetime

def transform_data(products):
    print("🔧 Transforming data...")

    try:
        # Convert list of dict to DataFrame
        df = pd.DataFrame(products)
        print(f"📊 Initial data shape: {df.shape}")

        # Drop products with unknown titles
        df = df[df['title'].str.lower() != 'unknown product']
        print(f"🗃️ After removing 'unknown product' titles: {df.shape}")

        # Clean and convert price to float (assume in USD, convert to IDR)
        df['price'] = (
            df['price']
            .str.replace(r"[^\d.]", "", regex=True)
            .replace("", np.nan)
            .astype(float) * 16000  # USD to IDR conversion
        )

        # Extract numeric rating
        df['rating'] = df['rating'].str.extract(r"([\d.]+)").astype(float)

        # Extract number of color variants
        df['colors'] = df['colors'].str.extract(r"(\d+)").astype(int)

        # Clean size and gender fields
        df['size'] = df['size'].str.replace("Size:", "", regex=False).str.strip()
        df['gender'] = df['gender'].str.replace("Gender:", "", regex=False).str.strip()

        # Drop rows with missing values
        before_dropna = df.shape[0]
        df.dropna(inplace=True)
        after_dropna = df.shape[0]
        print(f"🧼 Dropped {before_dropna - after_dropna} rows with missing values")

        # Drop duplicate rows
        before_dedup = df.shape[0]
        df.drop_duplicates(inplace=True)
        after_dedup = df.shape[0]
        print(f"🧹 Dropped {before_dedup - after_dedup} duplicate rows")

        # Add timestamp
        df["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        print(f"✅ Final transformed data shape: {df.shape}")
        return df

    except Exception as e:
        print("❌ An error occurred during transformation:")
        print(f"   {e}")
        return pd.DataFrame()  # return empty DataFrame as fallback
