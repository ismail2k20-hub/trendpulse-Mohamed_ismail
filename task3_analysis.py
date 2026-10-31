
"""
TrendPulse - Task 3: Analysis with Pandas and NumPy

This program analyses the cleaned stories from Task 2.
It calculates statistics, identifies trending categories,
creates new columns, and saves the analysed data.
"""

import pandas as pd
import numpy as np
import os


# --------------------------------------------------
# 1. LOAD AND EXPLORE THE DATA
# --------------------------------------------------

def load_data():

    # Read the cleaned CSV file created in Task 2
    input_file = "data/trends_clean.csv"

    if not os.path.exists(input_file):
        print("Error: trends_clean.csv not found.")
        print("Please complete Task 2 first.")
        return None

    df = pd.read_csv(input_file)

    print("Loaded data:", df.shape)

    # Display the first five rows
    print("\nFirst 5 rows:")
    print(df.head())

    # Display average score and comments
    print("\nAverage score:", df["score"].mean())
    print("Average comments:", df["num_comments"].mean())

    return df


# --------------------------------------------------
# 2. ANALYSIS USING NUMPY
# --------------------------------------------------

def analyse_data(df):

    print("\n--- NumPy Stats ---")

    # Convert score column into a NumPy array
    scores = df["score"].to_numpy()

    # Calculate statistical values
    mean_score = np.mean(scores)
    median_score = np.median(scores)
    std_score = np.std(scores)

    max_score = np.max(scores)
    min_score = np.min(scores)

    print("Mean score:", mean_score)
    print("Median score:", median_score)
    print("Std deviation:", std_score)
    print("Max score:", max_score)
    print("Min score:", min_score)

    # Find the category with the highest number of stories
    category_counts = df["category"].value_counts()

    if not category_counts.empty:

        most_category = category_counts.idxmax()
        most_category_count = category_counts.max()

        print(
            f"\nMost stories in: {most_category} "
            f"({most_category_count} stories)"
        )

    # Find the story with the highest number of comments
    most_commented_index = df["num_comments"].idxmax()

    most_commented_story = df.loc[most_commented_index]

    print("\n--- Most Commented Story ---")
    print("Title:", most_commented_story["title"])
    print("Comments:", most_commented_story["num_comments"])


# --------------------------------------------------
# 3. ADD NEW COLUMNS
# --------------------------------------------------

def add_columns(df):

    # Calculate the average score for all stories
    average_score = df["score"].mean()

    # Engagement measures comments relative to score
    # Adding 1 prevents division by zero
    df["engagement"] = (
        df["num_comments"] / (df["score"] + 1)
    )

    # A popular story has a score greater than average
    df["is_popular"] = df["score"] > average_score

    print("\n--- New Columns Added ---")
    print(df[[
        "title",
        "score",
        "num_comments",
        "engagement",
        "is_popular"
    ]].head())

    return df


# --------------------------------------------------
# 4. SAVE THE ANALYSED DATA
# --------------------------------------------------

def save_data(df):

    # Make sure the data folder exists
    os.makedirs("data", exist_ok=True)

    output_file = "data/trends_analysed.csv"

    # Save the updated DataFrame as CSV
    df.to_csv(output_file, index=False)

    print(f"\nSuccessfully saved {len(df)} rows to {output_file}")


# --------------------------------------------------
# 5. MAIN FUNCTION
# --------------------------------------------------

def main():

    print("=" * 50)
    print("TREND PULSE - DATA ANALYSIS")
    print("=" * 50)

    # Step 1: Load and explore data
    df = load_data()

    if df is None:
        return

    if df.empty:
        print("The cleaned CSV contains no stories.")
        return

    # Step 2: Perform NumPy analysis
    analyse_data(df)

    # Step 3: Add two new columns
    df = add_columns(df)

    # Step 4: Save the analysed data
    save_data(df)

    print("\nTask 3 completed successfully!")


# --------------------------------------------------
# 6. RUN THE PROGRAM
# --------------------------------------------------

if __name__ == "__main__":
    main()
