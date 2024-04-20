import json
import requests

def scrape(url):
    items = []
    while url:
        res = requests.get(url)
        if res.status_code == 200:
            print("Fetching results from ", url, "...")
            temp = res.json()
            items.extend(temp['results'])
            url = temp.get('next')
        else:
            print("Failed to fetch results from ", url, ".")
            break
    return items

def main():
    base_url = "https://www.infravelo.de/api/v1/projects"
    items = scrape(base_url)
    with open("infravelo-projects.json", "w") as f:
        json.dump(items, f, indent=2)
    return

if __name__ == "__main__":
    main()
