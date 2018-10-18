# encoding: utf-8
__author__ = 'fanzhikang'
__date__ = '2018/10/15 21:08'

class transCookie:
    def __init__(self, cookie):
        self.cookie = cookie

    def stringToDict(self):

        itemDict = {}
        items = self.cookie.split(';')
        for item in items:
            key = item.split('=')[0].strip()
            value = item.split('=')[1]
            itemDict[key] = value
        return itemDict

if __name__ == "__main__":
    cookie = "TY_SESSION_ID=7f28ae2e-2ab9-47cf-8af7-b449cfef304d; admin_show_testqm_new=customStr%3Dtype+classification+content+difficult+creater+createTime+sender%26%26customPageCount%3D10%26%26; gr_user_id=b7c46ae1-4a59-401a-b860-e17fb2bbf9f2; JSESSIONID=aaa-L6aAkII6Bc7jNUBzw; kwd=%E6%9C%AA%E7%9F%A5; source=5FG4jd63b9SGDn92HERnf0ERGe83nr74bf84nf; TY_SESSION_ID=0925e0cc-fa2e-4812-962b-55c65c002cca; 87d10bc8158a4ed0a2206a6f0bdd2a5c_gr_last_sent_cs1=3383449; Hm_lvt_0502cfa1e2a3555b1fd1668ef723940d=1539238279; grwng_uid=f8981028-cf4b-40c9-b42d-1001a72221ef; nb-referrer-hostname=admin.kaoshixing.com; nb-start-page-url=https%3A%2F%2Fadmin.kaoshixing.com%2F; Hm_lpvt_0502cfa1e2a3555b1fd1668ef723940d=1539238293; 87d10bc8158a4ed0a2206a6f0bdd2a5c_gr_session_id=a60fb47c-da29-4437-a9b5-71fe594ce204; 87d10bc8158a4ed0a2206a6f0bdd2a5c_gr_last_sent_sid_with_cs1=a60fb47c-da29-4437-a9b5-71fe594ce204; 87d10bc8158a4ed0a2206a6f0bdd2a5c_gr_session_id_a60fb47c-da29-4437-a9b5-71fe594ce204=true; sessionId=aaadHkGVFzefbcyWpOyzw; 87d10bc8158a4ed0a2206a6f0bdd2a5c_gr_cs1=3383449"
    trans = transCookie(cookie)
    print(trans.stringToDict())