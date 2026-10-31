
"""
TrendPulse - Task 4: Data Visualisation

This program creates three charts using Matplotlib
and combines them into one dashboard.
"""

import pandas as pd
import matplotlib.pyplot as plt
import os


# --------------------------------------------------
# 1. LOAD DATA AND CREATE OUTPUT FOLDER
# --------------------------------------------------

def load_data():

    input_file = "data/trends_analysed.csv"

    if not os.path.exists(input_file):
        print("Error: trends_analysed.csv not found.")
        print("Please complete Task 3 first.")
        return None

    df = pd.read_csv(input_file)

    if df.empty:
        print("Error: The CSV file contains no stories.")
        return None

    # Convert the popularity column into True/False values
    df["is_popular"] = (
        df["is_popular"]
        .astype(str)
        .str.strip()
        .str.lower()
        .map({"true": True, "false": False})
    )

    # Create outputs folder if it does not exist
    os.makedirs("outputs", exist_ok=True)

    print("Data loaded successfully.")
    print("Total stories:", len(df))

    return df


# --------------------------------------------------
# 2. CHART 1 - TOP 10 STORIES BY SCORE
# --------------------------------------------------

def create_chart1(df, ax=None):

    # Select the 10 stories with the highest scores
    top_stories = df.nlargest(10, "score").copy()

    # Shorten titles longer than 50 characters
    top_stories["short_title"] = top_stories["title"].apply(
        lambda title: title[:47] + "..."
        if len(str(title)) > 50
        else title
    )

    # Reverse the order so the highest score appears at the top
    top_stories = top_stories.sort_values("score")

    # Create a new figure when no dashboard axis is provided
    if ax is None:
        fig, ax = plt.subplots(figsize=(12, 7))
    else:
        fig = None

    ax.barh(
        top_stories["short_title"],
        top_stories["score"]
    )

    ax.set_title("Top 10 Stories by Score")
    ax.set_xlabel("Story Score")
    ax.set_ylabel("Story Title")

    if fig is not None:
        fig.tight_layout()
        fig.savefig("outputs/chart1_top_stories.png", dpi=300,
                    bbox_inches="tight")
        plt.close(fig)

        print("Chart 1 saved: outputs/chart1_top_stories.png")


# --------------------------------------------------
# 3. CHART 2 - STORIES PER CATEGORY
# --------------------------------------------------

def create_chart2(df, ax=None):

    # Count how many stories belong to each category
    category_counts = df["category"].value_counts()

    if ax is None:
        fig, ax = plt.subplots(figsize=(9, 6))
    else:
        fig = None

    # Each bar gets a different colour from Matplotlib's colour cycle
    ax.bar(
        category_counts.index,
        category_counts.values,
        color=plt.cm.tab10.colors[:len(category_counts)]
    )

    ax.set_title("Stories per Category")
    ax.set_xlabel("Category")
    ax.set_ylabel("Number of Stories")

    # Rotate category labels for better readability
    ax.tick_params(axis="x", rotation=30)

    if fig is not None:
        fig.tight_layout()
        fig.savefig("outputs/chart2_categories.png", dpi=300,
                    bbox_inches="tight")
        plt.close(fig)

        print("Chart 2 saved: outputs/chart2_categories.png")


# --------------------------------------------------
# 4. CHART 3 - SCORE VS COMMENTS
# --------------------------------------------------

def create_chart3(df, ax=None):

    if ax is None:
        fig, ax = plt.subplots(figsize=(9, 6))
    else:
        fig = None

    # Separate popular and non-popular stories
    popular = df[df["is_popular"] == True]
    not_popular = df[df["is_popular"] == False]

    # Plot non-popular stories
    ax.scatter(
        not_popular["score"],
        not_popular["num_comments"],
        label="Not Popular",
        alpha=0.7
    )

    # Plot popular stories
    ax.scatter(
        popular["score"],
        popular["num_comments"],
        label="Popular",
        alpha=0.7
    )

    ax.set_title("Score vs Comments")
    ax.set_xlabel("Story Score")
    ax.set_ylabel("Number of Comments")

    ax.legend()

    if fig is not None:
        fig.tight_layout()
        fig.savefig("outputs/chart3_scatter.png", dpi=300,
                    bbox_inches="tight")
        plt.close(fig)

        print("Chart 3 saved: outputs/chart3_scatter.png")


# --------------------------------------------------
# 5. CREATE COMBINED DASHBOARD
# --------------------------------------------------

def create_dashboard(df):

    # Create a dashboard with three chart areas
    fig, axes = plt.subplots(2, 2, figsize=(18, 12))

    # Place the three charts into the dashboard
    create_chart1(df, axes[0, 0])
    create_chart2(df, axes[0, 1])
    create_chart3(df, axes[1, 0])

    # Hide the unused fourth area
    axes[1, 1].axis("off")

    # Add the overall dashboard title
    fig.suptitle(
        "TrendPulse Dashboard",
        fontsize=20,
        fontweight="bold"
    )

    fig.tight_layout(rect=[0, 0, 1, 0.96])

    # Save dashboard before displaying it
    fig.savefig(
        "outputs/dashboard.png",
        dpi=300,
        bbox_inches="tight"
    )

    print("Dashboard saved: outputs/dashboard.png")

    return fig


# --------------------------------------------------
# 6. MAIN FUNCTION
# --------------------------------------------------

def main():

    print("=" * 50)
    print("TREND PULSE - DATA VISUALISATION")
    print("=" * 50)

    # Step 1: Load the analysed CSV
    df = load_data()

    if df is None:
        return

    # Step 2: Create individual charts
    create_chart1(df)
    create_chart2(df)
    create_chart3(df)

    # Step 3: Create combined dashboard
    dashboard = create_dashboard(df)

    print("\nAll visualisations created successfully!")
    print("Check the outputs folder for the PNG files.")

    # Display the dashboard after saving all PNG files
    plt.show()


# --------------------------------------------------
# 7. RUN THE PROGRAM
# --------------------------------------------------

if __name__ == "__main__":
    main()
