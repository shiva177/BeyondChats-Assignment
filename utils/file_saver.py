import os

def save_to_file(username: str, cleaned_data: list):
    """
    Saves cleaned Reddit data to a text file under output/{username}_cleaned.txt
    """
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    filepath = os.path.join(output_dir, f"{username}_cleaned.txt")
    with open(filepath, "w", encoding="utf-8") as f:
        for item in cleaned_data:
            if item["type"] == "post":
                f.write(f"[POST]\nTitle: {item['title']}\nText: {item['text']}\nSubreddit: {item['subreddit']}\nURL: {item['url']}\n\n")
            elif item["type"] == "comment":
                f.write(f"[COMMENT]\nText: {item['body']}\nSubreddit: {item['subreddit']}\nURL: {item['url']}\n\n")
    
    print(f"\n💾 Saved cleaned data to: {filepath}")
