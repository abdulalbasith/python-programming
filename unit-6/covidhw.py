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
        covid_data_response = requests.request("GET", url, headers=headers).json()
        self.covid_data = covid_data_response ["response"]

    def top_ten (self):
        cases_list = []
        for covid_cases in self.covid_data:
            
            cases_list.append(covid_cases["cases"])

            sorted_list = sorted(cases_list, key=lambda k:k['total'],reverse=True)

        return sorted_list [0:9]

    def get_country_stats (self,country):
        for item in self.covid_data:
            if item ["country"] == country:
                return item
            
    def test_unavailable (self):
        list_of_countries = []
        for items in self.covid_data:
            if type(items ["tests"]["total"]) != int:
                list_of_countries.append (items["country"])
        return list_of_countries

    def stats_to_file(self,filename):
        for items in self.covid_data:
            data_dump = {
                    "country":items["country"]
                    }

        with open (filename,"w") as dump_file:
            json.dumps(data_dump,dump_file)


c = CovidStats()
c.fetch_statistics()
#c.stats_to_file("test.json")
#print (c.top_ten())
#print (c.fetch_statistics())
#print (c.get_country_stats("Canada"))
print(c.test_unavailable())