from json import JSONEncoder
import json

# 112- convert the following dictionary into json format.

data = {"key1": "value1", "key2": "value2"}

print(json.dumps(data))

# 113- Access the value of key2 from the following json.

sample_json = """{"key1": "value1", "key2": "value2"}"""

data = json.loads(sample_json)
print(data["key2"])


# 114- sort json keys in and write them into a file.

sample_json = {"id": "1", "name": "value2", "age": 29}

with open("sample_jason.json", "w") as file:
    json.dump(sample_json, file, indent=4, sort_keys=True)


# 115- Access the nested key "salary" from the following json.

sample_json = """
    {
      "company":{
        "employee":{
           "name":"emma",
           "payble":{
              "salary":7000,
              "bonus":800
           }
        }
      }
    }
"""

data = json.loads(sample_json)
print(data["company"]["employee"]["payble"]["salary"])


# 116- convert the following vehicle object into json.

# from json import JSONEncoder
class Vehicle:
    def __init__(self, name, engine, price):
        self.name = name
        self.engine = engine
        self.price = price


class VehicleEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


vehicle = Vehicle("Toyota Rav4", "2.5L", 32000)

vehicle_json = json.dumps(vehicle, indent=4, cls=VehicleEncoder)
print(vehicle_json)


# 117- convert the following json into a vehicle object.

{"name": "Toyota Rav4", "engine": "2.5L", "price": 32000}


class Vehicle:
    def __init__(self, name, engine, price):
        self.name = name
        self.engine = engine
        self.price = price


def vehicle_decoder(obj):
    return Vehicle(obj["name"], obj["engine"], obj["price"])


vehicle = json.loads(
    '{"name": "Toyota Rav4", "engine": "2.5L", "price": 32000}', object_hook=vehicle_decoder)

print(vehicle.name, vehicle.engine, vehicle.price)


# 118- parse the following json to get all the values of a key "name" within an array.
[
    {
        "id": 1,
        "name": "name1",
        "color": [
            "red",
            "green"
        ]
    },
    {
        "id": 2,
        "name": "name2",
        "color": [
            "pink",
            "yellow"
        ]
    }
]


sample_json = """
[
    {
        "id": 1,
        "name": "name1",
        "color": [
            "red",
            "green"
        ]
    },
    {
        "id": 2,
        "name": "name2",
        "color": [
            "pink",
            "yellow"
        ]
    }
]
"""
data = []

try:
    data = json.loads(sample_json)
except Exception as ex:
    print(ex)

data_list = [item.get("name") for item in data]
print(data_list)
