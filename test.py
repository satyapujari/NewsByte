import urllib.request
from bs4 import BeautifulSoup

url = "https://timesofindia.indiatimes.com/india/pm-narendra-modi-addresses-rally-in-delhi-top-quotes/articleshow/72923909.cms"
html =  urllib.request.urlopen(url)

#http = urllib3.PoolManager()
#http.request(url)
#html = http.request('GET',url)
#print(html. )
soup = BeautifulSoup(html,"lxml")

print(soup.title)

# get values:
print(soup.title.string)

# kill all script and style elements
for script in soup(["script", "style"]):
    script.extract()    # rip it out

# get text
text = soup.get_text()


# break into lines and remove leading and trailing space on each
lines = (line.strip() for line in text.splitlines())
# break multi-headlines into a line each
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# drop blank lines
text = '\n'.join(chunk for chunk in chunks if chunk)

print(text)