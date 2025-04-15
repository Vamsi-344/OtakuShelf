from bs4 import BeautifulSoup
import requests

def scrapeChapter(url):
    # Get the HTML body from the url
    r = requests.get(url)
    # print(r.text)

    # Create a Soup from the HTML we obtained
    soup = BeautifulSoup(r.text, 'html.parser')

    # Filter the div which contains the chapter content
    chr_content = soup.find(attrs={"id": "chr-content"})

    # Fetch both the chapter heading and the content
    chr_head = chr_content.find("strong").text
    chr_paras = []

    for child in chr_content.find_all("p", recursive=False):
        chr_paras.append(child.text)
    
    return chr_head, chr_paras
    # print(chr_head)
    # print(chr_paras)