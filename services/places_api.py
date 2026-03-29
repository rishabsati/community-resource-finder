# Handles Google Places API requests for community resource searches
import os
import requests

API_KEY = os.getenv("GOOGLE_API_KEY")


def search_places(location, category):
    # Map UI category names to better Google search terms
    category_map = {
        "Food Banks": "food bank",
        "Shelters": "homeless shelter",
        "Free Clinics": "free clinic",
        "Mental Health Services": "mental health services",
        "Job Help": "employment center"
    }

    # Build the text search query
    query = f"{category_map.get(category, category)} in {location}"

    url = "https://maps.googleapis.com/maps/api/place/textsearch/json"

    params = {
        "query": query,
        "key": API_KEY
    }

    try:
        # Send request to Google Places API
        response = requests.get(url, params=params)
        data = response.json()

        results = []

        # Keep only the top 20 results and format them for the GUI
        for place in data.get("results", [])[:20]:
            name = place.get("name", "No name")
            address = place.get("formatted_address", "No address")

            results.append(f"{name} - {address}")

        return results

    except Exception as e:
        print("API Error:", e)
        return []