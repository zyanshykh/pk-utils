import re

def is_valid_cnic(cnic: str) -> bool:
    """13 digits, with or without dashes: 42101-1234567-1"""
    return bool(re.fullmatch(r"\d{5}-?\d{7}-?\d", cnic.strip()))
