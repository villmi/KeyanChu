import scrapy
import mysql.connector
import time
import random
import datetime
import traceback

"this is a spider for KeyanChu Mrs.Gao"


class ZhaobiaoSpider(scrapy.Spider):
    name = "KeyanChu"

    def start_requests(self):
        url = "http://keyan.njue.edu.cn/class.asp?ClassID=192&page=5"
        yield scrapy.request(url=url, callback=self.parse)
        pass

    def parse(self, response):
        table = response.xpath('/html/body/table[4]/tbody/tr/td[2]/table[4]/tbody/tr/td[2]/table[1]')
        print(table)
        pass
