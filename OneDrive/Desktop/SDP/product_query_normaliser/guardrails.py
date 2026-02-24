import re


def extract_numeric_budget(text: str):
    """
    Extract numeric budget like:
    4000
    4k
    4 k
    4,000
    """

    text = text.lower()

    # Match 4k, 5k etc.
    match_k = re.search(r'(\d+)\s?k', text)
    if match_k:
        return int(match_k.group(1)) * 1000

    # Match 4000 or 4,000
    match_num = re.search(r'(\d{1,3}(?:,\d{3})+|\d+)', text)
    if match_num:
        value = match_num.group(1).replace(",", "")
        return int(value)

    return None


def validate_budget(budget: int):
    """
    Business rule:
    - Must be positive
    - Must be between 500 and 200000
    """

    if budget is None:
        return False, "Budget not found."

    if budget <= 0:
        return False, "Budget must be positive."

    if budget < 500:
        return False, "Budget too low for most products."

    if budget > 200000:
        return False, "Budget exceeds reasonable product range."

    return True, "Valid budget."