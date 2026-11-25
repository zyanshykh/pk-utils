from pk_utils.cities import get_cities, is_pakistani_city

def test_get_cities():
    assert "Karachi" in get_cities("sindh")
    assert get_cities("Unknown") == []
    assert len(get_cities()) > 10

def test_is_pakistani_city():
    assert is_pakistani_city(" lahore ")
    assert not is_pakistani_city("Paris")
