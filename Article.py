class Article():
    '''
    Represents a news article. 

    TODO: Could decompose company into a separate class.
    '''

    def __init__(self, title, url, company_name = 'n\\a', company_site = 'n\\a'):
        self.company_name = company_name
        self.company_site = company_site
        self.title = title
        self.url = url

    def __eq__(self, other):
        return self.company_name == other.company_name and \
            self.company_site == other.company_site and \
            self.title == other.title and \
            self.url == other.url

    def __str__(self):
        return self.company_name + ' ' + self.title
