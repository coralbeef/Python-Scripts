#!/usr/bin/python3

import requests
import json

r=requests.get("https://api.fixer.io/latest?base=USD&symbols=NOK")
resp=json.loads(r.text)
print (resp["base"], resp["rates"]["NOK"])


