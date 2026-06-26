import requests

url = "https://randomuser.me/api/?results=20&nat=in"

responce = requests.get(url)

print(responce.status_code)

data = responce.json()
# print(data)

listOfUser = data["results"]
# print(listOfUser)

# print(listOfUser[0])

# print(listOfUser[0]["name"])
name = listOfUser[0]["name"]["title"] + " " + listOfUser[0]["name"]["first"] + " " +listOfUser[0]["name"]["last"]
print(name)

for user in listOfUser:
    name = user["name"]["title"] + " " + user["name"]["first"] + " " +user["name"]["last"]
    print(name)

