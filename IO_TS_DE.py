import requests
import zipfile
import io
import pandas as pd

# Base parameters
BASE_URL = 'https://www-genesis.destatis.de/genesisWS/rest/2020/'
API_TOKEN = "you token"
LANGUAGE = 'en'

headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'username': API_TOKEN,
    'password': ''
}

# List of table codes (different revisions)
TABLE_CODES = [
    '81511-0001',
    '81511-0002',
    '81511-0003',
    '81511-0004',
    '81511-0005'
]

def unzip_csv(response):
    """
    Unzip the response content and return the first CSV file handle.
    """
    file_bytes = io.BytesIO(response.content)
    with zipfile.ZipFile(file_bytes) as zf:
        csv_filename = zf.namelist()[0]
        return zf.open(csv_filename)

def read_csv_file(csv_file):
    """
    Read a semicolon-delimited CSV, handling European-style decimals and common NA markers.
    """
    return pd.read_csv(
        csv_file,
        delimiter=';',
        decimal=',',
        na_values=["...", ".", "-", "/", "x"]
    )

def download_and_combine_tables(table_codes):
    """
    Download each table, unzip it, read into a DataFrame, 
    tag it with its source code, and concatenate all into one DataFrame.
    """
    frames = []
    for code in table_codes:
        print(f"📥 Downloading table {code}...")
        response = requests.post(
            BASE_URL + 'data/tablefile',
            headers=headers,
            data={
                'name': code,
                'compress': 'true',
                'format': 'ffcsv',
                'language': LANGUAGE
            }
        )
        
        if response.status_code == 200:
            csv_file = unzip_csv(response)
            df = read_csv_file(csv_file)
            df["source_table"] = code  # keep track of origin
            frames.append(df)
            print(f"✅ Successfully loaded {code} ({df.shape[0]} rows)")
        else:
            print(f"❌ Failed to download {code}: HTTP {response.status_code}")

    combined_df = pd.concat(frames, ignore_index=True)
    print(f"\n📊 All tables combined into DataFrame with shape: {combined_df.shape}")
    return combined_df

if __name__ == "__main__":
    # Download and merge all specified tables
    df_all = download_and_combine_tables(TABLE_CODES)
    
    # Show a sample of the combined data
    print("\n=== Sample of Combined Data ===")
    print(df_all.head())
