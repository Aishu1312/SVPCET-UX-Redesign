import json
from datetime import datetime

def format_notice_date(date_value):
    """
    Safely formats notice dates without crashing when the input format varies.
    Returns a dictionary with 'day' and 'month'.
    """
    if not date_value:
        return {"day": "", "month": ""}

    date_text = str(date_value).strip()

    formats = [
        "%Y-%m-%d",
        "%d %B %Y",
        "%d %b %Y",
        "%d-%m-%Y",
        "%d/%m/%Y",
        "%Y/%m/%d",
    ]

    for fmt in formats:
        try:
            parsed = datetime.strptime(date_text, fmt)
            return {
                "day": parsed.strftime("%d"),
                "month": parsed.strftime("%b")
            }
        except ValueError:
            continue

    # Safe fallback if format is unrecognized
    # We attempt to extract something that looks like a day/month, or just return the text
    parts = date_text.split()
    if len(parts) >= 2:
        return {
            "day": parts[0][:2],
            "month": parts[1][:3].upper()
        }
    
    return {
        "day": date_text[:2],
        "month": ""
    }

def safe_get_data(filepath="data/mock_data.json"):
    """
    Safely loads JSON data with a fallback empty structure to prevent app crashes.
    """
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data
    except (FileNotFoundError, json.JSONDecodeError):
        return {
            "programs": [],
            "notices": [],
            "placements": {
                "highest_package": "N/A",
                "average_package": "N/A",
                "top_recruiters": [],
                "placement_percentage": "N/A"
            },
            "stats": {
                "students": "N/A",
                "faculty": "N/A",
                "alumni": "N/A",
                "acres_campus": "N/A"
            }
        }
