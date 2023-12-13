from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class CrawlingSpider(CrawlSpider):
    name = 'SPDVcrawler'
    allowed_domains = ['vietsov.com.vn']
    start_urls = ['https://www.vietsov.com.vn/']
    
    
    rules = (
        Rule(LinkExtractor(allow = 'Pages/SanPhamDV.aspx'), callback = 'parse_SPDV'),
        
        
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
    
    
    def parse_SPDV(self, response):
        title = self.processed_text(response.css('.product-name a::text').getall()[0])
        description = self.processed_text(response.xpath('//div[@class="desription"]//text()').get())
        product_content = list(map(self.processed_text, response.css('.product-name a::text').getall()[1:]))
        product_imgs = list(map(lambda x: "https://www.vietsov.com.vn/" + x, response.xpath('//img[contains(@class, "hideo")]/@src').extract()))
        content = description + '\n' + '\n'.join(product_content)
        
        yield {
            'title': title,
            'content': [content]
        }
        
        