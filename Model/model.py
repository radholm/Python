from json_players import get_obj
from Model.team_calc import calc_team_means

class Model:
    
    boxScoreList = [] # [[team1boxscores], [team2boxscores]]
    
    team1 = []  # [[player1], [player2], ...]
    
    team2 = []  # [[player1], [player2], ...]

    def calculate_box_score(players):
        Model.create_team_profiles(players)
        Model.calculate_team_means(Model.team1, Model.team2)
        
    def create_team_profiles(players): # [[player], [offense], [defense]], bug if teams unequal?
        plaP = 0
        for p in range(len(players.players)): # p is never used
            vitalsPlayer = players.players[plaP]
            if vitalsPlayer.team == 'LAL': # If multiple teams, change this
                Model.team1.append([vitalsPlayer])
                plaP += 1
            else:
                Model.team2.append([vitalsPlayer])
                plaP += 1
                
    def calculate_team_means(team1, team2):
        teams = [team1, team2]
        calc_team_means(team1)
        #for t in range(len(teams)):
        #    for pt in range(len(teams[t])):
        #        for ptr in range(len(teams[t][pt])):
        #           print((teams[t][pt][ptr]))
    
#class PlayerBoxScore(object):
   # name = None
   # fgm, fga, fgp, tpm, tpa, tpp, trb, ast, pts = 0
    
  #  def __init__(self, name, fgm, fga, tpm, tpa, ast):
  #      self.name = name
  #      self.fgm = fgm
  #      self.fga = fga
  #      self.fgp = ""(fgm/fga)*100 + " %"
  #      self.tpm = tpm
  #      self.tpa = tpa
  #      self.tpp = ""(tpm/tpa)*100 + " %"
  #     self.ast = ast
        
  #  def __repr__(self):
  #      pass
        
    
