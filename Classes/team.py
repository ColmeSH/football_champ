import json
class Team(json.JSONEncoder):

    def __init__(self, name):
        self.name = name
        self.points = 0
        self.teamid = 0

    def jdefault(self, o):
        if isinstance(o, set):
            return list(o)
        return o.__dict__

    # def __str__(self):
    #     return "TEAM: {}".format(self.name)
    #
    # def __repr__(self):
    #     return self.__str__()
