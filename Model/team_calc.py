class Team_calc():
    
    tOff = 0
    tDef = 0
        
    def team_off_mean(pOff):
        for k, v in pOff.items():
            Team_calc.tOff += v
    
    def team_def_mean(pDef):
        for k, v in pDef.items():
            Team_calc.tDef += v


def calc_team_means(team):
    print(len(team))
    for p in range(len(team)):
        Team_calc.team_off_mean(team[p][1])
        Team_calc.team_def_mean(team[p][2])
    print(Team_calc.tOff)
    print(Team_calc.tDef)
    #asd = Team_calc(team)
    #print(Team_calc.tOff)
    #print(Team_calc.tDef)
    #Team_calc.team_off_mean(team)
    #Team_calc.team_def_mean(team)
