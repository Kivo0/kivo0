import pathlib
import re
import os
import requests

root = pathlib.Path(__file__).parent.resolve()

if __name__ == "__main__":
    readme = root / "README.md"
    readme_contents = readme.open().read()
    r = requests.get('https://quotes.rest/quote/random?language=en&limit=1')
    readme.open("w").write(r)
