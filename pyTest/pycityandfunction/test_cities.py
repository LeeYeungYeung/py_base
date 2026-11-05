from city_and_country import get_city_and_country

def test_get_city_country_population():
    city_and_country = get_city_and_country('Shanghai', 'China',2000000)
    assert city_and_country == 'Shanghai, China, Population: 2000000'

def test_get_city_country():
    city_and_country = get_city_and_country('Shanghai', 'China')
    assert city_and_country == 'Shanghai, China'