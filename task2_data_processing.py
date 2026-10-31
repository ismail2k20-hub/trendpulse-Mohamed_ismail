
"""
TrendPulse - Task 2: Clean the Data and Save as CSV

This program loads the JSON file created in Task 1,
cleans the data using Pandas, and saves it as a CSV file.
"""

import pandas as pd
import glob
import os


# --------------------------------------------------
# 1. FIND AND LOAD THE JSON FILE
# --------------------------------------------------

def load_data():

    # Find all JSON files created by Task 1
    json_files = glob.glob("data/trends_*.json")

    if not json_files:
        print("Error: No JSON file found in the data folder.")
        return None

    # Select the latest JSON file
    input_file = sorted(json_files)[-1]

    print(f"Loading file: {input_file}")

    # Load JSON data into a Pandas DataFrame
    df = pd.read_json(input_file)

    print(f"Loaded {len(df)} stories.")

    return df


# --------------------------------------------------
# 2. CLEAN THE DATA
# --------------------------------------------------

def clean_data(df):

    # Make a copy so that the original DataFrame is unchanged
    df = df.copy()

    # Convert score and num_comments into numeric values.
    # Invalid score values become missing and will be removed.
    df["score"] = pd.to_numeric(df["score"], errors="coerce")

    df["num_comments"] = pd.to_numeric(
        df["num_comments"], errors="coerce"
    )

    # Remove duplicate stories using post_id
    df = df.drop_duplicates(subset="post_id", keep="first")

    print(f"After removing duplicates: {len(df)}")

    # Remove rows where important fields are missing
    df = df.dropna(subset=["post_id", "title", "score"])

    print(f"After removing nulls: {len(df)}")

    # Remove unnecessary spaces from story titles
    df["title"] = df["title"].astype(str).str.strip()

    # Remove stories with empty titles
    df = df[df["title"] != ""]

    # Replace missing or invalid comment counts with zero
    df["num_comments"] = df["num_comments"].fillna(0)

    # Convert score and num_comments to integers
    df["score"] = df["score"].astype(int)
    df["num_comments"] = df["num_comments"].astype(int)

    # Remove stories with a score below 5
    df = df[df["score"] >= 5]

    print(f"After removing low scores: {len(df)}")

    return df


# --------------------------------------------------
# 3. SAVE THE CLEANED DATA AS CSV
# --------------------------------------------------

def save_data(df):

    # Make sure the data folder exists
    os.makedirs("data", exist_ok=True)

    # Save the cleaned DataFrame as CSV
    output_file = "data/trends_clean.csv"

    df.to_csv(output_file, index=False, encoding="utf-8")

    print(f"\nSaved {len(df)} rows to {output_file}")

    # Display the number of stories in each category
    print("\nStories per category:")

    category_summary = df["category"].value_counts()

    print(category_summary.to_string())


# --------------------------------------------------
# 4. MAIN FUNCTION
# --------------------------------------------------

def main():

    print("=" * 50)
    print("TREND PULSE - DATA CLEANING")
    print("=" * 50)

    # Step 1: Load the JSON file
    df = load_data()

    if df is None:
        return

    # Step 2: Clean the data
    cleaned_df = clean_data(df)

    # Step 3: Save the cleaned data
    save_data(cleaned_df)

    print("\nTask 2 completed successfully!")


# --------------------------------------------------
# 5. RUN THE PROGRAM
# --------------------------------------------------

if __name__ == "__main__":
    main()
