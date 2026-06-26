import requests 
def getWeather():
    try:
        API_KEY = "ca018df54353f065aaed7d802825b8be"

        city = input("Enter city name : ")

        url = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid="+API_KEY+"&units=metric"

        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            print("CITY : ", data["name"])
            print("Temparature : ", data["main"]["temp"])
        else:
            print("API error", response.status_code)
    except Exception as e:
        print("Something went wrong")  # 1.no internet connection 2API server down 3invalid api 4JSON parse error
        print("Error", e)

getWeather()