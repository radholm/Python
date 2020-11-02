from typing import OrderedDict
from collections import Counter

class Team_calc():
    
    sumDict = OrderedDict()
    sumVal = 0
    kvDict = OrderedDict()

    def attr_val_list(self):
        """This breaks the object and returns a dict"""
        items = self.__dict__.items()
        for k, v in items:
            Team_calc.kvDict[k] = v
            Team_calc.sumDict.update({k, v})

    def team_mean(player):
        asd = Team_calc.attr_val_list(player[0].ratings[0].offense[0])
        #data = dict(zip(list_with_keys, list_with_values))
        print(Team_calc.kvDict)
        print(Team_calc.sumVal)


def calc_team_means(team):
    for p in range(len(team)):
        #sum((Counter(dict(x)) for x in input), Counter())
        Team_calc.team_mean(team[p])
