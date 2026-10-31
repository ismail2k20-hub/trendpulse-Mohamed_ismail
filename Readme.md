# TrendPulse: What's Actually Trending Right Now

## Project Overview

TrendPulse is a Python-based data analysis project that collects, processes, analyses, and visualises trending stories from Hacker News.

The project uses the Hacker News API to collect story information, cleans and prepares the collected data, performs statistical analysis, and creates visualisations to identify trending topics and stories.

The project is divided into four tasks:

1. Data Collection
2. Data Processing
3. Data Analysis
4. Data Visualisation

## Objectives

- Collect trending stories using the Hacker News API.
- Categorise stories into different topics.
- Clean and prepare the collected data using Pandas.
- Perform statistical analysis using NumPy.
- Identify popular stories and engagement patterns.
- Create charts and a dashboard using Matplotlib.

## Technologies Used

- **Python** – Main programming language
- **Hacker News API** – Data source
- **Requests** – API communication
- **Pandas** – Data cleaning and processing
- **NumPy** – Statistical calculations
- **Matplotlib** – Data visualisation
- **JSON and CSV** – Data storage formats
- **Git and GitHub** – Version control and project submission

## Project Structure

```text
TrendPulse/
│
├── data/
│   ├── trends_YYYYMMDD.json
│   ├── trends_clean.csv
│   └── trends_analysed.csv
│
├── outputs/
│   ├── chart1_top_stories.png
│   ├── chart2_categories.png
│   ├── chart3_scatter.png
│   └── dashboard.png
│
├── task1_data_collection.py
├── task2_data_processing.py
├── task3_analysis.py
├── task4_visualization.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

*Note: `YYYYMMDD` represents the date on which the data was collected. The data and output files are generated when the corresponding scripts are executed.*

## Installation and Setup

### 1. Clone the Repository

```bash
git clone <your-github-repository-url>
```

Navigate to the project directory:

```bash
cd TrendPulse
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate the virtual environment in Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

If dependencies have not yet been added to `requirements.txt`, install them using:

```bash
python -m pip install requests pandas numpy matplotlib
```

## Tasks and Implementation

### Task 1 – Data Collection

**File:** `task1_data_collection.py`

**Objective:** Collect trending stories from the Hacker News API.

Implementation:

- Fetch the top story IDs from the Hacker News API.
- Retrieve individual story details using the API.
- Categorise stories into five categories:
  - Technology
  - World News
  - Sports
  - Science
  - Entertainment
- Collect a maximum of 25 stories per category.
- Include a two-second delay between category collection loops.
- Store the collected information in JSON format.

**Data fields collected:**

- `post_id`
- `title`
- `category`
- `score`
- `num_comments`
- `author`
- `collected_at`

**Output:** `data/trends_YYYYMMDD.json`

### Task 2 – Data Processing

**File:** `task2_data_processing.py`

**Objective:** Clean and prepare the collected story data for analysis.

Implementation:

- Load the latest JSON file using Pandas.
- Remove duplicate records based on `post_id`.
- Remove rows with missing essential values such as `post_id`, `title`, or `score`.
- Convert `score` and `num_comments` into integer data types.
- Remove stories with a score below 5.
- Remove unnecessary whitespace from story titles.
- Save the cleaned dataset as a CSV file.
- Display the number of records after cleaning and the category-wise story counts.

**Output:** `data/trends_clean.csv`

### Task 3 – Data Analysis

**File:** `task3_analysis.py`

**Objective:** Analyse the cleaned dataset to identify trends and engagement patterns.

Implementation:

- Load the cleaned CSV dataset.
- Display the first five records and dataset dimensions.
- Calculate the average story score and average number of comments.
- Calculate the following statistical measures for story scores using NumPy:
  - Mean
  - Median
  - Standard deviation
  - Maximum
  - Minimum
- Identify the category with the highest number of stories.
- Identify the story with the highest number of comments.
- Calculate an engagement metric:

  `engagement = num_comments / (score + 1)`

- Create an `is_popular` column to identify stories with scores above the average score.
- Save the analysed dataset as a CSV file.

**Output:** `data/trends_analysed.csv`

### Task 4 – Data Visualisation

**File:** `task4_visualization.py`

**Objective:** Create visualisations to understand trending stories, category distribution, and engagement.

Implementation:

**Chart 1 – Top 10 Stories by Score**

- Horizontal bar chart showing the top 10 stories based on score.
- Shortened long story titles for better readability.
- Displays story titles and scores.

**Output:** `outputs/chart1_top_stories.png`

**Chart 2 – Stories per Category**

- Bar chart showing the number of stories in each category.
- Uses different colours for each category.
- Displays category names and story counts.

**Output:** `outputs/chart2_categories.png`

**Chart 3 – Score vs Number of Comments**

- Scatter plot comparing story scores and number of comments.
- Uses different colours to distinguish popular and non-popular stories.
- Includes a legend to identify both groups.

**Output:** `outputs/chart3_scatter.png`

**Bonus – TrendPulse Dashboard**

- Combines all three visualisations into a single dashboard.
- Uses Matplotlib subplots.
- Includes the title "TrendPulse Dashboard".

**Output:** `outputs/dashboard.png`

All charts are saved using `plt.savefig()` before displaying them using `plt.show()`.

## How to Run the Project

Execute the Python scripts in the following order from the project root directory:

**Step 1 – Data Collection**

```bash
python task1_data_collection.py
```

**Step 2 – Data Processing**

```bash
python task2_data_processing.py
```

**Step 3 – Data Analysis**

```bash
python task3_analysis.py
```

**Step 4 – Data Visualisation**

```bash
python task4_visualization.py
```

Each task generates the output required by the next task. Therefore, run the scripts in the specified order.

## Final Outputs

| Task | Generated Output |
|---|---|
| Task 1 | Dated JSON file containing collected stories |
| Task 2 | `trends_clean.csv` |
| Task 3 | `trends_analysed.csv` |
| Task 4 | Three individual chart images and one dashboard |

## Key Learnings

Through this project, I gained practical experience in:

- Working with REST APIs and retrieving real-time data.
- Handling JSON and CSV datasets.
- Data cleaning and preprocessing using Pandas.
- Performing statistical analysis using NumPy.
- Creating data visualisations using Matplotlib.
- Organising a multi-step Python project.
- Using Git and GitHub for version control and project submission.

## Conclusion

TrendPulse demonstrates a complete data analytics workflow, starting from collecting data through an API to cleaning, analysing, and visualising the results.

The project helps transform raw trending-story data into meaningful insights about popular stories, category distribution, and user engagement.

---

**Project:** TrendPulse – What's Actually Trending Right Now  
**Language:** Python  
**Data Source:** Hacker News API