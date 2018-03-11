#coding=utf-8
#今日头条
import urllib2
import requests
import json

def get_url():
    #文章
    # url = 'https://www.toutiao.com/c/user/article/?page_type=1&user_id=67517973927&max_behot_time=0&count=20&as=A1D5FA5A552471F&cp=5AA57457F14F4E1&_signature=nBAc-BARxsEx-kJ5imBXKJwQHO'
    # global count
    # try:
    #     headers={
    #         'Host': 'www.toutiao.com',
    #         'accept': 'text/javascript, text/html,application/xml,text/xml,*/*',
    #         'accept-encoding': 'gzip,deflate,br',
    #         'User-Agent': 'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1; 125LA; .NET CLR 2.0.50727; .NET CLR 3.0.04506.648; .NET CLR 3.5.21022)',
    #         'Connection': 'Keep-Alive',
    #         'Content-Type': 'application/x-www-form-urlencoded',
    #         'Accept-Language': 'zh-cn',
    #         'cookie':'ga=GA1.2.1020650197.1520446957; tt_webid=6530269973758330376; tt_webid=6530269973758330376; WEATHER_CITY=%E5%8C%97%E4%BA%AC'
    #     }
    #     response = requests.get(url,headers = headers)
    #     print response.text
    #     Jdata = json.loads(response.text)
    #     # print Jdata
    #     news = Jdata['data']
    #
    #     for n in news:
    #         title = n['title']
    #         go_detail_count = n['go_detail_count']
    #         comments_count = n['comments_count']
    #         detail_play_effective_count = n['detail_play_effective_count']
    #         print title, '|', go_detail_count, '|', comments_count, '|', detail_play_effective_count
    #
    # except urllib2.URLError, e:
    #     print e.reason

        # 微头条
        # url = 'https://www.toutiao.com/c/ugc/content/list/67517973927/?t=1520780874700'
        # global count
        # try:
        #     headers={
        #         'Host': 'www.toutiao.com',
        #         'accept': 'text/javascript, text/html,application/xml,text/xml,*/*',
        #         'accept-encoding': 'gzip,deflate,br',
        #         'User-Agent': 'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1; 125LA; .NET CLR 2.0.50727; .NET CLR 3.0.04506.648; .NET CLR 3.5.21022)',
        #         'Connection': 'Keep-Alive',
        #         'Content-Type': 'application/x-www-form-urlencoded',
        #         'Accept-Language': 'zh-cn',
        #         'cookie':'ga=GA1.2.1020650197.1520446957; tt_webid=6530269973758330376; tt_webid=6530269973758330376; WEATHER_CITY=%E5%8C%97%E4%BA%AC'
        #     }
        #     response = requests.get(url,headers = headers)
        #     print response.text
        #     Jdata = json.loads(response.text)
        #     # print Jdata
        #     news = Jdata['data']
        #
        #     for n in news['list']:
        #         forward_num = n['forward_num']
        #         read_count = n['read_count']
        #         rich_content = n['rich_content']
        #         comment_count = n['comment_count']
        #         open_url = n['open_url']
        #         content = n['content']
        #         print read_count, '|', comment_count, '|', open_url
        #
        # except urllib2.URLError, e:
        #     print e.reason

        # 视频
        url = 'https://www.toutiao.com/c/user/article/?page_type=0&user_id=50656620572&max_behot_time=0&count=20&as=A1451A9AC504959&cp=5AA574D9F589EE1&_signature=zetorxAdl1dgATYu6mLtA83raL'
        global count
        try:
            headers={
                'Host': 'www.toutiao.com',
                'accept': 'text/javascript, text/html,application/xml,text/xml,*/*',
                'accept-encoding': 'gzip,deflate,br',
                'User-Agent': 'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1; 125LA; .NET CLR 2.0.50727; .NET CLR 3.0.04506.648; .NET CLR 3.5.21022)',
                'Connection': 'Keep-Alive',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Accept-Language': 'zh-cn',
                'cookie':'ga=GA1.2.1020650197.1520446957; tt_webid=6530269973758330376; tt_webid=6530269973758330376; WEATHER_CITY=%E5%8C%97%E4%BA%AC'
            }
            response = requests.get(url,headers = headers)
            print response.text
            Jdata = json.loads(response.text)
            # print Jdata
            news = Jdata['data']

            for n in news:
                title = n['title']
                go_detail_count = n['go_detail_count']
                comments_count = n['comments_count']
                media_url = n['media_url']
                video_duration_str = n['video_duration_str']
                print title, '|', go_detail_count, '|', comments_count, '|', media_url, '|', video_duration_str

        except urllib2.URLError, e:
            print e.reason


if __name__ == '__main__':
    count = 0
    get_url()