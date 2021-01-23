from Console import UI
import requests

if __name__ == '__main__':


    koords = UI.TinkerUI()  # Get Koordinates over UI
    lat = koords[0]
    lon = koords[1]
    lat = str(lat)  # make strings for API call
    lon = str(lon)

    link = "http://127.0.0.1:5000/snow?lat="+lat+"&lon="+lon #call of the internal API in Main with Koordinates
    response = requests.get(link)
    print(response) #response code'
    x = response.json()
    print(x) #Print response
