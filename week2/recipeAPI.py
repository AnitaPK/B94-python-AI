import requests

response = requests.get("https://dummyjson.com/recipes")

print(response.status_code)

data = response.json()

listOfRecipe = data["recipes"]

for rec in listOfRecipe:
    recName = rec["name"]
    print(recName)