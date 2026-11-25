from pk_utils.iban import is_valid_iban

def test_valid():
    assert is_valid_iban("PK36SCBL0000001123456702")
    assert is_valid_iban("pk36 scbl 0000 0011 2345 6702")

def test_invalid():
    assert not is_valid_iban("PK37SCBL0000001123456702")  # wrong check digits
    assert not is_valid_iban("PK36SCBL000000112345670")   # too short
    assert not is_valid_iban("GB82WEST12345698765432")    # not Pakistan
