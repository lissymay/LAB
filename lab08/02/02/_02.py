import requests
from bs4 import BeautifulSoup
import csv

def fetch_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None

def parse_page(html):
    soup = BeautifulSoup(html, 'html.parser')
    results = []
    for row in soup.select('tbody tr'):
        cells = row.find_all('td')
        if len(cells) >= 5:
            year = cells[0].text.strip()
            athlete_name = cells[1].text.strip()
            country = cells[2].text.strip()
            time = cells[3].text.strip()
            date = cells[4].text.strip()
            results.append([year, athlete_name, country, time, date])
    return results

def scrape_data(discipline, gender):
    base_url = 'https://worldathletics.org/records/toplists/sprints/'
    results = []
    for year in range(2001, 2025):
        url = f"{base_url}{discipline}/outdoor/{gender}/senior/{year}"
        html = fetch_url(url)
        if html:
            results += parse_page(html)
    return results

if __name__ == '__main__':
    disciplines = ['100-metres', '200-metres', '400-metres']
    genders = ['men', 'women']
    all_results = []

    for discipline in disciplines:
        for gender in genders:
            results = scrape_data(discipline, gender)
            all_results += results

    with open('top_results.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Year', 'Athlete Name', 'Country', 'Time', 'Date'])
        writer.writerows(all_results)
