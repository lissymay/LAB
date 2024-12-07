import requests
import json

response = requests.get('https://restcountries.com/v3.1/region/Asia')
countries = response.json()

filtered_countries = [country for country in countries if country['population'] > 30000000]

result = []
for country in filtered_countries:
    country_data = {
        'name': country['name']['common'],
        'capital': country['capital'][0] if country.get('capital') else 'No capital',
        'area': country['area'],
        'population': country['population'],
        'flag_url': country['flags']['png']
    }
    result.append(country_data)

with open('results.json', 'w') as file:
    json.dump(result, file, indent=4)

for country in result:
    country['population_density'] = country['population'] / country['area']

sorted_countries = sorted(result, key=lambda x: x['population_density'], reverse=True)
top_5_countries = sorted_countries[:5]

print("Top 5 countries by population density:")
for country in top_5_countries:
    print(country['name'])

for country in top_5_countries:
    flag_url = country['flag_url']
    flag_response = requests.get(flag_url)
    with open(f"{country['name']}.png", 'wb') as file:
        file.write(flag_response.content)
