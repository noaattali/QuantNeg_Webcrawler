import tqdm
import requests
from bs4 import BeautifulSoup
import QuaNISC
import NPR_webscraper

clauses = 0


hub_url = "https://www.npr.org/programs/all-things-considered/archive?date=12-31-2021"
page = requests.get(hub_url)
soup = BeautifulSoup(page.content, "html.parser")

def validate_quant_neg(article_link: str):
    page = requests.get(article_link)
    soup = BeautifulSoup(article_link)
    sentences = extract_transcript(soup)
    if QuaNISC.is_quantifier_negation(sentences):
        identifications, indices = QuaNISC.find_quantifer_negation(sentences)
        context = get_context(sentences, indices)
        #grab audiofile
        title, speakers, date = extract_metadata(soup)
        clauses += clause_counter()



def grab_day_links():#month_link: str):
    test = "https://www.npr.org//programs/all-things-considered/archive?date=12-31-2021"
    page = requests.get(test)
    month = BeautifulSoup(page.content, "html.parser")
    episode_list = month.find(id="episode-list")
    temp_list = []
    for article in episode_list.find_all("article", {"class": "program-segment"}):
        validate_quant_neg(article.find('a').get('href'))

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