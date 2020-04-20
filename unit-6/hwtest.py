import requests

url = "https://covid-193.p.rapidapi.com/statistics"
headers = {
    'x-rapidapi-host': "covid-193.p.rapidapi.com",
    'x-rapidapi-key': "7d4ccbc25bmsh49d7ffce4bf360ap1abf2fjsn6e4b1323ce66"
    }
covid_data_response = requests.request("GET", url, headers=headers).json()
covid_data = covid_data_response["response"]

for items in covid_data:
    print (items ["tests"]["total"])