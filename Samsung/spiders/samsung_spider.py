# -*- coding: utf-8 -*-
from copy import deepcopy

from scrapy.spiders import CrawlSpider, Request
from Samsung.items import DeviceItem


class SamsungDeviceSpider(CrawlSpider):
    name = 'samsung_devices'
    start_urls = ['http://samsung-updates.com/']

    custom_settings = {
        'DOWNLOAD_DELAY': 1
    }

    def parse(self, response):
        for device in response.css('select[name="page"] option'):
            url = device.css('::attr(value)').extract_first('').strip('#')
            if not url:
                continue
            yield Request(response.urljoin(url), self.parse_device)

    def parse_device(self, response):
        for record in response.css('#flist > tr')[1:]:
            info = []
            for row in record.css('td'):
                value = row.css('a::text').extract_first() or row.css('::text').extract_first('Android').strip()
                info.append(value)

            device = DeviceItem(
                device_name=info[0],
                model=info[1],
                region=info[2],
                version=info[3],
                os=info[4],
                os_version=info[5],
                build_date=info[6]
            )
            # download_url = record.css('td a::attr(href)').extract()[-1]
            # meta = deepcopy(response.meta)
            # meta['item'] = device
            # yield Request(response.urljoin(download_url), self.parse_download_link, meta=meta)
            yield device

    def parse_download_link(self, response):
        ## File download code to added here

        print(response)
