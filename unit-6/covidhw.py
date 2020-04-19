import requests
import json

class CovidStats ():

    def __init__ (self):
        self.covid_data = {}

    def fetch_statistics (self):

        url = "https://covid-193.p.rapidapi.com/statistics"
        headers = {
            'x-rapidapi-host': "covid-193.p.rapidapi.com",
            'x-rapidapi-key': "7d4ccbc25bmsh49d7ffce4bf360ap1abf2fjsn6e4b1323ce66"
            }
        self.covid_data = requests.request("GET", url, headers=headers).json()
        return self.covid_data ["response"]

    def top_ten (self):
        
        print (self.covid_data[])

    def get_country_stats (self,country):
        for item in self.covid_data:
            break
    
c = CovidStats()

print (c.top_ten())
