from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
class CrawlingSpider(CrawlSpider):
    name = 'GTcrawler'
    allowed_domains = ['vietsov.com.vn']
    start_urls = ['https://www.vietsov.com.vn/']
    
    
    rules = (
        Rule(LinkExtractor(allow = 'Pages/GioiThieu.aspx')),
        Rule(LinkExtractor(allow = 'Pages/GioiThieuCT.aspx'), callback = 'parse_GT'),
        Rule(LinkExtractor(allow = 'Pages/LichSuhinhthanh.aspx'), callback = 'parse_LSHT'),
        Rule(LinkExtractor(allow = 'Pages/CoCau.aspx'), callback = 'parse_CCTC'),
        Rule(LinkExtractor(allow = 'Pages/lanhdao.aspx'), callback = 'parse_LD'),
        Rule(LinkExtractor(allow = 'Pages/LinhVuc.aspx'), callback = 'parse_LV'),
        Rule(LinkExtractor(allow = 'Pages/TiemNang.aspx'), callback = 'parse_TN'),
        Rule(LinkExtractor(allow = 'Pages/NhungThanhTuu.aspx'), callback = 'parse_TT'),
        # Rule(LinkExtractor(allow = 'Pages/HinhAnh.aspx'), callback = 'parse_HA'),
        Rule(LinkExtractor(allow = 'Pages/cacDanhHieu.aspx'), callback = 'parse_DH'),
        Rule(LinkExtractor(allow = 'Pages/AnToanSKMT.aspx'), callback = 'parse_ATSKMT'),
        
        
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
    
    def parse_GT(self, response):
        title = self.processed_text(response.xpath('//div[@style="text-align: justify;"]//text()').getall()[1])
        content = '\n'.join(i for i in list(map(self.processed_text, response.xpath('//div[@style="text-align: justify;"]//text()').getall()[3:])) if i is not None)
        img = "https://www.vietsov.com.vn" + response.xpath('//div[contains(@style, "text-align: center;")]/img/@src').get()
        yield {
            'title': title,
            # 'image': img,
            'content': [content]
        }
    
        
    def parse_LSHT(self, response):
        title = self.processed_text(response.xpath('//h3[contains(@style, "color:red")]/text()').get())
        year_list = ["1981", "1984", "1985", "1986", "1987", "1995", "1997", "2001", "2005", "2009", "2010", "2012", "2015", "2019", "2021"]
        content = []
        for y in year_list:
            date_event = response.xpath(f'//li[contains(@id, {y})]/h1/text()').getall()
            event = list(map(self.processed_text, response.xpath(f'//li[contains(@id, {y})]/p/text()').getall()))
            img = "https://www.vietsov.com.vn" + response.xpath(f'//li[contains(@id, {y})]//@src').get()
            content.append({
                'dateEvent': date_event,
                'event': event,
                'image': img
            })
        final_content = []
        for c in content:
            for i in range(len(c['dateEvent'])):
                content_str = ': '.join([c['dateEvent'][i], c['event'][i]]) + '\n'
            final_content.append(content_str.strip())
        yield {
            'title': title,
            'content': ['\n'.join(final_content)]
        }
        
        
    
    def parse_CCTC(self, response):
        title = self.processed_text(response.xpath('//div[@style="text-align: center;"]//text()').getall()[1])
        content = self.processed_text(response.xpath('//h4/text()').getall()[0])
        img = []
        img.append(response.xpath('//div[contains(@class, "wrapper-text")]//@src').getall()[1])
        img.append(response.xpath('//div[contains(@class, "wrapper-text")]//@src').getall()[3])
        img.append(response.xpath('//div[contains(@class, "wrapper-text")]//@src').getall()[5])
        img.append(response.xpath('//div[contains(@class, "wrapper-text")]//@src').getall()[7])
        img = list(map(lambda x: "https://www.vietsov.com.vn"+x, img))
        yield {
            'title': title,
            # 'image': img,
            'content': [content]
        }
        
        
        
    def parse_LD(self, response):
        title = self.processed_text(response.xpath('//h3[contains(@style, "color:RED")]/text()').get())
        img = response.xpath('//img[contains(@class, "hideo")]/@src').getall()
        img = list(map( lambda x: "https://www.vietsov.com.vn" + x, img))
        member_name = [response.xpath('//p[contains(@class, "product-name")]//text()').getall()[i] for i in[1,5,9,13,17,21,25,33,37]] + [response.xpath('//h4[contains(@class, "product-name")]//text()').getall()[0]]
        member_name = list(map(self.processed_text, member_name))
        member_name = member_name[:7] + [None] + member_name[7:9] + [None] + [member_name[9]] + [None]  
        member_role = [response.xpath('//p[contains(@class, "product-name")]//text()').getall()[i] for i in[3,7,11,15,19,23,27,31,35,39,43]] + [response.xpath('//h4[contains(@class, "product-name")]//text()').getall()[1]] + [response.xpath('//p[contains(@class, "product-name")]//text()').getall()[47]]
        member_role = list(map(self.processed_text, member_role))
        member = []
        for i in range(len(member_name)):
            if member_name[i] is None: continue
            member_name_position = member_name[i] + ': ' + member_role[i] + '\n'
            member.append(member_name_position)
                # 'image': img[i],
            
        yield {
            'title': title,
            'content': ['\n'.join(member)]
        }
        
        
        
    def parse_LV(self, response):
        title = self.processed_text(response.xpath('//div[contains(@class, "ms-rtestate-field")]//text()').getall()[1])
        content = '\n'.join(i for i in list(map(self.processed_text,response.xpath('//div[contains(@class, "ms-rtestate-field")]//text()').getall()[7:])) if i is not None)
        img = "https://www.vietsov.com.vn" + response.xpath('//p[contains(@style, "text-align: center;")]//@src').get()
        yield {
            'title': title,
            # 'image': img,
            'content': [content]
        }
        
        
        
    def parse_TN(self, response):
        title = self.processed_text(response.xpath('//div[contains(@class, "ms-rtestate-field")]//text()').getall()[0])
        content = '\n'.join(i for i in list(map(self.processed_text, response.xpath('//div[contains(@class, "ms-rtestate-field")]//text()').getall()[2:])) if i is not None)
        img = "https://www.vietsov.com.vn" + response.xpath('//p[contains(@style, "text-align: center;")]//@src').get()
        yield {
            'title': title,
            # 'image': img,
            'content': [content]
        }
        
        
        
    def parse_TT(self, response):
        title = self.processed_text(response.xpath('//h3[contains(@style, "color:red")]/text()').get())
        number = response.xpath('//h6//text()').getall()[:4] + response.xpath('//h1//text()').getall() + response.xpath('//h6//text()').getall()[4:]
        content = response.xpath('//p1//text()').getall()[:4] + [" " + response.xpath('//p//text()').getall()[0]] + response.xpath('//p1//text()').getall()[4:]
        achievements = '\n'.join(i for i in list(map(lambda x, y: x + y, number, content)) if i is not None)
        yield {
            'title': title,
            'content': [achievements]
        }
        
        
    def parse_HA(self, response):
        title = self.processed_text(response.xpath('//h4/text()').get())
        img = list(map(lambda x: "https://www.vietsov.com.vn" + x,response.xpath('//div[contains(@class, "navigation")]//@src').getall()))
        yield {
            'title': title,
            # 'image': img
        }
        
        

    def parse_DH(self, response):
        title = self.processed_text(response.xpath('//h3//text()').get())
        img = list(map(lambda x: "https://www.vietsov.com.vn" + x, response.xpath('//img[contains(@class, "hideo")]/@src').getall()))
        medal = list(map(self.processed_text, [response.xpath('//h4[contains(@class, "product-name1")]//text()').getall()[i] for i in [0,1,2,4,5,6,8,9,10,11,12,13,14,15,16,18,19,20,21,22]]))
        medal = [medal[0] +" "+ medal[1]] + medal[2:]
        full_medal = list(map(lambda x, y: 
            # 'image': x,
            y + '\n'
        , img, medal))
        full_medal = ''.join(full_medal)
        yield {
            'title': title,
            'content': [full_medal]
        }
        
        
        
    def parse_ATSKMT(self, response):
        title = self.processed_text(response.xpath('//p[contains(@style, "text-align: center;")]//text()').getall()[1]+ " "+\
        response.xpath('//p[contains(@style, "text-align: center;")]//text()').getall()[4])
        img = list(map(lambda x: "https://www.vietsov.com.vn" + x,response.xpath('//p[contains(@style, "text-align: justify")]//@src').getall() + \
        response.xpath('//p[contains(@style, "text-align: left")]//@src').getall()))
        TEXT = list(map(self.processed_text, response.xpath('//p[contains(@style, "text-align: justify;")]//text()').getall()))
        policy = '\n'.join(i for i in TEXT[4:17] if i is not None)
        capability = '\n'.join(i for i in TEXT[20:35] if i is not None)
        model_of_ATSKMT_system = img[0]
        graph_of_ATSKMT_system = img[1]
        strength_of_ATSKMT_system = ' '.join(i for i in TEXT[54:74] if i is not None)
        achievement = '\n'.join(i for i in TEXT[76:] if i is not None)
        content = []
        content.append(f"Mô tả: {TEXT[1]}")
        content.append(f"Chính sách: {policy}")
        content.append(f"Năng lực: {capability}")
        content.append(f"Những tính năng nổi trội: {strength_of_ATSKMT_system}")
        content.append(f"Thành tựu: {achievement}")
        # content = {
        #     'description': TEXT[1],
        #     'policy': policy,
        #     'capability': capability,
        #     'modelOfATSKMTSystem': model_of_ATSKMT_system,
        #     'graphOfATSKMTSystem': graph_of_ATSKMT_system,
        #     'strengOfATSKMTSystem': strength_of_ATSKMT_system,
        #     'achievement': {
        #         'content': achievement,
        #         'image': img[2]
        #     }
            
        # }
        
        yield {
            'title': title,
            'content': content
        }
    