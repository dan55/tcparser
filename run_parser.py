''' Run the TechCrunchParser  '''

from TCParser import TechCrunchParser

if __name__ == '__main__':
    parser = TechCrunchParser()

    parser.get_articles()
    
    parser.write_csv()