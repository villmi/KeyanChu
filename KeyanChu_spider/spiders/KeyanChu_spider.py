import scrapy
import time


"this is a spider for KeyanChu Mrs.Gao"


class ZhaobiaoSpider(scrapy.Spider):
    name = "KeyanChu"

    def start_requests(self):
        url = "http://keyan.njue.edu.cn/class.asp?ClassID=192&page=17"
        yield scrapy.Request(url=url, callback=self.parse,
                             meta={'page': 17})

    def parse(self, response):
        td1s = response.xpath('//a[@class = "a03"]')
        td1s = td1s[4:]
        for td in td1s:
            url = td.xpath("@href").extract()[0]
            url = "http://keyan.njue.edu.cn/"+url
            yield scrapy.Request(url=url, callback=self.parseUrl, meta={'id': url[-4:]})
        #page = int(response.meta['page'])
        #if page < 16:
            #page += 1
            #url = "http://keyan.njue.edu.cn/class.asp?ClassID=192&page=%d" % page
            #print("%d is over" % (int(page)-1))
            #time.sleep(3)
            #yield scrapy.Request(url=url, callback=self.parse, meta={'page': page})

    def parseUrl(self, response):
        tds = response.xpath('//td[@class = "td2"]')
        for td in tds:
            td = td.xpath("string(.)").extract()[0]
            td = td.replace('\r', "").replace("\n", "").replace("\t", "").replace("\xa0", "")
            info = open("gao5.txt", "a")
            info.write(td)
            info.write("@")
            aa = response.meta['id']
            info.write(aa)
            info.write("\n")
            info.close()
