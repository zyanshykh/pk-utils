import re

def normalize_mobile(number: str) -> str | None:
    """Return mobile in 03XXXXXXXXX format, or None if invalid."""
    digits = re.sub(r"[\s\-()]", "", number)
    if digits.startswith("+92"):
        digits = "0" + digits[3:]
    elif digits.startswith("0092"):
        digits = "0" + digits[4:]
    elif digits.startswith("92"):
        digits = "0" + digits[2:]
    if re.fullmatch(r"03\d{9}", digits):
        return digits
    return None

def is_valid_mobile(number: str) -> bool:
    return normalize_mobile(number) is not None
