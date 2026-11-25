from pk_utils.mobile import normalize_mobile, is_valid_mobile

def test_normalize():
    assert normalize_mobile("0300-1234567") == "03001234567"
    assert normalize_mobile("+92 300 1234567") == "03001234567"
    assert normalize_mobile("923001234567") == "03001234567"

def test_invalid():
    assert normalize_mobile("12345") is None
    assert not is_valid_mobile("0446-1234567")
