import requests
import json

class NhlTeams:
    def __init__(self):
        response = requests.get('https://statsapi.web.nhl.com/api/v1/teams').json()
        self.nhl_stats = response['teams']

    def get_team_names (self):
        i=0
        while i < len(self.nhl_stats): 
            for item in self.nhl_stats:
                print (item["name"])
            i+=1

    def show_teams (self):
        print (json.dumps(self.nhl_stats[0], indent =2))
    
    #def win_count (self):
    
    def get_oldest_team (self):
        sorted_list = sorted(self.nhl_stats, key=lambda k: k['firstYearOfPlay'])
        print (sorted_list[0]["name"])

        
        
t = NhlTeams()

#t.show_teams()
t.get_oldest_team()