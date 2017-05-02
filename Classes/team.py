class TeamNotFound(Exception):
    
    def __init__(self):
        self.message = 'Team Not Found'


class Team(object):

    def __init__(self, name):
        self.name = name
        self.points = 0

    def __str__(self):
        return "TEAM: {}".format(self.name)

    def __repr__(self):
        return self.__str__()


class Tournament(object):
    
    teams = []
    
    def __init__(self, name):
        self.name = name

    def _generate_id(self):
        try:
            return self.teams[-1]['_id'] + 1
        except IndexError:
            return 1

    def add_team(self, team):
        self.teams.append({"_id": self._generate_id(),
                           "team": team})
        return self.teams[-1]

    def get_team(self, team_id):
        for index, team in enumerate(self.teams):
            if team['_id'] == team_id:
                return index, team
        raise TeamNotFound
