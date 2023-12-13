from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import scrapy
class CrawlingSpider(CrawlSpider):
    name = 'TDTScrawler'
    allowed_domains = ['vietsov.com.vn']
    start_urls = ['https://www.vietsov.com.vn/']
    
    
    rules = (
        Rule(LinkExtractor(allow = 'Pages/tuyendung.aspx'), callback = 'parse_TD'),
        Rule(LinkExtractor(allow = 'Pages/tuyensinh1.aspx'), callback = 'parse_TS'),
        
        
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
            
        text = text.strip()
        
        if text=='':
            return None
        
        return text
    
    
    def parse_TD(self, response):
        title = self.processed_text(response.xpath('//div[contains(@class, "ms-rtestate-field")]/span/strong/text()').get())
        content = ' '.join(i for i in list(map(self.processed_text, response.xpath('//div[contains(@class, "ms-rtestate-field")]//text()').getall()[1:3])) if i is not None)+'\n'+\
        ' '.join(i for i in list(map(self.processed_text, response.xpath('//div[contains(@class, "ms-rtestate-field")]//text()').getall()[3:])) if i is not None)
        
        yield {
            'title': title,
            'content': [content]
        }
        
        
    def parse_TS(self, response):
        title = self.processed_text(response.xpath('//div[contains(@class, "ms-rtestate-field")]/span/strong/text()').get())
        content = self.processed_text(response.xpath('//h3//text()').get())
        link = list(map(lambda x: "https://www.vietsov.com.vn/" + x, response.xpath('//div/p/a/@href').getall()[:2]))
        yield {
            'title': title,
            'content': [content],
            # 'link': link
        }