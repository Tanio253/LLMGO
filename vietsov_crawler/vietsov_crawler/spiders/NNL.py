from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import scrapy
class CrawlingSpider(CrawlSpider):
    name = 'NNLcrawler'
    allowed_domains = ['vietsov.com.vn']
    start_urls = ['https://www.vietsov.com.vn/']
    
    
    rules = (
        Rule(LinkExtractor(allow = 'Pages/nguonnhanluc.aspx'), callback = 'parse_NL'),
        
        
    )
    
    
    def processed_text(self, text):
        if text==None:
            return text
        while '\xa0' in text:
            text = text.replace('\xa0',' ')
        
        while '\u200b' in text:
            text = text.replace('\u200b','')
        
        while '\r\n' in text:
            text = text.replace('\r\n','')
        
        while '\t' in text:
            text = text.replace('\t','')    
        
        while '\n' in text:
            text = text.replace('\n',' ')    
        text = text.strip()
        
        if text=='':
            return None
        
        return text
    
    
    
    def parse_NL(self, response):
        title = response.xpath('//h1/text()').get()
        img =  "https://www.vietsov.com.vn" + response.xpath('//div[contains(@class, "wrapper-text")]//@src').get()
        content = '\n'.join(i for i in list(map(self.processed_text, response.xpath('//div[contains(@class, "nnl-content")]//text()').getall()[2:])) if i is not None).strip()
        yield {
            'title': title,
            'image': img,
            'content': content
        }