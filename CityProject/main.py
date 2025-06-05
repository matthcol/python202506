from city import City

# build objects with City constructor
city1 = City("Toulouse")
city2 = City(name="Revel")
city3 = City("St-Orens-de Gameville", population=13_766, zipcode="31650")
city4 = City("Pau", zipcode="64000")
city5 = City("Ajaccio", zipcode="20000")
city6 = City("Bastia", zipcode="20200")
city7 = City("Basse Terre", zipcode="97100")


for city in city1, city2, city3, city4, city5, city6, city7:
    print(city) # eq: print(str(city))
    print(repr(city))
    print("\t- type:", type(city))
    print("\t- name:", city.name)
    print("\t- population:", city.population)
    print("\t- zipcode:", city.zipcode)
    print("\t- department:", city.department())