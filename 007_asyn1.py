__author__ = 'cuizhe01'

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.httpclient

import urllib
import json
import datetime
import time

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        query = self.get_argument('a')
        sleeping = self.get_argument('t')
        client = tornado.httpclient.HTTPClient()
        response = client.fetch("http://gc.ditu.aliyun.com/geocoding?" + \
                urllib.parse.urlencode({"a": query, "ie": "utf-8", "inputT": 1103}))
        html = response.body
        html = html.decode('utf-8')
        print(sleeping)
        time.sleep(float(sleeping))
        # body = json.loads(html)
        # result_count = len(body['results'])
        # now = datetime.datetime.utcnow()
        # raw_oldest_tweet_at = body['results'][-1]['created_at']
        # oldest_tweet_at = datetime.datetime.strptime(raw_oldest_tweet_at,
        #         "%a, %d %b %Y %H:%M:%S +0000")
        # seconds_diff = time.mktime(now.timetuple()) - \
        #         time.mktime(oldest_tweet_at.timetuple())
        # tweets_per_second = float(result_count) / seconds_diff
        self.write("""
<div style="text-align: center">
    <div style="font-size: 72px">%s</div>
    <div style="font-size: 44px">%s</div>
    <div style="font-size: 24px">同步版本</div>
</div>""" % (query, html))

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r"/", IndexHandler)])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()