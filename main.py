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

def search_months(year_list: list):
    # for year in year_list:
    #     for month in year:
    #         pass
    for i in range(len(year_list[0])):
        print(year_list[0][i])

def crawl_NPR_archives():
    archive_container = soup.find("nav", {"class": "archive-nav"})
    years = archive_container.find_all("div")[1:] #Remove year 2022 as it has no handwritten transcripts
    search_months(years)
    print(years)

def write_csv_file():
    pass



if __name__ == "__main__":
    crawl_NPR_archives()