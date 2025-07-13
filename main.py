import tempfile
import os
os.environ["TMPDIR"] = "/tmp"
tempfile.tempdir = "/tmp"

from scraper.reddit_api import get_user_data

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

    print(f"Fetching data for u/{username}...\n")

    try:
        content = get_user_data(username)

        if not content:
            print("No posts or comments found.")
            return

        print("✅ Data fetched successfully!\n")
        for item in content[:1000]:
            print(item)
            print("-" * 60)

    except Exception as e:
        print(f"❌ Error occurred: {str(e)}")

    print("🔚 Script completed")

if __name__ == "__main__":
    main()
