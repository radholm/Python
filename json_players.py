import json


class Players:

    def __init__(self, dict1):
        self.__dict__.update(dict1)
        
    def __repr__(self):
        return f'<Player { self.fullname }>'


def dict_obj(dict1):
    return json.loads(json.dumps(dict1), object_hook=Players)

def get_obj():
    with open('players.json') as json_file:
        players_dict = json.load(json_file)
        apb = dict_obj(players_dict)
        return apb
    