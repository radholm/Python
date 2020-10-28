from json_players import get_obj

class Model:
    
    plaP = 0
    
    boxScoreList = [] # [[team1boxscores], [team2boxscores]]
    
    team1 = []  # [[player1], [player2], ...]
    
    team2 = []  # [[player1], [player2], ...]

    def calculate_box_score(players):
        Model.create_team_profiles(players)
        
    def create_team_profiles(players): # [[vitals], [offense], [defense]]
        vitalsPlayer = players.players[Model.plaP]
        offensePlayer = players.players[Model.plaP].ratings[0].offense[0]
        defensePlayer = players.players[Model.plaP].ratings[1].defense[0]
        offAttr = Model.attr_val_list(offensePlayer)
        defAttr = Model.attr_val_list(defensePlayer)
        Model.team1.append([vitalsPlayer, offAttr, defAttr])

    def attr_val_list(self):
        kvlist = []
        items = self.__dict__.items()
        for k, v in items:
            kvlist.append({k, v})
        return kvlist
    
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
        
    
