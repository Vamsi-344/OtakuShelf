from bs4 import BeautifulSoup
import requests

# Get the HTML body from the url
r = requests.get('https://novelbin.com/b/devils-son-in-law/chapter-1')
# print(r.text)

# Create a Soup from the HTML we obtained
soup = BeautifulSoup(r.text, 'html.parser')

# Filter the div which contains the chapter content
chr_content = soup.find(attrs={"id": "chr-content"})

# Fetch both the chapter heading and the content
chr_head = chr_content.find("h4").text
chr_paras = []

for child in chr_content.find_all("p", recursive=False):
    chr_paras.append(child.text)

print(chr_head)
print(chr_paras)
# print(soup.find(attrs={"id": "chr-content"}).find("h4", recursive=False).text)
# print(soup.find(attrs={"id": "chr-content"}).find_all("p", recursive=False))
# for child in soup.find(attrs={"id": "chr-content"}, recursive=False).children:
#     print(child)
# print(soup.find("h4"))
# print(soup.find_all("p"))