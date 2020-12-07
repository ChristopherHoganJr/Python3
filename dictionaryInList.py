travel_log = [
    {
        'country':'france', 
        'cities_visited': ['paris','lille','dijon'], 
        'total_visits': 12},
    {
        'country':'germany', 
        'cities_visited': ['berlin','hamburg','stuttgart'], 
        'total_visits': 5
        }
]

def add_new_country(country_visited, times_visited, cities_visited):
    new_country = {}
    new_country['country'] = country_visited
    new_country['cities_visited'] = cities_visited
    new_country['total_visits'] = times_visited
    travel_log.append(new_country)
    print(travel_log)




add_new_country('russia', ['moscow','saint petersburg'], 2)

print(travel_log)
