from pk_utils.mobile import normalize_mobile, is_valid_mobile

def test_normalize():
    assert normalize_mobile("0346-3435119") == "03463435119"
    assert normalize_mobile("+92 346 3435119") == "03463435119"
    assert normalize_mobile("923463435119") == "03463435119"

def test_invalid():
    assert normalize_mobile("12345") is None
    assert not is_valid_mobile("0446-3435119")
