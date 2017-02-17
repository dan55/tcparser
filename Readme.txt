Overview:

    
    Creates a CSV file containing the titles and URLs of the 20 "latest" articles on TechCrunch's homepage. It 

includes the company the article concerns by scraping the "card" on the right-hand of the article. If none 

exists, company information is recorded as 'n/a'.



Files:

    Article.py - a class that represents an article

    TCParser.py - a class representing the parser 

    run_parser.py - invoked directly with no args to runs the program 

    tests.py - a test suite

    test_stub.html - sample markup of an article stub on the homepage for testing



Major TODO:

    There is occasionally a card with multiple entities (not just the company), and the parser chooses the 

wrong entity. 