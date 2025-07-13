import tempfile
import os

os.environ["TMPDIR"] = "/tmp"
tempfile.tempdir = "/tmp"

from scraper.reddit_api import get_user_data
from cleaner.clean_reddit_data import clean_reddit_data
from utils.file_saver import save_to_file  # ✅ Importing new utility

def extract_username_from_url(url: str) -> str:
    parts = url.strip("/").split("/")
    if "user" in parts:
        index = parts.index("user")
        return parts[index + 1] if index + 1 < len(parts) else None
    return None

def main():
    print("Reddit Profile Scraper")
    profile_url = input("Enter Reddit profile URL: ").strip()

    username = extract_username_from_url(profile_url)
    print("🔥 Reached username extraction block")
    print(f"👤 Username detected: {username}")

    if not username:
        print("❌ Invalid Reddit profile URL.")
        return

    print(f"📥 Fetching data for u/{username}...\n")

    try:
        content = get_user_data(username)
        print("✅ Raw data fetched successfully!\n")

        print(f"📊 Total items before cleaning: {len(content)}")

        cleaned = clean_reddit_data(content)
        print(f"🧽 Total items after cleaning: {len(cleaned)}\n")

        print("🔎 Cleaned Content Preview (Top 5):\n")
        for item in cleaned[:5]:
            print(item)
            print("-" * 60)

        save_to_file(username, cleaned)  # ✅ Save to text file

    except Exception as e:
        print(f"❌ Error occurred: {str(e)}")

    print("\n🔚 Script completed")

if __name__ == "__main__":
    main()
