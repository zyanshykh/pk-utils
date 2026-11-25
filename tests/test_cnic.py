from pk_utils.cnic import is_valid_cnic

def test_valid():
    assert is_valid_cnic("42101-1234567-1")
    assert is_valid_cnic("4210112345671")

def test_invalid():
    assert not is_valid_cnic("123")
