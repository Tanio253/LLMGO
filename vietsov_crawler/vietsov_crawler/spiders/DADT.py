from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import scrapy
class CrawlingSpider(CrawlSpider):
    name = 'DADTcrawler'
    allowed_domains = ['vietsov.com.vn']
    start_urls = ['https://www.vietsov.com.vn/']
    
    
    rules = (
        Rule(LinkExtractor(allow = 'Pages/DuAn.aspx'), callback = 'parse_partner'),
        Rule(LinkExtractor(allow = 'Pages/KhoiThuongTang.aspx'), callback = 'parse_KTT'),
        
        
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
    
    
    def parse_partner(self, response):
        title = 'partner'
        content = list(map(lambda x: "https://www.vietsov.com.vn" + x,response.xpath('//div[contains(@id, "sliderParent")]//@src').getall()[:7]))
        yield {
            'title': title,
            'content': content
        }
        links = response.xpath('//div[contains(@class, "more-details")]//@href').getall()
        NC_link = "https://www.vietsov.com.vn"  + links[0]
        DH_link = "https://www.vietsov.com.vn"  + links[1]
        CTKT_link = "https://www.vietsov.com.vn"  + links[2]
        LDCD_link = "https://www.vietsov.com.vn"  + links[3]
        KTT_link = "https://www.vietsov.com.vn"  + links[4]
        
        
        if NC_link:
            yield scrapy.Request(url = NC_link, callback = self.parse_NC)
            
        if DH_link:
            yield scrapy.Request(url = DH_link, callback = self.parse_DH)
            
        if CTKT_link:
            yield scrapy.Request(url = CTKT_link, callback = self.parse_CTKT)
            
        if LDCD_link:
            yield scrapy.Request(url = LDCD_link, callback = self.parse_LDCD)
            
        if KTT_link:
            yield scrapy.Request(url = KTT_link, callback = self.parse_KTT)
        
    
    def parse_NC(self, response):
        title = self.processed_text(response.xpath('//span[contains(@class, "ms-rteFontSize-4")]//text()').getall()[1])
        content = '\n'.join(i for i in list(map(self.processed_text, response.xpath('//div[contains(@class, "ms-rtestate-field")]/p//text()').getall()[4:6])) if i is not None)
        yield {
            'title': title,
            'content': content
        }
        
        
    def parse_DH(self, response):
        title = self.processed_text(response.xpath('//span[contains(@class, "ms-rteFontSize-4")]//text()').getall()[1])
        id = response.xpath('//td[contains(@width, "44")]/p//strong/text()').getall()[1:]
        mine = response.xpath('//td[contains(@width, "175")]/p/span/text()').getall()
        guest = response.xpath('//td[contains(@width, "163")]/p/span/text()').getall()
        job_do = list(map(self.processed_text, response.xpath('//td[contains(@width, "464")]/p//span/text()').getall()))
        job_do = [job_do[1]] + [job_do[2] + '\n' + job_do[3]] + [job_do[4]+ '\n'+ job_do[5]] + [job_do[6]] + [job_do[7]] + [job_do[9]]
        content = [{
            'id': i,
            'mine':m,
            'guest': g,
            'job_do': j,
        } for i, m, g, j in zip(id, mine, guest, job_do)]
        yield {
            'title': title,
            'content': content,
        }
        
        
        
    def parse_CTKT(self, response):
        title = self.processed_text(response.xpath('//span[contains(@class, "ms-rteFontSize-4")]//text()').getall()[0])
        ###drop 39.75pt because the same as title
        height = ['49.5pt','48pt','32.25pt','30pt','66pt','44.25pt','38.25pt','64.5pt','58.5pt','41.25pt',\
            '0.5in','39pt','35.25pt','63.75pt','75pt','27pt','37.5pt','54.75pt','43.5pt','63pt','80.25pt','22.5pt','81.75pt']
        height_duplicate = {
            '49.5pt': 1,
            '30pt': 1,
            '66pt': 1,
            '44.25pt': 1,
            '38.25pt': 1,
            '64.5pt': 1,
            '58.5pt': 1,
            '41.25pt': 1,
            '39pt': 1,
            '35.25pt': 1,
            '27pt': 1,
            '37.5pt': 1,
            '54.75pt': 1,
            '43.5pt': 1,
            '63pt': 1,
            '80.25pt': 1,
            '22.5pt': 1,
            '81.75pt': 1,
            '48pt': 4,
            '32.25pt': 6,
            '0.5in': 2,
            '63.75pt': 2,
            '75pt': 2
        }
        ##48pt: 4
        ##32.25pt: 6
        ##0.5in: 2
        ##63.75pt: 2
        ##75pt: 2
        content = []
        for h in height:
            duplicate = height_duplicate[h]
            if duplicate!=1:
                for i in range(duplicate):
                    content.append({
                        'year': self.processed_text(response.xpath(f'//tr[contains(@style,"height: {h};")]')[i].xpath('./td[1]/p//font/text()').get()),
                        'client': self.processed_text(response.xpath(f'//tr[contains(@style,"height: {h};")]')[i].xpath('./td[2]/p//font/text()').get()),
                        'country': self.processed_text(response.xpath(f'//tr[contains(@style,"height: {h};")]')[i].xpath('./td[3]/p//font/text()').get()),
                        'project_name': self.processed_text(response.xpath(f'//tr[contains(@style,"height: {h};")]')[i].xpath('./td[4]/p//font/text()').get()),
                        'facility': list(map(self.processed_text, response.xpath(f'//tr[contains(@style,"height: {h};")]')[i].xpath('./td[5]/p//font/text()').getall())),
                        'scopeOfWork': self.processed_text(response.xpath(f'//tr[contains(@style,"height: {h};")]')[i].xpath('./td[6]/p//font/text()').get()),
                        'Pipe': self.processed_text(response.xpath(f'//tr[contains(@style,"height: {h};")]')[i].xpath('./td[7]/p//font/text()').get()),
                        'completionDate': self.processed_text(response.xpath(f'//tr[contains(@style,"height: {h};")]')[i].xpath('./td[8]/p//font/text()').get()),
                    })
            else:
                content.append({
                        'year': self.processed_text(response.xpath(f'//tr[contains(@style,"height: {h};")]').xpath('./td[1]/p//font/text()').get()),
                        'client': self.processed_text(response.xpath(f'//tr[contains(@style,"height: {h};")]').xpath('./td[2]/p//font/text()').get()),
                        'country': self.processed_text(response.xpath(f'//tr[contains(@style,"height: {h};")]').xpath('./td[3]/p//font/text()').get()),
                        'project_name': self.processed_text(response.xpath(f'//tr[contains(@style,"height: {h};")]').xpath('./td[4]/p//font/text()').get()),
                        'facility': list(map(self.processed_text, response.xpath(f'//tr[contains(@style,"height: {h};")]').xpath('./td[5]/p//font/text()').getall())),
                        'scopeOfWork': self.processed_text(response.xpath(f'//tr[contains(@style,"height: {h};")]').xpath('./td[6]/p//font/text()').get()),
                        'Pipe': self.processed_text(response.xpath(f'//tr[contains(@style,"height: {h};")]').xpath('./td[7]/p//font/text()').get()),
                        'completionDate': self.processed_text(response.xpath(f'//tr[contains(@style,"height: {h};")]').xpath('./td[8]/p//font/text()').get()),
                    })
        
        content.append({
                        'year': self.processed_text(response.xpath(f'//tr[contains(@style,"height: 39.75pt;")]')[1].xpath('./td[1]/p//font/text()').get()),
                        'client': self.processed_text(response.xpath(f'//tr[contains(@style,"height: 39.75pt;")]')[1].xpath('./td[2]/p//font/text()').get()),
                        'country': self.processed_text(response.xpath(f'//tr[contains(@style,"height: 39.75pt;")]')[1].xpath('./td[3]/p//font/text()').get()),
                        'project_name': self.processed_text(response.xpath(f'//tr[contains(@style,"height: 39.75pt;")]')[1].xpath('./td[4]/p//font/text()').get()),
                        'facility': list(map(self.processed_text, response.xpath(f'//tr[contains(@style,"height: 39.75pt;")]')[1].xpath('./td[5]/p//font/text()').getall())),
                        'scopeOfWork': self.processed_text(response.xpath(f'//tr[contains(@style,"height: 39.75pt;")]')[1].xpath('./td[6]/p//font/text()').get()),
                        'Pipe': self.processed_text(response.xpath(f'//tr[contains(@style,"height: 39.75pt;")]')[1].xpath('./td[7]/p//font/text()').get()),
                        'completionDate': self.processed_text(response.xpath(f'//tr[contains(@style,"height: 39.75pt;")]')[1].xpath('./td[8]/p//font/text()').get()),
                    })        
        
            
        yield {
            'title': title,
            'content': content,
        }
        
        
        
    def parse_LDCD(self, response):
        title = self.processed_text(response.xpath('//strong[contains(@class, "ms-rteFontSize-4")]//text()').get())
        content = []
        num_rows = 18
        for i in range(num_rows):
            content.append({
                'id': self.processed_text(response.xpath('//tr[contains(@style, "height: 31.15pt;")]')[i].xpath('./td[1]/p//font/text()').get()),
                'project_name': self.processed_text(response.xpath('//tr[contains(@style, "height: 31.15pt;")]')[i].xpath('./td[2]/p//font/text()').get()),
                'client': self.processed_text(response.xpath('//tr[contains(@style, "height: 31.15pt;")]')[i].xpath('./td[3]/p//font/text()').get()),
                'scope': self.processed_text(response.xpath('//tr[contains(@style, "height: 31.15pt;")]')[i].xpath('./td[4]/p//font/text()').get()),
                'weight': self.processed_text(response.xpath('//tr[contains(@style, "height: 31.15pt;")]')[i].xpath('./td[5]/p//font/text()').get()),
                'installationMethod': self.processed_text(response.xpath('//tr[contains(@style, "height: 31.15pt;")]')[i].xpath('./td[6]/p//font/text()').get()),
                'crane': self.processed_text(response.xpath('//tr[contains(@style, "height: 31.15pt;")]')[i].xpath('./td[7]/p//font/text()').get()),
                'launchingBarge': self.processed_text(response.xpath('//tr[contains(@style, "height: 31.15pt;")]')[i].xpath('./td[8]/p//font/text()').get()),
                
            })
            
        yield {
            'title': title,
            'content': content,
        }
        
        
        
    def parse_KTT(self, response):
        title = self.processed_text(response.xpath('//strong[contains(@class, "ms-rteFontSize-4")]//text()').get())
        content = []
        num_rows = 10
        for i in range(num_rows):
            content.append({
                'id': self.processed_text(response.xpath('//tr[contains(@style, "height: 31.15pt;")]')[i].xpath('./td[1]/p/strong/text()').get()),
                'project_name': self.processed_text(response.xpath('//tr[contains(@style, "height: 31.15pt;")]')[i].xpath('./td[2]/p//font/text()').get()),
                'client': self.processed_text(response.xpath('//tr[contains(@style, "height: 31.15pt;")]')[i].xpath('./td[3]/p//font/text()').get()),
                'scope': self.processed_text(response.xpath('//tr[contains(@style, "height: 31.15pt;")]')[i].xpath('./td[4]/p//font/text()').get()),
                'weight': self.processed_text(response.xpath('//tr[contains(@style, "height: 31.15pt;")]')[i].xpath('./td[5]/p//font/text()').get()),
                'installationMethod': self.processed_text(response.xpath('//tr[contains(@style, "height: 31.15pt;")]')[i].xpath('./td[6]/p//font/text()').get()),
                'crane': self.processed_text(response.xpath('//tr[contains(@style, "height: 31.15pt;")]')[i].xpath('./td[7]/p//font/text()').get()),
                'remark': self.processed_text(response.xpath('//tr[contains(@style, "height: 31.15pt;")]')[i].xpath('./td[8]/p//font/text()').get()),
                
            })
            
        yield {
            'title': title,
            'content': content,
        }