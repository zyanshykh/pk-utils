# pk-utils 🇵🇰

Validation and helper utilities for Pakistan-specific data.

## Install
    pip install pk-utils   (coming soon)

## Usage
    from pk_utils.cnic import is_valid_cnic
    from pk_utils.mobile import normalize_mobile
    from pk_utils.iban import is_valid_iban
    from pk_utils.cities import get_cities

    is_valid_cnic("42101-1234567-1")      # True
    normalize_mobile("+92 300 1234567")   # "03001234567"

## Roadmap
- [x] CNIC validation
- [x] Mobile normalization
- [x] IBAN validation
- [x] City list
- [ ] NTN validation

## Contributing
Check the issues labeled `good first issue`. PRs welcome!
