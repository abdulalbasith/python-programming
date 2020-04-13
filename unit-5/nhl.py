import requests

class NhlTeams:
    def __init__(self):
        response = requests.get('https://statsapi.web.nhl.com/api/v1/teams').json()
        self.nhl_stats = response['teams']
    def get_team_names (self):
        i=0
        while i < len(self.nhl_stats): 
            for item in self.nhl_stats:
                return item["teamName"]
            i+=1

d=NhlTeams()
print(d.get_team_names())