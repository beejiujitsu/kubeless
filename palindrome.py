def palindrome(event, context):
    import re

    normalized = re.sub(r"\W+", "", event["data"].decode("utf-8")).lower()
    return str(normalized == normalized[::-1])
