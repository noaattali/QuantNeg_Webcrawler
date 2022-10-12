import tqdm
import pandas as pd
import csv
import requests
from bs4 import BeautifulSoup


story_links= []
story_name = []
match_case = []
context = []


hub_url = "https://www.npr.org/programs/all-things-considered/archive?date=12-31-2021"
page = requests.get(hub_url)
soup = BeautifulSoup(page.content, "html.parser")

def grab_day_links():#month_link: str):
    test = "https://www.npr.org//programs/all-things-considered/archive?date=12-31-2021"
    page = requests.get(test)
    month = BeautifulSoup(page.content, "html.parser")
    day_segments = month.find(id="episode-list")
    for segment in day_segments:
        print(segment.next_sibling)



def search_months(year_list: list):
    main_link = "https://www.npr.org/"
    for year in year_list[:12]: #Ends at 2010
        for link in year.find_all('li'):
            grab_day_links(main_link + link.a.get("href"))

        "We put link.a to get the descendent of <li>"

def crawl_NPR_archives():
    archive_container = soup.find("nav", {"class": "archive-nav"})
    years = archive_container.find_all("div")[1:] #Remove year 2022 as it has no handwritten transcripts
    # search_months(years)
    grab_day_links()

def write_csv_file():
    pass



if __name__ == "__main__":
    crawl_NPR_archives()