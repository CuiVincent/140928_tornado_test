from tornado.log import app_log

__author__ = 'cuizhe01'
import os.path
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

class BaseHandler(tornado.web.RequestHandler):
    def write_error(self, status_code, **kwargs):
        print(kwargs)
        if status_code == 404:
            self.clear()
            self.render('404.html')
        elif status_code == 500:
            self.clear()
            self.render('500.html')
        else:
            super(BaseHandler, self).write_error(status_code, **kwargs)

class IndexHandler(BaseHandler):
    def get(self):
        raise AttributeError
        self.render('index.html')

class PageNotFoundHandler(BaseHandler):
    """Generates an error response with ``status_code`` for all requests."""
    def initialize(self, status_code):
        self.set_status(status_code)

    def prepare(self):
        raise  tornado.web.HTTPError(self._status_code)

    def check_xsrf_cookie(self):
        # POSTs to an ErrorHandler don't actually have side effects,
        # so we don't need to check the xsrf token.  This allows POSTs
        # to the wrong url to return a 404 instead of 403.
        pass


if __name__ == '__main__':
    tornado.web.ErrorHandler = PageNotFoundHandler
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[(r'/', IndexHandler)],
        template_path=os.path.join(os.path.dirname(__file__), "013_error_page1/templates")
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()