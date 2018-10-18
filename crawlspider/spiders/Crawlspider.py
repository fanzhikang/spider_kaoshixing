# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule, Spider


class CrawlspiderSpider(Spider):
    name = 'Crawlspider'
    allowed_domains = ['kaoshixing.com']
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36"
    }

    # start_urls = ['https://www.kaoshixing.com/']
    cookie = {'TY_SESSION_ID': '0925e0cc-fa2e-4812-962b-55c65c002cca',
     'admin_show_testqm_new': 'customStr%3Dtype+classification+content+difficult+creater+createTime+sender%26%26customPageCount%3D10%26%26',
     'gr_user_id': 'b7c46ae1-4a59-401a-b860-e17fb2bbf9f2', 'JSESSIONID': 'aaa-L6aAkII6Bc7jNUBzw',
     'kwd': '%E6%9C%AA%E7%9F%A5', 'source': '5FG4jd63b9SGDn92HERnf0ERGe83nr74bf84nf',
     '87d10bc8158a4ed0a2206a6f0bdd2a5c_gr_last_sent_cs1': '3383449',
     'Hm_lvt_0502cfa1e2a3555b1fd1668ef723940d': '1539238279', 'grwng_uid': 'f8981028-cf4b-40c9-b42d-1001a72221ef',
     'nb-referrer-hostname': 'admin.kaoshixing.com', 'nb-start-page-url': 'https%3A%2F%2Fadmin.kaoshixing.com%2F',
     'Hm_lpvt_0502cfa1e2a3555b1fd1668ef723940d': '1539238293',
     '87d10bc8158a4ed0a2206a6f0bdd2a5c_gr_session_id': 'a60fb47c-da29-4437-a9b5-71fe594ce204',
     '87d10bc8158a4ed0a2206a6f0bdd2a5c_gr_last_sent_sid_with_cs1': 'a60fb47c-da29-4437-a9b5-71fe594ce204',
     '87d10bc8158a4ed0a2206a6f0bdd2a5c_gr_session_id_a60fb47c-da29-4437-a9b5-71fe594ce204': 'true',
     'sessionId': 'aaadHkGVFzefbcyWpOyzw', '87d10bc8158a4ed0a2206a6f0bdd2a5c_gr_cs1': '3383449'}

    def start_requests(self):
        url = 'https://admin.kaoshixing.com/admin/showtestqm_new'
        # data = {
        #     'userNameInput': 'CECC511',
        #     'password': 'cecc511'
        # }
        # url = 'https://www.kaoshixing.com/account/login/5769'
        # return [scrapy.Request(url, meta={'cookiejar': 1 },headers=self.headers, callback=self.post_login)]
        return [scrapy.FormRequest(url, cookies=self.cookie, callback=self.parse_page)]
    # def post_login(self, response):
    #     return [scrapy.FormRequest.from_response(response,
    #                                              headers = self.headers,
    #                                              formdata={
    #                                                  "userName": "CECC511 @ cecctm.com",
    #                                                  "userNameInput" : "CECC511",
    #                                                  "newCompanyId" : "5769",
    #                                                  "password" : "5c3a0d081b1bf8b462429e45f1c7d579",
    #                                                  "remember" : "false"
    #                                              },
    #                                              meta = {'cookiejar':response.meta['cookiejar']},
    #                                              callback = self.after_login,
    #                                              dont_click=True)]

    # def after_login(self, response):
    #     return scrapy.Request(
    #         "https://admin.kaoshixing.com/account/admin/index",
    #         meta={'cookiejar': response.meta['cookiejar']},
    #         callback=self.parse_page)

    def parse_page(self, response):
        print(response.body.decode('utf-8'))
        print("===" + response.url)


        # ths = response.css('#grid-data thead tr th')#grid-data > tbody > tr:nth-child(1)
        # title = response.xpath('//*[@id="grid-data"]/tbody/tr[1]/td[4]')
        # for th in ths[1:]:
        #     title = th.css('a span:nth-child(1)::text').extract_first()
        #     print("========="+str(title))
        # url2 = 'https://admin.kaoshixing.com/account/admin/index'
        # request = scrapy.Request(url2, callback=self.parse_profile)
        # yield request

    # def parse_profile(self, response):
    #     with open('kaoshi.html', 'w', encoding='utf-8') as f:
    #         f.write(response.text)
    #         f.close()
