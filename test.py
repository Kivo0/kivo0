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
    readme.open("w").write('# Bonjour:exclamation: :fr: :soccer:'+'\n')
    readme.open("a").write('``` diff'+' \\'+'\n''-!A NeW inspirational quote every day!- '+'\n'+'```'+'\n')
    readme.open("a").write(data['content']+' \\'+'\n'+'by '+data['originator']['name'])
    
