from bs4 import BeautifulSoup
import requests

def scrapeChapter(url):
    # Get the HTML body from the url
    r = requests.get(url)
    
    # Create a Soup from the HTML we obtained
    soup = BeautifulSoup(r.text, 'html.parser')

    # Filter the div which contains the chapter content
    chr_content = soup.find(attrs={"id": "chr-content"})

    # Get all immediate children elements
    children = list(chr_content.children)
    
    # Skip over any whitespace or newlines
    first_real_element = next(child for child in children if getattr(child, 'text', '').strip())

    # Extract the chapter title
    chr_head = first_real_element.get_text(strip=True)

    # Extract the content paragraphs, skipping the first element
    chr_paras = [
        child.get_text(strip=True)
        for child in children
        if child != first_real_element and child.name == 'p'
    ]

    return chr_head, chr_paras
