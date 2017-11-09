import json, sys
import urllib.request
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import quote_plus

class Reverso:

    def __init__(self, src="fr", dest="es"):
        self.src = self.get_mapped_language(src)
        self.dest = self.get_mapped_language(dest)

    def get_mapped_language(self, short):
        return {
                'fr': 'french',
                'es': 'spanish',
                'en': 'english',
                'pt': 'portuguese',
                'ru': 'russian',
                'de': 'german',
        }[short]

    def translate(self, query, src=None, dest=None):
        if src is not None:
            self.src = self.get_mapped_language(src)
        if dest is not None:
            self.dest = self.get_mapped_language(dest)
        url = "http://context.reverso.net/translation/%s-%s/%s" % (self.src, self.dest, quote_plus(query))
        req = urllib.request.Request(
	    url, 
	    data=None, 
	    headers={
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
            }
        )
        webpage = urllib.request.urlopen(req).read()
        soup = BeautifulSoup(webpage, 'html.parser')
        examples = soup.find_all("div", class_="example")
        res = []
        for idrow, row in enumerate(examples):
            src = row.find('div',class_='src')
            trg = row.find('div',class_='trg')
            tr = {
                'fr': src.text.strip(),
                'es': trg.text.strip()
            }
            res.append(tr)
        return res


if __name__ == '__main__':
    reverso = Reverso()
    print(reverso.translate('très bien'))
