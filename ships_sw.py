import pymongo as pym
import requests as req


def get_ship_data():
    try:
        response = req.get("https://swapi.dev/api/starships/?page=4")
        return response.json()['results']
    except req.exceptions.RequestException as e:
        print("Error getting starship data: ", e)

def insert_ship_data(starships):
    client = pym.MongoClient()
    db = client['starwars']
    collection = db['starships']

    collection.insert_many(starships)
    print("Starship data inserted.")

def main():
    starship_data = get_ship_data()
    insert_ship_data(starship_data)


main()

