from View.view import View
from Model.model import Model
from json_handler import JSONHandler

class Controller:
    
    allPlayers = JSONHandler.get_players_obj()

    def generate_box_score():
        obj = Model.calculate_box_score(Controller.allPlayers)
        #View.dis_box_score()
        #playerBoxScore = Model.calculate_box_score_player(player)
        #player.team.Add(playerBoxScore)
        #player.team += playerBoxScore.GetTotalPoints()
