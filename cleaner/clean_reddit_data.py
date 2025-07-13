import re

def clean_reddit_data(data):
    """
    Cleans and filters Reddit posts/comments by removing removed/deleted/empty ones,
    and optionally short or spammy-looking content.
    """
    cleaned = []

    for item in data:
        if item.get("type") == "post":
            title = item.get("title", "").strip()
            text = item.get("text", "").strip()
            if not title or text.lower() in ["[removed]", "[deleted]", ""]:
                continue
            if len(title) + len(text) < 20:
                continue
            item["title"] = remove_noise(title)
            item["text"] = remove_noise(text)
            cleaned.append(item)

        elif item.get("type") == "comment":
            body = item.get("body", "").strip()
            if body.lower() in ["[removed]", "[deleted]", ""] or len(body) < 20:
                continue
            item["body"] = remove_noise(body)
            cleaned.append(item)

    return cleaned

def remove_noise(text):
    """
    Removes URLs, markdown, and unnecessary symbols from text.
    """
    text = re.sub(r"http\S+", "", text)  # remove URLs
    text = re.sub(r"[\*_~>`]", "", text)  # remove markdown symbols
    text = re.sub(r"\s+", " ", text)  # normalize spaces
    return text.strip()
