# encoding: utf-8
__author__ = 'fanzhikang'
__date__ = '2018/10/16 14:02'

import requests

class crawlscore:
    def __init__(self, url):
        self.url = url

    def getscore(self):
        datas = {
            'username': 'U201617042',
            'password': 'afzk2014',
            'code' : 'code',
            'lt' : 'LT-NeusoftAlwaysValidTicket',
            'execution' : 'e1s1',
            '_eventId' : 'submit'
        }
        headers = {
            "Referer" : "https://pass.hust.edu.cn/cas/login?service=http%3A%2F%2Fone.hust.edu.cn%2Fdcp%2Findex.jsp",
            "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36",
            "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Language" : "zh-CN,zh;q=0.9"
        }
        session = requests.session()
        response = session.post(self.url, headers=headers, data=datas)
        return (response.url)

if __name__ == "__main__":
    url = 'https://pass.hust.edu.cn/cas/login?service=http%3A%2F%2Fhubs.hust.edu.cn%2Fhustpass.action'
    crawl = crawlscore(url)
    print(crawl.getscore())