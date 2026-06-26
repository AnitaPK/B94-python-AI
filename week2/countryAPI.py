import requests


def fetchAPI():
    url = "https://countriesnow.space/api/v0.1/countries"
    try:
        print("--------")
        response = requests.get(url)
        if(response.status_code == 200):
            # print(response.status_code)
            res = response.json()

            # print(res["data"])
            listOfCountry = res["data"] 
            # print(listOfCountry[0])
            country = listOfCountry[0]
            print(country)
            citiesAFG = country["cities"]
            print(citiesAFG)
        else:
            print("API error", response.status_code)
    except Exception as e:
        print("Something went wrong")  # 1.no internet connection 2API server down 3invalid api 4JSON parse error
        print("Error", e)

fetchAPI()