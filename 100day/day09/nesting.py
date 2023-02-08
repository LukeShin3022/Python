#Nesting
capitals = {
    "France": "Paris",
    "Germany":"Berlin"
}

#Nesting a List in a dictionary
travel_log = {
    "France": {"cities_visited":["Paris","Lille","Dijon"],"total_visits":12},
    "Germany":{"cities_visited":["Berlin","Hamburg","Stuttgart"],"total_visits":5}
}

print(travel_log['France']['total_visits'])


#Nesting Dictionary in a List
travel_log = [
    {
        "contry":"France",
        "cities_visited":["Paris","Lille","Dijon"],
        "total_visits":12
    },
    {
        "contry":"Germany",
        "cities_visited":["Berlin","Hamburg","Stuttgart"],
        "total_visits":5
    }
]

for travel in travel_log:
    print(travel['contry'])
    print(travel['cities_visited'])
    print(travel['cities_visited'][1])
    print(travel['total_visits'])