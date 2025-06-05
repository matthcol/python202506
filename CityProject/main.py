from city import City, CityWithAirport

# build objects with City constructor
cities: list[object] = [
    City("Toulouse"),
    City(name="Revel"),
    City("St-Orens-de Gameville", population=13_766, zipcode="31650"),
    City("Pau", zipcode="64000"),
    City("Ajaccio", zipcode="20000"),
    City("Bastia", zipcode="20200"),
    City("Basse Terre", zipcode="97100"),
]

cities.append(1)

for data in cities:
    print(data) # eq: print(str(city))
    print(repr(data))
    print("\t- type:", type(data))
    if isinstance(data, City):
        print("\t- name:", data.name)
        print("\t- population:", data.population)
        print("\t- zipcode:", data.zipcode)
        print("\t- department:", data.department())

cityw = CityWithAirport("Biarritz", airport="LFBZ")
assert isinstance(cityw, CityWithAirport)
assert isinstance(cityw, City)
assert isinstance(cityw, object)

city = City("Bayonne")
assert not isinstance(city, CityWithAirport)
assert isinstance(city, City)
assert isinstance(city, object)

cityw2 = CityWithAirport.from_city_and_airport(city, "LFBY")
print(repr(cityw2))
