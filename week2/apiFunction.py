import requests




def fetchAPI():
    url = "http://jsonplaceholder.typicode.com/users"

    try:
        response = requests.get(url)
        print(response.status_code)

        if response.status_code == 200:
            # print(response.text)
            print("----------------------")
            print(type(response.text))

            data = response.json()

            user = data[0]
            print(user)
            print("----------------")
            print("Name: ",user["name"])
            print("----------------")
            print("Email : ",user["email"])
            print("----------------")

            print(user["address"]["zipcode"])
            print("----------------")

            print(user["address"]["geo"]["lat"])
            print("----------------")
        else:
            print("API error", response.status_code)
    except Exception as e:
        print("Something went wrong")  # 1.no internet connection 2API server down 3invalid api 4JSON parse error
        print("Error", e)

fetchAPI()