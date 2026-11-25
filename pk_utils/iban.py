import re

def is_valid_iban(iban: str) -> bool:
    """Validate a Pakistani IBAN (PK + 2 digits + 4 letters + 16 digits)."""
    iban = re.sub(r"[\s\-]", "", iban).upper()
    if not re.fullmatch(r"PK\d{2}[A-Z]{4}\d{16}", iban):
        return False
    rearranged = iban[4:] + iban[:4]
    numeric = "".join(str(int(c, 36)) for c in rearranged)
    return int(numeric) % 97 == 1
