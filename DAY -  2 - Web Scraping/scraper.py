# WHATEVER YOU DO, DO IT ETHICALLY

# install the modules

# pip3 install requests
# pip3 install beautifulsoup4

# import libraries
import requests
from bs4 import BeautifulSoup
import pprint

# send request
res = requests.get('https://news.ycombinator.com/news')

# Parse as html
soup = BeautifulSoup(res.text, 'html.parser')

# select elements
storylink = soup.select('.storylink')
subtext = soup.select('.subtext')

# Have fun ;)


def sort_links(hn):
    return sorted(hn, key=lambda hn: hn['points'], reverse=True)


def show_links(storylink, subtext):
    hn = []
    for idx, item in enumerate(storylink):
        link_text = item.text
        link = item['href']
        vote = subtext[idx].select('.score')
        if len(vote) > 0:
            points = int(vote[0].text.replace(' points', ''))

            if points > 99:
                hn.append({'title': link_text, 'link': link, 'points': points})
    return sort_links(hn)


pprint.pprint(show_links(storylink, subtext))
