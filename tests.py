import os
import unittest

from bs4 import BeautifulSoup

from Article import Article
from TCParser import TechCrunchParser, soupify

class ParserTest(unittest.TestCase):
    def setUp(self):
        self.parser = TechCrunchParser()

        self.local_stub = 'test_stub.html'
        self.article_url = 'https://techcrunch.com/2017/02/15/reddit-tweaks-and-renames-public-front-page/'
        self.article_title = 'Reddit tweaks and renames public front\xa0page'
        self.company = 'reddit'
        self.company_url = 'http://www.reddit.com'

        self.article_with_no_company = 'https://techcrunch.com/2017/02/16/after-puzder-withdraws-trump-names-his-new-pick-for-labor-secretary/' 
        self.article_no_co_title = 'After Puzder withdraws, Trump names his new pick for labor secretary'

        self.csv_file = 'techcrunch_articles_test.csv'

    def get_local_test_stub(self, filename):
        ''' Returns a bs4 object of a local article stub '''

        f = open(filename, 'r')

        return BeautifulSoup(f)

    def test_parser_returns_article_stubs_from_homepage(self):
        num_stubs_expected = 20

        ret = self.parser.get_article_stubs()

        self.assertEqual(len(ret), num_stubs_expected)

    def test_parse_stub_returns_article_url_and_title(self):
        ret = self.parser.parse_stub(self.get_local_test_stub(self.local_stub))   
        self.assertEqual(ret, (self.article_url, self.article_title))

    def test_parse_article_with_company_returns_company_url_and_name(self):
        ret = self.parser.parse_article(self.article_url)

        self.assertEqual(ret, (self.company_url, self.company))

    def test_parse_article_without_company_raises_exception(self):
        self.assertRaises(AttributeError, self.parser.parse_article, self.article_with_no_company)

    def test_get_article_with_company_returns_article_obj(self):
        expected_article = Article(
            self.article_title,
            self.article_url,
            self.company, 
            self.company_url
        )

        ret = self.parser.get_article(self.article_title, self.article_url)

        self.assertEqual(ret, expected_article)

    def test_get_article_without_company_returns_article_obj(self):
        expected_article = Article(
            url=self.article_with_no_company,
            title=self.article_no_co_title
        )

        ret = self.parser.get_article(self.article_no_co_title, self.article_with_no_company)

        self.assertEqual(ret, expected_article)
        
    def test_write_csv(self):
        expected_num_articles = 20

        self.parser.get_articles()

        self.assertEqual(len(self.parser.articles), expected_num_articles)

        self.parser.write_csv(self.csv_file)

        self.assertTrue(os.path.isfile(self.csv_file))

        os.remove(self.csv_file)

if __name__ == '__main__':
    unittest.main()