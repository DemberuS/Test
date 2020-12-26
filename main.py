import requests


def temp_and_pressure():
    url = "https://api.openweathermap.org/data/2.5/onecall?"
    params = {"lat": "55.7522", "lon": "37.6156", "exclude": "alerts,current,minutely,hourly",
              "appid": "46df3823e340ff9bc4ac32beb62c0d70", "units": "metric"}
    r = requests.get(url, params)
    text = r.json()
    a_temp, pressure = 0.0, 20000
    for i in range(5):
        new_pressure = int(text['daily'][i]['pressure'])
        if pressure > new_pressure:
            pressure = new_pressure
        temp = text['daily'][i]['feels_like']['eve']
        a_temp += float(temp)
    return f"Средняя вечерняя температура на предстоящие 5 дней = {int(a_temp / 5)}, а наименьшее давление = {pressure}"


print(temp_and_pressure())
