import json, requests
 
base_url =  "https://api.openweathermap.org/data/2.5/weather"
appid = "0a04a18985b95bbdd90429f6968d49f0"
city = input(f"Please type in your city:")
url = f"{base_url}?q={city}&units=imperial&APPID={appid}"
print(url)
print ()

response = requests.get(url)
unformatted_data = response.json()

print(unformatted_data)

#unformatted temp
temp = unformatted_data["main"]["temp"]
print(f"The current temp is: {temp}")

temp_max = unformatted_data["main"]["temp_max"]
print(f"The max temp is: {temp_max}")

if city != quit:
  
else:
  break
  print()
#need hel