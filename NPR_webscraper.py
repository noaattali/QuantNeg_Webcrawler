import requests
from bs4 import BeautifulSoup

def grab_audio_link(soup):
    """We can find the audio download button under wrapper > primary audio >
    audio-module-tools > audio-tool audio-tool-download ...."""
    audio_container = soup.find("li", class_ ="audio-tool audio-tool-download")
    attributes = audio_container.find("a")
    print(attributes['href'])

def extract_transcript(soup):
    text_container = soup.find(class_ = "transcript storytext")
    text_tags = text_container.find_all("p")
    for lines in text_tags:
        print(lines.string)


def extract_metadata():
    title
    speakers
    date



if __name__ == "__main__":
    url = "https://www.npr.org/templates/story/story.php?storyId=19075588"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

