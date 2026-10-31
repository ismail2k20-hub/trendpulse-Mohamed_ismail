
"""
TrendPulse - Task 1: Fetch Data from API

Fetches Hacker News top stories, assigns categories,
and saves the collected stories to a JSON file.
"""

import requests
import json
import os
import time
from datetime import datetime

# --------------------------------------------------
# 1. API CONFIGURATION
# --------------------------------------------------

TOP_STORIES_URL = "https://hacker-news.firebaseio.com/v0/topstories.json"
ITEM_URL = "https://hacker-news.firebaseio.com/v0/item/{}.json"

HEADERS = {
    "User-Agent": "TrendPulse/1.0"
}

MAX_STORY_IDS =750
MAX_PER_CATEGORY = 25

# --------------------------------------------------
# 2. CATEGORY KEYWORDS
# --------------------------------------------------

CATEGORY_KEYWORDS = {
    "technology": [
        "AI", "software", "tech", "code", "computer",
        "data", "cloud", "API", "GPU", "LLM"
    ],

    "worldnews": [
        "war", "government", "country", "president",
        "election", "climate", "attack", "global"
    ],

    "sports": [
        "NFL", "NBA", "FIFA", "sport", "game",
        "team", "player", "league", "championship"
    ],

    "science": [
        "research", "study", "space", "physics",
        "biology", "discovery", "NASA", "genome"
    ],

    "entertainment": [
        "movie", "film", "music", "Netflix", "game",
        "book", "show", "award", "streaming"
    ]
}


# --------------------------------------------------
# 3. FUNCTION TO FETCH TOP STORY IDS
# --------------------------------------------------

def fetch_top_story_ids():

    print("Fetching top story IDs...")

    try:
        response = requests.get(
            TOP_STORIES_URL,
            headers=HEADERS,
            timeout=15
        )

        response.raise_for_status()

        story_ids = response.json()

        # Fetch only the first 500 IDs
        return story_ids[:MAX_STORY_IDS]

    except requests.RequestException as error:

        print("Error fetching story IDs:", error)

        return []


# --------------------------------------------------
# 4. FUNCTION TO FETCH ONE STORY
# --------------------------------------------------

def fetch_story(story_id):

    url = ITEM_URL.format(story_id)

    try:
        response = requests.get(
            url,
            headers=HEADERS,
            timeout=15
        )

        response.raise_for_status()

        story = response.json()

        # Skip deleted stories, missing stories,
        # and records without titles
        if not story or story.get("deleted") or story.get("dead"):
            return None

        if not story.get("title"):
            return None

        return story

    except requests.RequestException as error:

        print(f"Could not fetch story {story_id}: {error}")

        return None


# --------------------------------------------------
# 5. FUNCTION TO ASSIGN A CATEGORY
# --------------------------------------------------

def assign_category(title):

    title_lower = title.lower()

    for category, keywords in CATEGORY_KEYWORDS.items():

        for keyword in keywords:

            if keyword.lower() in title_lower:
                return category

    # Ignore stories that do not match any category
    return None


# --------------------------------------------------
# 6. FETCH STORY DETAILS
# --------------------------------------------------

def collect_story_details(story_ids):

    print("Fetching individual story details...")

    stories = []

    for index, story_id in enumerate(story_ids, start=1):

        story = fetch_story(story_id)

        if story is not None:

            stories.append(story)

        if index % 50 == 0:
            print(f"Processed {index}/{len(story_ids)} stories")

    return stories


# --------------------------------------------------
# 7. GROUP STORIES INTO CATEGORIES
# --------------------------------------------------

def group_stories_by_category(stories):

    collected_at = datetime.now().astimezone().isoformat(
        timespec="seconds"
    )

    category_results = {}

    for category in CATEGORY_KEYWORDS:

        print(f"Collecting category: {category}")

        category_stories = []

        for story in stories:

            assigned_category = assign_category(
                story.get("title", "")
            )

            if assigned_category == category:

                formatted_story = {
                    "post_id": story.get("id"),
                    "title": story.get("title"),
                    "category": category,
                    "score": story.get("score", 0),
                    "num_comments": story.get("descendants", 0),
                    "author": story.get("by", ""),
                    "collected_at": collected_at
                }

                category_stories.append(formatted_story)

                if len(category_stories) == MAX_PER_CATEGORY:
                    break

        category_results[category] = category_stories

        print(
            f"{category}: {len(category_stories)} stories collected"
        )

        # Wait 2 seconds between category loops,
        # not between individual story API requests.
        if category != list(CATEGORY_KEYWORDS.keys())[-1]:
            time.sleep(2)

    return category_results


# --------------------------------------------------
# 8. SAVE DATA TO JSON
# --------------------------------------------------

def save_to_json(category_results):

    os.makedirs("data", exist_ok=True)

    all_stories = []

    for category in category_results:

        all_stories.extend(category_results[category])

    filename_date = datetime.now().strftime("%Y%m%d")

    filename = f"data/trends_{filename_date}.json"

    try:

        with open(filename, "w", encoding="utf-8") as file:

            json.dump(
                all_stories,
                file,
                indent=4,
                ensure_ascii=False
            )

        print("\nData successfully saved!")
        print(f"Collected {len(all_stories)} stories.")
        print(f"Saved to {filename}")

    except OSError as error:

        print("Error saving JSON file:", error)


# --------------------------------------------------
# 9. MAIN FUNCTION
# --------------------------------------------------

def main():

    print("=" * 50)
    print("TREND PULSE - DATA COLLECTION")
    print("=" * 50)

    # Step 1: Get top 500 story IDs
    story_ids = fetch_top_story_ids()

    if not story_ids:
        print("No story IDs received. Stopping program.")
        return

    print(f"Received {len(story_ids)} story IDs.")

    # Step 2: Fetch story details
    stories = collect_story_details(story_ids)

    print(f"Successfully fetched {len(stories)} story details.")

    # Step 3: Categorise stories
    category_results = group_stories_by_category(stories)

    # Step 4: Save JSON
    save_to_json(category_results)

    print("\nTask 1 completed!")


# --------------------------------------------------
# 10. RUN PROGRAM
# --------------------------------------------------

if __name__ == "__main__":
    main()
