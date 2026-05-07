import re

def mask_pii(text: str):
    # Mask Aadhaar (12 digits)
    text = re.sub(r'\b\d{4}\s?\d{4}\s?\d{4}\b', 'XXXX-XXXX-XXXX', text)

    # Mask phone numbers (10 digits)
    text = re.sub(r'\b\d{10}\b', 'XXXXXXXXXX', text)

    # Mask bank/account numbers (9-18 digits)
    text = re.sub(r'\b\d{9,18}\b', 'XXXXXXXXXXXX', text)

    return text