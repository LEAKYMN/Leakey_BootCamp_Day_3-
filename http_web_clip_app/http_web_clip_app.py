import pyowm

owm = pyowm.OWM('44ab67a5aca5f101a7eef4aa2569c453')  
observation = owm.weather_at_place("Cambridge,uk")  
w = observation.get_weather()  
temperature = w.get_temperature('celsius')  
tomorrow = pyowm.timeutils.tomorrow()  
wind = w.get_wind()  
print(w)  
print(wind)  
print(temperature)  
print(tomorrow)  