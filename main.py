import json,requests
covid=requests.get("https://api.covid19api.com/summary")
data=json.loads(covid.text)
print("worldwide")
latest=data['Global']
print(f"New Confirmed Cases:{latest['NewConfirmed']}")
print("New Deaths:"+str(latest['NewDeaths']))
print("New Recovered Cases:"+str(latest['NewRecovered']))
print("Total Confirmed Cases:"+str(latest['TotalConfirmed']))
print("Total Deaths:"+str(latest['TotalDeaths']))
print("Total Recovered Cases:"+str(latest['TotalRecovered']))
location=''
while location!='Q':
    print("Enter location:(press q to quit)")
    location=input()
    location=location[0:1].upper()+location[1:]
    l=data['Countries']
    country=[z for z in l if z['Country']==location]
    if len(country)==0:
        if location!='Q':
            print("invalid country!")
        continue
    else:
        country=country[0]
        print("New Confirmed Cases:"+str(country['NewConfirmed']))
        print("New Deaths:"+str(country['NewDeaths']))
        print("New Recovered Cases:"+str(country['NewRecovered']))
        print("Total Confirmed Cases:"+str(country['TotalConfirmed']))
        print("Total Deaths:"+str(country['TotalDeaths']))
        print("Total Recovered Cases:"+str(country['TotalRecovered']))
