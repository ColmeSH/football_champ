class Team():

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "TEAM: {}".format(self.name)

    def __repr__(self):
        return self.__str__()