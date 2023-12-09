from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import scrapy
class CrawlingSpider(CrawlSpider):
    name = 'CSVCcrawler'
    allowed_domains = ['vietsov.com.vn']
    start_urls = ['https://www.vietsov.com.vn/']
    
    
    rules = (
        Rule(LinkExtractor(allow = 'Pages/cosovatchat.aspx'), callback = 'parse_CSVC'),
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
    
    
    def parse_CSVC(self, response):
        title = response.xpath('//h1//text()').get()
        num_rows = 10
        content = []
        content_final = []
        for i in range(num_rows):
            content.append({
                'Tên': self.processed_text(response.xpath('//h4[contains(@class, "base-name")]//text()').getall()[i]),
                'Hình ảnh': "https://www.vietsov.com.vn" + response.xpath('//div[contains(@class, "element-item")]')[i].xpath('.//@src').get(),
                'Mô tả': self.processed_text(response.xpath('//div[contains(@class, "desription")]//text()').getall()[i]),
                'Nội dung': '\n'.join(i for i in (list(map(self.processed_text, response.xpath('//div[contains(@class, "content")]/ul')[i].xpath('.//text()').getall()))) if i is not None)
                
            })
        for c in content:
            content_list = [i for item in c.items() for i in item]
            content_str = '\n'.join(content_list)
            content_final.append(content_str)
        yield {
            'title': title,
            'content': content_final
        }
        
        