from utils.extract import collect_all_products
from utils.transform import transform_data
from utils.load import save_to_csv, save_to_google_sheets, save_to_postgres

def main():
    print("🚀 Starting ETL Process")
    print("="*60)

    # Extract
    print("\n📦 [1/3] Extracting data...")
    raw_data = collect_all_products()
    print(f"✅ Extracted {len(raw_data)} products")

    if not raw_data:
        print("❌ No data extracted. Terminating process.")
        return

    # Transform
    print("\n🧹 [2/3] Transforming data...")
    transformed = transform_data(raw_data)
    print(f"✅ Transformed data with shape: {transformed.shape}")

    # Load
    print("\n📤 [3/3] Loading data...")
    print("💾 Saving to CSV...")
    save_to_csv(transformed)

    print("🐘 Saving to PostgreSQL...")
    save_to_postgres(transformed)

    print("📄 Saving to Google Sheets...")
    save_to_google_sheets(
        transformed,
        spreadsheet_id="12UgW5b89lXCEeQLpls539lhmK6MYopd1yFk6FYVvDjI",
        range_name="Sheet1!A1"
    )

    print("\n🎉 ETL Process Completed Successfully!")
    print("="*60)


if __name__ == "__main__":
    main()
