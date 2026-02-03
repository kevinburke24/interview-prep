records = [
    {"name": "Alice", "city": "Boston", "score": 92},
    {"name": "Bob", "city": "NYC", "score": 85},
    {"name": "Charlie", "city": "Boston", "score": 78},
]

# Generate a new dictionary that returns all the names
# associated with each city.

# I am going to loop through list, checking if the city
# already exists in the output dictionary that we are building.
# If the city already exists in our output dict, append name.
# If it doesn't, add a new city, list entry to the output
# dictionarty

def create_city_dict(records):
    out = {}
    for record in records:
        city = record["city"]
        if city in out:
            out[city].append(record["name"])
        else:
            out[city] = [ record["name"] ]
    return out

if __name__ == "__main__":
    out = create_city_dict(records)
    for k,v in out.items():
        print(k)
        print(v)