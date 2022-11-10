# scraping the frist 2 pages of hacker news and taking showing the news with at least 100 points (more relevant) - sorted in DESC order
import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/news?p=2')
# using beautiful soup to clean the data
soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res.text, 'html.parser')

links = soup.select('.titleline > a')
links2 = soup.select('.titleline > a')
subtext = soup.select('.subtext')
subtext2 = soup.select('.subtext')

mega_links = links + links2
mega_subtext = subtext + subtext2


def sort_stories_by_voted(hnlist):
    # need to pass a key as to what it must be sorted by
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


def create_custom_hn(links, subtext):
    hn = []
    for index, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[index].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_voted(hn)


pprint.pprint(create_custom_hn(mega_links, mega_subtext))
