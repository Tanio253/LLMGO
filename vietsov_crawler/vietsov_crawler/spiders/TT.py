from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import scrapy
class CrawlingSpider(CrawlSpider):
    name = 'TTcrawler'
    allowed_domains = ['vietsov.com.vn']
    start_urls = ['https://www.vietsov.com.vn/']
    
    
    rules = (
        Rule(LinkExtractor(allow = 'Pages/Details.aspx'), callback = "parse_news", follow = True),
           
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
    
    
    def parse_news(self, response):
        title = self.processed_text(response.xpath('//div[@class="title1"]//text()').get())
        date_published = response.xpath('//div[@id="topcontent"]/b/text()').get()
        content = ' '.join(i for i in list(map(self.processed_text, response.xpath('//div[@id="topslidesdiv"]/div//text()').getall())) if i is not None)
        img = list(map(lambda x: "https://www.vietsov.com.vn/" + x, response.xpath('//div[@id="topslidesdiv"]//p//img//@src').getall()))
        content = f"Ngày phát hành: {date_published}\n{content}"
        yield {
            'title': title,
            'content': [content],
            # 'image': img,
        }