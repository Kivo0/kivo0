import pathlib
import re
import os
import requests

root = pathlib.Path(__file__).parent.resolve()

if __name__ == "__main__":
    readme = root / "README.md"
    readme_contents = readme.open().read()
    
    url = "https://quotes15.p.rapidapi.com/quotes/random/"
    querystring = {"language_code":"en"}
    headers = {
        'x-rapidapi-host': "quotes15.p.rapidapi.com",
        'x-rapidapi-key': "8f79eb00b6msh6295f7072540bd7p1d294ajsn323ad8c01598"
    }
    res = requests.request("GET", url, headers=headers, params=querystring)
    data = res.json()
    #print(data['content'])
    readme.open("w").write("""This is inspirational qoutes that gets updated every 5 min.\"""+""" 
    """)
    readme.open("a").write(data['content']+"""  \"""+'by '+data['originator']['name'])
    
