import urllib.request
from bs4 import BeautifulSoup

class Parser(object):

    def __init__(self, url):
        self.html = urllib.request.urlopen(url)
        self.soup = BeautifulSoup(self.html, "lxml")


    def get_tittle(self):
        return self.soup.title.string

    def get_fullText(self):
        # kill all script and style elements
        for script in self.soup(["script", "style"]):
            script.extract()  # rip it out
        # get text
        text = self.soup.get_text()

        # break into lines and remove leading and trailing space on each
        lines = (line.strip() for line in text.splitlines())
        # break multi-headlines into a line each
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        # drop blank lines
        text = '\n'.join(chunk for chunk in chunks if chunk)
        return text







