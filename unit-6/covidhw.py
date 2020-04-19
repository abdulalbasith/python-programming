import requests
import json

class CovidStats ():

    def __init__ (self):
        self.covid_data = []

    def fetch_statistics (self):

        url = "https://covid-193.p.rapidapi.com/statistics"
        headers = {
            'x-rapidapi-host': "covid-193.p.rapidapi.com",
            'x-rapidapi-key': "7d4ccbc25bmsh49d7ffce4bf360ap1abf2fjsn6e4b1323ce66"
            }
        self.covid_data = requests.request("GET", url, headers=headers).json()
        return self.covid_data ["response"]

    def top_ten (self):
        unsorted_data_list = []        
        for items in self.covid_data:
            for item in items:
                unsorted_data_list.append(item["cases"])
        return unsorted_data_list

    def get_country_stats (self,country):
        
        url = "https://covid-193.p.rapidapi.com/statistics"
        
        querystring = {"country":country}

        headers = {
            'x-rapidapi-host': "covid-193.p.rapidapi.com",
            'x-rapidapi-key': "7d4ccbc25bmsh49d7ffce4bf360ap1abf2fjsn6e4b1323ce66"
            }

        response = requests.request("GET", url, headers=headers, params=querystring).json()
        return response ["response"]
         
c = CovidStats()
print (c.top_ten())

# print (c.top_ten())

