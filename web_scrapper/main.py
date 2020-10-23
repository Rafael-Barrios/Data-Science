import argparse
import logging
logging.basicConfig(level=logging.INFO) #Genera información simple de la web visitada

from common import config


logger = logging.getLogger(__name__)


def _news_scraper(news_site):
    host = config()['news_sites'][news_site]['url']

    logging.info('Beginning scraper for {}'.format(host))



if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    news_site_choices = list(config()['news_sites'].keys())
    parser.add_argument('news_site',
                        help='La nueva web que quieres parsear',
                        type=str,
                        choices=news_site_choices)

    args = parser.parse_args()
    _news_scraper(args.news_site)

