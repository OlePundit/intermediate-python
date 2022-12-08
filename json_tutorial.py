import json


person ={"name":"John", "age":30, "city":"New York","hasChildren": False, "titles":["engineer","programmer"]}


personJson = json.dumps(person, indent=4, sort_keys=True)
print(personJson)

#with open('person.json', 'w') as file:
 #   json.dump(person, file, indent=4)


with open('person.json', 'r') as file:
    person = json.loads(personJson)
    print(person)

class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age

user = User('Max', 27)

def encode_user(o):
    if isinstance(o, User):
        return {'name': o.name, 'age': o.age, o.__class__.__name__: True}

    else:
        raise TypeError('object of type user is not JSON serializable')


#userJSON = json.dumps(user, default=encode_user)
#print(userJSON)


from json import JSONEncoder
class UserEncoder(JSONEncoder):

    def default(self, o):
        if isinstance(o, User):
            return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
        return JSONEncoder.defaut(self, o)


#userJSON = json.dumps(user, cls=UserEncoder)
userJSON = UserEncoder().encode(user)
print(userJSON)

def decode_user(dct):
    if User.__name__ in dct:
        return User(name=dct['name'], age=dct['age']) #How to decode objects e.g dict
    return dct


user =json.loads(userJSON, object_hook=decode_user)
print(user)
print(user.name)