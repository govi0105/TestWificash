import scrapy
from bs4 import BeautifulSoup
from Youtube_ultra.utils import MGClient


class Youtube_ultra(scrapy.Spider):
    name = "ultra"

    start_urls=['https://www.youtube.com/watch?v=Ol58Mo98AOE']

    def __init__(self):
        self.db = MGClient().get_mongo_client()

    def parse(self, response):
        soup = BeautifulSoup(response.body,'html.parser')
        for i in  soup.find('div',id='watch7-sidebar-modules').find_all('a'):
            url = 'https://www.youtube.com/' + i.get('href')
            if not self.db.Youtube_test.find_one({'source_url':url}):
                self.db.Youtube_test.insert({'source_url':url})
                print '>>>>>>>>>>>>>>>>>insert success<<<<<<<<<<<<<<<'
                yield scrapy.Request(url=url,callback=self.parse_again)
            else:
                print '>>>>>>>>>>>>>>>>>>alread exists<<<<<<<<<<<<<<'



    def parse_again(self,response):
        soup = BeautifulSoup(response.body,'html.parser')
        for i in  soup.find('div',id='watch7-sidebar-modules').find_all('a'):
            url = 'https://www.youtube.com/' + i.get('href')
            if not self.db.Youtube_test.find_one({'source_url':url}):
                self.db.Youtube_test.insert({'source_url':url})
                print '>>>>>>>>>>>>>>>>>insert success<<<<<<<<<<<<<<<'
                yield scrapy.Request(url=url,callback=self.parse)
            else:
                print '>>>>>>>>>>>>>>>>>>alread exists<<<<<<<<<<<<<<'