# from django.contrib.auth import logout as logouts
# from django.http import HttpResponse
#
# from .models import BooksModel
# from .models import Datastore
# from .models import Question
# from .models import Quiz
# from .models import Simplebook
# from .models import Textbook
import datetime as dt
import json

import requests
from django.db.models import Max
from django.shortcuts import render

from .models import Weather  # this is model which is used to save the data


def weather(request):
    # print("Weather")
    city = ""
    jsondata = ""
    data = ""
    save = ""
    now = ""
    now1 = ""
    temp = ""
    feel = ""
    country = ""
    weather = ""
    wind = ""
    time = ""
    diff = 10 ** 9
    if request.GET:
        city = request.GET["city"]
        opt = request.GET["option"]
        now = (dt.datetime.now())
        time1 = int(now.strftime("%y%m%d%H%M%S"))
        print(time1)
        time2 = (Weather.objects.aggregate(Max('time')))
        # time2 = Weather.objects.raw('SELECT time FROM weather WHERE id = (SELECT MAX(id) FROM weather)')

        time2 = int(time2['time__max'])
        print(time2)
        t = (time1 - time2)
        print(t)

        if opt == "save":
            diff = request.GET["diff"]
            city = request.GET["city"]
            temp = request.GET["tem"]
            feel = request.GET["feel"]
            country = request.GET["country"]
            weather = request.GET["weather"]
            wind = request.GET["wind"]
            time = request.GET["time"]
            # print(time)
            if int(diff) == 0 or int(diff) < 10000:
                value = Weather(city=city, tempreture=temp, feel=feel, country=country, weather=weather,
                                wind_speed=wind,
                                time=time)
                value.save()
            else:
                Weather.objects.filter(city=city).update(tempreture=temp, feel=feel, country=country, weather=weather,
                                                         wind_speed=wind,
                                                         time=time)

            # print("Saved")   # this is for testing perpose just to chech that data are saving or not
        else:
            d = Weather.objects.filter(city=city)
            if len(d) == 0:
                print("Weather")
                # print(dt.datetime.fromtimestamp(1624491535))
                now = (dt.datetime.now())
                print(now.strftime("%y%m%d%H%M%S"))
                now1 = (now.strftime("%y%m%d%H%M%S"))
                appid = "36a7c5ba449a153d278a8cbab4152450"
                # city = "varanasi"
                params = {'appid': appid, "q": city, "units": "metric"}
                url = "https://api.openweathermap.org/data/2.5/weather?q={1}&appid={0}&units=metric".format(appid, city)
                # url = "https://api.openweathermap.org/data/2.5/forecast?lat=25.3333&lon=83&appid=4a1f8a61b74546825af1e0be106e797b
                # &units=metric"
                # print("Calling")
                response = requests.get(url, params)
                code = response.status_code
                # print(code)
                # 200 means success
                # Status code 404 not found
                # Sttus code 401 is not authorized
                # print(response.text)
                if code != 200:
                    print("Error")
                else:
                    jsondata = json.loads(response.text)
                    # print(jsondata)
                    # print(jsondata["main"]["temp"])
                    data = jsondata["main"]["temp"]
                    # print(jsondata["weather"][0]["description"])

                    temp = jsondata["main"]["temp"]
                    feel = jsondata["main"]["feels_like"]
                    country = jsondata["sys"]["country"]
                    weather = jsondata["weather"][0]["description"]
                    wind = jsondata["wind"]["speed"]
                    time = now1
            else:
                w = d[0]
                t = int(w.time)
                time1 = int(now.strftime("%y%m%d%H%M%S"))
                diff = time1 - t;
                if diff < 10000:
                    temp = w.temperature
                    feel = w.feel
                    country = w.country
                    weather = w.weather
                    wind = w.wind_speed
                    time = now1
                else:
                    print("Weather")
                    # print(dt.datetime.fromtimestamp(1624491535))
                    now = (dt.datetime.now())
                    print(now.strftime("%y%m%d%H%M%S"))
                    now1 = (now.strftime("%y%m%d%H%M%S"))
                    appid = "36a7c5ba449a153d278a8cbab4152450"
                    # city = "varanasi"
                    params = {'appid': appid, "q": city, "units": "metric"}
                    url = "https://api.openweathermap.org/data/2.5/weather?q={1}&appid={0}&units=metric".format(appid,
                                                                                                                city)
                    # url = "https://api.openweathermap.org/data/2.5/forecast?lat=25.3333&lon=83&appid=4a1f8a61b74546825af1e0be106e797b
                    # &units=metric"
                    # print("Calling")
                    response = requests.get(url, params)
                    code = response.status_code
                    # print(code)
                    # 200 means success
                    # Status code 404 not found
                    # Sttus code 401 is not authorized
                    # print(response.text)
                    if code != 200:
                        print("Error")
                    else:
                        jsondata = json.loads(response.text)
                        # print(jsondata)
                        # print(jsondata["main"]["temp"])
                        data = jsondata["main"]["temp"]
                        # print(jsondata["weather"][0]["description"])
                        temp = jsondata["main"]["temp"]
                        feel = jsondata["main"]["feels_like"]
                        country = jsondata["sys"]["country"]
                        weather = jsondata["weather"][0]["description"]
                        wind = jsondata["wind"]["speed"]
                        time = now1

    return render(request, "weather.html",
                  {'time_diff': diff, 'city': city, "feel": feel, 'temp': temp, "country": country, "weather": weather,
                   "wind": wind, 'time': time})


# def time(request):
#     now = (dt.datetime.now())
#     time1 = int(now.strftime("%y%m%d%H%M%S"))
#     print(time1)
#     time2 = (Weather.objects.filter(city="bhagalpur"))
#     # time2 = Weather.objects.raw('SELECT time FROM weather WHERE id = (SELECT MAX(id) FROM weather)')
#
#     # if (len(time2) == 0):
#
#     # # time2 = int(time2['time__max'])
#     # # print(time2)
#     # # t = time1 - time2
#     # # print(t)
#     # if t >= 3000:
#     #     Weather.objects.filter(city="varanasi").update(tempreture=2, feel=50)
#     return render(request, "weather.html")
