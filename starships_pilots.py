import pymongo as pym
import requests as req

client = pym.MongoClient()
db = client['starwars']


def get_pilot(ship):
    response = req.get("https://swapi.dev/api/starships/" + str(ship))
    return response.json()["pilot"]


def get_name(pilot):
    response = req.get(str(pilot))
    return response.json()["name"]


starships = db.starships.find({}, {"_id": 0, "pilots": 1, "name": 1})

for starship in starships:
    ids = []
    flyers = starship['pilots']
    s_name = starship['name']
    if flyers:
        for flyer in flyers:
            name = get_name(flyer)
            names = db.characters.find_one({"name": name}, {"_id": 1})
            ids.append(names["_id"])
            print(ids)
        db.starships.update_one({"name": s_name}, {"$set": {"pilots": ids}})
    else:
        print(flyers)


