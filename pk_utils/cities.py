CITIES = {
    "Sindh": ["Karachi", "Hyderabad", "Sukkur", "Larkana", "Mirpur Khas"],
    "Punjab": ["Lahore", "Faisalabad", "Rawalpindi", "Multan", "Gujranwala"],
    "Khyber Pakhtunkhwa": ["Peshawar", "Mardan", "Abbottabad", "Swat"],
    "Balochistan": ["Quetta", "Gwadar", "Turbat"],
    "Islamabad Capital Territory": ["Islamabad"],
}

def get_cities(province: str | None = None) -> list[str]:
    """Return cities of a province, or all cities if province is None."""
    if province is None:
        return [city for cities in CITIES.values() for city in cities]
    for name, cities in CITIES.items():
        if name.lower() == province.lower():
            return list(cities)
    return []

def is_pakistani_city(name: str) -> bool:
    return name.strip().lower() in {c.lower() for c in get_cities()}
