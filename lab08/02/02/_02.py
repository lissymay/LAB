import requests
from bs4 import BeautifulSoup
import csv

url = "https://worldathletics.org"

def scrape_site(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup

def get_top_athlete_data(discipline, gender, year_start, year_end):
    results = []
    for year in range(year_start, year_end + 1):
        specific_url = f"{url}/records/toplists/{gender}/{discipline}/{year}"
        soup = scrape_site(specific_url)
        
        table = soup.find('table', {'class': 'records-table'})
        if table:
            rows = table.find_all('tr')
            for row in rows[1:2]:
                cols = row.find_all('td')
                if len(cols) > 5:
                    rank = cols[0].text.strip()
                    athlete_name = cols[1].text.strip()
                    dob = cols[2].text.strip()
                    country = cols[3].text.strip()
                    venue = cols[4].text.strip()
                    event_date = cols[5].text.strip()

                    if rank == '1':
                        results.append([year, athlete_name, country, venue, event_date, dob])
        else:
            print(f"Can not find {discipline}, {gender}, {year}")
            print(f"HTML content: {soup.prettify()}")
    
    return results

def main():
    disciplines = ["60m", "100m", "200m", "400m"]
    genders = ["men", "women"]
    year_start = 2001
    year_end = 2024

    all_results = []

    for discipline in disciplines:
        for gender in genders:
            results = get_top_athlete_data(discipline, gender, year_start, year_end)
            all_results.extend(results)

    with open('top_results.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Year", "Athlete Name", "Country", "Venue", "Event Date", "DOB"])
        writer.writerows(all_results)

if __name__ == "__main__":
    main()
