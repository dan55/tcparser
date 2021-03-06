import csv

from Article import Article
from bs4 import BeautifulSoup
from collections import namedtuple

import urllib

class TechCrunchParser():
    def __init__(self, homepage='https://techcrunch.com/'):
        self.homepage = homepage
        self.articles = []

    def get_article_stubs(self, page=None):
        ''' Scrape homepage for article stubs and return them as bs4 elements '''

        if page:
            # TODO: add pagination handling
            pass

        homepage = TechCrunchParser.soupify(url=self.homepage)

        return homepage.find_all(class_='post-title')

    def get_article(self, title, url):
        ''' Return an Article object after examining the article for company information '''

        try:
            company_url, company_name = self.parse_article(url)
            article = Article(title, url, company_name, company_url) 
        except (AttributeError, TypeError) as e:
            article = Article(title, url) 

        return article
    
    def get_articles(self):
        ''' Store the articles (to be written to CSV for now) '''

        for stub in self.get_article_stubs():
            article_url, article_title = self.parse_stub(stub)

            article = self.get_article(article_title, article_url)

            self.articles.append(article)

    def parse_stub(self, article_stub):
        ''' Parse an article stub for url to full article and title '''

        link_to_full_article = article_stub.find('a')

        url = link_to_full_article['href']
        title = link_to_full_article.find(text=True) 

        return (url, title)

    def parse_article(self, article_url):
        ''' Attempt to extract company information from article. 
            If not present bs4 raises AttributeError.

            TODO: Improve error handling? 
        '''

        article = TechCrunchParser.soupify(article_url)

        card = article.find(class_='data-card')
        card_links = card.find('a')

        company_name = card_links.find(text=True).strip()

        # This is a link to crunchbase
        #company_site = card_links['href']

        # TODO: OMG fix this!
        company_site = card.find(text='Website').parent.next_sibling.next_sibling.find('a')['href']
        
        return (company_site, company_name)

    def write_csv(self, filename='techcrunch_articles.csv'):
        ''' Write results to csv in the current directory '''

        filemode = 'w' # create or overwrite

        with open(filename, filemode) as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            
            # header
            writer.writerow(['Article Title', 'Article URL', 'Company', 'Company Website'])

            for article in self.articles:
                writer.writerow([article.title, article.url, article.company_name, article.company_site])

    # TODO: Move to a utility/helper class
    @staticmethod
    def soupify(url):
        ''' Return a BeautifulSoup object given a url '''

        return BeautifulSoup(urllib.request.urlopen(url))