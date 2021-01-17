import requests

from GetListsfromRequest import listmaker



def requester(time, lat, lon):

    key="e0b5c266d88db4937c26274e7b914494"

    link="https://api.openweathermap.org/data/2.5/onecall/timemachine?lat="+lat+"&lon="+lon+"&dt="+time+"&appid="+key


    response = requests.get(link)
    print("API Response:", response.status_code)


    pass_times = response.json()


    weather_value=listmaker.makelist(pass_times) #call the Listmaker to evaluate response data
    return(weather_value)

