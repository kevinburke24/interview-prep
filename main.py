import csv
def read_stream_from_csv(path):
    with open(path, "") as f:
        reader = csv.DictReader(f)
        for row in reader:
            yield row

def group_cities_from_records(records):
    cities = {}
    for record in records:
        city = record["city"]
        name = record["name"]
        if city is None or name is None:
            continue

        if city not in cities:
            cities[city] = []
        cities[city].append(name)
    for city in cities:
        cities[city].sort()
    return cities

if __name__ == "__main__":
    records = [ { "name" : "Theodore", "city" : "Boston", "score" : 4 }, {"name" : "Kevin", "city" : "NYC", "score" : 5}, {"name" : "Al", "city" : "NYC", "score" : 5} ]
    print(group_cities_from_records(records))