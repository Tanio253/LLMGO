from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import scrapy
class CrawlingSpider(CrawlSpider):
    name = 'DVTTcrawler'
    allowed_domains = ['vietsov.com.vn']
    start_urls = ['https://www.vietsov.com.vn/']
    
    
    rules = (
        Rule(LinkExtractor(allow='Pages/DVTV.aspx')),
        Rule(LinkExtractor(allow = 'Pages/xnkt.aspx'), callback='parse_xnkt'),
        Rule(LinkExtractor(allow = 'Pages/xnxl.aspx'), callback='parse_xnxl'),
        Rule(LinkExtractor(allow = 'Pages/xnk.aspx'), callback='parse_xnk'),
        Rule(LinkExtractor(allow = 'Pages/xnkhoan.aspx'), callback='parse_xnkhoang'),
        Rule(LinkExtractor(allow = 'Pages/xndvl.aspx'), callback='parse_xndvl'),
        Rule(LinkExtractor(allow = 'Pages/xnvtb.aspx'), callback='parse_xnvtb'),
        Rule(LinkExtractor(allow = 'Pages/xndvc.aspx'), callback='parse_xndvc'),
        Rule(LinkExtractor(allow = 'Pages/xncd.aspx'), callback='parse_xncd'),
        Rule(LinkExtractor(allow = 'Pages/vien.aspx'), callback='parse_vien'),
        Rule(LinkExtractor(allow = 'Pages/ttat.aspx'), callback='parse_ttat'),
        Rule(LinkExtractor(allow = 'Pages/ttyt.aspx'), callback='parse_ttyt'),
        # Rule(LinkExtractor(allow = 'Pages/cntt.aspx'), callback='parse_cntt'),                         
        
        
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
    


    def parse_xnkt(self, response):
        title = response.css('.ms-rteFontSize-4 strong::text').get()
        addr = [response.xpath('//div[@style="text-align: center;"]/p/strong/text()').getall()[0][9:]]
        contact = response.xpath('//div[@style="text-align: center;"]/p/strong/text()').getall()[1:]
        contact = list(map(self.processed_text, contact))
        website_link = response.xpath('//div[@style="text-align: center;"]/p/a/@href').getall()
        contact +=website_link
        
        TEXT = list(map(self.processed_text, response.xpath('//p/text()').getall()))
        about = [TEXT[0]]
        mission = response.xpath('//div[@class="ms-rtestate-field"]/ul[1]/li//text()').getall()[:-1]
        resources = TEXT[1:3]
        productService = response.xpath('//div[@class="ms-rtestate-field"]/ul[2]/li//text()').getall()
        certificate = [TEXT[3]]
        partner = [TEXT[4]]
        content = '\n'.join(i for i in (addr + contact + about + mission + resources + certificate + productService + partner) if i is not None)
        nghiduong_link = 'https://www.vietsov.com.vn/' + response.xpath('//ul[contains(@class, "menu-list")]//a/@href').getall()[12]
        khachsan_link = 'https://www.vietsov.com.vn/' + response.xpath('//ul[contains(@class, "menu-list")]//a/@href').getall()[13]
        bvvt_link = 'https://www.vietsov.com.vn/' + response.xpath('//ul[contains(@class, "menu-list")]//a/@href').getall()[14]
        dsno_link = 'https://www.vietsov.com.vn/' + response.xpath('//ul[contains(@class, "menu-list")]//a/@href').getall()[15]
        yield {
            'title': title,
            'content': content,
        }
        
        if nghiduong_link:
            yield scrapy.Request(url = nghiduong_link, callback = self.parse_nghiduong)
            
        if khachsan_link:
            yield scrapy.Request(url = khachsan_link, callback = self.parse_khachsan)
            
        if bvvt_link:
            yield scrapy.Request(url = bvvt_link, callback = self.parse_bvvt)
            
        if dsno_link:
            yield scrapy.Request(url = dsno_link, callback = self.parse_dsno)
            
        
        
    def parse_xnxl(self, response):
        title = self.processed_text(response.xpath('//div[@style="text-align: center;"]//text()').getall()[1] + " " +\
            response.xpath('//div[@style="text-align: center;"]//text()').getall()[4] + " " +\
            response.xpath('//div[@style="text-align: center;"]//text()').getall()[7]
            )
        addr = [self.processed_text(response.xpath('//p[@style="text-align: center;"]//text()').getall()[0][9:])]
        contact =response.xpath('//p[@style="text-align: center;"]//text()').getall()[1:]
        contact = list(map(self.processed_text, contact))
        # website_link = response.xpath('//p[@style="text-align: center;"]//a/@href').get()
        # contact +=website_link
        
        TEXT = list(map(self.processed_text, response.xpath('//p/text()').getall()))
        UL_TEXT = response.xpath('//div[@class="ms-rtestate-field"]//ul')
        
        about = [TEXT[2]]
        mission = [TEXT[3]]
        resources = TEXT[4:11]
        certificate = [TEXT[11]]
        productService = list(map(self.processed_text, UL_TEXT[0].xpath('.//li//text()').getall()))
        partner = TEXT[12:14] + list(map(self.processed_text, UL_TEXT[1].xpath('.//li//text()').getall()))
        content = '\n'.join(i for i in (addr + contact + about + mission + resources + certificate + productService + partner) if i is not None)
        
        
        yield {
            'title': title,
            'content': content
        }
        
        
    def parse_xnk(self, response):
        title = self.processed_text(response.css('.ms-rteFontSize-4::text').get())
        addr = [response.xpath('//p[@style="text-align: center;"]/strong/em/text()').getall()[1][9:]]
        contact = response.xpath('//p[@style="text-align: center;"]/strong/em/text()').getall()[2:]
        contact = list(map(self.processed_text, contact))
        website_link = [response.xpath('//p[@style="text-align: center;"]/a/@href').get()]
        contact +=website_link
        
        TEXT = list(map(self.processed_text, response.xpath('//p/text()').getall()))
        UL_TEXT = response.xpath('//div[@class="ms-rtestate-field"]//ul')
        about = [TEXT[2]]
        mission = list(map(self.processed_text, UL_TEXT[0].xpath('.//li//text()').getall()))
        resources = list(map(self.processed_text, UL_TEXT[1].xpath('.//li//text()').getall()))
        certificate = list(map(self.processed_text, UL_TEXT[4].xpath('.//li//text()').getall()))
        productService = list(map(self.processed_text, UL_TEXT[5].xpath('.//li//text()').getall()))
        partner = list(map(self.processed_text, UL_TEXT[8].xpath('.//li//text()').getall()))
        content = '\n'.join(i for i in (addr + contact + about + mission + resources + certificate + productService + partner) if i is not None)
        
        yield {
            'title': title,
            'content': content
        }
        
        
        
    def parse_xnkhoang(self, response):
        title = self.processed_text(response.css('.ms-rteFontSize-4::text').get())
        addr = [''.join(response.xpath('//p[@style="text-align: center;"]/strong/em/text()').getall()[:2])[9:]]
        contact = response.xpath('//p[@style="text-align: center;"]/strong/em/text()').getall()[4:6]
        contact = list(map(self.processed_text, contact))
        website_link = [response.xpath('//p[@style="text-align: center;"]/a/strong/em/text()').get()]
        contact +=website_link
        
        TEXT = list(map(self.processed_text, response.xpath('//p/text()').getall()))
        UL_TEXT = response.xpath('//div[@class="ms-rtestate-field"]//ul')
        
        about = [TEXT[2]]
        mission = list(map(self.processed_text, UL_TEXT[0].xpath('.//li//text()').getall()))
        resources = TEXT[3:5]
        certificate = [TEXT[5]]
        productService = list(map(self.processed_text, UL_TEXT[1].xpath('.//li//text()').getall()))
        partner = [TEXT[6]] + list(map(self.processed_text, UL_TEXT[2].xpath('.//li//text()').getall())) + [TEXT[7]]
        content = '\n'.join(i for i in (addr + contact + about + mission + resources + certificate + productService + partner) if i is not None)
        
        yield {
            'title': title,
            'content': content
        }
        
        
        
    def parse_xndvl(self, response):
        title = self.processed_text(response.css('.ms-rteFontSize-4::text').get())
        addr = response.xpath('//p[@style="text-align: center;"]/strong/strong/text()').getall()[1:5]
        contact = response.xpath('//p[@style="text-align: center;"]/strong/strong/text()').getall()[6:]
        contact = list(map(self.processed_text, contact))
        website_link = [response.xpath('//p[@style="text-align: center;"]//a/@href').get()]
        contact +=["Website: "]+website_link
        
        TEXT = list(map(self.processed_text, response.xpath('//p/text()').getall()))
        UL_TEXT = response.xpath('//div[@class="ms-rtestate-field"]//ul')
        
        about = [TEXT[1]]
        mission = [TEXT[2]]
        resources = TEXT[3:6]
        certificate = [TEXT[6]]
        productService = list(map(self.processed_text, UL_TEXT[0].xpath('.//li//text()').getall()))
        partner = [TEXT[8]]
        content = '\n'.join(i for i in (addr + contact + about + mission + resources + certificate + productService + partner) if i is not None)
        
        yield {
            'title': title,
            'content': content
        }
        
        
        
    
    def parse_xnvtb(self, response):
        title = self.processed_text(response.css('.ms-rteFontSize-4::text').get())
        addr = [''.join(response.xpath('//p[@style="text-align: center;"]/strong/text()').getall()[3:12])]
        contact = response.xpath('//p[@style="text-align: center;"]/strong/text()').getall()[12:]
        contact = list(map(self.processed_text, contact))
        website_link = [response.xpath('//p[@style="text-align: center;"]//a/@href').get()]
        contact +=["Website: "] +website_link
        
        TEXT = list(map(self.processed_text, response.xpath('//p/text()').getall()))
        UL_TEXT = response.xpath('//div[@class="ms-rtestate-field"]//ul')
        
        about = [TEXT[2]]
        mission = list(map(self.processed_text, UL_TEXT[0].xpath('.//li//text()').getall()))
        resources = list(map(self.processed_text, UL_TEXT[1].xpath('.//li//text()').getall()))
        certificate = [TEXT[3]]
        productService = list(map(self.processed_text, UL_TEXT[2].xpath('.//li//text()').getall())) + \
            list(map(self.processed_text, UL_TEXT[3].xpath('.//li//text()').getall())) + \
            list(map(self.processed_text, UL_TEXT[4].xpath('.//li//text()').getall()))    
        partner = TEXT[5:7]
        content = '\n'.join(i for i in (addr + contact + about + mission + resources + certificate + productService + partner) if i is not None)
        
        yield {
            'title': title,
            'content': content
        }
        
        
        
    def parse_xndvc(self, response):
        title = self.processed_text(response.css('.ms-rteFontSize-4::text').get())
        addr = [response.xpath('//p[@style="text-align: center;"]/strong/strong/text()').getall()[3]]
        contact = response.xpath('//p[@style="text-align: center;"]/strong/strong/text()').getall()[5:]
        contact = list(map(self.processed_text, contact))
        website_link = [response.xpath('//p[@style="text-align: center;"]//a/strong/text()').get()]
        contact +=["Website: "] +website_link
        
        TEXT = list(map(self.processed_text, response.xpath('//p/text()').getall()))
        UL_TEXT = response.xpath('//div[@class="ms-rtestate-field"]//ul')
        
        about = [TEXT[2]]
        mission = [TEXT[3]]
        resources = [TEXT[4]] + list(map(self.processed_text, UL_TEXT[0].xpath('.//li//text()').getall())) + [TEXT[5]]
        certificate = [TEXT[6]]
        productService = list(map(self.processed_text, UL_TEXT[1].xpath('.//li//text()').getall()))
        partner = TEXT[7:9]
        content = '\n'.join(i for i in (addr + contact + about + mission + resources + certificate + productService + partner) if i is not None)
        
        
        yield {
            'title': title,
            'content': content
        }
        
        
        
    def parse_xncd(self, response):
        title = self.processed_text(response.css('.ms-rteFontSize-4::text').get())
        addr = [''.join(response.xpath('//p[@style="text-align: center;"]/strong//text()').getall()[3:11])]
        contact = response.xpath('//p[@style="text-align: center;"]/strong//text()').getall()[11:]
        contact = list(map(self.processed_text, contact))
        website_link = [response.xpath('//p[@style="text-align: center;"]//a/@href').get()]
        contact +=["Website: "] +website_link
        
        TEXT = list(map(self.processed_text, response.xpath('//p/text()').getall()))
        UL_TEXT = response.xpath('//div[@class="ms-rtestate-field"]//ul')
        
        about = [TEXT[2]]
        mission = list(map(self.processed_text, UL_TEXT[0].xpath('.//li//text()').getall()))
        resources = TEXT[3:6] + list(map(self.processed_text, UL_TEXT[1:3].xpath('.//li//text()').getall())) 
        certificate = [TEXT[6]] + list(map(self.processed_text, UL_TEXT[3].xpath('.//li//text()').getall()))
        productService = list(map(self.processed_text, UL_TEXT[4:10].xpath('.//li//text()').getall()))
        partner = [TEXT[8]]+ list(map(self.processed_text, UL_TEXT[10].xpath('.//li//text()').getall()))
        content = '\n'.join(i for i in (addr + contact + about + mission + resources + certificate + productService + partner) if i is not None)
        
        yield {
            'title': title,
            'content': content,
        }
        


    def parse_vien(self, response):
        title = self.processed_text(''.join(response.css('.ms-rteFontSize-4 strong::text').getall()))
        addr = [self.processed_text(''.join(response.xpath('//p[@style="text-align: center;"]/strong//text()').getall()[1:12]))]
        contact = response.xpath('//p[@style="text-align: center;"]/strong//text()').getall()[12:]
        contact = list(map(self.processed_text, contact))
        # website_link = response.xpath('//p[@style="text-align: center;"]//a/@href').get()
        # contact +=website_link
        
        TEXT = list(map(self.processed_text, response.xpath('//p/text()').getall()))
        UL_TEXT = response.xpath('//div[@class="ms-rtestate-field"]//ul')
        
        about = [TEXT[2]]
        mission = list(map(self.processed_text, UL_TEXT[0].xpath('.//li//text()').getall()))
        resources = [''.join(TEXT[3:5])] + [TEXT[5]] + [''.join(TEXT[7:9])]
        certificate = [TEXT[9]]
        productService = list(map(self.processed_text, UL_TEXT[1].xpath('.//li//text()').getall()))
        partner = TEXT[10:16]
        content = '\n'.join(i for i in (addr + contact + about + mission + resources + certificate + productService + partner) if i is not None)
        
        yield {
            'title': title,
            'content': content
        }
        
     
        
    def parse_ttat(self, response):
        title = self.processed_text(response.css('.ms-rteFontSize-4::text').get())
        addr = [self.processed_text(''.join(response.xpath('//p[@style="text-align: center;"]//text()').getall()[5]))]
        contact = [self.processed_text(response.xpath('//p[@style="text-align: center;"]//text()').getall()[6])]
        # website_link = response.xpath('//p[@style="text-align: center;"]//a/@href').get()
        # contact +=website_link
        
        TEXT = list(map(self.processed_text, response.xpath('//p/text()').getall()))
        UL_TEXT = response.xpath('//div[@class="ms-rtestate-field"]//ul')
        
        about = [TEXT[1]]
        mission = TEXT[2:7]
        resources = [TEXT[8]]
        certificate = TEXT[9:16]
        productService = [TEXT[16]] + list(map(self.processed_text, UL_TEXT[0:4].xpath('.//li//text()').getall()))
        partner = TEXT[21:23] 
        content = '\n'.join(i for i in (addr + contact + about + mission + resources + certificate + productService + partner) if i is not None)
        
        yield {
            'title': title,
            'content': content,
        }



    def parse_ttyt(self, response):
        title = self.processed_text(response.xpath('//strong[contains(@class,"ms-rteFontSize-4")]//text()').get())
        addr = [self.processed_text(response.xpath('//p[@style="text-align: center;"]//text()').getall()[2][9:])]
        contact = [self.processed_text(''.join(response.xpath('//p[@style="text-align: center;"]//text()').getall()[3:]))]
        # website_link = response.xpath('//p[@style="text-align: center;"]//a/@href').get()
        # contact +=website_link
        
        TEXT = list(map(self.processed_text, response.xpath('//p/text()').getall()))
        UL_TEXT = response.xpath('//div[@class="ms-rtestate-field"]//ul')
        
        about = [TEXT[1]]
        mission = list(map(self.processed_text, UL_TEXT[0].xpath('.//li//text()').getall()))
        resources = TEXT[3:5] + list(map(self.processed_text, UL_TEXT[1].xpath('.//li//text()').getall()))
        certificate = [TEXT[5]]
        productService = list(map(self.processed_text, UL_TEXT[2].xpath('.//li//text()').getall()))
        partner = [TEXT[6]]
        content = '\n'.join(i for i in (addr + contact + about + mission + resources + certificate + productService + partner) if i is not None)
        
        yield {
            'title': title,
            'content': content
        }
        
        
        
    def parse_cntt(self, response):
        title = self.processed_text(response.xpath('//p[@style="text-align: center;"]//text()').getall()[0])
        addr = [self.processed_text(response.xpath('//p[@style="text-align: center;"]//text()').getall()[1][9:])]
        contact = [self.processed_text(''.join(response.xpath('//p[@style="text-align: center;"]//text()').getall()[2:]))]
        # website_link = response.xpath('//p[@style="text-align: center;"]//a/@href').get()
        # contact +=website_link
        
        TEXT = list(map(self.processed_text, response.xpath('//p/text()').getall()))
        UL_TEXT = response.xpath('//div[@class="ms-rtestate-field"]//ul')
        
        about = [TEXT[2]]
        mission = list(map(self.processed_text, UL_TEXT[0].xpath('.//li//text()').getall()))
        resources = TEXT[3:5] + list(map(self.processed_text, UL_TEXT[1].xpath('.//li//text()').getall()))
        certificate = TEXT[5:7]
        productService = list(map(self.processed_text, UL_TEXT[2:4].xpath('.//li//text()').getall())) + list(map(lambda x: "https://www.vietsov.com.vn" + x, response.xpath('//p//img/@src').getall()))
        partner = [TEXT[12]] + list(map(self.processed_text, UL_TEXT[4].xpath('.//li//text()').getall()))
        content = '\n'.join(i for i in (addr + contact + about + mission + resources + certificate + productService + partner) if i is not None)
        
        yield {
            'title': title,
            'content': content
        }
        
        
        
    def parse_khachsan(self, response):
        title = self.processed_text(response.xpath('//p[@style="text-align: center;"]//text()').getall()[0])
        addr = [self.processed_text(response.xpath('//p[@style="text-align: center;"]//text()').getall()[3][1:])]
        contact = [self.processed_text(''.join(response.xpath('//p[@style="text-align: center;"]//text()').getall()[5:]))]
        # website_link = response.xpath('//p[@style="text-align: center;"]//a/@href').get()
        # contact +=website_link
        
        TEXT = list(map(self.processed_text, response.xpath('//p/text()').getall()))
        UL_TEXT = response.xpath('//div[@class="ms-rtestate-field"]//ul')
        
        about = TEXT[0:2]
        facilities = response.xpath('//div[@class="ms-rtestate-field"]//ul')[0:2].xpath('.//li//text()').getall()
        # mission = list(map(self.processed_text, UL_TEXT[0].xpath('.//li//text()').getall()))
        # resources = TEXT[3:5] + list(map(self.processed_text, UL_TEXT[1].xpath('.//li//text()').getall()))
        # certificate = TEXT[5:7]
        # productService = list(map(self.processed_text, UL_TEXT[2:4].xpath('.//li//text()').getall())) + list(map(lambda x: "https://www.vietsov.com.vn" + x, response.xpath('//p//img/@src').getall()))
        # partner = [TEXT[12]] + list(map(self.processed_text, UL_TEXT[4].xpath('.//li//text()').getall()))
        content = '\n'.join(i for i in (addr + contact + about + facilities) if i is not None)
        
        yield {
            'title': title,
            'content': content
        }
        
        
        
    def parse_nghiduong(self, response):
        title = self.processed_text(response.xpath('//p[@style="text-align: center;"]//text()').getall()[0])
        addr = [self.processed_text(response.xpath('//p[@style="text-align: center;"]//text()').getall()[1][9:])]
        contact = [self.processed_text(''.join(response.xpath('//p[@style="text-align: center;"]//text()').getall()[2:]))]
        # website_link = response.xpath('//p[@style="text-align: center;"]//a/@href').get()
        # contact +=website_link
        
        TEXT = list(map(self.processed_text, response.xpath('//p/text()').getall()))
        UL_TEXT = response.xpath('//div[@class="ms-rtestate-field"]//ul')
        
        about = TEXT[0:7]
        # mission = list(map(self.processed_text, UL_TEXT[0].xpath('.//li//text()').getall()))
        # resources = TEXT[3:5] + list(map(self.processed_text, UL_TEXT[1].xpath('.//li//text()').getall()))
        # certificate = TEXT[5:7]
        # productService = list(map(self.processed_text, UL_TEXT[2:4].xpath('.//li//text()').getall())) + list(map(lambda x: "https://www.vietsov.com.vn" + x, response.xpath('//p//img/@src').getall()))
        # partner = [TEXT[12]] + list(map(self.processed_text, UL_TEXT[4].xpath('.//li//text()').getall()))
        content = '\n'.join(i for i in (addr + contact + about) if i is not None)
        
        yield {
            'title': title,
            'content': content
        }
        
        
        
    def parse_bvvt(self, response):
        title = self.processed_text(response.xpath('//p[@style="text-align: center;"]//text()').getall()[0])
        addr = [self.processed_text(response.xpath('//p[@style="text-align: center;"]//text()').getall()[6])]
        contact = [self.processed_text(''.join(response.xpath('//p[@style="text-align: center;"]//text()').getall()[8:]))]
        # website_link = response.xpath('//p[@style="text-align: center;"]//a/@href').get()
        # contact +=website_link
        
        TEXT = list(map(self.processed_text, response.xpath('//p/text()').getall()))
        UL_TEXT = response.xpath('//div[@class="ms-rtestate-field"]//ul')
        
        about = [TEXT[4]]
        mission = TEXT[5:8]
        resources = TEXT[8:11]
        certificate = TEXT[11:13]
        active = [TEXT[13]] + list(map(self.processed_text, UL_TEXT[0].xpath('.//li//text()').getall()))
        content = '\n'.join(i for i in (addr + contact + about + mission + resources + certificate + active ) if i is not None)
        
        yield {
            'title': title,
            'content': content
        }
        
        
    def parse_dsno(self, response):
        title = self.processed_text(response.xpath('//p[@style="text-align: center;"]//text()').getall()[0])
        addr = [self.processed_text(response.xpath('//p[@style="text-align: center;"]//text()').getall()[1][9:])]
        contact = [self.processed_text(''.join(response.xpath('//p[@style="text-align: center;"]//text()').getall()[2:]))]
        # website_link = response.xpath('//p[@style="text-align: center;"]//a/@href').get()
        # contact +=website_link
        
        TEXT = list(map(self.processed_text, response.xpath('//p/text()').getall()))
        UL_TEXT = response.xpath('//div[@class="ms-rtestate-field"]//ul')
        
        about = [TEXT[0]]
        mission = list(map(self.processed_text, UL_TEXT[0].xpath('.//li//text()').getall()))
        resources = [TEXT[1]]
        certificate = [TEXT[2]]
        productService = list(map(self.processed_text, UL_TEXT[1].xpath('.//li//text()').getall()))
        partner = [TEXT[3]]
        content = '\n'.join(i for i in (addr + contact + about + mission + resources + certificate + productService + partner) if i is not None)
        
        yield {
            'title': title,
            'content': content
        }
